# Upwork stratejisi — tek belge

**Son güncelleme:** 2026-09-30 · **Tek kaynak.** Eski Upwork dokümanlarının hepsi bu belgeye birleştirildi ve silindi. Burada olmayan kural geçersiz.

**Kim:** Oğuzhan, Bursa (GMT+3), Upwork'te 0 yorum. **Alan:** WordPress/Elementor, landing page, düzeltmeler, hız, Google Sheets/Apps Script, Python, küçük web ve n8n/API işleri. **Sınırlar:** telefon ve video görüşme yok, saatlik iş yok, ücretsiz iş yok.

---

## İçindekiler

1. Hedefler
2. Nerede kaybediyoruz — 1. parti bulgular
3. Müşteriler ne diyor — 2. parti bulgular
4. İlan akışı ve saatler
5. GO / SKIP
6. Boost
7. Ön-iş — önce yap, sonra teklif et
8. Açılış — kart ilk 150 karakterde kazanılır
9. Mektup gövdesi, fiyat, milestone
10. Müşteri tipine ve duruma göre ayar
11. Demo ve risk kararları
12. Test hattı — göndermeden önce
13. Rakip kartları ve hakem prompt'u
14. Cevap geldikten sonra — kapanış
15. Profil, Rising Talent, Project Catalog
16. Günlük akış
17. Ölçüm ve haftalık ayar
18. Asla yapılmayacaklar

Ek A — Vibeworker filtre JSON'ları · Ek B — Teklif log'u

---

## 1) Hedefler

| Metrik | Piyasa ortalaması | **Hedef** |
| --- | --- | --- |
| Teklif açılma | %40–50 | **%70+** |
| Açılan → cevap | %10–20 | **%35–50** |
| Cevap → işe alım | — | **%50–60** |
| **İşe alım / teklif** | %2–4 | **%12–20** |

%12–20 = açılma × cevap × kapanış (0,70 × 0,45 × 0,50 ≈ %16; iyi haftada 0,75 × 0,50 × 0,55 ≈ %20). Her kural bu üç çarpandan birini büyütür.

---

## 2) Nerede kaybediyoruz — 1. parti bulgular (Upwork'ün kendi kaynakları)

| Gözlem | Upwork'ün kuralı | Sonuç |
| --- | --- | --- |
| Boost'luyken 0 açılma, boost'tan düşünce ilan hareketleniyor | Boost şu durumlarda biter: müşteri etkileşime girer, teklifi 3 kez açıp işlem yapmaz, **kartı 5 kez görüp tıklamaz**, ya da geçilirsin | 35'te geçilmiyoruz, o halde düşüş büyük ihtimalle **"kart görüldü, tıklanmadı"**. Sorun sıralama değil, **kart**. |
| sand.show: 23 teklif, 0 açılmış, ilan kapandı | Müşteri public teklifleri açmadan davet, Uma shortlist'i veya direkt teklifle işe alabilir | Bazı ilanlar baştan kazanılamaz. Ön-kontrol (§5.3) ile elenir. |
| "Belki arkadaşına verdi" | İlan sayfasında "Invites sent / Interviewing" görünür | Başvurmadan önce bakılır, Connect yanmaz. |
| Rakipler 60K$, boost'a abanıyor | Boost'lu ilk 4 her şeyin üstünde sabit; altı "best match" (kategori, beceri, JSS, mektuptaki anahtar kelimeler) | İlk 4 = masaya oturmak, kazanmak değil. |

**Kartta ne görünür:** isim, foto, rozet, saatlik ücret, JSS, profil başlığı ve mektubun ilk ~150 karakteri (mobilde ~110). Veteranın rozet ve JSS'i var, bizim yok. Eşitleyebileceğimiz tek alan **ilk 150 karakter**.

**Uma Recruiter (Upwork'ün AI işe alım aracı):** teklif metnini ve tarama cevaplarını ilanın gereksinimleriyle karşılaştırıp puanlar, uygunluk ve JSS'i de tartar, birkaç saat içinde "Shortlisted" sekmesine liste koyar. Kullanan müşteriler ~%30 daha sık işe alır. Sonuç: ilandaki her gereksinim metinde **aynı kelimeyle** geçmeli, başvuru **ilk ~6 saatte** yapılmalı.

**Düzenleme ve boost (Upwork Help "Edit your proposal"):**
- Mektup, ekler ve cevaplar **6 saat içinde veya müşteri görene kadar** düzenlenebilir.
- Boost'suz gönderilen teklife sonradan boost eklenebilir; var olan boost değiştirilemez.
- Mektup **düz metin**: `**kalın**`, `#`, backtick olduğu gibi görünür.

**Profil (28 Mayıs 2026'dan beri):** tek dinamik profil; ilana en uygun portföy öğesini öne çıkarır; 20 hard skill + 2 soft skill.

---

## 3) Müşteriler ne diyor — 2. parti bulgular

| Kaynak | Söylenen | Anlamı |
| --- | --- | --- |
| Müşteri, r/Upwork | Kendini anlatan kısımları atladım; metrikleri profilde görürüm. Ne yapacağını, milestone'ları, süreyi, iletişimi görmek istedim. | Kendini anlatma, **iş akışını** göster. |
| Müşteri, r/Upwork | İlan başına 100–150 aynı AI teklifi alıyorum. | İnsan gibi, kısa, somut olan ayrışır. |
| $1M+ kazanan UX tasarımcı | İlk mektupta soru sorma, müşteri üşenir. Doğrudan öneriyle başla. | Açılış = teşhis/öneri. |
| Top Rated'e verilen tavsiye | Rozetini ilk cümleye yazma; neredeyse herkes top-rated. | Veteranın rozeti bile kartta ayırt etmiyor. |
| "13 teklif, 0 görüntülenme" | Açılış belirsizdi, en güçlü rakam 6 paragraf aşağıdaydı; müşteri kartı junk mail gibi geçti. | Bizim durumumuzun tarifi. |
| Yeni freelancer'lar (3 teklifte iş, 1 teklifte iş) | Yazmadan önce müşterinin sitesine/brief'ine bakan 60–90 sn Loom. | Önce iş, sonra metin. |

**Sentez:** veteranın kart avantajı zayıf, fark yaratan tek şey açılış metni ve veteranların çoğu orada şablon kullanıyor. $100–300'lık işe 15 dk ön-iş ayırmak veteranın ekonomisine uymaz, bize uyar. **Asimetri bizden yana.**

---

## 4) İlan akışı ve saatler

**Kaynaklar:** Upwork Plus önerileri + kayıtlı aramalar (ana hat), Vibeworker Pro push (P1–P5 çan açık, P6 sadece feed, Shortlist çanı kapalı). Filtre JSON'ları Ek A'da.

**Vibeworker ortak ayarlar:** Hunting mode **Quick Wins**, AI ranking **Review Stacking**; Sniper ve High Value preset'leri kapalı. Bildirim: uygulama içi push açık, sessiz saat 01:00–09:00 (Europe/Istanbul); telefonda Vibeworker için pil kısıtlaması kapalı. Slack yok.

| TR saati (GMT+3) | Yoğunluk | Ne yap |
| --- | --- | --- |
| 01:00–09:00 | Çok az | Sessiz saat |
| 09:30–10:00 | Az | Gece ilanlarına bak (60 dk'dan eskiyse SKIP) |
| **11:00–13:00** | Orta (UK + erken US) | Av bloğu 1 |
| **15:00–22:00** | **En yoğun** (US Doğu iş günü) | Av bloğu 2, telefon açık |
| 22:00–00:30 | Orta-az (US Batı) | Sadece taze ve iyi ilan |

Pazartesi en yoğun gün. **Kalibrasyon:** push <5/gün → rating 4.5 ve spent $500 eşiğini gevşet; push >40/gün ve çoğu alakasız → exclude listesine kelime ekle; Vibeworker push 5 dk'dan geç geliyorsa telefonun pil tasarrufu kısıtlıyordur.

---

## 5) GO / SKIP

### 5.1 30 saniyelik akış

```
Bildirim → saatlik / görüşme şart / ≤$49?     → SKIP
         → arena dışı (§5.2)?                 → SKIP
         → Activity kötü (§5.3)?              → SKIP
         → K1 / K2 (kalabalık, yaşlı, hızlı)? → SKIP
         → B4+1 > tavan (§6)?                 → SKIP
         → GO → ön-iş (§7) → açılış (§8) → test hattı (§12) → gönder + boost
```

**Tier yok, gördükçe saldır:** arena içindeki her alan eşit; "önce WordPress" diye bir sıra yok.

### 5.2 Arena haritası

| Arena (GO olabilir) | Kanıt varlığı |
| --- | --- |
| WordPress / Elementor düzeltme | 1 sayfalık "başlamadan önce notlar" PNG'si (sand.show formatı) |
| Landing page (WP / Elementor / HTML) | CoolAir HVAC ve ProFix Plumbing Playground demoları |
| Hız / Core Web Vitals | PageSpeed önce/sonra tablosu |
| Google Sheets / Apps Script | sheet-notify demosu |
| Python (script, CSV, PDF, veri temizleme) | tidycsv, docbrief |
| Küçük web (HTML/CSS/JS, küçük React düzeltme) | Kod parçası ekran görüntüsü |
| Küçük n8n / API bağlantısı | Akış şeması PNG |
| Tasarım → HTML, küçük Figma işi | Önce/sonra mini revizyon |

**Arena dışı (SKIP):** AI agent / RAG üretim sistemi, GHL, CRM kurulumu, ML / model eğitimi, trading / MT4, WooCommerce checkout, mobil uygulama, retainer, CAPTCHA bypass, login arkası scrape, akademik iş, Upwork dışı ödeme.

### 5.3 Activity ön-kontrolü (ilan sayfası → "Activity on this job")

| Sinyal | Karar |
| --- | --- |
| Invites sent ≥ 5 ve Interviewing ≥ 1, ilan > 6 saat | SKIP (davetlilerden seçiyor) |
| Interviewing ≥ 2, ilan > 12 saat | SKIP |
| "Last viewed by client" > 24 saat önce | SKIP |
| Müşteri hire rate < %30 ve 5+ ilan açmış | SKIP (seçmeyen müşteri) |
| Müşteri 0 işe alım + bütçe < $50 + belirsiz brief | SKIP |
| Yeni ilan (< 2 saat), Interviewing 0 | SALDIR |

### 5.4 Rekabet kartı K1–K6 (ilk tutan satır geçerli)

İlan sayfasından oku: yaş (dk), teklif sayısı, hız = teklif ÷ max(yaş_dk, 5), boost tablosu (ilk 4 bid).

| # | Koşul | Karar |
| --- | --- | --- |
| K1 | Teklif ≥ 20 veya yaş > 60 dk | SKIP |
| K2 | Hız > 1,0/dk (ör. 15 dk'da 15+ teklif, bot yoğun ilan) | SKIP |
| K3 | $80+, arena içi, B4+1 ≤ tavan | Teklif + boost = B4+1 |
| K4 | $50–79, arena içi, B4+1 ≤ 11 | Teklif + boost = B4+1 |
| K5 | B4+1 > tavan | SKIP, Connect 0 |
| K6 | ≤ $49 veya arena dışı | SKIP |

---

## 6) Boost

**Mekanik (Upwork):** ilk 4 slot en üstte sabit; açık artırma 7 gün veya işe alıma kadar; toplam harcama = teklif Connect + boost bid. Ücret: boost'luyken müşteri etkileşime girerse veya açık artırma bittiğinde hâlâ ilk 4'teysen. İlk 4'ten düşer ve etkileşim yoksa boost Connect **iade**; teklif Connect iade edilmez. Bid bir kez verilir, artırılamaz. Bazı ilanlarda placebo açık artırma olur (gönderim sonrası bildirilir). Upwork'e göre boost %17 daha fazla görülme, %24'e kadar daha fazla işe alım sağlıyor.

**Tavan (4. sıra için, 1. için değil):**

| Bütçe | Tavan |
| --- | --- |
| $50–79 | **11** |
| $80–99 | **15** |
| $100–199 | **35** (saha: < 30 ilk 4'ten düşüyor, 35 tutuyor) |
| $200+ | **40** |

```
gerekli = B4 + 1
gerekli > tavan → SKIP
aksi           → boost = gerekli   (tablo boşsa tavana kadar)
B1 ne olursa olsun 1. sırayı kovalama (B1 = 100 tek başına SKIP sebebi değil)
```

**Örnekler:** $150, tablo 100/28/27/26 → boost 27. $150, tablo 100/40/38/36 → SKIP. $40 → SKIP (taban).

**Kurallar:**
- $80+ işte boost'suz gönderim yok; boost ilk gönderimde (ilk dakikalar en ucuz). Sonradan ekleme sadece yedek.
- İlk 2 satır zayıfsa boost basma; önce metni düzelt (test hattı §12).
- **Kilitli boost toplamı ≤ 120.** Aşarsa Connect al veya o ilanı SKIP et. Bakiye < teklif + bid → SKIP veya Connect al.
- Maliyet: teklif + boost ≤ işin ~%15'i.
- Log: boost bid, durum (açık / ödendi / iade), düşüş sebebi (outbid / kart görüldü / etkileşim).

---

## 7) Ön-iş — önce yap, sonra teklif et

**Kök ilke:** ilanı oku → işin en küçük gerçek parçasını yap → onu görünür yap (link, Loom, ekran görüntüsü, demo) → açılışı o parçanın sonucu olarak yaz. Müşteri kaliteyi para vermeden görür; veteranın geçmişi güven vaadi, bizim parça güven kanıtı. **Dürüstlük sınırı:** sadece gerçekten yapılan parça gösterilir; sonuç uydurulmaz; çözüm kodunun tamamı ücretsiz verilmez.

| Arena | Ön-iş | Açılış |
| --- | --- | --- |
| Elementor / WP düzeltme | Siteyi 390 px'te aç, kırılan 1–2 yeri işaretli ekran görüntüsü, sebebi | "Your [sayfa] breaks at 390 px because [sebep], marked screenshot + fix below." |
| Landing page | Hero bölümünü Playground'da müşterinin metniyle kur | "I built your hero section with your copy already, live link:" |
| Hız / CWV | PageSpeed, LCP öğesi ve en büyük 2 sebep | "Your mobile LCP is [X]s, caused by [öğe]; two fixes get it under 2.5s." |
| Sheets / Apps Script | İstenen akışın küçük çalışan kopyası | "I made a working copy of your [form→sheet→email] flow, test it here:" |
| Python | Örnek girdiyle çalışan script, önce/sonra | "Ran a sample of your [CSV/PDF] through a script, before/after:" |
| Küçük web / JS | Hatayı yeniden üret, sebebi tek satır | "The [hata] comes from [sebep], one-line fix, shown below." |
| n8n / API | Düğüm şeması + kritik nokta | "Mapped your [A→B] flow in 5 nodes; the tricky part is [X], handled." |
| Tasarım / Figma | Tek ekranın önce/sonra mini revizyonu | "Redid your [ekran] above the fold, before/after:" |
| Site yok, sadece brief | 3 maddelik yapı + bir kör nokta | "Your brief has one gap that changes the build: [X]. Plan below." |

**Süre:** $50–99 → 10 dk (ekran görüntüsü / tek teşhis). $100–199 → 15 dk (60 sn Loom veya mini demo). $200+ → 20 dk (çalışan parça + Loom).

**Loom:** 60–90 sn; ilk 5 saniyede müşterinin kendi sayfası/dosyası ekranda; tanıtım yok; sonunda "this is what I'd do first".

---

## 8) Açılış — kart ilk 150 karakterde kazanılır

### 8.1 Altı arketip (güçlüden zayıfa)

| # | Arketip | Kalıp | Örnek |
| --- | --- | --- | --- |
| A1 | Yapılmış iş | "I already [yaptım] for your [şey], [link/ek]." | "I rebuilt your pricing hero in Elementor with your copy, live preview link below, mobile included." |
| A2 | Teşhis + sebep | "Your [şey] [sorun] because [sebep], fix below." | "Your header overlaps the form on iPhone because the sticky container has no top offset, marked screenshot below." |
| A3 | Rakam | "[Metrik] is [X] on [cihaz]; [N] changes fix it." | "Your homepage LCP is 5.8s on mobile; it's one 2.4 MB hero image and a render-blocking font." |
| A4 | Çerçeve değişimi | "You asked for [X], but [Y] is what's blocking you." | "You asked for a redesign, but only 2 sections break on mobile, a fix is faster and keeps your SEO." |
| A5 | Karar kısayolu | "Short version: [çözüm], [süre], [fiyat]." | "Short version: 3 Elementor fixes, done in 24h, fixed $90, marked screenshots of each below." |
| A6 | Kör nokta | "One thing your post doesn't mention will decide this: [X]." | "One thing decides this migration: your WooCommerce order history, here's how I'd move it safely." |

### 8.2 Yasaklar (ilk 150 karakter)

"Hi/Hello there", "Dear hiring manager", "I" ile başlamak, "experience", "years", "excited", "I came across", "I hope", rozet/JSS, ilan başlığını tırnakla tekrar, soruyla açmak. Müşteri adı biliniyorsa sadece "Hi Sarah," olabilir.

### 8.3 10/10 açılış testi (her madde 2 puan; 10 değilse gönderme)

| Test | 2 puan | 0 puan |
| --- | --- | --- |
| Kendi kelimesi | İlandaki isim/sayfa/araç aynen geçiyor | "your website" |
| Somutluk | Sebep, rakam, cihaz, piksel, dosya adı | "clean", "professional" |
| Yapılmış iş kancası | Link/ek/Loom'a işaret ediyor | "I can do" |
| Kartta bitiyor | ≤150 karakterde anlam tam; ilk 110 karakter tek başına anlamlı | Cümle kartın dışında bitiyor |
| Sıfır ben | Özne müşteri veya iş | "I/I'm/my experience" |

Ek kontrol: bu cümleyi başka hiçbir teklifte görmeyecek mi? Hayırsa 0/10.

### 8.4 Kartın geri kalanı

| Öğe | Karar |
| --- | --- |
| Başlık | `Elementor & WordPress Fixes in 24h · Landing Pages · Google Sheets Automation` |
| Foto | Yüz net, göz teması, sade arka plan; logo/avatar yok |
| Saatlik ücret (fixed işte bile kartta görünür) | **$25–35**; $5–15 "ucuz = risk" sinyali |
| Rozet | Rising Talent gelirse karta çıkar (§15) |

---

## 9) Mektup gövdesi, fiyat, milestone

### 9.1 Yapı (90–150 kelime, düz metin)

1. **Açılış** (A1–A6).
2. **Kanıt satırı:** link / "Loom (60 sec):" / "Attached: 1-page notes". Tek satır.
3. **Plan (3 madde):** her madde = çıktı + gün. Son madde test (390 / 768 / 1366 px) ve teslim şekli. Maddeler `1)` `2)` `3)` ile.
4. **Fiyat + milestone:** "Fixed $X. Milestone 1 = [çıktı 1], approve only when you see it."
5. **İletişim:** "Everything in writing + Loom updates; replies within 1 hour (GMT+3)."
6. **Yenilik satırı (opsiyonel):** "New to Upwork, not to WordPress: [demo linki]."
7. **CTA:** tek, 5 saniyelik evet/hayır sorusu: "Want me to start with [çıktı 1] today?"

En fazla 2 link (Loom + demo), tek ek (adı anlamlı), tek soru, iletişim bilgisi yok. İlan soru sorduysa veya gizli kelime istediyse cevap 3. satırda. Tarama sorularının cevabı kanıt (link/sayı), sıfat değil.

### 9.2 Şablon

```
[İlandaki kelime] [somut sonuç], [kanıt: Loom/link/ekteki 1 sayfa].
[Gizli kelime veya müşteri sorusunun cevabı, varsa.]

Plan:
1) [çıktı 1], [gün]
2) [çıktı 2], [gün]
3) [çıktı 3 + test: 390 / 768 / 1366 px], [gün]

Fixed $[X], [N] days. Approve milestone 1 only when you see [çıktı 1].
Everything in writing, updates by Loom, replies within 1 hour.

[Tek, 5 saniyelik soru]?
```

### 9.3 Tam örnek — Elementor düzeltme, $120, 18 teklif, 3 veteran boost'lu

Veteranın kartı: "Hello! I have carefully read your job description and I'm confident I'm the perfect fit. With 9+ years of WordPress and Elementor experience…"

Bizim kart (141 karakter): "Your /services page breaks at 390 px: the 3-column container doesn't stack and the CTA falls off screen. Marked screenshots + fix plan below."

```
Loom (70 sec): [link], I walk through both issues on your live Elementor site.

Plan:
1) Stack the service columns and fix the CTA on mobile, same day
2) Check the other 4 pages you listed at 390 / 768 / 1366 px, day 2
3) Send a before/after screenshot sheet, then you approve

Fixed $120, 2 days. Approve milestone 1 only after you see /services fixed on your own phone.
Everything in writing, updates by Loom, replies within 1 hour.

Want me to start with /services today?
```

### 9.4 Fiyat ve milestone

- Bütçeye eşit veya altı. Bütçe düşükse fiyatı değil **scope'u** küçült: "$49 = the menu and the form; the speed pass is a second milestone."
- $100–150 işte iki seçenek: "Option A: the two fixes, $79. Option B: fixes + mobile pass on all pages + speed quick wins, $129."
- Teklif ekranında milestone'ları yaz: `M1 Diagnosis + fix on staging, $X, [date]` · `M2 Live + before/after report, $Y, [date]`. ≤ $80 tek milestone.
- Garanti: "If the same issue comes back within 7 days, I fix it free." · "If I can't find the cause in the first hour, I'll say so and you pay nothing."
- Ücretsiz test yok; yerine $15–29 ilk milestone. Yorum karşılığı indirim asla.

---

## 10) Müşteri tipine ve duruma göre ayar

| Müşteri | Belirti | Açılış | Gövde |
| --- | --- | --- | --- |
| Acil / bozuk site | "ASAP", "urgent", "broken" | A2 + "today" | Süre saatle, küçük milestone |
| Detaycı / teknik | Uzun ilan, araç isimleri | A3 veya A6 | Teknik adımlar, test listesi |
| Ajans | "our client", "ongoing" | A5 | Süreç, iletişim ritmi, white-label ("you own the files") |
| Bütçe hassas | Düşük bütçe, "simple" | A4 ("fix yeter, redesign değil") | Dar scope, sabit fiyat |
| Upwork'te yeni müşteri | 0 işe alım | A1 | "Hire → fund milestone; Upwork holds the money until you approve." |
| Tecrübeli müşteri | 10+ işe alım | A2 / A3 | Kısa, sıfır dolgu |

| Durum | Yapılacak |
| --- | --- |
| Yanlış çözüm istiyor ("install a speed plugin") | Kanıtla nazik düzeltme: "A cache plugin alone won't fix the 4.2 s LCP; the 1.9 MB hero image is the problem. That fix is included, and I'll add caching too." |
| İstenen bütçeye sığmıyor | Scope'u böl: "$150 covers the home page done properly; the other 4 pages are a second milestone." |
| Eski freelancer kaçmış / iletişim şikayeti | "You'll get a 3-line update at 9am your time every day, even if it's just 'on track'." |
| "Agency? Where are you based?" | "Solo, Bursa, Turkey (GMT+3), online US mornings and the full UK day." |
| Davet (invite) | Aynı yapı, 5 dk içinde; "Thanks for the invite," + bulgu |
| İlan güncellendi | Teklifi Edit ile güncelle (6 saat / görülene kadar) |

---

## 11) Demo ve risk kararları

| Müşteri ne istiyor | Risk | Teklifte | Yapılmaz |
| --- | --- | --- | --- |
| "Link to similar work" | Düşük | Tek demo (HVAC/Plumbing) veya repo | Özel mock |
| "Look at my site, tell me what's wrong" | Düşük | Yazılı teşhis | Canlıda kod değişikliği |
| "Screenshot of how you'd fix it" | Orta | İşaretli ekran görüntüsü | Tam çözüm kodu |
| "Quick mockup before hire" | Orta–yüksek | $100+ landing: 15 dk hero mock (görsel). Daha küçük işte: $15–29 ücretli mikro-milestone | Tam site ücretsiz |
| "Free test / prove yourself" | Yüksek | "$[15–29] milestone for [smallest item] today" | Ücretsiz iş |
| "Pay after we see it" / platform dışı | Kesin SKIP | — | Her şey |

**60 sn veto (senin kararın modelin üstünde):** gerçek efor > 4 saat ama bütçe < $80 → SKIP veya scope küçült; "unlimited revisions" → teklifte "2 rounds", kabul etmezse SKIP; demo isteniyor + bütçe < $70 → demo yok.

---

## 12) Test hattı — göndermeden önce (toplam ≤ 10 dk)

**Modeller:**
- **Yazar:** Claude Opus 5.5 (mektup, ön-iş notları). Hızlı GO/SKIP ön elemesi: Composer 2.5.
- **Hakemler:** yazardan **farklı aile**, iki tane: GPT 5.6 ve Gemini 3.8. İkisi de geçirmeli.

Testler sırayla; herhangi biri kalırsa düzelt ve o testten tekrar başla. En fazla 3 tur; 3 turda geçmezse arketipi değiştir, yine olmazsa SKIP.

| # | Test | Kim | Geçme şartı |
| --- | --- | --- | --- |
| T1 | **Gereksinim çıkarma** (Uma simülasyonu) | Hakem 1 | İlandan zorunlu gereksinimler + birebir kelimeler listesi çıkar (araç, sayfa, çıktı, süre, soru, gizli kelime) |
| T2 | **Kural kontrolü** | `scripts/proposal_lint.py` | `RESULT: PASS` |
| T3 | **Kanıt doğrulama** | Sen + hakem 2 | Mektuptaki her iddia ön-iş bulgusuyla eşleşiyor; linkler gizli pencerede açılıyor; Loom public |
| T4 | **Ek görsel 3 saniye testi** | Hakem 1 (görsel) | "3 saniyede bu görsel ne diyor?" cevabı amaçlanan mesajla aynı; 390 px genişlikte okunuyor |
| T5 | **Kör kart paneli** (§13) | Hakem 1 ve 2 | İki sırada, 3 personadan en az 2'sinde açılan 2 karttan biri; bot/şablon diye işaretlenmemiş |
| T6 | **Mektup + itiraz** | Hakem 2 | En az 2 persona "mesaj atarım"; elit veteranla eşit veya üstünde; "işe almamak için en güçlü sebep" mektupta önceden cevaplanmış |
| T7 | **Dil** | Hakem 1 | Doğal ABD/İngiltere İngilizcesi; Türkçe'den çeviri kokan yapı yok; kısaltmalar (I'd, you'll) var |
| T8 | **Son insan kontrolü** | Sen | "Bunu okuyan yorgun bir esnaf tıklar mı?" Evet değilse gönderme |

### 12.1 T2 — kural kontrolü (script)

```bash
python3 scripts/proposal_lint.py letter.txt \
  --must "Elementor,/services,mobile" \
  --title "Fix Elementor mobile layout" \
  --check-links
```

`--must` = T1'in çıkardığı birebir kelimeler. Script şunları kontrol eder: 90–150 kelime; selam veya "I" ile başlamama; ilk 150 karakterde kendini anlatma yok; ilk cümle kartta bitiyor; AI/şablon kalıpları (seamless, leverage, proven track record, I'd be happy to…); markdown yok; en fazla 2 uzun tire; tam 1 soru; en fazla 2 link ve açılıyorlar; "I/my" ile başlayan cümle ≤ %30; cümle uzunlukları tekdüze değil; ilan başlığı birebir tekrar edilmemiş; zorunlu kelimelerin hepsi metinde, en az biri kartta. Masaüstü (150) ve mobil (110) kartı ayrıca yazdırır.

### 12.2 T1 prompt'u (gereksinim çıkarma)

```
You are Upwork's Uma Recruiter. From the job post below, list:
1) every hard requirement (tools, pages, outputs, deadline, format),
2) the exact words the client used for each (verbatim, no synonyms),
3) any question or hidden keyword the client asked applicants to include,
4) the single outcome the client cares about most.
Return a comma-separated list of the verbatim terms at the end.
JOB POST: <ilan>
```

### 12.3 Hakem zaafları ve karşılıkları

| Zaaf | Karşılık |
| --- | --- |
| Yazar kendi metnini kayırır | Hakem farklı aile; iki hakem |
| AI tarzı metni sever | T2 kural kontrolü + T5'te "hangileri bot?" sorusu |
| Sıra etkisi | Kartlar 2 farklı sırada |
| Pipet rakip | Her testte zorunlu elit veteran kartı (§13) |
| Puan şişirme | Puan değil davranış: "Sadece 2 kart açabilirsin" |
| Tek persona tesadüfü | 3 persona paneli |
| Kanıtı doğrulayamaz | T3: sadece gerçek bulgu, çalışan link |
| Hakeme göre optimize etme | En fazla 3 tur; sadece gerçekle değiştir; T8 son karar insanın |
| Simülasyon ≠ piyasa | Kalibrasyon (aşağıda) |

**Hakem kalibrasyonu (başta bir kez):** kazandığı bilinen 3 açılış (r/Upwork ve ilk iş hikâyeleri) + atlandığı bilinen 3 açılış (bizim açılmayan eski açılışlarımız dahil) karışık verilir. Hakem en az 5/6 doğru ayırmazsa prompt sertleştirilir veya model değiştirilir.

**Canlı kalibrasyon:** her 10 teklifte simülasyonun "açardı / açmazdı" kararı Insights'taki gerçek açılmayla karşılaştırılır. Uyum < %70 → panel veya prompt değişir. 10 teklif ön-sinyal, 30 teklif karar.

**Kalan riskler:** rakip kartlarını biz yazıyoruz (haftalık bakım §13.4 ile kapanır); tüm modeller benzer önyargılı (tek gerçek ölçü canlı kalibrasyon); kart dışı kayıplar (davet, Uma, direkt teklif, placebo, müşterinin hiç bakmaması) simülasyonla değil §5.3 ve Project Catalog ile çözülür.

---

## 13) Rakip kartları ve hakem prompt'u

### 13.1 Gerçek saha ($100–300 WP/Sheets ilanı, ilk 2 saat, 15–25 teklif)

| Tip | Pay | Kartta görünen |
| --- | --- | --- |
| Bot / otomatik teklif (GigRadar, Vollna, Upwex, kendi n8n'i) | %30–40 | AI yazımı, ilan başlığını tekrar, 30–90 sn'de gelir, çoğu boost'lu |
| Şablon veteran (Top Rated, $20K–100K) | %20–25 | "I have carefully read…", rozet + JSS %98–100 |
| Ajans | %10–15 | "Our team", 50+ iş, $25–40/hr |
| Ucuz toplu teklifçi | %10–15 | $5–12/hr, "I can start now" |
| Özgül orta seviye | %5–10 | 5–20 iş, somut açılış |
| Elit özgül veteran | %3–5 | Teşhis + kanıt + rozet. **Asıl rakip.** |

### 13.2 Kart kütüphanesi (~150 karakter + meta; `[ ]` ilana uyarlanır)

| # | Tip | Meta | Kart |
| --- | --- | --- | --- |
| B1 | Bot | JSS 96%, Top Rated, $18K, $25/hr, boosted, 40 sn | "Hi there, I just reviewed your posting for '[ilan başlığı]' and I'm confident I can deliver exactly what you need with precision and quality." |
| B2 | Bot | JSS 100%, $9K, $30/hr, boosted | "I understand you need [ilan kelimeleri]. I have extensive experience in [beceri 1], [beceri 2] and [beceri 3] and can start immediately." |
| B3 | Bot | Rozet yok, $2K, $20/hr | "Greetings! Your project caught my attention because it aligns perfectly with my expertise in [beceri]. Let me handle this seamlessly for you." |
| B4 | Bot | JSS 98%, Top Rated Plus, $45K, $35/hr, boosted | "Dear Client, I've gone through your requirements and I'm excited to help. As a seasoned [rol] I bring a proven track record of delivering high-quality results." |
| V1 | Şablon veteran | JSS 100%, Top Rated, $62K, 140 iş, $40/hr | "Hello! I have carefully read your job description and I'm confident I'm the perfect fit. With 9+ years in WordPress and Elementor, I've completed 140+ projects…" |
| V2 | Şablon veteran | JSS 99%, Top Rated Plus, $110K, $50/hr | "Hi, I'm [Ad], a senior WordPress developer with 10 years of experience. I've built and fixed 300+ websites for clients in the US, UK and Australia." |
| V3 | Şablon veteran | JSS 97%, Top Rated, $38K, $35/hr | "Hi [müşteri adı], I can definitely help with this. I specialize in exactly this kind of work and have done it many times before. Happy to hop on a quick call…" |
| A1 | Ajans | JSS 98%, $250K, 600 iş, $30/hr, boosted | "Our team of 12 WordPress experts has delivered 600+ projects on Upwork. We can assign a dedicated developer today and have your [iş] done within 48 hours." |
| A2 | Ajans | JSS 100%, $80K, $28/hr | "We reviewed your requirements and prepared a plan: (1) audit, (2) fixes, (3) QA on all devices. Our PM will be your single point of contact throughout." |
| C1 | Ucuz | JSS yok, $600, $8/hr | "Hi sir, I can do this job perfectly. I am expert in wordpress elementor. I will start right now and finish today. Please check my profile. Thanks." |
| C2 | Ucuz | JSS 89%, $3K, $10/hr | "I can do it in 2 hours for $30. I have done 100+ same work. Message me." |
| M1 | Özgül orta | JSS 100%, 14 iş, $6K, $30/hr | "Looked at [site]: the mobile header overlaps the hero because the sticky section has no top padding. Quick fix, plus I'd check the other pages at 390 px." |
| M2 | Özgül orta | JSS 94%, 22 iş, $11K, $28/hr | "For your [Sheets akışı], an onEdit trigger plus a MailApp call covers it; the only tricky part is duplicate rows, which I'd handle with a key column." |
| E1 | Elit | JSS 100%, Top Rated Plus, $64K, 210 iş, $45/hr | "Your mobile menu issue is almost always a z-index clash with the sticky header in Elementor. I fixed the same thing for 40+ sites, can do it today." |
| E2 | Elit | JSS 100%, Expert-Vetted, $150K, $60/hr | "Two things in your brief are connected: the slow LCP and the Elementor animations. Fix one and the other goes away. 2-min Loom on your site: [link]" |
| E3 | Elit | JSS 99%, Top Rated Plus, $88K, $40/hr | "I built the exact [form → Sheet → Slack] flow for [benzer sektör] last month; screen recording of it running: [link]. Yours would take ~2 days." |

E2 ve E3 Loom/link taşıyor: "önce yap" ilkesini uygulayan rakip de var. Bizim fark: onlarınki **benzer** iş, bizimki **bu ilanın kendi sayfası/verisi**.

### 13.3 Alan kurma (her testte 8 kart)

2 bot (en az biri boosted) · 1 şablon veteran (boosted) · 1 ajans (boosted) · 1 ucuz · 1 özgül orta · **1 elit (zorunlu, ilana gerçekçi uyarlanmış, zayıflatmak yasak)** · biz (JSS yok, rozet yok, $30/hr, boosted). 4 kart boosted. Sıra 2 kez karıştırılır.

### 13.4 Hakem prompt'u (T5 + T6, tek çağrı)

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
TASK 3 (only for cards opened by at least 2 personas): read the full cover letter and the attached image description.
  For each persona: would you message this freelancer today, yes/no? What sentence almost made you skip? What would have made you message instantly? What is the strongest reason NOT to hire them?
  Rank all opened proposals from "hire first" to "pass".
TASK 4: Is there anything in the no-JSS freelancer's proposal that you cannot verify and would distrust? Anything that reads as AI-written?

Rules: no praise, no hedging, no "it depends". Be the kind of client who skips 20 proposals in a minute.
```

**Bakım:** her hafta r/Upwork ve Upwork Community'den 1–2 yeni gerçek kart ekle (özellikle elit); Insights'ta ilk 4'te görülen rakip rozet/ücret bilgisini meta'lara yansıt; artık görülmeyen tipi emekliye ayır.

---

## 14) Cevap geldikten sonra — kapanış

**Hız:** 5 dk içinde (hedef), en geç 1 saat. İlk mesajda bir sonraki küçük çıktı ("Here's the fixed mobile preview for /services, same as in the Loom").

**R1 — İlk cevap**

```
Thanks, [NAME]. Had a proper look at [SITE]: [FINDING 1, cause], [FINDING 2, cause]. Both are fixable today.

Milestone text you can paste straight in: "[SCOPE LINE, e.g. Fix the mobile menu and the contact form on acmeplumbing.com; backup first; before/after screenshots], $[PRICE], delivered by [DAY, TIME ET]."

On your side it's Hire, then fund the milestone; Upwork holds the money until you approve. I'm online for the next [N] hours.

One thing I need after hire: [WP admin login / view access / the logo].
```

**R2 — "Can you do it cheaper?"**

```
Happy to make it fit. The price covers [3 things]; if budget is tight I'd rather drop [ITEM 3] than rush the other two, which brings it to $[LOWER]. Which matters more to you, [ITEM 2] or [ITEM 3]?
```

**R3 — "Others quoted less."**

```
Understood. The difference is what's included: root-cause fix, backup, before/after report and 7 days of follow-up. If the numbers still don't work, tell me which item to drop.
```

**R4 — "Let's have a call."** (görüşme yok)

```
I work fully in writing, which keeps every decision on record. I've recorded a 2-minute Loom answering the points you'd raise on a call: [link]. Anything else, send it here and I'll reply within the hour.
```

**R5 — "Can you start with a small test?"**

```
I don't do unpaid tests, but I can make the first milestone small: [SMALLEST ITEM] for $[15–29], delivered today. If you like how that goes, the rest follows as a second milestone.
```

**R6 — Sessizlik:** 24 saat → 1 yeni bulgu + milestone metni. 48 saat → "If you've gone another way, no problem, tell me and I'll close the thread."

**İşe alım sonrası ilk 60 dk:** "Got it, thanks. Backup taken, starting now. First update by [TIME]." → söz verilen saatte 3 satır güncelleme. Fonlanmadan işe başlanmaz.

---

## 15) Profil, Rising Talent, Project Catalog

| Eylem | Neden |
| --- | --- |
| Kimlik doğrulama + çekim yöntemi + profil %100 | Rising Talent şartları; Upwork davetiyle gelebilir (rozet karta çıkar, +30 Connect). Diğer yol: 4.8+ puan ve $250 kazanç. Son 90 günde teklif şartı |
| 20 hard skill + 2 soft skill, arena kelimeleriyle | "Best match" ve Uma eşleşmesi |
| Her arena için en az 1 portföy öğesi | Dinamik profil ilana uygun olanı öne çıkarır |
| Başlık, foto, ücret | §8.4 |
| Availability: "Available now" | Müşteri filtresi |
| Availability Badge (Connect ile haftalık, opsiyonel) | Sıralama etkisi yok; sadece "Available now" filtresi. Önce Catalog |

**Project Catalog (teklifsiz, boost'suz, saatliksiz kanal):**

| Paket | Başlangıç / Standart / Premium |
| --- | --- |
| Elementor / WordPress düzeltme (3 hata, mobil dahil) | $60 / $120 / $220 |
| Tek sayfa landing page (WP veya HTML) | $150 / $280 / $450 |
| Google Sheets + Apps Script otomasyonu (form → sheet → bildirim) | $80 / $160 / $300 |

Kapak görselleri `assets/upwork-portfolio-covers/` formatında.

---

## 16) Günlük akış

**Faz 1 (ilk 3 gün veya ilk 2 işe alıma kadar):** günlük teklif tavanı yok; uygun her GO atılır; aynı anda en fazla 2 aktif sözleşme. **Faz 2:** günde 4–8 GO, teslim öncelikli.

1. Bildirim → §5.1 akışı (≤ 2 dk).
2. GO → ön-iş (§7, 10–20 dk).
3. Mektup (§8–9, 5 dk).
4. Test hattı (§12, ≤ 10 dk).
5. Gönder + boost (§6) → log satırı (Ek B).
6. Cevap → §14.
7. Gün sonu 5 dk: T+24h dolan tekliflerde Insights (açıldı mı, teklif sayısı, boost durumu) → log.

İlk 2 saat altın, 6 saat sınır; bildirimden gönderime ~30 dk hedef.

**DUR sinyalleri:** Gün 3 bitti, işe alım 0 ve açılma < %30 → hacmi 1 gün durdur, açılışı değiştir. Bakiye < 80 Connect → dur veya 200–400 Connect al. 2 aktif sözleşme → yeni GO ≤ 6/gün.

---

## 17) Ölçüm ve haftalık ayar

| Gözlem | Ayar |
| --- | --- |
| Kart hiç açılmıyor (açılma < %40, 10 teklif) | Açılış, başlık, foto A/B |
| Boost'tan düşüş, Insights'ta bid hâlâ ilk 4 bandında | "Kart görüldü, tıklanmadı" → açılış arketipini değiştir |
| Açılıyor, cevap < %20 | Gövde / kanıt / fiyat |
| Cevap iyi, işe alım < %40 | Kapanış: 5 dk cevap, milestone metni hazır, iki seçenek fiyat |
| GO anında ort. teklif ≥ 10 | Bildirim geç: pil tasarrufu, peak saat, `posted_within_hours` 12 |
| Simülasyon ile gerçek açılma uyumu < %70 | Hakem prompt'u veya paneli değiştir |
| İşe alım ≥ %15 | Hacmi artır, kurallara dokunma |

Haftada tek ayar; en fazla 5 gün dene, kötüleşirse geri al. Stats and Trends sayfasında boost'lu / boost'suz açılma haftalık karşılaştırılır.

---

## 18) Asla yapılmayacaklar

- İlana özgü isim geçmeyen genel teklif; ilk cümlede kendini anlatmak
- 3+ link, PDF portföy dökümü, uzun özgeçmiş
- Deneyim, sonuç veya müşteri sayısı uydurmak; "agency" demek
- Ücretsiz iş (teşhis evet, düzeltme hayır); çözüm kodunun tamamını teklife yazmak
- Upwork dışı iletişim bilgisi veya ödeme
- Yorum karşılığı indirim veya "5 star" istemek
- Bütçenin üstüne teklif; scope'u belirsiz bırakmak
- Fonlanmadan işe başlamak
- Müşterinin yanlış çözümüne sessizce evet demek
- Test hattından geçmemiş teklifi boost'la göndermek

---

## Ek A — Vibeworker filtre JSON'ları

Kullanım: filtre ⚙️ → View / edit as JSON → Edit → kutuyu temizle → yapıştır → Done → Save changes. Kategoriler JSON'da yok; her filtrede CATEGORIES satırından ayarla. P1–P5 çan açık, P6 çan kapalı (sadece feed), Shortlist çanı P1–P5 kurulunca kapalı.

**Ortak şablon** (her preset'te `keywords_include`, `keywords_exclude`, `budget_min_fixed`, `connects_max` aşağıdaki tabloya göre değişir):

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 50,
  "hide_unposted_budget": false,
  "connects_max": 12,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": [],
  "keywords_require": [],
  "keywords_exclude": [],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```

**Ortak exclude:**

```json
["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes"]
```

`react` bilerek exclude: React ilanlarının çoğu sıfırdan uygulama. Küçük React düzeltmeleri Upwork Plus önerilerinden gelir.

| Preset | `budget_min_fixed` | `connects_max` | `keywords_include` (herhangi biri) | Ortak exclude'a ek |
| --- | --- | --- | --- | --- |
| **P1 WP-Fix** | 50 | 12 | wordpress, elementor, divi, wpbakery, white screen, critical error, plugin conflict, contact form, wpforms, contact form 7 | custom plugin, plugin development, theme development, membership, lms, from scratch |
| **P2 Speed-Mobile** | 50 | 12 | page speed, pagespeed, core web vitals, gtmetrix, lighthouse, site speed, slow website, load time, mobile responsive, mobile friendly, responsive fix | seo retainer, monthly seo |
| **P3 Landing-Local** | 80 | 12 | landing page, one page, one-page, single page, small business website, simple website, hvac, plumbing, plumber, roofing, electrician, contractor, home services, cleaning, landscaping, google ads, lead generation | — |
| **P4 Sheets-Excel** | 50 | 8 | google sheets, excel, spreadsheet, vlookup, xlookup, pivot table, conditional formatting, formula, dashboard, tracker, calculator | data entry, bookkeeping, power bi, tableau, financial model, vba |
| **P5 Small-Web** | 50 | 8 | quick fix, small fix, small change, small task, html css, css fix, figma to html, psd to html, migrate, migration, dns, ssl, hosting, github pages, netlify, ga4, google tag manager, pixel, calendly, booking widget | — |
| **P6 Scripts-AI** (çan kapalı) | 50 | 12 | python, apps script, google apps script, automation, automate, csv, pdf, openai, chatgpt, claude, api integration, webhook, zapier, n8n, make.com | linkedin, instagram, facebook, captcha, scrape, scraping, machine learning model, fine-tune, fine-tuning, computer vision |
| **Shortlist** (tek filtre, çan kapalı) | 50 | 12 | P1–P6 include listelerinin birleşimi | football, power bi, tableau, exhibitor, exhibitor list, trade show, sponsors, lead list, data entry, linkedin, instagram, facebook, scrape, scraping, captcha, selenium, playwright, video call, phone call, zoom, google meet, native english, native speaker, kimai, custom plugin, plugin development, theme development, from scratch, manuscript, mobile game, user acquisition, voxel |

Shortlist'te `keywords_require` boş kalır (her kelime zorunlu olursa ilan kaçar).

---

## Ek B — Teklif log'u

Her teklifi gönderince bir satır; T+24h Insights; cevap/işe alım geldikçe aynı satır güncellenir.

| # | Tarih (GMT+3) | İlan | Arena | Bütçe | Yaş | Teklif sayısı | Hız | B1 / B4 | Karar (K#) | Boost bid | Boost sonucu (açık / ödendi / iade) | Düşüş sebebi (outbid / kart görüldü / etkileşim) | Arketip (A1–A6) | Ön-iş | Lint | Sim (tur, kart sırası, mektup) | Kelime | Açıldı mı (T+24h) | Cevap | İşe alım | Not |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-09-28 04:43 | Build n8n SEO Content Generation Workflow | n8n | $40 | 7 dk | <5 | ~0,1 | — | (bugün K6 SKIP) | yok | — | — | — | node map PNG | — | — | 292 | 22 teklif, 18 açılmamış, 0 mesaj | — | — | Öğrenme örneği. Kanada, 4.9★, %58 hire, $2,1k / 51 işe alım. Sapmalar: 292 kelime, 2 soru, 7 madde |
| 2 | 2026-09 | sand.show düzenlemeleri | WP | — | — | 23 | — | — | K3 | 35 | — | — | — | Looms + başlamadan önce notlar PNG | — | — | — | 23 teklif, 0 açılmış, ilan kapandı | — | — | Kart dışı kayıp (§2) |

**Boost sandığı:** kilitli toplam ≤ 120.

| # | Tarih | İlan | Bütçe | B1 / B4 | Bid | Durum | Kilitli toplam |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | **0** |

**Haftalık özet:** GO sayısı · açılma oranı (açılan/GO) · boost'lu vs boost'suz açılma · cevap oranı · işe alım · simülasyon-gerçek uyumu · bu hafta çekilen tek ayar.
