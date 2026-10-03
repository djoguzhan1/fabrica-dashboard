#!/usr/bin/env python3
import json
import subprocess
import sys
import os
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def score_pct(args):
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_score.py", "--verified", "--scenario", "hardest"] + args,
        capture_output=True,
        text=True,
    )
    import re
    m = re.search(r"= ([\d.]+)%", p.stdout)
    assert m, p.stdout + p.stderr
    return float(m.group(1))


def test_standard_complete_at_least_30():
    p = score_pct(["--go-standard-complete"])
    assert p >= 30.0, p


def test_bundle_standard_hardest():
    stub = os.path.join(ROOT, "kits/chat_stubs/first_reply.json")
    b = {
        "job_post": "Fix Elementor mobile sticky header",
        "title": "Elementor mobile",
        "budget_fixed": 130,
        "primary_deliverable": "sticky header padding",
        "primary_terms": ["Elementor", "mobile"],
        "prework_slice": "kit-based proof",
        "letter": "Elementor mobile sticky overlap — start with WORD test",
        "screening": {"required": True, "start_with_prefix": "Elementor"},
        "go_standard": {
            "complete": True,
            "lint_passed": True,
            "m1_micro_text": "M1 $35 24h",
            "fixed_offer_line": "Fixed $130",
            "arena_kit_proof": os.path.join(ROOT, "kits/elementor-mobile/fix-sticky-offset.css"),
            "chat_bundle_path": stub,
            "judge1_pass": True,
            "hardest_scenario": True,
            "field_bot_heavy": True,
            "client_picky": True,
        },
        "client_facts": {"job_age_minutes": 12, "hires": 12, "hire_rate_pct": 26},
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(b, f)
        path = f.name
    v = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/job_bundle_validate.py", path],
        capture_output=True,
        text=True,
    )
    assert v.returncode == 0, v.stdout + v.stderr
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_score_from_bundle.py", path],
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0
    assert float(__import__("re").search(r"= ([\d.]+)%", p.stdout).group(1)) >= 30.0


if __name__ == "__main__":
    test_standard_complete_at_least_30()
    test_bundle_standard_hardest()
    print("ok")
