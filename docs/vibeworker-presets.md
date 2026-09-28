# Vibeworker filtre JSON’ları (yapıştırmaya hazır)

Kullanım: filtre ⚙️ → **View / edit as JSON** → **Edit** → kutudaki her şeyi sil → aşağıdaki bloğu yapıştır → **Done** → alanları kontrol et → **Save changes**.
Kategoriler JSON’da yok; her filtrede **CATEGORIES** satırından ayarla (DevOps kapalı, Web & Mobile Design varsa açık).
`job_type: null` = Both, `experience_level: null` = Any, `min_percentile: null` = AI match Any.
Bildirim: P1–P5 çan açık, P6 çan kapalı, Shortlist çanı P1–P5 hazır olunca kapalı.

Ayrıntı ve gerekçeler: `docs/upwork-vibeworker-pro-setup.md` Bölüm 5D.

## Shortlist (geniş akış)

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 20,
  "hide_unposted_budget": false,
  "connects_max": 12,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": [],
  "keywords_require": [],
  "keywords_exclude": ["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes"],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```

## P1 WP-Fix

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 30,
  "hide_unposted_budget": false,
  "connects_max": 12,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": ["wordpress","elementor","divi","wpbakery","white screen","critical error","plugin conflict","contact form","wpforms","contact form 7"],
  "keywords_require": [],
  "keywords_exclude": ["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes","custom plugin","plugin development","theme development","membership","lms","from scratch"],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```

## P2 Speed-Mobile

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 50,
  "hide_unposted_budget": false,
  "connects_max": 12,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": ["page speed","pagespeed","core web vitals","gtmetrix","lighthouse","site speed","slow website","load time","mobile responsive","mobile friendly","responsive fix"],
  "keywords_require": [],
  "keywords_exclude": ["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes","seo retainer","monthly seo"],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```

## P3 Landing-Local

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 80,
  "hide_unposted_budget": false,
  "connects_max": 12,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": ["landing page","one page","one-page","single page","small business website","simple website","hvac","plumbing","plumber","roofing","electrician","contractor","home services","cleaning","landscaping","google ads","lead generation"],
  "keywords_require": [],
  "keywords_exclude": ["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes"],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```

## P4 Sheets-Excel

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 25,
  "hide_unposted_budget": false,
  "connects_max": 8,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": ["google sheets","excel","spreadsheet","vlookup","xlookup","pivot table","conditional formatting","formula","dashboard","tracker","calculator"],
  "keywords_require": [],
  "keywords_exclude": ["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes","data entry","bookkeeping","power bi","tableau","financial model","vba"],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```

## P5 Small-Web

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 20,
  "hide_unposted_budget": false,
  "connects_max": 8,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": ["quick fix","small fix","small change","small task","html css","css fix","figma to html","psd to html","migrate","migration","dns","ssl","hosting","github pages","netlify","ga4","google tag manager","pixel","calendly","booking widget"],
  "keywords_require": [],
  "keywords_exclude": ["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes"],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```

## P6 Scripts-AI (çan kapalı)

```json
{
  "job_type": null,
  "experience_level": null,
  "budget_min": 0,
  "budget_min_hourly": 15,
  "budget_min_fixed": 40,
  "hide_unposted_budget": false,
  "connects_max": 12,
  "require_payment_verified": true,
  "min_client_rating": 4.5,
  "min_client_spent": 500,
  "min_hire_rate": 30,
  "min_hires": null,
  "keywords_include": ["python","apps script","google apps script","automation","automate","csv","pdf","openai","chatgpt","claude","api integration","webhook","zapier","n8n","make.com","scrape","scraping"],
  "keywords_require": [],
  "keywords_exclude": ["woocommerce","shopify","react","next.js","nextjs","vue","angular","react native","flutter","mobile app","ios app","android app","fullstack","full stack","full-stack","blockchain","crypto","nft","web3","trading bot","homework","thesis","unpaid","free test","test task","telegram only","outside upwork","us citizen","us person","security clearance","senior developer","senior engineer","lottery","casino","betting","gambling","power apps","power automate","mentor","mentorship","devops","terraform","ansible","kubernetes","linkedin","instagram","facebook","captcha","machine learning model","fine-tune","fine-tuning","computer vision"],
  "exclude_locations": [],
  "min_percentile": null,
  "posted_within_hours": 24
}
```
