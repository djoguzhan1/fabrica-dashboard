#!/usr/bin/env python3
"""CI: en zor senaryo + Tam GO sözleşmesi → P >= 30%.

Gönderim öncesi tek bayrak: --tam-go-complete (job_bundle_validate PASS).
"""
import re
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_P = 0.30


def run_score(extra):
    cmd = [
        sys.executable,
        f"{ROOT}/scripts/go_score.py",
        "--verified",
        "--scenario",
        "hardest",
    ] + extra
    p = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r"= ([\d.]+)%", p.stdout or "")
    if not m:
        print("FAIL: no score\n", p.stdout, p.stderr)
        sys.exit(1)
    return float(m.group(1)) / 100.0, (p.stdout or "").strip()


def main():
    p_plan, line_plan = run_score([])
    print("=== en zor, Tam GO henüz yok (planlama) ===")
    print(line_plan)
    print(f"P={p_plan:.1%} (gönderme — pipeline bitir)")

    p_send, line_send = run_score(["--tam-go-complete"])
    print("\n=== en zor + Tam GO complete (gönderim) ===")
    print(line_send)
    print(f"P={p_send:.1%}")

    if p_send < MIN_P:
        print(f"\nFAIL: Tam GO complete P {p_send:.1%} < {MIN_P:.0%}")
        sys.exit(1)
    print(f"\nPASS: en zor + tam-go-complete P >= {MIN_P:.0%}")


if __name__ == "__main__":
    main()
