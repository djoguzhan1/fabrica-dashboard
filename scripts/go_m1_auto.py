#!/usr/bin/env python3
"""Generate micro M1 + fixed-offer lines from budget and primary deliverable."""
import argparse


def m1_amount(budget: float) -> int:
    if budget < 80:
        return 25
    if budget < 150:
        return 35
    if budget < 250:
        return 45
    return 55


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, required=True)
    ap.add_argument("--deliverable", required=True)
    ap.add_argument("--days", type=int, default=1)
    a = ap.parse_args()
    m1 = m1_amount(a.budget)
    m1_line = (
        f"Milestone 1: {a.deliverable.strip()[:80]} — ${m1}, "
        f"delivered within {a.days * 24}h; you review on Upwork before the rest is scoped."
    )
    fixed = f"Fixed ${int(a.budget)} total for the scope in your post (escrow, approve M1 to release)."
    print(m1_line)
    print(fixed)


if __name__ == "__main__":
    main()
