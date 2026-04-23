"""Run scenarios via a configured agent CLI and parse stream-json tool calls."""

from __future__ import annotations

import json
import re
import shlex
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from scripts.parser import ObservationEvent
from scripts.scenario_generator import Scenario
from scripts.utils import agent_cli

SANDBOX_BASE = Path("/tmp/skill-comply-sandbox")
ALLOWED_MODELS = frozenset({"haiku", "sonnet", "opus"})


@dataclass(frozen=True)
class ScenarioRun:
    scenario: Scenario
    observations: tuple[ObservationEvent, ...]
    sandbox_dir: Path


def run_scenario(
    scenario: Scenario,
    model: str = "sonnet",
    max_turns: int = 30,
    timeout: int = 300,
    skill_path: Path | None = None,
) -> ScenarioRun:
    """Execute a scenario and extract tool calls from stream-json output."""
    if model not in ALLOWED_MODELS:
        raise ValueError(f"Unknown model: {model!r}. Allowed: {ALLOWED_MODELS}")

    sandbox_dir = _safe_sandbox_dir(scenario.id)
    _setup_sandbox(sandbox_dir, scenario)

    cli = agent_cli()
    prompt = _prompt_with_skill_context(scenario.prompt, skill_path)
    result = subprocess.run(
        [
            cli, "-p", prompt,
            "--model", model,
            "--max-turns", str(max_turns),
            "--add-dir", str(sandbox_dir),
            "--allowedTools", "Read,Write,Edit,Bash,Glob,Grep",
            "--output-format", "stream-json",
            "--verbose",
        ],
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=sandbox_dir,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{cli} -p failed (rc={result.returncode}): {result.stderr[:500]}"
        )

    observations = _parse_stream_json(result.stdout)

    return ScenarioRun(
        scenario=scenario,
        observations=tuple(observations),
        sandbox_dir=sandbox_dir,
    )


def _prompt_with_skill_context(prompt: str, skill_path: Path | None) -> str:
    """Inject the target skill/rule text into the scenario prompt.

    The generated scenarios mention the behavior under test, but a fresh agent
    CLI process may not have this repo's skill registry loaded. Include the
    source skill explicitly so the scenario measures compliance rather than
    ambient skill discovery.
    """
    if skill_path is None:
        return prompt

    skill_content = skill_path.read_text(encoding="utf-8")
    return (
        "You are being evaluated for compliance with the following skill/rule.\n"
        "Follow it when it applies to the task. If the skill requires subagents "
        "but this runtime cannot expose subagent telemetry, make the separate "
        "voices explicit in your final answer.\n\n"
        "<skill_under_test>\n"
        f"{skill_content}\n"
        "</skill_under_test>\n\n"
        "<scenario_prompt>\n"
        f"{prompt}\n"
        "</scenario_prompt>"
    )


def _safe_sandbox_dir(scenario_id: str) -> Path:
    """Sanitize scenario ID and ensure path stays within sandbox base."""
    safe_id = re.sub(r"[^a-zA-Z0-9\-_]", "_", scenario_id)
    path = SANDBOX_BASE / safe_id
    # Validate path stays within sandbox base (raises ValueError on traversal)
    path.resolve().relative_to(SANDBOX_BASE.resolve())
    return path


def _setup_sandbox(sandbox_dir: Path, scenario: Scenario) -> None:
    """Create sandbox directory and run setup commands."""
    if sandbox_dir.exists():
        shutil.rmtree(sandbox_dir)
    sandbox_dir.mkdir(parents=True)

    subprocess.run(["git", "init"], cwd=sandbox_dir, capture_output=True)

    for cmd in scenario.setup_commands:
        parts = shlex.split(cmd)
        subprocess.run(parts, cwd=sandbox_dir, capture_output=True)


def _parse_stream_json(stdout: str) -> list[ObservationEvent]:
    """Parse stream-json output into ObservationEvents.

    Stream-json format:
    - type=assistant with content[].type=tool_use → tool call (name, input)
    - type=user with content[].type=tool_result → tool result (output)
    """
    events: list[ObservationEvent] = []
    pending: dict[str, dict] = {}
    event_counter = 0

    for line in stdout.strip().splitlines():
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        msg_type = msg.get("type")

        if msg_type == "assistant":
            content = msg.get("message", {}).get("content", [])
            for block in content:
                if block.get("type") == "tool_use":
                    tool_use_id = block.get("id", "")
                    tool_input = block.get("input", {})
                    input_str = (
                        json.dumps(tool_input)[:5000]
                        if isinstance(tool_input, dict)
                        else str(tool_input)[:5000]
                    )
                    pending[tool_use_id] = {
                        "tool": block.get("name", "unknown"),
                        "input": input_str,
                        "order": event_counter,
                    }
                    event_counter += 1
                elif block.get("type") == "text":
                    events.append(ObservationEvent(
                        timestamp=f"T{event_counter:04d}",
                        event="assistant_message",
                        tool="AssistantMessage",
                        session=msg.get("session_id", "unknown"),
                        input="",
                        output=str(block.get("text", ""))[:5000],
                    ))
                    event_counter += 1

        elif msg_type == "user":
            content = msg.get("message", {}).get("content", [])
            if isinstance(content, list):
                for block in content:
                    tool_use_id = block.get("tool_use_id", "")
                    if tool_use_id in pending:
                        info = pending.pop(tool_use_id)
                        output_content = block.get("content", "")
                        if isinstance(output_content, list):
                            output_str = json.dumps(output_content)[:5000]
                        else:
                            output_str = str(output_content)[:5000]

                        events.append(ObservationEvent(
                            timestamp=f"T{info['order']:04d}",
                            event="tool_complete",
                            tool=info["tool"],
                            session=msg.get("session_id", "unknown"),
                            input=info["input"],
                            output=output_str,
                        ))

    for _tool_use_id, info in pending.items():
        events.append(ObservationEvent(
            timestamp=f"T{info['order']:04d}",
            event="tool_complete",
            tool=info["tool"],
            session="unknown",
            input=info["input"],
            output="",
        ))

    return sorted(events, key=lambda e: e.timestamp)
