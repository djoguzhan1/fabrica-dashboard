#!/usr/bin/env python3
"""CI: en zor senaryo — Standart GO ve Tam GO gönderimde P >= 30%."""
import re
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_P = 0.30


def run_score(extra):
    cmd = [sys.executable, f"{ROOT}/scripts/go_score.py", "--verified", "--scenario", "hardest"] + extra
    p = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r"= ([\d.]+)%", p.stdout or "")
    if not m:
        print("FAIL:", p.stdout, p.stderr)
        sys.exit(1)
    return float(m.group(1)) / 100.0, (p.stdout or "").strip()


def main():
    _, line_draft = run_score([])
    print("=== en zor, gönderim hazır değil (draft) ===")
    print(line_draft)

    p_std, line_std = run_score(["--go-standard-complete"])
    print("\n=== en zor + Standart GO (Tam değil) ===")
    print(line_std)
    if p_std < MIN_P:
        print(f"FAIL standard P {p_std:.1%} < {MIN_P:.0%}")
        sys.exit(1)

    p_tam, line_tam = run_score(["--tam-go-complete"])
    print("\n=== en zor + Tam GO ===")
    print(line_tam)
    if p_tam < MIN_P:
        print(f"FAIL tam P {p_tam:.1%} < {MIN_P:.0%}")
        sys.exit(1)

    print(f"\nPASS: standard & tam send-ready >= {MIN_P:.0%}")


if __name__ == "__main__":
    main()
