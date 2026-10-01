#!/usr/bin/env python3
"""Rough parse of pasted Vibeworker/Upwork job text into precheck args.

Usage: python3 scripts/parse_vibeworker_paste.py < paste.txt
Prints suggested go_pipeline command (manual verify).
"""
import re
import sys

text = sys.stdin.read()
budget = re.search(r"\$(\d+(?:\.\d+)?)", text)
ongoing = bool(re.search(r"ongoing", text, re.I))
title_m = re.search(r"^(.{10,120})$", text.strip().split("\n")[0] if text.strip() else "")
b = budget.group(1) if budget else "100"
title = (title_m.group(1) if title_m else "job").replace('"', "'")
print(f'python3 scripts/go_pipeline.py --budget {b} --payment-verified --title "{title[:80]}"', end="")
if ongoing:
    print(" --ongoing", end="")
print(" < post.txt")
