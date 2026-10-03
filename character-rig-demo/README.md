# Karakter rig denemesi (senin orman JPG → katman + Three.js)

Tek kaynak görsel: `assets/source.jpg` (720×1280, ayakta orman sahnesi). Başka karakter dosyası kullanılmıyor.

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

## Animasyon (şimdilik)

- Nefes (gövde scale), baş spring + mouse parallax
- Saç ve çanlar overlap / spring
- Hafif bacak sway (ayakta poz)

## Kol kaldırma

Bu pozda kollar gövdenin arkasında; ayrı kol parçası yok. Kol denemesi için ya ön/yan pozlu görsel ya da Photoshop’ta `arm_upper` / `arm_lower` PNG’leri gerekir.
