# Portfolio — kalıcı canlı linkler

Bu dosyayı Upwork, Fiverr, e-posta imzası ve profillerde **aynı URL’leri** kullanmak için sakla.

## 1) Hedef linkler (Upwork / profil — `web-dev-portfolio`)

Yayınlandığında **asıl** adresler bunlar. Kod hazır; `web-dev-portfolio` repoya push edildiğinde GitHub Pages otomatik güncellenir.

| Sayfa | Kalıcı URL |
| --- | --- |
| Ana sayfa (hub) | https://djoguzhan1.github.io/oguzehan-salatan/ |
| CoolAir HVAC demo | https://djoguzhan1.github.io/oguzehan-salatan/demos/hvac-landing/ |
| ProFix Plumbing demo | https://djoguzhan1.github.io/oguzehan-salatan/demos/plumbing-landing/ |

**Yayın:** `fabrica-dashboard` → Actions → **Publish web-dev-portfolio to GitHub Pages** (secret `WEB_DEV_PORTFOLIO_PAT`) veya Cursor uygulamasına `web-dev-portfolio` yazma izni ver. Adımlar: `PUBLISH.md`.

---

## 2) GitHub Pages — `fabrica-dashboard` (temiz `github.io`, tek tık)

Kod `gh-pages` dalında. **Bir kez** aç:  
https://github.com/djoguzhan1/fabrica-dashboard/settings/pages → **Deploy from a branch** → `gh-pages` / **(root)** → Save.

| Sayfa | Kalıcı URL |
| --- | --- |
| Ana sayfa | https://djoguzhan1.github.io/fabrica-dashboard/ |
| HVAC demo | https://djoguzhan1.github.io/fabrica-dashboard/demos/hvac-landing/ |
| Plumbing demo | https://djoguzhan1.github.io/fabrica-dashboard/demos/plumbing-landing/ |

---

## 3) CDN yedek (şimdi çalışır — repo public olduğu sürece kalıcı)

Pages veya `web-dev-portfolio` push’u beklerken **aynı yeni site** bu adreslerde de açılır (jsDelivr / Statically, `gh-pages` dalından).

| Sayfa | Kalıcı yedek URL |
| --- | --- |
| Ana sayfa | https://cdn.statically.io/gh/djoguzhan1/fabrica-dashboard@gh-pages/index.html |
| HVAC demo | https://cdn.statically.io/gh/djoguzhan1/fabrica-dashboard@gh-pages/demos/hvac-landing/index.html |
| Plumbing demo | https://cdn.statically.io/gh/djoguzhan1/fabrica-dashboard@gh-pages/demos/plumbing-landing/index.html |

Hub içinden demo linkleri klasör URL’si kullanır; GitHub Pages’te sorunsuz. Sadece CDN’de demo açmıyorsa yukarıdaki **index.html** satırlarını kullan.

---

## Kopyala-yapıştır (tek satır)

```
Hub:     https://djoguzhan1.github.io/oguzehan-salatan/
HVAC:    https://djoguzhan1.github.io/oguzehan-salatan/demos/hvac-landing/
Plumbing: https://djoguzhan1.github.io/oguzehan-salatan/demos/plumbing-landing/
```

Pages açıkken `fabrica-dashboard` yolunu kullanacaksan `web-dev-portfolio` → `fabrica-dashboard` ile değiştir.

Son güncelleme: 2026-09-24 · Kaynak dal: `fabrica-dashboard` → `gh-pages` / `master` → `web-dev-portfolio/`
