# Log → model calibration (every 10 sends)

## Columns to fill
`opened`, `replied`, `hired`, `band`, `precheck`, `boost_status`, `loss_stage` (card / reply / hire / skip)

## Adjustments
| Pattern | Action |
| --- | --- |
| tam-paket + opened <40% | T5 panel or opener archetype A/B |
| opened ok, reply <25% | Prework type (slice vs video) |
| reply ok, hire <40% | §23 templates; enable `--chat-ready` on all threads |
| sim PASS, opened FAIL | Terra high one week on Judge 1 |
| precheck SKIP but you would have won | Do not loosen without 3 examples — log `false_skip` |

## go_score weight tweaks (manual)
Edit `scripts/go_score.py` hire/reply deltas; document change in Ek B weekly note.
