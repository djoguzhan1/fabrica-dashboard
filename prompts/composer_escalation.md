# Composer escalation (§12.0.2) — decision tree

| Signal | Action |
| --- | --- |
| `go_precheck.py` SKIP | Stop. No Tasks. Tell user reasons. |
| lint FAIL (length/AI) | Writer retry same model |
| lint FAIL (must_terms) | Re-run T1 → writer |
| J1 FAIL, J2 PASS | Tur++; J1 feedback to writer |
| J2 FAIL (proof), J1 PASS | Tur++; strengthen prework or J2 medium |
| Both FAIL "bot/AI" | Change archetype A1→A2→A3 |
| Both FAIL "elit wins" | Prework slice + writer medium; else SKIP |
| J1/J2 conflict | T8 required; default FAIL |
| 3 tur exhausted | SKIP |
| Budget ≥150 or B4≥25 | Start on Opus medium + Gemini medium |
| SNIPER + hire_without_call=no | Fix blocker once; Grok holdout optional |

Never raise Opus high / Terra max (cost cap).
