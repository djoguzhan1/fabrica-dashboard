# En zor tam GO — %30 sözleşmesi

## Kural (değişmez)

**En zor bağlamda gönderim** `go_standard.complete` veya `tam_go.complete` + validate PASS. Skor:

```bash
python3 scripts/go_score_from_bundle.py bundle.json
# veya
python3 scripts/go_score.py --scenario hardest --tam-go-complete --verified
```

→ **P ≥ 30%**, tavan **33%** (`tam-go-floor` / `tam-go-cap`).

Pipeline bitmeden skor düşük kalır (**bilerek**); gönderme yok.

## En zor bağlam tanımı

| Boyut | Değer |
| --- | --- |
| Gönderim | yaş ≤15 dk, teklif ≤8, K1/K2 geçer |
| `--field-bot-heavy` | Bot/şablon yoğun |
| `--client-picky` | hire &lt;30%, 5+ iş (`--allow-picky-client`) |
| Screening | zorunlu + lint PASS |
| 0 yorum, davet yok | |

`--scenario hardest` = yukarıdaki test preset’i.

## Tam GO = tek bayrak

11 ayrı CLI bayrak yerine **`--tam-go-complete`**: pipeline’ın ürettiği her şey (audit, dilim, video, sim T8, M1, chat, fixed offer) tamamlandı demek.

`job_bundle.json` → `tam_go`:

| Alan | Gönderim için |
| --- | --- |
| `complete` | true |
| `audit_report_path` | site_audit çıktısı |
| `slice_evidence` | çalışan dilim |
| `loom_or_video_path` | sessiz video |
| `sim_t8_pass` + `beats_elite` | §13 + T8 |
| `m1_micro_text`, `fixed_offer_line` | §22 |
| `chat_bundle_ready` | §23 hazır |
| `letter` | lint PASS metin |

## CI

```bash
python3 scripts/go_hardest_scenario.py
```

- Planlama (tam GO yok): düşük P — OK.
- `--tam-go-complete`: **≥ 30%** — zorunlu PASS.

Kalibrasyon: gerçek log %30 altında kalırsa kapılar sıkılır, taban şişirilmez (`docs/calibration.md`).
