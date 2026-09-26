# docbrief

Turn a PDF, a text file or a web page into a one-page brief: summary, key points, facts with page numbers, action items and open questions. Works with OpenAI or Anthropic models; long documents are read in sections and combined.

```
docbrief quarterly-report.pdf -o brief.md
docbrief https://example.com/terms --provider anthropic
docbrief notes/*.md -o briefs/
```

Before spending anything, see what a run would cost:

```
$ docbrief --dry-run https://arxiv.org/pdf/1706.03762
Attention Is All You Need
  source   https://arxiv.org/pdf/1706.03762
  size     15 page(s), 6,022 words, ~12,232 input tokens
  chunks   4 × ≤12,000 chars → 5 API call(s)
  model    openai/gpt-4o-mini
  cost     ~$0.0032 (estimate, before any call is made)
```

## What you get

One Markdown file (or JSON with `--json`) in this shape:

```markdown
# <title>

*Source: report.pdf · 6,022 words · gpt-4o-mini*

## Summary
3–6 sentences in plain language.

## Key points
- 4–8 sentences, most important first.

## Facts and figures
- Concrete numbers, dates, names, definitions, each with (p. N) where the model found it.

## Action items
- [ ] Deadlines, commitments, next steps mentioned in the text.

## Open questions
- Things the document leaves unclear or contradicts itself on.
```

The prompts tell the model to work only from the supplied text and to leave things out rather than guess. Page markers are kept through chunking so the page references in *Facts and figures* point at real pages. That reduces invented content; it does not eliminate it. Read the brief before you forward it.

## How it works

1. **Extract** – `pypdf` for PDFs (per page), `selectolax` for HTML (drops nav, footer, scripts, forms; keeps article/main), plain read for `.txt`/`.md`. URLs are fetched with `httpx`; a URL that serves a PDF is handled as a PDF.
2. **Chunk** – text is split into sections of at most `--max-chunk-chars` (default 12,000 ≈ 3k tokens), on paragraph then sentence boundaries, each carrying its `[page N]` markers.
3. **Brief** – a single-chunk document gets one call. Longer documents get one *notes* call per section and one final call that combines the notes into the JSON brief (map-reduce). Malformed JSON is tolerated where possible and reported otherwise.
4. **Report** – token usage and an approximate cost are printed to stderr after the run.

Scanned PDFs have no text layer; run OCR first (e.g. `ocrmypdf`) or you will get a clear error instead of an empty brief.

## Install

Python 3.10 or newer.

```
pip install "docbrief[openai] @ git+https://github.com/djoguzhan1/docbrief"
# or
pip install "docbrief[anthropic] @ git+https://github.com/djoguzhan1/docbrief"
```

Set a key in your environment (or copy `.env.example` to `.env` and load it):

```
export OPENAI_API_KEY=sk-...
# or
export ANTHROPIC_API_KEY=sk-ant-...
export DOCBRIEF_PROVIDER=anthropic
```

Keys are read from the environment only and are never written to disk or logs by this tool.

## Usage

```
docbrief SOURCE [SOURCE ...] [options]

  -o, --out PATH          write Markdown to this file (one source) or into this directory (several)
  --json                  print JSON instead of Markdown
  --provider {openai,anthropic}
  --model NAME            override the default model
  --max-chunk-chars N     section size per request (default 12000)
  --dry-run               size, chunking and cost estimate; makes no API calls
```

Default models are `gpt-4o-mini` and `claude-3-5-haiku-latest`. Model names change; if your account has newer ones, pass `--model` or set `DOCBRIEF_MODEL`. Prices in `providers.py` are approximate list prices used only for the estimate.

From Python:

```python
from docbrief import load, summarize, render_markdown
from docbrief.providers import get_provider

doc = load("contract.pdf")
brief = summarize(doc, get_provider("openai"))
print(brief.summary)
for fact in brief.facts:
    print(fact.page, fact.statement)
open("brief.md", "w").write(render_markdown(brief))
```

## Changing the prompts

They are plain strings in `src/docbrief/prompts.py`. Common edits: a different language for the output, a fixed set of headings for a report template, or a stricter rule about what counts as a fact. Nothing else needs to change.

## Development

```
pip install -e ".[dev]"
ruff check .
pytest
docbrief --dry-run examples/meeting-notes.md
```

Tests use a fake provider, so they run offline and cost nothing. `examples/meeting-notes.md` is a fictional set of meeting minutes with numbers, dates and action items, useful for a first real run.

## License

MIT © 2026 Oğuzhan Salatan
