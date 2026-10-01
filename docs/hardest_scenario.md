# En zor tam GO senaryosu (ölçülebilir)

Amaç: **Connect harcandığında** tam §21/§22 hattının, soğuk teklif + zor müşteri + bot-yoğun saha + screening + elit rakip simülasyonunda **en az %30 teklif → işe alım** hedefini **kanıtlanabilir artefaktlarla** desteklemek. Bu tablo “iyi his” değil; her kaldıraç bir bayrak + dosya.

## Tanım: “en zor” (gönderim anı)

| Boyut | Değer | Not |
| --- | --- | --- |
| Zaman | yaş ≤ 15 dk, teklif ≤ 8 | K1/K2 geçer; erken boost |
| Rakip saha | `--field-bot-heavy` | Bot/şablon yoğun; teklif sayısı band seçmez |
| Müşteri | hire rate &lt; %30, 5+ iş | Precheck: varsayılan SKIP; **`--allow-picky-client`** + tam yığın zorunlu |
| Screening | `--screening-required` | `screening_extractor` + lint PASS |
| Biz | 0 yorum, davet yok | Taban hire freni |
| Paket | tam-paket yapısı | boost ilk 4, strong ön-iş, exact demo, scope net, interviewing 0, invites &lt; 5 |

Peak’te 25+ teklif **bu senaryo değil** (K1 SKIP veya `--competition-applied` sonradan açılma düşürür; tam GO gönderim anında yapılır).

## Tam yığın (11 kapı) — hepsi TRUE olmadan %30 floor yok

| # | Bayrak | Kanıt |
| --- | --- | --- |
| 1 | `--boost-top4` | B4+1 tavan altında |
| 2 | `--prework strong` + `--demo-match exact` + `--scope-clear` | JOB_BUNDLE primary net |
| 3 | `--audit-findings` | `site_audit.mjs` → somut bulgu kartta |
| 4 | `--slice-delivered` | Builder: müşteri varlığında çalışan dilim (§21.1) |
| 5 | `--sim-t8-pass` | §13 panel: ≥2 persona açar, `beats_elite`, T8 PASS |
| 6 | `--letter-screening-pass` | `proposal_lint.py` screening |
| 7 | `--profile-highlights` | İlana uygun 1–2 highlight seçildi |
| 8 | `--m1-micro` | Mektup + §23: $20–40 / 24h M1 metni |
| 9 | `--chat-ready` | `reply_lint.py` first/interview hazır |
| 10 | `--fixed-offer-ready` | §21.2 sabit fiyat + milestone cümlesi |
| 11 | `--reply-under-10m` | SOHBET hattı ≤10 dk (log) |

Meta: `--tam-stack` → yukarıdakilerin hepsi; eksikse stderr’de liste, floor uygulanmaz.

## Huni hedefi (en zor + tam yığın)

§22.1’den türetilmiş **taban** (floor, sadece 11 kapı açık):

| Aşama | En zor taban | Normal tam GO taban |
| --- | --- | --- |
| open | **73%** | 80% |
| reply | **58%** | 60% |
| hire | **71%** (picky: **70%**) | 70% |
| **P** | **≥ 30%** (tavan **33%**, §22 dürüst) | ~33% |

- `p_raw < 30%` → floor: `max(hesaplanan, taban huni)`.
- `p_raw ≥ 30%` → cap **33%** (aşırı bonus birikimini engeller).

Kalibrasyon: `docs/calibration.md` — gerçek log %30 altına düşerse taban veya kapılar güncellenir.

## Komutlar

```bash
# Ölçüm + CI floor
python3 scripts/go_hardest_scenario.py

# Tek ilan
python3 scripts/go_score.py --scenario hardest --tam-stack \
  --audit-findings --slice-delivered --sim-t8-pass --m1-micro \
  --profile-highlights --fixed-offer-ready --reply-under-10m \
  --letter-screening-pass --chat-ready
```

Precheck (picky):

```bash
python3 scripts/go_precheck.py --budget 130 --payment-verified \
  --allow-picky-client --age-minutes 12 --proposals 6 \
  --client-hire-rate 26 --client-hires 12 ...
```

## Dürüstlük sınırı

%30 **yalnızca** 11 kapı + simülasyon PASS ile modellenir. Eksik dilim, elit’i geçemeyen panel veya screening FAIL → floor yok; P hesaplanan huni (genelde %12–22 en zorda).

Davet kanalı ayrı şerit (~%35+); bu doküman **soğuk tam GO** içindir.
