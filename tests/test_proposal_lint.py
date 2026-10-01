#!/usr/bin/env python3
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ~100 words; Google Sheets + onEdit in first 150 chars; passes hard lint rules.
CARD_MUST_LETTER = """\
Google Sheets onEdit automation emails the row owner when column D changes — same trigger pattern as your intake tab.

The handler uses SpreadsheetApp and MailApp only, no add-ons. A test copy is linked below: edit column D once and the inbox copy arrives within about a minute.

Scope is the notification flow only, not dashboards or charts. Fixed $90 covers trigger wiring plus the email template, delivered within 24 hours.

Milestone one is the onEdit email path end to end. Which sheet tab name should the trigger watch for edits?
"""


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
    code, out = lint(["--card-must", "Google Sheets,onEdit"], CARD_MUST_LETTER)
    assert code == 0, out
    assert "PASS  primary deliverable in card" in out
    assert "RESULT: PASS" in out


def test_ban_in_card_fail():
    body = (
        "Your mobile LCP is 5.8s on the homepage; I also built your Sheets onEdit flow.\n\n"
        "Link below.\n\n"
        "Fixed $90.\n\n"
        "Which column triggers email?"
    )
    code, out = lint(["--ban-in-card", "LCP,PageSpeed", "--card-must", "Sheets"], body)
    assert code != 0
    assert "no off-scope audit in card" in out
    assert "FAIL" in out


if __name__ == "__main__":
    test_card_must_pass()
    test_ban_in_card_fail()
    print("ok")
