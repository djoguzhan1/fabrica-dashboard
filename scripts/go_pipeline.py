#!/usr/bin/env python3
"""Print Composer checklist for one job (stdin = description)."""
import argparse
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, required=True)
    ap.add_argument("--title", default="")
    ap.add_argument("--payment-verified", action="store_true")
    ap.add_argument("--ongoing", action="store_true")
    ap.add_argument("--b4-plus-one", type=int)
    args, score_extra = ap.parse_known_args()
    post = sys.stdin.read()
    path = "/tmp/go_pipeline_post.txt"
    open(path, "w", encoding="utf-8").write(post)

    pre = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_precheck.py",
         "--budget", str(args.budget), "--title", args.title,
         "--payment-verified", "--description-file", path]
        + (["--ongoing"] if args.ongoing else [])
        + (["--b4-plus-one", str(args.b4_plus_one)] if args.b4_plus_one else []),
        capture_output=True, text=True,
    )
    print("=== PRECHECK ===")
    print(pre.stdout)
    if pre.returncode != 0:
        print("\nSTOP: no model pipeline")
        sys.exit(1)

    score = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_score.py",
         "--budget", str(args.budget), "--verified", "--proposals", "3",
         "--boost-top4", "--prework", "strong", "--scope-clear", "--demo-match", "exact"]
        + score_extra,
        capture_output=True, text=True,
    )
    print("=== SCORE ===")
    print(score.stdout)
    # EV hint
    import re
    m = re.search(r"= ([0-9.]+)%", score.stdout)
    if m:
        p = float(m.group(1)) / 100
        subprocess.run(
            [sys.executable, f"{ROOT}/scripts/estimate_ev.py",
             "--budget", str(args.budget), "--p", str(p)],
            check=False,
        )
    print("\n=== NEXT ===")
    print("1) Parallel Tasks: prompts/researcher.md, builder_opus.md, visual_agent.md")
    print("2) writer_opus.md → proposal_lint.py (--card-must, --ban-in-card)")
    print("3) judge1_terra.md + judge2_gemini.md parallel")
    print("4) T8 → send boost B4+1")
    print("5) On message: SOHBET → prompts/chat_*.md + reply_lint.py --chat-ready for rescore")


if __name__ == "__main__":
    main()
