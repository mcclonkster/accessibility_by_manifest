from __future__ import annotations

import logging
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


LOGGER_NAME = "accessibility_by_manifest"


def get_logger(name: str | None = None) -> logging.Logger:
    return logging.getLogger(LOGGER_NAME if name is None else f"{LOGGER_NAME}.{name}")


@contextmanager
def run_log(path: Path, *, overwrite: bool) -> Iterator[Path]:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "w" if overwrite else "a"
    logger = get_logger()
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(path, mode=mode, encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
    logger.addHandler(handler)
    try:
        logger.info("Log started: %s", path)
        yield path
    finally:
        logger.info("Log finished: %s", path)
        logger.removeHandler(handler)
        handler.close()
