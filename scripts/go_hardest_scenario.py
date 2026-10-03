#!/usr/bin/env python3
"""CI: L1/L2/L3 en zor — standard < tam < apex."""
import re
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_score(extra):
    cmd = [sys.executable, f"{ROOT}/scripts/go_score.py", "--verified", "--scenario", "hardest"] + extra
    p = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r"= ([\d.]+)%", p.stdout or "")
    if not m:
        print("FAIL:", p.stdout, p.stderr)
        sys.exit(1)
    return float(m.group(1)), (p.stdout or "").strip()


def main():
    p_std, l1 = run_score(["--go-standard-complete"])
    p_tam, l2 = run_score(["--tam-go-complete"])
    p_apex, l3 = run_score(["--apex-go-complete"])

    print("L1 standard:", l1)
    print("L2 tam:", l2)
    print("L3 apex:", l3)

    if p_std < 30 or p_tam < 35 or p_apex < 40:
        sys.exit(1)
    if not (p_std < p_tam < p_apex):
        print(f"FAIL ordering: {p_std} {p_tam} {p_apex}")
        sys.exit(1)
    print(f"\nPASS: L1≥30% L2≥35% L3≥40% and strict ordering")


if __name__ == "__main__":
    main()
