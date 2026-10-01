#!/usr/bin/env python3
import json
import subprocess
import sys
import os
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def validate(bundle):
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/job_bundle_validate.py"],
        input=json.dumps(bundle),
        capture_output=True,
        text=True,
    )
    return p.returncode, p.stdout + p.stderr


def base_bundle():
    return {
        "job_post": "Fix Elementor mobile menu",
        "title": "Elementor fix",
        "budget_fixed": 130,
        "primary_deliverable": "mobile menu z-index fix",
        "primary_terms": ["Elementor", "mobile"],
        "prework_slice": "preview link",
        "letter": "Cover letter with primary fix.",
        "screening": {"required": False},
        "tam_go": {"complete": False},
    }


def test_tam_go_complete_requires_artifacts():
    b = base_bundle()
    b["tam_go"] = {"complete": True, "sim_t8_pass": True, "beats_elite": True}
    code, out = validate(b)
    assert code == 1 and "tam_go.complete" in out


def test_tam_go_complete_pass_scores():
    b = base_bundle()
    b["tam_go"] = {
        "complete": True,
        "sim_t8_pass": True,
        "beats_elite": True,
        "audit_report_path": "/tmp/audit/report.json",
        "slice_evidence": "https://example.com/preview",
        "loom_or_video_path": "/tmp/loom.mp4",
        "m1_micro_text": "M1: mobile fix $35 24h",
        "fixed_offer_line": "Fixed $130 for scope",
        "chat_bundle_ready": True,
        "hardest_scenario": True,
        "field_bot_heavy": True,
        "client_picky": True,
    }
    b["client_facts"] = {"job_age_minutes": 12, "hires": 12, "hire_rate_pct": 26}
    code, out = validate(b)
    assert code == 0 and "tam_go.complete" in out
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(b, f)
        path = f.name
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_score_from_bundle.py", path],
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0
    assert "= 30." in p.stdout or "= 31." in p.stdout or "= 32." in p.stdout or "= 33." in p.stdout


if __name__ == "__main__":
    test_tam_go_complete_requires_artifacts()
    test_tam_go_complete_pass_scores()
    print("ok")
