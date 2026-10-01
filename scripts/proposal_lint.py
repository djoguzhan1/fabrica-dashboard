#!/usr/bin/env python3
"""Rule-based pre-send check for an Upwork cover letter.

Usage:
  python3 scripts/proposal_lint.py letter.txt [--must "Elementor,contact form"]
                                    [--card-must "Google Sheets,onEdit"]
                                    [--ban-in-card "LCP,PageSpeed,overflow"]
                                    [--title "Fix Elementor mobile layout"] [--check-links]

Exit code 0 = all hard checks pass, 1 = at least one FAIL.
"""
import argparse
import re
import statistics
import sys
import urllib.request

CARD_DESKTOP = 150
CARD_MOBILE = 110
WORDS_MIN, WORDS_MAX = 90, 150
MAX_LINKS = 2
MAX_EM_DASHES = 2

OPENER_BANNED_START = re.compile(
    r"^\s*(hi|hello|hey|dear|greetings|good (morning|afternoon|day)|i\b|i'm|i am|my name)",
    re.I,
)
OPENER_BANNED_WORDS = [
    "experience", "years", "excited", "came across", "i hope", "top rated", "perfect fit",
    "job success", "jss", "expert-vetted", "carefully read", "i am confident", "i'm confident",
]
AI_PHRASES = [
    "delve", "seamless", "seamlessly", "leverage", "i'd be happy to", "i would be happy to",
    "proven track record", "aligns perfectly", "with precision", "rest assured", "look no further",
    "cutting-edge", "robust", "elevate", "streamline", "tailored", "i understand you need",
    "i have carefully read", "i've gone through your requirements", "don't hesitate",
    "feel free to reach out", "high-quality results", "top-notch", "game-changer",
    "in today's", "furthermore", "moreover", "additionally,", "ensure a smooth",
]
MARKDOWN = re.compile(r"(\*\*|__|^#{1,6}\s|`)", re.M)
URL = re.compile(r"https?://\S+")


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if len(p.strip().split()) >= 3]


def check_links(urls):
    bad = []
    for u in urls:
        u = u.rstrip(").,;")
        try:
            req = urllib.request.Request(u, method="GET", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                if r.status >= 400:
                    bad.append(f"{u} -> {r.status}")
        except Exception as e:  # noqa: BLE001
            bad.append(f"{u} -> {e}")
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("letter")
    ap.add_argument("--must", default="", help="comma-separated job terms that must appear verbatim in letter")
    ap.add_argument("--card-must", default="", help="primary deliverable terms; all must appear in first 150 chars")
    ap.add_argument("--ban-in-card", dest="ban_in_card", default="", help="off-scope audit terms; must not appear in first 150 chars")
    ap.add_argument("--title", default="", help="job title; repeating it verbatim is a bot sign")
    ap.add_argument("--screening-start", default="",
                    help="if client said proposal must start with X, check card starts with it (case-insensitive prefix)")
    ap.add_argument("--check-links", action="store_true")
    a = ap.parse_args()

    text = open(a.letter, encoding="utf-8").read().strip()
    low = text.lower()
    flat = re.sub(r"\s+", " ", text)
    results = []

    def res(level, name, detail=""):
        results.append((level, name, detail))

    words = len(re.findall(r"\b[\w'’-]+\b", URL.sub("", text)))
    res("PASS" if WORDS_MIN <= words <= WORDS_MAX else "FAIL", "word count", f"{words} (target {WORDS_MIN}-{WORDS_MAX})")

    card = flat[:CARD_DESKTOP]
    mobile = flat[:CARD_MOBILE]
    res("FAIL" if OPENER_BANNED_START.search(flat) else "PASS", "opener does not start with greeting/I", card[:40] + "…")
    hits = [w for w in OPENER_BANNED_WORDS if w in card.lower()]
    res("FAIL" if hits else "PASS", "no self-talk in first 150 chars", ", ".join(hits))
    first_sentence_end = re.search(r"[.!?:]", flat)
    ends_in_card = bool(first_sentence_end) and first_sentence_end.start() < CARD_DESKTOP
    res("PASS" if ends_in_card else "FAIL", "first sentence ends inside the 150-char card")
    res("INFO", "desktop card (150)", card)
    res("INFO", "mobile card (110)", mobile)

    ai = [p for p in AI_PHRASES if p in low]
    res("FAIL" if ai else "PASS", "no AI/template phrases", ", ".join(ai))

    res("FAIL" if MARKDOWN.search(text) else "PASS", "plain text (no markdown)")

    dashes = text.count("—")
    res("FAIL" if dashes > MAX_EM_DASHES else "PASS", "em dashes", f"{dashes} (max {MAX_EM_DASHES})")

    q = text.count("?")
    res("PASS" if q == 1 else "FAIL", "exactly one question", str(q))

    urls = URL.findall(text)
    res("PASS" if len(urls) <= MAX_LINKS else "FAIL", "link count", f"{len(urls)} (max {MAX_LINKS})")
    if a.check_links and urls:
        bad = check_links(urls)
        res("FAIL" if bad else "PASS", "links open", "; ".join(bad))

    sents = sentences(text)
    if sents:
        i_starts = sum(1 for s in sents if re.match(r"^(i|i'm|i've|i'd|i'll|my)\b", s, re.I))
        ratio = i_starts / len(sents)
        res("FAIL" if ratio > 0.3 else "PASS", "sentences starting with I/my", f"{i_starts}/{len(sents)}")
        if len(sents) >= 4:
            sd = statistics.pstdev(len(s.split()) for s in sents)
            res("WARN" if sd < 3 else "PASS", "sentence length varies (uniform = AI-like)", f"stdev {sd:.1f} words")

    if a.title and a.title.lower() in low:
        res("FAIL", "job title not repeated verbatim (bot sign)", a.title)

    if a.screening_start:
        need = a.screening_start.strip().lower()
        if not card.lower().startswith(need) and need not in card.lower()[:80]:
            res("FAIL", "screening: card must lead with client instruction", a.screening_start[:60])

    musts = [m.strip() for m in a.must.split(",") if m.strip()]
    if musts:
        missing = [m for m in musts if m.lower() not in low]
        res("FAIL" if missing else "PASS", "job requirement terms present verbatim", "missing: " + ", ".join(missing) if missing else f"{len(musts)}/{len(musts)}")
        if not a.card_must:
            in_card = [m for m in musts if m.lower() in card.lower()]
            res("PASS" if in_card else "FAIL", "at least one job term inside the card", ", ".join(in_card))

    card_musts = [m.strip() for m in a.card_must.split(",") if m.strip()]
    if card_musts:
        missing_card = [m for m in card_musts if m.lower() not in card.lower()]
        res("FAIL" if missing_card else "PASS", "primary deliverable in card (150)", "missing: " + ", ".join(missing_card) if missing_card else f"{len(card_musts)}/{len(card_musts)}")

    bans = [b.strip() for b in a.ban_in_card.split(",") if b.strip()]
    if bans:
        hit = [b for b in bans if b.lower() in card.lower()]
        res("FAIL" if hit else "PASS", "no off-scope audit in card", ", ".join(hit) if hit else "clean")

    width = max(len(n) for _, n, _ in results)
    for level, name, detail in results:
        print(f"{level:4}  {name:<{width}}  {detail}")
    failed = any(l == "FAIL" for l, _, _ in results)
    print("\nRESULT:", "FAIL" if failed else "PASS")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
