# Upwork anlık ilan bildirimi — kurulum (3. taraf + tam kapsam)

**Amaç:** İlgi alanlarına düşen **yeni** ilanlar telefona **~30–90 saniye** içinde gelsin; sen Upwork’te sürekli kaydırma yapma. Teklif atmak için ayrıca **72h plan** (`docs/upwork-72h-first-job-plan.md`, dal `cursor/upwork-72h-plan-5f90`) içindeki **EV / Tier** kuralları geçerli — bildirim ≠ her ilana başvuru.

**Son güncelleme:** 2026-09-26

---

## 1) Önerilen araç paketi (“cimri değil”, solo freelancer)

| Katman | Araç | Neden | Kabaca maliyet |
| --- | --- | --- | --- |
| **Ana hat (hız + filtre)** | **[UpHunt](https://uphunt.io)** | 2026 karşılaştırmalarında **en düşük gecikme** (~30 sn), açıklanabilir skor, bütçe/ülke/payment verified, Slack/Telegram/push/webhook | Ücretli plan (siteden; çoklu feed + kanal için) |
| **Yedek hat (kaçırma riski)** | **[Vibeworker](https://tryvibeworker.com) Pro** | Aynı aramaları **push + Telegram** paralel; kilit ekranı bildirimi; webhook | ~$19/ay |
| **İkinci bağımsız izleyici** | **[Upwatcher](https://www.upwatcher.io)** | Upwork arama URL’sini yapıştır → Telegram; **Upwork şifresi vermiyorsun** (ToS dostu); saniyeler içinde ping iddiası | Free 1 feed + ücretli çoklu feed |
| **Upwork içi yedek** | **Freelancer Plus** | Resmi “instant job” + bid içgörüsü | ~$19,99/ay + Connects |

**Kullanma:** En az **UpHunt + Vibeworker Pro** kur. Upwatcher’ı **Tier-1 aramalarına** (Q1–Q8) ikinci hat olarak ekle. GigRadar / tam otomatik bid araçları **önerilmez** (ToS + ajans fiyatı).

**Telegram:** Tek bir grup/kanal aç: `Upwork Jobs — Oğuzhan`. UpHunt + Vibeworker + Upwatcher hepsi buraya gitsin; mükerrer ilanları araçların dedupe özelliği varsa aç.

---

## 2) Upwork arama filtreleri (her Q için aynı)

Upwork → **Find Work** → arama kutusuna sorguyu yapıştır → filtreler:

| Filtre | Değer |
| --- | --- |
| Sort | **Newest** |
| Posted | **Last 24 hours** (Upwatcher/UpHunt’te “yeni ilan” modu varsa onu da aç) |
| Job type | **Fixed price** ve **Hourly** (ikisi de) |
| Budget / rate | **$20 – $1,000** (bildirimde gürültüyü keser; **$15 işler gelmez** — bilinçli: plan tabanı $20 Tier-2) |
| Client | **Payment verified** ✓ |
| Proposals | **Less than 5** ve **5 to 10** |
| Experience | **Entry** + **Intermediate** |
| Location (opsiyonel) | US, UK, Canada, Australia öncelik — **zorunlu değil** (Worldwide ilanları kaçırma) |

**Kategoriler** (mümkün olduğunca işaretle; Upwork ağacı değişebilir):

- Web, Mobile & Software Dev → Web Development  
- Scripts & Utilities  
- AI Apps & Integration  
- Data Extraction / ETL  
- Other – Software Development  

Aramayı **Save** et → URL’yi kopyala → UpHunt / Vibeworker / Upwatcher’a **ayrı feed** olarak ekle.

---

## 3) Araç içi global filtreler (tüm feed’ler)

Bildirimde **yüksek eşleşme** istiyorsun; yine de blacklist’i araçta da uygula (gürültü %40–60 azalır, kaçan iş az):

**Her zaman hariç tut (kelime / NOT):**

`woocommerce AND (checkout OR cart OR payment OR subscription)`, `shopify`, `react native`, `flutter`, `ios app`, `android app`, `full stack saas`, `blockchain`, `crypto`, `nft`, `machine learning model`, `fine-tuning`, `homework`, `assignment`, `thesis`, `exam`, `free test`, `unpaid`, `telegram only`, `whatsapp`, `outside upwork`

**Upwork arama NOT örnekleri** (sorguya ekle): `NOT woocommerce`, `NOT shopify`, `NOT (react OR vue OR angular)`.

**Minimum skor (UpHunt / Vibeworker):** Başlangıç **6/10**; günde 50+ bildirim gelirse **7**’ye çık. Tier-1 feed’lerde (Q1–Q8) skor eşiğini **5** tutabilirsin.

---

## 4) Tam ilgi alanı — 20 kayıtlı arama (Q1–Q20)

Kaynak: 72h plan Bölüm 2 + Ek F. **Hepsini** kur; isimlendirme: `Q01-WP-bug`, `Q02-WP-speed`, …

### Küme A — WordPress, hız, landing (Tier-1, öncelik feed)

| ID | Upwork sorgu |
| --- | --- |
| Q1 | `wordpress AND (broken OR "not working" OR error OR "white screen" OR "critical error" OR conflict OR bug) NOT woocommerce` |
| Q2 | `wordpress AND (slow OR speed OR "page speed" OR pagespeed OR "core web vitals" OR gtmetrix OR lighthouse)` |
| Q3 | `elementor AND (fix OR broken OR mobile OR responsive OR "not working")` |
| Q4 | `"landing page" AND (hvac OR plumbing OR plumber OR roofing OR electrician OR contractor OR "home services" OR cleaning OR landscaping OR locksmith)` |
| Q5 | `("landing page" OR "one page website" OR "one-page website" OR "single page website") AND ("small business" OR local OR "google ads" OR leads)` |
| Q6 | `("small business website" OR "simple website" OR "basic website" OR "5 page website" OR "3 page website") NOT (shopify OR react OR app)` |
| Q7 | `("mobile friendly" OR "mobile responsive" OR responsive) AND (fix OR website) AND (html OR css OR wordpress)` |
| Q8 | `("contact form" OR "form not sending" OR "form not working") AND (wordpress OR website)` |

### Küme B — Sheets / Excel (Tier-2)

| ID | Upwork sorgu |
| --- | --- |
| Q9 | `("google sheets" OR excel OR spreadsheet) AND (formula OR formulas OR vlookup OR xlookup OR "pivot table" OR dashboard OR "clean up" OR cleanup OR "conditional formatting")` |
| Q10 | `("google sheets" OR excel) AND (template OR tracker OR calculator OR "quick" OR urgent OR "small task")` |

### Küme C — Tasarım → HTML, küçük WP görevleri (Tier-2)

| ID | Upwork sorgu |
| --- | --- |
| Q11 | `(figma OR psd OR pdf OR xd) AND ("to html" OR "html css" OR "html/css" OR convert)` |
| Q12 | `(wordpress OR website OR html OR css) AND (install OR setup OR "set up" OR migrate OR "small change" OR "small changes" OR "quick fix" OR tweak OR urgent OR asap OR "today")` |

### Küme D — Script, otomasyon, AI, deploy (Tier-3 / Ek F — geniş havuz)

| ID | Upwork sorgu |
| --- | --- |
| Q13 | `(fix OR bug OR error OR broken OR "not working" OR debug) AND (html OR css OR javascript OR php OR python OR script OR website)` |
| Q14 | `(script OR automate OR automation OR "automatic") AND (python OR javascript OR node OR "google sheets" OR "apps script" OR csv OR excel OR pdf)` |
| Q15 | `(chatgpt OR openai OR gpt OR claude OR anthropic OR "ai") AND (integrate OR integration OR api OR automate OR chatbot OR prompt OR summarize)` |
| Q16 | `(api OR webhook OR zapier OR make OR n8n) AND (connect OR integrate OR integration OR sync OR "send to")` |
| Q17 | `("small task" OR "quick task" OR "one-time" OR "one time" OR "small job" OR "quick fix" OR "small project") AND (code OR script OR website OR fix OR python OR javascript)` |
| Q18 | `("need help" OR "help me" OR "walk me through" OR troubleshoot OR "screen share") AND (code OR script OR website OR wordpress OR python OR excel OR sheets)` |
| Q19 | `(deploy OR deployment OR hosting OR dns OR ssl OR "github pages" OR netlify OR vercel) AND (website OR site OR app)` |
| Q20 | `(scrape OR scraping OR extract OR "pull data" OR "collect data") AND (website OR csv OR excel OR "google sheets") NOT (linkedin OR instagram OR facebook OR login)` |

**Portföy kanıt linkleri (teklifte):**

- Web: https://djoguzhan1.github.io/web-dev-portfolio/  
- tidycsv: https://github.com/djoguzhan1/tidycsv  
- docbrief: https://github.com/djoguzhan1/docbrief  
- sheet-notify: https://github.com/djoguzhan1/sheet-notify  

---

## 5) Hangi aramayı hangi araca (pratik dağılım)

| Araç | Feed sayısı | Ne yükle |
| --- | --- | --- |
| **UpHunt** | **20** (hepsi) | Q1–Q20 URL + global filtreler + min skor |
| **Vibeworker Pro** | **20** | Aynı URL’ler; **push** açık |
| **Upwatcher** | **8** | Sadece **Q1–Q8** (en yüksek hire olasılığı) |
| **Freelancer Plus** | Upwork içi | Aynı 12 aramayı Upwork’te “Save” + instant alert |

UpHunt/Vibeworker’de 20 feed limiti çıkarsa: önce Q1–Q12, sonra Q13–Q20’yi ikinci hesap/plan veya Upwatcher’a böl.

---

## 6) Kurulum adımları (sırayla, ~90 dk)

### Adım 0 — Telegram (10 dk)

1. Telegram’da kanal veya grup: `Upwork Jobs`.
2. Bildirimler: **ses açık**, önizleme açık, “önemli” (iOS/Android).
3. Sessiz saat: **01:00–09:00 GMT+3** (UpHunt / Vibeworker quiet hours).

### Adım 1 — UpHunt (30 dk)

1. Hesap aç → Telegram bağla.
2. Her Q için: Upwork’te aramayı oluştur → filtreleri §2’ye göre ayarla → **Copy link** → UpHunt’a “Add feed”.
3. Feed adı: `Q01-WP-bug` … `Q20-scrape-public`.
4. Global exclusions §3.
5. **Minimum AI score:** 6 (Q1–Q8 için 5).
6. Kanallar: Telegram + **push** (varsa) + webhook (opsiyonel, ileride).

### Adım 2 — Vibeworker Pro (25 dk)

1. Pro’ya geç.
2. Aynı 20 URL’yi ekle.
3. **Push notification** açık (Telegram sessizdeyken yedek).
4. Skor eşiği 6.

### Adım 3 — Upwatcher (15 dk)

1. Q1–Q8 URL’lerini yapıştır.
2. Telegram’a yönlendir.
3. Quiet hours 01:00–09:00 GMT+3.

### Adım 4 — Upwork (10 dk)

1. **Freelancer Plus** (anında iş + bid içgörüsü).
2. Q1–Q12’yi Upwork’te **Save search** + e-posta/push.
3. **Availability Badge** (haftalık max 20 Connect).
4. En az **1 aktif teklif** tut (Plus anlık bildirim şartı olabilir).

### Adım 5 — 2 dakikalık test (10 dk)

1. Upwork’te dar bir test araması kaydet (ör. `wordpress AND broken`).
2. Üç kanaldan ping süresini not et (hedef: **< 2 dk**).
3. Gecikme > 5 dk ise feed URL’sini ve “last 24h” filtresini kontrol et.

---

## 7) Bildirim geldiğinde (30 sn — başvuru kararı)

| Kontrol | Gönder | Atla |
| --- | --- | --- |
| Blacklist (§3, plan Ek F4) | | ✓ |
| Bütçe | Tier-1 ≥ $30, Tier-2 ≥ $20, Tier-3 ≥ $30 (F4 tablosu) | $15 “full redesign” vb. |
| Connects | ≤ 12; ucuz işte ≤ 6 | 11 Connect + $15 |
| Proposals | < 20 veya ilan < 15 dk | 50+ |
| Scope | Tek cümle DoD yazılabiliyor | Belirsiz “make it better” |
| EV (plan Ek C E1) | ≥ 4 | < 3 |

**Hız:** Tier-1 → **5 dk** içinde teklif; şablonlar T1/T2/T3/S4/S5/T6 (plan Bölüm 5 + Ek F6).

### 7.1 Fiyat bandı (hedef)

| Bant | Karar | Not |
| --- | --- | --- |
| **$50–150** | **Ana hedef** (strateji sweet spot) | İlk review’un geldiği yer; teklif başına denetim + ek buraya |
| $150–400 | GO, Tier-1 ise | Landing / hız / 1–3 sayfa; 2 milestone |
| $400–800 | Sadece Tier-1 tam eşleşme | 72h’de kapanmayabilir; scope dar tut |
| $20–49 | GO ama **yalın** | Mock yok, denetim kısa; ≤3 saat efor, tek teslimat |
| $15–19 | Yalnızca ≤1 saat efor **ve** ≤6 Connects | Review değeri fiyattan büyük |
| $800+ | SKIP | 72h penceresinde kapanmaz |
| Saatlik | $20/sa × ≤5 saat, contract’ta saat tavanı | Tracker zorunlu |

Teklif tutarı ilan bütçesine **eşit veya altında**. Bütçe düşükse fiyatı değil **scope’u** küçült (“$29 = 1 fix, 3 değil”).

### 7.2 Boost kararı (hepsi sağlanmalı)

| Koşul | Eşik |
| --- | --- |
| İlan yaşı | **15–60 dk** (<5 dk faydasız, >60 dk zararlı) |
| Tier | **Tier-1 tam eşleşme** (WP fix / hız / landing) |
| Bütçe | **≥ $80 sabit** — boost maliyeti gelirin %5’ini geçmesin |
| 1. sıra fiyatı | **≤ 10 Connects**; 13+ isteniyorsa vazgeç |
| Teklif sayısı | < 10 |
| Müşteri | ≥1 hire **ve** harcama geçmişi |
| Bütçe disiplini | Sprint başına **en fazla 3 boost** (1 ödül + 2 koşullu) |

**Neden bu kadar dar:** Connect $0,15. $40’lık işte 11 Connect teklif + 13 Connect boost = $3,60, gelirin ~%9’u. Aynı 13 Connect’i **iki taze ilana** koymak, iş alma olasılığına ~6–7 kat fazla katkı yapıyor (plan Ek C R1). Boost, teklifin zayıflığını telafi etmez — sadece görünürlük satın alır.

Gönderim sonrası boost eklemek: etkisi ölçülmemiş, **yapma**.

### 7.3 Boost savaş sandığı (baştan ayır)

Teklif Connect’leri ile **karıştırma**. Plus + teklif alımları (~1.200 Connect / sprint) günlük hacim için; boost ayrı bir “cephe”.

| Kalem | Miktar | Not |
| --- | --- | --- |
| **Sprint başı sandık** | **60 Connect (~$9)** | Upwork’ten al, bakiyede “sadece boost” diye not et |
| Tek seferde max bid | **10 Connect** | 1. sıra 11+ istiyorsa → sandığa dokunma, boost yok |
| Sprintte max kullanım | **3 boost** | ~30 Connect max (~$4,50) — geri kalan 30 Connect yedek / 2. hafta |
| Hedef iş bütçesi (boost’lu) | **$80–400** sabit | Sweet spot **$100–150** landing / WP hız |
| Hedef iş bütçesi (boost’suz) | **$50–150** | $50–79 her zaman boost **kapalı** |

**Oyunu bitiren kural:** Boost sandığı **görünürlük** satın alır; kapanışı **teklif metni + hız** getirir. Sandık boşalınca sprint bitene kadar boost yok — teklif hacmi devam eder.

Takip: `docs/upwork-proposal-log.md` → “Boost sandığı” tablosu; her boost sonrası `Sandık kalan` güncelle.

**İlk review sonrası (isteğe bağlı):** Sandığı **40 Connect**’e indir veya sadece **$150+** işlerde aç; ilk 3 review gelene kadar 60 / 3 boost kuralı yeterli.

### 7.4 Agresif mod — “görünmez teklif atmam” (0 review sprint)

**Fikir:** Teklif Connect’i zaten gidiyor; Tier-1 + doğru bütçede **görünürlük satın al**. Kar kalır: hedef **iş alma maliyeti** (teklif + boost) gelirin **≤%15’i** ($100 iş → ≤$15 toplam Connect).

#### Rahat sprint bütçesi (72 saat, max kapanış)

| Kalem | Connect | ~USD ($0,15) | Not |
| --- | --- | --- | --- |
| Freelancer Plus | (100 dahil) | ~$20 | Anlık iş + içgörü |
| **Teklif havuzu** (ayrı) | **~900** | **~$135** | ~70–80 teklif × ~11 ort. |
| **Boost sandığı** (ayrı, karışmaz) | **120** | **~$18** | Agresif cephe |
| Badge / yedek | ~20 | ~$3 | |
| **Toplam Connect nakit** | **~1.020** | **~$153** | Plus’taki 100’ü say |
| **Toplam sprint (nakit)** | | **~$175–190** | Araçlar (Vibeworker) hariç |

İlk iş **$80–150** gelirse Connect maliyeti (~$20–30 teklif + ~$2–5 boost) hâlâ **yüksek marj** bırakır (Upwork %10 fee sonrası da).

#### Boost sandığı — agresif kurallar

| Sandık | **120 Connect** başlangıç |
| --- | --- |
| Sprintte max boost | **12** (≈10 Connect ort. → ~120 tavan) |
| Tek boost tavanı | **1. sıra + 1 Connect**, **max 15 Connect** |
| Min iş bütçesi (boost açık) | **$80 sabit** |
| Alt bant $50–79 | Teklif **evet**, boost **hayır** |

**SALDIR (boost zorunlu değil ama önerilen — hepsi ✅):**

| Bant | Koşullar | Max boost bid |
| --- | --- | --- |
| **A — altın** | $100–200 · Tier-1 (WP fix / hız / landing) · ilan **10–45 dk** · proposals **<8** · müşteri ≥1 hire · teklif denetimli | 1. sıra ≤12 → **bid = min(1. sıra+1, 12)** |
| **B — gümüş** | $80–99 veya $201–350 · Tier-1 · ilan **15–60 dk** · proposals **<12** | Max **10** |
| **C — pas** | $50–79 · Tier-1/2 · boost kapalı | 0 |

**ASLA boost:** $40 ve altı · ilan <10 dk (plan: boost faydasız) · proposals **≥20** · 1. sıra zaten **≥16** · müşteri 0 hire + <$50 · gönderim **sonrası** boost.

**Görünürlük mantığı:** Tier-1 + bant A/B’de teklif atıyorsan ve 1. sıra **≤12** ise **boost’u varsayılan aç**; teklif metni zayıfsa boost yakma (önce metni düzelt).

#### Günlük fren

- Boost sandığı **<30** kaldı → sadece **bant A**.
- Bugün **4 boost** harcandı → yarın sabaha kadar sadece bant A.
- **2 gün üst üste** cevap yok → boost’u 1 hafta **max 10 Connect**’e indir; teklif metnini A/B (açılış) değiştir.

Takip: `docs/upwork-proposal-log.md` — Boost sandığı tablosu (**120** başlangıç).

---

## 7.4 Rahat bütçe — teklif + boost (max kapanış, hâlâ marj)

**Gerçek:** İlk sprint yatırım. Gelir $50–150/iş; Upwork ~%10 keser. “Kar”, 1–3 review sonrası dönüşüm yükselince gelir; şimdi amaç **iş kapatmak**, Connect’i sıfıra indirmek değil.

**Görünürlük:** Taze ilan (<15 dk, <5 teklif) → boost **gerekmez**, hız + ilk 2 cümle yeter. İlan **15–60 dk**, 4 boost slotu dolu, **$80+ Tier-1** → boost **mantıklı**; görünmezsen teklif atmak boşa yakmaya yakın. O yüzden bütçe **iki havuz**.

### Havuzlar (2 haftalık “rahat” sprint)

| Havuz | Connect | ~$ (0,15) | Ne için |
| --- | --- | --- | --- |
| **A — Teklif** | **750** | **~112** | ~65–70 GO teklif (ort. 11 Connect) |
| **B — Boost sandığı** | **80** | **~12** | 8× ~10 Connect veya 5× daha yüksek 1. sıra |
| **C — Yedek** | **70** | **~10** | Hafta 2, ani 1. sıra 12 Connect, iade gecikmesi |
| **Toplam Connect** | **900** | **~135** | |
| **Freelancer Plus** | — | **~20** | Anlık iş + bid içgörüsü |
| **Nakit tavan (rahat)** | | **~155** | Plus + 900 Connect alımı |

Mevcut **104 Connect** varsa: **~800 Connect daha al** → toplam ~900; içinden **80’i boost** diye ayır (not / ayrı say).

### Boost ne zaman (görünmezlik kuralı)

| Durum | Boost |
| --- | --- |
| İlan <15 dk, proposals <5 | **Hayır** — zaten üstte |
| İlan 15–60 dk, $80–400, Tier-1, proposals <10, 1. sıra ≤10 | **Evet** (sandıktan) |
| İlan 15–60 dk, $50–79 | **Hayır** — fiyat düşük, boost ROI kötü; hız + ek |
| İlan >60 dk veya proposals 20+ | **Teklif atma** veya boost’suz (çoğu zaman atla) |
| 1. sıra ≥11 Connect | **Hayır** — sandıkta kal |

Sprintte boost tavanı: **8 kullanım** (rahat) veya disiplinli **5** (marj için). Her boost = önce teklif metni + denetim/ek hazır; zayıf teklife boost yok.

### Beklenen sonuç (dürüst, rahat senaryo)

| Metrik | Rahat plan |
| --- | --- |
| GO teklif | ~65–70 / 2 hafta |
| Boost harcaması | ~40–80 Connect (~6–12 $) |
| Hire hedefi (strateji) | **%12–20** → **8–14 teklifte 1** → 65 teklifte **~5–8 hire** teorik üst; ilk review için **gerçekçi 2–4 hire** |
| Gelir (2–4 × $80 ort.) | **~160–320 $** |
| Connect + Plus | **~155 $** |
| İlk review sonrası net | İş ücretinden Upwork payı düşülür; sprint **küçük artı veya başabaş** normal, asıl kazanç review |

**Agresif (max kapanış, daha az marj):** A=1000, B=120, C=80 Connect → ~$180 Connect + Plus; boost 10–12 kez; sadece Tier-1 $100+.

**Minimum (marj, yavaş):** A=500, B=40, C=30 → boost 4 kez; taze ilanlara ağırlık.

### Senin bakiyeyle (104 Connect)

1. **~700–800 Connect satın al** (rahat A+B+C’ye yaklaş).  
2. **80 Connect = boost sandığı** (dokunma, sadece 7.2 + 7.4 tablosu).  
3. Günlük: önce taze GO; 15–60 dk ve $80+ görürsen sandıktan boost.  
4. Sandık **20’nin altına** inince 40 Connect daha al, yine sadece boost’a.

---

## 8) Aylık maliyet özeti (cimri değil senaryo)

| Kalem | ~USD/ay |
| --- | --- |
| UpHunt (ücretli, çoklu feed) | site fiyatı |
| Vibeworker Pro | ~19 |
| Upwatcher (çoklu feed) | site fiyatı |
| Freelancer Plus | ~19,99 |
| Connects (teklif hacmine göre) | ~150–200 |
| **Toplam sabit** | **~60–100+** + Connects |

Bu, “sürekli Upwork’te oturma” maliyetinin karşılığıdır; ilk review sprinti ile uyumlu.

---

## 9) İlgili repo dosyaları

| Dosya | Dal |
| --- | --- |
| `docs/upwork-72h-first-job-plan.md` | `cursor/upwork-72h-plan-5f90` |
| `docs/upwork-profile.md` | `cursor/upwork-profile-5f90` |
| `docs/upwork-portfolio/README.md` | `cursor/proof-projects-5f90` |

---

## 10) Senin yapman gerekenler (bugün)

- [ ] Telegram kanalı + ses
- [ ] UpHunt: 20 feed
- [ ] Vibeworker Pro: 20 feed + push
- [ ] Upwatcher: Q1–Q8
- [ ] Freelancer Plus + 12 saved search Upwork içi
- [ ] Test ping + ilk gerçek Tier-1 teklif

İlan geldiğinde sohbete **başlık + bütçe + Connects + proposals + müşteri özeti** yapıştır; EV ve örnek cover letter yazılır.
