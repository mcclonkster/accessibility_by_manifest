"""Shared utilities for skill-comply scripts."""

from __future__ import annotations

import os


def agent_cli() -> str:
    """Return the configured agent CLI for skill-comply subprocess calls."""
    return os.environ.get("SKILL_COMPLY_AGENT_CLI", "claude")


def extract_yaml(text: str) -> str:
    """Extract YAML from LLM output, stripping markdown fences if present."""
    lines = text.strip().splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines)
