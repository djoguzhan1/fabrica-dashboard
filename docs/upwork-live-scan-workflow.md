# Canlı ilan tarama — Ek E (alt oturum yok)

Upwork, sunucu veya headless tarayıcıdan **girişsiz** erişimi Cloudflare ile keser. İkinci hesap, ajans alt oturumu veya bulutta Upwork’a login **yasak** (ToS + plan kuralı).

**Çözüm:** Kendi **ana Upwork oturumunda** (telefon veya bilgisayar, zaten giriş yaptığın sekme) arama sayfasını aç → konsolda çıkarıcıyı çalıştır → JSON’u bu repoda skorla. Upwork’a sadece sen girersin; araç yalnızca ekranda zaten görünen DOM’u okur.

## 1) Kayıtlı arama URL’leri

Terminalde (veya Cloud Agent’ta):

```bash
node scripts/upwork-scan/run.mjs --urls
```

Her `Q1`–`Q12` linkini **aynı tarayıcıda** aç (çıkış yapma, yeni hesap açma).

**UI filtreleri** (her aramada elle):

- Sort: **Newest**
- Posted: **Last 24 hours**
- **Payment verified**
- Budget: **$20 – $1,000**
- Proposals: **Less than 5** + **5 to 10**
- Experience: **Entry** + **Intermediate**

## 2) İlanları çıkar (ana oturum)

1. Arama sonuçları yüklendikten sonra `F12` → **Console**.
2. `scripts/upwork-scan/bookmarklet/extract-tiles.source.js` dosyasının **tamamını** yapıştır → Enter.
3. `Extracted N jobs. JSON copied to clipboard.` görürsün.
4. Panodaki JSON’u `scripts/upwork-scan/inbox/q1.json` olarak kaydet (veya birleştir).

Aynı adımı her aktif sorgu için tekrarla (günde 12 tur; odak Blok D/E saatlerinde).

### İş detayı (A/B adayları için)

Kapılar **G5** (invites/interviewing) ve **G7** (Connects) liste kartında olmayabilir.

1. İlanı aç (aynı sekme).
2. Console’a `scripts/upwork-scan/bookmarklet/extract-detail.source.js` yapıştır.
3. JSON’u `inbox/detail-abc123.json` kaydet; skorlayıcıda birleştir.

## 3) Skorla (Ek E A/B/C)

```bash
node scripts/upwork-scan/run.mjs scripts/upwork-scan/inbox/q1.json scripts/upwork-scan/inbox/q2.json
```

Çıktı:

- **A** (≥10 puan) → teşhis-önce teklif (PSI + ekran görüntüsü), şablon satırındaki T1/T2/T3/S4/S5
- **B** (6–9) → kısa şablon, boost yok
- **SKIP** → Connects harcama

`--all` ile atlananların nedenini gör.

## 4) Operasyon sırası (ilk gün)

1. Profil yaması (plan Bölüm 1) bitmeden teklif yok.
2. `Q1`–`Q4` + `Q8` taraması (Tier-1) → A listesi.
3. Her **A** ilanı: pagespeed.web.dev → teşhis açılışı → teklif ≤5 dk (ilan yaşı).
4. Gün sonu: ≥19 teklif, görüntülenme oranı → Ek D şelalesi (K3/K3b).

## Cloud Agent’a JSON gönderme

- Dosyayı `scripts/upwork-scan/inbox/` altına commit/push et, veya
- Sohbete JSON ekle; agent `run.mjs` ile skorlar ve APPLY sırası verir.

## Test (örnek veri)

```bash
node scripts/upwork-scan/run.mjs scripts/upwork-scan/fixtures/sample-tiles.json
```

Beklenen: 2× A veya B, 1× SKIP (React long-term).
