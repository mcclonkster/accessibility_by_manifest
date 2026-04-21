from __future__ import annotations

import re

XML_ILLEGAL_RE = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")
WHITESPACE_RE = re.compile(r"\s+")


def clean_text(value: object) -> str:
    text = "" if value is None else str(value)
    text = XML_ILLEGAL_RE.sub("", text)
    return WHITESPACE_RE.sub(" ", text).strip()
