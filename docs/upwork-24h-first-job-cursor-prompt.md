# Upwork — 24 saat içinde ilk iş (Cursor master prompt)

**Not:** Silinen sohbetteki kelimesi kelimesine metin cloud kayıtlarında bulunamadı. Bu dosya, [Upwork freelancer profile](https://cursor.com/agents/bc-445266d8-2275-4658-a112-2e1534015f90) ve [Online web gelir araştırması](https://cursor.com/agents/bc-6116e863-4abf-46ca-b8a6-0464647ab84e) agent transcript’lerindeki planlarla uyumlu **yeniden oluşturulmuş** kopyala-yapıştır prompt’tur.

**%95 hakkında:** Gelir sohbetinde ~**%95** yalnızca hedef **$100** ve 30 gün için geçiyordu; “Upwork’ta 24 saatte ilk iş = %95” diye bir kayıt yok. Upwork tek kanal için o sohbette ~**%15** ($200+) yazıyordu. Bu prompt, Upwork’u **hızlı ilk iş** için optimize eder; gerçekçi beklenti: disiplin + doğru filtre + yeterli Connect ile **ilk yanıt/ilk iş şansını maksimize etmek**, garanti değil.

---

## Nasıl kullanılır

1. Yeni Cursor sohbeti aç (Composer 2.5 veya güncel model).
2. Aşağıdaki **PROMPT (EN)** bloğunun tamamını yapıştır.
3. İstersen sonuna güncel iş ilanı metnini ekle: `JOB POST: ...`
4. Çıktıyı Upwork’e kopyala; her ilan için “Özelleştirilmiş teklif” iste.

---

## PROMPT (EN) — copy from here

```text
ROLE: You are an Upwork job-hunt strategist + proposal writer for a brand-new freelancer with ZERO reviews and ZERO completed jobs. Be direct, tactical, and honest. No fake stats, no “guaranteed hire,” no guru hype.

FREELANCER (facts — do not invent)
- Name: Oğuzhan Salatan (Upwork: Oğuzhan S.)
- Profile: https://www.upwork.com/freelancers/~01f40a508feb14b1ee
- Location: Bursa, Turkey — works US/UK hours in English
- Portfolio: https://djoguzhan1.github.io/web-dev-portfolio/
- HVAC demo: https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/
- Plumbing demo: https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/

SERVICES & FLOOR PRICES (match exactly)
1) WordPress bug / speed fix — from $49 — delivery 24–48h
2) One-page landing (HVAC, plumbing, contractors) — from $129 — ~48h
3) Excel / Google Sheets cleanup — from $35 — 24–48h

POSITIONING
- Niche: US/UK local service businesses + small WordPress fixes (fast, low-risk first jobs).
- Proof: “Click before you hire” — both live demos + portfolio.
- Tone: calm expert. Short sentences. No “Dear client,” no “I would be honored,” no “passionate ninja.”

GOAL
Maximize probability of landing the FIRST paid Upwork job within 24 HOURS of starting active search (first interview invite or contract), not “get rich.”

CONSTRAINTS
- Upwork Basic: ~10 free Connects/month — treat Connects as scarce; only bid on high-fit jobs.
- New profile: compete on speed, clarity, live demos, and narrow scope — NOT on years of experience.
- Do not mention Fiverr, Payoneer, or Turkey tax in client-facing copy.

TASK A — JOB FILTER CHECKLIST (output as a scannable checklist I use before spending Connects)
Score each job 0–2 per row; recommend APPLY only if total ≥ 14/20. List red flags that mean SKIP even if cheap Connects.

Include rows for:
- Posted within last 24 hours (or “Interviewing” with <5 proposals)
- Client payment verified + hire rate reasonable
- Budget fits ($30–500 fixed or $15–45/hr for small tasks)
- Job type matches one of the 3 services (WordPress fix / landing / sheets)
- Clear deliverable (URL, bug description, or sheet sample) — not vague “build my startup”
- Low competition signal (few proposals OR client actively interviewing)
- English communication
- No “unlimited revisions” / full e-commerce / 20-page site for $50

TASK B — DAILY 24-HOUR SPRINT ROUTINE (time-boxed, total ~2 hours)
Give minute-by-minute blocks for:
- Job search filters (keywords + saved searches)
- How many proposals max per day with 10 Connects
- When to boost “Available now” (tradeoff)
- Speed: reply to client messages within 15 minutes during US morning + UK afternoon overlap
- What to do if zero invites after 8 proposals (pivot job type, not quit)

TASK C — PROPOSAL SYSTEM
1) One master template ≤ 120 words for WordPress fix jobs
2) One master template ≤ 120 words for landing page jobs
3) One master template ≤ 90 words for Excel/Sheets jobs

Each template MUST include:
- One sentence proving I read the post (reference their URL/business/problem)
- One bullet with demo link relevant to their niche (HVAC vs plumbing vs generic local)
- Fixed scope + price anchor from floor prices + delivery time
- One clarifying question
- Sign-off with first name only

TASK D — CUSTOM PROPOSAL FOR THIS JOB (if I paste a job below)
If no job pasted, show a realistic EXAMPLE job (WordPress speed fix, $80 budget, US HVAC company) and write the full customized proposal.

Rules for customized proposal:
- 90–150 words
- No attachments promised I don’t have
- Offer a 10-minute Loom or screenshot plan only if job is landing/fix
- Milestone suggestion: 100% on delivery for <$150 jobs

TASK E — PROFILE SNIPPETS (for Upwork UI)
- 2-line “Invite to interview” boost text
- 1-line answer to “Why should we hire you with no reviews?”

TASK F — HONEST ODDS (short)
One paragraph: what actually moves probability for a zero-review profile in 24h vs what is luck. No fake “95% guarantee.”

OUTPUT LANGUAGE
- Checklists & strategy: Turkish (so I execute fast)
- All Upwork-ready proposal text: English only

JOB POST (optional — paste below this line in the chat, not inside this prompt block):
```

---

## İlgili kayıtlar

| Kaynak | Ne var |
|--------|--------|
| `docs/upwork-profile.md` | Profil metni (MSG 0 TASK çıktısı) |
| `docs/upwork-profile-fill-pack.md` | Catalog, fiyat, Connect notları |
| Agent bc-6116e863 | %85–90 / %96–97 çok kanallı plan; %95 = $100 hedefi |
| Agent bc-445266d8 | Profil + demo upgrade; silinen prompt yok |
