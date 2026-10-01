#!/usr/bin/env python3
"""Demo slice: dedupe CSV by email column."""
import csv
import sys

col = sys.argv[1] if len(sys.argv) > 1 else "email"
seen = set()
w = csv.writer(sys.stdout)
r = csv.DictReader(sys.stdin)
if r.fieldnames:
    w.writerow(r.fieldnames)
for row in r:
    key = row.get(col, "").strip().lower()
    if key and key in seen:
        continue
    if key:
        seen.add(key)
    w.writerow([row.get(f, "") for f in r.fieldnames])
