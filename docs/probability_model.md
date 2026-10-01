# İhtimal modeli (sistem içi)

Tek teklif P = `open × reply × hire` (`go_score.py`). **Teklif sayısı band seçmez.**

## Varsayılan huni (tam-paket, boost ilk 4)
| Aşama | Oran |
| --- | --- |
| open | ~80% |
| reply | ~60% |
| hire | ~51–60% |
| **P** | **~28–33%** |

## Hire katmanı bonusları (kümülatif, script)
- İyi müşteri: hire rate ≥70%, spent ≥$100 → +5%
- Davet → +10% hire, +15% reply
- `--chat-ready` (§23 metin hazır) → +4% hire
- 0 yorum: taban ~51%; 3+ yorum: +3%/yorum (max 5)

## Yapısal eleme
`go_precheck.py` SKIP → P=0, model yok.

## 10 teklifte 2 iş
Tam-paket ~%30 → beklenen 3 iş; %20 hedefi tam-paket + sohbet hattı ile tutar.

Kalibrasyon: `docs/calibration.md`
