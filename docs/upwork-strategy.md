# Upwork stratejisi — tek belge

**Son güncelleme:** 2026-09-30 · **Tek kaynak.** Eski Upwork dokümanlarının hepsi bu belgeye birleştirildi ve silindi. Burada olmayan kural geçersiz.

**Kim:** Oğuzhan, Bursa (GMT+3), Upwork'te 0 yorum. **Alan:** WordPress/Elementor, landing page, düzeltmeler, hız, Google Sheets/Apps Script, Python, küçük web ve n8n/API işleri. **Sınırlar:** telefon ve video görüşme yok, saatlik sözleşme ve izleme yok (saatlik ilanlara fixed teklifle girilir, §21.2), ücretsiz iş yok.

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
19. İşe alımı artıran eklemeler
20. Keskin nişancı modu — teklif başına %25–40
21. Seçici olmadan kazanmak — model ekibi + daha fazla ilan

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
Bildirim → görüşme şart / ≤$49?              → SKIP
         → saatlik ilan?                      → §21.2 fixed dönüşümü (SKIP değil)
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

**Genişletilmiş arena (§21.3, küçük düzeltme işleri):** Shopify tema/CSS düzeltmesi, Webflow / Wix / Squarespace düzeltmesi, küçük React/Next.js bileşen hatası, HTML e-posta şablonu, GA4 / GTM / pixel kurulumu, Zapier / Make akışı, Airtable / Notion otomasyonu.

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
| Ödemesi doğrulanmış yeni müşteri (net brief) veya geçmişinde az yorumlu freelancer işe almış | **GO+** (öncelik, §19) |

### 5.4 Rekabet kartı K1–K6 (ilk tutan satır geçerli)

İlan sayfasından oku: yaş (dk), teklif sayısı, hız = teklif ÷ max(yaş_dk, 5), boost tablosu (ilk 4 bid).

| # | Koşul | Karar |
| --- | --- | --- |
| K1 | Teklif ≥ 20, veya yaş > 60 dk **ve** teklif ≥ 10 (eski ama boş ilan GO olabilir) | SKIP |
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

**Bütçe bandı önceliği (Connect kısıtlıysa, 2026-09 araştırması):** Sabit fiyatlı ilanlarda medyan bütçe $100 (UpHunt, 2.451 ilan; Upwatcher $150). Yani $100 en kalabalık fiyat noktası: ucuz toplu teklifçi ve bot en çok burada. Tavan $100–199 bandında aynı (35), bu yüzden boost maliyeti işin yüzdesi olarak $150'de en makul. Sıra: **$130–199 > $200+ > $100–129**. Hiçbiri atlanmaz; Connect azsa önce bu sırayla harcanır. İlk 3 yorum gelince $200+ öne geçer.

**Örnekler:** $150, tablo 100/28/27/26 → boost 27. $150, tablo 100/40/38/36 → SKIP. $40 → SKIP (taban).

**Kurallar:**
- $80+ işte boost'suz gönderim yok; boost ilk gönderimde (ilk dakikalar en ucuz). Sonradan ekleme sadece yedek.
- İlk 2 satır zayıfsa boost basma; önce metni düzelt (test hattı §12).
- **Kilitli boost toplamı ≤ 120.** Aşarsa Connect al veya o ilanı SKIP et. Bakiye < teklif + bid → SKIP veya Connect al.
- Maliyet: teklif + boost ≤ işin ~%15'i.
- Log: boost bid, durum (açık / ödendi / iade), düşüş sebebi (outbid / kart görüldü / etkileşim).

**Bütçe bandı önceliği (aynı anda iki GO gelirse; eleme değil):** **$120–180 önce**, sonra $181–250, sonra $100–119. $100 piyasanın medyan bütçesi, en kalabalık ve bot yoğun bant; $150 aynı boost tavanıyla (35) %50 daha fazla kâr bırakır; $200+ tavan 40 ve müşteri 0 yorumluya daha temkinli, bu yüzden M1 küçük tutulur ($40–60). Her GO'da kazanç ≈ net ücret − (teklif + boost) ÷ P.

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

### 7.1 Asıl istek önce — site bulgusu ikinci planda

Modeller **o ilana özel** çalışır. Araştırmacı siteyi tarar ama **ilan metnindeki asıl teslimat** her şeyin üstünde.

**Composer, T1'den sonra JOB_BUNDLE'a yazır:**

| Alan | İçerik |
| --- | --- |
| `primary_deliverable` | Müşterinin istediği tek cümle (ör. "Apps Script: form → Sheet → email") |
| `primary_terms` | Kartta ve dilimde geçecek birebir kelimeler (T1) |
| `secondary_findings` | Site audit / ek bulgular (LCP, taşma, kırık form…) — **ilan bunu istemiyorsa** |
| `prework_slice` | Sadece **primary** için yapılmış dilim |
| `plan2_note` | İsteğe bağlı 2. milestone metni (secondary için) |

**Kurallar (yazar + görselci + yapımcı + hakem):**

| Durum | Kart / ilk cümle | Ön-iş / video | Mektup gövdesi |
| --- | --- | --- | --- |
| Bulgu **doğrudan** asıl işe bağlı (mobil ilan + mobil taşma) | Teşhis asıl işte | İşaretli ekran görüntüsü asıl sayfada | Aynı |
| Bulgu **başka** (Sheets ilanı, sitede LCP kötü) | **Sadece Sheets**; LCP kartta **yasak** | Dilim = Sheet akışı; LCP video'da **yok** | Asıl iş + fiyat; LCP **en fazla 1 cümle**: "After the script is live, I also noticed slow mobile LCP — happy to quote that as milestone 2 if you want." |
| Müşteri sitede **hiç** bahsetmedi, URL yok | Site audit **teklife sokulmaz** | Brief / demo / plan | — |
| İlan "site speed" der, müşteri aslında "logo değişimi" yazmışsa net değilse | Netleştiren **tek soru** | Teşhis yok | "Just to scope M1: is this the logo swap only, or speed too?" |

**Lint:** `proposal_lint.py --card-must` = `primary_terms`; `--ban-in-card` = secondary'den kelimeler (ör. `LCP,PageSpeed,overflow` Sheets ilanında). **T3b Scope:** Hakem 1 — "Does the opening sell what they asked for, or hijack with unrelated site issues?" → hijack = FAIL.

**Sohbet hattı (§23):** Müşteri mesajı da aynı kural; cevap önce onun son sorusu / offer scope, audit ikinci planda.

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

**Tek sohbet (Cloud Agent):** Composer 2.5 orkestra eder; yazar ve hakemler **alt agent (Task)** ile ayrı modellerde çalışır. Otomatik fix: `proposal_lint.py` → geçmezse yazar Task tekrar (hakem feedback ile) → max 3 tur. İki hakem **paralel** Task.

### 12.0 Varsayılan model seti — tasarruflu, risk vermez

Ödün yok: hepsi **low** değil; **lint + iki hakem + T8** zorunlu. Low sadece hızlı/ucuz katmanlarda; asıl sıkılık **GPT Terra Medium** hakemde.

| Rol | Model (slug) | Neden |
| --- | --- | --- |
| **Orkestra + GO/SKIP + ön-iş koordinasyon** | Bu sohbet: **Composer 2.5** | Tek thread; lint çalıştırma; tur sayacı; paket hazırlama |
| **Yazar** (mektup, tarama cevapları, ön-iş metinleri) | **`claude-opus-5-5-low`** | Talimat takibi + kısa İngilizce; maliyet düşük |
| **Hakem 1** (T1 gereksinim, T5 kart paneli, T4 ek 3 sn, T7 dil) | **`gpt-5.6-terra-medium`** | Farklı aile; medium = şişirme puanına karşı sert |
| **Hakem 2** (T3 kanıt, T6 mektup + itiraz, T5 ikinci sıra) | **`gemini-3.8-flash-low`** | İkinci aile; hızlı ikinci görüş; kart sırası B |

**Geçme:** lint `PASS` + Hakem 1 ve 2 geçti + **T8 sen** (esnaf tıklar mı). Biri FAIL → fix turu.

**Yükseltme (sadece o ilan, maliyet artar ama risk düşer):** bütçe **≥ $150** veya B4 ≥ 25 veya elit veteran kartı mektubumuzdan güçlü görünüyorsa → yazar **`claude-opus-5-5-medium`**, Hakem 2 **`gemini-3.8-flash-medium`**. Hakem 1 medium kalır.

**Asla:** yazar = hakem aynı model/aile; hakem olmadan gönderim; lint FAIL ile gönderim.

**Senin tetik cümlesi (her GO/TEST):**

```text
TEST veya GO. Model seti: varsayılan §12.0. Alt agent, otomatik fix max 3 tur.
[ilan / screenshot] · Boost tablosu · Activity
```

### 12.0.1 Mekanizma — tek sohbet, modeller birbirine konuşmaz

**Net kural:** Opus, GPT ve Gemini **birbirini görmüyor**. Sadece **Composer 2.5 (bu sohbet)** hepsini çağırır, araya **yapılandırılmış paket** koyar, cevapları okur, sonraki adımı seçer.

```
Sen
 └─► Composer 2.5 (tek thread, durum makinesi)
        │
        ├─► [Task] Opus 5.5 Low/Medium  ← JOB_BUNDLE + WRITER_TASK → letter + screening
        ├─► shell: proposal_lint.py     ← modelsiz
        ├─► [Task] GPT Terra Medium     ← JOB_BUNDLE + CARDS + letter → JUDGE1_JSON
        └─► [Task] Gemini Flash Low/Med ← aynı paket, sıra B → JUDGE2_JSON
        │
        └─► Composer: PASS/FAIL, tur++, yükseltme?, sana özet
```

**Alt agent nasıl açılır:** Composer `Task` ile **tek seferlik** görev verir (prompt + paket). Alt agent bitince **sadece çıktı** döner (metin veya JSON). Composer bunu bir sonraki Task’a **kopyalar**; modeller arası sohbet yok.

**JOB_BUNDLE (her Task’a giden ortak blok):**

| Alan | İçerik |
| --- | --- |
| `job_post` | İlan metni (verbatim) |
| `client_facts` | Ülke, harcama, hire rate, yaş, teklif sayısı |
| `activity` | Davet / interviewing / last viewed |
| `boost_table` | B1–B4 |
| `prework` | Gerçek bulgular, linkler, ek açıklaması (uydurma yok) |
| `primary_deliverable` | T1: müşterinin asıl istediği (§7.1) |
| `primary_terms` / `secondary_findings` | Kart vs 2. plan ayrımı |
| `must_terms` | T1 çıktısı (birebir kelimeler) |
| `cards_a` / `cards_b` | 8 rakip + biz (§13), sıra B karışık |
| `letter` | Güncel mektup (fix turunda güncellenir) |
| `tur` | 1–3 |
| `writer_model` / `judge2_model` | Şu anki slug (varsayılan veya yükseltilmiş) |

**Composer sana her GO/TEST sonunda yazır:** `tur`, `lint`, `J1/J2` özet, `model_set`, `yükseltme nedeni` (varsa), `GO gönder` veya `SKIP` veya `T8 sende`.

### 12.0.2 Yükseltme — yetmediğini nasıl anlar?

**Başlangıç:** her zaman §12.0 varsayılan (Opus Low + Terra Medium + Gemini Low).

**A) İlan açılırken otomatik (Composer, GO’dan önce):** aşağıdakilerden **biri** varsa **ilk turda** yükseltilmiş set:

| Tetik | Yükseltme |
| --- | --- |
| Fixed bütçe **≥ $150** | Yazar → `claude-opus-5-5-medium`, Hakem 2 → `gemini-3.8-flash-medium` |
| Boost tablosunda **B4 ≥ 25** | Aynı |
| İlan metni **> 2500 karakter** veya 5+ zorunlu araç | Aynı |

**B) Tur içinde otomatik (test hattı sonucu):**

| Tetik | Aksiyon |
| --- | --- |
| **T2 lint FAIL** ve sebep dil/AI kalıbı/uzunluk | Yazar tekrar (aynı model); 2. lint FAIL → yazar **medium**’a yüksel |
| **T2 lint FAIL** ve sebep eksik `must_terms` | T1 tekrar (GPT) → yazar düzelt |
| **Hakem 1 FAIL**, Hakem 2 PASS | Tur++; feedback ile yazar; tur 3 hâlâ J1 FAIL → Hakem 1 **`gpt-5.6-terra-high`** (sadece o ilan) |
| **Hakem 2 FAIL** (kanıt/itiraz), J1 PASS | Tur++; tur 2’de Hakem 2 → **medium**; tur 3 hâlâ FAIL → **SKIP** (kanıt/ön-iş zayıf) |
| **İkisi FAIL** “bot/AI” | Yazar + lint; arketip değiştir (A1→A2…) |
| **İkisi FAIL** “elit veteran daha iyi” | Ön-iş güçlendir (daha somut bulgu); yazar medium; 1 tur daha; yoksa SKIP |
| **J1 ve J2 çelişir** (biri aç, biri atla) | Üçüncü hakem yok; **T8 zorunlu** + konservatif: geçmedi say |
| **3 tur tükendi** | SKIP (Connect yok) |

**C) Senin yükseltmen:** mesajda `YÜKSELT` veya `kritik ilan` → A seti. `Düşük mod` → varsayılan §12.0 (sadece düşük bütçe / alıştırma).

**D) Uzun vadeli (log):** son 10 GO’da sim PASS ama Insights açılma < %30 → bir sonraki ilanlarda **varsayılan** Hakem 1 Terra **high** veya yazar **medium** (haftada bir kez, §17).

**Yükseltme tavanı (maliyet):** bir ilanda en fazla yazar medium + J2 medium + (isteğe bağlı) J1 high; **Opus high / Terra max** yok — o noktada SKIP veya sen T8 ile manuel gönder.

### 12.0.3 Serbest sohbet yok, üç kontrollü ek var

Hakemler arasında serbest tartışma **yok**: birbirine uyum sağlar (grup düşüncesi), maliyeti katlar, metni hakemlerin zevkine kaydırır. Yerine:

| Ek | Ne zaman | Nasıl |
| --- | --- | --- |
| **Çapraz sorgu (1 tur)** | J1 ve J2 çelişirse | Composer her hakeme diğerinin **gerekçesini** (kararını değil) verir: "Bu itiraz geçerli mi? Kararını koru veya değiştir, tek cümle sebep." Hâlâ çelişirse geçmedi say |
| **Saklı hakem** | Mektup J1 + J2'yi geçtikten sonra, **tek sefer** | Fix turlarında hiç kullanılmamış üçüncü aile: `grok-4.7-low` (Cursor havuzu, ucuz). Sadece T5 kart paneli. Açmazsa → gönderme, 1 tur daha veya SKIP. Metin iki hakeme göre cilalandığı için bu, ezberlemeyi yakalar |
| **Kör geri bildirim** | Her fix turunda | Yazara hakem puanı/kararı gitmez; sadece "atlatan cümle" ve "eksik kanıt" satırları gider. Yazar hakemi memnun etmeye değil, müşteriye yazmaya devam eder |

**Hakem çıktı formatı (zorunlu JSON, çelişkiyi ölçülebilir yapar):**

```json
{"opened_ours_order_a": true, "opened_ours_order_b": true, "flagged_bot": false,
 "personas_would_message": 2, "beats_elite": true,
 "skip_sentence": "...", "missing_proof": "...", "strongest_objection": "...", "verdict": "PASS"}
```

**Gerçek geri besleme:** her gönderilen teklifin Insights sonucu (açıldı / cevap / işe alım) kalibrasyon setine eklenir. Ayda bir: hakemlere geçmiş 10 kartı kör verip gerçek sonucu tahmin ettir; en kötü tahmin eden hakem değiştirilir.

Testler sırayla; herhangi biri kalırsa düzelt ve o testten tekrar başla. En fazla 3 tur; 3 turda geçmezse arketipi değiştir, yine olmazsa SKIP.

| # | Test | Kim | Geçme şartı |
| --- | --- | --- | --- |
| T1 | **Gereksinim çıkarma** (Uma simülasyonu) | Hakem 1 (GPT Terra Medium) | İlandan zorunlu gereksinimler + birebir kelimeler listesi çıkar (araç, sayfa, çıktı, süre, soru, gizli kelime) |
| T2 | **Kural kontrolü** | `scripts/proposal_lint.py` | `RESULT: PASS` |
| T3 | **Kanıt doğrulama** | Sen + hakem 2 | Mektuptaki her iddia ön-iş bulgusuyla eşleşiyor; linkler gizli pencerede açılıyor; Loom public |
| T3b | **Scope — asıl istek** | Hakem 1 | Kart ve dilim **primary**'yi satıyor; unrelated site audit kartı ele geçirmiyor (§7.1); secondary varsa plan-2 cümlesi, ücretsiz iş vaadi yok |
| T4 | **Ek görsel 3 saniye testi** | Hakem 1 (görsel) | "3 saniyede bu görsel ne diyor?" cevabı amaçlanan mesajla aynı; 390 px genişlikte okunuyor |
| T5 | **Kör kart paneli** (§13) | Hakem 1 ve 2 | İki sırada, 3 personadan en az 2'sinde açılan 2 karttan biri; bot/şablon diye işaretlenmemiş |
| T6 | **Mektup + itiraz** | Hakem 2 (Gemini Flash Low/Medium) | En az 2 persona "mesaj atarım"; elit veteranla eşit veya üstünde; "işe almamak için en güçlü sebep" mektupta önceden cevaplanmış |
| T7 | **Dil** | Hakem 1 (GPT Terra Medium) | Doğal ABD/İngiltere İngilizcesi; Türkçe'den çeviri kokan yapı yok; kısaltmalar (I'd, you'll) var |
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
4) the single PRIMARY deliverable (what they are hiring for now),
5) SECONDARY findings you might notice on their site but they did NOT ask for (list separately; empty if N/A).
Return:
PRIMARY_TERMS: <comma-separated verbatim terms for the card>
SECONDARY_TERMS: <comma-separated; off-scope audit words to ban from card if job is not about these>
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

## 19) İşe alımı artıran eklemeler (2026-09-30 araştırması)

Açılma tarafı §7–§13 ile güçlü. En zayıf halka **son aşama**: müşteri açıyor, beğeniyor, ama 0 yorumlu birine para vermekten çekiniyor. Aşağıdakiler en çok bu aşamayı hedefler; etki sırasına göre.

| # | Ekleme | Kaynak | Hedeflediği aşama | Yapılacak |
| --- | --- | --- | --- | --- |
| 1 | **İlk yorum sprinti** | Müşteri yorumları (r/Upwork): ilk işe alımda portföy uyumu + iletişim belirleyici; yorum ikinci planda ama 0 yorum son aşamada fren | Cevap → işe alım | İlk **2 işe alıma kadar** öncelik: net scope'lu **$50–150** düzeltme işleri. Büyük işe de teklif at ama "ilk yorumu kim en hızlı verir?" sorusuyla sırala |
| 2 | **Başlangıç milestone'u (varsayılan)** | Müşteriler "önce küçük ücretli iş" istiyor | Cevap → işe alım | İlk 3 işe alımda $100+ tekliflerde M1 = en küçük görünür çıktı ($25–40, aynı gün). Müşterinin riski $25'e iner |
| 3 | **Profile highlights (her teklifte)** | Upwork Help: teklif formunda profilden **en fazla 4** öğe (portföy, sertifika, geçmiş iş) eklenebilir | Açılan → cevap | Her GO'da ilanın arenasına uyan 1–2 portföy öğesini seç (landing → CoolAir/ProFix; Sheets → sheet-notify; Python → tidycsv/docbrief) |
| 4 | **Direct Contracts ile gerçek ilk yorum** | Upwork Help: Direct Contract geri bildirimi JSS'e, Rising Talent'a, kazanca **aynı şekilde** sayılır | Hepsi (rozet + yorum) | Gerçekten iş isteyen bir tanıdık/yerel işletme varsa işi Upwork Direct Contract ile yap. **Sahte iş veya para karşılığı yorum yasak** (ToS, hesap kapanır) |
| 5 | **Davet kanalı** | Upwork: %100 profil 4,5 kat daha fazla işe alım; Availability Badge ~%50 daha fazla davet (~14 Connect/hafta). Başlık, açıklamanın ilk 2 cümlesi ve beceri etiketleri aramada en ağır sinyal | Teklifsiz işe alım | Başlığı ve açıklamanın ilk 2 cümlesini arena kelimeleriyle yaz; beceri etiketlerini gerçek ilanlardan topla; görsel portföy; **30–60 sn profil videosu** (önceden kaydedilmiş, görüşme değil); ilk yorumdan sonra Badge'i 1 hafta dene |
| 6 | **90 gün kuralı** | Upwork: yeni freelancer ilk tekliften sonraki 90 günde kazanç yoksa profil **gizliye** alınır, aramadan çıkar | Davet kanalı | İlk teklif tarihini log'a yaz; 60. günde hâlâ işe alım yoksa Catalog fiyatlarını düşür, Direct Contract ara |
| 7 | **Davet = en hızlı cevap** | Davetle gelen müşteri zaten seni seçmiş | Cevap → işe alım | Davet push'u açık; **5 dk** içinde ön-iş + mektup; K1/K2 uygulanmaz, sadece §5.2 ve §5.3 |
| 8 | **Yeni müşteriye sıcak bak** | r/Upwork: 0 yorumlu yeni müşteriler çoğu zaman daha az seçici, sonra uzun vadeli oluyor | Cevap → işe alım | Ödemesi doğrulanmış, net brief'li, 0 işe alımlı müşteri **GO+** (öncelik). Doğrulanmamış ödeme hâlâ SKIP |
| 9 | **Müşterinin geçmişinde yeni freelancer var mı** | Müşteri iş geçmişi | Cevap → işe alım | Geçmiş işlerinde az yorumlu freelancer işe almışsa **GO+**; sadece Top Rated almışsa normal GO |
| 10 | **Teklif sonrası değer ekleme** | Upwork Help: 6 saat / görülene kadar düzenleme; mesaj odası teklifle açılır ama bazı hesaplarda müşteri yazana kadar kapalı | Açılma → cevap | Görülmediyse ve 6 saat dolmadıysa: yeni bir bulgu/ek ile teklifi **Edit** et. Mesaj odası açıksa 24 saatte **tek** değer mesajı (yeni bulgu + M1 metni). "Checking in" yok |

**Tahmini etki (dürüst):** 1 + 2 + 3 birlikte son aşamayı ~%45–55'ten ~%55–65'e çıkarabilir. Bu da ilan başına işe alımı yaklaşık **%9'dan %11–13'e** taşır. 4 (Direct Contract) ve 5 (davet) teklif hesabının **dışında** ek iş getirir. İlk yorum geldikten sonra son aşamadaki fren büyük ölçüde kalkar; plandaki %12–20 hedefine giden yol buradan geçer.

**Yorum isteme (işten sonra, kurala uygun):** Teslimde "Everything's live; if anything looks off in the next 7 days, tell me and I'll fix it" → müşteri memnunsa kapanışta "If you're happy with the work, a short review on the contract helps a lot." İndirim veya "5 star" talebi yok.

---

## 20) Keskin nişancı modu — teklif başına %25–40 hedefi

**Gerçek:** ilan başına işe alım sadece metinle %9'dan %39'a çıkmaz; 0 yorumlu bir profilin rastgele GO ilanında son aşaması buna izin vermez. %39'a giden yol **seçim**: sadece kazanma ihtimali yüksek ilana teklif atmak. Hacim düşer, teklif başına oran yükselir.

| Şerit | Ne | Beklenen işe alım / teklif | Hacim |
| --- | --- | --- | --- |
| **Davet** | Müşteri bizi davet etti | **%35–45** | Profil ve Catalog'a bağlı |
| **SNIPER** | `go_score.py` ≥ %25 | **%25–35** | Günde 1–2 |
| **GO** | %10–25 | %10–15 | Günde 2–4 |
| **SKIP** | < %10 | — | Connect 0 |

Karışım örneği: 1 davet + 4 SNIPER + 5 GO ≈ 0,40 + 1,2 + 0,6 = 2,2 iş / 10 teklif → **~%22 ortalama**. Davetler arttıkça ve ilk yorumlar geldikçe ortalama %30–40 bandına yaklaşır.

### 20.1 Adım 0 — kazanma tahmini (`scripts/go_score.py`)

Test hattından **önce**, Connect harcamadan:

```bash
python3 scripts/go_score.py --age 10 --proposals 3 --budget 120 --verified \
  --boost-top4 --scope-clear --demo-match exact --prework strong --hires-new-freelancers
# open 90% x reply 60% x hire 59% = 31.9%  ->  SNIPER
```

Girdiler: ilan yaşı, teklif sayısı (sadece K1/K2 ve hız için — **SNIPER/GO şeridi teklif sayısına göre değil**), bütçe, ödeme doğrulaması, Activity (interviewing / invites sent), müşteri sinyalleri, scope netliği, demo uyumu, ön-iş gücü, boost ilk 4, davet, yorum sayımız.

**Şerit mantığı (boost erken atıldığı için):** Bildirimle gideriz; teklif sayısı sonra zirve yapar, bu yüzden **%32 / %18 / %12 tablosu teklif dilimine göre ayrılmaz.**

| Band (`go_score` çıktısı) | Ne | Tipik **P** (boost ilk 4 + §21 varsayımı) |
| --- | --- | --- |
| **tam-paket** | boost + ön-iş strong + demo exact/close + scope net + interviewing 0 + invites < 5 + K1/K2 geçti | **~%28–32** (SNIPER) |
| **standart** | GO gönderilir; ön-iş light veya interviewing 1 veya demo sadece close | **~%16–22** |
| **risk** | Kanıt zayıf / interviewing ≥ 2 — normalde §5.3 SKIP; geçtiyse | **~%10–14** |
| **davet** | `--invite` | **~%34** |

Teklif sayısı yalnızca **SKIP** için: K1 (≥20 veya yaşlı+kalabalık), K2 (hız > 1/dk). Gönderdiğimiz ilanda “az teklif vs çok teklif” diye ihtimal satırı seçilmez.

Ağırlıklar başlangıç tahmini; **her 10 teklifte log'daki gerçek sonuçla** yeniden ayarlanır.

### 20.2 SNIPER ilanlarda modellerin ekstra işi

| Katman | Normal GO | SNIPER |
| --- | --- | --- |
| Ön-iş | 10–20 dk bulgu | **"Yapılmış dilim"**: müşterinin kendi sayfasında/verisinde çalışan küçük parça (tam iş değil) + 60–90 sn Loom |
| Yazar | Opus Low | **Opus Medium** |
| Hakem 1 | Terra Medium | Terra Medium + saklı hakem Grok |
| Ek hakem sorusu | — | "Would you hire this person **today** without a call? If not, what exact thing stops you?" Cevaptaki engel mektupta çözülmeden gönderilmez |
| Tarama cevapları | Kanıt | Her cevaba 1 somut link/rakam |
| Kapanış | R1–R6 | Mesaj gelince **cevap da test hattından** geçer (§20.3) |

### 20.3 Sohbet aşaması için model döngüsü (en büyük kayıp burada)

0 yorumun freni en çok müşteri yazdıktan sonra çıkar. Müşteri mesajı gelince:

1. Composer mesajı ve ilan paketini hazırlar.
2. Yazar (Opus Low) R1–R6'dan uygun cevabı + M1 milestone metnini yazar.
3. Hakem 1 (Terra Medium) müşteri personasıyla: "Would you send the offer now? What's missing?" → `yes/no + tek eksik`.
4. `no` ise tek düzeltme turu, sonra gönder. Hedef: **5 dk içinde** cevap.

### 20.4 Hız otomasyonu (opsiyonel, kurulum gerekir)

Vibeworker'ın webhook kanalı yeni ilanı bir Cursor Automation'a gönderip taslak GO paketini (skor, ön-iş listesi, mektup taslağı, lint) **bildirimden 2–3 dk sonra** hazır edebilir. Gönderim ve boost her zaman **elle** kalır (otomatik teklif Upwork ToS ihlali).

---

## 21) Seçici olmadan kazanmak — model ekibi + daha fazla ilan

İlan az geliyor; daha da seçici olamayız. İki yol: **aynı ilanda kazanma oranını** model ekibiyle yükseltmek, **gelen ilan sayısını** büyütmek. `go_score.py` artık eleme için değil, **hangi ilana ne kadar model gücü verileceğini** seçmek için kullanılır.

### 21.1 Her ilana SNIPER muamelesi — paralel model ekibi

Sorun: SNIPER kalitesinde ön-iş elle 20–30 dk sürüyor, bu yüzden her ilana yapılamıyordu. Çözüm: Composer ilan gelir gelmez **aynı anda** 3 alt agent açar; ön-iş 5–10 dakikaya iner, her GO ilan SNIPER kalitesinde gider.

```
Composer (ilan geldi, t=0)
 ├─► [Task] Araştırmacı   (composer-2.5 + tarayıcı)  → site_audit + ilan: PRIMARY vs SECONDARY raporu (§7.1)
 ├─► [Task] Yapımcı       (claude-opus-5-5-low)       → dilim **yalnızca primary** (Sheets ilanı = script, WP = o sayfa)
 └─► [Task] Görselci      (composer-2.5)             → video/PNG **primary**'yi gösterir; secondary yoksa kullanılmaz
        │  (t ≈ 8 dk, üçü birleşir)
        ▼
 Yazar (Opus Low) → lint → Hakem 1 + 2 (paralel) → saklı hakem → sen (T8)
```

| Ajan | Yeni | Neden kazanma oranını artırır |
| --- | --- | --- |
| **Araştırmacı** | Evet | Her açılış A2/A3 (teşhis, rakam) olur; tahmin değil ölçülmüş bulgu |
| **Yapımcı** | Evet | Her açılış A1 ("already did X for your Y") olabilir: en güçlü arketip, veteranın yapmadığı şey |
| **Görselci** | Evet | Ek görsel + **sessiz video**: sen konuşmadan Loom etkisi. Video = müşterinin kendi sitesinde düzeltilmiş hali |

**Sınır:** yapılmış dilim küçük ve görsel kalır (ekran görüntüsü, önizleme linki, kısa video). Tam çözüm kodu veya dosya teslim edilmez; iş, milestone fonlanınca teslim edilir.

**Beklenen etki (aynı ilan havuzunda):** açılma +10 puan (A1/A2 kartı), cevap +10–15 puan (çalışan dilim), işe alım +5 puan (risk görünür şekilde düştü) → ilan başına **~%9'dan ~%16–22'ye**. Seçicilik artmadı; her ilana daha güçlü teklif gitti.

### 21.2 Saatlik ilanları fixed'e çevir (takip yok)

Saatlik ilanlar havuzun büyük kısmı; hepsini atlamak ilanların yarısından fazlasını kaybetmek demek. Kural **değişmiyor**: saatlik çalışma ve izleme yok. Yöntem: saatlik ilana teklif at, ama **fixed milestone öner**.

- Teklif ekranında saatlik ücret alanına profil ücretini yaz. Mektubun kanıt satırından sonra: "I'd suggest a fixed price for this: $[X] for [çıktı 1 + 2], delivered in [N] days, so you pay for results, not hours."
- Müşteri kabul ederse **fixed sözleşme** ister ("Could you send it as a fixed-price offer?"). Müşteri saatlik sözleşmede ısrar ederse nazikçe çekil.
- Sadece net scope'lu, kısa saatlik ilanlar ("~5–10 hours", "small fix", tek teslim). "Ongoing", "40 hrs/week", "long-term" SKIP.
- Hakem sorusuna ek: "Would you accept a fixed-price offer instead of hourly for this?"

### 21.3 Arenayı yapımcı ajanla genişlet

Cursor ile kod yazan ajanlar birçok platformda küçük düzeltme yapabiliyor. "Küçük düzeltme" işlerinde arena genişler (§5.2 genişletilmiş arena). Koşullar:
- İş **tek parça ve teslim edilebilir** (bir tema hatası, bir bileşen, bir akış). Sıfırdan mağaza, uygulama, entegrasyon sistemi değil.
- Araştırmacı ön-işte sorunu **yeniden üretebildiyse** GO. Üretemediyse SKIP.
- Portföy yoksa kanıt = yapılmış dilim (videolu).

### 21.4 Kaçan ilanları geri kazan

| Kayıp | Çözüm |
| --- | --- |
| Uykuda gelen ilanlar (sabah 4 iyi ilan kaçtı) | K1 artık yaşa değil **teklif sayısına** bakıyor: 3 saatlik ama 6 teklifli ilan GO. Sabah 09:30 bloğunda gece ilanları taranır |
| Aynı müşteri tekrar ilan açar | Kazanamadığın iyi müşteriyi log'a "izle" diye yaz; yeni ilanında "Saw your earlier post about [X]" ile başla (A1 kanıt hazır) |
| Kaybedilen ilanda ön-iş boşa gitti | Dilim ve video **portföye** eklenir (müşteri adı/verisi olmadan): her kayıp yeni kanıt üretir |

### 21.5 Filtre değişiklikleri (Ek A'ya uygulandı)

- Ortak exclude'dan `shopify`, `react`, `next.js`, `nextjs` çıkarıldı; yerine `shopify app`, `shopify store setup`, `react app from scratch`, `saas mvp` eklendi.
- Yeni **P7 Stretch-Fix** preset'i: `shopify theme, shopify css, webflow, wix, squarespace, react bug, next.js bug, email template, html email, ga4, google tag manager, meta pixel, zapier, make.com, airtable, notion`.
- `job_type: null` kalır (saatlik dahil); saatlik ilan §21.2 ile işlenir.

---

## 22) %33 planı — teklif başına işe alım

### 22.1 Hedef huni

| Aşama | Şimdi (tahmin) | Hedef | Kaldıraç |
| --- | --- | --- | --- |
| Açılma (kart görüldü → tıklandı) | ~55% | **80%** | Boost B4+1, ilk 15 dk, kart cümlesinde müşterinin kendi sayfası/sorunu (§22.3) |
| Yanıt (açıldı → mesaj) | ~35% | **60%** | Ekran görüntüsü + 30–60 sn sessiz video + çalışan dilim (§21.1, §22.3) |
| İşe alım (mesaj → sözleşme) | ~45% | **70%** | Teklif-hazır ilk yanıt + küçük başlangıç milestone'u + sosyal kanıt (§22.2, §22.4) |
| **Toplam** | ~9% | **~33%** | 0.80 × 0.60 × 0.70 |

Dürüst aralık: 0 yorumla ilk 10 teklifte **%20–28** beklenir; 3–5 yorum veya davetlerle **%30+**. Her kaldıraç ayrı ölçülür (§22.6).

### 22.2 Yorumsuz sosyal kanıt (son aşama, en büyük kaldıraç)

Tanıdık yok: platform dışı referans ve Direct Contract **kullanılmaz**. Yerine:

1. **Riski müşteriden al:** Sabit fiyat + escrow + "Milestone 1 sadece siz test edip onaylayınca serbest bırakılır; beğenmezseniz 1 revizyon dahil." Ücretsiz iş değil, onaya bağlı ödeme (Upwork'ün zaten sağladığı güvence, açıkça söylenir).
2. **Mikro ilk milestone:** Büyük işte bile ilk adım $20–40 / 24 saat ("mobile fix only"). Yeni birini denemenin maliyeti düşer; ilk yorum hızlı gelir.
3. **İlk 3 iş = yorum işi:** İlk 3 işte fiyat piyasanın ~%70'i (ücretsiz değil), teslim süre sözünün yarısında, bitince kibarca yorum istenir. 3 yorumdan sonra normal fiyat.
4. **Kanıt = müşterinin kendi sayfası:** Yorum yerine `site_audit.mjs` bulgusu + işaretli PNG + 30–60 sn video + çalışan dilim. "Bana güven" değil "sorununu zaten buldum".
5. **Canlı demo portföyü:** Her arenada 1 canlı demo (Elementor landing, Apps Script otomasyonu, Python araç, n8n akışı) + kısa vaka yazısı ("sorun → çözüm → sonuç sayısı"). Kaybedilen ilanların dilimleri buraya eklenir (§21.4).
6. **Project Catalog:** "WordPress/Elementor mobile fix — 24h" $30–50 paket. Tanıdık gerekmez; ilk satış = ilk yorum.
7. **Yeni freelancer'a açık müşteri:** `go_score.py --hires-new-freelancers` yüksek puanlı ilanlarda boost önce harcanır.
8. **Profil %100** (4.5x) + Availability Badge (~%50 daha fazla davet). Her teklife en uygun 4 highlight.
9. 90 gün kuralı: ilk tekliften sonra 90 gün kazanç yoksa profil gizlenir; bu adımlar **ilk 2 haftada** yapılır.

Tanıdıksız dürüst aralık: 0 yorumla **%18–25**; ilk 3 yorumdan sonra **%28–33**; davetli ilanlarda **%35+**.

### 22.2.1 Yorumsuz %30 yolu: davet payını artır (karma huni)

Soğuk teklifte yorumsuz tavan ~%23–25. Davetli teklifte ~%35–45 (müşteri seni zaten seçmiş). Bu yüzden %30'un yolu, teklif sayısını azaltmadan **tekliflerin içindeki davet payını ~%40'a çıkarmak**:

| Karışım | Soğuk (%23) | Davet (%40) | Teklif başına |
| --- | --- | --- | --- |
| Şimdi | %95 | %5 | ~%24 |
| Hedef | %60 | %40 | **~%30** |

Davet motoru (tanıdık, görüşme, saatlik, ücretsiz iş gerektirmez):
1. **Profil SEO:** Başlık müşterinin aradığı kelimeyle: "WordPress & Elementor Fixes | Speed, Mobile, Landing Pages". Overview'un ilk 2 satırı ve 15 skill etiketi, ilanlarda en sık geçen kelimelerle birebir (Vibeworker ilanlarından çıkarılır).
2. **2 uzmanlaşmış profil:** (a) WordPress/Elementor, (b) Google Sheets/Apps Script + Python otomasyon. Her biri kendi aramasında çıkar; davet yüzeyi 2 katı.
3. **3 Project Catalog paketi:** Mobil düzeltme, hız optimizasyonu, Apps Script otomasyonu. Katalog ayrı arama kanalıdır, paket sayfası davet getirir.
4. **Availability Badge sürekli açık** (~%50 daha fazla davet) ve **davete ilk 1 saatte yanıt**. Yanıt hızı arama sıralamasını etkiler.
5. **Portföy = arama yüzeyi:** Her canlı demo başlığı arama kelimesi taşır ("Elementor mobile menu fix — before/after").
6. **Davetlere öncelik:** Davet gelince sniper ekibi (§20–21) önce ona çalışır, boost gerekmez. `go_score.py --invite`.

Ölçüm: Ek B log'unda her teklif `kaynak: soğuk/davet` ile işaretlenir. 2 haftada davet payı %20'nin altındaysa önce profil başlığı ve etiketler değiştirilir.

### 22.3 Araştırmacı ajanın aracı: `scripts/site_audit.mjs`

```bash
node scripts/site_audit.mjs https://musteri-sitesi.com audit-out
```

390/768/1366 px ekran görüntüsü + yatay taşma yapan elemanlar, kırık görseller, konsol hataları, başarısız istekler, LCP, küçük dokunma hedefleri. Çıktı `report.json`; Visual ajan PNG'yi işaretler, Writer ilk cümleye **somut bulguyu** koyar ("Your hero overflows 38px on iPhone — here's the fix"). Müşterinin URL'si yoksa ilandaki ekran görüntüsü/tarif kullanılır. Ücretsiz iş değil: sadece teşhis + küçük dilim, teslimat sözleşmeden sonra.

### 22.4 Teklif-hazır ilk yanıt

Müşteri mesaj attığında 10 dk içinde tek mesajda: (1) tek cümle sorun özeti, (2) 3 maddelik plan, (3) sabit fiyat + teslim süresi, (4) **küçük ilk milestone** ("Milestone 1: mobile fix, $X, 24h"), (5) tek soru. Görüşme istenirse: "I work async — here's a 45s walkthrough video instead." Writer bu mesajı teklifle birlikte önceden hazırlar; müşteri yanıtlayınca sadece uyarlanır.

### 22.5 Hazır dilim kitleri (Builder 3 dk)

`kits/` altında arena başına iskelet tutulur: Elementor mobil düzeltme CSS'i, landing page hero bloğu, Apps Script tetikleyici/e-posta şablonu, Python scraper/CSV temizleyici, n8n webhook akışı, Shopify/Webflow CSS düzeltme. Builder sıfırdan değil kitten başlar → her GO'da çalışan dilim, maliyet artmadan.

### 22.6 Hız + öğrenme döngüsü

- **Hız:** Vibeworker bildirimi → tek komutla JOB_BUNDLE (ilan metni yapıştır) → ekip paralel çalışır; hedef bildirimden gönderime **≤15 dk**. Gönderim her zaman **manuel** (ToS: otomatik teklif yok).
- **Arketip A/B:** Her teklif log'a arketip (Teşhis / Dilim / Video / Soru-önce), boost, yaş, teklif sayısı, sonuç (görüldü/yanıt/işe alım) ile yazılır. 10 teklifte bir: en düşük açılma → kart cümlesi değişir; en düşük yanıt → ön-iş türü değişir; en düşük işe alım → ilk yanıt/milestone değişir. Kazanan arketip Writer prompt'una örnek olarak eklenir.
- **Yargıç kalibrasyonu:** Kazanan/kaybeden gerçek teklifler holdout yargıca (grok) körlemesine verilir; skor sonuçla uyuşmuyorsa T1–T8 eşikleri güncellenir.

---

## 23) Sohbet ve mülakat hattı — teklif hattından ayrı model sistemi

Teklif hattı (§12) kartı açtırır. Bu hat **mesajdan sözleşmeye** kadar çalışır. Ayrı çünkü amaç farklı: artık "tıklar mı" değil, **"şimdi offer gönderir mi"**. Kayıp en çok burada olur (§20.3).

**Tetik:** Upwork'te müşteri mesajı, "invited to interview" veya offer bildirimi. Sen mesajı (ve varsa önceki konuşmayı) sohbete yapıştırırsın: `SOHBET` + mesaj.

### 23.1 Sohbet ekibi (tek sohbet, alt agent)

```
Sen: SOHBET + müşteri mesajı
 └─► Composer 2.5 — CHAT_BUNDLE hazırlar (ilan, gönderilen teklif, ön-iş, tüm konuşma, fiyat, M1)
      ├─► [Task] Triage     (gemini-3.8-flash-low)   → mesaj tipi + risk bayrakları (JSON)
      ├─► [Task] Yazar      (claude-opus-5-5-low)    → cevap + (gerekirse) milestone metni
      ├─► shell: reply_lint.py --stage <tip>         → modelsiz kural kontrolü
      ├─► [Task] Müşteri    (gpt-5.6-terra-medium)   → bu müşteri personası: "offer gönderir misin?"
      └─► [Task] Bekçi      (grok-4.7-low)           → ToS + senin sınırların + scope/fiyat tutarlılığı
      └─► Composer: PASS → sana kopyala-yapıştır cevap; FAIL → tek düzeltme turu (max 2)
```

Hedef süre: mesaj geldikten **≤ 10 dk** içinde gönderim. Gönderen her zaman sensin.

**Scope (§7.1):** Triage önce müşteri mesajındaki **asıl isteği** çıkarır. Cevap önce onu kapatır; site audit bulgusu yalnızca ilgiliyse veya plan-2 olarak geçer.

### 23.2 Triage — mesaj tipleri

| Tip | Örnek | Ne yapılır | `--stage` |
| --- | --- | --- | --- |
| **İlk mesaj / ilgi** | "Hi, can you tell me more?" | R1: bulgu + milestone metni + tek ihtiyaç | first |
| **Yazılı mülakat soruları** | "How would you do X? Timeline? Similar work?" | Her soruya numaralı kısa cevap + kanıt linki + milestone | interview |
| **Sesli/video görüşme isteği** | "Can we do a quick call?" | R4: yazılı çalışma + **önceden kaydedilmiş sessiz, altyazılı video** (Görselci ajan, §21.1) sorulacak noktaları cevaplar | objection |
| **Fiyat itirazı** | "Too expensive / others quoted less" | R2/R3: scope küçült, fiyatı değil | objection |
| **Test / ücretsiz örnek** | "Do a small test first" | R5: ücretli mikro milestone ($15–29) | objection |
| **Saatlik ısrarı** | "Send an hourly contract" | Fixed offer öner; ısrarda nazikçe çekil (§21.2) | objection |
| **Offer hazırlığı** | "What should I put in the milestone?" | Kopyalanabilir milestone: scope + $ + teslim saati | offer |
| **Scope büyümesi** | "Can you also add…?" | Evet ama **ayrı milestone + fiyat** | scope |
| **Kırmızı bayrak** | Upwork dışı ödeme/iletişim, "önce iş sonra ödeme", fonlanmamış başlangıç | Kibar ret + Upwork kuralı; gerekirse konuşmayı bitir | — |

### 23.3 Müşteri hakemi (Terra Medium) — sorular

Aynı müşteri personası (ilandaki dil, bütçe, müşteri geçmişi) konuşmanın tamamını okur:

1. "Would you send an offer **right now**? yes/no."
2. "What single thing is still stopping you?"
3. "Did the reply answer **every** question you asked? List unanswered ones."
4. "Does anything sound like a bot, a template, or a pushy sales line?"

`no` veya cevapsız soru varsa yazar tek turda sadece o engeli çözer. 2. tur da `no` ise Composer sana engeli yazar; karar senin.

### 23.4 Bekçi (Grok Low) — sınırlar

FAIL sayılır: Upwork dışı iletişim/ödeme; telefon/video görüşme teklifi; saatlik sözleşme veya takip kabulü; ücretsiz iş; teklifteki fiyat/süreyle çelişen rakam; teslim edemeyeceğin söz; yorum karşılığı indirim. `reply_lint.py` aynı kuralların ilk süzgeci, bekçi bağlama bakar ("I can call" gizli teklifi, önceki mesajla çelişen fiyat).

### 23.5 Yazılı mülakat şablonu

```
Answers in order:
1) [Soru 1 kısa cevabı + neden]
2) Timeline: [çıktı 1] by [gün/saat ET], [çıktı 2] by [gün].
3) Similar work: [1 link: demo veya yapılmış dilim].

Milestone text you can paste: "[scope], $[fiyat], delivered by [gün]".
Anything unclear, ask here and I'll answer within the hour.
```

### 23.6 Sesli görüşme istenirse

- Cevap R4 + **45–90 sn sessiz, altyazılı ekran kaydı**: müşterinin sitesinde sorun → plan → teslim. Görselci ajan hazırlar, sen konuşmazsın.
- Müşteri görüşmede ısrar ederse: "Totally understand if a call is a must for you; in that case I'm probably not the right fit, and I wish you a smooth project." Konuşma kapanır, log'a `kayıp: call` yazılır. 10 kayıpta 3+ `call` ise video şablonu değişir.

### 23.7 Offer geldikten sonra

1. Offer'ı kontrol et: fixed mi, milestone tutarı ve scope yazışmayla aynı mı. Değilse kabul etmeden önce düzeltme iste.
2. Kabul → R-işe alım mesajı (§14 son satır): "Backup taken, starting now. First update by [TIME]."
3. Fonlanmadan iş yok. Teslimde 7 gün düzeltme sözü; kapanışta §19'daki kurala uygun yorum ricası.

### 23.8 Ölçüm

Ek B log'una: `mesaj tipi`, `cevap süresi (dk)`, `hakem yes/no`, `sonuç (offer / sessiz / kayıp: fiyat|call|saatlik|başkası)`. 10 konuşmada bir: en sık kayıp nedeni için şablon değişir. Hedef: mesaj → offer **≥ %60**.

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
["woocommerce","shopify app","shopify store setup","react app from scratch","saas mvp","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes"]
```

Sıfırdan mağaza/uygulama işleri (`shopify app`, `react app from scratch`, `saas mvp`) exclude'da; küçük Shopify/React düzeltmeleri P7 ile gelir (§21.3).

| Preset | `budget_min_fixed` | `connects_max` | `keywords_include` (herhangi biri) | Ortak exclude'a ek |
| --- | --- | --- | --- | --- |
| **P1 WP-Fix** | 50 | 12 | wordpress, elementor, divi, wpbakery, white screen, critical error, plugin conflict, contact form, wpforms, contact form 7 | custom plugin, plugin development, theme development, membership, lms, from scratch |
| **P2 Speed-Mobile** | 50 | 12 | page speed, pagespeed, core web vitals, gtmetrix, lighthouse, site speed, slow website, load time, mobile responsive, mobile friendly, responsive fix | seo retainer, monthly seo |
| **P3 Landing-Local** | 80 | 12 | landing page, one page, one-page, single page, small business website, simple website, hvac, plumbing, plumber, roofing, electrician, contractor, home services, cleaning, landscaping, google ads, lead generation | — |
| **P4 Sheets-Excel** | 50 | 8 | google sheets, excel, spreadsheet, vlookup, xlookup, pivot table, conditional formatting, formula, dashboard, tracker, calculator | data entry, bookkeeping, power bi, tableau, financial model, vba |
| **P5 Small-Web** | 50 | 8 | quick fix, small fix, small change, small task, html css, css fix, figma to html, psd to html, migrate, migration, dns, ssl, hosting, github pages, netlify, ga4, google tag manager, pixel, calendly, booking widget | — |
| **P6 Scripts-AI** (çan kapalı) | 50 | 12 | python, apps script, google apps script, automation, automate, csv, pdf, openai, chatgpt, claude, api integration, webhook, zapier, n8n, make.com | linkedin, instagram, facebook, captcha, scrape, scraping, machine learning model, fine-tune, fine-tuning, computer vision |
| **P7 Stretch-Fix** | 50 | 12 | shopify theme, shopify css, webflow, wix, squarespace, react bug, next.js bug, email template, html email, ga4, google tag manager, meta pixel, zapier, make.com, airtable, notion | from scratch, full store, ongoing, 40 hours |
| **Shortlist** (tek filtre, çan kapalı) | 50 | 12 | P1–P7 include listelerinin birleşimi | football, power bi, tableau, exhibitor, exhibitor list, trade show, sponsors, lead list, data entry, linkedin, instagram, facebook, scrape, scraping, captcha, selenium, playwright, video call, phone call, zoom, google meet, native english, native speaker, kimai, custom plugin, plugin development, theme development, from scratch, manuscript, mobile game, user acquisition, voxel |

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
