# Docs

## Rehberler

| Dosya | Açıklama |
|---|---|
| [eskisehir-ekim-gezi-rehberi.md](./eskisehir-ekim-gezi-rehberi.md) | Eskişehir 2–4 Ekim 2026 gezi, etkinlik, sosyalleşme ve flört planı (tam sohbet derlemesi) |
| [upwork-strategy.md](./upwork-strategy.md) | **Upwork tek belge:** GO/SKIP, boost, ön-iş, açılış, test hattı, rakip kartları, kapanış, profil, Vibeworker filtreleri, teklif log'u |

Teklif kural kontrolü: `python3 scripts/proposal_lint.py letter.txt --must "..." --check-links`

GO yapısal kontrol (teklif sayısı yok): `python3 scripts/go_precheck.py --budget 100 --payment-verified --title "..." < post.txt`

Orkestrasyon: [go-orchestration.md](./go-orchestration.md) · Promptlar: `prompts/`
