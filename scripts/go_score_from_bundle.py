#!/usr/bin/env python3
"""Score from JOB_BUNDLE after job_bundle_validate.py PASS."""
import json
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    data = json.load(open(path, encoding="utf-8") if path else sys.stdin)

    v = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/job_bundle_validate.py"] + ([path] if path else []),
        input=None if path else json.dumps(data),
        capture_output=True,
        text=True,
    )
    if v.returncode != 0:
        print(v.stdout, v.stderr)
        sys.exit(1)

    cf = data.get("client_facts") or {}
    act = data.get("activity") or {}
    tg = data.get("tam_go") or {}
    gs = data.get("go_standard") or {}
    args = [
        sys.executable,
        f"{ROOT}/scripts/go_score.py",
        "--verified",
        "--budget",
        str(data.get("budget_fixed") or 100),
        "--age",
        str(cf.get("job_age_minutes") or 12),
        "--interviewing",
        str(act.get("interviewing") or 0),
        "--invites",
        str(act.get("invites_sent") or 0),
        "--client-hires",
        str(cf.get("hires") or 0),
        "--boost-top4",
        "--scope-clear",
    ]
    if cf.get("hire_rate_pct") is not None:
        args += ["--client-hire-rate", str(cf["hire_rate_pct"])]
    scr = data.get("screening") or {}
    if scr.get("required"):
        args.append("--screening-required")
    if tg.get("field_bot_heavy") or gs.get("field_bot_heavy"):
        args.append("--field-bot-heavy")
    if tg.get("client_picky") or gs.get("client_picky"):
        args.append("--client-picky")
    if tg.get("hardest_scenario") or gs.get("hardest_scenario"):
        args += ["--scenario", "hardest"]
    if gs.get("complete"):
        args.append("--go-standard-complete")
    if tg.get("complete"):
        args.append("--tam-go-complete")
    subprocess.run(args, check=True)


if __name__ == "__main__":
    main()
