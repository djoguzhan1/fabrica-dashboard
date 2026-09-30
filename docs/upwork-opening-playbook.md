# Açılış oyun kitabı — kart ilk 150 karakterde kazanılır

**Tarih:** 2026-09-30 · **Üst doküman:** `upwork-arena-strategy.md` (1. parti bulgular). Bu doküman **2. parti** kaynaklara dayanır: müşterilerin kendi anlatımları, $1M+ kazanan veteranlar, ilk işini kazanan yeni freelancer'lar.
**Tek amaç:** müşteri kartı gördüğü anda "bu kişi işimi zaten çözmeye başlamış" desin ve **tıklasın**.

---

## 1) 2. parti bulgular — müşteriler ve veteranlar ne diyor

| Kaynak | Söylenen | Bizim için anlamı |
| --- | --- | --- |
| Müşteri, r/Upwork "Proposal thoughts as a client" | Kendini anlatan kısımları **atladım**. Metrikleri profilde görürüm. Ne yapacağını, milestone'ları, süreyi, iletişimi görmek istedim. | Kendini anlatma, profil zaten anlatıyor. **İş akışını** göster. |
| Müşteri, r/Upwork cover letter review | "İlan başına 100–150 aynı AI teklifi alıyorum. Açılışın açtırmıyor, soru çok uzun, CTA yok." | Sel AI şablonu. İnsan gibi, kısa, somut olan ayrışır. |
| $1M+ kazanan UX tasarımcı | İlk mektupta soru sorma, müşteri cevaplamaya üşenir. **Doğrudan öneriyle başla:** "For your project I'd start by…" | Açılış = **teşhis/öneri**, soru değil. |
| r/Upwork, Top Rated Plus soruyor | "Rozetini ilk cümlede yazma, müşteri zaten görüyor. Neredeyse herkes top-rated, anlamı yok. Upwork formatı değişti, kartta ~bir buçuk cümle görünüyor." | Veteranın rozeti bile artık ayırt etmiyor. **Kartta ayırt eden tek şey metin.** |
| r/Upwork, "13 teklif, 0 görüntülenme" | Kartta ~250 karakter görünüyor. Açılışta iş etiketi ve "I help companies…" gibi belirsiz bir cümle vardı. En güçlü rakam 6 paragraf aşağıdaydı. Müşteri kartı açmadan okuyup **junk mail** gibi geçti. | Bizim 0 görüntülenmemizin birebir tarifi. En güçlü şey **ilk satırda** olmalı. |
| Yeni freelancer, 3 teklifte iş (LinkedIn) | Loom teklifleri: müşterinin problemini parçalayıp çözümü gösteren kısa video. | Loom = "işi başlatmış" kanıtı. |
| Yeni freelancer, 1 teklif → 5 dk'da iş | Yazmadan önce 90 sn Loom: brief'e bak, fark ettiğini söyle. | Önce iş, sonra metin. |
| Sıfır yorumlu profil testi (2026) | Yazılı açılış: "I recorded a 60-second video showing exactly how I'd fix [problem] — link below." Botlar özel ekran denetimi kaydedemez. | Açılışın kendisi **kanıta davet**. |
| Medium, ilk iş hikâyesi | 5–10 teklifli ilan, her satır ilana özel, "Upwork'te yeniyim, işte yeni değilim", 30 dk'da cevap, ücretli test, işe alım. | Az rakipli ilan + tam özelleştirme + hız. |

**Sentez:** 60K$'lık adamın kartta avantajı rozet ve JSS. Ama müşterinin gözünde "neredeyse herkes top-rated", yani kartta **fark yaratmıyor**. Fark yaratan tek şey açılış metni ve veteranların çoğu orada şablon kullanıyor. **Savaş alanı eşit: ilk 150 karakter.**

---

## 2) Kök ikna ilkesi — "Önce yap, sonra teklif et"

Mektup kalıbı değil, **sıra** değişiyor:

1. **İlanı oku → işin en küçük gerçek parçasını yap** (10–20 dk).
2. O parçayı **görünür** yap: link, Loom, ekran görüntüsü, canlı demo.
3. Açılışı **o parçanın sonucu** olarak yaz.

Müşteri kartta şunu okur: *"I already did X for your Y, here's the link."* Veteran şunu yazar: *"With 8+ years of experience in WordPress…"*. Müşterinin beyninde ilki **iş**, ikincisi **reklam**.

Neden kökten işe yarar:
- **Risk sıfırlanır:** müşteri parayı vermeden önce kaliteyi görmüş olur. Veteranın geçmişi = güven vaadi; senin parçan = **güven kanıtı**.
- **AI-sel'den çıkar:** 100–150 AI teklifi arasında gerçek bir çıktı taşıyan tek teklif.
- **Uma'yı besler:** yaptığın parça ilanın gereksinim kelimeleriyle anlatılır → eşleşme puanı.
- **Veteran bunu yapmaz:** $100–300'lık işe 15 dk ön-iş ayırmak onun ekonomisine uymaz. Senin için tek fırsat bu. **Asimetri bizden yana.**

Dürüstlük sınırı: sonuç uydurma, müşterinin görmediği iş sahiplenme. Sadece **gerçekten yaptığın** parçayı göster.

---

## 3) Ön-iş menüsü — iş türüne göre ne yapılır (10–20 dk)

| Arena | Ön-iş (gerçek parça) | Açılışta ne yazar |
| --- | --- | --- |
| Elementor / WP düzeltme | Sitesini 390 px'te aç, kırılan 1–2 yeri işaretli ekran görüntüsüyle göster, sebebini yaz (padding, container, sticky header vb.) | "Your [sayfa] breaks at 390 px because [sebep], marked screenshot + fix below." |
| Landing page | Hero bölümünü WP Playground'da (CoolAir/ProFix altyapısı) onun metniyle kur | "I built your hero section with your copy already, live link:" |
| Hız / CWV | PageSpeed çalıştır, LCP öğesini ve en büyük 2 sebebi bul | "Your mobile LCP is [X]s, caused by [öğe]; two fixes get it under 2.5s." |
| Sheets / Apps Script | İstenen akışın küçük bir çalışan kopyası (örnek sheet + 20 satır script) | "I made a working copy of your [form→sheet→email] flow, test it here:" |
| Python | Örnek girdiyle çalışan script, girdi → çıktı ekran görüntüsü | "Ran a sample of your [CSV/PDF] through a script, before/after:" |
| Küçük web / JS / React düzeltme | Hatayı yeniden üret, sebebi tek satırda | "The [hata] comes from [sebep], one-line fix, shown below." |
| n8n / API | Akışın düğüm şeması (PNG), kritik noktası (auth, rate limit) | "Mapped your [A→B] flow in 5 nodes; the tricky part is [X], handled." |
| Tasarım / Figma / UX | Tek ekranın önce/sonra mini revizyonu | "Redid your [ekran] above the fold, before/after:" |
| Site yok, sadece brief | Brief'ten 3 maddelik yapı taslağı + bir kör nokta | "Your brief has one gap that changes the build: [X]. Plan below." |

**Süre kuralı:** $50–99 → 10 dk (ekran görüntüsü/tek teşhis). $100–199 → 15 dk (Loom 60 sn veya mini demo). $200+ → 20 dk (çalışan parça + Loom).

---

## 4) Açılış arketipleri — 150 karakterde tam anlam

Her açılış **kartta bitmeli**: 150 karakter içinde cümle tamamlanır, bir fayda ve bir merak kancası taşır. Güçlüden zayıfa:

| # | Arketip | Kalıp | Örnek (WP) |
| --- | --- | --- | --- |
| A1 | **Yapılmış iş** | "I already [yaptım] for your [şey], [link/ek]." | "I rebuilt your pricing hero in Elementor with your copy, live preview link below, mobile included." |
| A2 | **Teşhis + sebep** | "Your [şey] [sorun] because [sebep], fix below." | "Your header overlaps the form on iPhone because the sticky container has no top offset, marked screenshot below." |
| A3 | **Rakam** | "[Metrik] is [X] on [cihaz]; [N] changes fix it." | "Your homepage LCP is 5.8s on mobile; it's one 2.4 MB hero image and a render-blocking font." |
| A4 | **Çerçeve değişimi** | "You asked for [X], but [Y] is what's blocking you." | "You asked for a redesign, but only 2 sections break on mobile, a fix is faster and keeps your SEO." |
| A5 | **Karar kısayolu** | "Short version: [çözüm], [süre], [fiyat]." | "Short version: 3 Elementor fixes, done in 24h, fixed $90, marked screenshots of each below." |
| A6 | **Kör nokta** | "One thing your post doesn't mention will decide this: [X]." | "One thing decides this migration: your WooCommerce order history, here's how I'd move it safely." |

**Yasaklar (ilk 150 karakter):** "Hi/Hello there", "Dear hiring manager", "I", "I'm", "experience", "years", "excited", "I came across", "I hope", "Top Rated", rozet/JSS, iş başlığını tekrar yazmak, soruyla açmak. Müşterinin adı biliniyorsa sadece "Hi Sarah," (7 karakter) olur.

---

## 5) 10/10 açılış testi — göndermeden önce puanla

Her madde 2 puan. **10/10 değilse gönderme, yeniden yaz.**

| Test | 2 puan | 0 puan |
| --- | --- | --- |
| **Kendi kelimesi** | İlandaki bir isim/sayfa/araç aynen geçiyor | Genel ifade ("your website") |
| **Somutluk** | Sebep, rakam, cihaz, piksel, dosya adı | Sıfat ("clean", "professional") |
| **Yapılmış iş kancası** | Link/ek/Loom'a işaret ediyor | Vaat ("I can do") |
| **Kartta bitiyor** | ≤150 karakterde anlam tam | Cümle kartın dışında bitiyor |
| **Sıfır ben** | Özne müşteri veya iş | "I/I'm/my experience" |

Kontrol: açılışı sadece kartta okuyan biri **başka hiçbir teklifte aynı cümleyi görmeyecek** mi? Evet değilse 0/10.

---

## 6) Kartın geri kalanı — metin dışı sinyaller

Müşteri kartta isim, foto, rozet, ücret, JSS ve profil başlığını görür (Upwork kendi rehberinde başlığın da tıklamayı etkilediğini söylüyor).

| Öğe | Karar |
| --- | --- |
| **Başlık** | Sonuç + hız + alan: `Elementor & WordPress Fixes in 24h · Landing Pages · Google Sheets Automation`. Genel "Web Developer" değil. |
| **Foto** | Yüz net, göz teması, sade arka plan, gülümseme. Logo/avatar yok. |
| **Saatlik ücret** (fixed işte bile kartta görünür) | $5–15 "ucuz = risk" sinyali verir. Arena ortalamasının altına inme: **$25–35** bandı. Fixed teklif fiyatı ayrıca belirlenir. |
| **JSS yok** | Telafi metinde: yapılmış iş kancası JSS'in yerini tutar. |
| **Rozet** | Rising Talent (bkz. arena stratejisi §8), gelirse karta çıkar. |

---

## 7) Mektubun gövdesi — açılıştan sonra (açıldıysa 15–30 sn)

Müşterinin anlattığı istek: *ne yapacaksın, milestone'lar, süre, inceleme, iletişim.* Sırasıyla:

1. **Açılış** (A1–A6).
2. **Kanıt satırı:** link / "Loom (60 sec):" / "Attached: 1-page notes". Tek satır.
3. **Akış (3 madde):** her madde = çıktı + gün. Son madde test (390/768/1366 px) ve teslim şekli.
4. **Fiyat + milestone:** "Fixed $X. Milestone 1 = [çıktı 1], approve only when you see it."
5. **İletişim:** "Everything in writing + Loom updates; replies within 1 hour (GMT+3)."
6. **Yenilik satırı (opsiyonel, 1 cümle):** "New to Upwork, not to WordPress: [demo linki]."
7. **CTA:** tek, 5 saniyelik karar: "Want me to start with [çıktı 1] today?" Soru sormak değil, **evet/hayır kararı**.

Toplam 90–150 kelime. Başlık, bullet'lı "WHY ME" bölümü, emoji, uzun liste yok.

---

## 8) Müşteri tipine göre ayar (aynı ilke, farklı vurgu)

| Müşteri tipi | Belirtisi | Açılış vurgusu | Gövde vurgusu |
| --- | --- | --- | --- |
| Acil / bozuk site | "ASAP", "urgent", "broken" | A2 teşhis + "today" | Süre saatle, milestone küçük |
| Detaycı / teknik | Uzun ilan, araç isimleri | A3 rakam veya A6 kör nokta | Adımlar teknik, test listesi |
| Ajans (tekrar iş verir) | "our client", "ongoing" | A5 karar kısayolu | Süreç, iletişim ritmi, teslim formatı |
| Bütçe hassas | Düşük bütçe, "simple" | A4 çerçeve ("fix yeter, redesign değil") | Kapsamı daralt, fiyatı sabitle |
| Yeni müşteri (0 işe alım) | Hire rate yok | A1 yapılmış iş (güven en çok burada lazım) | Milestone güvencesi, net adımlar |
| Tecrübeli müşteri (10+ işe alım) | Yüksek hire rate | A2/A3 (şablonları ezbere biliyor) | Kısa, profesyonel, sıfır dolgu |

---

## 9) Tam örnek — Elementor düzeltme, $120, 18 teklif, 3 veteran boost'lu

**Veteranın kartı (tipik):**
> Hello! I have carefully read your job description and I'm confident I'm the perfect fit. With 9+ years of WordPress and Elementor experience…

**Bizim kart (141 karakter):**
> Your /services page breaks at 390 px: the 3-column container doesn't stack and the CTA falls off screen. Marked screenshots + fix plan below.

**Gövde:**
> Loom (70 sec): [link], I walk through both issues on your live site.
>
> Plan:
> 1) Stack the service columns and fix the CTA on mobile, same day
> 2) Check the other 4 pages you listed at 390 / 768 / 1366 px, day 2
> 3) Send a before/after screenshot sheet, then you approve
>
> Fixed $120, 2 days. Approve milestone 1 only after you see /services fixed on your own phone.
> Everything in writing, updates by Loom, replies within 1 hour.
>
> Want me to start with /services today?

Müşterinin kafası: veteran = "yine aynı şablon". Bizimki = "sayfamı açmış, sorunu bulmuş, telefonumdan kontrol edebilirim". **Tıklanan kart bu.**

---

## 10) Hız ve zamanlama

- **İlk 2 saat altın, 6 saat sınır** (Uma shortlist'i birkaç saat içinde oluşur). Ön-iş 10–20 dk'yı geçmez.
- Bildirim → 2 dk ön-kontrol (arena stratejisi §6) → 15 dk ön-iş → 5 dk metin → 10/10 testi → gönder + boost tablosu.
- Müşteri yazınca **≤1 saat** içinde cevap ver ve ilk mesajda bir sonraki küçük çıktıyı ekle ("Here's the fixed mobile preview for /services, same as in the Loom").

---

## 11) Ölçüm — açılışın çalıştığını nasıl bileceğiz

`upwork-proposal-log.md`'ye ekle: `arketip (A1–A6)`, `ön-iş türü`, `açılış puanı (/10)`, `açıldı mı`, `cevap`.

- 10 teklif sonra açılma oranını arketip bazında karşılaştır; en iyisine ağırlık ver.
- Kart açılıp cevap gelmiyorsa sorun gövde veya fiyat; kart hiç açılmıyorsa sorun açılış veya başlık/foto.
- Hedef (master plan): açılma ≥ %70.
