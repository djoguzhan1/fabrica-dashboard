# GO katmanları (L0–L4) — **bizim** iç operasyon

Bu dosya rakip veya “Upwork standardı” kıyası değil; **fabrica GO hattının** paketleri. Gerçek başarı: `docs/bizim_basari.md` + `go_bizim_ozet.py`.  
`go_score` yüzdeleri = gönderim öncesi **iç EV**; Insights sonucu değil.

## Katman tablosu (aynı ilan, gönderim anı)

| Katman | Tetik | Ek sistem işi | Model P (en zor, validate PASS) |
| --- | --- | --- | --- |
| **L0 plan** | precheck GO | skor taslağı | ~%8 (gönderme) |
| **L1 Standart** | `go_standard.complete` | enrich, lint, kit, M1, chat stub, J1/T8 | **%30–33** |
| **L2 Tam** | `tam_go.complete` | + dilim, audit, Loom, sim beats_elite | **%35–38** |
| **L3 Apex** | `apex_go.complete` | + Uma echo, aktif müşteri, GO+ sinyal, katalog/portföy, 6h edit planı, elite margin | **%40–42** |
| **L4 Davet** | `--invite` | profil/katalog/badge motoru (ayrı kanal) | **%35–45** (soğukla karışmaz) |

%40 hedefi **L3 Apex** = L2 + müşteri/zaman/kanıt zinciri. Davet (L4) ayrı log alanı `kaynak: davet|soğuk`.

---

## “Uçuk” ama uygulanabilir fikirler (tüm sistem)

### 1. Sinyal düzlemi (Signal plane)
Vibeworker / webhook → tek `JOB_BUNDLE` + otomatik `go_client_echo.py` + `go_send_window.py`. İnsan yapıştırmaz; Apex alanları ilan gelirken dolar.

### 2. Kanıt zinciri (Proof graph)
`kit → post_diagnosis → audit → slice → loom` sırası bundle’da `proof_chain[]`. Her adım bir link; letter’da yalnızca **en güçlü 2** (spam yok). Skor: zincir uzunluğu reply/hire delta.

### 3. Uma echo katmanı
Müşterinin ilanından **birebir 3–5 kelime** (araç, sayfa, çıktı) kartın ilk 110 karakterine zorunlu (`go_client_echo.py`). Screening + Shortlist uyumu.

### 4. Zaman nişancısı
`go_send_window.py`: müşteri ülkesine göre **09:00–11:30 yerel** gönderim penceresi. Erken boost + “client active” (`last_viewed < 6h`) Apex kapısı.

### 5. Çift yüzey teklif
Aynı bundle’dan: (A) cover letter, (B) 1 sayfalık “Plan PDF” ekran görüntüsü (primary + M1 tablosu). Hakem: “attachment worth opening?”.

### 6. Screening cevap bankası
`kits/screening_bank/` — 20 kalıp (timeline, similar work, fixed vs hourly). Triage tipine göre `reply_lint` otomatik doldurur → hire aşaması kaybı azalır.

### 7. EV vali (Connect governor)
`estimate_ev.py --min-p 0.40` Apex’ten düşükse boost bid düşür veya SKIP değil **L1’e düş** önerisi. Connect sıkışınca $120–180 + Apex önceliği.

### 8. Karma huni (portföy seviyesi)
Haftalık hedef: tekliflerin ≥%25’si davet/katalog kaynaklı (§22.2.1). Tek ilan P’si değil, **portföy ortalaması** %40’a yaklaşır. Log: `kaynak`.

### 9. 6 saat ikinci darbe
Gönderim sonrası `edit_six_hour_plan` — görülmediyse **yeni bulgu** ile Edit (§19). Apex kapısı: plan metni bundle’da. Açılma hunisi ikinci şans.

### 10. Elite margin
Simülasyonda **3/3 persona** “elit’ten önce hire” + yazılı gerekçe JSON. Tam GO’da “beats_elite”; Apex’te **unanimous** (`elite_margin_unanimous`).

---

## %40’a giden yol (dürüst)

| Adım | Etki |
| --- | --- |
| L1 her GO | taban %30 en zor |
| L2 rekabet/elit ilan | +5 puan bandı |
| L3 Apex (echo + aktif client + GO+ + katalog + 6h plan + unanimous) | +2–4 puan bandı → **%40** model |
| L4 davet payı %40 | portföy ortalaması %40+ |

Kalibrasyon: Apex gönderimlerinde log `tier=apex`; 10 send sonra gerçek hire < %32 ise Apex kapıları sıkılır, taban düşürülür.

## Komutlar

```bash
python3 scripts/go_client_echo.py --title "..." < post.txt
python3 scripts/go_send_window.py --country US
python3 scripts/go_hardest_scenario.py   # L1/L2/L3
```
