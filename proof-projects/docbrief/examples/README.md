# Examples

`meeting-notes.md` is a fictional set of steering-meeting minutes (about 570 words) with figures,
dates, decisions and action items. It is a good first document because you can check every
line of the brief against the source in a minute.

```
docbrief --dry-run meeting-notes.md        # size and cost, no API call
docbrief meeting-notes.md -o brief.md      # needs OPENAI_API_KEY or ANTHROPIC_API_KEY
```

Public documents that exercise the PDF and multi-chunk paths:

```
docbrief --dry-run https://arxiv.org/pdf/1706.03762           # 15-page paper, 4 chunks
docbrief https://arxiv.org/pdf/1706.03762 -o attention.md
docbrief https://en.wikipedia.org/wiki/Warehouse_management_system -o wms.md
```

Briefs are not committed here on purpose: model output changes between versions, and a
checked-in sample would go stale. Run one and read it against the source instead.
