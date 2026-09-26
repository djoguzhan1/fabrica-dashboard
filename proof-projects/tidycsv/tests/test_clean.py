import pandas as pd
import pytest

from tidycsv.clean import clean, normalize_header, normalize_headers, parse_dates, parse_number


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("  Order ID ", "order_id"),
        ("Amount ($)", "amount"),
        ("customer_email", "customer_email"),
        ("First-Name", "first_name"),
        ("", "column"),
    ],
)
def test_normalize_header(raw, expected):
    assert normalize_header(raw) == expected


def test_duplicate_headers_get_suffixes():
    assert normalize_headers(["Name", "name", "NAME", "Unnamed: 3"]) == ["name", "name_2", "name_3", "column"]


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("$1,234.50", 1234.5),
        ("(45.00)", -45.0),
        (" 89 ", 89.0),
        ("12%", 12.0),
        ("-7", -7.0),
        ("€ 2.500,00", 2500.0),
        ("1.234,5", 1234.5),
        ("1,5", 1.5),
        ("abc", None),
        ("", None),
        (None, None),
        (3, 3.0),
    ],
)
def test_parse_number(raw, expected):
    assert parse_number(raw) == expected


def test_parse_dates_unifies_formats():
    series = pd.Series(["2026-03-04", "03/04/2026", "4 Mar 2026", "March 4, 2026", "not a date"])
    parsed, formats_used = parse_dates(series)
    assert parsed.notna().tolist() == [True, True, True, True, False]
    assert parsed.dropna().nunique() == 1
    assert formats_used == 4


def test_parse_dates_dayfirst():
    series = pd.Series(["04/03/2026"])
    parsed, _ = parse_dates(series, dayfirst=True)
    assert parsed.iloc[0] == pd.Timestamp("2026-03-04")


def messy_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            " Order ID": ["1", "2", "2", "3", ""],
            "Status": ["shipped", "Shipped ", "Shipped ", "SHIPPED", ""],
            "Amount ($)": ["$10.00", "20", "20", "(5.00)", ""],
            "When": ["2026-01-02", "01/03/2026", "01/03/2026", "4 Jan 2026", ""],
            "Notes": ["n/a", "", "", "call first ", ""],
            "": ["", "", "", "", ""],
        }
    )


def test_clean_end_to_end():
    result = clean(messy_frame())
    df = result.frame

    assert list(df.columns) == ["order_id", "status", "amount", "when", "notes"]
    assert result.rows_in == 5
    assert result.rows_out == 3  # one empty row, one exact duplicate
    assert result.column_types == {
        "order_id": "text",
        "status": "text",
        "amount": "number",
        "when": "date",
        "notes": "text",
    }
    assert df["status"].tolist() == ["Shipped", "Shipped", "Shipped"]
    assert df["amount"].tolist() == [10.0, 20.0, -5.0]
    assert df["when"].dt.strftime("%Y-%m-%d").tolist() == ["2026-01-02", "2026-01-03", "2026-01-04"]
    assert df["notes"].iloc[0] is None
    assert df["notes"].iloc[2] == "call first"

    actions = {c.action for c in result.changes}
    assert {"Headers normalised", "Empty rows removed", "Empty columns removed", "Duplicate rows removed"} <= actions


def test_clean_can_keep_duplicates_and_case():
    result = clean(messy_frame(), dedupe=False, unify_case=False)
    assert result.rows_out == 4
    assert sorted(result.frame["status"].tolist()) == ["SHIPPED", "Shipped", "Shipped", "shipped"]


def test_identifier_columns_stay_text():
    frame = pd.DataFrame({"zip": ["02134", "10001"], "amount": ["1", "2"]})
    result = clean(frame)
    assert result.column_types == {"zip": "text", "amount": "number"}
    assert result.frame["zip"].tolist() == ["02134", "10001"]
