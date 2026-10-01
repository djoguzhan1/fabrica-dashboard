# GO orchestration — Composer 2.5 tek sohbet

Tam referans: `docs/upwork-strategy.md` §12, §21, §23. Prompt dosyaları: `prompts/`.

## Tetik

```text
GO. Model seti §12.0. Max 3 tur.
[ilan metni veya screenshot]
Boost: B1=… B2=… B3=… B4=…
Activity: interviewing … invites …
Müşteri: ülke, spent, hire%, ödeme doğrulandı mı
```

## Adım 0 — yapısal (teklif sayısı yok)

```bash
python3 scripts/go_precheck.py --budget 100 --payment-verified \
  --title "..." --description-file /tmp/post.txt \
  --ongoing --interviewing 0 --invites 0 --b4-plus-one 27
```

`SKIP` → Connect 0, model yok.

## Adım 1 — skor bandı

```bash
python3 scripts/go_score.py --age 12 --proposals 3 --budget 100 --verified \
  --boost-top4 --scope-clear --demo-match exact --prework strong
```

`proposals` varsayılan 3 = erken bildirim varsayımı; **band teklif sayısıyla seçilmez**.

## Adım 2 — paralel ön-iş (§21.1)

Task + `prompts/researcher.md` → Task builder → Task visual → birleşir JOB_BUNDLE.

## Adım 3 — yaz → lint

```bash
python3 scripts/proposal_lint.py letter.txt \
  --must "term1,term2" \
  --card-must "primary1" \
  --ban-in-card "LCP,PageSpeed" \
  --title "Job title" --check-links
```

## Adım 4 — hakemler paralel

`prompts/judge1_terra.md` + `prompts/judge2_gemini.md` + cards §13.

## Adım 5 — T8 → gönder + boost B4+1

Log (Ek B): `b4_at_send`, `budget_band`, `band`, `primary_deliverable`.

## İhtimal kaldıraçları (sistem içi, güncel)

| Kaldıraç | Etki (son aşama / toplam) |
| --- | --- |
| `tam-paket` + boost ilk 4 | ~%28–32 teklif → işe alım |
| En zor + Standart GO | **%30–33** (`docs/go_standard.md`) |
| En zor + Tam GO | **%35–38** (`docs/hardest_scenario.md`) |
| `--chat-ready` (§23 metin hazır) | hire +~4 puan |
| İyi müşteri (hire ≥70%, spent ≥$100) | hire +~5 puan |
| `standart` paket | ~%16–22 |
| Yapısal SKIP (precheck) | %0 — model çalışmaz |

Kalibrasyon: her 10 gönderimde log → `go_score` ağırlıkları elle ince ayar (§17).

## SOHBET tetik

```text
SOHBET
[müşteri mesajı + konuşma]
```

`prompts/chat_triage.md` → writer → `reply_lint.py --stage …`
