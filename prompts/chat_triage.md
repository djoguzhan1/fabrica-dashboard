# Chat Triage (gemini-3.8-flash-low)

Classify latest CLIENT message. JSON only.

```json
{
  "stage": "first|interview|objection|offer|scope|red_flag",
  "primary_request": "what they want answered now",
  "objection_type": "price|call|hourly|test|competitor|silence|none",
  "must_answer_terms": [],
  "risk_flags": []
}
```

Scope rule: reply must close `primary_request` before any audit upsell (§7.1).
