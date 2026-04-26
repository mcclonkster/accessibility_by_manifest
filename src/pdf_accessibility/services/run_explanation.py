from __future__ import annotations

import json
import os
import subprocess
import tempfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib import request
from urllib.error import HTTPError, URLError

from accessibility_by_manifest.util.logging import get_logger
from pdf_accessibility.models.state import DocumentState


DEFAULT_OPENROUTER_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
DEFAULT_LMSTUDIO_ENDPOINT = "http://localhost:1234/v1/chat/completions"
DEFAULT_OUTPUT_NAME = "run_explanation.md"
DEFAULT_LOG_NAME = "run_explanation.log"
LOGGER = get_logger("pdf_accessibility.run_explanation")


class RunExplainerError(RuntimeError):
    pass


@dataclass(frozen=True)
class RunExplainerConfig:
    provider: str
    model: str | None = None
    endpoint: str | None = None
    timeout_seconds: int = 180
    output_name: str = DEFAULT_OUTPUT_NAME
    log_name: str = DEFAULT_LOG_NAME


def generate_run_explanation_markdown(document: DocumentState, config: RunExplainerConfig) -> Path:
    prompt = build_run_explanation_prompt(document)
    log_path = document.run_dir / "logs" / config.log_name
    markdown = _generate_markdown(prompt, config, run_dir=document.run_dir, log_path=log_path)
    path = document.run_dir / config.output_name
    text = markdown.rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
    document.output_artifacts.run_explanation_markdown = path
    document.output_artifacts.run_explanation_log = log_path if log_path.exists() else None
    LOGGER.info("Run explanation written: path=%s provider=%s", path, config.provider)
    return path


def build_run_explanation_prompt(document: DocumentState) -> str:
    operator_guide = _load_json(document.run_dir / "operator_guide.json")
    finalization_status = _load_json(document.run_dir / "finalization_status.json")
    artifact_manifest = _load_json(document.run_dir / "artifact_manifest.json")
    review_tasks = _load_json(document.run_dir / "review_tasks.json")
    review_decisions = _load_json(document.run_dir / "review_decisions.json")
    writeback_report = _load_json(document.run_dir / "writeback_report.json")

    unresolved_tasks = [
        task
        for task in review_tasks
        if isinstance(task, dict) and not bool(task.get("resolved"))
    ]
    resolved_tasks = [
        task
        for task in review_tasks
        if isinstance(task, dict) and bool(task.get("resolved"))
    ]
    blocker_counts_by_issue_code = dict(
        sorted(Counter(str(task.get("issue_code", "UNKNOWN")) for task in unresolved_tasks).items())
    )
    actionable_blockers = _select_actionable_blockers(unresolved_tasks, limit=8)
    structural_blockers = _select_structural_blockers(
        unresolved_tasks,
        finalization_status=finalization_status,
        writeback_report=writeback_report,
        limit=8,
    )
    resolved_input_preview = _select_resolved_inputs(
        review_decisions=review_decisions,
        resolved_tasks=resolved_tasks,
        limit=8,
    )
    summary = {
        "run_dir": str(document.run_dir),
        "document_status": document.document_status.value,
        "finalization_state": document.finalization_state.value,
        "blocker_ids": document.blocker_ids,
        "max_blockers_to_enumerate": 8,
        "blocker_counts_by_issue_code": blocker_counts_by_issue_code,
        "actionable_blockers": actionable_blockers,
        "structural_blockers": structural_blockers,
        "already_resolved_inputs": resolved_input_preview,
        "operator_guide": operator_guide,
        "finalization_status": finalization_status,
        "artifact_manifest": artifact_manifest,
        "review_task_count": len(review_tasks) if isinstance(review_tasks, list) else 0,
        "unresolved_review_task_count": len(unresolved_tasks),
        "resolved_review_task_count": len(resolved_tasks),
        "unresolved_review_task_preview": unresolved_tasks[:12],
        "review_decision_count": len(review_decisions) if isinstance(review_decisions, list) else 0,
        "writeback_report": writeback_report,
    }
    summary_json = json.dumps(summary, indent=2, ensure_ascii=False)
    return (
        "You are writing a markdown run explanation for the accessibility_by_manifest PDF workflow.\n"
        "Use only the provided run data. Do not invent facts.\n"
        "Audience: a human operator opening the run directory.\n"
        "Explain what happened, what blocked finalization or what succeeded, which artifact files matter most, "
        "and the concrete next step.\n"
        "Keep it concise and specific.\n"
        "Explicitly separate actionable blockers, structural blockers, and already-resolved inputs.\n"
        "Use blocker_counts_by_issue_code as the primary blocker summary instead of re-deriving counts yourself.\n"
        "Do not enumerate more than max_blockers_to_enumerate blockers across the explanation.\n"
        "Make the Next Step section short, prioritized, and operator-actionable.\n"
        "If the run is finalized, say no manual next step is required.\n"
        "Use these sections when relevant:\n"
        "# Run Explanation\n"
        "## Status\n"
        "## Why It Stopped Or Succeeded\n"
        "## Actionable Blockers\n"
        "## Structural Blockers\n"
        "## Already Resolved Inputs\n"
        "## Key Files\n"
        "## Next Step\n"
        "## Notes\n\n"
        "Run data:\n"
        f"{summary_json}\n"
    )


def _generate_markdown(prompt: str, config: RunExplainerConfig, *, run_dir: Path, log_path: Path) -> str:
    provider = config.provider.strip().lower()
    if provider == "codex":
        return _run_codex_cli(prompt, config, run_dir=run_dir, log_path=log_path)
    if provider == "claude_code":
        return _run_claude_cli(prompt, config, log_path=log_path)
    if provider == "openrouter":
        return _run_openrouter(prompt, config, log_path=log_path)
    if provider == "ollama":
        return _run_ollama(prompt, config, log_path=log_path)
    if provider == "lmstudio":
        return _run_lmstudio(prompt, config, log_path=log_path)
    raise RunExplainerError(f"Unsupported explainer provider: {config.provider}")


def _run_codex_cli(prompt: str, config: RunExplainerConfig, *, run_dir: Path, log_path: Path) -> str:
    if not _command_exists("codex"):
        raise RunExplainerError("codex CLI is not installed or not on PATH")
    with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as temp_output:
        output_path = Path(temp_output.name)
    cmd = [
        "codex",
        "exec",
        prompt,
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "-C",
        str(run_dir),
        "-o",
        str(output_path),
    ]
    if config.model:
        cmd.extend(["--model", config.model])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=config.timeout_seconds, check=False)
    except OSError as exc:
        output_path.unlink(missing_ok=True)
        _write_explainer_log(log_path, provider="codex", model=config.model, error=str(exc))
        raise RunExplainerError(str(exc)) from exc
    _write_explainer_log(
        log_path,
        provider="codex",
        model=config.model,
        command=cmd,
        stdout=result.stdout,
        stderr=result.stderr,
        returncode=result.returncode,
    )
    if result.returncode != 0:
        output_path.unlink(missing_ok=True)
        raise RunExplainerError(result.stderr.strip() or result.stdout.strip() or "codex explainer failed")
    try:
        return output_path.read_text(encoding="utf-8")
    finally:
        output_path.unlink(missing_ok=True)


def _run_claude_cli(prompt: str, config: RunExplainerConfig, log_path: Path) -> str:
    if not _command_exists("claude"):
        raise RunExplainerError("claude CLI is not installed or not on PATH")
    cmd = ["claude", "--print", "--output-format", "text", prompt]
    if config.model:
        cmd.extend(["--model", config.model])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=config.timeout_seconds, check=False)
    except OSError as exc:
        _write_explainer_log(log_path, provider="claude_code", model=config.model, error=str(exc))
        raise RunExplainerError(str(exc)) from exc
    _write_explainer_log(
        log_path,
        provider="claude_code",
        model=config.model,
        command=cmd,
        stdout=result.stdout,
        stderr=result.stderr,
        returncode=result.returncode,
    )
    if result.returncode != 0:
        raise RunExplainerError(result.stderr.strip() or result.stdout.strip() or "claude explainer failed")
    return result.stdout.strip()


def _run_openrouter(prompt: str, config: RunExplainerConfig, log_path: Path) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        _write_explainer_log(log_path, provider="openrouter", model=config.model, error="OPENROUTER_API_KEY is not set")
        raise RunExplainerError("OPENROUTER_API_KEY is not set")
    model = config.model or "openai/gpt-5-mini"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }
    endpoint = config.endpoint or DEFAULT_OPENROUTER_ENDPOINT
    response_data = _post_json(
        endpoint,
        payload,
        timeout_seconds=config.timeout_seconds,
        headers={"Authorization": f"Bearer {api_key}"},
    )
    _write_explainer_log(log_path, provider="openrouter", model=model, endpoint=endpoint, response=response_data)
    try:
        return str(response_data["choices"][0]["message"]["content"]).strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RunExplainerError(f"Unexpected OpenRouter response shape: {response_data}") from exc


def _run_ollama(prompt: str, config: RunExplainerConfig, log_path: Path) -> str:
    model = config.model or "llama3.1"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2},
    }
    endpoint = config.endpoint or DEFAULT_OLLAMA_ENDPOINT
    response_data = _post_json(endpoint, payload, timeout_seconds=config.timeout_seconds)
    _write_explainer_log(log_path, provider="ollama", model=model, endpoint=endpoint, response=response_data)
    response_text = response_data.get("response")
    if not isinstance(response_text, str):
        raise RunExplainerError(f"Unexpected Ollama response shape: {response_data}")
    return response_text.strip()


def _run_lmstudio(prompt: str, config: RunExplainerConfig, log_path: Path) -> str:
    model = config.model or "local-model"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "stream": False,
    }
    endpoint = config.endpoint or DEFAULT_LMSTUDIO_ENDPOINT
    response_data = _post_json(endpoint, payload, timeout_seconds=config.timeout_seconds)
    _write_explainer_log(log_path, provider="lmstudio", model=model, endpoint=endpoint, response=response_data)
    try:
        return str(response_data["choices"][0]["message"]["content"]).strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RunExplainerError(f"Unexpected LM Studio response shape: {response_data}") from exc


def _post_json(
    endpoint: str,
    payload: dict[str, Any],
    *,
    timeout_seconds: int,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    request_headers = {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)
    http_request = request.Request(endpoint, data=data, headers=request_headers, method="POST")
    try:
        with request.urlopen(http_request, timeout=timeout_seconds) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RunExplainerError(f"{exc.code} {exc.reason}: {body}") from exc
    except (OSError, URLError, json.JSONDecodeError) as exc:
        raise RunExplainerError(str(exc)) from exc


def _command_exists(name: str) -> bool:
    from shutil import which

    return which(name) is not None


def _load_json(path: Path) -> Any:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _select_actionable_blockers(tasks: list[dict[str, Any]], *, limit: int) -> list[dict[str, Any]]:
    actionable_issue_codes = {
        "DOCUMENT_TITLE_MISSING",
        "DOCUMENT_LANGUAGE_MISSING",
        "IMAGE_ONLY_PAGE_OCR_REQUIRED",
        "TABLE_HEADERS_UNCERTAIN",
        "TABLE_STRUCTURE_SPOT_CHECK",
        "FIGURE_ALT_TEXT_REQUIRED",
        "FIGURE_ALT_TEXT_SPOT_CHECK",
    }
    selected: list[dict[str, Any]] = []
    for task in tasks:
        issue_code = str(task.get("issue_code", "UNKNOWN"))
        if issue_code not in actionable_issue_codes:
            continue
        selected.append(_task_brief(task))
        if len(selected) >= limit:
            break
    return selected


def _select_structural_blockers(
    tasks: list[dict[str, Any]],
    *,
    finalization_status: Any,
    writeback_report: Any,
    limit: int,
) -> list[dict[str, Any]]:
    structural: list[dict[str, Any]] = []
    if isinstance(finalization_status, dict):
        categories = finalization_status.get("writeback_blocking_categories")
        details = finalization_status.get("writeback_blocking_details")
        if isinstance(categories, list):
            for category in categories[:limit]:
                detail = details.get(category) if isinstance(details, dict) else None
                structural.append(
                    {
                        "kind": "writeback_category",
                        "category": category,
                        "detail": detail,
                    }
                )
    for task in tasks:
        issue_code = str(task.get("issue_code", "UNKNOWN"))
        if issue_code != "TAGGED_DRAFT_NOT_FINAL":
            continue
        structural.append(_task_brief(task))
        if len(structural) >= limit:
            break
    return structural[:limit]


def _select_resolved_inputs(
    *,
    review_decisions: Any,
    resolved_tasks: list[dict[str, Any]],
    limit: int,
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if isinstance(review_decisions, list):
        for decision in review_decisions:
            if not isinstance(decision, dict):
                continue
            items.append(
                {
                    "kind": "review_decision",
                    "decision_type": decision.get("decision_type"),
                    "target_review_task_id": decision.get("target_review_task_id"),
                    "value": decision.get("value"),
                }
            )
            if len(items) >= limit:
                return items
    for task in resolved_tasks:
        items.append(
            {
                "kind": "resolved_review_task",
                "issue_code": task.get("issue_code"),
                "target_ref": task.get("target_ref"),
            }
        )
        if len(items) >= limit:
            break
    return items


def _task_brief(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "task_id": task.get("task_id"),
        "issue_code": task.get("issue_code"),
        "severity": task.get("severity"),
        "target_ref": task.get("target_ref"),
        "reason": task.get("reason"),
    }


def _write_explainer_log(
    path: Path,
    *,
    provider: str,
    model: str | None,
    endpoint: str | None = None,
    command: list[str] | None = None,
    stdout: str | None = None,
    stderr: str | None = None,
    returncode: int | None = None,
    response: Any = None,
    error: str | None = None,
) -> None:
    payload = {
        "provider": provider,
        "model": model,
        "endpoint": endpoint,
        "command": command,
        "returncode": returncode,
        "stdout": stdout,
        "stderr": stderr,
        "response": response,
        "error": error,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
