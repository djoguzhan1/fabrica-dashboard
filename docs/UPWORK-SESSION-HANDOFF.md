# Upwork / portföy — oturum handoff (tüm sohbetler için)

**Son güncelleme:** 2026-09-26  
**Repo:** https://github.com/djoguzhan1/fabrica-dashboard  
**Kullanıcı:** Oğuzhan S. (Bursa, Turkey) — Upwork yeni, 0 review, dürüst profil.

---

## Önemli: neden diğer sohbet “handoff dosyasını bulamadı”?

1. **`/cursor/stores/self/…` sadece o Cloud Agent oturumuna özel.** Yeni sohbet = genelde yeni VM; bu yol orada yok veya boş. **Güvenilir kaynak bu dosya (GitHub).**
2. **`master` dalında her şey yok.** Proof projeler ve portföy görselleri şu an **`cursor/proof-projects-5f90`** üzerinde (PR #8). `git checkout master` yapıp `proof-projects/` aramak boşa çıkar.
3. **Profil metni** `docs/upwork-profile.md` → dal **`cursor/upwork-profile-5f90`** (PR #3), master’da değil.
4. **72 saat planı** `docs/upwork-72h-first-job-plan.md` → dal **`cursor/upwork-72h-plan-5f90`** (PR #6). Bazı workspace’lerde plan başka dala kopyalanmış olabilir; kaynak dal bu.

### Yeni sohbette agent’a ne yazılır (kopyala-yapıştır)

```text
fabrica-dashboard repo: önce docs/UPWORK-SESSION-HANDOFF.md dosyasını oku.
Proof projeler ve Upwork portföy paketi için dal: cursor/proof-projects-5f90 (PR #8).
Plan için: cursor/upwork-72h-plan-5f90 içindeki docs/upwork-72h-first-job-plan.md.
Profil için: cursor/upwork-profile-5f90 içindeki docs/upwork-profile.md.
```

Veya dosyayı sohbete **@docs/UPWORK-SESSION-HANDOFF.md** ile ekle (dalı `proof-projects` veya merge sonrası `master`).

---

## Dosya / dal haritası

| İçerik | Yol | Dal | PR |
| --- | --- | --- | --- |
| Bu handoff | `docs/UPWORK-SESSION-HANDOFF.md` | `cursor/proof-projects-5f90` | #8 |
| Proof repos (kaynak) | `proof-projects/tidycsv`, `docbrief`, `sheet-notify` | `cursor/proof-projects-5f90` | #8 |
| Publish komutları | `proof-projects/README.md` | `cursor/proof-projects-5f90` | #8 |
| Upwork portföy metin + PNG | `docs/upwork-portfolio/` | `cursor/proof-projects-5f90` | #8 |
| 72h plan + Ek A–F | `docs/upwork-72h-first-job-plan.md` | `cursor/upwork-72h-plan-5f90` | #6 |
| Upwork profil (EN) | `docs/upwork-profile.md` | `cursor/upwork-profile-5f90` | #3 |
| Demolar + hub | `web-dev-portfolio/` | **`master`** (PR #4 merge) | #4 |
| Canlı site | ayrı repo | `github.com/djoguzhan1/web-dev-portfolio` | — |

**PR #8:** https://github.com/djoguzhan1/fabrica-dashboard/pull/8  
Merge edilmeden `master`’da `proof-projects/` ve `docs/upwork-portfolio/` görünmez.

---

## Kronoloji (ne yapıldı)

1. Upwork profil metni → PR #3  
2. HVAC + Plumbing demoları + hub → PR #4 → **master**  
3. 72h ilk iş planı (Ek E ~390 Connects, Ek F geniş havuz / tidycsv-docbrief-sheet-notify) → PR #6  
4. Proof projeler + Upwork portföy paketi → PR #8  

---

## PR #8 özeti

### `proof-projects/tidycsv/`
- CLI: dağınık CSV → 3 sayfalı Excel (Data, Summary+grafik, Changes)
- 27 test, ruff, CI 3.10–3.12, MIT  
- GitHub (kullanıcı açacak): `djoguzhan1/tidycsv`

### `proof-projects/docbrief/`
- PDF/URL/metin → sayfa referanslı brief; `--dry-run`; env-only keys  
- 19 offline test; örnek LLM çıktısı commit edilmedi  
- GitHub: `djoguzhan1/docbrief`

### `proof-projects/sheet-notify/`
- Apps Script: e-posta + Slack, Settings tab, Notified + lock  
- GitHub: `djoguzhan1/sheet-notify`

### `docs/upwork-portfolio/`
- 6 kalem kapak + ek görseller; metinler `docs/upwork-portfolio/README.md`  
- Yükleme sırası: HVAC → Plumbing → tidycsv → docbrief → sheet-notify → Hub  

---

## Canlı demolar

| Ne | URL |
| --- | --- |
| Hub | https://djoguzhan1.github.io/web-dev-portfolio/ |
| HVAC demo | https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/ |
| Plumbing demo | https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/ |

Lighthouse (hub metni): HVAC mobile 99/100/100/100; Plumbing 100×4.

---

## Kurallar (müşteri metni)

- İngilizce only; sahte review/deneyim yok  
- Demolar: fictional company (CoolAir / ProFix style)  
- Fiverr, TR vergi, Payoneer yok  
- Teklif: Dear client / ninja / guru / passionate yok; iletişim bilgisi teklifte yok  
- docbrief: müşteri secret’ları AI’a paste edilmez  

**Ek F:** Title ~65 char, tidycsv + docbrief proof, ~70 proposal / ~475 Connects  
**Ek E:** ~390 Connects, ~$45–50  

---

## Kullanıcının yapması gerekenler

1. **PR #8 merge** (veya `git fetch && git checkout cursor/proof-projects-5f90`)  
2. `proof-projects/README.md` → üç public repo `gh repo create`  
3. docbrief gerçek run + kontrol  
4. Upwork portföy: PNG + `docs/upwork-portfolio/README.md` metinleri  
5. Teklif için `docs/upwork-72h-first-job-plan.md` (doğru daldan)  

Agent **kullanıcı adına GitHub repo oluşturamaz** (gh read-only veya yetki yok).

---

## Teknik notlar

- tidycsv: pandas 3 string dtype; Avrupa ondalık “son ayırıcı ondalık”  
- docbrief: map-reduce; PDF başlık `_guess_title()`  
- Portföy görselleri: puppeteer + sharp; xlsx → LibreOffice headless  

---

## Diğer dallar

| Dal | Konu |
| --- | --- |
| `cursor/upwork-live-scan-5f90` | Upwork tarama workflow |
| `cursor/live-portfolio-sync-5f90` | Canlı portföy sync |

Branch adı kalıbı: `cursor/<isim>-5f90`
