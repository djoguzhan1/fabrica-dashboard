#!/usr/bin/env python3
"""Fill go_standard fields on a JOB_BUNDLE (stdin → stdout)."""
import json
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    data = json.load(sys.stdin)
    budget = float(data.get("budget_fixed") or 100)
    deliverable = data.get("primary_deliverable") or data.get("title") or "scoped fix"
    m1 = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_m1_auto.py",
         "--budget", str(budget), "--deliverable", deliverable],
        capture_output=True,
        text=True,
        check=True,
    )
    lines = m1.stdout.strip().splitlines()
    m1_line = lines[0] if lines else ""
    fixed_line = lines[1] if len(lines) > 1 else ""

    post = data.get("job_post", "")
    post_path = "/tmp/go_standard_post.txt"
    with open(post_path, "w", encoding="utf-8") as f:
        f.write(post)
    kit = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_arena_kit.py",
         "--title", data.get("title", ""), "--description-file", post_path, "--json"],
        capture_output=True,
        text=True,
    )
    kit_info = json.loads(kit.stdout) if kit.returncode == 0 else {}

    gs = data.get("go_standard") or {}
    gs.setdefault("m1_micro_text", m1_line)
    gs.setdefault("fixed_offer_line", fixed_line)
    gs.setdefault("arena_kit_id", kit_info.get("arena_kit_id", "generic"))
    if kit_info.get("arena_kit_proof"):
        gs.setdefault("arena_kit_proof", kit_info["arena_kit_proof"])
    if not gs.get("post_diagnosis_line") and data.get("primary_terms"):
        gs.setdefault(
            "post_diagnosis_line",
            f"Primary deliverable: {deliverable} — terms matched: {', '.join(data['primary_terms'][:3])}.",
        )
    stub_path = os.path.join(ROOT, "kits/chat_stubs/first_reply.json")
    gs.setdefault("chat_bundle_path", stub_path)
    echo = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_client_echo.py",
         "--title", data.get("title", ""), "--json"],
        input=post,
        capture_output=True,
        text=True,
    )
    if echo.returncode == 0:
        ej = json.loads(echo.stdout)
        ax = data.get("apex_go") or {}
        ax.setdefault("uma_echo_terms", ej.get("uma_echo_terms", []))
        data["apex_go"] = ax
        gs.setdefault("must_terms_hint", ej.get("card_must", []))
    data["go_standard"] = gs
    json.dump(data, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
