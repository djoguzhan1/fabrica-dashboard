# Karakter rig denemesi (senin orman JPG → katman + Three.js)

Tek kaynak görsel: `assets/source.jpg` (720×1280, orman, kollar yanda). Başka karakter dosyası kullanılmıyor.

Katmanlar `scripts/split_layers.py` içindeki normalize poligon maskeleriyle üretilir.

## Komutlar

```bash
npm install
npm run dev
```

Maskeleri güncelledikten sonra:

```bash
python3 scripts/split_layers.py
```

Önizleme: `assets/layers/_mask_preview.png` (kırmızı çerçeveler).

## Animasyon

- Nefes, baş, saç, çanlar, bacak sway
- `arm_l_upper` / `arm_l_lower` ve sağ kol: omuz→dirsek zinciri, spring easing ile kol kaldırma döngüsü

## Katmanlar

`arm_*` maskeleri `scripts/split_layers.py` içinde; yeşil nokta = joint pivot.
