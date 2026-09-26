"""Split a document into model-sized chunks without losing page numbers."""

from __future__ import annotations

from dataclasses import dataclass

from .extract import Document

DEFAULT_MAX_CHARS = 12_000  # ~3k tokens; comfortable for every current model


@dataclass
class Chunk:
    index: int
    text: str
    pages: list[int]

    @property
    def page_label(self) -> str:
        if not self.pages:
            return ""
        if len(self.pages) == 1:
            return f"p. {self.pages[0]}"
        return f"pp. {self.pages[0]}–{self.pages[-1]}"


def _split_long_text(text: str, max_chars: int) -> list[str]:
    """Split on paragraph, then sentence boundaries; hard-cut only as a last resort."""
    if len(text) <= max_chars:
        return [text]
    parts: list[str] = []
    current = ""
    for paragraph in text.split("\n\n"):
        candidate = f"{current}\n\n{paragraph}" if current else paragraph
        if len(candidate) <= max_chars:
            current = candidate
            continue
        if current:
            parts.append(current)
            current = ""
        if len(paragraph) <= max_chars:
            current = paragraph
            continue
        sentence_buffer = ""
        for sentence in paragraph.replace(". ", ".\n").split("\n"):
            candidate = f"{sentence_buffer} {sentence}".strip()
            if len(candidate) <= max_chars:
                sentence_buffer = candidate
            else:
                if sentence_buffer:
                    parts.append(sentence_buffer)
                while len(sentence) > max_chars:
                    parts.append(sentence[:max_chars])
                    sentence = sentence[max_chars:]
                sentence_buffer = sentence
        current = sentence_buffer
    if current:
        parts.append(current)
    return parts


def split(document: Document, max_chars: int = DEFAULT_MAX_CHARS) -> list[Chunk]:
    chunks: list[Chunk] = []
    buffer = ""
    buffer_pages: list[int] = []

    def flush() -> None:
        nonlocal buffer, buffer_pages
        if buffer.strip():
            chunks.append(Chunk(len(chunks), buffer.strip(), sorted(set(buffer_pages))))
        buffer, buffer_pages = "", []

    for page in document.pages:
        marker = f"[page {page.number}]\n"
        for piece in _split_long_text(page.text, max_chars - len(marker)):
            addition = marker + piece
            if buffer and len(buffer) + len(addition) + 2 > max_chars:
                flush()
            buffer = f"{buffer}\n\n{addition}" if buffer else addition
            buffer_pages.append(page.number)
    flush()
    return chunks
