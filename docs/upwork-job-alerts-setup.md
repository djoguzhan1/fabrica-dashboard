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
