"""Thin wrappers around the OpenAI and Anthropic SDKs.

Keys come from the environment only (OPENAI_API_KEY / ANTHROPIC_API_KEY) and
are never logged or written anywhere by this tool.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Protocol

DEFAULT_MODELS = {
    "openai": "gpt-4o-mini",
    "anthropic": "claude-3-5-haiku-latest",
}

# USD per million tokens (input, output). Approximate list prices; edit to match your account.
PRICE_PER_MTOK: dict[str, tuple[float, float]] = {
    "gpt-4o-mini": (0.15, 0.60),
    "gpt-4o": (2.50, 10.00),
    "claude-3-5-haiku-latest": (0.80, 4.00),
    "claude-3-5-sonnet-latest": (3.00, 15.00),
}


class Provider(Protocol):
    name: str
    model: str

    def complete(self, system: str, user: str, max_tokens: int = 1500) -> str: ...


@dataclass
class Usage:
    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0

    def add(self, input_tokens: int, output_tokens: int) -> None:
        self.calls += 1
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens

    def cost(self, model: str) -> float | None:
        prices = PRICE_PER_MTOK.get(model)
        if prices is None:
            return None
        return (self.input_tokens * prices[0] + self.output_tokens * prices[1]) / 1_000_000


def estimate_tokens(text: str) -> int:
    """Rough but stable: 4 characters per token for English prose."""
    return max(1, len(text) // 4)


class OpenAIProvider:
    name = "openai"

    def __init__(self, model: str | None = None) -> None:
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set (see .env.example)")
        try:
            from openai import OpenAI
        except ImportError:
            raise RuntimeError("the openai package is missing: pip install 'docbrief[openai]'") from None
        self.model = model or DEFAULT_MODELS["openai"]
        self.client = OpenAI()
        self.usage = Usage()

    def complete(self, system: str, user: str, max_tokens: int = 1500) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            max_tokens=max_tokens,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        )
        if response.usage:
            self.usage.add(response.usage.prompt_tokens, response.usage.completion_tokens)
        return response.choices[0].message.content or ""


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model: str | None = None) -> None:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError("ANTHROPIC_API_KEY is not set (see .env.example)")
        try:
            from anthropic import Anthropic
        except ImportError:
            raise RuntimeError("the anthropic package is missing: pip install 'docbrief[anthropic]'") from None
        self.model = model or DEFAULT_MODELS["anthropic"]
        self.client = Anthropic()
        self.usage = Usage()

    def complete(self, system: str, user: str, max_tokens: int = 1500) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=0.2,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        self.usage.add(response.usage.input_tokens, response.usage.output_tokens)
        return "".join(block.text for block in response.content if getattr(block, "type", "") == "text")


@dataclass
class FakeProvider:
    """Deterministic provider for tests and --dry-run; never touches the network."""

    responses: list[str] = field(default_factory=list)
    name: str = "fake"
    model: str = "fake-model"
    usage: Usage = field(default_factory=Usage)
    prompts: list[tuple[str, str]] = field(default_factory=list)

    def complete(self, system: str, user: str, max_tokens: int = 1500) -> str:
        self.prompts.append((system, user))
        self.usage.add(estimate_tokens(system + user), 200)
        if self.responses:
            return self.responses.pop(0)
        return "{}"


def get_provider(name: str | None = None, model: str | None = None) -> Provider:
    name = (name or os.environ.get("DOCBRIEF_PROVIDER") or "openai").lower()
    model = model or os.environ.get("DOCBRIEF_MODEL") or None
    if name == "openai":
        return OpenAIProvider(model)
    if name == "anthropic":
        return AnthropicProvider(model)
    raise ValueError(f"unknown provider '{name}' (use openai or anthropic)")
