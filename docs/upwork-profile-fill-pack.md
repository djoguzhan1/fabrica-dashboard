# Upwork Profil Doldurma Paketi — alan alan, kopyala-yapıştır

Bu dosya, profildeki **her alanı** tek oturumda doldurman için hazırlandı. Talimatlar Türkçe, yapıştırılacak metinlerin tamamı İngilizce. Başlık / overview / skills için ana metin [upwork-profile.md](./upwork-profile.md) dosyasında; burada tekrar edilmedi.

Neden sen yapıştırıyorsun, ben değil: bulut sunucudan Upwork giriş sayfası Cloudflare bot doğrulamasında takılıyor (test edildi), ortamda giriş bilgin yok, ve yeni bir hesaba ABD veri merkezi IP'sinden girmek Upwork'ün dolandırıcılık filtrelerini tetikleyip hesabı incelemeye aldırabilir. Aşağıdaki sıra ile 30–40 dakikada biter.

Karakter sınırları (Eylül 2026, Upwork yardım merkezi): portfolio başlık 70 / rol 100 / açıklama 600, 5 etiket, görsel önerisi 1000×750 (4:3); Project Catalog başlık 75 ("You will get" hariç), açıklama 120–1.200, 5 arama etiketi, 3 paket. Bu dosyadaki tüm bloklar bu sınırlara göre ölçüldü.

Görseller: `docs/assets/upwork/` klasöründe, yüklemeye hazır (4:3 kapaklar 2000×1500, desktop 1440×900, mobil 780×1688, tam sayfa JPG).

---

## Sıra (profil sayfası → kalem ikonları)

1. Title → `upwork-profile.md` Section A (Best)
2. Overview → `upwork-profile.md` Section B
3. Hourly rate → aşağıda
4. Skills → `upwork-profile.md` Section C (10 + opsiyonel 10)
5. Languages → aşağıda
6. Employment history (+30%) → aşağıda
7. Education (+20%) → aşağıda
8. Portfolio (+20%) → 4 madde, aşağıda
9. Other experiences (+5%) → aşağıda
10. Linked accounts (+10%) → aşağıda
11. Certifications (+10%) → sadece gerçekten sahip olduklarını
12. Video introduction (+10%) → senaryo aşağıda
13. Working style (opsiyonel test) → kendin çöz, 10 dk
14. Verify your identity → kimlik + selfie, kendin
15. Profil fotoğrafı → aşağıda
16. Availability → aşağıda
17. Project Catalog → 3 ilan, aşağıda

---

## 3. Hourly rate

**$20/hr** gir. $49'lık fix ≈ 2–2,5 saat iş; $20 bununla tutarlı. Şu anki $3.00 ABD/İngiltere müşterisine "düşük kalite" sinyali veriyor ve sabit fiyatlı ilanlarla çelişiyor. Sabit fiyatlı işleri etkilemez.

## 5. Languages

- Turkish → **Native or Bilingual**
- English → dürüst seç: canlı görüşmeyi rahat yürütüyorsan **Fluent**, değilse **Conversational**. Müşteri bunu ilk aramada test eder; abartma.

---

## 6. Employment history (+30%)

Upwork sıralamasında en ağır bölüm. Anahtar kelimeler (WordPress, landing page, speed) başlıkta ve açıklamada geçmeli. Sadece gerçek işler, gerçek tarihler.

### Kayıt 1 — bugün doğru olan

| Alan | Değer |
|---|---|
| Title | `Freelance Web Developer — WordPress Fixes & Landing Pages` |
| Company | `Self-employed` |
| Location | `Bursa, Turkey` |
| Start date | web işi almaya başladığın ay/yıl (gerçek) |
| I currently work here | ✓ |

**Description** (max 500):

```text
Independent web developer for local service businesses in the US and UK. I fix WordPress bugs and speed problems (broken layouts, plugin conflicts, mobile issues, slow load times) with a root-cause fix and a before/after speed check. I build one-page landing sites for HVAC, plumbing and contractor businesses in hand-coded HTML/CSS with click-to-call, reviews, FAQ and service-area sections. I also clean up Excel and Google Sheets files: formulas, formatting, simple dashboards.
```

### Kayıt 2 — sadece gerçekten çalıştıysan (şablon)

Daha önce bir şirkette/projede geliştirici olarak çalıştıysan (ör. dashboard işi) ekle; yoksa bu kaydı atla.

| Alan | Değer |
|---|---|
| Title | gerçek unvanın, ör. `Junior Software Developer` |
| Company | gerçek şirket adı |
| Location | şehir, ülke |
| Dates | gerçek başlangıç–bitiş |

**Description** şablonu (max 500) — köşeli parantezleri gerçek bilgiyle doldur, bilmediğini sil:

```text
Developed and maintained [web/internal] applications for [company type]. Worked with HTML, CSS, [PHP / C# / Python], and [React/TypeScript] on [what you built, e.g., an internal management dashboard]. Responsible for [bug fixing, new features, data handling]. Delivered [1–2 concrete outcomes you can defend in an interview].
```

---

## 7. Education (+20%)

Sıralamaya etkisi yok ama tamamlanma yüzdesine +20. Doğru olanı gir: bitmemiş bölüm için "Attended" seçilebilir; lise de sayılır. Alanlar: School · Degree · Field of study · Dates · Description (boş bırakılabilir).

---

## 8. Portfolio (+20%) — 4 madde

Her madde için: Title → Role → Description → Skills (5) → Project URL → görseller → Completion date (yayınladığın ay). "Related Upwork jobs" boş kalır (henüz yok). Kapak görseli olarak `*-cover-4x3.png` dosyasını seç; galeriye desktop, mobil ve tam sayfa görselleri ekle.

### Portfolio 1 — CoolAir HVAC

**Title** (max 70):

```text
HVAC Landing Page — CoolAir HVAC demo, mobile-first, click-to-call
```

**Role** (max 100):

```text
Web developer — layout, hand-coded HTML/CSS, copy structure, mobile optimization, deployment
```

**Description** (max 600):

```text
Demo landing page for a Dallas HVAC company, built to show local service businesses what a conversion-focused site looks like. Split hero with rating badge and two calls to action, stats bar (years, rating, response time, guarantee), services grid, customer reviews, service-area list, FAQ and a sticky tap-to-call button on mobile. Hand-coded HTML and CSS with no page builder, so the page stays light and fast on mobile data. Same-day and 24/7 messaging, upfront-pricing copy and click-to-call phone links throughout. Live: djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/
```

- **Skills (5):** Landing Page · HTML · CSS · Responsive Design · Web Design
- **Project URL:** https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/
- **Görseller:** `hvac-cover-4x3.png` (kapak) · `hvac-desktop.png` · `hvac-mobile.png` · `hvac-desktop-full.jpg`

### Portfolio 2 — ProFix Plumbing

**Title** (max 70):

```text
Emergency Plumbing Landing Page — ProFix Plumbing demo, call-first
```

**Role** (max 100):

```text
Web developer — emergency-style UX (alert bar, sticky call header), hand-coded HTML/CSS, mobile QA
```

**Description** (max 600):

```text
Demo landing page for a 24/7 emergency plumber in Phoenix, built for one job: get a stressed homeowner to call. Red emergency alert bar with the phone number, sticky header with a call button, hero promising a 60-minute response, stats bar (years, rating, response time, jobs completed), six-service grid, customer reviews, service-area list, FAQ and a final call-to-action block. Hand-coded HTML/CSS, mobile-first, click-to-call on every phone number. Pairs with the CoolAir HVAC demo for comparing two local-service layouts. Live: djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/
```

- **Skills (5):** Landing Page Design · Web Development · HTML · CSS · Mobile UI Design
- **Project URL:** https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/
- **Görseller:** `plumbing-cover-4x3.png` (kapak) · `plumbing-desktop.png` · `plumbing-mobile.png` · `plumbing-desktop-full.jpg`

### Portfolio 3 — Portfolio sitesi

**Title** (max 70):

```text
Web Developer Portfolio Site — services, pricing and live demos
```

**Role** (max 100):

```text
Web developer — design, copy, hand-coded HTML/CSS, GitHub Pages deployment
```

**Description** (max 600):

```text
My own business site, built the same way I build client sites. Dark hero with an at-a-glance panel (48-hour delivery, response time, starting price), three service cards with upfront pricing, two live demo projects, a four-step "how I work" process and an FAQ. Hand-coded HTML/CSS, mobile-first, deployed on GitHub Pages. Every claim on the page is something a client can verify by clicking: the demos are live and the prices are the ones I quote. Live: djoguzhan1.github.io/web-dev-portfolio/
```

- **Skills (5):** Web Design · HTML · CSS · Responsive Design · Website Copywriting
- **Project URL:** https://djoguzhan1.github.io/web-dev-portfolio/
- **Görseller:** `portfolio-home-cover-4x3.png` (kapak) · `portfolio-home-desktop.png` · `portfolio-home-mobile.png` · `portfolio-home-desktop-full.jpg`

### Portfolio 4 — Spreadsheet cleanup örneği

Üçüncü hizmetin görsel kanıtı. Görsel sentetik veriyle hazırlandı ve üzerinde "Sample data (synthetic)" yazıyor; açıklama da bunu söylüyor. Gerçek müşteri gibi sunma.

**Title** (max 70):

```text
Spreadsheet Cleanup — Excel / Google Sheets before-and-after sample
```

**Role** (max 100):

```text
Spreadsheet cleanup — deduplication, format normalization, formula repair, summary rows
```

**Description** (max 600):

```text
Sample cleanup built on synthetic data to show the delivery standard for Excel and Google Sheets work. Before: a raw export with duplicate customers, nine phone formats, eight date formats, mixed-case emails, blank cells and broken totals (#VALUE!, #REF!). After: one header row, one format per column (phones, ISO dates, currency), duplicates removed, missing or non-numeric values flagged instead of guessed, working SUM and AVERAGE rows, frozen header with filters, and a short notes line explaining every change. Typical turnaround for a file like this: 1–2 days.
```

- **Skills (5):** Microsoft Excel · Google Sheets · Data Cleaning · Spreadsheet Skills · Data Entry
- **Project URL:** boş bırak (veya portfolio sitesinin Excel bölümü)
- **Görseller:** `sheets-cleanup-sample-4x3.png`

---

## 9. Other experiences (+5%)

**Subject:**

```text
Self-directed project: local-business landing page series (2026)
```

**Description:**

```text
Designed and built two complete demo sites (CoolAir HVAC, ProFix Plumbing) and a portfolio site to a client-ready standard: mobile-first layouts, click-to-call, review, FAQ and service-area sections, hand-coded HTML/CSS, deployed on GitHub Pages. Used as live, clickable proof for clients before hiring.
```

Gerçekten tamamladığın bir bootcamp / kurs varsa ikinci kayıt olarak ekle (kurum adı, yıl, ne öğrendiğin — 2 cümle).

## 10. Linked accounts (+10%)

- **GitHub** → `github.com/djoguzhan1` (demoları barındırıyor; en alakalı bağlantı). `web-dev-portfolio` reposunun public olduğundan ve README'sinde canlı demo linklerinin bulunduğundan emin ol.
- Stack Overflow hesabın varsa onu da bağla; yoksa açma.

## 11. Certifications (+10%)

Sahte sertifika yok. Elinde yoksa, hizmetlerinle doğrudan ilgili ve ücretsiz alınabilen seçenekler — **bitirdikten sonra** ekle:

- Google Analytics Certification (Skillshop, ücretsiz, birkaç saat) — landing page müşterileri ölçüm sorar.
- Yoast "SEO for beginners" (ücretsiz, sertifikalı) — local SEO argümanını destekler.
- freeCodeCamp "Responsive Web Design" (ücretsiz; uzun ama HTML/CSS iddianı belgeler).

Upwork'ün Certifications alanı listeden seçtirir; sertifika listede yoksa "Other experiences" altına yaz.

## 12. Video introduction (+10%)

Kayıt: telefon göz hizasında, gün ışığı, sade arka plan, lense bak, tek çekim yeter. YouTube'a **unlisted** yükle, linki Upwork'teki "Video introduction" alanına yapıştır. Hedef süre 50–60 saniye.

**Senaryo (~150 kelime, sakin tempoda ~60 saniye):**

```text
Hi, I'm Oğuzhan, a web developer based in Turkey working with local service businesses in the US and UK.

If your WordPress site is slow or broken, I find the root cause and fix it in 24 to 48 hours. If you don't have a site yet, I build one-page landing sites for HVAC, plumbing and contractor businesses — fast, mobile-first, with a tap-to-call button, reviews and an FAQ. I also clean up Excel and Google Sheets files.

Before you hire me, you can click through two live demo sites on my profile: a CoolAir HVAC page and an emergency plumbing page. They're built exactly the way I would build yours.

I reply within an hour, you get a fixed price before any work starts, and revisions are included.

Send me your site URL or your business type, and I'll come back with a quote and a delivery date. Thanks.
```

## 15. Profil fotoğrafı

Mevcut fotoğraf siyah-beyaz ve el yüzü gölgeliyor. Upwork'ün kendi önerisi: renkli, aydınlık, önden, omuz hizası, sade arka plan, hafif gülümseme. Sıfır yorumlu profilde fotoğraf güvenin büyük kısmını taşıyor; 5 dakikalık iş, etkisi yüksek.

## 16. Availability

- Hours per week → **More than 30 hrs/week**
- Profile visibility → **Public** (zaten öyle)
- "Available now" rozeti → opsiyonel; Connects harcar, ilk 2–3 hafta açık tutmak yeni profile görünürlük sağlar.

---

## 17. Project Catalog — 3 ilan

Find Work → Your services → Create Project. Başlığa "You will get" yazma; Upwork ekliyor. Kategori seçiminde "Other" seçme; en yakın Web Development / WordPress / Data Entry seçeneğini al. Her ilan Upwork onayından geçer (birkaç gün).

### İlan 1 — WordPress fix

**Title** (max 75):

```text
your WordPress bug or speed problem fixed in 24–48 hours
```

- **Category:** Development & IT → Web Development (WordPress seçeneği varsa onu al)
- **Search tags (5):** wordpress bug fix · wordpress speed optimization · wordpress error · elementor fix · wordpress maintenance
- **Kapak görseli:** `portfolio-home-cover-4x3.png`

**Paketler:**

| | Starter | Standard | Advanced |
|---|---|---|---|
| Price | $49 | $99 | $179 |
| Delivery | 2 days | 3 days | 4 days |
| Revisions | 1 | 2 | 3 |
| Scope | One WordPress issue fixed (layout, plugin conflict, mobile bug, error message). Root-cause fix, not a patch. Before/after screenshots. | Up to 3 issues fixed + speed tune-up: caching, image compression, script cleanup. Before/after PageSpeed report. | Full site health pass: all reported bugs, speed optimization, mobile check on real devices, safe plugin/theme update pass with backup, 7-day post-delivery support. |

- **Add-ons:** Extra-fast delivery (24h) +$25 · Additional issue +$25

**Description** (min 120, max 1200):

```text
Slow or broken WordPress site? I fix the cause, not the symptom.

What I fix: broken layouts after an update, Elementor or theme display problems, plugin conflicts, mobile issues, contact forms not sending, error messages, slow load times.

How it works: you send the site URL, a short description of the problem and a temporary admin login. I reproduce the issue, take a backup, fix it, and send before/after screenshots or a PageSpeed report. Fixes are delivered in 24–48 hours.

Speed work includes caching setup, image compression, removing unused scripts and database cleanup, measured with Google PageSpeed Insights before and after.

I am new to Upwork, so pricing is intro-level. Delivery standards are not. Not sure which tier fits? Message me with your URL and I will tell you before you order.
```

**Requirements (müşteriye sorular):**

1. (Mandatory) Site URL
2. (Mandatory) Describe the problem: what happens, on which page, since when. Screenshots help.
3. (Mandatory) Create a temporary Administrator user for me and share it via Upwork messages. You can delete it after delivery.
4. (Optional) Hosting provider and whether you have a recent backup.

### İlan 2 — Landing page

**Title** (max 75):

```text
a one-page landing site for your HVAC, plumbing or contractor business
```

- **Category:** Development & IT → Web Development (veya Web & Mobile Design → Landing Page varsa)
- **Search tags (5):** landing page · hvac website · plumbing website · local business website · one page website
- **Kapak görseli:** `hvac-cover-4x3.png`; galeriye `plumbing-cover-4x3.png` ve mobil görseller

**Paketler:**

| | Starter | Standard | Advanced |
|---|---|---|---|
| Price | $129 | $249 | $399 |
| Delivery | 2 days | 3 days | 5 days |
| Revisions | 1 | 2 | 3 |
| Scope | One-page site, up to 6 sections (hero, services, why-us, reviews, FAQ, contact), mobile-first, tap-to-call, your logo and colors, delivered as ready-to-upload files. | Starter + service-area section, contact form, Google Maps embed, on-page SEO (titles, meta, LocalBusiness schema), speed check, hosting setup help (GitHub Pages, Netlify or your host). | Standard + built on WordPress so you can edit it yourself (or up to 3 static pages), Google Business Profile link-up, image optimization, 14-day post-launch support. |

- **Add-ons:** Extra section +$25 · Copywriting from your notes +$40 · Extra-fast delivery (24h) +$50

**Description** (min 120, max 1200):

```text
A one-page website built for one job: turning visitors into phone calls.

Who it is for: HVAC, plumbing, electrical, roofing, cleaning and other local service businesses in the US and UK that need a professional site fast.

What you get: a mobile-first page with a clear hero and call to action, services, trust points (licensed, insured, response time), customer reviews, FAQ, service areas and a tap-to-call button that follows the visitor on mobile. Hand-coded HTML/CSS with no page-builder bloat, so it loads fast on a phone.

See it before you buy: two live demos are on my profile, a CoolAir HVAC page and a ProFix emergency plumbing page. Your site is built to the same standard, in your colors, with your logo, phone number and service list.

Process: send your business details (requirements below). First version in 48 hours on Starter. Revisions included. You receive the files plus setup help, or I install it for you.

Questions about scope or hosting? Message me first. I answer within an hour.
```

**Requirements:**

1. (Mandatory) Business name, city / service area, phone number, opening hours.
2. (Mandatory) Your top 4–6 services and one or two things that make you different (licensed, same-day, family-owned, years in business).
3. (Optional) Logo and brand colors, or write "no logo yet".
4. (Optional) 3–5 real customer reviews you have permission to publish.
5. (Optional) Photos of your team, trucks or finished work.
6. (Optional) Do you already have a domain or hosting? Which provider?

### İlan 3 — Excel / Google Sheets

**Title** (max 75):

```text
your Excel or Google Sheets file cleaned, fixed and organized
```

- **Category:** Admin Support → Data Entry (veya Data Cleaning seçeneği varsa)
- **Search tags (5):** excel cleanup · google sheets · data cleaning · excel formulas · spreadsheet dashboard
- **Kapak görseli:** `sheets-cleanup-sample-4x3.png`

**Paketler:**

| | Starter | Standard | Advanced |
|---|---|---|---|
| Price | $35 | $75 | $149 |
| Delivery | 2 days | 2 days | 4 days |
| Revisions | 1 | 2 | 3 |
| Scope | 1 file, up to 2 sheets / 1,000 rows: remove duplicates, fix formatting and data types, repair broken formulas, consistent headers, frozen header row and filters. | Up to 5 sheets / 10,000 rows: Starter + lookup and summary formulas, data validation and dropdowns, a summary tab with totals, conditional formatting. | Standard + a dashboard tab with charts and pivot tables, simple automation (Google Apps Script or Excel macros) for repetitive steps, 7-day support. |

- **Add-ons:** Extra file +$20 · Short screen-recording walkthrough of the changes +$15

**Description** (min 120, max 1200):

```text
Messy spreadsheet slowing your team down? I clean it up and hand it back organized, with working formulas and a short note on what changed.

Typical jobs: customer or job lists with duplicates and inconsistent formatting, exports from invoicing or CRM tools that need restructuring, broken VLOOKUP or SUMIF formulas, and sheets that several people edit and nobody trusts anymore.

What you get: clean, consistent data (one header row, correct types, no duplicates), formulas that work and are easy to follow, filters and frozen headers, and on higher tiers a summary tab or dashboard with charts. Google Sheets or Excel, your choice.

Your data stays private: I work only inside the file you share, delete my copy after delivery, and can sign a simple NDA if you need one.

Delivery in 1–2 days for most files. Not sure which tier? Send the file or a screenshot and I will tell you before you order.
```

**Requirements:**

1. (Mandatory) Upload the file, or share a Google Sheets link with edit access.
2. (Mandatory) What should the finished file look like, and what do you use it for day to day?
3. (Mandatory, multiple choice) Deliver as: Excel (.xlsx) / Google Sheets / Both
4. (Optional) Any columns or sheets I must not touch.

---

## Bitirdikten sonra 5 dakikalık kontrol

- Profil "See public view" ile aç: başlık, overview ve 4 portfolio maddesi görünüyor mu?
- Overview'daki 3 link tıklanıyor mu (Upwork bazen düz metin gösterir; sorun değil, kopyalanabilir).
- Tamamlanma yüzdesi 100% olmalı; eksik kalan tek şey "Working style" testi olabilir (opsiyonel).
- Project Catalog ilanları "Under review" durumunda görünüyorsa tamam; onay birkaç gün sürer.
