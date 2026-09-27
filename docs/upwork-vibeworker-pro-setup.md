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

Gecikme: genelde ilan sonrası **~2–5 dk** push (FAQ).

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

1. **Onboarding “Shortlist” kalite zinciri** (Step 4) — “sana ping atılmaya değer mi?” global eşikler. *All Jobs* ve *Shortlist* feed’lerine uygulanır (onboarding metni).
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

### Step 2 — Kategoriler (7 kutu)
- Web Development, Scripts & Utilities, AI Apps & Integration, Other - Software Development  
- Data Extraction/ETL, Data Analysis & Testing  
- DevOps & Solution Architecture  
- ❌ Ecommerce, Mobile, Design, Marketing, Admin, Engineering, Accounting, Writing, Legal, Translation…

### Step 3 — Referral
- **Skip**

### Step 4 — Shortlist zinciri (gevşet)
**Açık tut:** payment verified · hire rate **30%+** · client spent **$500+** (tek spend eşiği; $2k/$10k/$50k üst üste **kapalı**) · client rating **4.5+** (4.8 **kapalı**)

**Kapat:** hire rate 50% / 70% · spent $2k+ / $10k+ / $50k+ · **fixed price $100+** (WP $30–99 işleri için)

Hedef: ~**40–80 iş/gün** shortlist; demo listedeki $8k SaaS ilanları kategori genişliğinden — **preset exclude** ile kesilir.

### Step 5
- Bitir → ana uygulama

---

## 5) Kurulum bittikten sonra (sıra önemli)

### A) Pro
- Ayarlar / Upgrade → **Pro** ($19/ay). Ödeme: uygulama içi (Play) veya web.

### B) Hunting mode
- **Settings / Profile → Hunting mode → Quick Wins**

### C) Bildirim (Android)
1. Uygulama: **Settings → Notifications** (Vibeworker içi) → **Mobile push ON**, quiet hours **01:00–09:00** (Europe/Istanbul).  
2. Telefon: **Ayarlar → Uygulamalar → Vibeworker → Bildirimler** → açık, ses.

**Slack kullanma** (telefonda çalışmıyor). Telegram opsiyonel; istemezsen kapalı.

### D) Filter preset’ler (plan Q1–Q12 + Tier-3)

Her preset: **Payment verified**, Fixed + Hourly, **Mobile push ON** (bu preset için).

**Ortak exclude:** `woocommerce`, `shopify`, `react`, `react native`, `next.js`, `fullstack`, `saas`, `mobile app`, `squarespace`, `homework`, `nft`, `crypto`

| Preset adı | Min fixed $ | Include (örnek) | Bildirim |
|------------|-------------|-----------------|----------|
| WP-fix | 30 | wordpress, broken, elementor, plugin, mobile, contact form | Push ON |
| Landing-local | 80 | landing page, one page, hvac, plumbing, contractor, local | Push ON |
| Speed-mobile | 50 | page speed, pagespeed, lighthouse, slow, responsive | Push ON |
| Sheets-excel | 25 | google sheets, excel, vlookup, formula, cleanup, dashboard | Push ON |
| Scripts-AI | 40 | python, automation, apps script, openai, webhook, csv | Push isteğe bağlı |

**Skor eşiği** (preset’te varsa): başlangıç **quick-win ≥ 6** veya genel **6/10**; günde 40+ push → 7.

**Feed vs bildirim:** Bir preset’i sadece “browse” için feed’e, sadece WP-fix + Landing + Speed için push’a atayabilirsin (doküman: feed ve notification yüzeyleri ayrı atanabilir — uygulamada preset → Alerts).

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
| Yanlış işler ($8k fullstack) | Preset **exclude** kelimeleri; Step 4’te $100+ fixed kapalı mı |
| Çok az iş | Shortlist çok sıkı → Step 4 gevşet; min bütçe düşürme, exclude artır |
| Link açılmıyor | Free kotası — **Pro** |
| Slack | Vibeworker’da gerek yok |

---

## 8) Plan uyumu özeti

| 72h plan | Vibeworker karşılığı |
|----------|---------------------|
| Anlık bildirim | Pro + **mobile push** |
| Q1–Q12 niş | 4–5 preset + exclude |
| EV / Tier teklif | Değişmez; uygulama sadece alarm |
| 0 review | **Quick Wins** + düşük quick-win eşiği değil, **scope clarity** öncelik |
| Slack/Telegram | Opsiyonel; sen: **sadece push** |

---

## 9) Destek

hello@tryvibeworker.com · Uygulama içi yardım.
