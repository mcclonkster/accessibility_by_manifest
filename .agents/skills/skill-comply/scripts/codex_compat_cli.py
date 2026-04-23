#!/usr/bin/env python3
"""Claude-style CLI compatibility wrapper for running skill-comply with Codex.

skill-comply's runner was written for the Claude CLI shape:

    claude -p PROMPT --model sonnet --output-format stream-json ...

Codex uses:

    codex exec --json PROMPT

This wrapper accepts the subset of Claude-style flags used by skill-comply,
invokes `codex exec`, and translates Codex JSONL command events into the
Claude stream-json tool_use/tool_result shape consumed by scripts.runner.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-p", dest="prompt", required=True)
    parser.add_argument("--model", dest="model")
    parser.add_argument("--max-turns", dest="max_turns")
    parser.add_argument("--add-dir", dest="add_dirs", action="append", default=[])
    parser.add_argument("--allowedTools", dest="allowed_tools")
    parser.add_argument("--output-format", dest="output_format", default="text")
    parser.add_argument("--verbose", action="store_true")
    args, unknown = parser.parse_known_args()

    codex_cmd = [
        "codex",
        "exec",
        "--json",
        "--ephemeral",
        "--skip-git-repo-check",
        "--full-auto",
    ]

    codex_model = os.environ.get("SKILL_COMPLY_CODEX_MODEL")
    if codex_model:
        codex_cmd.extend(["--model", codex_model])

    for add_dir in args.add_dirs:
        codex_cmd.extend(["--add-dir", add_dir])

    # Use stdin for prompts so long generated prompts do not hit argv limits.
    with tempfile.NamedTemporaryFile(prefix="skill-comply-codex-", suffix=".txt", delete=False) as f:
        output_path = Path(f.name)

    codex_cmd.extend(["--output-last-message", str(output_path), "-"])

    result = subprocess.run(
        codex_cmd,
        input=args.prompt,
        capture_output=True,
        text=True,
        cwd=Path.cwd(),
        timeout=None,
    )

    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        sys.stderr.write(result.stdout)
        output_path.unlink(missing_ok=True)
        return result.returncode

    if args.output_format == "stream-json":
        for line in _codex_jsonl_to_claude_stream(result.stdout):
            print(json.dumps(line))
    else:
        final_text = ""
        if output_path.exists():
            final_text = output_path.read_text(encoding="utf-8")
        if not final_text:
            final_text = _last_agent_message(result.stdout)
        print(final_text)

    output_path.unlink(missing_ok=True)
    return 0


def _codex_jsonl_to_claude_stream(stdout: str) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    session_id = "codex"
    for raw_line in stdout.splitlines():
        try:
            msg = json.loads(raw_line)
        except json.JSONDecodeError:
            continue

        if msg.get("type") == "thread.started":
            session_id = str(msg.get("thread_id") or session_id)
            continue

        if msg.get("type") != "item.completed":
            continue

        item = msg.get("item") or {}
        item_type = item.get("type")
        if item_type == "agent_message":
            text = str(item.get("text") or "")
            if text:
                events.append({
                    "type": "assistant",
                    "session_id": session_id,
                    "message": {
                        "content": [{
                            "type": "text",
                            "text": text,
                        }],
                    },
                })
            continue

        if item_type != "command_execution":
            tool_use_id = str(item.get("id") or f"codex_item_{len(events)}")
            events.append({
                "type": "assistant",
                "message": {
                    "content": [{
                        "type": "tool_use",
                        "id": tool_use_id,
                        "name": f"Codex:{item_type or 'unknown'}",
                        "input": item,
                    }],
                },
            })
            events.append({
                "type": "user",
                "session_id": session_id,
                "message": {
                    "content": [{
                        "type": "tool_result",
                        "tool_use_id": tool_use_id,
                        "content": json.dumps(item)[:5000],
                    }],
                },
            })
            continue

        tool_use_id = str(item.get("id") or f"codex_tool_{len(events)}")
        command = str(item.get("command") or "")
        output = str(item.get("aggregated_output") or "")
        exit_code = item.get("exit_code")
        if exit_code is not None:
            output = f"Exit code {exit_code}\n{output}"

        events.append({
            "type": "assistant",
            "message": {
                "content": [{
                    "type": "tool_use",
                    "id": tool_use_id,
                    "name": "Bash",
                    "input": {"command": command},
                }],
            },
        })
        events.append({
            "type": "user",
            "session_id": session_id,
            "message": {
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use_id,
                    "content": output,
                }],
            },
        })

    return events


def _last_agent_message(stdout: str) -> str:
    last = ""
    for raw_line in stdout.splitlines():
        try:
            msg = json.loads(raw_line)
        except json.JSONDecodeError:
            continue
        item = msg.get("item") or {}
        if msg.get("type") == "item.completed" and item.get("type") == "agent_message":
            last = str(item.get("text") or "")
    return last


if __name__ == "__main__":
    raise SystemExit(main())
