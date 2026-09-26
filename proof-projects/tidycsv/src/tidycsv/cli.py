"""Command line entry point: tidycsv input.csv -o report.xlsx"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

from . import __version__
from .clean import clean, normalize_header
from .report import write_report


def read_csv(path: Path, encoding: str | None, delimiter: str | None) -> pd.DataFrame:
    """Read with the given encoding, falling back to the two we see most often."""
    encodings = [encoding] if encoding else ["utf-8-sig", "cp1252", "latin-1"]
    last_error: Exception | None = None
    for enc in encodings:
        try:
            return pd.read_csv(
                path,
                dtype=str,
                keep_default_na=False,
                encoding=enc,
                sep=delimiter,
                engine="python" if delimiter is None else "c",
                skip_blank_lines=False,
            )
        except UnicodeDecodeError as exc:
            last_error = exc
    raise SystemExit(f"Could not decode {path.name}: {last_error}. Try --encoding.")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="tidycsv",
        description="Clean a messy CSV and write an Excel report (Data, Summary, Changes).",
    )
    p.add_argument("input", type=Path, help="CSV file to clean")
    p.add_argument("-o", "--output", type=Path, help="Excel file to write (default: <input>_report.xlsx)")
    p.add_argument("--group-by", metavar="COLUMN", help="category column for the summary table and chart")
    p.add_argument("--sum", dest="sum_column", metavar="COLUMN", help="numeric column to total per category")
    p.add_argument("--dayfirst", action="store_true", help="read ambiguous dates as day/month/year")
    p.add_argument("--keep-duplicates", action="store_true", help="do not remove exact duplicate rows")
    p.add_argument("--keep-case", action="store_true", help="do not unify 'Shipped' / 'shipped' / 'SHIPPED'")
    p.add_argument("--encoding", help="input encoding (default: try utf-8, cp1252, latin-1)")
    p.add_argument("--delimiter", help="field delimiter (default: detect)")
    p.add_argument("--version", action="version", version=f"tidycsv {__version__}")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.input.exists():
        print(f"tidycsv: {args.input} does not exist", file=sys.stderr)
        return 2

    frame = read_csv(args.input, args.encoding, args.delimiter)
    result = clean(
        frame,
        dedupe=not args.keep_duplicates,
        unify_case=not args.keep_case,
        dayfirst=args.dayfirst,
    )

    # Column names in the report are normalised, so accept either spelling.
    group_by = normalize_header(args.group_by) if args.group_by else None
    sum_column = normalize_header(args.sum_column) if args.sum_column else None
    for name, label in ((group_by, "--group-by"), (sum_column, "--sum")):
        if name and name not in result.frame.columns:
            columns = ", ".join(result.frame.columns)
            print(f"tidycsv: {label} column '{name}' not found. Columns: {columns}", file=sys.stderr)
            return 2

    output = args.output or args.input.with_name(f"{args.input.stem}_report.xlsx")
    write_report(result, output, source_name=args.input.name, group_by=group_by, sum_column=sum_column)

    ncols = len(result.frame.columns)
    print(f"{args.input.name}: {result.rows_in} rows in, {result.rows_out} rows out, {ncols} columns")
    for change in result.changes:
        where = f"{change.column}: " if change.column else ""
        print(f"  - {where}{change.action.lower()} ({change.count})")
    types = ", ".join(f"{c}={t}" for c, t in result.column_types.items())
    print(f"  types: {types}")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
