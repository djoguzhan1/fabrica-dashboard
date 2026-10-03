# Karakter rig denemesi (PNG → katman + Three.js)

Tek JPG çömelmiş poz için otomatik **kaba poligon maskeleri** ile katmanlara ayırma ve pürüzsüz idle animasyon.

## Komutlar

```bash
npm install
npm run dev
```

Katmanları yeniden üretmek (maskeleri `scripts/split_layers.py` içinde düzenle):

```bash
python3 scripts/split_layers.py
```

## Sınırlar

Bu pozda dizler gövdeyi kapattığı için **kol kaldırma** ayrı parça olarak yapılamaz; boşluk kalır. İlk deneme: nefes, baş, saç, çanlar, kamera parallax.

Daha iyi kesim için Photoshop’ta parçalı PNG verip aynı `manifest.json` yapısına koyabilirsin.
