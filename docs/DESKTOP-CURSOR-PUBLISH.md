# Masaüstü Cursor — canlı siteyi yayınla (tek görev)

Upwork linkleri `https://djoguzhan1.github.io/web-dev-portfolio/` bu repodan geliyor. Kod `fabrica-dashboard` içinde hazır; cloud agent `web-dev-portfolio` repoya push edemiyor (403). **Senin GitHub oturumun** ile bir kez yayınlanmalı.

## Seçenek A — Cloud agent’ın yapması (en kolay)

1. GitHub → **Settings** → **Developer settings** → **Fine-grained tokens** → **Generate**.
2. Repository access: **Only** `djoguzhan1/web-dev-portfolio` → Permissions: **Contents** Read and write.
3. GitHub → `djoguzhan1/fabrica-dashboard` → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
   - Name: `WEB_DEV_PORTFOLIO_PAT`
   - Value: token
4. Cloud agent’a yaz: **“WEB_DEV_PORTFOLIO_PAT eklendi, portfolio’yu yayınla.”**

Agent workflow’u tetikler veya script çalıştırır; 1–2 dk sonra üç Upwork URL’si güncellenir.

## Seçenek B — Masaüstü Cursor (bu repoda)

1. `fabrica-dashboard` klasörünü Cursor’da aç.
2. Terminal: `gh auth login` (hesap `djoguzhan1` olmalı).
3. Agent’a şunu gönder (kopyala-yapıştır):

```
Run bash scripts/publish-web-dev-portfolio.sh from repo root. If push fails, fix auth and retry until https://djoguzhan1.github.io/web-dev-portfolio/ shows external styles.css and title contains "Landing pages and WordPress fixes". Do not delete docs/ or fiverr-screenshots/ in web-dev-portfolio repo.
```

## Seçenek C — Cursor GitHub uygulamasına repo ekle

GitHub → **Settings** → **Applications** → **Cursor** → **Configure** → Repository access → **`web-dev-portfolio`** işaretle → Save.

Cloud agent’a: **“web-dev-portfolio erişimi verdim, yayınla.”**

## Doğrulama

- Hub: sayfa kaynağında `link rel="stylesheet" href="styles.css"` ve Lighthouse 99–100 metni.
- HVAC: `<title>` içinde `Same-Day AC Repair` (pipe `|` eski sürüm).
