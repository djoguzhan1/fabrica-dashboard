#!/usr/bin/env python3
"""JOB_BUNDLE validator — Standard GO or Tam GO send contracts."""
import json
import os
import re
import sys

REQUIRED = [
    "job_post", "title", "budget_fixed", "primary_deliverable",
    "primary_terms", "prework_slice",
]

SCREENING_HINTS = re.compile(
    r"(start your proposal with|begin your (cover )?letter with|include the word|"
    r"answer the following|to be considered|hidden keyword|must mention)",
    re.I,
)

TAM_GO_SEND_KEYS = [
    ("audit_report_path", "site_audit report path"),
    ("slice_evidence", "working slice URL or path"),
    ("loom_or_video_path", "loom/video path"),
    ("m1_micro_text", "M1 milestone text"),
    ("fixed_offer_line", "fixed price line"),
]


def load_data(path):
    if path:
        return json.load(open(path, encoding="utf-8"))
    return json.load(sys.stdin)


def validate_standard(data, scr):
    gs = data.get("go_standard") or {}
    fails = []
    if not gs.get("complete"):
        return ["go_standard.complete not set"]
    if not gs.get("lint_passed"):
        fails.append("go_standard.lint_passed (proposal_lint exit 0)")
    if not (data.get("letter") or "").strip():
        fails.append("letter")
    for key in ("m1_micro_text", "fixed_offer_line", "chat_bundle_path"):
        if not (gs.get(key) or "").strip():
            fails.append(f"go_standard.{key}")
    if not (gs.get("arena_kit_proof") or "").strip() and not (gs.get("post_diagnosis_line") or "").strip():
        fails.append("arena_kit_proof or post_diagnosis_line")
    if not (gs.get("judge1_pass") or gs.get("human_t8")):
        fails.append("judge1_pass or human_t8")
    if scr.get("required"):
        for kw in scr.get("hidden_keywords") or []:
            if kw.lower() not in data.get("letter", "").lower():
                fails.append(f"screening keyword in letter: {kw}")
        prefix = scr.get("start_with_prefix") or ""
        if prefix and not data.get("letter", "").lstrip().startswith(prefix):
            fails.append("screening start_with_prefix")
    cb = gs.get("chat_bundle_path") or ""
    if cb and not os.path.isfile(cb):
        fails.append(f"chat_bundle_path not found: {cb}")
    return fails


def validate_tam(data, scr):
    tg = data.get("tam_go") or {}
    fails = []
    if not tg.get("sim_t8_pass") or not tg.get("beats_elite"):
        fails.append("tam_go.sim_t8_pass and beats_elite")
    if not tg.get("chat_bundle_ready"):
        fails.append("tam_go.chat_bundle_ready")
    for key, label in TAM_GO_SEND_KEYS:
        if not (tg.get(key) or "").strip():
            fails.append(f"tam_go.{key} ({label})")
    if scr.get("required") and not scr.get("must_answer_in_letter"):
        fails.append("screening answers for letter")
    return fails


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    data = load_data(path)
    missing = [k for k in REQUIRED if not data.get(k)]
    if missing:
        print("FAIL missing:", ", ".join(missing))
        sys.exit(1)
    if not data.get("primary_terms"):
        print("FAIL primary_terms empty")
        sys.exit(1)

    post = data.get("job_post", "")
    scr = data.get("screening") or {}
    if SCREENING_HINTS.search(post) or scr.get("required"):
        scr["required"] = True
        if not scr.get("must_answer_in_letter") and not scr.get("hidden_keywords") and not scr.get("start_with_prefix"):
            print("FAIL screening job but screening fields empty")
            sys.exit(1)

    tg = data.get("tam_go") or {}
    gs = data.get("go_standard") or {}
    ax = data.get("apex_go") or {}

    if ax.get("complete"):
        fails = []
        if not gs.get("complete"):
            fails.append("go_standard.complete")
        else:
            fails += validate_standard(data, scr)
        if not tg.get("complete"):
            fails.append("tam_go.complete")
        else:
            fails += validate_tam(data, scr)
        letter = data.get("letter", "")
        for term in ax.get("uma_echo_terms") or []:
            if term.lower() not in letter[:110].lower():
                fails.append(f"uma_echo in card: {term}")
        if ax.get("client_last_viewed_hours") is None or ax["client_last_viewed_hours"] > 6:
            fails.append("client_last_viewed_hours <= 6")
        if not (ax.get("go_plus_reason") or "").strip():
            fails.append("go_plus_reason")
        if not (ax.get("catalog_or_portfolio_url") or "").strip():
            fails.append("catalog_or_portfolio_url")
        if not (ax.get("edit_six_hour_plan") or "").strip():
            fails.append("edit_six_hour_plan")
        if not ax.get("elite_margin_unanimous"):
            fails.append("elite_margin_unanimous")
        if len(ax.get("proof_chain") or []) < 2:
            fails.append("proof_chain min 2")
        if fails:
            print("FAIL apex_go.complete:")
            for f in fails:
                print(" ", f)
            sys.exit(1)
        print("PASS apex_go.complete")
        sys.exit(0)

    if tg.get("complete"):
        fails = []
        if not gs.get("complete"):
            fails.append("go_standard.complete required before tam_go")
        else:
            fails = validate_standard(data, scr)
        fails += validate_tam(data, scr)
        if fails:
            print("FAIL tam_go.complete:")
            for f in fails:
                print(" ", f)
            sys.exit(1)
        print("PASS tam_go.complete")
        sys.exit(0)

    if gs.get("complete"):
        fails = validate_standard(data, scr)
        if fails:
            print("FAIL go_standard.complete:")
            for f in fails:
                print(" ", f)
            sys.exit(1)
        print("PASS go_standard.complete — score: go_score_from_bundle.py")
        sys.exit(0)

    print("PASS job_bundle draft (set go_standard.complete or tam_go.complete to send)")
    sys.exit(0)


if __name__ == "__main__":
    main()
