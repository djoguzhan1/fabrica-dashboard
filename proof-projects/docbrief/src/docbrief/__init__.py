"""docbrief - structured briefs of PDFs, text files and web pages."""

__version__ = "0.1.0"

from .brief import Brief, Fact, render_markdown, summarize  # noqa: E402
from .extract import Document, load  # noqa: E402

__all__ = ["Brief", "Document", "Fact", "__version__", "load", "render_markdown", "summarize"]
