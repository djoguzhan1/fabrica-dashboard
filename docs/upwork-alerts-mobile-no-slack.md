# Upwork ilan uyarısı — telefon only, Slack yok

**Durum:** Telefonda Chrome → Slack (`Connect Slack`, `api.slack.com`) → *browser not supported*. Normal; Slack mobil tarayıcıyı bilerek kapatıyor.

**Çözüm:** Slack’i şimdilik bırak. İlan linki = **UpHunt paneli** + **Freelancer Plus** (zaten var).

---

## 5 dakika kurulum (sadece UpHunt uygulaması / Chrome → uphunt.io)

### 1) Feed / Listener oluştur

1. Chrome → **uphunt.io** → giriş.
2. **Create Listener** veya **Feeds** → **+ New**.
3. Doldur:
   - Name: `wp-fix`
   - Keywords: `wordpress fix broken error mobile`
   - Min budget: **20**
   - Payment verified: **on**
4. **Save**.

İkinci feed (isteğe bağlı): `landing page small business local` — aynı filtreler.

Turuncu uyarı (*No channel connected*) **görmezden gel** — ilanlar yine feed’de birikir.

### 2) Bildirim (Slack olmadan)

Aynı **Notifications** sayfasında:

- **Email** / **Email digest** varsa → **açık**, sık sıklık: **hourly** veya **instant** (ne sunuyorsa).
- **Slack / Telegram** → dokunma.

### 3) Freelancer Plus (Upwork uygulaması)

- Kayıtlı arama: `wordpress broken fix` + `landing page local`.
- **≥1 aktif teklif** (Plus anlık iş için).
- Bildirimler açık.

### 4) Günlük ritim (2 dk, 3–4 kez)

1. UpHunt → **Feeds** → yeni match → **job link** → Upwork teklif.
2. Plus bildirimi gelirse → aynı EV / teklif stratejisi.

Slack’i sonra **sadece PC’de** 2 dk bağlarsın; şart değil.

---

## Ne zaman Slack?

- PC/Mac Chrome → UpHunt **Connect Slack** → `#upwork`  
- veya `api.slack.com/apps` → Incoming Webhooks → URL → UpHunt Webhook.

Telefonda tekrar deneme — zaman kaybı.

---

## İlgili

- Teklif: `docs/upwork-proposal-strategy.md`
- Tam alert planı (PC sonrası): `docs/upwork-job-alerts-setup.md`
