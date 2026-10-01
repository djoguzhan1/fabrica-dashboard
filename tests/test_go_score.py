#!/usr/bin/env python3
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(args):
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_score.py", *args],
        capture_output=True,
        text=True,
    )
    return p.stdout


def test_chat_ready_increases_hire():
    base = run(["--age", "10", "--budget", "100", "--verified", "--boost-top4",
                "--scope-clear", "--demo-match", "exact", "--prework", "strong"])
    ready = run(["--age", "10", "--budget", "100", "--verified", "--boost-top4",
                 "--scope-clear", "--demo-match", "exact", "--prework", "strong", "--chat-ready"])
    def pct(s):
        return float(s.split("hire ")[1].split("%")[0])
    assert pct(ready) > pct(base)


if __name__ == "__main__":
    test_chat_ready_increases_hire()
    print("ok")
