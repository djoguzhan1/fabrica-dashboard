# 72h plan — Slack bağlanamadı: plandan ödün yok

**Durum:** Mobilde Slack OAuth / `api.slack.com` → *browser not supported*. **Slack planın zorunlu parçası değil.**

Orijinal plan (`docs/upwork-72h-first-job-plan.md`, dal `cursor/upwork-72h-plan-5f90`) şunu ister:

- Kayıtlı aramalar (Q1–Q20 mantığı)
- **Anlık veya çok hızlı bildirim** (Slack **veya** Telegram **veya** webhook **veya** Upwork Plus)
- Whitelist / EV / 5 dk teklif SLA
- Teklif stratejisi (`docs/upwork-proposal-strategy.md`)

**Slack** yalnızca `docs/upwork-job-alerts-setup.md` içindeki **örnek kanallardan biri**. Değiştirmek = planı bozmak değil.

---

## Mobil uyumlu yığın (Slack’siz, planla aynı hedef)

| Plan ihtiyacı | Senin kurulum |
|---------------|----------------|
| Hızlı haber | **Freelancer Plus** anlık iş (Upwork uygulaması push) — zaten var |
| Dar filtre + skor | **UpHunt** Listener/Feed (kelime, bütçe ≥20, verified) — Slack bağlı olmasa da **feed’de birikir** |
| İkinci hat (isteğe bağlı, ~$19) | **Vibeworker Pro** → **telefon push** (Slack/Telegram kanalı şart değil) |
| Yedek | UpHunt **e-posta** (Notifications’ta varsa) |
| Upwork içi | **12 kayıtlı arama** + bildirim (plan Ek Q1–Q12) |

Turuncu *No channel connected* = **push gelmez**; **dinleme ve feed listesi çalışır**. Hızı **Plus + (isteğe bağlı Vibeworker push)** verir.

---

## Yapma / yap

| Yapma | Yap |
|-------|-----|
| Telefonda Slack / api.slack.com | UpHunt **Listener kaydet** |
| Plana “Slack şart” sanma | Plus bildirim + feed kontrolü |
| Connect Slack’e tekrar bas | Notifications → **Email** aç (varsa) |

---

## Günlük ritim (plan SLA ile uyumlu)

1. **Plus push** veya **Vibeworker push** → ilan açılır.
2. Yoksa günde **4 kez** (sabah, öğle, akşam, gece): UpHunt **Feeds** → yeni match → link.
3. **30 sn EV** → GO ise **5 dk içinde** teklif (`docs/upwork-proposal-strategy.md`).

Bu, plandaki “bildirim geldikçe <5 dk gönder” mantığının mobil karşılığıdır.

---

## PC gelince (opsiyonel bonus)

Slack veya UpHunt Webhook — **ekstra konfor**, plan tamamlanması için **şart değil**.
