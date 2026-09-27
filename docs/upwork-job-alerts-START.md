# Upwork bildirim — bugün başla (45 dk pilot)

Pilot bitince aynı adımları Q2–Q20 için tekrarla. Tam liste: [upwork-job-alerts-setup.md](./upwork-job-alerts-setup.md).

---

## Aşama 1 — Telegram (5 dk)

**Seçenek 1 — En kolay (önerilen ilk gün):** Sadece bot DM. UpHunt bağlandığında bildirimler **bot sohbetine** gelir; kanal açmana gerek yok.

**Seçenek 2 — Tek ekran (3 araç için):**

1. Telegram → **New Channel** → ad: `Upwork Jobs`
2. **Private channel** seç
3. Abone: sadece sen

Sonra UpHunt / Vibeworker / Upwatcher “Connect Telegram” dediğinde bu kanalı seç veya botu kanala **admin** ekle (araç talimatına uy).

**Telefon ayarı:** Kanal/bot sohbeti → bildirim **açık**, önemli / ses açık.

---

## Aşama 2 — UpHunt hesabı (5 dk)

1. https://uphunt.io → Sign up
2. **Connect Telegram** → Telegram’da “Allow” / kanalı seç
3. Ücretli plan: **çoklu feed** açık olsun (20 arama için)

---

## Aşama 3 — İlk Upwork araması (Q1 pilot) (10 dk)

1. Upwork → giriş → **Find Work**
2. Arama kutusuna **aynen** yapıştır:

```text
wordpress AND (broken OR "not working" OR error OR "white screen" OR "critical error" OR conflict OR bug) NOT woocommerce
```

3. Filtreler:

| Filtre | Değer |
| --- | --- |
| Sort | Newest |
| Posted | Last 24 hours |
| Payment verified | On |
| Job type | Fixed + Hourly |
| Budget | $20 – $1000 |
| Proposals | Less than 5, 5 to 10 |
| Experience | Entry, Intermediate |

4. **Save search** → isim: `Q01-WP-bug`
5. Tarayıcı adres çubuğundan **tam URL** kopyala (filtreler URL’de kalmalı)

---

## Aşama 4 — UpHunt’a feed (5 dk)

1. UpHunt → Add feed / New monitor
2. Ad: `Q01-WP-bug`
3. Upwork search URL yapıştır
4. Telegram kanalı seç
5. Kaydet

**Test:** Upwork’te kayıtlı aramayı aç; yeni ilan çıkana kadar bekle veya Q2’yi de ekle. İlk ping **&lt; 5 dk** hedef (çoğu zaman &lt; 2 dk).

---

## Aşama 5 — Kalan 19 arama (30–60 dk)

Her biri için: Upwork’te sorgu → aynı filtreler → Save → URL → UpHunt feed.

### Q02

```text
wordpress AND (slow OR speed OR "page speed" OR pagespeed OR "core web vitals" OR gtmetrix OR lighthouse)
```

### Q03

```text
elementor AND (fix OR broken OR mobile OR responsive OR "not working")
```

### Q04

```text
"landing page" AND (hvac OR plumbing OR plumber OR roofing OR electrician OR contractor OR "home services" OR cleaning OR landscaping OR locksmith)
```

### Q05

```text
("landing page" OR "one page website" OR "one-page website" OR "single page website") AND ("small business" OR local OR "google ads" OR leads)
```

### Q06

```text
("small business website" OR "simple website" OR "basic website" OR "5 page website" OR "3 page website") NOT (shopify OR react OR app)
```

### Q07

```text
("mobile friendly" OR "mobile responsive" OR responsive) AND (fix OR website) AND (html OR css OR wordpress)
```

### Q08

```text
("contact form" OR "form not sending" OR "form not working") AND (wordpress OR website)
```

### Q09

```text
("google sheets" OR excel OR spreadsheet) AND (formula OR formulas OR vlookup OR xlookup OR "pivot table" OR dashboard OR "clean up" OR cleanup OR "conditional formatting")
```

### Q10

```text
("google sheets" OR excel) AND (template OR tracker OR calculator OR "quick" OR urgent OR "small task")
```

### Q11

```text
(figma OR psd OR pdf OR xd) AND ("to html" OR "html css" OR "html/css" OR convert)
```

### Q12

```text
(wordpress OR website OR html OR css) AND (install OR setup OR "set up" OR migrate OR "small change" OR "small changes" OR "quick fix" OR tweak OR urgent OR asap OR "today")
```

### Q13

```text
(fix OR bug OR error OR broken OR "not working" OR debug) AND (html OR css OR javascript OR php OR python OR script OR website)
```

### Q14

```text
(script OR automate OR automation OR "automatic") AND (python OR javascript OR node OR "google sheets" OR "apps script" OR csv OR excel OR pdf)
```

### Q15

```text
(chatgpt OR openai OR gpt OR claude OR anthropic OR "ai") AND (integrate OR integration OR api OR automate OR chatbot OR prompt OR summarize)
```

### Q16

```text
(api OR webhook OR zapier OR make OR n8n) AND (connect OR integrate OR integration OR sync OR "send to")
```

### Q17

```text
("small task" OR "quick task" OR "one-time" OR "one time" OR "small job" OR "quick fix" OR "small project") AND (code OR script OR website OR fix OR python OR javascript)
```

### Q18

```text
("need help" OR "help me" OR "walk me through" OR troubleshoot OR "screen share") AND (code OR script OR website OR wordpress OR python OR excel OR sheets)
```

### Q19

```text
(deploy OR deployment OR hosting OR dns OR ssl OR "github pages" OR netlify OR vercel) AND (website OR site OR app)
```

### Q20

```text
(scrape OR scraping OR extract OR "pull data" OR "collect data") AND (website OR csv OR excel OR "google sheets") NOT (linkedin OR instagram OR facebook OR login)
```

---

## Aşama 6 — Yarın (yedek hatlar)

1. **Vibeworker Pro** → aynı 20 URL + push açık
2. **Upwatcher** → Q01–Q08 URL
3. **Freelancer Plus** + Upwork’te saved search bildirimleri

---

## Bana geri yaz (pilot bittiğinde)

- UpHunt’a bağlandın mı? (Evet/Hayır)
- İlk feed adı: Q01-WP-bug eklendi mi?
- İlk Telegram ping geldi mi? (Evet/Hayır — gelmediyse kaç dk bekledin)
- Ekran görüntüsü takılırsan: UpHunt feed ekranı + Upwork filtre ekranı

İlk gerçek ilan mesajını buraya yapıştır → gönder/atla + teklif metni yazılır.
