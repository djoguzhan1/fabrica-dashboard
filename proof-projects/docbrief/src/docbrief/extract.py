"""Turn a PDF, a text file or a web page into plain text with page numbers."""

from __future__ import annotations

import io
import re
from dataclasses import dataclass, field
from pathlib import Path

USER_AGENT = "docbrief/0.1 (+https://github.com/djoguzhan1/docbrief)"
_WS_RE = re.compile(r"[ \t\u00a0]+")
_BLANK_LINES_RE = re.compile(r"\n{3,}")


@dataclass
class Page:
    number: int
    text: str


@dataclass
class Document:
    source: str
    title: str
    pages: list[Page] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n\n".join(p.text for p in self.pages)

    @property
    def words(self) -> int:
        return sum(len(p.text.split()) for p in self.pages)


def tidy(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _WS_RE.sub(" ", text)
    text = "\n".join(line.strip() for line in text.split("\n"))
    return _BLANK_LINES_RE.sub("\n\n", text).strip()


def from_pdf_bytes(data: bytes, source: str) -> Document:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    title = None
    if reader.metadata and reader.metadata.title:
        title = str(reader.metadata.title).strip() or None
    pages = []
    for index, page in enumerate(reader.pages, start=1):
        text = tidy(page.extract_text() or "")
        if text:
            pages.append(Page(index, text))
    if not pages:
        raise ValueError(f"{source}: no extractable text (scanned PDF? run OCR first)")
    return Document(source=source, title=title or _guess_title(pages[0].text) or Path(source).name, pages=pages)


def _guess_title(first_page: str) -> str | None:
    """Pick the most title-like line near the top: short, several words, mostly capitalised."""
    best, best_score = None, 0.0
    for line in first_page.split("\n")[:10]:
        words = line.split()
        if not 2 <= len(words) <= 14 or len(line) > 100:
            continue
        score = sum(word[0].isupper() for word in words) / len(words)
        if score > best_score:
            best, best_score = line.strip(), score
    return best if best_score >= 0.6 else None


def from_html(html: str, source: str) -> Document:
    from selectolax.parser import HTMLParser

    tree = HTMLParser(html)
    for selector in ("script", "style", "noscript", "nav", "header", "footer", "aside", "form", "iframe", "svg"):
        for node in tree.css(selector):
            node.decompose()

    title_node = tree.css_first("title")
    h1 = tree.css_first("h1")
    title = (h1.text(strip=True) if h1 else "") or (title_node.text(strip=True) if title_node else "") or source

    main = tree.css_first("article") or tree.css_first("main") or tree.css_first("[role=main]") or tree.body
    if main is None:
        raise ValueError(f"{source}: empty page")

    blocks: list[str] = []
    for node in main.css("h1, h2, h3, h4, p, li, blockquote, pre, td, th, figcaption"):
        text = node.text(separator=" ", strip=True)
        if text:
            blocks.append(text)
    text = tidy("\n\n".join(blocks)) if blocks else tidy(main.text(separator="\n", strip=True))
    if not text:
        raise ValueError(f"{source}: no readable text")
    return Document(source=source, title=title, pages=[Page(1, text)])


def from_url(url: str, timeout: float = 30.0) -> Document:
    import httpx

    response = httpx.get(url, follow_redirects=True, timeout=timeout, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    content_type = response.headers.get("content-type", "").lower()
    if "pdf" in content_type or url.lower().endswith(".pdf"):
        return from_pdf_bytes(response.content, url)
    return from_html(response.text, url)


def from_text_file(path: Path) -> Document:
    text = tidy(path.read_text(encoding="utf-8", errors="replace"))
    if not text:
        raise ValueError(f"{path}: file is empty")
    first_line = text.split("\n", 1)[0].lstrip("# ").strip()
    title = first_line if len(first_line) <= 120 else path.stem
    return Document(source=str(path), title=title, pages=[Page(1, text)])


def load(source: str) -> Document:
    """Load a PDF/TXT/MD path or an http(s) URL."""
    if source.startswith(("http://", "https://")):
        return from_url(source)
    path = Path(source)
    if not path.exists():
        raise FileNotFoundError(source)
    if path.suffix.lower() == ".pdf":
        return from_pdf_bytes(path.read_bytes(), str(path))
    if path.suffix.lower() in (".html", ".htm"):
        return from_html(path.read_text(encoding="utf-8", errors="replace"), str(path))
    return from_text_file(path)
