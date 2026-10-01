# Bizim sistem başarısı (tek ölçüt)

**Başarı = Upwork Insights + Ek B log’undaki gerçek sonuçlar.**  
`go_score` içindeki %30 / %38 / %42, başkalarının “standartı” değil; **bizim hattın o gönderimde ne kadar hazır olduğuna** bağlı **iç tahmin** (Connect harcamadan önce EV hesabı). Gerçek başarıyı o yüzdeler tek başına tanımlamaz.

## Ne sayılır, ne sayılmaz

| Sayılır (bizim başarı) | Sayılmaz |
| --- | --- |
| Ek B: **açıldı / cevap / işe alım** (satır satır) | Rakip teklif sayısı, “piyasa ortalaması” |
| Sohbet log: **mesaj → offer** oranı (§23, hedef ≥%60) | Upwork’teki başka freelancer JSS |
| Haftalık: **işe alım ÷ GO** (Connect harcanan gönderim) | Simülasyon PASS = işe alım sanmak |
| `precheck SKIP` → Connect **0** (doğru eleme) | Model P’si yüksek diye gönderim saymak |
| Davet + Catalog kanalı (ayrı `kaynak`) | Başkasının “standart GO” tanımı |

## Hedefler (bizim plan, §12 / §22 / Ek B)

| Metrik | İlk faz (0 yorum) | Sistem iyileşince |
| --- | --- | --- |
| GO → **açılma** (T+24h) | ≥%50 | ≥%70 |
| Açılan → **cevap** | ≥%35 | ≥%50 |
| Cevap → **işe alım** | ≥%45 | ≥%60 |
| **GO → işe alım** | ≥%12 (10’da ~1–2) | ≥%20 |
| Sohbet → **offer** | ≥%50 | ≥%60 |

10 gönderimde **2 işe alım** = başarı; kalibrasyon `docs/calibration.md`.

## İç paketler (operasyon adı — rekabet kıyası değil)

| Kod | Anlam | Bizim hatta zorunlu olan |
| --- | --- | --- |
| **paket-min** | `go_standard.complete` | lint, M1, kit, chat stub, judge1/T8 |
| **paket-tam** | `tam_go.complete` | + dilim, audit, Loom, sim beats_elite |
| **paket-apex** | `apex_go.complete` | + echo, aktif client, GO+, 6h edit, elite 3/3 |

Ek B’ye her gönderimde yaz: `tier=paket-min|paket-tam|paket-apex`, `validate_pass`, `system_p_at_send` (skor çıktısı).

**Başarı sorusu:** “Bu paketle gönderdik; Insights ne dedi?” — skor sadece “bu paketi bitirdik mi?” sözleşmesi.

## Haftalık rutin (5 dk)

```bash
python3 scripts/go_bizim_ozet.py docs/proposal_log.tsv
```

Çıktı: bizim açılma / cevap / işe alım / kayıp aşaması (`loss_stage`). Sim ile gerçek uyumu <%70 ise prompt/panel değişir (§17), `go_score` ağırlığı değil önce metin ve ön-iş.

## %40 bizim sistemde ne demek?

- **Tek soğuk teklif:** `paket-apex` + validate = iç model **%40–42** (EV için); gerçek işe alım yine Ek B ile ölçülür.  
- **Portföy:** soğuk + davet/katalog karışımıyla haftalık **GO→işe alım** %20+ (§22.2.1) — asıl “sistem başarısı”.

Özet: **Başkalarının standardını takip etmiyoruz; kendi log’umuz, kendi hattımız, kendi hedef tablomuz.**
