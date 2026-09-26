"""Command-line entry point."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .brief import estimate, render_markdown, summarize
from .chunk import DEFAULT_MAX_CHARS
from .extract import load
from .providers import DEFAULT_MODELS, get_provider


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="docbrief",
        description="Summarise PDFs, text files and web pages into a structured brief.",
    )
    parser.add_argument("sources", nargs="+", metavar="SOURCE", help="PDF/TXT/MD/HTML path or http(s) URL")
    parser.add_argument("-o", "--out", type=Path, help="write Markdown here (one file: exact path; several: directory)")
    parser.add_argument("--json", action="store_true", help="print the brief as JSON instead of Markdown")
    parser.add_argument("--provider", choices=sorted(DEFAULT_MODELS), help="default: $DOCBRIEF_PROVIDER or openai")
    parser.add_argument("--model", help="override the provider's default model ($DOCBRIEF_MODEL)")
    parser.add_argument(
        "--max-chunk-chars",
        type=int,
        default=DEFAULT_MAX_CHARS,
        help=f"section size sent per request (default {DEFAULT_MAX_CHARS})",
    )
    parser.add_argument("--dry-run", action="store_true", help="show size, chunking and cost estimate; no API calls")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def _print_dry_run(source: str, args: argparse.Namespace) -> None:
    document = load(source)
    est = estimate(document, args.max_chunk_chars)
    provider_name = args.provider or "openai"
    model = args.model or DEFAULT_MODELS[provider_name]
    print(f"{document.title}")
    print(f"  source   {document.source}")
    print(f"  size     {len(document.pages)} page(s), {document.words:,} words, ~{est.input_tokens:,} input tokens")
    print(f"  chunks   {len(est.chunks)} × ≤{args.max_chunk_chars:,} chars → {est.calls} API call(s)")
    cost = est.cost(model)
    cost_text = f"~${cost:.4f}" if cost is not None else "unknown (model not in price table)"
    print(f"  model    {provider_name}/{model}")
    print(f"  cost     {cost_text} (estimate, before any call is made)")


def _output_path(args: argparse.Namespace, source: str, count: int) -> Path | None:
    if args.out is None:
        return None
    if count == 1 and args.out.suffix:
        return args.out
    stem = Path(source.rstrip("/").split("/")[-1] or "brief").stem or "brief"
    return args.out / f"{stem}.md"


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.dry_run:
        for index, source in enumerate(args.sources):
            if index:
                print()
            try:
                _print_dry_run(source, args)
            except Exception as exc:  # noqa: BLE001 - report and continue with the next source
                print(f"{source}: {exc}", file=sys.stderr)
        return 0

    try:
        provider = get_provider(args.provider, args.model)
    except (RuntimeError, ValueError, ImportError) as exc:
        print(f"docbrief: {exc}", file=sys.stderr)
        return 2

    failures = 0
    for index, source in enumerate(args.sources):
        try:
            document = load(source)
            brief = summarize(document, provider, args.max_chunk_chars)
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"{source}: {exc}", file=sys.stderr)
            continue

        text = json.dumps(brief.to_dict(), indent=2, ensure_ascii=False) + "\n" if args.json else render_markdown(brief)
        target = _output_path(args, source, len(args.sources))
        if target is None:
            if index:
                print()
            sys.stdout.write(text)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            print(f"wrote {target}  ({document.words:,} words → {brief.chunks} chunk(s), {provider.model})")

    usage = getattr(provider, "usage", None)
    if usage is not None and usage.calls:
        cost = usage.cost(provider.model)
        cost_text = f", ~${cost:.4f}" if cost is not None else ""
        print(
            f"{usage.calls} API call(s), {usage.input_tokens:,} in / {usage.output_tokens:,} out tokens{cost_text}",
            file=sys.stderr,
        )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
