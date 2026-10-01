#!/usr/bin/env python3
"""JOB_BUNDLE validator before spawn Tasks or before send (Tam GO)."""
import json
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
            print("FAIL screening job but screening.must_answer_in_letter / hidden_keywords / start_with_prefix empty")
            sys.exit(1)

    ban = data.get("ban_in_card") or []
    prim = " ".join(data.get("primary_terms", [])).lower()
    for b in ban:
        if b.lower() in prim:
            print(f"WARN ban_in_card overlaps primary: {b}")

    tg = data.get("tam_go") or {}
    if tg.get("complete"):
        fails = []
        if not tg.get("sim_t8_pass") or not tg.get("beats_elite"):
            fails.append("tam_go.sim_t8_pass and beats_elite required for complete")
        if not (data.get("letter") or "").strip():
            fails.append("letter required for tam_go.complete")
        if not tg.get("chat_bundle_ready"):
            fails.append("tam_go.chat_bundle_ready")
        for key, label in TAM_GO_SEND_KEYS:
            if not (tg.get(key) or "").strip():
                fails.append(f"tam_go.{key} ({label})")
        if scr.get("required") and not scr.get("must_answer_in_letter"):
            fails.append("screening answers for letter")
        if fails:
            print("FAIL tam_go.complete:")
            for f in fails:
                print(" ", f)
            sys.exit(1)
        print("PASS tam_go.complete — run: python3 scripts/go_score_from_bundle.py", path or "<bundle>")
    else:
        print("PASS job_bundle (tam_go.complete not set — do not send yet)")

    sys.exit(0)


if __name__ == "__main__":
    main()
