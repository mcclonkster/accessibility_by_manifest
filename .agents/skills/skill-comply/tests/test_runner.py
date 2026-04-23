"""Tests for scenario runner parsing and prompt preparation."""

from pathlib import Path

from scripts.runner import _parse_stream_json, _prompt_with_skill_context


def test_parse_stream_json_captures_assistant_text() -> None:
    stdout = (
        '{"type":"assistant","session_id":"sess-1","message":{"content":['
        '{"type":"text","text":"## Council\\n**Skeptic:** challenge premise"}]}}\n'
    )

    events = _parse_stream_json(stdout)

    assert len(events) == 1
    assert events[0].event == "assistant_message"
    assert events[0].tool == "AssistantMessage"
    assert "Skeptic" in events[0].output


def test_prompt_with_skill_context_injects_skill_body(tmp_path: Path) -> None:
    skill = tmp_path / "SKILL.md"
    skill.write_text("# Council\nLaunch Skeptic, Pragmatist, and Critic.", encoding="utf-8")

    prompt = _prompt_with_skill_context("Decide between A and B.", skill)

    assert "<skill_under_test>" in prompt
    assert "Launch Skeptic, Pragmatist, and Critic." in prompt
    assert "<scenario_prompt>" in prompt
    assert "Decide between A and B." in prompt
