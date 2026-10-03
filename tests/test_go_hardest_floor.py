#!/usr/bin/env python3
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_hardest_tam_stack_at_least_30pct():
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_hardest_scenario.py"],
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0, p.stdout + p.stderr


if __name__ == "__main__":
    test_hardest_tam_stack_at_least_30pct()
    print("ok")
