from __future__ import annotations

import json
import logging
import os
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from accessibility_by_manifest.util.logging import LOGGER_NAME, get_logger
from pdf_accessibility.persistence.run_record import update_run_status


LOGGER = get_logger("pdf_accessibility.runtime")


class _RunContextFilter(logging.Filter):
    def __init__(self, *, run_id: str, run_dir: Path) -> None:
        super().__init__()
        self.run_id = run_id
        self.run_dir = str(run_dir)

    def filter(self, record: logging.LogRecord) -> bool:
        record.run_id = self.run_id
        record.run_dir = self.run_dir
        record.service_name = "accessibility_by_manifest"
        record.event_dataset = "pdf_accessibility"
        return True


class _JsonEventFormatter(logging.Formatter):
    _reserved = {
        "args",
        "asctime",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",
        "levelname",
        "levelno",
        "lineno",
        "module",
        "msecs",
        "msg",
        "message",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "stack_info",
        "thread",
        "threadName",
    }

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "@timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "message": record.getMessage(),
            "log.level": record.levelname.lower(),
            "log.logger": record.name,
            "service.name": getattr(record, "service_name", "accessibility_by_manifest"),
            "event.dataset": getattr(record, "event_dataset", "pdf_accessibility"),
            "process.pid": os.getpid(),
            "run.id": getattr(record, "run_id", None),
            "run.dir": getattr(record, "run_dir", None),
        }
        extras: dict[str, object] = {}
        for key, value in record.__dict__.items():
            if key in self._reserved or key.startswith("_"):
                continue
            if key in {"service_name", "event_dataset", "run_id", "run_dir"}:
                continue
            extras[key.replace("_", ".")] = value
        payload.update(extras)
        if record.exc_info:
            payload["error.stack_trace"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


@contextmanager
def run_logging(run_dir: Path, *, argv: list[str] | None = None) -> Iterator[Path]:
    logs_dir = run_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / "execution.log"
    debug_log_path = logs_dir / "debug.log"
    events_path = logs_dir / "events.jsonl"
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    run_filter = _RunContextFilter(run_id=run_dir.name, run_dir=run_dir)
    started_at = datetime.now(timezone.utc)

    file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
    file_handler.addFilter(run_filter)

    debug_file_handler = logging.FileHandler(debug_log_path, mode="a", encoding="utf-8")
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
    debug_file_handler.addFilter(run_filter)

    events_handler = logging.FileHandler(events_path, mode="a", encoding="utf-8")
    events_handler.setLevel(logging.DEBUG)
    events_handler.setFormatter(_JsonEventFormatter())
    events_handler.addFilter(run_filter)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
    stderr_handler.addFilter(run_filter)

    logger.addHandler(file_handler)
    logger.addHandler(debug_file_handler)
    logger.addHandler(events_handler)
    logger.addHandler(stderr_handler)
    try:
        update_run_status(run_dir, run_status="running", started_at=started_at.isoformat())
        LOGGER.info("Run started: run_dir=%s", run_dir, extra={"event_action": "run_started"})
        LOGGER.debug("Debug log started: path=%s", debug_log_path)
        yield log_path
        ended_at = datetime.now(timezone.utc)
        update_run_status(
            run_dir,
            run_status="completed",
            started_at=started_at.isoformat(),
            ended_at=ended_at.isoformat(),
            duration_ms=int((ended_at - started_at).total_seconds() * 1000),
            exit_code=0,
        )
        LOGGER.info("Run finished: run_dir=%s", run_dir, extra={"event_action": "run_finished"})
    except Exception as exc:
        ended_at = datetime.now(timezone.utc)
        update_run_status(
            run_dir,
            run_status="failed",
            started_at=started_at.isoformat(),
            ended_at=ended_at.isoformat(),
            duration_ms=int((ended_at - started_at).total_seconds() * 1000),
            exit_code=1,
            error_message=str(exc),
        )
        LOGGER.exception("Run failed: run_dir=%s", run_dir, extra={"event_action": "run_failed"})
        raise
    finally:
        logger.removeHandler(file_handler)
        logger.removeHandler(debug_file_handler)
        logger.removeHandler(events_handler)
        logger.removeHandler(stderr_handler)
        file_handler.close()
        debug_file_handler.close()
        events_handler.close()
        stderr_handler.close()
