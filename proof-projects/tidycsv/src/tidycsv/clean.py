"""Cleaning steps for messy CSV data.

Everything here works on a pandas DataFrame and records what it changed,
so the report can show the client exactly what happened to their data.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import pandas as pd

# Values that mean "no value" in the wild.
NA_TOKENS = {"", "-", "--", "n/a", "na", "n.a.", "null", "none", "nan", "#n/a", "?"}

# Formats tried in order when a column looks like dates. Day-first formats
# come after month-first because US clients are the common case; pass
# dayfirst=True to flip that.
DATE_FORMATS_MONTH_FIRST = (
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%m/%d/%y",
    "%d %b %Y",
    "%d %B %Y",
    "%b %d, %Y",
    "%B %d, %Y",
    "%Y/%m/%d",
    "%Y-%m-%d %H:%M:%S",
    "%m/%d/%Y %H:%M",
)
DATE_FORMATS_DAY_FIRST = (
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%d/%m/%y",
    "%d.%m.%Y",
    "%d %b %Y",
    "%d %B %Y",
    "%Y/%m/%d",
)


def _is_text(series: pd.Series) -> bool:
    """True for object and string dtypes (pandas 2 and 3)."""
    return pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series)


_CURRENCY_SYMBOL_RE = re.compile(r"[$€£₺¥]")
_PAREN_NEG_RE = re.compile(r"^\((.*)\)$")
_NUMBER_RE = re.compile(r"^[+-]?(\d+(\.\d*)?|\.\d+)$")


@dataclass
class Change:
    """One thing the cleaner did, in plain words."""

    column: str | None
    action: str
    count: int
    detail: str = ""

    def as_row(self) -> tuple[str, str, int, str]:
        return (self.column or "(table)", self.action, self.count, self.detail)


@dataclass
class CleanResult:
    frame: pd.DataFrame
    changes: list[Change] = field(default_factory=list)
    rows_in: int = 0
    rows_out: int = 0
    column_types: dict[str, str] = field(default_factory=dict)


def normalize_header(name: object) -> str:
    """'  Order ID ' -> 'order_id'; 'Amount ($)' -> 'amount'."""
    text = str(name).strip().lower()
    text = re.sub(r"[^\w]+", "_", text, flags=re.UNICODE)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "column"


def normalize_headers(columns: list[object]) -> list[str]:
    seen: dict[str, int] = {}
    out: list[str] = []
    for col in columns:
        base = normalize_header(col)
        if base.startswith("unnamed_"):
            base = "column"
        if base in seen:
            seen[base] += 1
            out.append(f"{base}_{seen[base]}")
        else:
            seen[base] = 1
            out.append(base)
    return out


def parse_number(value: object) -> float | None:
    """Parse '$1,234.50', '(45.00)', ' 89 ', '12%' into a float. None if it isn't one."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text:
        return None
    negative = False
    m = _PAREN_NEG_RE.match(text)
    if m:
        negative = True
        text = m.group(1)
    if text.endswith("%"):
        text = text[:-1]
    text = _CURRENCY_SYMBOL_RE.sub("", text).replace(" ", "")
    # "2.500,00" (European) vs "2,500.00" (US): the last separator is the decimal one.
    if "," in text and text.rfind(",") > text.rfind("."):
        text = text.replace(".", "").replace(",", ".")
    else:
        text = text.replace(",", "")
    if text.startswith("-"):
        negative = not negative
        text = text[1:]
    if not _NUMBER_RE.match(text):
        return None
    number = float(text)
    return -number if negative else number


def parse_dates(series: pd.Series, dayfirst: bool = False) -> tuple[pd.Series, int]:
    """Try each known format; return parsed datetimes and how many formats matched."""
    formats = DATE_FORMATS_DAY_FIRST if dayfirst else DATE_FORMATS_MONTH_FIRST
    text = series.astype("string").str.strip()
    result = pd.Series(pd.NaT, index=series.index, dtype="datetime64[ns]")
    formats_used = 0
    for fmt in formats:
        pending = result.isna() & text.notna()
        if not pending.any():
            break
        parsed = pd.to_datetime(text[pending], format=fmt, errors="coerce")
        if parsed.notna().any():
            formats_used += 1
            result.loc[pending] = parsed
    return result, formats_used


_IDENTIFIER_HINTS = ("id", "zip", "postcode", "postal_code", "phone", "sku", "code")


def _looks_like_identifier(column: str) -> bool:
    """IDs, ZIP codes and phone numbers must stay text; leading zeros matter."""
    return column == "id" or any(column.endswith(f"_{h}") or column == h for h in _IDENTIFIER_HINTS)


def _preferred_spelling(counts: pd.Series) -> str:
    """Most common spelling wins; 'Shipped' beats 'SHIPPED' and 'shipped' on a tie or near-tie."""
    ranked = sorted(
        counts.items(),
        key=lambda item: (item[1], item[0][:1].isupper() and not item[0].isupper()),
        reverse=True,
    )
    top_spelling, top_count = ranked[0]
    for spelling, count in ranked:
        if count >= top_count * 0.5 and spelling[:1].isupper() and not spelling.isupper():
            return spelling
    # Only ALL CAPS / lower-case variants seen: capitalise single words ("refunded" -> "Refunded").
    if " " not in top_spelling and top_spelling.isalpha():
        return top_spelling.capitalize()
    return top_spelling


def _share_parsed(parsed: pd.Series, original: pd.Series) -> float:
    non_null = original.notna().sum()
    return 0.0 if non_null == 0 else parsed.notna().sum() / non_null


def clean(
    frame: pd.DataFrame,
    *,
    dedupe: bool = True,
    unify_case: bool = True,
    dayfirst: bool = False,
    type_threshold: float = 0.9,
) -> CleanResult:
    """Run every cleaning step and return the cleaned frame plus a change log."""
    result = CleanResult(frame=frame, rows_in=len(frame))
    changes = result.changes
    df = frame.copy()

    # 1. Headers
    old_headers = list(df.columns)
    new_headers = normalize_headers(old_headers)
    renamed = sum(1 for a, b in zip(old_headers, new_headers, strict=True) if str(a) != b)
    df.columns = new_headers
    if renamed:
        changes.append(Change(None, "Headers normalised", renamed, "snake_case, trimmed, de-duplicated"))

    # 2. Whitespace and NA tokens in text columns
    stripped = 0
    na_filled = 0
    for col in df.columns:
        if not _is_text(df[col]):
            continue
        as_text = df[col].astype("string")
        trimmed = as_text.str.strip()
        stripped += int((as_text != trimmed).fillna(False).sum())
        lowered = trimmed.str.lower()
        is_na_token = lowered.isin(NA_TOKENS).fillna(False)
        na_filled += int((is_na_token & (lowered != "")).fillna(False).sum())
        trimmed = trimmed.mask(is_na_token, pd.NA)
        df[col] = trimmed.astype(object).where(trimmed.notna(), None)
    if stripped:
        changes.append(Change(None, "Whitespace trimmed", stripped, "leading/trailing spaces removed from cells"))
    if na_filled:
        changes.append(Change(None, "Placeholder values blanked", na_filled, "N/A, null, '-', '?' treated as empty"))

    # 3. Empty rows and columns
    before = len(df)
    df = df.dropna(how="all")
    if len(df) != before:
        changes.append(Change(None, "Empty rows removed", before - len(df)))
    empty_cols = [c for c in df.columns if df[c].isna().all()]
    if empty_cols:
        df = df.drop(columns=empty_cols)
        changes.append(Change(None, "Empty columns removed", len(empty_cols), ", ".join(empty_cols)))

    # 4. Types
    for col in df.columns:
        series = df[col]
        if not _is_text(series):
            result.column_types[col] = "number" if pd.api.types.is_numeric_dtype(series) else str(series.dtype)
            continue
        if _looks_like_identifier(col):
            result.column_types[col] = "text"
            continue
        numbers = series.map(parse_number)
        if _share_parsed(numbers, series) >= type_threshold:
            plain = series.astype("string").str.strip().str.match(_NUMBER_RE.pattern).fillna(False)
            converted = int((numbers.notna() & ~plain).sum())
            df[col] = numbers.astype(float)
            result.column_types[col] = "number"
            if converted:
                detail = "currency symbols, thousands separators, (negatives) handled"
                changes.append(Change(col, "Parsed as numbers", converted, detail))
            continue
        dates, formats_used = parse_dates(series, dayfirst=dayfirst)
        if _share_parsed(dates, series) >= type_threshold:
            df[col] = dates
            result.column_types[col] = "date"
            detail = f"{formats_used} input format(s) unified"
            changes.append(Change(col, "Parsed as dates", int(dates.notna().sum()), detail))
            continue
        result.column_types[col] = "text"

    # 5. Case variants in low-cardinality text columns ("shipped" / "Shipped" / "SHIPPED")
    if unify_case:
        for col, kind in result.column_types.items():
            if kind != "text":
                continue
            series = df[col].dropna().astype(str)
            if series.empty:
                continue
            lowered = series.str.lower()
            if lowered.nunique() > 25 or lowered.nunique() == series.nunique():
                continue
            canonical: dict[str, str] = {}
            for key, group in series.groupby(lowered):
                canonical[key] = _preferred_spelling(group.value_counts())
            mapped = lowered.map(canonical)
            fixed = int((mapped != series).sum())
            if fixed:
                df.loc[series.index, col] = mapped
                detail = "kept the most common spelling, preferring Title Case"
                changes.append(Change(col, "Case variants unified", fixed, detail))

    # 6. Duplicates
    if dedupe:
        before = len(df)
        df = df.drop_duplicates()
        if len(df) != before:
            changes.append(Change(None, "Duplicate rows removed", before - len(df), "exact duplicates only"))

    df = df.reset_index(drop=True)
    result.frame = df
    result.rows_out = len(df)
    return result
