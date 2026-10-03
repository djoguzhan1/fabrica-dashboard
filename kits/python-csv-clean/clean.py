#!/usr/bin/env python3
"""Dedupe CSV rows by key columns; strip whitespace on all fields."""
import argparse
import csv
from pathlib import Path

KEY_COLUMNS = ("email",)  # Builder adapts per job


def normalize_row(row: dict[str, str]) -> dict[str, str]:
    return {k: (v or "").strip() for k, v in row.items()}


def dedupe(rows: list[dict[str, str]], keys: tuple[str, ...]) -> list[dict[str, str]]:
    seen: set[tuple[str, ...]] = set()
    out: list[dict[str, str]] = []
    for row in rows:
        norm = normalize_row(row)
        key = tuple(norm.get(k, "").lower() for k in keys)
        if key in seen:
            continue
        seen.add(key)
        out.append(norm)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    ap.add_argument("-k", "--keys", default=",".join(KEY_COLUMNS))
    args = ap.parse_args()
    keys = tuple(k.strip() for k in args.keys.split(",") if k.strip())
    with args.input.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    cleaned = dedupe(rows, keys)
    if not cleaned:
        args.output.write_text("", encoding="utf-8")
        return
    with args.output.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cleaned[0].keys())
        w.writeheader()
        w.writerows(cleaned)
    print(f"{len(rows)} -> {len(cleaned)} rows")


if __name__ == "__main__":
    main()
