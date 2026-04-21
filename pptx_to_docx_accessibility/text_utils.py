from __future__ import annotations

import re


XML_ILLEGAL_CHAR_PATTERN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ud800-\udfff]")


def clean_text(value: object) -> str:
    text = "" if value is None else str(value)
    text = XML_ILLEGAL_CHAR_PATTERN.sub("", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    return " ".join(line for line in lines if line).strip()


def truncate_text(text: str, limit: int = 220) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."
