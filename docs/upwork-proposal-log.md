# Upwork teklif takip tablosu

**Kurallar:** `docs/upwork-master-plan.md` (tek kaynak). Sprint: **600 Connect** = ~480 teklif + **120 boost sandığı** (aynı anda en fazla 120 kilitli). Karar K1–K6, bid formülü §5.3.

Sütunlar 72h planı Ek A’dan + rekabet (`docs/upwork-job-alerts-setup.md` §7.5). Her teklifi gönderdikten hemen sonra bir satır ekle; **T+24h** Insights → `Rekabet (T+24h)`; cevap / interview / offer geldikçe aynı satırı güncelle.
Haftalık 5 dk: açılış/cevap → `docs/upwork-proposal-strategy.md` Bölüm 12. Haftalık 15 dk: **Haftalık rekabet özeti** + §7.5 D ayar çek.

| # | Tarih (GMT+3) | İlan | Tier | Tip | İlan yaşı (GO) | Teklif (GO) | Hız (/dk) | 1. sıra | Bütçe | Verilen fiyat | Connects | Boost bid | Şablon | Model | Kelime | Denetim / ek | Rekabet (T+24h) | Cevap | Interview | Offer | Contract | Not |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-09-28 04:43 | Build n8n SEO Content Generation Workflow | 3 | Fixed | 7 dk | <5 | ~0,1 | — | $40 | $40 | 11 | yok | özel (n8n) | Opus 5 Low | 292 | node map PNG | 22 prop, 18 unopened, 0 msg (Insights) | — | — | — | — | **R7/R2 uyarısı:** $40, boost yok; sonradan kalabalık. Sonraki: §7.5 R1–R9. Müşteri: Kanada, 4.9★, %58 hire, $2,1k / 51 hire. |

## Kural sapmaları (haftalık ölçümde ayır)

| # | Sapma | Kural | Sonraki teklifte |
| --- | --- | --- | --- |
| 1 | 292 kelime | 150–220 (Bölüm 5) | Node dökümü eke, mektupta 3 madde |
| 1 | 2 soru soruldu | Tek akıllı soru (Bölüm 5, blok 6) | Tek soru |
| 1 | 7 madde işareti | En fazla 3 (Bölüm 6) | 3 madde |

## Boost sandığı (savaş cephesi)

Kurallar: `upwork-master-plan.md` §5. Bid = max(B1+1, 6), tavan $80–99 → 12 · $100–199 → 15 · $200+ → 20. Geçilirsen iade gelir; aynı anda kilitli ≤120.

| # | Tarih | İlan | Bütçe | B1 / B4 | Boost bid | Durum (açık / ödendi / iade) | Kilitli toplam (≤120) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | **0** |

## Haftalık rekabet özeti (§7.5 D — 15 dk)

Hafta: `____` · GO teklif sayısı: `__`

| Metrik | Bu hafta | Not / eşik |
| --- | --- | --- |
| GO’da ort. teklif sayısı (gönderim anı) | | Hedef: &lt;10; ≥12 → bildirim hızı |
| GO’da ort. hız (teklif/max(yaş,5)) | | &gt;0,8 → min bütçe +10 |
| T+24h açılma oranı (açılan/GO) | | &lt;15% → SKIP eşiği 15 teklif |
| Boost kullanılan iş → mesaj oranı | | 0% 2 hafta → sadece bant A boost |
| Ort. 1. sıra (boost baktığın işler) | | ≥13 sürekli → connects_max 10 |
| **Bu hafta çekilen ayar** | | Örn. “R1: ≥15 SKIP” |

## Bekleyen aksiyonlar

- **İlan 1:** 24 saat cevap yoksa follow-up (strateji Bölüm 10). Cevap gelirse önce erişim listesi: n8n (cloud/self-hosted), Sheet, müşterinin LLM anahtarı, WordPress application password. Milestone fonlanmadan başlama.
