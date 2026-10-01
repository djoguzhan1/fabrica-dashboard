# Standart GO (Tam GO olmadan gönderim)

Her **GO** ilanında minimum sistem — paralel builder/video şart değil.

## Akış

1. `go_precheck` PASS  
2. `go_standard_enrich.py` → M1, arena kit, chat stub yolu  
3. Writer + `proposal_lint.py` → `lint_passed: true`  
4. Hakem 1 PASS **veya** insan T8 → `judge1_pass` / `human_t8`  
5. `go_standard.complete: true` → `job_bundle_validate.py` PASS  
6. `go_score_from_bundle.py` → en zorda **P ≈ 30–33%** (`tier=standard`)

## Zorunlu alanlar (`go_standard`)

| Alan | Kaynak |
| --- | --- |
| `m1_micro_text`, `fixed_offer_line` | `go_m1_auto.py` / enrich |
| `arena_kit_proof` veya `post_diagnosis_line` | `go_arena_kit.py` veya T1 |
| `chat_bundle_path` | `kits/chat_stubs/first_reply.json` |
| `lint_passed` | proposal_lint exit 0 |
| `letter` | Writer |

## Tam GO farkı

Tam GO = Standart GO **+** dilim, audit, Loom, sim beats_elite. Skor: **≈35–38%** en zorda (`tier=tam`); Standart **30–33%**. Ek iş = elit panel + müşteri diliminde kanıt.

## Komutlar

```bash
cat bundle.json | python3 scripts/go_standard_enrich.py > bundle.enriched.json
python3 scripts/job_bundle_validate.py bundle.enriched.json
python3 scripts/go_score_from_bundle.py bundle.enriched.json
```
