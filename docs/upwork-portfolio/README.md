# Upwork portfolio pack

Six portfolio items, ready to paste. Each folder holds the images in upload order
(`01-cover` becomes the thumbnail). All images are 1600×1200 PNG unless noted; the
`full-page` JPEGs are long scrolling captures for the last slot.

Upwork limits (as of writing): title 70 characters, description 600 characters,
up to 5 skills, up to 10 images per project, 10 MB per image. Every text below fits.

Order of adding on Upwork: **1 HVAC, 2 Plumbing, 3 tidycsv, 4 docbrief, 5 sheet-notify, 6 Hub.**
The first two show on the profile card; put the strongest visual first.

Before adding items 3–5, publish the three repos (see `proof-projects/README.md`) so
the project URLs resolve.

---

## 1. CoolAir HVAC — same-day repair landing page (demo)

**Folder:** `hvac/` · **Images:** `01` cover → `02` services → `03` specials → `04` reviews → `05` booking form → `06` FAQ → `07` full page
**Project URL:** https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/
**Role:** Design and front-end development
**Skills:** Landing Page, HTML5, CSS 3, JavaScript, Web Design

**Description (574 chars):**

> One-page site for a fictional Dallas–Fort Worth HVAC company, built to show what a service-business landing page should do: get the call. Live status bar (open / emergency line), click-to-call in the header and a fixed mobile call bar, flat-rate service tiles, seasonal specials, review cards, service-area ZIP checker, booking form with time slots, FAQ accordion. Hand-written HTML/CSS/JS, no page builder, self-hosted fonts, WebP/AVIF photos, LocalBusiness schema. Lighthouse (mobile): 99 performance, 100 accessibility, 100 best practices, 100 SEO. Open it on your phone.

---

## 2. ProFix Plumbing — 24/7 emergency plumber landing page (demo)

**Folder:** `plumbing/` · **Images:** `01` cover → `02` services → `03` pricing → `04` recent work → `05` reviews → `06` FAQ → `07` full page
**Project URL:** https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/
**Role:** Design and front-end development
**Skills:** Landing Page, HTML5, CSS 3, Responsive Design, Web Design

**Description (584 chars):**

> Emergency-first landing page for a fictional Phoenix plumbing company. The design starts from the situation a caller is in at 2 AM: red on-call bar with a live clock and average arrival time, one-tap call and "text us a photo" buttons, a three-field quick-request form above the fold. Below it: fixed-price service tiles, a sample estimate showing how pricing is explained, three recent jobs with photos, reviews, service-area ZIP check, FAQ. Distinct design from the HVAC demo, not a colour swap. Hand-written HTML/CSS/JS, no dependencies. Lighthouse (mobile): 100 / 100 / 100 / 100.

---

## 3. tidycsv — messy CSV to a clean Excel report

**Folder:** `tidycsv/` · **Images:** `01` cover → `02` Summary sheet → `03` Data sheet
**Project URL:** https://github.com/djoguzhan1/tidycsv
**Role:** Developer (Python)
**Skills:** Python, pandas, Data Cleaning, Microsoft Excel, Automation

**Description (576 chars):**

> Command-line tool that takes an export nobody wants to open — inconsistent headers, "N/A" and "-" placeholders, dates in four formats, "$1,386.10" next to "(45.00)" and "2.500,00", Shipped/shipped/SHIPPED, blank and duplicate rows — and writes an Excel workbook in one command. Data sheet as a proper Excel table with frozen header and number/date formats; Summary sheet with per-column stats, totals by category and a bar chart; Changes sheet listing every transformation with counts, so nothing happens silently. IDs and ZIPs stay text. pandas + openpyxl, 27 tests, CI, MIT.

---

## 4. docbrief — page-referenced briefs from PDFs and web pages

**Folder:** `docbrief/` · **Images:** `01` cover
**Project URL:** https://github.com/djoguzhan1/docbrief
**Role:** Developer (Python, LLM integration)
**Skills:** Python, OpenAI API, Anthropic Claude, Prompt Engineering, Automation

**Description (596 chars):**

> CLI that turns a PDF, text file or URL into a structured brief: summary, key points, facts with the page number they came from, action items and open questions — as Markdown or JSON. Long documents are split into page-aware sections, summarised into notes, then combined (map-reduce), so a 15-page paper costs a few tenths of a cent. `--dry-run` shows size, chunking and estimated cost before a single API call. Works with OpenAI or Anthropic; keys are read from the environment only and never logged. Prompts are plain text files, easy to adapt to a client's template. 19 offline tests, CI, MIT.

---

## 5. sheet-notify — email and Slack alerts for new Google Sheet rows

**Folder:** `sheet-notify/` · **Images:** `01` cover
**Project URL:** https://github.com/djoguzhan1/sheet-notify
**Role:** Developer (Google Apps Script)
**Skills:** Google Apps Script, Google Sheets, Slack, Email Automation, Automation

**Description (584 chars):**

> Google Apps Script that sends an email and/or a Slack message whenever a new row lands in a sheet — form responses, Zapier/Make pushes or manual entry. No add-on, no monthly fee; it runs inside the spreadsheet on the owner's account. Everything is configured in a Settings tab (recipients, webhook, subject template with {{Column}} placeholders, columns to include). Each row is delivered exactly once: a script lock prevents overlapping runs and a Notified column stores the timestamp or the error, so retries and bulk pastes cannot double-send. Pure helpers are unit-tested in Node.

---

## 6. Portfolio hub — landing pages and fixes for local service businesses

**Folder:** `hub/` · **Images:** `01` cover → `02` full page
**Project URL:** https://djoguzhan1.github.io/web-dev-portfolio/
**Role:** Design and development
**Skills:** Web Development, HTML5, CSS 3, Web Design, SEO

**Description (469 chars):**

> My own one-page site: what I build, how a project runs (scope and fixed quote first, first draft in 48 hours, replies within an hour during working hours), the two live demos with their Lighthouse scores, and a short FAQ. Same standards as the demos: hand-written HTML/CSS, self-hosted fonts, responsive images, no page builder, Lighthouse 99–100 on mobile and desktop. Included here because it is the fastest way to see how I present work and communicate with clients.

---

## Wording rules used above

- Demos are labelled as fictional companies. No client names, no invented results.
- Lighthouse numbers are the ones shown on the hub page and reproducible with Lighthouse 12, mobile preset.
- Test counts and Python versions match the repos' CI at the time of writing; update the text if the repos change.
