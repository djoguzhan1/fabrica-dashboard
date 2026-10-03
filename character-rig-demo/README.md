# Karakter rig denemesi (senin orman JPG → katman + Three.js)

Tek kaynak görsel: `assets/source.jpg` (720×1280, orman, kollar yanda).

## `localhost` bağlanmayı reddetti?

Bu normal: tarayıcı **senin bilgisayarındaki** `localhost`’a bakıyor. Sunucuyu **senin** açman gerekir (Cursor bulutu senin PC’ndeki 5173’e bağlamaz).

### Windows (PowerShell veya CMD)

```bash
cd character-rig-demo
npm install
npm run dev
```

Terminalde şuna benzer bir satır görürsün: `Local: http://localhost:5173/` — **o adresi** tarayıcıda aç.

Kapatmak: terminalde `Ctrl+C`.

Alternatif (production build önizleme):

```bash
npm run build
npm run preview
```

→ `http://localhost:4173`

### Canlı link (GitHub Pages, `master` deploy sonrası)

https://djoguzhan1.github.io/fabrica-dashboard/demos/character-rig/

(PR henüz merge değilse önce yerel `npm run dev` kullan veya PR branch’ini çek.)

---

## Katmanları yeniden üret

```bash
python3 scripts/split_layers.py
```

Önizleme: `assets/layers/_mask_preview.png`

## Animasyon

- Nefes, baş, saç, çanlar, bacak sway
- Kol zinciri (`arm_*`): spring ile kol kaldırma döngüsü
