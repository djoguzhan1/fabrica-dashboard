"""Map-reduce summarisation: notes per chunk, then one brief from the notes."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field

from . import prompts
from .chunk import DEFAULT_MAX_CHARS, Chunk, split
from .extract import Document
from .providers import PRICE_PER_MTOK, Provider, estimate_tokens

_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


@dataclass
class Fact:
    statement: str
    page: int | None = None


@dataclass
class Brief:
    title: str
    summary: str
    key_points: list[str] = field(default_factory=list)
    facts: list[Fact] = field(default_factory=list)
    action_items: list[str] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)
    source: str = ""
    words: int = 0
    chunks: int = 0
    model: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


def _extract_json(text: str) -> dict:
    """Accept the JSON object even if the model wrapped it in fences or prose."""
    cleaned = _FENCE_RE.sub("", text.strip()).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        start, end = cleaned.find("{"), cleaned.rfind("}")
        if start == -1 or end <= start:
            raise ValueError("model did not return a JSON object") from None
        return json.loads(cleaned[start : end + 1])


def _as_str_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def _as_facts(value: object) -> list[Fact]:
    facts: list[Fact] = []
    if not isinstance(value, list):
        return facts
    for item in value:
        if isinstance(item, dict) and item.get("statement"):
            page = item.get("page")
            try:
                page_number = int(page) if page is not None else None
            except (TypeError, ValueError):
                page_number = None
            facts.append(Fact(str(item["statement"]).strip(), page_number))
        elif isinstance(item, str) and item.strip():
            facts.append(Fact(item.strip()))
    return facts


def parse_brief(raw: str, document: Document) -> Brief:
    data = _extract_json(raw)
    return Brief(
        title=str(data.get("title") or document.title).strip(),
        summary=str(data.get("summary") or "").strip(),
        key_points=_as_str_list(data.get("key_points")),
        facts=_as_facts(data.get("facts")),
        action_items=_as_str_list(data.get("action_items")),
        open_questions=_as_str_list(data.get("open_questions")),
        source=document.source,
        words=document.words,
    )


def summarize(document: Document, provider: Provider, max_chunk_chars: int = DEFAULT_MAX_CHARS) -> Brief:
    chunks = split(document, max_chunk_chars)
    if len(chunks) == 1:
        raw = provider.complete(
            prompts.BRIEF_SYSTEM,
            prompts.BRIEF_USER_SINGLE.format(title=document.title, source=document.source, text=chunks[0].text),
            max_tokens=2000,
        )
    else:
        notes = []
        for chunk in chunks:
            note = provider.complete(
                prompts.NOTES_SYSTEM,
                prompts.NOTES_USER.format(
                    title=document.title, index=chunk.index + 1, total=len(chunks), text=chunk.text
                ),
                max_tokens=1200,
            )
            notes.append(f"## Section {chunk.index + 1} ({chunk.page_label})\n{note.strip()}")
        raw = provider.complete(
            prompts.BRIEF_SYSTEM,
            prompts.BRIEF_USER_FROM_NOTES.format(
                title=document.title, source=document.source, total=len(chunks), notes="\n\n".join(notes)
            ),
            max_tokens=2000,
        )
    brief = parse_brief(raw, document)
    brief.chunks = len(chunks)
    brief.model = provider.model
    return brief


def render_markdown(brief: Brief) -> str:
    lines = [f"# {brief.title}", ""]
    if brief.source:
        lines += [f"*Source: {brief.source} · {brief.words:,} words · {brief.model}*", ""]
    if brief.summary:
        lines += ["## Summary", "", brief.summary, ""]
    if brief.key_points:
        lines += ["## Key points", ""] + [f"- {point}" for point in brief.key_points] + [""]
    if brief.facts:
        lines += ["## Facts and figures", ""]
        for fact in brief.facts:
            suffix = f" (p. {fact.page})" if fact.page is not None else ""
            lines.append(f"- {fact.statement}{suffix}")
        lines.append("")
    if brief.action_items:
        lines += ["## Action items", ""] + [f"- [ ] {item}" for item in brief.action_items] + [""]
    if brief.open_questions:
        lines += ["## Open questions", ""] + [f"- {item}" for item in brief.open_questions] + [""]
    return "\n".join(lines).rstrip() + "\n"


@dataclass
class Estimate:
    chunks: list[Chunk]
    calls: int
    input_tokens: int
    output_tokens: int

    def cost(self, model: str) -> float | None:
        prices = PRICE_PER_MTOK.get(model)
        if prices is None:
            return None
        return (self.input_tokens * prices[0] + self.output_tokens * prices[1]) / 1_000_000


def estimate(document: Document, max_chunk_chars: int = DEFAULT_MAX_CHARS) -> Estimate:
    """What a run would cost, without calling any API."""
    chunks = split(document, max_chunk_chars)
    prompt_overhead = estimate_tokens(prompts.NOTES_SYSTEM + prompts.NOTES_USER)
    if len(chunks) == 1:
        input_tokens = estimate_tokens(prompts.BRIEF_SYSTEM + prompts.BRIEF_USER_SINGLE + chunks[0].text)
        return Estimate(chunks, calls=1, input_tokens=input_tokens, output_tokens=900)
    notes_in = sum(estimate_tokens(chunk.text) + prompt_overhead for chunk in chunks)
    notes_out = 350 * len(chunks)
    final_in = estimate_tokens(prompts.BRIEF_SYSTEM + prompts.BRIEF_USER_FROM_NOTES) + notes_out
    return Estimate(chunks, calls=len(chunks) + 1, input_tokens=notes_in + final_in, output_tokens=notes_out + 900)
