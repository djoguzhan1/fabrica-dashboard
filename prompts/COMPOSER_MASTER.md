# Composer master checklist (one GO)

1. Parse user paste → write `/tmp/job_post.txt`
2. `python3 scripts/go_pipeline.py --budget N --payment-verified --title "..." --ongoing? --b4-plus-one N < post.txt`
3. If STOP → tell user SKIP reasons only (no proposal count arguments)
4. Fill `job_bundle.schema.json` fields; `job_bundle_validate.py`
5. Parallel Task: `researcher.md`, `builder_opus.md`, `visual_agent.md`
6. Merge prework; T1 + **`screening_extractor.md` zorunlu** if post matches screening / bundle.screening.required
7. Task `writer_opus.md` → `proposal_lint.py` with `--card-must`, `--ban-in-card`, `--screening-start`, `--must-in-first-n-sentences 3`, `--forbidden-letter`
8. Parallel Task judges; `composer_escalation.md` on FAIL
9. User T8 → send; log Ek B with `b4_at_send`, `band`, `primary_deliverable`
10. On client message: `SOHBET` → triage → `chat_writer.md` → `reply_lint.py`; rescore with `--chat-ready` when reply drafted

Models never see each other's raw chat; only Composer passes JSON/text blocks.
