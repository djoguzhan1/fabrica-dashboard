# Canlıya al — güvenilir kalıcı linkler (2 dakika)

**Resmi adresler (yayın sonrası):**

| Sayfa | Kalıcı URL |
| --- | --- |
| Ana sayfa | https://djoguzhan1.github.io/oguzehan-salatan/ |
| HVAC demo | https://djoguzhan1.github.io/oguzehan-salatan/demos/hvac-landing/ |
| Plumbing demo | https://djoguzhan1.github.io/oguzehan-salatan/demos/plumbing-landing/ |

`github.io` + kişisel repo adı müşteriye güven verir; CDN veya geçici host gerekmez.

## Adımlar

### 1) Boş repo oluştur

https://github.com/new?name=oguzehan-salatan&description=Portfolio%20and%20live%20demos&visibility=public

- **Add a README** işaretleme (boş repo yeterli).
- **Create repository**.

### 2) Cursor’a sadece bu repo için yazma izni

GitHub → **Settings** → **Applications** → **Installed GitHub Apps** → **Cursor** → **Configure** → **Only select repositories** → **`oguzehan-salatan`** → Save.

### 3) Ajan’a yaz

> `oguzehan-salatan` repoya siteyi push et, Pages açık olsun.

Ajan `master` dalına site dosyalarını atar. GitHub Pages varsayılan olarak `master` / root’tan yayınlar (1–2 dk).

### Alternatif (sen push edersen)

```bash
git clone https://github.com/djoguzhan1/fabrica-dashboard.git
git clone https://github.com/djoguzhan1/oguzehan-salatan.git
rsync -av fabrica-dashboard/web-dev-portfolio/ oguzehan-salatan/
cd oguzehan-salatan
git add -A && git commit -m "Publish portfolio and demos" && git push
```

Settings → **Pages** → Source: **Deploy from a branch** → **master** / **(root)** → Save (gerekirse).

---

Eski `web-dev-portfolio` repo linkleri kullanılmayacak; Upwork ve profillerde yalnızca üstteki üç `oguzehan-salatan` URL’sini kaydet.
