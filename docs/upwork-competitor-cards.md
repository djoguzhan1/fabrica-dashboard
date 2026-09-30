# Rakip kart kütüphanesi + güçlendirilmiş hakem prompt'u

**Kullanım:** `upwork-opening-playbook.md` §12 müşteri simülasyonunda rakip alanı bu dosyadan kurulur. Amaç: hakem model **gerçek bir Upwork teklif listesi** görsün, bizim kart pipet rakiplere değil gerçek sahaya karşı sınansın.
**Kaynak:** r/Upwork'te müşterilerin ve freelancer'ların paylaştığı teklif örnekleri, GigRadar/Vollna/Upwex tarzı otomatik teklif araçlarının şablon çıktıları, Upwork Community'de "bu teklifi aldım" paylaşımları. Kartlar birebir kopya değil, **tip temsilcisi**; kelimeler ilana göre uyarlanır (`[ ]` alanları).

---

## 1) Gerçek saha nasıl görünür (müşterinin listesi)

Bir $100–300 WP/Sheets ilanına ilk 2 saatte gelen 15–25 teklifin tipik dağılımı:

| Tip | Pay | Kartta görünen |
| --- | --- | --- |
| **Bot / otomatik teklif** (GigRadar, Vollna, Upwex, kendi n8n'i) | %30–40 | AI yazımı, ilan başlığını tekrar eder, 30–90 sn içinde gelir, çoğu boost'lu |
| **Şablon veteran** (Top Rated, $20K–100K) | %20–25 | "I have carefully read…", rozet + JSS %98–100 |
| **Ajans hesabı** | %10–15 | "Our team", 50+ iş, hızlı, portföy yığını, $25–40/hr |
| **Ucuz toplu teklifçi** | %10–15 | $5–12/hr, "I can start now", kısa, hatalı İngilizce |
| **Özgül orta seviye** | %5–10 | 5–20 iş, somut açılış, JSS var |
| **Elit özgül veteran** | %3–5 | Teşhis + kanıt + rozet. **Asıl rakip.** |

Boost'lu ilk 4'te en sık: **bot + şablon veteran + ajans**; elit veteran nadiren boost basar (davetle geliyor). Yani ilk 4'te kartımız çoğunlukla bot ve şablona karşı, **ama müşterinin kafasındaki karşılaştırma** listenin tamamı.

---

## 2) Kart kütüphanesi (kartta görünen ~150 karakter + meta)

### T1 — Bot / otomatik teklif (her testte 2 tane)

| # | Meta | Kart metni |
| --- | --- | --- |
| B1 | JSS 96%, Top Rated, $18K, $25/hr, boosted, 40 sn'de geldi | "Hi there, I just reviewed your posting for '[ilan başlığı]' and I'm confident I can deliver exactly what you need with precision and quality." |
| B2 | JSS 100%, $9K, $30/hr, boosted | "I understand you need [ilan başlığındaki kelimeler]. I have extensive experience in [beceri 1], [beceri 2] and [beceri 3] and can start immediately." |
| B3 | Rozet yok, $2K, $20/hr | "Greetings! Your project caught my attention because it aligns perfectly with my expertise in [beceri]. Let me handle this seamlessly for you." |
| B4 | JSS 98%, Top Rated Plus, $45K, $35/hr, boosted | "Dear Client, I've gone through your requirements and I'm excited to help. As a seasoned [rol] I bring a proven track record of delivering high-quality results." |

Bot işaretleri (hakeme söylenir): ilan başlığını tırnak içinde tekrar, "precision/seamlessly/proven track record/aligns perfectly", 60 saniyeden hızlı gelme, her cümle aynı uzunlukta, ilana özgü hiçbir isim yok.

### T2 — Şablon veteran (her testte 1–2)

| # | Meta | Kart metni |
| --- | --- | --- |
| V1 | JSS 100%, Top Rated, $62K, 140 iş, $40/hr | "Hello! I have carefully read your job description and I'm confident I'm the perfect fit. With 9+ years in WordPress and Elementor, I've completed 140+ projects…" |
| V2 | JSS 99%, Top Rated Plus, $110K, $50/hr | "Hi, I'm [Ad], a senior WordPress developer with 10 years of experience. I've built and fixed 300+ websites for clients in the US, UK and Australia. Portfolio:…" |
| V3 | JSS 97%, Top Rated, $38K, $35/hr | "Hi [müşteri adı], I can definitely help with this. I specialize in exactly this kind of work and have done it many times before. Happy to hop on a quick call…" |

### T3 — Ajans (her testte 1)

| # | Meta | Kart metni |
| --- | --- | --- |
| A1 | Ajans, JSS 98%, $250K, 600 iş, $30/hr, boosted | "Our team of 12 WordPress experts has delivered 600+ projects on Upwork. We can assign a dedicated developer today and have your [iş] done within 48 hours." |
| A2 | Ajans, JSS 100%, $80K, $28/hr | "We reviewed your requirements and prepared a plan: (1) audit, (2) fixes, (3) QA on all devices. Our PM will be your single point of contact throughout." |

### T4 — Ucuz toplu teklifçi (her testte 1)

| # | Meta | Kart metni |
| --- | --- | --- |
| C1 | JSS yok, $600, $8/hr | "Hi sir, I can do this job perfectly. I am expert in wordpress elementor. I will start right now and finish today. Please check my profile. Thanks." |
| C2 | JSS 89%, $3K, $10/hr | "I can do it in 2 hours for $30. I have done 100+ same work. Message me." |

### T5 — Özgül orta seviye (her testte 1)

| # | Meta | Kart metni |
| --- | --- | --- |
| M1 | JSS 100%, 14 iş, $6K, $30/hr | "Looked at [site]: the mobile header overlaps the hero because the sticky section has no top padding. Quick fix, plus I'd check the other pages at 390 px." |
| M2 | JSS 94%, 22 iş, $11K, $28/hr | "For your [Sheets akışı], an onEdit trigger plus a MailApp call covers it; the only tricky part is duplicate rows, which I'd handle with a key column." |

### T6 — Elit özgül veteran (her testte **1, zorunlu**)

| # | Meta | Kart metni |
| --- | --- | --- |
| E1 | JSS 100%, Top Rated Plus, $64K, 210 iş, $45/hr | "Your mobile menu issue is almost always a z-index clash with the sticky header in Elementor. I fixed the same thing for 40+ sites, can do it today." |
| E2 | JSS 100%, Expert-Vetted, $150K, $60/hr | "Two things in your brief are connected: the slow LCP and the Elementor animations. Fix one and the other goes away. 2-min Loom on your site: [link]" |
| E3 | JSS 99%, Top Rated Plus, $88K, $40/hr | "I built the exact [form → Sheet → Slack] flow for [benzer sektör] last month; screen recording of it running: [link]. Yours would take ~2 days." |

E2 ve E3 **Loom veya link taşıyor**: yani "önce yap, sonra teklif et" ilkesini uygulayan rakip de var. Bizim fark: onlarınki **benzer** iş, bizimki **bu ilanın kendi sayfası/verisi**.

---

## 3) Alan kurma kuralı (her test için 8 kart)

| Slot | Tip | Not |
| --- | --- | --- |
| 1–2 | T1 bot | B1–B4'ten 2'si, ilana uyarlanmış; en az biri **boosted** işaretli |
| 3 | T2 şablon veteran | Boosted işaretli |
| 4 | T3 ajans | Boosted işaretli |
| 5 | T4 ucuz | — |
| 6 | T5 özgül orta | Rastgele |
| 7 | **T6 elit** | **Her testte zorunlu**; ilana uyarlanmış, gerçekçi teşhis içermeli |
| 8 | **Bizim kart** | Meta: JSS yok, rozet yok, $30/hr, boosted |

Bizim kart dahil **4 kart boosted** işaretlenir (gerçek ilk 4). Sıra 2 kez karıştırılır. Hakemden puan değil **davranış** istenir.

**Elit kartı zayıflatma yasağı:** E kartını ilana uyarlarken teşhisi gerçekçi ve doğru tut. Elit veteranı yenemeyen kart gönderilmez.

---

## 4) Güçlendirilmiş hakem prompt'u (tek çağrı, hakem = yazan modelden farklı aile)

```
You are simulating three real clients who posted the Upwork job below. You are NOT an assistant; you are busy buyers with money on the line.

JOB POST (verbatim): <ilan>
CLIENT FACTS: <ülke, toplam harcama, hire rate, ort. saatlik, önceki yorumlar, ilan yaşı, teklif sayısı>

PERSONAS (answer as each, separately):
P1 "Owner in a hurry": runs the business, 3 minutes for this, wants it fixed and gone.
P2 "Technical reviewer": has built sites/sheets before, spots hand-waving instantly.
P3 "Budget-sensitive": has been burned by an overpriced freelancer, checks rate and scope first.

None of you will do calls. All of you have received AI-written proposals before and resent them.

You see 8 proposal cards. Each shows: name, photo note, hourly rate, badges/JSS, "Boosted" flag, time since posting, and the first 150 characters of the cover letter. Nothing else.

CARDS (order A): <8 kart>

TASK 1 (each persona): You have time to open only 2 cards. Which 2? One line why each. Which cards do you assume are bots or templates, and why?
TASK 2: Same 8 cards in order B: <karıştırılmış>. Repeat Task 1. If your choice changed, say why.
TASK 3 (only for cards opened by ≥2 personas): read the full cover letter and the attached image description.
  For each persona: would you message this freelancer today, yes/no? What sentence almost made you skip? What would have made you message instantly?
  Rank all opened proposals from "hire first" to "pass".
TASK 4: Is there anything in the no-JSS freelancer's proposal that you cannot verify and would distrust? Anything that reads as AI-written?

Rules: no praise, no hedging, no "it depends". Be the kind of client who skips 20 proposals in a minute.
```

**Geçme eşiği (tek çağrıdan):**
- Task 1 ve 2: bizim kart **3 personadan en az 2'sinde**, **iki sırada da** açılan 2 karttan biri.
- Task 1: bizim kart **bot/şablon** diye işaretlenmemiş.
- Task 3: en az 2 persona "mesaj atarım" + sıralamada elit veteranın **üstünde veya eşit**.
- Task 4: doğrulanamaz veya AI kokan cümle **yok**; varsa o cümle düzeltilir, yeniden çalıştırılır (max 3 tur).

---

## 5) Botlara karşı ayrıca (rakip olarak değil, alan gerçekliği)

- Botlar ilk 60 sn'de gelir ve boost basar; ilk 4'ün 2–3'ü bot olabilir. Müşteri bunları **kartta** tanıyor ve atlıyor; bize sıra ilk 4'te olsak da **botlara benzemediğimiz** sürece gelir.
- Bizim kartın bot gibi görünmemesi için kural kontrolü (playbook §12.5): ilan başlığını tekrar etme, "seamless/precision/proven track record/aligns" yok, ilana özgü **en az bir isim** (sayfa, dosya, araç, rakam) var.
- Bot yoğun ilan (ilk 10 dk'da 15+ teklif) K2'ye takılır → SKIP; simülasyona bile gelmez.

---

## 6) Kütüphane bakımı

- Her hafta r/Upwork ve Upwork Community'den 1–2 yeni gerçek kart ekle (özellikle T6).
- Insights'ta gerçek ilk 4'te gördüğün rakip rozet/ücret bilgisini T1–T3 meta'larına yansıt.
- Bir kart tipinin gerçekte artık görülmediği anlaşılırsa emekliye ayır.
