#!/usr/bin/env python3
"""Structural GO/SKIP before Connects. Does NOT use proposal count for the decision.

Usage:
  python3 scripts/go_precheck.py --budget 100 --title "..." --description-file post.txt \\
      --ongoing --payment-verified --interviewing 0 --invites 0

Or pipe description:
  python3 scripts/go_precheck.py --budget 50 --title "Fix Elementor" < post.txt

Exit 0 = GO (structural), 1 = SKIP with reasons on stderr/stdout.
"""
import argparse
import re
import sys

ARENA_OUTSIDE = [
    r"\brag\b", r"retrieval[- ]augmented", r"langchain", r"pinecone", r"weaviate", r"chroma",
    r"vector\s+database", r"embedding(s)?\s+model", r"fine[- ]?tun", r"llm\s+train",
    r"train\s+(a|an)\s+model", r"\bghl\b", r"go\s*high\s*level", r"\bcrm\s+setup\b",
    r"woocommerce\s+checkout", r"mobile\s+app", r"react\s+native", r"\bflutter\b", r"\bsaas\s+mvp\b",
    r"react\s+app\s+from\s+scratch", r"shopify\s+app", r"shopify\s+store\s+setup", r"blockchain",
    r"\bnft\b", r"\bweb3\b", r"trading\s+bot", r"\bmt4\b", r"captcha", r"homework", r"thesis",
    r"unpaid\s+test", r"scrape\s+login", r"behind\s+login", r"devops", r"\bkubernetes\b",
    r"security\s+clearance", r"native\s+english\s+speaker", r"power\s+bi", r"\btableau\b",
]
ONGOING = [r"\bongoing\b", r"long[- ]term", r"40\s*hours?\s*/?\s*week", r"full[- ]time\s+position"]
CALL_REQUIRED = [r"video\s+call", r"phone\s+call", r"zoom\s+meeting", r"google\s+meet", r"hop\s+on\s+a\s+call"]
HUGE_SCOPE_LOW_BUDGET = [
    (r"figma.*(full|entire|complete).*(website|site)", 80),
    (r"(entire|full|complete)\s+(website|web\s*site)", 80),
    (r"from\s+scratch", 100),
    (r"build\s+(a|an)\s+(saas|app|platform)", 150),
]


def read_text(args):
    if args.description_file:
        return open(args.description_file, encoding="utf-8").read()
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return args.description or ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, required=True)
    ap.add_argument("--title", default="")
    ap.add_argument("--description", default="")
    ap.add_argument("--description-file")
    ap.add_argument("--payment-verified", action="store_true")
    ap.add_argument("--ongoing", action="store_true", help="job marked ongoing")
    ap.add_argument("--interviewing", type=int, default=0)
    ap.add_argument("--invites", type=int, default=0)
    ap.add_argument("--last-viewed-hours", type=float, default=None)
    ap.add_argument("--client-hire-rate", type=float, default=None)
    ap.add_argument("--client-hires", type=int, default=None)
    ap.add_argument("--b4-plus-one", type=int, default=None, help="required boost bid; compare to cap")
    a = ap.parse_args()

    text = f"{a.title}\n{read_text(a)}".lower()
    skips, warns, goplus = [], [], []

    if a.budget < 50:
        skips.append("K6: budget < $50")
    if not a.payment_verified:
        skips.append("payment not verified")

    for pat in CALL_REQUIRED:
        if re.search(pat, text, re.I):
            skips.append("client requires call (§5 / constraints)")
            break

    if a.ongoing or any(re.search(p, text, re.I) for p in ONGOING):
        skips.append("ongoing / long-term (§21.2)")

    for pat in ARENA_OUTSIDE:
        if re.search(pat, text, re.I):
            skips.append(f"arena outside: matched /{pat}/")
            break

    for pat, min_budget in HUGE_SCOPE_LOW_BUDGET:
        if a.budget < min_budget and re.search(pat, text, re.I):
            skips.append(f"scope vs budget: needs ~${min_budget}+ for this wording")

    if a.invites >= 5 and a.interviewing >= 1:
        skips.append("Activity: invites≥5 and interviewing≥1")
    if a.interviewing >= 2:
        skips.append("Activity: interviewing≥2")
    if a.last_viewed_hours is not None and a.last_viewed_hours > 24:
        skips.append("Activity: client last viewed >24h ago")
    if a.client_hire_rate is not None and a.client_hires and a.client_hires >= 5 and a.client_hire_rate < 30:
        skips.append("client hire rate <30% with 5+ jobs")

    if a.budget < 50 and a.client_hires == 0 and len(text) < 200:
        warns.append("new client + low budget + thin brief")

    cap = 11 if a.budget < 80 else (15 if a.budget < 100 else (35 if a.budget < 200 else 40))
    if a.b4_plus_one is not None and a.b4_plus_one > cap:
        skips.append(f"boost B4+1={a.b4_plus_one} > cap {cap}")

    if a.payment_verified and a.client_hires == 0 and "scope" in text:
        goplus.append("new verified client with readable scope")
    if a.client_hires == 0 and a.budget >= 50:
        pass  # not skip

    if skips:
        print("SKIP")
        for s in skips:
            print(f"  - {s}")
        if warns:
            print("WARN:")
            for w in warns:
                print(f"  - {w}")
        sys.exit(1)

    print("GO (structural)")
    if goplus:
        for g in goplus:
            print(f"  GO+: {g}")
    if warns:
        for w in warns:
            print(f"  WARN: {w}")
    print(f"  boost_cap_4th: {cap}")
    sys.exit(0)


if __name__ == "__main__":
    main()
