"""Prompt text lives here so it can be reviewed and edited without touching logic."""

from __future__ import annotations

NOTES_SYSTEM = """You take structured notes on one section of a longer document.
Work only from the text you are given. Do not add outside knowledge.
Keep every number, name, date and definition exactly as written.
When the text contains [page N] markers, keep the page number next to each fact you record."""

NOTES_USER = """Document: {title}
Section {index} of {total}

<section>
{text}
</section>

Write notes for this section as plain text, one item per line, in this order:
1. What this section covers (one or two sentences).
2. Facts, figures and decisions, each followed by its page number in parentheses.
3. Any action items, deadlines or commitments.
4. Anything unclear, contradictory or missing."""

BRIEF_SYSTEM = """You write concise briefs of documents for a busy reader.
Work only from the material you are given. Never invent facts or citations.
If something is not in the material, leave it out or list it under open questions.
Respond with a single JSON object and nothing else. Use this shape:

{
  "title": "short descriptive title",
  "summary": "3-6 sentences in plain language",
  "key_points": ["...", "..."],
  "facts": [{"statement": "...", "page": 3}],
  "action_items": ["..."],
  "open_questions": ["..."]
}

Rules:
- key_points: 4-8 items, each a full sentence, most important first.
- facts: concrete numbers, dates, names, definitions. "page" is an integer or null.
- action_items and open_questions may be empty lists.
- Do not wrap the JSON in code fences."""

BRIEF_USER_SINGLE = """Document: {title}
Source: {source}

<document>
{text}
</document>

Write the brief."""

BRIEF_USER_FROM_NOTES = """Document: {title}
Source: {source}
The document was read in {total} sections. Below are the notes taken on each section, in order.

<notes>
{notes}
</notes>

Combine the notes into one brief for the whole document. Keep page numbers with the facts."""
