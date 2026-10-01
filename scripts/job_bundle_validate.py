#!/usr/bin/env python3
"""JOB_BUNDLE validator before spawning Tasks."""
import json
import re
import sys

REQUIRED = [
    "job_post", "title", "budget_fixed", "primary_deliverable",
    "primary_terms", "prework_slice",
]

SCREENING_HINTS = re.compile(
    r"(start your proposal with|begin your (cover )?letter with|include the word|"
    r"answer the following|to be considered|hidden keyword|must mention)",
    re.I,
)


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

    post = data.get("job_post", "")
    scr = data.get("screening") or {}
    if SCREENING_HINTS.search(post) or scr.get("required"):
        if not scr.get("must_answer_in_letter") and not scr.get("hidden_keywords") and not scr.get("start_with_prefix"):
            print("FAIL screening job but screening.must_answer_in_letter / hidden_keywords / start_with_prefix empty")
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
