# Upwork — 72 Saatte İlk İş: Operasyon Planı

Oğuzhan S. · Bursa (GMT+3) · Hedef müşteri: ABD/İngiltere · Profil: 0 review, 0 iş (gerçek).
Tek hedef: **72 saat içinde en az 1 kabul edilmiş iş** (aktif contract veya fonlanmış milestone).

Sabit kurallar (tüm İngilizce metinler için): sadece İngilizce; sahte müşteri/review/deneyim yok; demolar "CoolAir HVAC style demo" / "emergency plumbing style demo" olarak anılır; Fiverr, vergi, ödeme aracı adı geçmez; "Dear client", "I would be honored", ninja/rockstar/guru/passionate yok; teklif içinde iletişim bilgisi yok (Upwork ToS).

Canlı linkler (yalnızca bunlar):

| Sayfa | URL |
| --- | --- |
| Portfolio hub | https://djoguzhan1.github.io/web-dev-portfolio/ |
| CoolAir HVAC style demo | https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/ |
| Emergency plumbing style demo | https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/ |
| Upwork profili | https://www.upwork.com/freelancers/~01f40a508feb14b1ee |

Saat dilimi (Eylül–Ekim 2026): US Eastern = EDT = GMT+3 **− 7 saat**; İngiltere = BST = GMT+3 **− 2 saat**.

Kaynaklar (Eylül 2026): Upwork yardım merkezi (Connects, Boosted Proposals, Edit proposal, Advanced search, Freelancer Plus, Availability Badge, Rising Talent, ToS), Upwork Spring 2026 ürün güncellemesi (Uma Recruiter shortlisting), GigRadar / OutBid / Upwatcher hız ve boost istatistikleri. Sayılar sektör ölçümüdür, garanti değildir.

---

## 0) Executive summary

**Ana tez.** Sıfır review'lı hesap için kazanma formülü üç çarpan ve bir üstür: **Hız × Eşleşme × Kanıt**, üs = **Hacim**.

- Hız: ilan yayınlandıktan sonraki ilk 5 dakikada gönderilen teklif, 30–60 dk sonra gönderilenin ~4 katı hire oranı alır (OutBid: %8,2 → %2,1; 6 saat sonrası %0,5). Cevap oranı da 3–4 dk'da %11,9, 5–6 dk'da %6,9'a düşer.
- Eşleşme: müşteri listede sadece ad, fotoğraf, başlık, ücret ve cover letter'ın **ilk iki cümlesini** görür; Uma Recruiter (Basic üyelikte de "zaman zaman", ~6 saat içinde) profil uygunluğu + portfolyo + teklif metni + eleme sorularına göre shortlist yapar. Bütçe dışı teklifler alta itilir.
- Kanıt: review yok → tıklanabilir kanıt var. İki canlı demo + Lighthouse 99–100 + "milestone fonlanmadan iş başlamaz, onaylamadan ödeme çıkmaz" güvencesi.
- Hacim: Connects bol → 72 saatte **100 teklif** (35/33/32), en az %60'ı ilan yaşı <5 dk iken.

**%95 kriteri nasıl karşılanıyor (dürüst model).** P(≥1 iş) = 1 − (1 − p)^n. p = teklif başına contract olasılığı; 0 review'lı, hızlı, eşleşmiş, kanıtlı ve intro fiyatlı teklif için ağırlıklı ortalama **p ≈ %3,2** (ilk 5 dk: ~%4; 5–15 dk: ~%2; 15–60 dk boost'lu: ~%2; karışım %60/%25/%15).

| p (teklif başı) | n = 50 | n = 75 | n = 100 | n = 125 |
| --- | --- | --- | --- | --- |
| %2,0 | %64 | %78 | %87 | %92 |
| %2,5 | %72 | %85 | %92 | %96 |
| **%3,2** | %80 | %91 | **%96** | %98 |
| %4,0 | %87 | %95 | %98 | %99 |

Kalan ~%4–5 riskin çoğu **korelasyonlu** risktir (tüm teklifleri aynı anda öldüren tek sebep: doğrulanmamış kimlik, Türkçe başlık, $3/sa ücret, kötü fotoğraf). Bu yüzden Bölüm 1 ön koşuldur ve Gün 1 sonundaki "görüntülenme oranı" kontrolü bu riski 24 saatte yakalar.

**3 günlük sayısal hedefler**

| Metrik | Gün 1 | Gün 2 | Gün 3 | 72 saat toplam |
| --- | --- | --- | --- | --- |
| Gönderilen teklif | 35 | 33 | 32 | **100** |
| İlan yaşı <5 dk gönderim payı | ≥%55 | ≥%60 | ≥%65 | ≥%60 |
| Tier-1 / Tier-2 karışımı | 55/45 | 60/40 | 65/35 | ~60/40 |
| Boost'lu teklif | ≤7 | ≤7 | ≤6 | ≤20 (%20) |
| Müşteri görüntüleme oranı | ≥%40 | ≥%40 | ≥%40 | ≥%40 |
| Cevap (müşteri mesajı) | ≥2 | ≥5 (küm.) | ≥7 (küm.) | ≥7 |
| Interview (canlı/derin yazışma) | ≥1 | ≥2 (küm.) | ≥3 (küm.) | ≥3 |
| Teklif (client offer) | 0–1 | ≥1 (küm.) | ≥2 (küm.) | ≥2 |
| **Fonlanmış contract** | – | 0–1 | **≥1** | **≥1** |
| Connects harcaması | ~450 | ~440 | ~430 | ~1.320 (≈ $200) |

Bütçe (Varsayım): Freelancer Plus $19,99 (100 Connects dahil) + ~1.200 Connects satın alma (≈ $180) + Availability Badge (~20 Connects/hafta). Toplam ≈ **$200–230**. İlk iş $49–$129 arası gelir; asıl kazanç ilk review'dur.
Maliyet katmanı: **Ek C** (nakit ≈ $120 / ≈ $90) · **Ek D** (ilk cevap öncesi nakit tavanı ≈ $35, toplam sprint ≈ $45–70, aynı P(≥1) modeli).

**Şimdi yap**
1. Bölüm 1'deki profil yamasını bu gece bitir (90 dk); yama bitmeden teklif gönderme.
2. Freelancer Plus'ı aç, 400 Connects al, Availability Badge'i aç (haftalık max 20).
3. Bölüm 2'deki 12 kayıtlı aramayı ve anlık bildirim aracını kur; Bölüm 5 şablonlarını metin genişletici/notlara yükle.

---

## 1) Profil → Teklif dönüşümü

Varsayım: Profil URL'si otomasyonla açılamadı (Upwork JavaScript doğrulaması). Analiz, daha önce paylaşılan ekran görüntülerine ve `docs/upwork-profile.md` bulgularına dayanır. Bölüm A/B metinleri zaten uygulanmışsa 1–3. maddeler "kontrol et" olarak okunur.

**Müşterinin teklif listesinde gördüğü katman** (ilk 2 saniye): fotoğraf, ad, başlık, ücret, ülke, rozetler (ID doğrulandı / Boosted), cover letter'ın ilk 2 cümlesi. Profil sayfasına geçen müşteri (ikinci 20 saniye): overview'un ilk 250 karakteri, portfolyo kapakları, tamamlanma/rozet, çalışma geçmişi. Yama listesi bu iki katmana göre sıralanmıştır.

**Yama listesi**

| # | Alan | Şu an (ekran görüntüsü) | Yama | Neden |
| --- | --- | --- | --- | --- |
| 1 | Başlık | Türkçe ("Web ve Yazilim Gelistirme") | Headline A (aşağıda) | Liste katmanında ilk okunan metin; aramada eşleşme |
| 2 | Saatlik ücret | $3,00/sa | **$20/sa** | $3 = "düşük kalite" sinyali; sabit fiyatlı işleri etkilemez |
| 3 | Kimlik doğrulama | Beklemede | Bu gece tamamla (ID + selfie/video) | 0 review'lı profilde en güçlü güven rozeti; bazı müşteriler filtreler |
| 4 | Fotoğraf | Siyah-beyaz, el yüzü gölgeliyor | Renkli, iyi ışık, önden, sade arka plan, hafif gülümseme | Liste katmanındaki tek görsel |
| 5 | Overview ilk 250 karakter | Türkçe / genel | Opener A (aşağıda) | Profil sayfasında "Read more" öncesi tek görünen metin |
| 6 | Portfolyo | Boş | 3 öğe: "CoolAir HVAC — Landing Page", "ProFix Plumbing — Emergency Landing Page", "Portfolio Hub — 100/100/100/100 Lighthouse"; her birinde masaüstü + mobil ekran görüntüsü, canlı link, 2 cümle açıklama, iş anahtar kelimeleri başlıkta | Uma "past work" sinyali; teklife "Profile highlights" olarak eklenir |
| 7 | Tamamlanma | %40 | %100: Çalışma geçmişi ("Freelance Web Developer, self-employed", gerçek tarihler) + Eğitim + Bağlı hesap (GitHub djoguzhan1) | Uma ve müşteri filtreleri; Rising Talent ön koşulu |
| 8 | Skills | Dağınık | 20 skill, 3 küme sırasıyla (aşağıda) | Aramada ve Uma eşleşmesinde |
| 9 | Uygunluk | – | "More than 30 hrs/week" + Availability Badge açık | "Available now" filtresi ve davet olasılığı |
| 10 | Dil | – | English: gerçek seviye (Varsayım: Fluent) | Yalan beyan yok; ABD/İngiltere müşterisi kontrol eder |
| 11 | Project Catalog | – | 3 liste (kümelerle aynı); onay 72 saati aşabilir | Ek kanal; sprint için opsiyonel |
| 12 | Ödeme/billing yöntemi | – | Doğrulanmış billing yöntemi ekle | Connects satın alımı ve Rising Talent şartı |

**Headline — 2 seçenek (İngilizce)**

```text
A (69 karakter, varsayılan):
WordPress Bug Fix & Speed Optimization | Local Business Landing Pages

B (68 karakter, Tier-2 payı %50'yi geçerse):
WordPress Bug & Speed Fixes | One-Page Landing Sites | Google Sheets
```

Kural: Başlık tektir; sprint boyunca en fazla bir kez değiştir (Gün 1 sonu metriğine göre).

**Overview — ilk 250 karakter (İngilizce)**

```text
Opener A (224 karakter, önerilen — kanıt önce):
I fix broken and slow WordPress sites in 24–48 hours and build one-page landing sites for local businesses (HVAC, plumbing, contractors) in 48 hours. Two live demos are linked below — open them on your phone before you hire.

Opener B (223 karakter — 0 review avantajı önce):
New on Upwork, so instead of reviews you get proof you can click: two live demo sites that score 99–100 on Google Lighthouse. I fix broken or slow WordPress sites in 24–48 hours and build one-page landing sites in 48 hours.
```

Overview'un kalanı `docs/upwork-profile.md` Bölüm B ile aynı kalır; yalnızca "I am new to Upwork…" paragrafı aşağıdaki kanıt paragrafıyla değiştirilir.

**Kanıt paragrafı — demo önce, 0 review avantajı (İngilizce, 96 kelime)**

```text
I am new to Upwork, so you will not find reviews on this profile yet. You will find something you can check yourself: two live demo sites, hand-coded, no page builder. The CoolAir HVAC style demo and the emergency plumbing style demo both score 99–100 on Google Lighthouse (mobile) for performance, accessibility, best practices and SEO, and each page transfers under 250 KB. Run either one through pagespeed.web.dev if you want to verify. Your job is built to the same standard, at intro pricing, with a fixed scope and delivery date agreed before any work starts.
```

**3 skill kümesi (Specialized Profiles 28 Mayıs 2026'da kaldırıldı → kümeler dört yerde yaşar: skill sırası, portfolyo öğesi, Project Catalog listesi, teklif şablonu)**

| Küme | Skill etiketleri (Upwork'te tam eşleşme ile seç) | Portfolyo öğesi | Project Catalog başlığı ("You will get" ekini Upwork koyar) | Şablon |
| --- | --- | --- | --- | --- |
| 1 · WordPress Repair | WordPress, WordPress Bug Fix, Page Speed Optimization, Elementor, WordPress Customization, PHP, CSS | Hub (Lighthouse kanıtı) | …your WordPress bug or speed problem fixed in 24–48 hours | T1 |
| 2 · Local Landing Pages | Landing Page, Landing Page Design, WordPress Landing Page, HTML, Responsive Design, Web Design, Local SEO | CoolAir HVAC + ProFix Plumbing | …a one-page landing site for your HVAC, plumbing or contractor business in 48 hours | T2, T3 |
| 3 · Sheets & Excel | Google Sheets, Microsoft Excel, Excel Formula, Data Cleaning, Spreadsheet Skills, Dashboard | Örnek dashboard (Gün 0'da 45 dk; Varsayım: yapılır) | …your Excel or Google Sheets formulas, cleanup or dashboard done in 24 hours | S4 |

Çeşitlilik böyle "dağınık" değil "üç ürün hattı" gibi görünür: her kümenin bir başlık ifadesi, bir portfolyo öğesi, bir katalog listesi ve bir teklif ailesi vardır.

**Şimdi yap**
1. Başlık A + Opener A + kanıt paragrafını yapıştır; ücreti $20/sa yap; fotoğrafı değiştir.
2. Kimlik doğrulamayı başlat, portfolyoya 3 öğeyi yükle, çalışma/eğitim/GitHub'ı ekle → %100.
3. 20 skill'i küme sırasıyla gir; Availability Badge'i aç.

---

## 2) Niş kilidi + geniş tarama

İlke: **geniş havuzda tara, dar whitelist'e başvur.** Tarama 12 kayıtlı arama + anlık bildirim ile yapılır; başvuru yalnızca aşağıdaki iki tabloya giren işlere.

**Tier-1 — demolarla örtüşen işler (öncelik, boost'a uygun)**

| # | İş tipi | OK bütçe (sabit) | Max scope | Şablon |
| --- | --- | --- | --- | --- |
| 1 | WordPress bug fix: bozuk düzen, plugin çakışması, "critical error"/beyaz ekran, güncelleme sonrası bozulma, mobil sorun, contact form göndermiyor, SSL mixed content | $30–300 | 1 kök neden, 24 saat | T1 |
| 2 | WordPress hız optimizasyonu: PageSpeed / Core Web Vitals / GTmetrix / "site slow" | $50–400 | 1 site, 48 saat, hedef puan yazılı | T1 |
| 3 | Yerel hizmet işletmesi için tek sayfa landing (HVAC, plumbing, elektrik, çatı, temizlik, peyzaj, çilingir, haşere, garaj kapısı, klima) | $100–600 | 1 sayfa, 48 saat | T2 |
| 4 | Google Ads / lead-gen landing page (tap-to-call, form) | $100–500 | 1 sayfa, 48 saat | T2 |
| 5 | Küçük işletme sitesi / yeniden tasarım, 1–3 sayfa | $150–800 | ≤3 sayfa, 4 gün, 2 milestone | T3 |
| 6 | "Make my site mobile friendly" / responsive HTML-CSS düzeltme | $30–200 | 1 site, 24–48 saat | T1 |

**Tier-2 — hızlı kapanan küçük işler (hacim, boost yok)**

| # | İş tipi | OK bütçe | Max scope | Şablon |
| --- | --- | --- | --- | --- |
| 7 | Excel/Sheets formül, temizlik, VLOOKUP/XLOOKUP, pivot, koşullu biçim, CSV birleştirme, küçük dashboard | $20–150 | ≤3 saat efor, 24 saat | S4 |
| 8 | Sheets şablon/tracker/hesaplayıcı | $25–150 | 1 dosya, 24 saat | S4 |
| 9 | Figma/PSD/PDF → tek sayfa HTML/CSS | $50–250 | 1 sayfa, 48 saat | S5 / T2 |
| 10 | Küçük WordPress görevleri: tema kurulumu, sayfa ekleme, form kurulumu, Elementor bölümü, GA4/GTM/pixel kurulumu, takvim/booking embed | $20–150 | ≤3 saat, aynı gün | S5 |
| 11 | Statik HTML sitede düzeltme / CSS parlatma | $20–150 | ≤3 saat, aynı gün | S5 |
| 12 | Küçük WordPress taşıma / DNS / hosting geçişi | $50–200 | 1 site, önce tam yedek | S5 |
| 13 | Hız/mobil denetim raporu (Lighthouse + 5 maddelik düzeltme listesi) — "kapanış ürünü" | $15–75 | 2 saat | S5 |

**Blacklist (tek cümle):** Whitelist dışı stack (React/Next/Vue uygulaması, Shopify tema geliştirme, sıfırdan özel plugin, mobil uygulama, aylık SEO/retainer, WooCommerce ödeme-stok akışı), "önce ücretsiz test görevi", Upwork dışı ödeme/iletişim isteyen, ödeme yöntemi doğrulanmamış + 0 hire + <$20 bütçe, "full-time / long-term hourly team member" ilanları ve scope'u tek cümlede yazılamayan işler → gönderme.

**Kayıtlı aramalar** (Upwork arama kutusu: büyük harf `AND` / `OR` / `NOT`, parantez, tırnak, `*` joker; `+ - !` desteklenmez. Her aramayı kaydet, bildirim aracına aynı sorguyu gir.)

| # | Tier | Sorgu |
| --- | --- | --- |
| Q1 | 1 | `wordpress AND (broken OR "not working" OR error OR "white screen" OR "critical error" OR conflict OR bug) NOT woocommerce` |
| Q2 | 1 | `wordpress AND (slow OR speed OR "page speed" OR pagespeed OR "core web vitals" OR gtmetrix OR lighthouse)` |
| Q3 | 1 | `elementor AND (fix OR broken OR mobile OR responsive OR "not working")` |
| Q4 | 1 | `"landing page" AND (hvac OR plumbing OR plumber OR roofing OR electrician OR contractor OR "home services" OR cleaning OR landscaping OR locksmith)` |
| Q5 | 1 | `("landing page" OR "one page website" OR "one-page website" OR "single page website") AND ("small business" OR local OR "google ads" OR leads)` |
| Q6 | 1 | `("small business website" OR "simple website" OR "basic website" OR "5 page website" OR "3 page website") NOT (shopify OR react OR app)` |
| Q7 | 1 | `("mobile friendly" OR "mobile responsive" OR responsive) AND (fix OR website) AND (html OR css OR wordpress)` |
| Q8 | 1 | `("contact form" OR "form not sending" OR "form not working") AND (wordpress OR website)` |
| Q9 | 2 | `("google sheets" OR excel OR spreadsheet) AND (formula OR formulas OR vlookup OR xlookup OR "pivot table" OR dashboard OR "clean up" OR cleanup OR "conditional formatting")` |
| Q10 | 2 | `("google sheets" OR excel) AND (template OR tracker OR calculator OR "quick" OR urgent OR "small task")` |
| Q11 | 2 | `(figma OR psd OR pdf OR xd) AND ("to html" OR "html css" OR "html/css" OR convert)` |
| Q12 | 2 | `(wordpress OR website OR html OR css) AND (install OR setup OR "set up" OR migrate OR "small change" OR "small changes" OR "quick fix" OR tweak OR urgent OR asap OR "today")` |

Filtreler (tüm aramalarda aynı): Sırala **Newest** · Posted **last 24 hours** · **Payment verified** açık · Job type Fixed **ve** Hourly · Bütçe $20–1.000 · Proposals **Less than 5** ve **5 to 10** (Tier-1'de ilan <15 dk ise 10–15 de kabul) · Experience Entry + Intermediate · Konum tercih: US, UK, CA, AU (zorunlu değil).

**Müşteri kalite filtresi (15 saniye):** Payment verified zorunlu · ≥1 hire veya ≥$100 harcama tercih (0 hire kabul ama Tier-2'de <$20 bütçe ise atla) · hire rate görünüyorsa ≥%40 · ilan metninde scope tek paragrafta anlaşılır · 50+ teklif almış ilan atla.

**Ucuz iş filtresi — operasyonel**

| Kural | Değer |
| --- | --- |
| Taban fiyat | $15 (yalnızca ≤1 saat efor ve ≤6 Connects ise) — ilk review'un değeri fiyattan büyük |
| Tier-2 OK bant | $20–150 sabit; saatlik ise $20/sa × ≤5 saat, contract'ta saat tavanı |
| Tier-1 OK bant | $30–800 sabit; $800 üstü 72 saatte kapanmaz, atla |
| Max scope Tier-2 | ≤3 saat efor · 1 teslimat · 1 revizyon turu · ≤48 saat teslim |
| Max scope Tier-1 | ≤2 iş günü efor · landing = 1 sayfa / fix = 1 kök neden · ≤2 revizyon turu |
| Teklif tutarı | İlan bütçesine eşit veya altında (bütçe dışı teklif alta sıralanır); bütçe intro fiyatın altındaysa fiyatı değil **scope'u** küçült ("$29 = 1 fix, 3 değil") |
| Efor eşiği | Gerçek süre tahminin 1,5 katını aşarsa dur → müşteriye 2 seçenek mesajı (ek milestone / scope küçült) |

**Scope creep kuralları (7)**
1. Fonlanmadan başlama: sabit fiyat ödeme koruması yalnızca fonlanmış milestone'da geçerli.
2. Milestone açıklaması = numaralı teslimat listesi; liste dışı her şey "yeni milestone, tek mesajla fiyat".
3. Saatlik işte Upwork tracker + contract'ta haftalık saat tavanı; tavanı müşteri yükseltir.
4. "Giderken küçük şeyler ekleriz" → "Elbette; her ek madde için tek satır fiyat veriyorum, siz onaylayınca ekliyorum."
5. Ön görüşme ≤15 dk, yalnızca Upwork Messages/Zoom; ücretsiz "deneme işi" yok — onun yerine $15–29 ilk milestone.
6. WordPress'te dokunmadan önce tam yedek; canlıya çıkış müşteri onayıyla.
7. Revizyon = liste içi düzeltme; yeni istek = ek milestone. Bunu teklif metninde ve interview'da aynı cümleyle söyle.

**Şimdi yap**
1. 12 sorguyu Upwork'te kaydet (filtreler dahil) ve bildirim aracına aynı sıralamayla gir.
2. Whitelist/blacklist tablosunu tek sayfa yazdır; her ilanda 30 saniyelik "Tier? Bütçe? Scope tek cümle?" kontrolü.
3. Takip tablosunu aç (Ek A sütunları) — ilk teklifle birlikte doldurmaya başla.

---

## 3) 72 saatlik operasyon

**Günlük blok tablosu (her gün aynı iskelet)**

| Blok | GMT+3 | US Eastern | UK | İş akışı | Aksiyon | Teklif hedefi |
| --- | --- | --- | --- | --- | --- | --- |
| A | 09:00–11:00 | 02:00–04:00 | 07:00–09:00 | Gece ABD ilanları (6–10 saat yaşlı, düşük değer), erken UK | Gece cevaplarını yanıtla (5 dk SLA); yalnızca <10 teklifli Tier-1 tam eşleşme + UK yeni ilanlar | 4 |
| B | 11:00–14:00 | 04:00–07:00 | 09:00–12:00 | UK sabah zirvesi | Tier-1 UK + Tier-2 hacim; bildirim geldikçe <5 dk gönder | 7 |
| C | 14:00–16:00 | 07:00–09:00 | 12:00–14:00 | Düşük akış | Mola/yemek; boost listesi hazırla; şablon ayarı; yalnızca bildirimle | 3 |
| D | 16:00–21:00 | 09:00–14:00 | 14:00–19:00 | **ABD zirvesi** (10–14 ET günün ilanlarının %22,9'u; 11:00 ET tepe) | Tier-1 odak, boost penceresi, interview'lar | 14 |
| E | 21:00–01:00 | 14:00–18:00 | 19:00–23:00 | ABD öğleden sonra (17:00 ET'de ilanların %43'ü ABD müşterisi) | Kapanış mesajları, follow-up, kalan Tier-1; Tier-2 doldurma | 5 |
| – | 01:00–09:00 | 18:00–02:00 | 23:00–07:00 | Uyku | Bildirim sessiz | 0 |

Toplam ≈ 33/gün. Bildirim geldiğinde blok fark etmez: 09:00–01:00 arası whitelist ilanına **5 dakika** içinde teklif.

**Gün bazlı odak**

| | Gün 1 | Gün 2 | Gün 3 |
| --- | --- | --- | --- |
| Odak | Hacim + hız disiplini; profil yamasının işe yaradığını doğrula | Optimizasyon: boost payını ve şablonu Gün 1 verisine göre ayarla | Kapanış: her sıcak lead'e küçük ilk milestone; teklif hacmi korunur |
| Teklif | 35 (T1 55 / T2 45) | 33 (60/40) | 32 (65/35) |
| Boost | ≤7, yalnızca Tier-1 sabit fiyat, ilan yaşı 15–60 dk | ≤7; cevap oranı <%5 ise boost payı %30'a | ≤6; sıcak lead'lerle çakışan blokta boost yerine mesajlaşmaya öncelik |
| Interview limiti | 3 canlı (15 dk) | 3 canlı | 3 canlı + sınırsız yazılı |
| Gün sonu metrik | Gönderim ≥35 · <5 dk payı ≥%55 · görüntülenme ≥%40 · cevap ≥2 | Küm. ≥68 · cevap ≥5 · interview ≥2 · offer ≥1 veya milestone önerisi gönderilmiş | Küm. ≥100 · contract ≥1 |
| Metrik → ayar | Görüntülenme <%25 → liste katmanı sorunu: Opener/ilk 2 cümle B varyantına geç, fotoğraf/ücret/ID kontrol. Görüntülenme OK, cevap 0 → gövde: %100 teklife siteye özel gözlem satırı + bant tabanı fiyat + yalnızca <5 teklifli ilan | Cevap ≥%8 → Tier-1 payını %70'e çıkar, Tier-2'yi azalt. Cevap var, interview yok → cevaba ilk mesajda milestone metniyle dön (Bölüm 5 köprü mesajı) | Interview var, offer yok → interview içinde $19–29 ilk milestone öner (Varyant B). Her cevaplı thread'e 24h follow-up |

**SLA tablosu**

| Olay | Süre | Not |
| --- | --- | --- |
| Whitelist ilan bildirimi → teklif gönderildi | ≤5 dk Tier-1 · ≤10 dk Tier-2 | 30–45 dk "ölü bölge"ye düşen ilanı boost'suz gönderme |
| Müşteri mesajı → cevap | ≤5 dk (09:00–01:00) | İlk cevapta her zaman köprü mesajı (milestone metni dahil) |
| Interview daveti → yanıt | ≤5 dk | 2 zaman aralığı öner, ET olarak yaz ("today 1:30 or 3:00 pm ET") |
| Offer → kabul | ≤15 dk (scope kontrolünden sonra) | Milestone açıklaması listeyle örtüşmüyorsa "request changes" |
| Contract → ilk mesaj | ≤10 dk | Erişim listesi + "başladım" mesajı; ilk teslimat ETA'sı |

**Takvim uyarlaması.** Varsayım: Gün 0 = bu gece (profil yaması), Gün 1 = ertesi sabah 09:00. Gün 1–2 hafta sonuna denk gelirse: hafta sonu ilan hacmi günlük ~%40 düşük (iki gün toplam %19,3) ama rakip de az → Tier-2 filtresini bir bant genişlet ($20–200), UK'ye ağırlık ver, boost bütçesinin %70'ini Pazartesi'ye sakla. Pazartesi–Çarşamba 72 saati (Salı en yoğun gün) mümkünse tercih edilen penceredir.

**Şimdi yap**
1. Telefona ET ve GMT+3 saat dilimlerini ekle; Blok D ve E'yi takvime "Upwork" olarak kilitle.
2. Bildirim aracında sessiz saatleri 01:00–09:00 GMT+3 yap.
3. Gün 1 sonu için 5 metriği takip tablosunun özet sekmesine formülle bağla (görüntülenme %, <5 dk %, cevap, interview, offer).

---

## 4) Connects & boost playbook

**Mekanikler (Eylül 2026)**

| Konu | Değer |
| --- | --- |
| Connect fiyatı | $0,15; özel adet alınabilir (min 10); tutma/rollover sınırı yok; doğrulanmış billing yöntemi gerekir |
| Teklif maliyeti | İlan başına 6–16+ (proje büyüklüğü/talep); ilanda yazılıdır |
| Geri iade | Yalnızca müşteri contract'sız iptal ederse veya Upwork ilanı kaldırırsa; **geri çekme iade etmez** |
| Boost | Açık artırma, 4 sabit slot; yalnızca açık artırma sonunda ilk 4'teysen veya müşteri etkileşirse ücretlenir; ilan başına tek boost; teklif başında karar (yardım sayfaları sonradan boost konusunda çelişkili → gönderim anında karar ver) |
| Boost zamanlaması (GigRadar) | <5 dk: fayda yok · 15–60 dk: +1,7 puan cevap · >60 dk: zararlı · en iyi bant 16–20 Connects · sabit fiyat ≈ saatlik işin 2 katı etki |
| Freelancer Plus | $19,99/ay: 100 Connects + anlık iş bildirimi (≥1 aktif teklif gerekir) + teklif içgörüleri (rakip bid aralığı) + Uma |
| Availability Badge | Haftalık değişken fiyat; max belirle (20); "available now" görünürlüğü |
| Ücret | Değişken hizmet ücreti %0–15; teklif/offer anında gösterilir ve o contract için sabitlenir |
| Rising Talent | Davet veya: 4,8★ + $250 / 12 ay + %100 profil + ID + çekim yöntemi → 30 Connects |

**Günlük dağılım**

| Kalem | Adet | Connects | $ |
| --- | --- | --- | --- |
| Boost'suz teklif | ~27 | ~270 (≈10/teklif) | ~$40 |
| Boost'lu Tier-1 teklif | ~6 | ~6 × (10 + 18) = ~170 | ~$25 |
| Toplam / gün | 33 | ~440 | ~$66 |
| 72 saat | 100 | ~1.320 | ~$200 |

**"Connects ucuz, cevap oranı pahalı."** Bir teklif ≈ 10 Connects = $1,50. %7 cevapla bir cevap ≈ $21; %3,2 contract olasılığıyla bir contract ≈ $47 Connects. İlk iş $49–129 + ilk review. Yani pahalı olan Connects değil, **cevap oranını düşüren teklif**tir: yavaş (>15 dk), genel, bütçe dışı veya eşleşmeyen teklif hem Connects yakar hem Uma nezdinde relevans puanını düşürür. Kural: hızlı ve eşleşmişe sınırsız harca; yavaş ve geneli gönderme.

**Karar ağacı (her ilan için ≤30 saniye)**

```text
İlan bildirimi
└─ Whitelist + müşteri filtresi geçti mi?  Hayır → atla
   └─ Evet. İlan yaşı?
      ├─ <5 dk  → HEMEN gönder, boost YOK (hız etkisi boost'tan büyük)
      ├─ 5–15 dk → gönder; boost YALNIZCA Tier-1 + sabit fiyat + <5 teklif + bütçe ≥$100 ise (bid 16)
      ├─ 15–60 dk → Tier-1 sabit fiyat: gönder + boost 16–20 (sabit fiyatta 2× etki)
      │             Tier-1 saatlik: gönder, boost yok
      │             Tier-2: <10 teklif ise gönder, boost yok; değilse atla
      └─ >60 dk → Tier-1 tam eşleşme + <10 teklif + ≥1 hire müşteri ise boost'suz gönder; diğer her şey atla
İstisna: ilanda "hired 1" veya "interviewing ≥3" görünüyorsa → atla (Connects iade edilmez)
Boost bid: teklif içgörüleri (Plus) mevcut bid aralığını gösterir → aralığın üst çeyreği, tavan 20
```

Ek C uygulanıyorsa bu ağacın boost dalları Ek C'deki "tek ödül boost'u + en fazla 2 koşullu boost" kuralıyla daraltılır; hız ve hacim dalları aynen kalır.

**Şimdi yap**
1. Freelancer Plus + 400 Connects (ilk satın alımda 50 bonus gelebilir) + Availability Badge (max 20/hafta).
2. Karar ağacını ekranın yanına yapıştır; boost'u yalnızca Tier-1 sabit fiyat + 15–60 dk penceresinde kullan.
3. Connects bakiyesi 150'nin altına inince 200 daha al (Blok D öncesi kontrol).

---

## 5) Teklif fabrikası

**Kurallar**
- İlk iki cümle liste katmanında görünür: 1. cümle müşterinin kendi sözcükleriyle problemi + net sonuç/süre; 2. cümle siteye/brief'e özel tek gözlem. Demo linki en erken 3. cümlede gelir (önizlemede URL yer israfıdır).
- Eleme sorularına **önce** ve tam cevap (Uma shortlist bunları okur); her soru 1–3 cümle.
- Ana şablon 150–190 kelime, kısa şablon ≤100 kelime. Her teklifte en az 2 işe özel satır (kopyala-yapıştır tespiti ve relevans için).
- Teklif tutarı ilan bütçesine eşit veya altında; sabit fiyatta milestone'lar Bölüm 6'daki gibi.
- "Profile highlights" ile iki demo portfolyo öğesi eklenir (Tier-1'de zorunlu).
- İletişim bilgisi yok; "Dear", "honored", "passionate" yok; imza yalnızca ad.
- Gönderilmemiş cevaplı thread yoktur: müşteri cevap vermeden mesaj gönderilemez → follow-up'lar yalnızca cevaplı thread'lerde.

**Trust stack (sıra sabit)**
1. Müşterinin sözcükleriyle problem → okuduğunu kanıtlar
2. Siteye/brief'e özel gözlem (1 satır) → uzmanlık
3. Eşleşen canlı demo linki → tıklanabilir kanıt
4. Lighthouse tek satır → doğrulanabilir sayı
5. Sabit fiyat + tarih (ET) + dahil olanlar → belirsizlik yok
6. 0 review dürüstlük satırı + intro fiyat → güven
7. Fonlanmış milestone / onaysız ödeme çıkmaz → risk transferi
8. Bir sonraki adımı başlatan tek soru → aksiyon

**T1 — WordPress fix / speed (Tier-1, İngilizce)**

```text
[CLIENT_PROBLEM_WORDS] — I can have this fixed within 24 hours of the milestone being funded, with a before/after check you can verify yourself. I looked at [SITE_URL] on my phone: [SPECIFIC_OBSERVATION].

What you get for $[PRICE]:
• Root-cause fix of [ISSUE] — not a plugin-on-top patch — tested on desktop and mobile
• A short before/after report: what was broken, what I changed, screenshots (and PageSpeed scores for speed jobs)
• A full backup before I touch anything; nothing goes live without your OK
• 7 days of free follow-up if the same issue comes back

Proof instead of reviews: I'm new on Upwork, so here is work you can click — https://djoguzhan1.github.io/web-dev-portfolio/ (hand-coded demo sites, 99–100 on Google Lighthouse for performance, accessibility, best practices and SEO).

Once the milestone is funded I'll send a 3-line access checklist (a temporary admin account works best) and start the same hour. I'm online until [TIME] pm ET today.

Which hosting provider are you on? That tells me whether caching is part of the fix.

Oğuzhan
```

**T2 — Yerel işletme landing page (Tier-1, İngilizce)**

```text
You need a [INDUSTRY] landing page that turns [Google Ads / local search] visitors into phone calls — one page, hand-coded, delivered in 48 hours at a fixed price. [SPECIFIC_OBSERVATION — e.g. "Your current page has no call button above the fold on mobile."] Open a finished example on your phone: https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/ — the sticky call button and the reviews block do the heavy lifting. For [BUSINESS_NAME]: same structure — one clear offer, tap-to-call, services, reviews, service areas, FAQ, contact form.

Fixed price $[PRICE], delivered in 48 hours:
• Hand-coded HTML/CSS, no page-builder bloat; my demos score 99–100 on Google Lighthouse (mobile)
• You send text, photos, phone number and service areas; I handle the rest
• Contact form, basic on-page SEO, Analytics / Ads tag if you use them
• Deployed to your hosting (or free hosting set up for you); 2 revision rounds; small fixes free for 7 days

I'm new on Upwork — intro pricing, and the demos stand in for reviews.

So I can start today: do you have a domain and hosting, and a logo plus 3–5 photos?

Oğuzhan
```

**T3 — Küçük işletme sitesi / yeniden tasarım, 1–3 sayfa (Tier-1, İngilizce)**

```text
Your [BUSINESS_TYPE] site needs [CLIENT_GOAL_WORDS] — I build exactly this kind of small business site: [N] pages, hand-coded, mobile first, delivered in [DAYS] days at a fixed price. [SPECIFIC_OBSERVATION about the current site or the brief.] Here is a finished example you can open now: https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/ (an emergency plumbing style demo; the HVAC one is on the same portfolio).

Scope I'd propose — fixed price $[PRICE]:
• Milestone 1 ($[M1]): home page live on a preview link within 24 hours; you approve before I continue
• Milestone 2 ($[M2]): remaining pages, contact form, mobile testing, basic SEO, files handed over or deployed to your hosting
• 2 revision rounds included; small fixes free for 7 days after delivery

Hand-coded HTML/CSS by default, or WordPress if you need to edit pages yourself — tell me which. My demos score 99–100 on Google Lighthouse (mobile); check any of them at pagespeed.web.dev. I'm new on Upwork, so intro pricing applies and the demos stand in for reviews.

Which pages do you need, and are logo, photos and text ready? I can start today.

Oğuzhan
```

**S4 — Sheets / Excel hızlı iş (Tier-2, kısa, İngilizce)**

```text
[CLIENT_TASK_WORDS] — I can deliver this in [2–24] hours for $[PRICE], with formulas that keep working when you add rows (no hard-coded ranges). [SPECIFIC_OBSERVATION — e.g. "From your description this is an XLOOKUP plus a monthly summary tab; I'd add a dropdown with data validation so new entries stay clean."]

Included: the finished file or sheet, a one-minute note on how it works, and one round of changes. I'm new on Upwork, so this is intro pricing with same-day delivery. Share the file (or a copy with dummy data) and I'll start right away.

Oğuzhan
```

**S5 — Küçük web görevi: kurulum / ayar / HTML-CSS düzeltme / dönüştürme (Tier-2, kısa, İngilizce)**

```text
[CLIENT_TASK_WORDS] — a quick one; I can do it within [2–6] hours of the milestone being funded, for $[PRICE]. [SPECIFIC_OBSERVATION].

You get: the change done and tested on desktop and mobile, a backup taken first (for WordPress), and a before/after screenshot. I'm new on Upwork; here is my hand-coded work to check — https://djoguzhan1.github.io/web-dev-portfolio/ (99–100 on Google Lighthouse). Send the URL and I'll start now.

Oğuzhan
```

**Özelleştirme kontrol listesi (≤90 saniye)**
1. İlandan 3–6 kelimeyi kopyala → `[CLIENT_PROBLEM_WORDS]` (müşterinin kendi ifadesi).
2. URL varsa telefonda 20 saniye aç → 1 somut gözlem (`[SPECIFIC_OBSERVATION]`); URL yoksa brief'teki detaya referans.
3. Şablonu tier'a göre seç; `[PRICE]` Bölüm 6 tablosundan, ilan bütçesine eşit/altı; `[DATE]/[TIME]` ET olarak.
4. Eleme sorularını önce ve tam cevapla.
5. Profile highlights: 2 demo öğesi (Tier-1) / Sheets örneği (S4, varsa).
6. Sabit fiyat → milestone(lar) Bölüm 6; saatlik → $20/sa + "about 3 hours, capped at 4".
7. Boost kararı: Bölüm 4 ağacı.
8. 10 saniyelik okuma: "Dear" yok, iletişim bilgisi yok, link doğru demo, dil İngilizce.
9. Takip tablosuna yaz (ilan yaşı, tier, Connects, boost).

**Follow-up (yalnızca müşterinin cevap verdiği thread'lerde, İngilizce)**

```text
24h:
Quick follow-up on [JOB_TITLE]: I had another look at [SITE / the brief] and [ONE_NEW_FINDING]. If you'd like to go ahead, the milestone would be "[SCOPE_LINE] — $[PRICE], delivered by [DAY, TIME ET]". If you've gone another way, no problem — tell me and I'll close the thread.

48h:
Last note from me on this one: the intro price ($[PRICE]) stands this week. If timing is the issue, we can start with the $[19/29] [audit report / first fix] so you have something in hand today and decide on the rest afterwards. Either way, thanks for your time.
```

**Müşteri cevap verdi → offer'a köprü mesajı (İngilizce)**

```text
Thanks, [NAME]. To get this done today: 1) [ONE_CONCRETE_QUESTION_OR_FINDING]. 2) I'd set the milestone as "[SCOPE_LINE] — $[PRICE], delivered by [DAY, TIME ET]". If that works, click Hire on my proposal and fund the milestone — I start the minute it's funded, and you release payment only when you've approved the result.
```

**3 pre-offer varyantı (İngilizce)**

```text
Variant A — standart, tek milestone:
Here is the exact milestone text so you can paste it into the offer: "[SCOPE_LINE: e.g. Fix the broken mobile menu and the contact form on example.com; backup first; before/after screenshots] — $[PRICE], delivered by [DAY, TIME ET]." Anything outside that line I'll quote separately before doing it.

Variant B — küçük başla (kararsız müşteri / Gün 3):
If you'd rather start small: Milestone 1 — $[19/29] — [a PageSpeed + mobile audit with a 5-point fix list / the first fix] within 2 hours, so you see how I work first. Milestone 2 — $[REST] — [MAIN_DELIVERABLE] by [DAY]. You can stop after milestone 1 with no obligation.

Variant C — "no reviews" itirazı:
Fair question — I'm new on Upwork, so there are no reviews on my profile yet. Three things protect you: the milestone is funded to Upwork, not paid to me, and you release it only when you approve the work; the demo sites are live now and you can run them through pagespeed.web.dev yourself; and we can make the first milestone small. If the first delivery isn't what you expected, don't approve it.
```

**Şimdi yap**
1. 5 şablonu + köprü mesajı + 3 varyantı metin genişleticiye kısayolla kaydet (`;t1`, `;t2`, `;t3`, `;s4`, `;s5`, `;bridge`, `;va`, `;vb`, `;vc`).
2. İlk 3 teklifi bilinçli yavaş yaz (5 dk), kontrol listesini uygula; sonra 3 dk hedefi.
3. Her cevaplı thread'e takvimde 24h ve 48h hatırlatıcı koy.

---

## 6) Fiyat & kapanış

**Intro fiyat tablosu (72 saat, Upwork; müşteri bütçesine eşit/altı olacak şekilde uygulanır)**

| Hizmet | Intro (sprint) | Normal | Teslim | Milestone yapısı |
| --- | --- | --- | --- | --- |
| WordPress bug fix (1 kök neden) | **$49** | $79 | 24 saat | Tek milestone $49, fonlanınca başla |
| WordPress speed optimization | **$89** (Varsayım) | $149 | 48 saat | M1 $29 audit + plan (2 saat) · M2 $60 uygulama + rapor |
| Tek sayfa landing (el kodu) | **$129** | $199 | 48 saat | M1 $49 tasarım taslağı önizleme (24 saat) · M2 $80 final + dosyalar |
| Küçük işletme sitesi, 3 sayfa | **$249** | $399 | 4 gün | M1 $99 ana sayfa önizleme · M2 $150 diğer sayfalar + teslim |
| Excel / Sheets görev | **$35** | $59 | 24 saat | Tek milestone |
| Sheets dashboard / şablon | **$79** | $129 | 48 saat | M1 $29 yapı · M2 $50 formüller + teslim |
| Küçük web görevi (kurulum / ayar / tweak) | **$25** | $45 | Aynı gün | Tek milestone |
| Hız/mobil denetim raporu (kapanış ürünü) | **$19** | $39 | 2 saat | Tek milestone → ana işe köprü |
| Saatlik işler | **$20/sa** | $30/sa | – | Contract'ta saat tavanı; tracker |

**Fiyat kuralları**
- Bütçe bantta ise bütçeye eşit veya %10 altı teklif ver (bütçe dışı = alta sıralanır).
- Bütçe intro fiyatın altındaysa fiyatı değil scope'u küçült; asla $15 altı.
- İlk milestone her zaman küçük ($19–49): 0 review'lı hesapta müşterinin riski düşer, kapanış oranı yükselir.
- Değişken hizmet ücreti teklif ekranında görünür; tabloda yazan fiyatlar müşterinin ödediği fiyattır, ücreti içselleştir (ücret için fiyat yükseltme yok).
- "Şimdi başlayabilir misin?" → "Yes — the minute the milestone is funded."

**Milestone örnekleri (offer'a yapıştırılacak İngilizce satırlar)**

```text
WordPress fix:   "Fix the mobile menu and the contact form on example.com; full backup first; before/after screenshots — $49, by Tue 5 pm ET"
Speed, M1:       "PageSpeed + Core Web Vitals audit of example.com with a prioritised fix list — $29, within 2 hours"
Speed, M2:       "Implement the fix list (caching, image compression, script deferral); target mobile Performance ≥ 85 — $60, by Wed 5 pm ET"
Landing, M1:     "Home page design for [Business] live on a preview link (hero, services, call button) — $49, within 24 hours"
Landing, M2:     "Final one-page site: reviews, service areas, FAQ, contact form, SEO basics, deployed to hosting — $80, within 48 hours of M1 approval"
Sheets:          "Monthly summary tab with XLOOKUP, dropdowns and conditional formatting on the shared sheet; one round of changes — $35, by tomorrow noon ET"
```

**5 dakikalık interview script (İngilizce, Upwork Messages/Zoom)**

```text
0:00–0:30  Open
"Thanks for the time, [NAME]. I've read the post and looked at [SITE / the file]. In five minutes I'd like to confirm three things and give you a fixed price and a delivery time. Sound good?"

0:30–2:00  Diagnose (three questions)
1. "What's the one outcome that makes this a success for you — [more calls / the error gone / the sheet just working]?"
2. "Who has the [WordPress admin and hosting login / logo, photos and text / the source file]? A temporary admin account for me is the cleanest."
3. "Is there a date or an event this has to be ready for?"

2:00–3:30  Scope, price, date
"Here's what I'd do: [THREE BULLETS]. Fixed price $[X], delivered by [DAY, TIME ET]. That includes [backup / before-after report / 2 revision rounds / 7 days of small fixes]. Anything outside those three points I'll quote in one line before doing it, so there are no surprises on the invoice."

3:30–4:30  Process and protection
"You'd hire through my proposal and fund the milestone. The money sits with Upwork, not with me, and you release it only when you've approved the result. [I take a full backup before touching anything / You'll see a preview link within 24 hours.]"

4:30–5:00  Close
"If that works, send the offer with the milestone '[SCOPE_LINE] — $[X]' and I start as soon as it's funded. I'm online until [TIME] pm ET today."

Objections
"No reviews yet?" → "Right — I'm new on Upwork. Two things you can check: the demo sites (run them through pagespeed.web.dev), and the funded milestone protects you. If you'd like, we start with a $[19/29] first milestone."
"Others quoted less." → "The difference is what's included: root-cause fix, backup, before/after report, 7 days of follow-up. If budget is tight I'd rather reduce scope — one fix instead of three — than quality."
"Can you start right now?" → "Yes. The minute the milestone is funded."
Hourly job → "$20/hr, about [N] hours, capped at [N+1] in the contract, tracked with the Upwork tracker."
```

**Şimdi yap**
1. Fiyat tablosunu ve milestone satırlarını şablon dosyasına ekle; her teklifte tablodan seç, ezberden fiyat verme.
2. Interview script'ini yazdır; ilk interview'dan önce 2 kez sesli prova.
3. Interview biterken milestone metnini yazılı olarak da thread'e yapıştır (Varyant A).

---

## 7) Kanıt paketi

**Paket sırası (teklifte ve interview'da aynı sıra)**

| Sıra | Öğe | Ne zaman |
| --- | --- | --- |
| 1 | Eşleşen demo linki: HVAC → HVAC / ev hizmetleri / genel yerel işletme; plumbing → acil servis, tesisat, çilingir, elektrik; diğer → hub | Her Tier-1 teklif, 1. paragraf |
| 2 | Hub linki (iki demo + Lighthouse halkaları + fiyatlar) | T1, S5 ve interview |
| 3 | Lighthouse tek satır (aşağıda) | Her Tier-1 teklif |
| 4 | Doğrulama cümlesi: "check any of them at pagespeed.web.dev" | Fiyat/güven itirazında |
| 5 | GitHub kod linki (`github.com/djoguzhan1/web-dev-portfolio`) | Yalnızca teknik müşteri veya "kodu görebilir miyim" |
| 6 | Profile highlights: 2 demo portfolyo öğesi | Tier-1'de zorunlu |
| 7 | Sheets örnek dosyası (görüntüleme linki) | S4 — Varsayım: Gün 0'da 45 dk'da yapılır |
| 8 | "What you'll receive" 3–4 madde listesi | Her teklif |

**Tek satır Lighthouse kanıtı (İngilizce)**

```text
Google Lighthouse, mobile: portfolio hub 100/100/100/100, CoolAir HVAC style demo 99–100 across all four categories, emergency plumbing style demo 100/100/100/100 — hand-coded, under 250 KB per page. Verify any of them at pagespeed.web.dev.
```

Not: PageSpeed Insights lab skoru cihaz/ağ koşuluna göre 1–3 puan oynayabilir; "99–100" ifadesi bu yüzden aralık olarak kalır. Sayılar bu depodaki Lighthouse 12.8 ölçümleridir (`web-dev-portfolio/` hub ve demolar).

**Şimdi yap**
1. Portfolyo öğelerinin başlıklarına iş anahtar kelimelerini koy ("Landing Page", "WordPress", "Lighthouse 100").
2. Telefonda 3 linki yer imine al; interview'da ekran paylaşımı için hub'ı açık tut.
3. Sheets örnek dosyasını (görüntüleme linki, örnek veri) 45 dk'da yap ve S4'e ekle.

---

## 8) 72H KPI

**Hedefler (günlük ve kümülatif)**

| Metrik | Gün 1 | Gün 2 (küm.) | Gün 3 (küm.) | Eşik altı ise → aksiyon |
| --- | --- | --- | --- | --- |
| Teklif | 35 | 68 | 100 | 20:00 GMT+3'te hedefin %60'ının altında → Tier-2 bandını $20–200'e genişlet, Q12'yi ikinci sekmede açık tut, Blok E'ye +5 |
| <5 dk gönderim payı | ≥%55 | ≥%60 | ≥%60 | <%50 → bildirim aracı/ses kontrolü; şablon kısayollarını kontrol; ilan başına süre 3 dk hedefi |
| Görüntülenme | ≥%40 | ≥%40 | ≥%40 | 20 teklif sonra <%30 → liste katmanı: Opener B, ilk 2 cümle varyantı, fotoğraf/ücret/ID durumunu doğrula |
| Cevap | ≥2 | ≥5 | ≥7 | 40 teklif sonra <%4 → gövde: %100 teklife özel gözlem, bant tabanı fiyat, yalnızca <5 teklifli ilan, boost payı %30 |
| Interview | ≥1 | ≥2 | ≥3 | Cevap var interview yok → ilk cevapta köprü mesajı + 2 ET zaman aralığı |
| Offer | 0–1 | ≥1 | ≥2 | 3 interview sonra 0 offer → interview içinde Varyant B ($19–29 ilk milestone); script'i 2:00–3:30 bölümüne göre kısalt |
| Fonlanmış contract | – | 0–1 | **≥1** | Gün 3 12:00 GMT+3'te 0 → her sıcak thread'e Varyant B + 48h mesajı; Blok D'de yalnızca Tier-1 <5 dk + boost 20 |
| Connects | ~450 | ~890 | ~1.320 | Bakiye <150 → 200 al (Blok D öncesi) |

**Ayar mantığı (yalnızca aksiyon)**
- Katman teşhisi sabittir: görüntülenme düşük = liste katmanı (başlık, fotoğraf, ücret, ilk 2 cümle); görüntülenme iyi, cevap düşük = gövde katmanı (gözlem satırı, fiyat, eşleşme); cevap iyi, offer düşük = kapanış katmanı (köprü mesajı, küçük milestone, ET zaman önerisi).
- Her ayar 24 saatlik veri üzerinden yapılır; aynı gün iki değişken birden değiştirilmez.
- Contract geldiği an: teslimatı planlanan sürenin %70'inde bitirmeyi hedefle, teslimde review isteme cümlesi: "If you're happy with the result, a short review here helps me a lot as a new freelancer — and I'm around for the 7 days of small fixes."
- Contract sonrası teklif göndermeye devam et (ikinci iş, JSS için ≥2 contract gerekir).

**Şimdi yap**
1. Takip tablosunun özet sekmesine bu 8 metriği ve eşiklerini gir; her gün 23:30 GMT+3'te 5 dakikalık kontrol.
2. Eşik altı metrik için tabloda yazan tek aksiyonu uygula; başka değişiklik yapma.
3. İlk contract'ta teslimat + review isteme cümlesini takvime yaz.

---

## Ek A — Takip tablosu sütunları

`Tarih · Saat (GMT+3) · İlan URL · Tier · İş tipi · İlan yaşı (dk) · Teklif sayısı (ilanda) · Bütçe · Verilen fiyat · Connects · Boost (bid) · Şablon · Gözlem satırı yazıldı (E/H) · Eleme sorusu (E/H) · Görüntülendi · Cevap (saat) · Interview · Offer · Contract · Not`

## Ek B — Gün 0 kontrol listesi (90 dk + 45 dk opsiyonel)

1. Profil: Başlık A, Opener A, kanıt paragrafı, $20/sa, fotoğraf, 20 skill, %100 tamamlanma, kimlik doğrulama başlatıldı, billing yöntemi.
2. Portfolyo 3 öğe (masaüstü + mobil görsel + canlı link).
3. Freelancer Plus, 400 Connects, Availability Badge (max 20/hafta).
4. 12 kayıtlı arama + anlık bildirim aracı (Varsayım: Zenfl / Integrono / OutBid / UpAlerts / Upwatcher'dan biri; ~1 dk gecikme) + sessiz saat 01:00–09:00.
5. Şablon kısayolları, fiyat tablosu, interview script'i, takip tablosu.
6. Opsiyonel 45 dk: Sheets örnek dashboard (görüntüleme linki) → S4 ve portfolyo.
7. Project Catalog 3 liste (onay 72 saati aşabilir; gönder ve bırak).

## Ek C — Maliyet optimizasyonu (aynı plan, aynı olasılık, düşük nakit)

İlke: Plan (100 teklif, 5 dk SLA, bloklar, şablonlar, fiyatlar, KPI) değişmez. Değişen şey **harcama katmanı**: Connects'i olasılığa katkısı en yüksek yere koy, katkısı düşük yerlerden çek, bedava girişleri sıraya al, satın almayı kademeli yap.

**Neden aynı olasılık?** λ = Σ p_i (beklenen contract sayısı) korunur:

| Değişiklik | λ etkisi |
| --- | --- |
| 15–60 dk boost'lu dilim (15 teklif, ~%2) boost'suz kalır (~%1,3) | −0,10 |
| >60 dk ilanlara teklif kesilir (~5 teklif, ~%0,7) → yerine taze ilan (~%3,5) | +0,14 |
| "Yerleşik müşteri" ağırlığı (≥1 hire + harcama) tüm tekliflerde p'yi göreli +%10–15 yükseltir | +0,30–0,45 |
| **Net** | λ: 3,2 → ≥3,3 → P(≥1) ≥ %96 |

**Marjinal Connect verimi (kararın matematiği)**

| Harcama | Connects | p katkısı | pp / Connect |
| --- | --- | --- | --- |
| Taze (<5 dk) teklif | 10 | ~4,0 pp | **0,40** |
| 5–15 dk teklif | 10 | ~2,0 pp | 0,20 |
| Boost (15–60 dk ilan, +~1 pp) | 18 | ~1,0 pp | 0,06 |
| >60 dk teklif | 10 | ~0,7 pp | 0,07 |

Sonuç: 18 Connects'lik bir boost yerine ~2 taze teklif, olasılığa 6–7 kat fazla katkı yapar. Boost bütçesi neredeyse tamamen taze teklife döner.

**Revize edilenler**

| # | Plan maddesi | Eski | Yeni | Tasarruf |
| --- | --- | --- | --- | --- |
| R1 | Boost (Bölüm 4) | ≤20 boost × 16–20 | **1 ödül boost'u** (ilk boost ücretlenirse Upwork 10 Connects verir; bid ≤12, net ≈2) + en fazla 2 koşullu boost (skor 7 + Plus içgörüsünde ilk-4 eşiği ≤10) | ~320 Connects |
| R2 | Teklif başına Connects | ~10 ort., sınır yok | İlanda yazan Connects **≤8 tercih, >12 atla** (skor ≥6 hariç) | ~200 Connects |
| R3 | >60 dk ilan (Bölüm 4 ağacı) | Tier-1 tam eşleşme ise gönder | **Gönderme** (davet hariç) | ~50 Connects |
| R4 | Satın alma | Gün 0'da 400 + gerektiğinde | **Kademeli**: Gün 0 Plus (100 + 50 bonus, Varsayım: uygunluk) + 150 satın; her gece bakiye <120 ise 150 al; ilk fonlanmış contract'tan sonra alım durur, kalan bakiyeyle 10 teklif/gün "sürdürme modu" | Beklenen nakit düşer (contract Gün 2'de gelirse Gün 3 alımı yok) |
| R5 | Availability Badge | max 20/hafta | max 10/hafta (davet = 0 Connects kanalı, kapatma) | ~10 Connects |
| R6 | Müşteri filtresi (Bölüm 2) | Payment verified zorunlu, ≥1 hire tercih | **Yerleşik müşteri +2 puan** (hem hire olasılığı yüksek hem interview'a dönüşürse Upwork teklif Connects'ini iade edip üstüne ekleyebilir) | Dolaylı: başarıya giden yolun kendi maliyetini geri ödemesi |
| R7 | Gün 0 sırası (Ek B) | Önce satın al | **Önce bedava**: onboarding görevleri (profil kurulumu, kimlik doğrulama, nasıl-yapılır videoları) Connects verir → bakiyeyi gör → sonra Plus/alım | ~20 Connects (Varsayım) |

**Eklenenler**

| # | Ekleme | Kural |
| --- | --- | --- |
| E1 | **EV skoru** (her ilan, 20 sn) | <5 dk +2 · 5–15 dk +1 · Tier-1 +1 · yerleşik müşteri (≥1 hire ve harcama) +2 · <5 teklif +1 · Connects ≤8 +1 → **≥4 gönder**, 3 = yalnızca Tier-1, <3 atla. Hacim koruması: 20:00 GMT+3'te günlük hedefin %60'ı altındaysa eşik 3'e iner (plan hedefi tasarruftan önce gelir) |
| E2 | **0-Connects kanalları** | Davetler (Badge + başlık anahtar kelimeleri + davete ≤5 dk yanıt) · Project Catalog (Gün 0'da gönder; onaylanırsa sipariş 0 Connects) · cevaplı thread'lerde 24h/48h follow-up (mesaj 0 Connects — en ucuz dönüşüm kolu) · Uma shortlist (profil uygunluğu, bedava) |
| E3 | **İade takibi** | Takip tablosuna "İade" sütunu: müşteri ilanı hire'sız kapatırsa Connects otomatik iade; yerleşik müşteriyle interview'da iade + ödül gelebilir. Gerçekleşen maliyet nominalin ~%10–20 altı (Varsayım) |
| E4 | **18 Connects testi** | ≥3 teklif ve ≥54 Connects harcamada Upwork bazı hesaplara 18 Connects verir (ayda 2 kez, test) — otomatik; Gün 1'de zaten tetiklenir |
| E5 | **Plus kararı** | Plus $19,99 = 100 Connects ($15 değer) + 50 bonus (uygunsa) + anlık bildirim + bid içgörüsü → fiilen ≤$5 prim; **kal**, ama yenileme öncesi iptal hatırlatıcısı koy. Bonus için uygun değilsen ve ücretsiz bildirim aracı ≤2 dk gecikmeyle çalışıyorsa Plus'sız da aynı maliyet |
| E6 | **Seviye 2 (veriye bağlı)** | Gün 1 sonu: cevap ≥%8 **ve** görüntülenme ≥%45 ise filtreli p ≈ %4 doğrulanmış sayılır → 72 saat hedefi 75 teklife iner (P aynı: 1 − 0,96^75 ≈ %95). Değilse 100'de kal |

**Bütçe: önce / sonra**

| Kalem | Plan (nominal) | Ek C Seviye 1 (n=100) | Ek C Seviye 2 (n=75) |
| --- | --- | --- | --- |
| Teklif Connects | 100 × 10 = 1.000 | 100 × 8 = 800 | 75 × 8 = 600 |
| Boost | 20 × 18 = 360 | 1 ödül + ≤2 koşullu ≈ 36 (net ~26) | ≈ 36 |
| Badge | 20 | 10 | 10 |
| **Nominal ihtiyaç** | ~1.320–1.380 | **~850** | **~650** |
| Bedava giriş | Plus 100 | Plus 100 + bonus 50 + onboarding ~20 = 170 | 170 |
| Satın alınacak | ~1.220 (≈$183) | ~680 (≈$102) | ~480 (≈$72) |
| Plus | $19,99 | $19,99 | $19,99 |
| **Nakit** | **≈ $203** | **≈ $122 (−40%)** | **≈ $92 (−55%)** |
| İadeler sonrası gerçekleşen (Varsayım) | – | ≈ $105 | ≈ $78 |
| Kademeli alım + erken contract | – | beklenen ≈ $90–110 | ≈ $70–85 |

**Değişmeyenler:** 100 teklif hedefi (Seviye 2 yalnızca Gün 1 verisiyle açılır), 5 dk SLA, blok saatleri, şablonlar, trust stack, fiyat tablosu, milestone yapısı, interview script'i, KPI eşikleri, Gün 1 sonu katman teşhisi.

**Şimdi yap**
1. Ek B'nin sırasını değiştir: önce onboarding görevleri → bakiye → Plus → 150 Connects; Badge max 10.
2. Karar ağacına EV skorunu ekle; boost'u "1 ödül + ≤2 koşullu" ile sınırla; >60 dk ilanları kapat.
3. Takip tablosuna "Skor", "İade" sütunlarını ekle; Gün 1 sonunda E6 kontrolünü yap.

---

## Ek D — Düşük ön ödeme (aynı olasılık, max kalite, nakit ≈ $45–70)

**Sorun.** Ek C toplam sprint maliyetini düşürür ama yine de Gün 0'da ~$100+ Connects yüklemesi gibi hissedilir. Upwork'te asıl risk "iş gelmeden para çıkması"dır; çözüm **şelale harcama** + **daha az ama daha iyi teklif** (kalite ↑, düşük EV teklifleri ↓).

**Temel fikir.** Olasılığı hacimle değil **seçilmiş hacimle** koru: 72 saatte **70–75 teklif**, ortalama **p ≈ %4,2–4,5** (yalnızca skor ≥5 ilanlar + <5 dk ağırlığı) → λ ≈ 3,1–3,4 → P(≥1) ≈ **%95–97** (aynı band). Gönderilen her teklif hâlâ tam özelleştirme, trust stack ve Tier-1'de demo linki — düşen şey "ucuz/uyumsuz ilana şişirilmiş hacim"dir.

| Katman | Ek C | Ek D |
| --- | --- | --- |
| Boost | ≤3 | **0** (hız zaten kazanıyor; boost = düşük marj) |
| Availability Badge (72 sa) | 10 Connects | **0** (davet kanalı; ilk işten sonra aç) |
| Freelancer Plus | Gün 0 | **Gün 2'ye ertele** (ücretsiz bildirim aracı ≤2 dk ise); görüntülenme <%30 ise Plus al, bid içgörüsü için |
| EV eşiği (varsayılan) | ≥4 | **≥5** (20:00 hacim telafisi: ≥4) |
| Connects/ilan | ≤8, >12 atla | **≤6 tercih, 7–8 skor≥6, >8 atla** |
| İlan yaşı | >60 dk yok | **>45 dk yok** (Tier-1 tam eşleşme bile) |
| Teklif hedefi | 75–100 | **70–75** (λ ile telafi) |

**Bedava Connects yığını (Gün 0, sıra önemli)**

1. Onboarding görevleri (profil, kimlik, videolar) — Varsayım: ~10–20 Connects.
2. Basic aylık 10 Connects (Plus yoksa).
3. **Minimum satın alma:** 10 Connects = **$1,50** → uygun hesaplarda **+50 bonus** (Upwork: ilk bundle veya Plus; bonus her hesapta görünmeyebilir — Varsayım: görünür).
4. Gün 1 sonu: ≥3 teklif + ≥54 harcanmış Connects → test ödülü **+18** (ayda 2 kez, herkese değil).

Gün 0 sonu bakiye (Varsayım): ~70–90 Connects, nakit **$1,50**.

**Şelale — ilk müşteri cevabı / interview öncesi nakit tavanı ≈ $35**

| Kapı | Koşul | Nakit | Ne yapılır |
| --- | --- | --- | --- |
| K0 | Profil %100 + kimlik başlatıldı | $0 | Teklif yok |
| K1 | K0 tamam | **$1,50** | Min bundle → bonus; yalnızca skor ≥5 |
| K2 | 12 teklif gönderildi | $0 | Metrik: görüntülenme oranı |
| K3 | Görüntülenme ≥%25 **veya** ≥1 cevap | **+$15** (~100 Connects) | Sprint devam |
| K3b | Görüntülenme <%25 ve 0 cevap | **+$0** | Opener B + fotoğraf/ücret; para değil profil düzelt |
| K4 | ≥1 interview veya ≥2 cevap | **+$15** (tavan) | Kapanış sprinti; Plus (gerekirse) |
| **Tavan** | İlk fonlanmış contract öncesi | **≈ $31,50** | K3b tetiklenmediyse |

Contract Gün 2–3'te gelirse toplam nakit genelde **$32–48** + iadeler; kötü profil senaryosunda (K3b) para dökülmez, önce düzeltme.

**λ hesabı (Ek D)**

| Dilim | Adet | p | λ katkı |
| --- | --- | --- | --- |
| Skor ≥5, <5 dk | ~42 | %4,8 | 2,02 |
| Skor ≥5, 5–15 dk | ~18 | %3,0 | 0,54 |
| Skor 5, 15–45 dk (Tier-1) | ~10 | %2,0 | 0,20 |
| Davet (0 Connects) | ~2–4 | %12 | 0,24–0,48 |
| **Toplam** | **~72–74** | **~%4,2 ort.** | **~3,0–3,3** |

P(≥1) ≈ **%95–97**. Davet sayısı düşükse teklif hedefini 78'e çıkar (yalnızca skor ≥5); nakit K4 ile +$15.

**Kalite neden max kalır (neyi kesmiyoruz)**

- Profil yaması, kanıt paragrafı, portfolyo 3 öğe, kimlik, $20/sa.
- Her gönderilen teklif: 2 işe özel satır, eleme soruları tam, şablon gövdesi aynı, Tier-1'de demo + Lighthouse.
- <5 dk SLA **skor ≥5** ilanlarda değişmez.
- Fiyat/milestone/interview script aynı.

**Kaliteyi düşüren şeyleri bilinçli kesiyoruz:** genel/ucuz/yaşlı ilan, boost ile "görünürlük satın alma", Badge ile haftalık vergi, Plus'ı ihtiyaç yokken Gün 0'da ödeme.

**Bütçe karşılaştırma (72 saat, model)**

| | Orijinal | Ek C | Ek D |
| --- | --- | --- | --- |
| Toplam nakit (nominal) | ≈ $203 | ≈ $92–122 | **≈ $45–70** |
| İlk cevap öncesi nakit tavanı | ≈ $180+ | ≈ $60–90 | **≈ $32–35** |
| Teklif adedi | 100 | 75–100 | 70–75 |
| P(≥1) model | %96 | %95–96 | %95–97 |
| Ortalama teklif kalitesi | iyi | iyi | **daha iyi** (seçilmiş alt küme) |

**Ek D'de revize / eklenen maddeler (Ek C üzerine)**

| | Revize |
| --- | --- |
| Bölüm 4 | Boost tamamen kapalı; Badge 72 saat kapalı |
| Bölüm 2 EV | Varsayılan eşik **5**; yerleşik müşteri +2 aynı |
| Ek B sırası | Onboarding → Basic 10 → **$1,50 min alım** → teklif; Plus **ertele** |
| Takip tablosu | **"Kapı"** sütunu (K0–K4), **"Ön ödeme küm."** ($) |
| KPI | Gün 1: 22 teklif (skor ≥5), görüntülenme ≥%25; değilse K3b profil sprinti, Connects alımı dur |

**Dürüst taban.** Upwork'te **sıfır nakit** ile 72 saatte %95 mümkün değil (teklif = Connects). Makul taban: **~$30–50 nakit** + bedava yığın + disiplin. Bunun altı ya hacmi ya p'yi düşürür; %95+ ile uyumlu değil.

**Şimdi yap**
1. Ek D şelalesini takip tablosuna yaz; K1 = $1,50 min alım, K3/K4 koşullarını hatırlatıcıya koy.
2. Bildirim aracını Gün 0'da kur (Plus'sız); 2 dk test et — çalışıyorsa Plus'ı Gün 2'ye bırak.
3. İlk 12 tekliften sonra görüntülenme hesapla: <%25 ise para ekleme, Bölüm 1 Opener B'ye geç.

---

## Ek E — Nihai düşük maliyet modu (v2): seçici saldırı + teşhis-önce teklif

Öncelik: Ek E, Ek C ve Ek D ile çakıştığı yerde **geçerli olan** katmandır. Ek D'nin nakit şelalesi (K0–K4) ve bedava Connects yığını aynen kalır; Ek C'nin EV skoru ve Ek D'nin "skor ≥5" eşiği yerine aşağıdaki **A/B/C skor kartı** geçer. Bölüm 0–8'in şablonları, fiyatları, blokları, SLA'sı ve KPI mantığı değişmez.

**Tez.** Olasılık teklif sayısına değil λ = Σ p_i toplamına bağlıdır. En ucuz olasılık Connects'le değil **dakikayla** satın alınır: doğru ilanı seçmek (p'yi 2× yükseltir, 0 Connects) ve müşterinin *kendi sitesi* hakkında ölçülmüş bir teşhisle açmak (p'yi bir kademe daha yükseltir, 0 Connects). Bu ikisi n'i 100'den ~57'ye indirir; Connects ihtiyacı ~1.320'den ~390'a düşer; P(≥1) aynı bantta kalır.

**Marjinal verim (kararın matematiği)**

| Kaldıraç | Maliyet | p etkisi (Varsayım) | Verim |
| --- | --- | --- | --- |
| A-sınıf ilan seçimi (skor kartı) | 0 Connects, 30 sn | ortalama p %3,2 → %5,5 | sınırsız |
| Teşhis-önce açılış (PSI sayısı + görünür sorun) | 0 Connects, 3–4 dk | A-sınıfta +1–2 puan | sınırsız |
| Ek taze teklif (<5 dk) | ~7 Connects | +4–5,5 puan | 0,6–0,8 pp/Connect |
| Boost | 18 Connects | +~1 puan | 0,06 pp/Connect |
| Availability Badge (72 sa) | ~10 Connects | 0 review'lı profilde davet nadir | düşük |

**Skor kartı (her ilan, ≤30 sn, ilan sayfasındaki alanlardan)**

Kapılar — hepsi geçmeli, biri kalırsa gönderme:

| Kapı | Koşul |
| --- | --- |
| G1 | Tier-1 veya Tier-2 whitelist'te; blacklist yok |
| G2 | Payment verified |
| G3 | İlan yaşı ≤15 dk (Tier-1 tam eşleşme ve <5 teklif ise ≤45 dk) |
| G4 | Proposals <10 |
| G5 | Invites sent = 0 ve Interviewing = 0 (müşterinin elinde aday yok) |
| G6 | Bütçe ≥ taban ve intro fiyat ≤ ilan bütçesi |
| G7 | İlanda yazan Connects ≤8 (skor ≥12 ise ≤10) |
| G8 | Scope tek cümlede yazılabiliyor |

Puanlar:

| Puan | Sinyal | Neden |
| --- | --- | --- |
| +3 | İlan yaşı <5 dk | Hız etkisi (hire ×4) |
| +2 | Proposals "Less than 5" | İlk sayfada, boost'suz görünürsün |
| +2 | Müşteri ≥1 hire **ve** hire rate ≥%50 | İlanların ~yarısı hiç hire'a dönmez; bu müşteri döner |
| +2 | İlanda site URL'si var | Teşhis-önce açılış yapılabilir (en güçlü ikna kolu) |
| +2 | "Last viewed by client" ≤1 saat | Müşteri şu an teklif okuyor → aynı gün karar |
| +1 | Total spent ≥$500 | Ödeme alışkanlığı |
| +1 | Müşteri US/UK/CA/AU | Blok D/E'de canlı kapanış |
| +1 | Eleme sorusu var | Bot teklif azalır; Uma cevapları okur |
| +1 | urgent / asap / today / this week | 72 saat içinde hire |
| +1 | Sabit fiyat | Fonlanmış milestone, hızlı kapanış |
| +1 | Connects ≤6 | Maliyet |
| −2 | Expert seviye | 0 review'lı profil elenir |
| −2 | 10+ ilan ve hire rate <%30 | Toplayıcı müşteri |
| −1 | long-term / ongoing / team / full-time | 72 saatte kapanmaz |

Sınıflar ve p (Varsayım): **A ≥10 → p ≈ %5,5** · **B 6–9 → p ≈ %3,5** · **C ≤5 → gönderme.** Hacim koruması: 20:00 GMT+3'te günlük kotanın %60'ı dolmadıysa o gece B eşiği 5'e iner (hedef tasarruftan önce gelir).

**λ bütçesi ve günlük kota**

| Dilim | Adet (72 sa) | p | λ | Connects (ort.) |
| --- | --- | --- | --- | --- |
| A-sınıf | 45 (15/gün) | %5,5 | 2,48 | 45 × 7 = 315 |
| B-sınıf | 12 (4/gün) | %3,5 | 0,42 | 12 × 6 = 72 |
| Davet (0 Connects; Badge kapalı, Varsayım: 1–2) | 1–2 | %12 | 0,12–0,24 | 0 |
| **Toplam** | **~57–59** | **~%5,2** | **~3,0–3,1** | **~390** |

P(≥1) = 1 − e^−λ ≈ **%95–96** (Bölüm 0 ile aynı bant). Blok dağılımı (19/gün): A 2 · B 4 · C 1 · D 8 · E 4. Teklif başına süre: A-sınıf 6–8 dk (teşhis + ekran görüntüsü), B-sınıf 3 dk → günde ~2 saat yazım; kalan zaman izleme ve kapanış.

**Uyarlanır hacim (para yalnızca veri isterse çıkar) — Gün 1 sonu, ~19 teklif**

| Gün 1 sonucu | Gün 2–3 günlük kota | Ek nakit | Not |
| --- | --- | --- | --- |
| ≥3 cevap (≥%15) | 16 | −$5 | p doğrulandı; A-sınıfa daralt |
| 2 cevap (~%10) | 19 | $0 | Plan |
| 1 cevap (~%5) | 24 | +$10 | B eşiği 5; teşhis kalitesini denetle (her A teklifinde sayı var mı?) |
| 0 cevap, görüntülenme <%25 | 19 | $0 | Ek D K3b: liste katmanı (Opener B, fotoğraf, ücret, kimlik); Connects alımı dur |
| 0 cevap, görüntülenme ≥%25 | 26 | +$14 | Gövde katmanı: %100 teşhisli açılış, bant tabanı fiyat, yalnızca A-sınıf |

**Teşhis-önce teklif stratejisi (ikna kalitesi)**

Kural: *Müşterinin sitesi hakkındaki kanıt, benim sitem hakkındaki kanıttan güçlüdür.* Trust stack sırası A-sınıfta şöyle değişir: 1 ölçülmüş teşhis (onların sitesi) → 2 düzeltme + fiyat + süre → 3 demo/Lighthouse kanıtı → 4 risk transferi (fonlanmış küçük milestone) → 5 tek soru.

| Adım | Süre | Ne |
| --- | --- | --- |
| 1 | 60 sn | URL'yi pagespeed.web.dev'e ver (mobil): puan + ilk 2 sorun (ör. hero görsel MB, render-blocking script sayısı, LCP saniyesi) |
| 2 | 30 sn | Telefonda aç: 1 görünür sorun (üst katta telefon yok, menü taşıyor, form hata veriyor) |
| 3 | 60 sn | PSI sonucunun ekran görüntüsü, 3 daire → teklife ek dosya |
| 4 | 2–3 dk | Şablon T1/T2/T3'ün ilk paragrafını aşağıdaki teşhis açılışıyla değiştir; sayı ilk cümlede |
| 5 | 30 sn | Fiyat çapası: "$49 intro (regular $79)"; eleme sorularına "doğrudan cevap + 1 somut detay + gerekirse 1 link" |
| 6 (ops.) | 3 dk | Bütçe ≥$150 A-sınıf ilanda 60 sn ekran videosu (Loom tarzı link); günde ≤3; videoda iletişim bilgisi yok |

URL yoksa (landing/Sheets): "mikro-plan" açılışı — 3 satırlık sektöre/açıklamaya özel yapı veya formül listesi.

**Teşhis açılışları (İngilizce — T1/T2/T3/S4'ün ilk paragrafının yerine)**

```text
Speed (T1):
Your homepage scores [41]/100 on mobile PageSpeed right now — the [2.8 MB hero image] and [11 render-blocking scripts] account for most of it. I can take it to 85+ within 48 hours of the milestone being funded, for $[89] intro (regular $149), with the before/after PageSpeed reports attached.

Bug (T1):
I opened [SITE] on my phone: [the menu overlaps the logo below 400 px, and the contact form returns a 500 error] — the second one usually points to a mail plugin conflict after an update. Fixed within 24 hours of funding for $[49] intro (regular $79), full backup first, before/after screenshots included.

Landing (T2, existing site or ad):
Your [Google Ads] traffic lands on a page with [no phone number above the fold and a 4.1-second mobile load] — that is where the calls leak. A one-page, hand-coded landing page with a sticky tap-to-call button, delivered in 48 hours for $[129] intro (regular $199), fixes both.

Landing (T2/T3, no site yet — micro-plan):
For a [roofing] company in [Austin], the page that converts is: one offer in the headline ("Roof repair today — call before 2 pm"), tap-to-call in the header, three services, five reviews, service-area list, FAQ, short form. I build exactly that, hand-coded, in 48 hours for $[129] intro (regular $199).

Sheets (S4, no file yet — micro-plan):
From your description this is [a monthly summary tab driven by XLOOKUP + SUMIFS, with a dropdown to keep entries clean] — about two hours of work. Delivered today for $[35] intro (regular $59), with formulas that keep working when you add rows.

Attachment caption (put as the last line before the name):
Attached: your PageSpeed result from today with the three biggest issues circled.
```

**60 saniyelik video (opsiyonel, A-sınıf, bütçe ≥$150; İngilizce)**

```text
0–5 s   "Hi [NAME], Oğuzhan here — this is your site on a phone."
5–25 s  Point 1 with the number: "[Mobile score 41; this 2.8 MB image is most of it.]"
25–40 s Point 2 visible: "[No phone number above the fold — on mobile that's the call you lose.]"
40–55 s Demo: "Here is the same structure done right — sticky call button, sub-250 KB page." (open the matching demo)
55–60 s "Fixed price, 48 hours, funded milestone — details in the proposal."
```

**Eleme sorusu cevap kalıbı (İngilizce)**

```text
[Direct answer in one sentence.] [One specific detail from their post or site.] [Optional: one link — demo or portfolio item.]
Never: "See cover letter." Never: a paragraph longer than three sentences.
```

**Bölüm bazlı revizyon özeti (v1 → v2)**

| Bölüm | v1 | v2 (Ek E) |
| --- | --- | --- |
| 0 | 100 teklif, λ 3,2, ≈$200 | 57–59 teklif (uyarlanır 50–75), λ 3,0–3,1, nakit ≈ **$45–65** |
| 2 | Filtre + müşteri filtresi | **Skor kartı** (8 kapı + puan; A/B/C); Invites 0 / Interviewing 0 / Last viewed ≤1 sa eklendi; Connects ≤8 kapısı |
| 3 | 33/gün, blok A4 B7 C3 D14 E5 | 19/gün, blok A2 B4 C1 D8 E4; teklif başına 6–8 dk (A) |
| 4 | Boost ≤20, Badge 20, Plus Gün 0, 400 Connects | **Boost 0, Badge 0**, Plus Gün 2'ye ertelenir (ücretsiz bildirim ≤2 dk ise), Ek D şelalesi ($1,50 → +$15 → +$15) |
| 5 | Trust stack: problem → gözlem → demo → … | A-sınıfta **teşhis-önce** sıra; teşhis açılışları; PSI ekran görüntüsü eki; fiyat çapası; eleme kalıbı; opsiyonel 60 sn video |
| 6 | Intro fiyat | Aynı + "intro (regular $X)" çapası her teklifte |
| 7 | Kanıt paketi 1–8 | **Sıra 0: müşterinin sitesine ait ölçüm** (PSI sayısı + görsel), sonra 1–8 |
| 8 | KPI 35/68/100 | KPI 19/38/57 (uyarlanır); cevap hedefleri aynı (≥2/≥5/≥7) çünkü oran yükselir; takip tablosuna "Skor", "Sınıf", "p", "λ küm.", "Teşhis (E/H)" sütunları |

**Bütçe (72 saat, model)**

| Kalem | v1 | Ek C | Ek D | **Ek E** |
| --- | --- | --- | --- | --- |
| Teklif | 100 | 75–100 | 70–75 | **57–59** (uyarlanır 50–75) |
| Ortalama p | %3,2 | %3,5–4 | %4,2 | **%5,2** |
| λ / P(≥1) | 3,2 / %96 | ≥3,3 / %96 | 3,0–3,3 / %95–97 | **3,0–3,1 / %95–96** |
| Connects (nominal) | ~1.320 | ~650–850 | ~450 | **~390** |
| Bedava yığın | 100 | 170 | ~70–100 | ~70–100 |
| Satın alınacak | ~1.220 | ~480–680 | ~350–380 | **~290–320** |
| Nakit (Plus dahil/hariç) | ≈$203 | ≈$92–122 | ≈$45–70 | **≈$45–50** (Plus gerekirse +$20 → ≤$65) |
| İlk cevap öncesi nakit tavanı | $180+ | $60–90 | ≈$32 | **≈$32** (Ek D şelalesi) |
| Teklif başına dakika | 3 | 3 | 3–4 | **6–8 (A) / 3 (B)** |

**Değişmeyenler:** profil yaması, kanıt paragrafı, 5 dk SLA (A-sınıfta), şablon gövdeleri, fiyat tablosu, milestone yapısı, interview script'i, katman teşhisi, Ek D şelalesi. **Kesilenler:** boost, Badge (72 sa), yaşlı/genel/kalabalık ilanlar, Connects >8 ilanlar, Gün 0'da Plus.

**Şimdi yap**
1. Skor kartını tek sayfa yazdır; takip tablosuna "Skor / Sınıf / p / λ küm. / Teşhis" sütunlarını ekle; A ≥10, B 6–9, C gönderme.
2. pagespeed.web.dev'i yer imine al; PSI ekran görüntüsü + 3 daire akışını bir kez 90 sn'de prova et; teşhis açılışlarını `;dx-speed` `;dx-bug` `;dx-landing` `;dx-plan` `;dx-sheets` kısayollarına kaydet.
3. Gün 1 sonu 19 teklifte cevap sayısına göre uyarlanır kota tablosunu uygula; Connects alımı yalnızca Ek D kapıları açıldıkça.
