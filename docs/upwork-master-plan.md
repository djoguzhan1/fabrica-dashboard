# Upwork ana plan — %20 hedefi (tek kaynak)

**Son güncelleme:** 2026-09-28 · **Bağlayıcı doküman budur.** Diğer Upwork dokümanlarıyla çelişki olursa **bu geçerlidir**.

| Eski doküman | Artık ne için |
| --- | --- |
| `upwork-proposal-strategy.md` | Teklif şablonları (P0–P4), kapanış cümleleri, risk matrisi detayı |
| `vibeworker-presets.md` | Yapıştırmaya hazır filtre JSON’ları |
| `upwork-vibeworker-pro-setup.md` | Vibeworker kurulum ekranları |
| `upwork-job-alerts-setup.md` | Q1–Q20 arama sorguları. **Bütçe / boost bölümleri (§7.1–7.5) geçersiz → bu doküman** |
| `upwork-proposal-log.md` | Takip tablosu (sütunlar §9’a göre) |

---

## 1) Hedef

| Metrik | Piyasa ortalaması | **Hedef** |
| --- | --- | --- |
| Teklif açılma | %40–50 | **%70+** |
| Açılan → cevap | %10–20 | **%35–50** |
| **Hire / teklif** | %2–4 | **%12–20** |

%20’ye götüren 4 kaldıraç (hepsi şart, biri eksikse oran düşer):

1. **Görünürlük** — teklif müşterinin ilk ekranında olmalı (hız veya boost). Görünmeyen teklif %0’dır.
2. **Seçicilik** — kazanılamayacak ilana teklif yok (§4 REKABET kartı).
3. **Teklif kalitesi** — mini denetim + 150–220 kelime + tek soru (§6).
4. **Kapanış** — 5 dk içinde cevap, 24/48 saat takip (§7).

**Temel ilke:** Görünmeyeceksen teklif atma. Connect’i kalabalığa değil, görünür olacağın ilana harca.

---

## 2) Bütçe — 600 Connect sprinti

| Havuz | Connect | Kural |
| --- | --- | --- |
| **Teklif havuzu** | **~480** | ~10–11 Connect/teklif → **~45 teklif** |
| **Boost sandığı** | **120** | Ayrı say. Aynı anda **en fazla 120** kilitli (§5) |

- **Tempo:** günde **8 GO** (en fazla 10, kalite düşmeyecekse) → **5–6 gün** agresif sprint.
- **Sprint sonu tahmini (garanti değil):** ~45 teklif × %9–11 → **4–5 iş**. %20’ye ulaşılırsa **~9 iş**.
- **Takviye:** Sandık boost’a yetmezse **teklif sayısını azalt**, boost’tan kısma. Daha çok hacim istersen **+300 Connect** teklif havuzuna eklenir.

---

## 3) İlan akışı ve saatler

**Kaynak:** Vibeworker Pro P1–P5 push (JSON: `vibeworker-presets.md`), P6 sadece feed, Plus kayıtlı aramaları yedek. Shortlist çanı P1–P5 kurulunca **kapalı**.

**Beklenti:** 10–30 push/gün → %25+ GO adayı → REKABET kartı sonrası **5–10 gerçek GO**.

| TR saati (GMT+3) | Yoğunluk | Ne yap |
| --- | --- | --- |
| 01:00–09:00 | Çok az | Sessiz saat (uyu) |
| 09:30–10:00 | Az | Gece ilanlarına bak (60 dk’dan eskiyse SKIP) |
| **11:00–13:00** | Orta (UK + erken US) | Av bloğu 1 |
| **15:00–22:00** | **En yoğun** (US Doğu iş günü) | **Av bloğu 2**, telefon açık |
| 22:00–00:30 | Orta-az (US Batı) | Sadece taze ve iyi ilan |

Pazartesi en yoğun gün; Pazar 18:00 sonrası küçük bir artış olur.

**Kalibrasyon (ilk 48 saat):** push <5/gün → rating 4.5 ve spent $500 eşiğini gevşet. Push >40/gün ve çoğu alakasız → exclude listesine kelime ekle.

---

## 4) REKABET kartı — GO / SKIP (teklif yazmadan önce, 30 sn)

İlan sayfasından oku:

- **Yaş** (dakika) ve **teklif sayısı**
- **Hız** = teklif ÷ max(yaş_dk, 5)
- **Boost tablosu** — teklif ekranının altında: ilk 4 slotun bid’leri ve 1. sıra fiyatı

**Önce ön eleme (her ilan):** blacklist, bütçe <$50, Tier dışı, özel eklenti, uzmanlık gerektiren stack, 0 hire + <$50 müşteri → **SKIP**.

**Karar tablosu (ilk tutan satır geçerli):**

| # | Koşul | Karar |
| --- | --- | --- |
| K1 | Teklif **≥20** veya yaş **>60 dk** | **SKIP** |
| K2 | Hız **>1,0/dk** (ör. 15 dk’da 15+ teklif) | **SKIP** |
| K3 | **$80+** Tier-1 ve **4. sıra bid’i ≤14** | **Teklif + boost** (§5) |
| K4 | **$80+** Tier-1 ve 4. sıra bid’i **≥15** | Yaş <10 dk ve teklif <5 ise boost’suz teklif; aksi **SKIP** |
| K5 | **$50–79**, yaş **<15 dk**, teklif **<5** | Teklif, **boost yok** |
| K6 | **$50–79**, diğer her durum | **SKIP** |

**Sert kural:** $80+ ilanda boost yapamıyorsan veya yapmıyorsan, sadece **taze (<10 dk) ve boş (<5 teklif)** ilana teklif atılır. Kalabalık + boost yok = **SKIP**.

---

## 5) Boost — doğru model (Upwork resmi kuralları)

### 5.1 Nasıl çalışıyor (doğrulanmış)

Kaynak: Upwork Help — *Boost your proposal*, *When and what will I be charged?*, *Can I boost my proposal again?*

| Kural | Anlamı |
| --- | --- |
| Açık artırma, **ilk 4 slot** | En yüksek 4 bid müşterinin listesinin en üstünde, “Boosted” etiketiyle görünür |
| Açık artırma **7 gün** veya hire’a kadar sürer | Sonradan gelen biri seni geçebilir |
| **Ücret sadece iki durumda:** müşteri boost’luyken etkileşime girerse **veya** açık artırma bittiğinde hâlâ ilk 4’teysen | Görünürlük işe yaradıysa ödersin |
| **Geçilirsen ve etkileşim yoksa → boost Connect’i iade** | Kaybeden boost’un maliyeti ~0 (teklif Connect’i iade edilmez) |
| Boost **sadece gönderimde, tek sefer**; bid **sonradan artırılamaz** | Doğru bid’i ilk seferde ver |
| Boost şu durumlarda biter: müşteri etkileşime girer, 3 kez açıp işlem yapmaz, 5 kez görüp etkileşime girmez veya geçilirsin | Kısa ama yoğun bir görünürlük penceresi |
| Min bid = **4. sıra + 1** | Tablo gönderim öncesi görünür |
| Bazı ilanlar **placebo** (boost gösterilmez, Connect alınmaz) | Ölçüm gürültüsü; sorun değil |

### 5.2 Bunun plana etkisi (eski planın hataları)

| Eski kural | Neden yanlış | Yeni kural |
| --- | --- | --- |
| “<10 dk ilanda boost faydasız” | Taze ilanda bid en ucuz halinde; kalabalık sonra gelir ve boost’suz teklif aşağı iner | **Tier-1 $80+ ilanda taze de olsa boost** |
| “Bid = 1. sıra + 1, max 10–12” | Düşük bid geçilir → iade edilir ama görünürlük de kaybolur; bid sonradan artırılamaz | Kalıcı olmayı hedefleyen bid (§5.3) |
| “Sprintte max 3 / 8 / 12 boost” | Kaybeden boost iade edildiği için sayı değil **kilitli Connect** sınırlı | **Aynı anda en fazla 120 Connect kilitli** |
| “Boost pahalı, az kullan” | Sadece işe yarayınca (etkileşim) ödüyorsun | Kaldıraç 1’in ana aracı → **K3’te varsayılan açık** |

### 5.3 Bid formülü

```
B1 = 1. sıra bid, B4 = 4. sıra bid (tablodan)

Hedef bid = max(B1 + 1, 6)    → 1. sıraya otur, geç gelenlere karşı pay bırak
Tavan     = bütçeye göre:
            $80–99   → 12
            $100–199 → 15
            $200+    → 20
Hedef bid > tavan ise:
            B4 + 1 ≤ tavan → bid = tavan (ilk 4’te, 1. değil)
            B4 + 1 > tavan → boost yok → K4
```

**Neden 1. sıra:** Sonradan gelen biri seni geçerse 4. sıradaki düşer, 1. sıradaki kalır. Kaybedersen zaten iade alırsın. Kaybetmenin maliyeti para değil, **görünürlük**.

**Maliyet tavanı:** teklif + boost ≤ iş bedelinin **~%15’i**. Örnek: $100 iş → 11 + 15 = 26 Connect ≈ $3,90 (%3,9). Bu yüzden tavanlar güvenli.

### 5.4 Sandık yönetimi (nakit akışı)

- Boost Connect’i **7 güne kadar kilitli** kalabilir (etkileşim yoksa ve hâlâ ilk 4’teysen açık artırma sonuna kadar), iadeler açık artırma kapanınca gelir.
- **Aynı anda kilitli boost toplamı ≤120.** Doluysa yeni boost yok → K4’e göre davran.
- Sandık <30 → sadece **$100+** ilanlara boost.
- Günlük log: `Boost bid`, `Sonuç` (ödendi / iade / hâlâ açık).

### 5.5 Haftalık boost kontrolü

| Gözlem | Ayar |
| --- | --- |
| Boost’lu tekliflerde açılma **<%50** | Sorun teklifin ilk 2 cümlesinde. Boost’u kısma, **açılışı değiştir** |
| Boost’lu açılma iyi, cevap **<%20** | Sorun gövdede (denetim/ek). Strateji Bölüm 3–5 |
| Çoğu boost **geçildi/iade** | Tavanı bir kademe yükselt ($100–199 → 18) |
| Nişte B4 sürekli **≥15** | O preset’te min bütçeyi **$100**’e çek |

---

## 6) Teklif kuralları (her GO’da, istisnasız)

- **150–220 kelime.** Göndermeden önce kelime sayısını kontrol et.
- **Tek soru**, **tek link**, **en fazla 3 madde işareti**. Detay ekte.
- İlk cümle: onların kelimesi veya site/ürün adı. “Hi” veya “I” ile başlama.
- Mini denetim: siteye gerçekten bakılmış 2–3 bulgu.
- Uydurma deneyim yok; 0 review cümlesi tek satır ve dürüst.
- Fiyat ≤ bütçe; bütçe düşükse **scope’u** küçült.
- Şablonlar ve kapanış metinleri: `upwork-proposal-strategy.md` Bölüm 5, 10.
- Model: teklif metni için **Claude Opus 5.5 Low**; hızlı GO/SKIP için **Composer 2.5**.
- Kurala uymadıysan log’a yaz (sessiz sapma yok).

---

## 7) Günlük akış

1. Push gelir → ön eleme (§4).
2. **REKABET kartı** → K1–K6.
3. GO ise: denetim 5–10 dk → teklif (§6) → **boost kararı ve bid gönderim ekranında** (§5.3).
4. Gönder → log satırı.
5. Cevap gelirse **5 dk içinde** yanıt; yoksa 24 saat sonra 1 yeni bulguyla takip, 48 saat sonra kısa kapanış.
6. Gün sonu 5 dk: T+24h dolan tekliflerde Insights (açıldı mı, teklif sayısı) → log.

---

## 8) Haftalık ayar (15 dk)

`upwork-proposal-log.md` → haftalık özet. Son 7 günde **≥5 GO** yoksa ayar çekme, önce hacmi artır.

| Gözlem | Ayar |
| --- | --- |
| GO anında ort. teklif **≥10** | Bildirim geç geliyor: pil tasarrufu, 15:00–22:00 telefon, `posted_within_hours` 12 |
| Boost’suz tekliflerde açılma **<%25** | Boost’suz teklifi sadece yaş <5 dk ise at |
| Açılma **≥%70**, hire **<%10** | Sorun kapanışta: 5 dk cevap, milestone metni, fiyat/scope |
| Hire **≥%15** | Hacmi artır (+Connect), kurallara dokunma |

Her ayarı **en fazla 5 gün** dene; kötüleşirse geri al.

---

## 9) Log sütunları

`# · Tarih · İlan · Tier · Bütçe · Yaş · Teklif · Hız · B1/B4 · Karar (K#) · Boost bid · Boost sonucu · Kelime · Ek · T+24h (açıldı/teklif) · Cevap · Hire · Not`
