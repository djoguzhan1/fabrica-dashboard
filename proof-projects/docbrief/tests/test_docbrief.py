import json
from pathlib import Path

import pytest

from docbrief import cli
from docbrief.brief import estimate, parse_brief, render_markdown, summarize
from docbrief.chunk import split
from docbrief.extract import Document, Page, from_html, from_text_file, load
from docbrief.providers import FakeProvider

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"

BRIEF_JSON = json.dumps(
    {
        "title": "Scanner rollout",
        "summary": "The pilot worked. Option B was chosen.",
        "key_points": ["Accuracy rose to 99.4%.", "Battery life is 8.5 hours."],
        "facts": [{"statement": "Pilot cost £14,200", "page": 1}, {"statement": "112 pickers", "page": None}],
        "action_items": ["Send comparison by 21 March"],
        "open_questions": ["Swansea Wi-Fi coverage"],
    }
)


# --- extract -----------------------------------------------------------------


def test_text_file_uses_first_heading_as_title():
    doc = from_text_file(EXAMPLES / "meeting-notes.md")
    assert doc.title.startswith("Warehouse Scanner Rollout")
    assert doc.words > 500
    assert len(doc.pages) == 1


def test_html_drops_navigation_and_scripts():
    html = """
    <html><head><title>Ignored</title><script>var x = 1;</script></head>
    <body><nav><a href="/">Home</a></nav>
    <article><h1>Refund policy</h1><p>Refunds are issued within 14 days.</p>
    <ul><li>Keep your receipt.</li></ul></article>
    <footer>© Example</footer></body></html>"""
    doc = from_html(html, "https://example.com/refunds")
    assert doc.title == "Refund policy"
    assert "14 days" in doc.text
    assert "Home" not in doc.text
    assert "var x" not in doc.text
    assert "Example" not in doc.text


def test_load_rejects_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load(str(tmp_path / "nope.pdf"))


def test_empty_text_file_is_an_error(tmp_path):
    empty = tmp_path / "empty.txt"
    empty.write_text("\n\n")
    with pytest.raises(ValueError):
        load(str(empty))


# --- chunk -------------------------------------------------------------------


def _doc(pages: list[str]) -> Document:
    return Document("test", "Test", [Page(i + 1, text) for i, text in enumerate(pages)])


def test_small_document_is_a_single_chunk():
    chunks = split(_doc(["alpha " * 50, "beta " * 50]), max_chars=5000)
    assert len(chunks) == 1
    assert chunks[0].pages == [1, 2]
    assert "[page 1]" in chunks[0].text and "[page 2]" in chunks[0].text


def test_chunks_respect_limit_and_keep_page_numbers():
    long_page = ("Sentence number one is here. " * 40).strip()
    chunks = split(_doc([long_page, long_page, long_page]), max_chars=900)
    assert len(chunks) > 3
    assert all(len(chunk.text) <= 900 for chunk in chunks)
    assert chunks[0].pages == [1]
    assert chunks[-1].pages == [3]
    assert chunks[0].page_label == "p. 1"


def test_page_label_for_range():
    chunks = split(_doc(["a" * 10, "b" * 10, "c" * 10]), max_chars=5000)
    assert chunks[0].page_label == "pp. 1–3"


# --- brief -------------------------------------------------------------------


def test_parse_brief_tolerates_code_fences():
    doc = _doc(["text"])
    brief = parse_brief(f"```json\n{BRIEF_JSON}\n```", doc)
    assert brief.title == "Scanner rollout"
    assert brief.facts[0].page == 1
    assert brief.facts[1].page is None
    assert brief.words == doc.words


def test_parse_brief_extracts_object_from_prose():
    brief = parse_brief(f"Here you go:\n{BRIEF_JSON}\nHope that helps.", _doc(["text"]))
    assert brief.key_points[0].startswith("Accuracy")


def test_parse_brief_fails_loudly_without_json():
    with pytest.raises(ValueError):
        parse_brief("I cannot do that.", _doc(["text"]))


def test_single_chunk_makes_one_call():
    provider = FakeProvider(responses=[BRIEF_JSON])
    brief = summarize(_doc(["short text"]), provider)
    assert provider.usage.calls == 1
    assert brief.chunks == 1
    assert brief.model == "fake-model"
    assert "short text" in provider.prompts[0][1]


def test_long_document_uses_notes_then_final_call():
    pages = [f"Paragraph about topic {i}. " * 60 for i in range(6)]
    provider = FakeProvider(responses=["notes 1", "notes 2", "notes 3", "notes 4", "notes 5", "notes 6", BRIEF_JSON])
    brief = summarize(_doc(pages), provider, max_chunk_chars=1600)
    assert brief.chunks == provider.usage.calls - 1 >= 2
    final_system, final_user = provider.prompts[-1]
    assert "notes 1" in final_user and f"notes {brief.chunks}" in final_user
    assert "JSON" in final_system


def test_render_markdown_sections():
    brief = parse_brief(BRIEF_JSON, Document("memo.md", "Memo", [Page(1, "x")]))
    brief.model = "fake-model"
    md = render_markdown(brief)
    assert md.startswith("# Scanner rollout\n")
    assert "## Key points" in md
    assert "- Pilot cost £14,200 (p. 1)" in md
    assert "- 112 pickers\n" in md
    assert "- [ ] Send comparison by 21 March" in md
    assert "## Open questions" in md


def test_estimate_costs_nothing_and_scales_with_chunks():
    doc = from_text_file(EXAMPLES / "meeting-notes.md")
    small = estimate(doc, max_chunk_chars=20_000)
    many = estimate(doc, max_chunk_chars=1_000)
    assert small.calls == 1
    assert many.calls == len(many.chunks) + 1 > 2
    assert many.input_tokens > small.input_tokens
    assert small.cost("gpt-4o-mini") is not None
    assert small.cost("unknown-model") is None


# --- cli ---------------------------------------------------------------------


def test_cli_dry_run(capsys):
    code = cli.main(["--dry-run", str(EXAMPLES / "meeting-notes.md")])
    out = capsys.readouterr().out
    assert code == 0
    assert "Warehouse Scanner Rollout" in out
    assert "1 API call(s)" in out
    assert "openai/gpt-4o-mini" in out


def test_cli_without_key_exits_2(monkeypatch, capsys):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("DOCBRIEF_PROVIDER", raising=False)
    code = cli.main([str(EXAMPLES / "meeting-notes.md")])
    assert code == 2
    assert "OPENAI_API_KEY" in capsys.readouterr().err


def test_cli_writes_markdown_with_fake_provider(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "get_provider", lambda *_: FakeProvider(responses=[BRIEF_JSON]))
    target = tmp_path / "brief.md"
    code = cli.main([str(EXAMPLES / "meeting-notes.md"), "-o", str(target)])
    assert code == 0
    assert target.read_text().startswith("# Scanner rollout")


def test_cli_json_output(monkeypatch, capsys):
    monkeypatch.setattr(cli, "get_provider", lambda *_: FakeProvider(responses=[BRIEF_JSON]))
    code = cli.main([str(EXAMPLES / "meeting-notes.md"), "--json"])
    assert code == 0
    data = json.loads(capsys.readouterr().out)
    assert data["facts"][0] == {"statement": "Pilot cost £14,200", "page": 1}


def test_guess_title_prefers_capitalised_short_line():
    from docbrief.extract import _guess_title

    page = "Provided proper attribution is provided, Google hereby grants permission to\nscholarly works.\n"
    page += "Attention Is All You Need\nAshish Vaswani\nGoogle Brain\n"
    assert _guess_title(page) == "Attention Is All You Need"
    assert _guess_title("just some lowercase prose that goes on and on\n") is None
