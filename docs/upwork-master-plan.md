# Upwork ana plan — %20 hedefi (tek kaynak)

**Son güncelleme:** 2026-09-28 · **Bağlayıcı doküman budur.** Diğer Upwork dokümanlarıyla çelişki olursa **bu geçerlidir**.

| Eski doküman | Artık ne için |
| --- | --- |
| `upwork-proposal-strategy.md` | Teklif şablonları (P0–P4), kapanış cümleleri, risk matrisi detayı |
| `vibeworker-presets.md` | Yapıştırmaya hazır filtre JSON’ları |
| `upwork-vibeworker-pro-setup.md` | Vibeworker kurulum ekranları |
| `upwork-job-alerts-setup.md` | Q1–Q20 arama sorguları ve araç kurulumu (eski bütçe/boost bölümleri kaldırıldı) |
| `upwork-arena-strategy.md` | Cevap tarafı: 1. parti boost/Uma bulguları, müşteri eleme aşamaları, 12 maddelik ikna listesi, ön-kontrol, Catalog |
| `upwork-opening-playbook.md` | 2. parti bulgular: "önce yap, sonra teklif et", ön-iş menüsü, A1–A6 açılışlar, 10/10 açılış testi |
| `upwork-competitor-cards.md` | Simülasyon için gerçekçi rakip kartları (bot, şablon veteran, ajans, ucuz, elit) ve tek çağrılık hakem prompt'u |
| `upwork-proposal-log.md` | Takip tablosu (sütunlar §9’a göre) |
| `upwork-72h-first-job-plan.md` (dal `cursor/upwork-72h-plan-5f90`) | Arşiv. EV, bütçe ve boost kuralları **geçersiz**; sadece arka plan |

---

## 0) Nihai kararlar — her kural %20’ye nasıl katkı yapar

%20 = **açılma × cevap × kapanış** çarpımı: 0,70 × 0,45 × 0,50 ≈ **%16**; iyi haftada 0,75 × 0,50 × 0,55 ≈ **%20**. Her karar bu üç çarpandan birini büyütür.

| # | Karar | Çarpan | Eski / kafa karıştıran | **Nihai** |
| --- | --- | --- | --- | --- |
| 1 | Görünmeyeceksen teklif atma | Açılma | Kalabalık ilana boost’suz teklif atılıyordu ($40 n8n, 22 teklif) | K1–K6: kalabalık → boost veya **SKIP** |
| 2 | $80+ Tier-1’de boost **varsayılan** | Açılma | “Boost pahalı, sprintte 3/8/12 kez” | Kaybeden boost iade edilir; sınır **kilitli ≤120**, sayı değil |
| 3 | Taze ilanda da boost | Açılma | “<10 dk boost faydasız” | Yanlıştı; müşteri erken bakar, boost o an işe yarar |
| 4 | **Sabit boost:** 50→11, 80–99→15, 100→20, 200→30; **≤15 dk** | Açılma | Düşük tavan / boost’suz | Erken dakika + sabit bid; B4+1 > bid → SKIP |
| 5 | Taban **$50** | Cevap/kapanış | $15–49 “yalın GO” bantları | ≤$49 **SKIP** (istisna yok) |
| 6 | Hız >1/dk → SKIP | Açılma | Sadece “<20 teklif” bakılıyordu | Yaş + hız birlikte |
| 7 | 150–220 kelime, tek soru, ≤3 madde | Cevap | İlk teklif 292 kelime, 2 soru, 7 madde | İstisnasız; sapma log’a |
| 8 | Mini denetim + ek her GO’da | Cevap | Bazen atlanıyordu | Zorunlu |
| 9 | 5 dk cevap, 24/48h takip | Kapanış | Yoktu / dağınıktı | §7 akış |
| 10 | Haftalık tek ayar, 5 gün dene | Hepsi | Aynı anda çok değişiklik | §8 tablo |
| 11 | **Faz 1:** Connect’e günlük tavan yok | Hacim | “600 = 45 teklif” kotası | K1–K6 GO → at; bakiye bitene veya §2.3 **DUR**’a kadar |
| 12 | **Faz 2:** 3. gün / 2 hire sonrası tempo düş | Hacim | Sabit 8 GO/gün | Teslim + nakit akışına göre 4–8 GO |

**Silinenler:** `upwork-job-alerts-setup.md` eski §7.1–7.5 (bant A/B/C, 3/8/12 boost, R1–R9) tamamen kaldırıldı. Geçerli tek karar tablosu **§4 K1–K6**, tek boost kuralı **§5**.

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

## 2) Bütçe — agresif mod (Connect kotası yok, kalite kotası var)

**Kaldırılan:** “600 Connect = en fazla ~45 teklif / günde 8 GO” — **yok**.  
**Kalan:** K1–K6, §6 teklif kalitesi, $50 taban, boost tavanı. Koşulu sağlayan ilana **bakiye yettiği sürece** teklif + (K3’te) boost.

### 2.1 Başlangıç (ör. 600 Connect)

| Havuz | Connect | Not |
| --- | --- | --- |
| **Boost için ayrı say** | **≥120** | Muhasebe; K3’te tavan bid harcanır. Kilitli boost toplamı pratikte **≤120** tut (7 gün kilit riski); yetmezse Connect al, tekliften çalma |
| **Teklif + ek boost** | Geri kalan | ~10–11 Connect/GO; K3’te +12…20 |

**600 Connect kabaca 3 gün agresif** (günde ~10–15 GO + çoğu $80+ boost): teklif ~110–165 Connect/gün bandı mümkün; boost’un önemli kısmı **iade** gelir, net tüketim daha düşük. 3. gün sonunda **durum değerlendir** (§2.3).

### 2.2 Faz 1 — ilk 3 gün (veya ilk 2 hire’a kadar, hangisi önce)

| Kural | Değer |
| --- | --- |
| Günlük GO tavanı | **Yok** — peak saatlerde **10–15 GO** hedefle (kalite düşerse dur) |
| Hangi ilan | Sadece **K1–K6 GO**; Shortlist gürültüsü SKIP |
| Boost | $80+ Tier-1, K3 → **bid = tavan** (§5.3) |
| Paralel teslim | **≤2 aktif sözleşme**; 3. hire gelmeden yeni GO’yu **6/gün**’e indir |

**Beklenti (garanti değil):** 3 günde **~25–40 GO** → %10–15 hire → **3–6 iş** başlangıcı; review akışı 1. hafta içinde.

### 2.3 DUR — ne zaman yavaşla veya Connect al

| Sinyal | Aksiyon |
| --- | --- |
| **Gün 3 bitti** | Log: GO, açılma, mesaj, hire. Hire **≥2** → Faz 2. Hire **0** ve açılma **<%30** → teklif metni, hacmi 1 gün **durdur** |
| Bakiye **<80** Connect | Dur veya **+200–400** al; boost kilitlerini say |
| **≥15 GO**, açılma **<%20** | Hacim artırma; §6 + açılış A/B |
| **≥2 hire** aynı anda aktif | Yeni GO **≤6/gün** (teslim öncelik) |
| İlk **funded milestone** | Kutla; Faz 2’ye geçmeyi düşün |

### 2.4 Faz 2 — “birkaç iş aldık, duruma bakarız”

- Tempo: **4–8 GO/gün** (teslime göre).
- Boost: aynı K3; sandık <30 → sadece **$100+**.
- Connect: kazançtan veya kasadan **sürdürülebilir** seviye (~150–250/hafta teklif hacmi); yine **günlük kota yok**, sadece K + DUR.

**Özet:** Agresif = **seçici olmayı bırakmıyoruz**, **yapay teklif tavanını bırakıyoruz**. Bütçe 3 gün yetiyorsa full gaz; sonra metrikle karar.

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
| K3 | **$80+** Tier-1, **B4+1 ≤ cap** ve **B1 ≤ cap** (§5.3) | Teklif + **boost = B4+1** (≤ cap) |
| K4 | **$50–79** Tier-1/2, **B4+1 ≤ 11**, **B1 ≤ 11** | Teklif + boost **11** veya **B4+1** |
| K5 | **B4+1 > cap** veya **B1 > cap** (balina) | **SKIP** — Connect **0** |
| K6 | **≤$49** veya Tier dışı | **SKIP** |

**Sert kural:** $80+ **boost’suz yok**. **1. sırayı kovalama** (B1=100 → SKIP). **4’e girebiliyorsan** (B4+1 ≤ cap) → gir; rekabet sonra artar, bid artıramazsın — o yüzden gönderim anındaki tablo **tek şans**.

---

## 5) Boost — güncel model (Upwork resmi, 2026 — araştırılmış)

**Kaynaklar (bağlayıcı mekanik):**
- [Boost your proposal](https://support.upwork.com/hc/en-us/articles/4406395531795-Boost-your-proposal)
- [When and what will I be charged?](https://support.upwork.com/hc/en-us/articles/40444950584083-When-and-what-will-I-be-charged)
- [Can I boost my proposal again?](https://support.upwork.com/hc/en-us/articles/40445096920851-Can-I-boost-my-proposal-again-or-update-it)

### 5.1 Mekanik (kısa, doğru)

| Konu | Upwork’ün dediği | Plan kararı |
| --- | --- | --- |
| **Ne satın alıyorsun** | İlk **4** teklif slotu (⚡ Boosted); müşteri listesinin üstü | K3’te $80+ Tier-1 → **hedef bu 4 slot** |
| **Süre** | Açık artırma **7 gün** veya işe hire | Boost Connect **günlerce kilitli** kalabilir; Faz 1’de bakiyeyi say (§5.4) |
| **Toplam harcama (gönderim)** | **Teklif Connect + boost bid** (ekran altta toplamı gösterir) | Log’a ikisini ayrı yaz |
| **Ne zaman **ücret** kesilir** | (1) Boost’luyken müşteri **uygun etkileşim** **veya** (2) açık artırma bittiğinde hâlâ **ilk 4**’teysen | Mesaj gelmese de 7 gün sonunda 4’te kalırsan **ödersin** — tavan bid bunun için |
| **Ne zaman iade** | İlk 4’ten **düşürüldün** ve uygun etkileşim **yok** → boost Connect iade (açık artırma kapanınca) | Geçilmek **para kaybı değil**; **görünürlük kaybı** + teklif Connect gider |
| **Bid sonrası** | Boost **bir kez**; bid **artırılamaz**; geçilirsen **yeniden boost yok** | **Asla** “sonra boostlarım” — K3’te gönderimde boost |
| **Sonra boost ekleme** | Yardım metinleri çelişkili; güvenli yol: **ilk gönderimde boost** | Boost’suz gönderip sonra eklemeye **güvenme** |
| **Boost biter** | Etkileşim; 3× açılıp işlem yok; 5× görülüp etkileşim yok; **geçilme** | Erken müşteri bakışı = boost süresi kısalır |
| **Min bid** | **4. sıra + 1** Connect | B4+1 > **sabit bid** → K5 SKIP |
| **Uygunluk** | Upwork eşleşmeye göre boost seçeneği göstermeyebilir | Seçenek yoksa K4 (taze boost’suz veya SKIP) |
| **Placebo** | Bazı ilanlarda boost müşteriye gitmez, Connect alınmaz | Sayma; normal |

**Unutma:** Rekabet **canlı ve 7 gün açık** — sen teklif attıktan **sonra** da biri 28 veya **100** bid atabilir; sen **artıramazsın** (iade veya ödeme). “Erken = güvende” **yanlış**; **güvence = gönderim anında tablo hâlâ bid’in altında** (§5.7).

### 5.2 Bunun plana etkisi (eski planın hataları)

| Eski kural | Neden yanlış | Yeni kural |
| --- | --- | --- |
| “<10 dk ilanda boost faydasız” | Taze ilanda bid en ucuz halinde; kalabalık sonra gelir ve boost’suz teklif aşağı iner | **Tier-1 $80+ ilanda taze de olsa boost** |
| “Bid = 1. sıra + 1” / düşük tavan | Tablo anlık; $40’da 19 bid | **Sabit bid tablosu** (§5.3) |
| “Sprintte max 3 / 8 / 12 boost” | Kaybeden boost iade edildiği için sayı kotası anlamsız | **Kilitli boost Connect** + bakiye (§5.4); Faz 1’de GO sayısı sınırsız |
| “Boost pahalı, az kullan” | Sadece işe yarayınca (etkileşim) ödüyorsun | Kaldıraç 1’in ana aracı → **K3’te varsayılan açık** |

### 5.3 Boost bid — **4. sıra stratejisi** (1. sırayı kovalama)

**Saha gerçeği (senin $150 / ~1 saat ekranı):** 100 / 28 / 27 / 26 Connect. Rekabet **sen girdikten sonra da** artar; “erken boost’suz” ve “sabit 20” **çoğu popüler ilanda yetmez**. SKIP her ilana değil — **balina (B1) kovalamayı** bırak, **ilk 4’e minimum bid** ile gir.

**Tavan (iş başına max boost — 1. için değil, 4. için):**

| Bütçe | Max boost |
| --- | --- |
| $50–79 | **11** |
| $80–99 | **15** |
| $100–149 | **25** |
| $150–199 | **30** |
| $200+ | **40** |

**Gönderim anında (tabloyu oku):**

```
cap = bütçeye göre max
B4 = 4. sıradaki bid

gerekli = B4 + 1          // ilk 4’e girmek için minimum

gerekli > cap  →  SKIP (4’e bile sığmıyorsun; 101’lik 1. sıraya asla girme)
B1 > cap       →  SKIP (balina; örn. B1=100, cap=30)
aksi           →  boost = min(cap, gerekli)   // çoğu zaman = gerekli; tablo boşsa cap’e kadar verebilirsin
```

**Örnek ($150, tablo 100/28/27/26):** cap=**30**, gerekli=**27** → boost **27** (4. sıra), **101 atma**. Sonra biri 100 zaten 1.’de; sen 2–4 arası görünürlük.

**Örnek ($40, tablo 19/18/17/12):** cap=11, gerekli=13 → **SKIP** (niş + bütçe uyumsuz).

**Sonradan geçilirsen:** iade; teklif Connect gider — **normal**. Plan “kaçış” değil, **doğru fiyatta 4’e gir**.

**Maliyet tavanı:** teklif + boost ≤ işin **~%15**; $150 + boost 30 ≈ %4–5.

### 5.7 Saha gerçeği — $150 iş, ~1 saat, tablo 100 / 28 / 27 / 26

Bu **normal** popüler ilanlarda; senin gözlemin doğru:

| Gerçek | Plan cevabı |
| --- | --- |
| İlk saatte tablo dolar, teklif 50+ olur | Gönderimde **tekrar say**; bildirimdeki “5 teklif” güvenilmez |
| **1. sıra 100 Connect** ($150 iş) | **Balina** — asla kovalama; **B1 > bid** → K5 SKIP |
| Sen **20** bid atıp 4’e girersin, sonra 100 gelir | **Beklenen**; boost iade, **teklif Connect gider** — sık tekrarlanırsa o niş **soğuk değil, sıcak** → min bütçe / filtre sıkı |
| “İlk 3 yeter” | Sadece **boost’ta kaldığın süre**; 3’ten düşersen biter |
| Sabit 20, $100–150 için | **Sadece B4+1 ≤ 20** (ör. 4. sıra ≤19) ilanlara; **26+ tablo** → SKIP |

**Balina / sıcak tablo (gönderim anı, SKIP):**

- **B1 > bid** (senin sabit boost’un) → **SKIP**
- **B1 ≥ 25** (hangi bütçe olursa olsun, balina sinyali) → **SKIP**
- **B4 + 1 > bid** → **SKIP** (4’e bile giremezsin)
- Örnek: $150, B1=100 → bid=20 → **K5**, Connect **0**

**Ne avlıyoruz:** Tablo **boş veya düşük** (B4 ≤ bid−1), **niş** (WP fix, form, hız — “website developer payments 3 ay” değil), bazen **gece/UK** düşük rekabet. Popüler $100–150 landing = çoğu zaman **mezar**.

**Sabit 20/30 yerine:** Tablo **100/28/27/26** → boost **27–30**, balina **101** değil. Popüler ilanların çoğu böyle; **SKIP sadece cap’i aşan tabloda**.

### 5.4 Sandık ve kilitli Connect (Faz 1 ile uyumlu)

- Her boost = **sabit bid** (§5.3) kadar Connect, **gönderimde rezerve**; ücret kesimi §5.1’e göre (etkileşim veya 7 gün sonu ilk 4).
- **Kilitli toplam** ≈ açık boost’ların bid’leri toplamı. **Hedef:** başlangıçta **≤120** kilitli (600’ün 120’si boost için ayrı say); Faz 1 agresifte çok K3 atarsan kilit **120’yi aşar** → ya **Connect al**, ya o ilanda **K4** (boost’suz taze) veya SKIP.
- **Bakiye < teklif + bid** → SKIP veya Connect al.
- Çoğu geçilme → iade gelir ama **gecikmeli**; günlük “kullanılabilir bakiye”yi Upwork’ten kontrol et.
- Faz 2: kilit **>150** sürekli → günlük K3 sayısını düşür veya tavanı sadece $100+’da kullan.
- Log: `Boost bid`, `Durum` = **açık / ödendi / iade**, `Kilitli toplam`.

### 5.5 Haftalık boost kontrolü

| Gözlem | Ayar |
| --- | --- |
| Boost’lu tekliflerde açılma **<%50** | Sorun teklifin ilk 2 cümlesinde. Boost’u kısma, **açılışı değiştir** |
| Boost’lu açılma iyi, cevap **<%20** | Sorun gövdede (denetim/ek). Strateji Bölüm 3–5 |
| Çoğu boost **geçildi/iade** ve açılma düşük | Sabit bid +2 ($100 bandı 20→22); veya sadece **≤10 dk** penceresi |
| Nişte B4 sürekli **≥15** | O preset’te min bütçeyi **$100**’e çek |

### 5.6 Boost — tek sayfa özet (gönderimde bak)

```
cap = $50→11 | $80→15 | $100→25 | $150→30 | $200→40
gerekli = B4 + 1

B1 > cap veya gerekli > cap? → SKIP (balina / sığmıyor)
$80+ Tier-1 GO? → boost = gerekli (≤ cap). 1. sıraya kovalama.
$50–79? → boost = min(11, gerekli)

Sonra rekabet artar; bid artıramazsın. Geçilirsen boost iade.
```

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

**Faz 1:** Tüm uygun GO’ları peak bloklarında işle (11–13, 15–22 TR); günlük sayı tavanı yok. **Faz 2:** günde 4–8 GO.

1. Push gelir → ön eleme (§4).
2. **REKABET kartı** → K1–K6.
3. GO ise: denetim 5–10 dk → teklif (§6) → gönderim: **sabit boost bid** (§5.3). Boost’suz gönderme.
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
