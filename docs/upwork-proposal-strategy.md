# Upwork teklif stratejisi — $50–150 işler, 0 review, maksimum dönüşüm

**Son güncelleme:** 2026-09-27
**Kapsam:** Filtreden geçmiş (“çok uygun”) bir ilana atılan **teklif mesajı** ve sonrasındaki **kapanış sohbeti**. 72h plan (`docs/upwork-72h-first-job-plan.md`) aynen geçerli; bu doküman onun üstüne **teklif katmanı**dır.
**Kural:** Abartı yok, sahte deneyim yok, Upwork dışı iletişim yok, “Dear client / honored / passionate” yok.

---

## 0) Dürüst hedefler

Piyasa gerçeği ($50–150, 10–20 teklifli ilanlar): ortalama freelancer **%5–10 cevap**, **%2–4 hire/teklif**. Bu stratejiyle gerçekçi hedef:

| Metrik | Ortalama | Hedef (bu strateji) |
| --- | --- | --- |
| Müşteri teklifi görüntüledi | %40–50 | **%70+** (hız + ilk 2 cümle) |
| Görüntüleyen → cevap | %10–20 | **%35–50** (mini denetim + ücretsiz teşhis teklifi) |
| Cevap → hire | %20–30 | **%50–60** (kapanış oyun kitabı) |
| **Hire / teklif** | %2–4 | **%12–20** |

%75 cevap / %80 kapanış tek tek ilanlarda olur; ortalama olarak hiçbir freelancer’da yok. **%2–4 → %12–20** = 4–6 kat; günde 7–10 teklifle **haftada 5–10 kapanış** demek. Asıl kazanç ilk 3–5 review.

---

## 1) Müşterinin 5 korkusu → her teklifte 5 cevap

$50–150’lık işi veren küçük işletme sahibi şunlardan korkar. Teklifin **her biri için tek satır** içermeli:

| Korku | Teklifteki cevap (tek satır) |
| --- | --- |
| **Ghost / gecikme** | Somut teslim: “done by Tuesday 3pm ET” + “online until 6pm your time” |
| **Siteyi daha kötü hale getirme** | “Full backup first, staging where your host has it, live only after you approve” |
| **Gizli maliyet** | Fixed price + numaralı teslimat listesi + “anything outside → one-line quote first” |
| **İletişim / dil** | Kısa, net İngilizce; “3-line update start and end of each day, your time” |
| **Kalitesiz freelancer** | **Kanıt**: sitesine bakılmış 3 bulgu + tek demo/repo linki + Lighthouse rakamı |

---

## 2) Ön koşul (dönüşüm tavanı)

Teklif ne kadar iyi olsa da müşteri profile tıklar. Eksikse tavan düşer:

- İngilizce başlık + overview (`docs/upwork-profile.md`)
- Saatlik ücret **$15–25** görünür ($3 = güven kaybı)
- Kimlik doğrulandı rozeti
- 6 portföy kalemi + canlı linkler (`docs/upwork-portfolio/README.md`)
- Net, renkli, yüz görünen fotoğraf
- GitHub bağlı, employment girilmiş, %100 tamamlanma

---

## 3) Teklif öncesi mini denetim (5–10 dk) — asıl silah

Diğer 15 kişi “I can do this” yazar. Sen **onların sitesine bakmış** olursun. Süre kısıtlı olduğu için iş tipine göre sabit checklist:

### 3.1 WordPress fix / mobil / form (URL varsa) — 6 dk

1. **Telefonda aç** (gerçek cihaz) + Chrome DevTools iPhone görünümü → gözle görülen 3 sorun (menü, overlap, CTA fold altında, form).
2. **View-source** → tema (`/wp-content/themes/AD/`), builder (elementor / divi / wpbakery), gördüğün plugin’ler (contact-form-7, wpforms, revslider, woocommerce), cache (wp-rocket, litespeed, w3tc).
3. **PageSpeed Insights** mobil: skor, LCP, en büyük görsel → ekran görüntüsü.
4. **Console**: hata sayısı ve kaynağı (“3 errors, one from the slider plugin”).
5. **Form**: alanlar, reCAPTCHA var mı; **test gönderimi yapma**.
6. Padlock / mixed content.

Çıktı: **3 bulgu** = 1 “kendin yapabilirsin” ipucu (karşılıklılık) + 2 “bunu ben düzeltirim”.

### 3.2 Hız — 6–8 dk

PSI mobil + masaüstü; LCP elemanı; toplam sayfa ağırlığı (Network); optimize edilmemiş görsel sayısı; render-blocking script; cache header var mı; font yükü. Hedef skoru **yazılı** söyle (“from 41 to 85+”).

### 3.3 Yerel landing page ($100–150) — 15–20 dk

Demo (HVAC/Plumbing) kopyası → **işletme adı, şehir, telefon, ana renk** değiştir → masaüstü 1600×1000 + telefon 390×844 ekran görüntüsü → tek PNG’de yan yana. **Yayınlama, sadece görüntü.** Mevcut siteleri varsa 3.1’den 2 bulgu ekle (“current page has no call button above the fold”).

### 3.4 Sheets / Excel — 8–12 dk

Anlattıkları yapıyı **5 sahte satırla** kur; formül yaklaşımını göster (XLOOKUP, koşullu biçim); kenar durumları yaz (boş satır, mükerrer, karışık tarih formatı). Ekran görüntüsü veya **view-only** link.

### 3.5 URL yok / brief belirsiz — 3 dk

Denetim yok. **P0 şablonu**: “URL gönder, 30 dk içinde ne olduğunu ve sabit fiyatı yazayım — ücretsiz.” Bu, cevap oranının en ucuz kaldıracı.

---

## 4) Örnek / kanıt sunma matrisi

“Örnek sunacak mıyız?” → **Her zaman, ama tek tip değil.**

| İş | Bütçe | Sunulan kanıt | Biçim | Süre |
| --- | --- | --- | --- | --- |
| WP fix, URL var | $30–80 | 3 bulgu + işaretli telefon ekran görüntüsü | 1 PNG ek | 6–8 dk |
| WP fix, URL var | $80–150 | Üstteki + **60–90 sn Loom** | PNG + link | 12–15 dk |
| Hız | her | PSI mobil ekranı + LCP elemanı; opsiyonel Loom | 1 PNG (+link) | 6–10 dk |
| Landing | $100–150 | **Kişiselleştirilmiş hero mock** + demo linki | 1 PNG + 1 link | 15–20 dk |
| Landing | <$100 | Demo linki + 8 bölüm listesi | metin + 1 link | 5 dk |
| Sheets | $35–150 | 5 satırlık mock | PNG veya view-only | 8–12 dk |
| URL yok | her | Ücretsiz teşhis teklifi + demo linki | metin + 1 link | 3–4 dk |

**Kurallar:**
- **Tek link.** İşe en yakın demo veya repo. Portföy dökümü yok.
- **Tek ek**, anlamlı ad: `acmeplumbing.com – mobile – 3 fixes.png`. PNG, <5 MB, 3 kırmızı daire + numaralı not.
- **Çözümü verme, nedeni ver.** “Header’daki 80px sabit yükseklik” de; CSS kodunu yazma. “20 dakikalık iş, girince hallederim.”
- **Loom** (ücretsiz): ekran + isteğe bağlı yüz balonu; İngilizce konuşmak rahat değilse **ekran + yazılı notlar**, ses yok. İçinde iletişim bilgisi yok. Başlık: `yoursite.com – 3 fixes – Oğuzhan`. Akış: 10 sn “I’m on your site on my phone” → 40 sn 3 bulgu → 20 sn “this page is the standard I’d deliver” (demo) → 10 sn “Hire and I start within the hour”.
- Mock/denetim yapılmaz: bütçe <$40, 20+ teklif, ilan >45 dk (plan), URL yok. O zaman P0 veya atla.

---

## 5) Teklif anatomisi (7 blok, 150–220 kelime)

Müşteri listede **ad, foto, başlık, ücret, ilk 2 cümle** görür. Uma da teklif metninde ilanın anahtar kelimelerini arar.

| # | Blok | İçerik |
| --- | --- | --- |
| 1 | **Cümle 1 — onların sorunu + senin bulgun** | Sitenin adı, gördüğün somut şey, muhtemel neden |
| 2 | **Cümle 2 — ne yapılır + ne zaman** | Süre (“about an hour”, “48 hours”) + bugün/tarih |
| 3 | **Bulgular** | 3 madde: 1 ücretsiz ipucu + 2 düzeltilecek; “screenshot attached” |
| 4 | **Teklif** | “Fixed price $X, done by DAY TIME ET” + 3 numaralı teslimat + backup/staging + garanti |
| 5 | **Kanıt** | Tek link + Lighthouse/test rakamı; 0 review cümlesi (dürüst, 1 satır) |
| 6 | **Tek akıllı soru + sonraki adım** | Uzmanlık gösteren soru; “Hire → fund milestone → I start within the hour”; online saati |
| 7 | **İmza** | Sadece `Oğuzhan` |

**İlk 2 cümle — kötü vs iyi**

- Kötü: `Hi, I'm a web developer with experience in WordPress and I can fix your site quickly.`
- İyi: `The menu on acmeplumbing.com opens behind the hero image on iPhone — it's the header's fixed height in the Astra custom CSS, about an hour to fix, and I can have it live today.`

“Hi” ile başlama; **sitenin adıyla** veya **onların kelimesiyle** başla.

---

## 6) İnsan hissi (yazım kuralları)

- Onların kelimelerini kullan (“looks off on iPhone” dediyse “iPhone” de, “mobile devices” deme).
- **Sadece bakan birinin fark edeceği 1 detay**: footer telefonu ile header telefonu farklı; 2023 tarihli “Christmas special”; boş “Testimonials” bölümü.
- Kısaltmalar: I’d, you’ll, it’s. Bir yerde 6 kelimelik cümle.
- Rakam: 2.3 MB, 4.1 s, 3 errors, 41 → 85.
- Saat dilimi ve saat: “It’s 10am in Atlanta as I write this.”
- Tek ünlem en fazla; emoji yok; “hope this finds you well” yok.
- En fazla 3 madde işareti; duvar metin yok.
- “I” ile başlayan cümle **en fazla 2**.
- Her teklifte ilk cümle farklı — şablon kokusu **ilk cümlede** anlaşılır.
- Yıl/deneyim iddiası yok; doğrulanabilir şey söyle (demo, skor, repo, test sayısı).

---

## 7) Şablonlar (İngilizce) — köşeli parantezler zorunlu doldurulur

### P1 — WordPress fix / mobil / form (URL var)

```text
[SITE] on an iPhone: [VISIBLE ISSUE 1 — e.g. the menu opens behind the hero image] and [VISIBLE ISSUE 2 — e.g. the "Get a quote" button sits below the fold], so most phone visitors never get to the call. Both come from [LIKELY CAUSE — e.g. the header's fixed height in the theme's custom CSS]; it's about [TIME] of work and I can have it live [today / by DAY].

What I checked in five minutes (screenshot attached): [FINDING 1], [FINDING 2 — e.g. 3 JavaScript errors on load, one from the slider plugin], and one thing you can do yourself right now: [FREE TIP — e.g. the 2.3 MB logo PNG; compressing it alone saves about a second].

Fixed price $[PRICE], done by [DAY, TIME ET]:
1. Fix [ISSUE 1] and [ISSUE 2] on all phone sizes — on staging first if your host has it, live after you approve
2. Full backup before I touch anything; before/after screenshots when I'm done
3. If the same issue comes back within 7 days, I fix it free. If I can't find the cause in the first hour, I'll say so and you pay nothing.

I'm new on Upwork, so instead of reviews here's work you can check on your phone: [DEMO LINK] — hand-coded, 99–100 on Google Lighthouse. Fixes get the same care.

One question: [SMART QUESTION — e.g. is the form on Contact Form 7 or WPForms? Same fix either way, it just changes whether I need SMTP access]. I'm online until [TIME] your time; on your side it's Hire → fund the milestone, and I start within the hour.

Oğuzhan
```

### P2 — Hız / Core Web Vitals

```text
[SITE] scores [SCORE] on mobile in PageSpeed right now, and most of it is one thing: [LCP ELEMENT — e.g. the 1.9 MB hero image loads at full size on phones] (report attached). Fixing that plus [SECOND CAUSE — render-blocking scripts / no caching / four font files] gets you to [TARGET]+ within 48 hours, without changing how the site looks.

In order: [1 — images to WebP/AVIF at the right sizes, lazy-load below the fold] · [2 — caching and minify with your host's tools or a cache plugin] · [3 — defer the scripts not needed above the fold]. Nothing exotic, nothing that breaks on the next WordPress update.

Fixed price $[PRICE], done by [DAY, TIME ET]:
1. Mobile score from [SCORE] to [TARGET]+ — same tool, same day — and Core Web Vitals in the green
2. Backup first, staging where your host offers it, before/after report with the numbers
3. 7 days of follow-up included if anything shifts

The standard I work to: [DEMO LINK] — my own pages score 99–100 on the same test. I'm new on Upwork, so this is priced to earn the review, not to cut corners.

If you can share WP admin (or a host login) after hire, I start within the hour. Online until [TIME] your time.

Oğuzhan
```

### P3 — Yerel landing page ($100–150)

```text
A [BUSINESS TYPE] landing page has one job: get the call. So I've already built the hero for [BUSINESS NAME] — screenshot attached — tap-to-call above the fold, service tiles and a review block, in your colours, for [CITY]. It's the same structure as this finished page: [DEMO LINK] — open it on your phone; the sticky call bar and the reviews do the heavy lifting.

Fixed price $[PRICE], first draft in 48 hours:
1. One page, hand-coded HTML/CSS (no page builder, so it loads in under 2 seconds): hero + call button, services, reviews, service areas, FAQ, contact form
2. Mobile-first, Lighthouse 95+ on all four scores, basic local SEO (title, meta, LocalBusiness schema, Google Maps embed)
3. Two rounds of changes; you get the files, plus setup on your domain if you want it

From you: logo (or just the name and colours), phone, 4–6 services, 3 reviews you already have, any photos — stock is fine to start.

I'm new on Upwork; the demo above is the standard, and you'll have a preview link within 24 hours of the milestone being funded, so you're never waiting in the dark. Online until [TIME] your time today.

Oğuzhan
```

### P4 — Sheets / Excel

```text
Your [SHEET DESCRIPTION] — I mocked it up with five sample rows to make sure I read it right (screenshot attached): [COLUMN] feeds [SUMMARY], duplicates get flagged instead of silently dropped, and blank rows don't break the totals. [SPECIFIC OBSERVATION — e.g. your date column mixes 03/04/2026 and 4 Mar; I'd normalise that first or every monthly total is wrong.]

Fixed price $[PRICE], delivered by [DAY, TIME ET]:
1. [DELIVERABLE — e.g. Summary tab with XLOOKUP, dropdowns and conditional formatting on your shared sheet]
2. A short note on how each formula works, so you can change it without me
3. One round of changes included

New on Upwork; this is the kind of work I do — a CSV/Excel clean-up tool with 27 tests: https://github.com/djoguzhan1/tidycsv. Share view access after hire and the first version is back within a few hours.

Oğuzhan
```

### P0 — URL yok / belirsiz brief (ücretsiz teşhis)

```text
"[CLIENT'S OWN PHRASE — e.g. the site looks off on mobile]" usually comes from one of three things: [CAUSE 1], [CAUSE 2] or [CAUSE 3] — and each is a different fix. Send me the URL and I'll reply within 30 minutes with exactly what's wrong and a fixed price. No charge, no obligation — and you'll know what to ask whoever you hire.

If it's what I expect, it's a one-day job: $[RANGE] fixed, full backup first, before/after screenshots, 7 days of follow-up. The standard I work to: [DEMO LINK] (open it on your phone). I'm new on Upwork, so I'm pricing to earn the review, not cutting corners.

Online until [TIME] your time.

Oğuzhan
```

### Eleme soruları

Soruları **ilk** ve **somut** cevapla; bulgularını tekrar kullan. “Why are you a good fit?” → 2 cümle: bulgu + kanıt linki. Boş bırakılan soru = teklif okunmaz.

---

## 8) Fiyat, milestone, garanti mekaniği

- **Bütçeye eşit veya altı** (bütçe dışı teklif alta düşer). Bütçe düşükse **fiyatı değil scope’u küçült**: “$49 = the menu and the form; the speed pass is a second milestone if you want it.”
- **$100–150 işlerde iki seçenek** (evet/evet): “Option A — the two fixes, $79. Option B — fixes + mobile pass on all pages + speed quick wins, $129.” <$60 tek fiyat.
- **Teklif ekranında milestone’ları yaz** (Upwork “by milestone”): `M1 Diagnosis + fix on staging — $X — [date]`, `M2 Live + before/after report — $Y — [date]`. ≤$80 tek milestone. Çoğu freelancer bunu boş bırakır.
- **Garanti** (Upwork mekaniğiyle uyumlu): “If the same issue comes back within 7 days, I fix it free.” + “If I can't find the cause in the first hour, I'll say so and you pay nothing.” (fonlanmış milestone iade edilir).
- **Saatlik ilan**: iki yol sun — “Hourly at $[20–25] with a 2-hour cap on the tracker, or fixed $[X] — your call.”
- **Ücretsiz deneme işi yok**; onun yerine $15–29 ilk milestone.
- Review karşılığı indirim **asla** (Upwork feedback manipülasyonu).

---

## 9) Duruma göre strateji

| Durum | Yapılacak |
| --- | --- |
| **Müşteri yanlış çözüm istiyor** (“install a speed plugin”) | Nazik düzeltme, kanıtla: “A cache plugin alone won't fix the 4.2 s LCP — the 1.9 MB hero image is the problem; that fix is included, and I'll add caching too.” Uzmanlık = güven. Küçümseme yok. |
| **İstenen şey bütçeye sığmaz** | Scope’u böl: “$150 covers the home page done properly; the other 4 pages are a second milestone at $X each.” |
| **Brief belirsiz, URL yok** | P0 — ücretsiz 30 dk teşhis. |
| **Eski freelancer kaçmış / şikayet var** (ilan veya geçmiş review’larda) | Onların acısını yansıt: “You'll get a 3-line update at 9am your time every day, even if it's just 'on track'.” |
| **Müşteri geçmişi: iletişim şikayeti** | Aynı satır + “Upwork messages, replies within the hour during your workday.” |
| **12+ ilan vermiş (Upwork tecrübeli)** | “Hire → fund milestone” anlatımını kısalt; doğrudan milestone metni. |
| **İlk ilanı (Upwork yeni)** | Adım adım: “On your side: open my proposal → Hire → fund $X. Money sits with Upwork until you approve.” |
| **Görüşme istiyor** | 10 dk Upwork call, **iki slot** onların saatinde bugün. Upwork dışı araç yok. |
| **“Are you an agency / where are you based?”** | “Solo, Bursa, Turkey (GMT+3) — online US mornings and the full UK day.” |
| **Reseller / ajans müşteri** | “Happy to work white-label; you own the files.” |
| **Nulled tema, black-hat SEO, login arkası scrape, ‘no AI tools’, ücretsiz test** | Gönderme. |
| **Davet (invite)** | Aynı yapı, 5 dk içinde; ilk cümle “Thanks for the invite —” + bulgu. |
| **20+ teklif almış ilan** | Denetim yapma; sadece P0/kısa versiyon veya atla. |
| **İlan güncellendi** | Teklifi **Edit** ile güncelle (Upwork izin verir). |

---

## 10) Cevap geldikten sonra: kapanış oyun kitabı

Cevap oranı teklife, **kapanış oranı ilk 3 mesaja** bağlıdır. Müşteri şu an online; **5 dk içinde** yaz (Upwork mobil bildirimi açık).

### R1 — İlk cevap (teşhis sözü verdiysen teşhisi getir)

```text
Thanks, [NAME]. Had a proper look at [SITE]: [FINDING 1 — cause], [FINDING 2 — cause]. Both are fixable today.

Here's the milestone text so you can paste it straight in: "[SCOPE LINE — e.g. Fix the mobile menu and the contact form on acmeplumbing.com; backup first; before/after screenshots] — $[PRICE], delivered by [DAY, TIME ET]."

On your side it's Hire → fund the milestone; Upwork holds the money until you approve. I'm online for the next [N] hours and would start right away.

One thing I need after hire: [WP admin login / view access / the logo].
```

### R2 — “Can you do it cheaper?”

```text
Happy to make it fit. The price covers [3 things]; if budget is tight I'd rather drop [ITEM 3] than rush the other two — that brings it to $[LOWER]. Which matters more to you, [ITEM 2] or [ITEM 3]?
```

(Fiyatı değil scope’u küçült. Review karşılığı indirim **yok**.)

### R3 — “Others quoted less.”

```text
Understood. The difference is what's included: root-cause fix, backup, before/after report and 7 days of follow-up. If you'd like to compare like for like, ask them for the same three — and if the numbers still don't work, tell me which item to drop.
```

### R4 — “Let's have a call.”

```text
Sure — 10 minutes on an Upwork call is enough. Today I can do [TIME 1] or [TIME 2] your time; which works? If it's easier, send the login after hire and I'll walk you through what I find on a short screen recording instead.
```

### R5 — “Can you start with a small test?”

```text
I don't do unpaid tests, but I can make the first milestone small: [SMALLEST ITEM] for $[15–29], delivered today. If you like how that goes, the rest follows as a second milestone.
```

### R6 — Sessizlik

- **24 saat**: 1 yeni bulgu + milestone metni tekrar (plan follow-up).
- **48 saat**: “If you've gone another way, no problem — tell me and I'll close the thread.” (0 Connect, yüksek dönüşüm; çoğu yeni freelancer hiç yapmaz.)

### Hire sonrası ilk 60 dk (review’un temeli)

“Got it, thanks — backup taken, starting now. First update by [TIME].” → söz verilen saatte 3 satır güncelleme.

---

## 11) Gönderim öncesi 60 sn kontrol

- [ ] Sitenin adı ve müşteri adı doğru yazıldı
- [ ] İlk 2 cümlede **bulgu + süre** var; “Hi/I” ile başlamıyor
- [ ] Fiyat = bid tutarı = milestone toplamı
- [ ] Teslim tarihi **müşterinin saat diliminde**
- [ ] **Tek** link, **tek** ek (adı anlamlı), iletişim bilgisi yok
- [ ] Eleme soruları cevaplandı
- [ ] İlanın anahtar kelimeleri (plugin/tema/araç adı) metinde doğal geçiyor
- [ ] Yasaklı kelime yok (Dear, honored, passionate, ninja, guru)
- [ ] Tek soru soruldu; soru brief’te zaten cevaplanmış bir şey değil
- [ ] Yazım kontrolü; kelime sayısı 150–220

---

## 12) Ölçüm ve iterasyon

Takip tablosu (plan Ek A) + 4 sütun: **Denetim yapıldı (E/H) · Ek (E/H) · Loom (E/H) · Açılış tipi (A: bulgu-önce / B: sonuç-önce)**.

Haftalık bakış:

| Sinyal | Sorun | Tek aksiyon |
| --- | --- | --- |
| Görüntülenme <%50 | Hız veya ilk 2 cümle | İlan yaşı <10 dk’ya çek; açılışı sitenin adıyla başlat |
| Görüntülenme iyi, cevap <%25 | Kanıt zayıf / ask büyük | Her teklife ek + ücretsiz teşhis cümlesi |
| Cevap iyi, hire <%40 | Kapanış | R1’i 5 dk içinde, milestone metni hazır; iki seçenek fiyat |
| Hire var, review düşük riski | Teslim | Günlük güncelleme + before/after raporu |

A/B: 1. hafta açılış A vs B dönüşümlü; 2. hafta kazananla devam, Loom’lu vs Loom’suz test.

---

## 13) Asla yapılmayacaklar

- Genel teklif (site adı geçmeyen) göndermek
- 3+ link, PDF portföy dökümü, uzun özgeçmiş
- Deneyim yılı / müşteri sayısı uydurmak; “agency” demek
- Ücretsiz iş yapmak (teşhis evet, düzeltme hayır) — çözüm kodunu teklife yazmak
- Upwork dışı iletişim bilgisi, WhatsApp/e-posta, ödeme aracı adı
- Review karşılığı indirim veya “5 star” istemek
- Bütçenin üstüne teklif; ya da bütçeyi sorgusuz kabul edip scope’u belirsiz bırakmak
- Fonlanmadan işe başlamak
- Müşterinin “yanlış” çözümüne sessizce evet demek (dürüst düzeltme yap)
- Gece yarısı acele teklif (kalite < hız değil; **hız + kalite**)

---

## 14) Günlük akış (7–10 teklif, ~2 saat)

0. **REKABET kartı** (30 sn, teklif yazmadan): yaş, teklif sayısı, hız = teklif÷max(yaş_dk,5), 1. sıra Connect, Insights ort. teklif. Karar: `docs/upwork-job-alerts-setup.md` **§7.5 B** (R1–R9). **$80+ ve (teklif≥8 veya yaş&gt;30 dk) + boost yok → SKIP.**
1. Bildirim → 30 sn EV/Tier kararı (plan).
2. **Denetim** 5–10 dk (Bölüm 3) → 3 bulgu + ek.
3. Şablon seç (P0–P4) → köşeli parantezleri doldur → ilk 2 cümleyi **yeniden yaz**.
4. Milestone’ları teklif ekranında yaz; bid = fiyat.
5. 60 sn kontrol → gönder → log.
6. Cevap gelince 5 dk içinde **R1**; 24/48h takip.
7. Günün sonunda 5 dk: hangi açılış görüntülendi, hangisi cevap aldı; **T+24h** dolan satırlarda Insights → log `Rekabet (T+24h)`.
8. Haftada 1× (15 dk): `docs/upwork-proposal-log.md` haftalık rekabet özeti → §7.5 **D** ayar çek.

**Hedef ritim:** ilan 0–10 dk yaşındayken **denetimli** teklif; “çok uygun” 7–10 ilanın **hepsine** ek/denetim; boost yalnızca **REKABET R4** (kalabalık $80+ Tier-1, 1. sıra ≤12) — taze ilanda hız, kalabalıkta boost veya SKIP.

---

## 15) Bu stratejinin “aşırı artıran” 7 çekirdeği

1. **Mini denetim**: siteye gerçekten bakılmış 3 bulgu — rakiplerin %95’i yapmaz.
2. **Ücretsiz 30 dk teşhis teklifi**: cevap vermeyi kolaylaştıran küçük “evet”.
3. **Kişiselleştirilmiş kanıt**: onların adıyla hero mock / işaretli ekran görüntüsü / 60 sn video.
4. **Risk sıfırlama**: backup + staging + 7 gün + “bulamazsam ödeme yok”.
5. **Yapıştırılabilir milestone metni + iki seçenek**: müşteri düşünmez, tıklar.
6. **Somut zaman ve saat dilimi**: “by 3pm ET Tuesday”, “online until 6pm your time”.
7. **5 dk cevap + 24/48h takip**: kapanış sohbette olur; sohbeti sen yönetirsin.

---

## 16) Risk matrisi — “yapalım mı?” ve demo kararları

**İlke:** Dönüşümü artırmak için kanıt veriyoruz; **ücretsiz iş / IP kaybı / scope tuzaklarına girmiyoruz.** Her ilan önce **risk sınıfı**, sonra **GO/MAYBE/SKIP**.

### 16.1 Risk sınıfları

| Sınıf | Ne demek | Model (Cursor) | Karar |
| --- | --- | --- | --- |
| **🟢 Düşük** | Net scope, $50–150, URL var, Tier-1/2, payment verified, &lt;15 teklif, demo **istemiyor** (sadece portföy linki yeter) | **Composer 2.5** veya **Sonnet Thinking Low/Medium** | Sen onayla → GO |
| **🟡 Orta** | “Show sample / send example / see your work for **this** project”, belirsiz revizyon, 15–20 teklif, $40–49 sınırda, müşteri 0 hire | **Composer 2.5** veya **Sonnet Thinking Medium** | **MAYBE** → kanıt matrisinde **sınırda** olan (mock/Loom) |
| **🔴 Yüksek** | Ücretsiz test, “do a page first then we hire”, sınırsız revizyon, tüm siteyi yenile $80, production şifresi önce, Upwork dışı ödeme, akademik, scrape login, “no AI” + AI işi | **Sonnet/Opus Thinking High** veya **Opus** (ikinci görüş) | Varsayılan **SKIP**; nadiren **GO + sıkı milestone** |
| **⚫ Kesin SKIP** | Blacklist (plan Ek F4), Woo checkout, mobil app, retainer, CAPTCHA bypass | **Fast / kendin** — AI’ya bile sorma | SKIP |

**Kural:** 🟡 ve 🔴 için **asla Fast** ile “çok uygun” deme. 🔴’de model “GO” dese bile **senin veto** geçer.

### 16.2 “Demo / örnek” istekleri — ne verilir, ne verilmez

| Müşteri ne diyor | Risk | Yapılacak (teklifte) | Yapılmayacak |
| --- | --- | --- | --- |
| “Link to similar work” | 🟢 | Tek **HVAC/Plumbing demo** veya **GitHub repo** | Özel mock |
| “Can you look at my site and tell me what’s wrong?” | 🟢 | **P0**: URL → 30 dk yazılı teşhis (ücretsiz **söz**, düzeltme yok) | Canlıda kod değişikliği |
| “Send a screenshot of how you’d fix it” | 🟡 | **İşaretli ekran görüntüsü** (mevcut site); çözüm kodu yok | Tam sayfa tasarım |
| “Build a quick mockup / sample homepage before hire” | 🟡–🔴 | **$100+ landing:** 15 dk **hero mock** (görüntü only). **&lt;$100 veya fix:** “After milestone — preview in 24h” veya **$15–29 paid micro-milestone** | Tam site ücretsiz |
| “Free test / trial task / prove yourself” | 🔴 | **R5:** “$[15–29] milestone for [smallest item] today” | Ücretsiz iş |
| “We’ll pay after we see it” / off-platform | ⚫ | SKIP | Her şey |
| “Use our brand, send full Figma-ready design free” | 🔴 | SKIP veya paid milestone + IP “you own files after payment” | Ücretsiz tasarım |

**Portföy vs proje demosu:** HVAC/Plumbing = **genel kanıt** (🟢). İsim/renk mock = **sadece $100+ landing veya hire sonrası** (🟡); fix işinde mock **yok**, screenshot yeter.

### 16.3 “Biz yapalım mı?” — 60 sn insan kontrolü (AI’dan sonra)

AI çıktısından sonra sen şunlardan **biri** varsa veto veya MAYBE:

1. Gerçek efor **&gt;4 saat** ama bütçe **&lt;$80** → SKIP veya scope küçült (AI’ya sor: “effort honest?”).
2. İlanda **“unlimited revisions”** / **“until satisfied”** → MAYBE + teklifte **2 round** yaz; kabul etmezlerse SKIP.
3. **Demo/mock** isteniyor + bütçe **&lt;$70** → demo **yok**, paid micro-milestone veya SKIP.
4. Müşteri **0 hire** + **&lt;$50** + belirsiz → SKIP (plan müşteri filtresi).
5. **Yanlış çözüm** (sadece plugin) + düşük bütçe → GO only if teklifte dürüst düzeltme + dar scope.

### 16.4 Cursor model seçimi (özet)

```
İlan geldi
  → Blacklist / $15 / 50+ proposals? → SKIP (modele sorma)
  → Risk 🟢, $20–80 → Composer 2.5: karar + teklif
  → Risk 🟢/🟡, $80–150 → Claude Opus 5.5 Low: teklif metni
  → Risk 🟡 (demo/sample isteği, belirsiz revizyon) → Claude Opus 5.5 Medium
  → Risk 🔴 (free test, sınırsız revizyon, production erişimi) → Opus 5.5 High/Max: varsayılan SKIP
  → $120+ veya ilk 3 review için kritik iş → Opus 5.5 Medium/High
```

**Neden bu dağılım:** teklif yazmak muhakeme değil **talimat takibi** işi — 60 sn kontrol listesi, 150–220 kelime, tek soru, 3 madde. Bunun için güçlü yazım + kurala sadakat gerekir, yüksek düşünme modu gerekmez. Yüksek mod **karar** tarafında (risk sınıfı, efor tahmini, veto) değerlidir. Hız gerektiğinde (ilan <10 dk) Composer 2.5 veya `-fast` varyantları.

**Model performansını ölçmedim** — bu dağılım görev tipine göredir. Takip tablosuna “Model” sütunu ekle; 2 hafta sonra cevap oranı hangi modelde yüksekse ona geç.

**Haftalık bütçe mantığı:** ~25 ilan 🟢 (Composer) + ~8 🟡 (Opus Low/Medium) + ~2 🔴 (High) = risk kontrollü, fatura makul.

### 16.4b Teklif yazdırma prompt’u (kopyala-yapıştır)

Karar GO çıktıktan sonra, teklif metni için. Dosya referanslarını `@` ile ekle.

```text
@docs/upwork-proposal-strategy.md @docs/upwork-72h-first-job-plan.md @docs/upwork-profile.md

Bu ilana Upwork cover letter yaz. Strateji dokümanı bağlayıcıdır, özellikle Bölüm 5 (7 blok), Bölüm 6 (insan hissi), Bölüm 11 (60 sn kontrol).

İlan:
[PASTE — başlık, açıklama, bütçe, tip, ilan yaşı, teklif sayısı, Connects]
Müşteri: [ülke, rating, harcama, hire rate, açtığı ilan sayısı, geçmiş yorumlar]

ZORUNLU:
- 150–220 kelime. Metnin sonunda kelime sayısını yaz.
- TEK soru. TEK link. En fazla 3 madde işareti.
- İlk cümle: onların kelimesi veya site/ürün adı. "Hi" veya "I" ile başlama.
- "I" ile başlayan en fazla 2 cümle. Kısaltma kullan (I'd, you'll).
- Uydurma deneyim/yıl yok. 0 review cümlesi tek satır, dürüst.
- Somut rakam ve saat dilimi. İletişim bilgisi yok.
- Yasaklı: Dear, honored, passionate, ninja, guru, "hope this finds you well".
- Fiyat = bid = milestone toplamı.

Ayrıca ver:
1. Milestone açıklaması (tek satır, müşterinin yapıştırabileceği).
2. Kanıt kararı: none / screenshot / mock / loom — Bölüm 4 matrisine göre, bütçeyle uyumlu mu.
3. Bölüm 11 kontrol listesi: madde madde ✅/❌.
4. Eleme sorusu varsa cevapları.
5. Kural dışına çıktığın her madde + gerekçe (sessiz sapma yok).
```

### 16.5 Karar prompt’u (risk dahil — kopyala-yapıştır)

```text
Upwork ilan — risk-aware karar. Plan + proposal strategy. 0 review, $50–150 sweet spot.

İlan:
[PASTE]

Önce risk sınıfı: GREEN / YELLOW / RED / BLACK (gerekçe 1 cümle).
Demo/sample/free test isteği var mı? Ne tür? Matris 16.2’ye göre ne VERİLİR / VERİLMEZ.
Karar: SKIP | MAYBE | GO ("çok uygun" = GO).
Tier, EV 0–7, önerilen $, boost, şablon P0–P4.
RED flag listesi (varsa).
Eğer MAYBE: hangi koşulda GO (ör. "$29 micro-milestone kabul ederse").
Eğer GO: kanıt türü (none / screenshot / mock / loom) — bütçe ve risk kurallarına uygun mu?
Veto önerisi: AI GO dese bile sen SKIP demeli misin? (evet/hayır + neden)

Kısa Türkçe özet. GO ise İngilizce ilk 2 cümle.
Conservative bias: şüphede SKIP veya MAYBE, ücretsiz işe GO yok.
```

İlgili: `docs/upwork-72h-first-job-plan.md` (dal `cursor/upwork-72h-plan-5f90`) · `docs/upwork-profile.md` (dal `cursor/upwork-profile-5f90`) · `docs/upwork-job-alerts-setup.md`.
