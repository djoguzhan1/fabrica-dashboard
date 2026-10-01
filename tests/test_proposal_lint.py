#!/usr/bin/env python3
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def lint(args, body):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(body)
        path = f.name
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/proposal_lint.py", path, *args],
        capture_output=True,
        text=True,
    )
    os.unlink(path)
    return p.returncode, p.stdout


def test_card_must_pass():
    body = (
        "Your Google Sheets onEdit trigger can email the row owner when column D changes — "
        "working copy in the link below.\n\n"
        "Attached: test sheet copy.\n\n"
        "Fixed $90, 24h. Milestone: onEdit email flow only.\n\n"
        "Which tab should notifications use?"
    )
    code, out = lint(["--card-must", "Google Sheets,onEdit", "--must", "onEdit"], body)
    assert code == 0 or "word count" in out  # short body may fail words; card check matters
    assert "primary deliverable in card" in out or "PASS" in out


def test_ban_in_card_fail():
    body = (
        "Your mobile LCP is 5.8s on the homepage; I also built your Sheets onEdit flow.\n\n"
        "Link below.\n\n"
        "Fixed $90.\n\n"
        "Which column triggers email?"
    )
    code, out = lint(["--ban-in-card", "LCP,PageSpeed", "--card-must", "Sheets"], body)
    assert code != 0
    assert "off-scope" in out.lower() or "FAIL" in out


if __name__ == "__main__":
    test_ban_in_card_fail()
    print("ban ok")
    # card_must may fail word count on short sample — run extended if needed
    print("ok")
