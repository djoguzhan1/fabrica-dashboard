#!/usr/bin/env python3
"""Minimal JOB_BUNDLE validator before spawning Tasks."""
import json
import sys

REQUIRED = [
    "job_post", "title", "budget_fixed", "primary_deliverable",
    "primary_terms", "prework_slice",
]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    data = json.load(sys.stdin if not path else open(path, encoding="utf-8"))
    missing = [k for k in REQUIRED if not data.get(k)]
    if missing:
        print("FAIL missing:", ", ".join(missing))
        sys.exit(1)
    if not data.get("primary_terms"):
        print("FAIL primary_terms empty")
        sys.exit(1)
    ban = data.get("ban_in_card") or []
    prim = " ".join(data.get("primary_terms", [])).lower()
    for b in ban:
        if b.lower() in prim:
            print(f"WARN ban_in_card overlaps primary: {b}")
    print("PASS job_bundle")
    sys.exit(0)


if __name__ == "__main__":
    main()
