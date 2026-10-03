#!/usr/bin/env python3
"""Pick arena kit + proof path from job text (PRIMARY evidence without full Tam GO slice)."""
import argparse
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RULES = [
    (r"elementor|wordpress|mobile menu|sticky", "elementor-mobile", "kits/elementor-mobile/fix-sticky-offset.css"),
    (r"landing|hero|above the fold", "landing-hero", "kits/landing-hero/index.html"),
    (r"google sheet|apps script|onedit|spreadsheet", "apps-script-notify", "kits/apps-script-notify/README.md"),
    (r"csv|pandas|python.*clean|dedupe", "python-csv-clean", "kits/python-csv-clean/clean.py"),
    (r"n8n|webhook|zapier|make\.com", "n8n-webhook", "kits/n8n-webhook/webhook-to-sheet.json"),
]


def pick(text: str):
    t = text.lower()
    for pat, kit_id, proof in RULES:
        if re.search(pat, t, re.I):
            return kit_id, os.path.join(ROOT, proof)
    return "generic", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="")
    ap.add_argument("--description-file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = a.title
    if a.description_file:
        text += "\n" + open(a.description_file, encoding="utf-8").read()
    kit_id, proof = pick(text)
    out = {"arena_kit_id": kit_id, "arena_kit_proof": proof}
    if a.json:
        print(json.dumps(out))
    else:
        print(kit_id)
        if proof:
            print(proof)


if __name__ == "__main__":
    main()
