#!/usr/bin/env python3
"""Measure en zor tam GO + tam-stack floor (CI gate >= 30%).

See docs/hardest_scenario.md
"""
import re
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_P = 0.30


def run_score(extra):
    cmd = [sys.executable, f"{ROOT}/scripts/go_score.py", "--verified", "--scenario", "hardest", "--tam-stack"] + extra
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = (p.stdout or "") + (p.stderr or "")
    m = re.search(r"= ([\d.]+)%", p.stdout or "")
    if not m:
        print("FAIL: no score line\n", out)
        sys.exit(1)
    return float(m.group(1)) / 100.0, p.stdout.strip(), p.stderr.strip()


def main():
    # Incomplete stack: must be below floor target
    p_weak, line_weak, _ = run_score([])
    print("=== incomplete tam-stack (expect no floor) ===")
    print(line_weak)
    print(f"P={p_weak:.1%}")

    gates = [
        "--audit-findings",
        "--slice-delivered",
        "--sim-t8-pass",
        "--letter-screening-pass",
        "--profile-highlights",
        "--m1-micro",
        "--chat-ready",
        "--fixed-offer-ready",
        "--reply-under-10m",
    ]
    p_full, line_full, err = run_score(gates)
    print("\n=== en zor + full tam-stack ===")
    print(line_full)
    if err:
        print(err)
    print(f"P={p_full:.1%}")

    if p_full < MIN_P:
        print(f"\nFAIL: P {p_full:.1%} < {MIN_P:.0%} floor")
        sys.exit(1)
    if "tam-stack-floor" not in line_full and "tam-stack-cap" not in line_full:
        print("\nWARN: expected tam-stack-floor or tam-stack-cap on full stack")
    print(f"\nPASS: en zor tam-stack P >= {MIN_P:.0%}")


if __name__ == "__main__":
    main()
