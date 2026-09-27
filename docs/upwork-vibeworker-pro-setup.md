# Vibeworker Pro — tam rehber (resmi doküman + 72h plan)

Kaynak: [tryvibeworker.com/ai-info](https://tryvibeworker.com/ai-info), [how-it-works](https://tryvibeworker.com/how-it-works), [FAQ](https://tryvibeworker.com/faq). Upwork planı: `docs/upwork-plan-bildirim-slack-degil.md` · Teklif: `docs/upwork-proposal-strategy.md`.

---

## 1) Vibeworker ne yapar / ne yapMAZ

| Yapar | YapMAZ |
|-------|--------|
| Public Upwork ilanlarını **yakın gerçek zamanlı** izler | Upwork şifresi / login **istemez** |
| Her ilanı **4 skor** + müşteri sinyalleri ile zenginleştirir | Otomatik teklif / bid (**ToS ihlali**) |
| **Filter preset** ile eşleşeni **push / Telegram / webhook / RSS** ile gönderir | Resmi Upwork API’si değil; bağımsız 3. parti |
| Pro’da **Upwork link** + **AI proposal draft** (düzenlemen şart) | **E-posta bildirimi yok** (2026 doküman) |

Gecikme: uygulama FAQ’sine göre ilan **~1 dk** içinde görülür, alarm hemen ardından gider. Tüm kanallar aynı hızda; push kurulum gerektirmediği için önerilir. Upwork login istemez. İptal: Google Play / App Store aboneliğinden.

---

## 2) Ürün mantığı (kafada net olsun)

```
Yeni Upwork ilanı
  → LLM: quick-win, scope clarity, red flags, effort (saat)
  → Preset filtresi: kategori, kelime, min bütçe, müşteri eşiği
  → (Opsiyonel) AI mode: profiline göre sıralama
  → Preset’te açık kanal: MOBILE PUSH → telefon
```

**İki ayrı katman:**

1. **Onboarding “Shortlist” ekranı** (Step 4) — sıkı müşteri eşikleriyle ilan sayısının nasıl düştüğünü gösteren bilgi ekranı; tikler tıklanmaz.
2. **Filter preset’ler** (kurulumdan sonra) — kelime, bütçe, exclude, bildirim kanalı. **Asıl niş daraltma burada.**

**Hunting mode (strateji):**

| Mod | Kim için | Sen (0 review) |
|-----|----------|----------------|
| **Quick Wins** | Net teslimat, verified client, tek oturumda kapanır; bütçe ikincil | **BUNU SEÇ** |
| Skill Match | Embedding, deneyime uygun akış | 5+ review sonra |
| High Value | Büyük kontrat, yüksek spend | İlk işlerde kaçırma küçük $50–150 |

AI ranking alt modu: `reviewStacking` (yeni freelancer) — Quick Wins ile uyumlu.

---

## 3) Free vs Pro

| | Free | Pro (~$19/ay) |
|---|------|----------------|
| Feed + skorları okuma | ✅ sınırsız | ✅ |
| **Push / Telegram / webhook** | ❌ | ✅ |
| Upwork link açma | Web: **10 ömür boyu**; mobil: günlük kota | Sınırsız |
| Proposal draft | Web: 5 ömür boyu; mobil: günlük kota | Sınırsız |

**Alarm için Pro şart.** Feed’e bakmak yetmez; ilk iş sprintinde Pro al.

---

## 4) Onboarding (Step 1–5) — planla uyumlu cevaplar

### Step 1 — Lanes
- ✅ Web / AI builder  
- ✅ Data / automation  
- ❌ Diğer lane’ler

### Step 2 — Kategoriler
- ✅ Web Development, Scripts & Utilities, AI Apps & Integration, Other - Software Development  
- ✅ Data Extraction/ETL, Data Analysis & Testing  
- ✅ **Web & Mobile Design** (listede varsa) — landing page / Figma→HTML / küçük site işlerinin bir kısmı burada açılır  
- ❌ **DevOps & Solution Architecture** — çoğu AWS/kurumsal (ör. “AWS FSx … US Person Required”); küçük DNS/SSL/hosting işleri zaten Web Development’a düşer  
- ❌ Ecommerce (Shopify/Woo), Mobile, Marketing, Engineering, Accounting, Writing, Legal, Translation…  
- Admin / Data Entry: **kapalı başla**; 3 günde Sheets işi neredeyse hiç gelmezse aç (Sheets preset’i kelimeyle süzer)

### Step 3 — Referral
- **Skip**

### Step 4 — Shortlist zinciri (bilgi ekranı)

Onboarding’de bu ekran **tıklanmıyor**; **Continue** de. Uygulama FAQ’si: “Shortlist is just the one we set up for you”, “every setting the tuner applied is visible and editable” — yani Pro sonrası **Shortlist filtresini aç ve aşağıdaki tabloya göre düzenle** (ya da bildirimini kapat). Asıl niş filtreler yine P1–P6 preset’leri (Bölüm 5D).

Hepsi açıkken 349 → **14,7 iş/gün** kalıyor ve örnek listenin tamamı plana göre SKIP ($8k fullstack, React SaaS, mobil trading app, .NET/AWS, SERP altyapısı, Squarespace 2 site göçü). Sebep: $2k/$10k/$50k spend + 4.8 + 70% hire + fixed $100+ birlikte “büyük kurumsal müşteri” filtresi oluyor. Preset’lerde bunun yerine:

| Eşik | Preset’te | Neden |
| --- | --- | --- |
| payment verified | ✅ | Plan: zorunlu |
| hire rate 30%+ | ✅ | Post edip hiç hire etmeyen müşteriyi keser (Connect israfı) |
| client has spent $500+ | ✅ | Tek spend eşiği; ciddi ama küçük müşteri |
| hire rate 50%+ | ❌ | 30% yeter; küçük işletmeleri gereksiz eler |
| client has spent $2k+ | ❌ | $50–150 işleri veren müşterinin çoğu bunun altında |
| client rating 4.5+ | ✅ | Zor müşteriyi eler, hacmi az düşürür (~%10) |
| client has spent $10k+ | ❌ | Büyük proje/ajans müşterisi |
| hire rate 70%+ | ❌ | Aşırı sıkı |
| client rating 4.8+ | ❌ | 4.5 yeter |
| client has spent $50k+ | ❌ | Kurumsal |
| **fixed price $100+** | ❌ **(en kritik)** | Açıksa $30–99 WP fix / hız / Sheets işleri hiç gelmez; alt sınırı preset’lerde ver |
| hourly $15/hr+ | ✅ | $5–10/sa işleri keser; profil ücreti $15–25 |

Preset’lerle hedef **10–30 push/gün**. Preset’te hire rate / spent / rating alanı yoksa: Settings’te “Shortlist” veya “Client quality” bölümüne bak; o da yoksa bu kontrolü bildirim geldiğinde plan müşteri filtresiyle elle yap. Preset’ler kurulduktan sonra da günde 5’ten az iş görünürse onboarding’i tekrarla veya destek adresine yaz.

### Step 5
- Bitir → ana uygulama

---

## 5) Kurulum bittikten sonra (sıra önemli)

### A) Pro
- Ayarlar / Upgrade → **Pro** ($19/ay). Ödeme: uygulama içi (Play) veya web.

### B) Hunting mode + skill profili
- **Settings / Profile → Hunting mode → Quick Wins**; AI ranking modu varsa **Review Stacking**.
- Hazır preset’ler: **Review Stacking** → temel al, aşağıdaki P1–P5’e göre düzenle. **Sniper** ve **High Value** → alarmı kapat veya sil (0 review’da büyük işlere Connect yakar).
- AI skorlar “skill profile”a göre hesaplanır: profil alanına `docs/upwork-profile.md` Section B overview’unu ve Section C skill listesini yapıştır (WordPress, WordPress Bug Fix, Page Speed Optimization, Landing Page, Responsive Design, CSS, Google Sheets, Microsoft Excel, Python, Google Apps Script).

### C) Bildirim (Android)
1. Uygulama: **Settings → Notifications** (Vibeworker içi) → **Mobile push ON**, quiet hours **01:00–09:00** (Europe/Istanbul).  
2. Telefon: **Ayarlar → Uygulamalar → Vibeworker → Bildirimler** → açık, ses.

**Slack kullanma** (telefonda çalışmıyor). Telegram opsiyonel; istemezsen kapalı.

### D) Filter preset’ler (plan Q1–Q20)

Arayüzdeki alan adları farklı olabilir; parantezde Vibeworker MCP alan adı var.

**Her preset’te ortak:**

| Alan | Değer |
| --- | --- |
| Payment verified (`requirePaymentVerified`) | ✅ |
| Min hire rate (`minHireRate`) | 0.3 |
| Min client spent (`minClientSpent`) | 500 |
| Min client rating (`minClientRating`) | 4.5 |
| Job type (`jobType`) | Fixed + Hourly |
| Experience (`experienceLevel`) | Entry + Intermediate (Expert kapalı) |
| Min hourly (`budgetMinHourly`) | 15 |
| Bütçesiz ilanı gizle (`hideUnpostedBudget`) | ❌ (saatlik ilanların çoğu ücret yazmıyor) |
| Posted within (`postedWithinHours`) | 2 — feed için; push zaten anlık. Plan: >60 dk ilana teklif yok |
| Exclude locations | boş |

**Ortak exclude (`keywordsExclude`):**

```text
woocommerce, shopify, squarespace, wix, react, next.js, nextjs, vue, angular, react native, flutter, mobile app, ios app, android app, fullstack, full stack, full-stack, saas, blockchain, crypto, nft, web3, trading bot, homework, assignment, thesis, unpaid, free test, test task, whatsapp, telegram only, outside upwork, us citizen, us person, security clearance, senior developer, senior engineer
```

`app` tek başına ve `long-term` exclude **edilmez**: ilki “apps script”i, ikincisi küçük işlerde sık geçen “potential long-term work” cümlesini keser.

**Preset’ler:**

| Preset | Tier / Q | Min fixed (`budgetMinFixed`) | Include (`keywordsInclude`, herhangi biri) | Ek exclude | Connects max | Skor | Push |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **P1 WP-Fix** | T1 · Q1, Q3, Q8 | 30 | wordpress, elementor, divi, wpbakery, white screen, critical error, plugin conflict, contact form, wpforms, contact form 7 | custom plugin, plugin development, theme development, membership, lms, from scratch | 12 | 5 | ✅ |
| **P2 Speed-Mobile** | T1 · Q2, Q7 | 50 | page speed, pagespeed, core web vitals, gtmetrix, lighthouse, site speed, slow website, load time, mobile responsive, mobile friendly, responsive fix | seo retainer, monthly seo | 12 | 5 | ✅ |
| **P3 Landing-Local** | T1 · Q4, Q5, Q6 | 80 | landing page, one page, one-page, single page, small business website, simple website, hvac, plumbing, plumber, roofing, electrician, contractor, home services, cleaning, landscaping, google ads, lead generation | — | 12 | 6 | ✅ |
| **P4 Sheets-Excel** | T2 · Q9, Q10 | 25 | google sheets, excel, spreadsheet, vlookup, xlookup, pivot table, conditional formatting, formula, dashboard, tracker, calculator | data entry, bookkeeping, power bi, tableau, financial model, vba | 8 | 6 | ✅ |
| **P5 Small-Web** | T2 · Q11, Q12, Q19 | 20 | quick fix, small fix, small change, small task, html css, css fix, figma to html, psd to html, migrate, migration, dns, ssl, hosting, github pages, netlify, ga4, google tag manager, pixel, calendly, booking widget | — | 8 | 6 | ✅ |
| **P6 Scripts-AI** | T3 · Q13–Q18, Q20 | 40 | python, apps script, google apps script, automation, automate, csv, pdf, openai, chatgpt, claude, api integration, webhook, zapier, n8n, make.com, scrape, scraping | linkedin, instagram, facebook, captcha, machine learning model, fine-tune, fine-tuning, computer vision | 12 | 7 | İlk hafta ❌ (sadece feed) |

P1–P3 için skor düşük tutulur: bunlar demolarla birebir örtüşen işler, kaçırmak pahalı. P6 kanıtları tidycsv / docbrief / sheet-notify; gürültü fazla olduğu için önce feed.

**Feed vs bildirim:** P1–P5 push’a, P6 yalnızca feed’e atanır (preset → Alerts). Telegram istersen yalnızca P1–P3 için aç; push ile aynı ilan iki kez gelir.

### D2) İlk 48 saat kalibrasyon

| Gözlem | Ayar |
| --- | --- |
| Push > 40/gün, çoğu alakasız | Skoru +1, exclude’a tekrar eden kelimeyi ekle |
| Push < 5/gün | Preset’lerde rating 4.5’i kaldır; sonra spent $500’ü kaldır; P1–P3 skorunu 4’e indir |
| Push → GO oranı < %20 | Hangi preset gürültü yapıyor bak; o preset’in include listesini daralt |
| Aynı alakasız iş tipi 3+ kez | Tek kelime exclude (ör. `elementor pro license`) |
| Vibeworker push 5 dk’dan geç geliyor | FAQ ~1 dk diyor: telefonun pil tasarrufu Vibeworker’ı kısıtlıyor olabilir (Ayarlar → Pil → kısıtlama yok); Q1–Q8 Upwork kayıtlı aramaları yedek olarak açık kalsın |

Hedef: **10–30 push/gün**, bunların **%25+’ı GO**.

### E) Freelancer Plus (zaten var)
- Upwork app: kayıtlı arama + push = **yedek hat**.

### F) UpHunt
- Slack bağlama. İsteğe bağlı feed listesi; **zorunlu değil** Vibeworker + Plus ile.

---

## 6) İlan geldiğinde (skorları oku)

| Skor | Anlam |
|------|--------|
| **Quick win** (0–10) | Sabit fiyat, net teslimat, tek oturum — 0 review için önemli |
| **Scope clarity** | Brief net mi; düşükse scope creep |
| **Red flags** (yüksek = temiz) | “Free test”, belirsiz brief uyarısı |
| **Effort (saat)** | Bütçe / $50–150 bandına uyuyor mu |

Akış: Push → işi aç → skor + açıklama → **Opus / EV** (`upwork-proposal-strategy.md`) → GO ise Upwork’te teklif. Draft’ı **kopyala-düzenle**; mini denetim + P1–P4 şart.

---

## 7) Sık hatalar

| Sorun | Çözüm |
|-------|--------|
| Push yok | Pro aktif mi? Preset’te **mobile push** açık mı? Telefon bildirimi kapalı mı? |
| Yanlış işler ($8k fullstack) | Preset **exclude** kelimeleri; Sniper / High Value preset’lerinin alarmı kapalı mı |
| Çok az iş | Preset müşteri eşiklerini gevşet (önce rating, sonra spent); min bütçeyi düşürme, exclude’u kontrol et |
| Step 4 tikleri kalkmıyor | Normal, bilgi ekranı; Continue de, ayarı preset’te yap |
| Link açılmıyor | Free kotası — **Pro** |
| Slack | Vibeworker’da gerek yok |

---

## 8) Plan uyumu özeti

| 72h plan | Vibeworker karşılığı |
|----------|---------------------|
| Anlık bildirim | Pro + **mobile push** |
| Q1–Q20 niş | 6 preset (P1–P5 push, P6 feed) + ortak exclude |
| EV / Tier teklif | Değişmez; uygulama sadece alarm |
| 0 review | **Quick Wins** + düşük quick-win eşiği değil, **scope clarity** öncelik |
| Slack/Telegram | Opsiyonel; sen: **sadece push** |

---

## 9) Destek

hello@tryvibeworker.com · Uygulama içi yardım.
