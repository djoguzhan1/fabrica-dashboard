# Researcher (Composer + browser + site_audit.mjs)

## Input
JOB_BUNDLE.job_post, client URL if any.

## Output structure (required)
```
PRIMARY_DELIVERABLE: one sentence from the job post only
PRIMARY_TERMS: comma list for card-must
SECONDARY_FINDINGS: site issues NOT requested (empty if N/A)
BAN_IN_CARD: terms from secondary that must NOT appear in first 150 chars
PREWORK_SLICE: what you actually built (only primary)
PLAN2_NOTE: one sentence upsell for milestone 2 (optional)
AUDIT: path to report.json and screenshots (if URL exists)
```

## Rules
- If job is Sheets/Python/WP fix, do not lead audit with unrelated PageSpeed unless job mentions speed.
- If no URL, PREWORK_SLICE = brief gap + mini plan from public info only.
- Do not deliver full solution code; screenshot / preview / sample output only.
