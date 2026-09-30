#!/usr/bin/env python3
"""Pre-send check for client chat replies (after the proposal).

Usage:
  python3 scripts/reply_lint.py reply.txt [--stage first|interview|objection|offer|scope] [--must "a,b"]

Exit 1 on FAIL. Stage changes the word limit and required elements.
"""
import argparse
import re
import sys

LIMITS = {"first": 130, "interview": 180, "objection": 110, "offer": 140, "scope": 120}

BANNED = [
    (r"\b(whatsapp|telegram|skype|discord|gmail|@gmail|phone number|my number|call me at)\b", "off-platform contact"),
    (r"\b(pay (me )?(outside|directly)|paypal|wise\.com|bank transfer|crypto)\b", "off-platform payment"),
    (r"\b(per hour|hourly rate|track(ed)? hours|time tracker|/hr)\b", "hourly/time tracking"),
    (r"\b(for free|free of charge|no charge|unpaid|free sample|free test)\b", "free work"),
    (r"\b(hop on a call|jump on a call|quick call|zoom|google meet|video call|phone call)\b", "call offer"),
    (r"\b(5[- ]star|five[- ]star|leave (me )?a review for)\b", "review solicitation"),
    (r"\b(guarantee(d)? (#?1|first page|ranking|results))\b", "result guarantee"),
    (r"\b(as an ai|language model|i'd be happy to|i hope this (message|email) finds you)\b", "AI phrasing"),
]

REQUIRED = {
    "offer": [(r"\$\s?\d", "price"), (r"\b(milestone|fixed)\b", "milestone/fixed wording"),
              (r"\b(by|within|today|tomorrow|\d+\s?(h|hours|days?))\b", "delivery time")],
    "first": [(r"\b(milestone|fixed|\$\s?\d)\b", "next-step offer (milestone or price)")],
    "scope": [(r"\b(milestone|separate|second|additional|\$\s?\d)\b", "extra scope priced separately")],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--stage", choices=sorted(LIMITS), default="first")
    ap.add_argument("--must", default="", help="comma-separated terms from the client's message")
    a = ap.parse_args()

    text = open(a.path, encoding="utf-8").read().strip()
    low = text.lower()
    fails, warns = [], []

    words = len(text.split())
    if words > LIMITS[a.stage]:
        fails.append(f"{words} words > {LIMITS[a.stage]} for stage '{a.stage}'")
    for pat, why in BANNED:
        if re.search(pat, low):
            fails.append(f"banned: {why}")
    for pat, why in REQUIRED.get(a.stage, []):
        if not re.search(pat, low):
            fails.append(f"missing: {why}")
    q = text.count("?")
    if q > 2:
        fails.append(f"{q} questions (max 2)")
    if q == 0 and a.stage != "offer":
        warns.append("no question: end with one clear next step or question")
    if re.search(r"(^|\n)\s*(#|\*|- )", text):
        warns.append("markdown-like formatting; Upwork chat shows it raw")
    for term in [t.strip() for t in a.must.split(",") if t.strip()]:
        if term.lower() not in low:
            fails.append(f"client term not answered: '{term}'")

    for w in warns:
        print("WARN:", w)
    for f in fails:
        print("FAIL:", f)
    print(f"words={words} stage={a.stage}")
    print("RESULT:", "FAIL" if fails else "PASS")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
