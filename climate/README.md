# El Niño olay veritabanı

`el-nino-database.json` — ONI tablolarından çıkarılmış olaylar ve **deprem metaforu** ile hesaplanmış toplam güç.

## Okuma

- **M_instant:** o dönemin ONI + 5 (2.0 → 7.0 deprem benzetmesi)
- **M_total:** olayın tüm dönemlerinin enerji toplamından türetilen kümülatif eşdeğer büyüklük
- **window:** resmi El Niño penceresi (ONI ≥ 0.5; sönümde son ≥ 0.5 dönem dahil)

Kar / iklim karşılaştırmalarında `events[].id` ile referans ver.
