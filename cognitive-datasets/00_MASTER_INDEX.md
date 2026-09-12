# PRATİK ZEKA / ANLIK PERFORMANS — MASTER VERİ SETİ

> **Profil:** Yavaş işlem hızı + aşırı düşünme + bilgi eksikliği + sözlü kodlama zayıf + sosyal donma + geç fark etme
> **Kök formül:** Hızlı tepki = Önceden yüklü bilgi (2'den 1'i) + Kalıp tanıma + 1 sn hareket
> **Kaynak sayısı:** 120+ akademik/klinik kaynak
> **Son güncelleme:** 2026-09-12

---

## 9 ANA SORUN + 2 KÖK NEDEN

| ID | Sorun | Dosya | Kaynak |
|----|-------|-------|--------|
| S01 | Aşırı Düşünme / Karar Felci | `S01_ASIRI_DUSUNME.json` | 18 |
| S02 | Bilgi Eksikliği / Ön Hazırlık Yok | `S02_BILGI_EKSIKLIGI.json` | 22 |
| S03 | Yavaş İşlem Hızı | `S03_YAVAS_ISLEM_HIZI.json` | 14 |
| S04 | Sözlü Öğrenme / Kodlama Zayıflığı | `S04_SOZLU_OGRENME.json` | 16 |
| S05 | Sosyal Donma / Zihin Boşalması | `S05_SOSYAL_DONMA.json` | 15 |
| S06 | Geç Fark Etme / Gözlemci Mod | `S06_GEC_FARK_ETME.json` | 12 |
| S07 | Eylem Başlatma Gecikmesi | `S07_EYLEM_BASLATMA.json` | 13 |
| S08 | Çalışma Belleği Aşırı Yükü | `S08_CALISMA_BELLEGI.json` | 11 |
| S09 | Tanıma Refleksi / Pratik Zeka Eksikliği | `S09_TANIMA_REFLEKSI.json` | 14 |

**Kök nedenler:** S01 (düşünme) + S02 (bilgi) → diğer 7 sorunu besler

---

## ÇÖZÜM HİYERARŞİSİ (Kanıt gücüne göre)

### Tier 1 — En güçlü kanıt (hemen uygula)
1. **Implementation Intentions (if-then)** — d=0.65 meta-analiz (Gollwitzer & Sheeran, 2006)
2. **Ön bilgi aktivasyonu** — advance organizers, 30-60 sn tarama
3. **Retrieval practice** — g=0.50-0.74 vs pasif okuma
4. **Time Pressure Management** — telafi stratejisi, RCT destekli
5. **1 saniye kuralı** — ağız önce, düşünme sonra

### Tier 2 — Güçlü kanıt (2-4 hafta)
6. **Dual coding** — yazı + görsel, %25-40 daha iyi hatırlama
7. **Spaced repetition** — g=0.74 spaced vs massed
8. **Graded exposure** — sosyal kaygı, 3-5 tekrar
9. **Recognition-primed training** — kalıp kartları
10. **Behavioral activation (CADDI)** — eylem başlatma, d=0.65

### Tier 3 — Destekleyici (uzun vade)
11. Speed-of-processing training (UFOV) — 10 seans, transfer kısıtlı
12. Cognitive training — laboratuvar iyileşme, günlük hayata transfer zayıf
13. Mindfulness — dikkat yönetimi
14. Chunking / şema oluşturma — uzmanlık geliştirme

---

## GÜNLÜK SİSTEM (15 dk)

```
SABAH (5 dk)
  → 3 if-then plan
  → Bugünkü ortamları tara (bilgi yükle)

GÜN İÇİ
  → 1 sn kuralı
  → Ortama girmeden 30 sn ön yükleme
  → 3× "ilk ses" antrenmanı

AKŞAM (5 dk)
  → Geç kaldım defteri
  → 1 kalıp kartı ekle
  → Spaced repetition (öğrenme)
```

---

## DOSYA YAPISI

Her JSON dosyası şunları içerir:
- `problem`: Tanım, belirtiler, mekanizma
- `research_sources[]`: Kaynak, bulgu, etki büyüklüğü, URL
- `solutions[]`: Kanıt seviyesi, protokol, süre
- `daily_protocol`: Günlük rutin
- `metrics`: Ölçüm
- `interactions`: Diğer sorunlarla ilişki
