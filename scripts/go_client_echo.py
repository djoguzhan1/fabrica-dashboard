#!/usr/bin/env python3
"""Extract Uma/Shortlist echo terms from job post (tools, deliverables, pages)."""
import argparse
import json
import re
import sys

STOP = {
    "the", "and", "for", "with", "you", "your", "need", "looking", "experience",
    "please", "must", "will", "this", "that", "from", "have", "are", "our",
}

TOOL_PAT = re.compile(
    r"\b(wordpress|elementor|woocommerce|shopify|webflow|google sheets|apps script|"
    r"python|n8n|zapier|make\.com|react|next\.js|html|css|javascript|api|webhook)\b",
    re.I,
)
PAGE_PAT = re.compile(r"\b(/[\w/-]+|homepage|landing page|contact page|mobile)\b", re.I)


def top_terms(text: str, limit=5):
    words = re.findall(r"[A-Za-z][A-Za-z0-9+#.]{1,}", text)
    scored = []
    seen = set()
    for w in words:
        lw = w.lower()
        if lw in STOP or len(lw) < 3:
            continue
        if lw in seen:
            continue
        seen.add(lw)
        score = 2 if w[0].isupper() and len(w) > 3 else 1
        scored.append((score, w))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [w for _, w in scored[:limit]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = a.title + "\n" + sys.stdin.read()
    tools = list(dict.fromkeys(m.group(0) for m in TOOL_PAT.finditer(text)))[:4]
    pages = list(dict.fromkeys(m.group(0) for m in PAGE_PAT.finditer(text)))[:3]
    terms = tools + pages + top_terms(text, 5)
    # dedupe preserve order
    out = []
    for t in terms:
        if t.lower() not in {x.lower() for x in out}:
            out.append(t)
    out = out[:6]
    if a.json:
        print(json.dumps({"uma_echo_terms": out, "card_must": out[:3]}, indent=2))
    else:
        for t in out:
            print(t)


if __name__ == "__main__":
    main()
