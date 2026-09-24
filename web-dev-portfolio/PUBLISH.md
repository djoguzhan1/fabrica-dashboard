# web-dev-portfolio yayınlama notu

Bu klasör, `djoguzhan1/web-dev-portfolio` deposunun kök dizini ile aynı yapıdadır.
Ajanın o depoya yazma yetkisi olmadığı için (push 403 aldı) dosyalar burada tutuldu.
Yayına almak için klasörün içeriğini o deponun köküne kopyalayıp push etmek yeterli.

## Neler değişti

| Yol | Durum |
| --- | --- |
| `index.html`, `styles.css`, `img/`, `fonts/` | Portföy ana sayfası yeniden yazıldı (gerçek demo ekran görüntüleri, Upwork CTA, OG görseli) |
| `demos/hvac-landing/` | CoolAir HVAC demosu yeniden yazıldı (`index.html`, `styles.css`, `main.js`, `img/`, `fonts/`) |
| `demos/plumbing-landing/` | ProFix Plumbing demosu yeniden yazıldı (`index.html`, `styles.css`, `main.js`, `img/`, `fonts/`) |

Silinmesi gereken dosya yok; eski tek dosyalık `index.html`'lerin üzerine yazılıyor.
Depodaki diğer klasörlere (`docs/`, `fiverr-screenshots/`, `platform-setup/`, `scripts/`) dokunulmuyor.

## Yol 1 — Elle kopyala (5 dakika)

```bash
# 1) Her iki depoyu yan yana klonla
git clone https://github.com/djoguzhan1/fabrica-dashboard.git
git clone https://github.com/djoguzhan1/web-dev-portfolio.git

# 2) Bu branch'i al
cd fabrica-dashboard && git checkout cursor/demo-upgrade-5f90 && cd ..

# 3) Kopyala (PUBLISH.md hariç)
rsync -av --exclude PUBLISH.md fabrica-dashboard/web-dev-portfolio/ web-dev-portfolio/

# 4) Yayınla
cd web-dev-portfolio
git add -A
git commit -m "Rebuild demos and portfolio hub"
git push origin master
```

GitHub Pages 1–2 dakika içinde günceller: <https://djoguzhan1.github.io/web-dev-portfolio/>

## Yol 2 — Ajan push etsin

GitHub → **Settings → Applications → Cursor** (ya da Installed GitHub Apps) → Repository access →
`web-dev-portfolio` deposunu ekle. Sonra ajana "web-dev-portfolio'ya push et" demek yeterli.

## Yayından sonra kontrol

- <https://pagespeed.web.dev/> ile üç sayfayı test et (yerelde: hub 100/100/100/100, HVAC 99–100, Plumbing 100).
- Demo sayfalarında saat bilgisi ziyaretçinin saatine göre hesaplanır (Dallas / Phoenix); açık-kapalı yazısı doğru görünmeli.
- OG görselleri: `img/og-image.jpg`, `demos/hvac-landing/img/og-image.jpg`, `demos/plumbing-landing/img/og-image.jpg`.
  Sayfa metni değişirse `og-image.jpg` dosyalarını yeniden çekmek gerekir (ekran görüntüsüdür).

## İçerikte kişisel varsayımlar (istersen düzelt)

Ana sayfada şu ifadeler geçiyor; gerçek çalışma düzenine göre değiştir:

- "Online 9 am – 11 pm GMT+3, Mon–Sat" (hakkımda kartı ve üstteki bilgi şeridi)
- "Small fixes free for 7 days after delivery" (hizmetler bölümü altı)
- "Two rounds of revisions included" (landing paketinde)
- "Replies within an hour during working hours"

Hepsi `index.html` içinde düz metin; arama yapıp değiştirmek yeterli.
