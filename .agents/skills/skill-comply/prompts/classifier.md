You are classifying observable events from a coding agent session against expected behavioral steps.

Events may be tool calls, command executions, generic harness events, or final assistant messages.
For each event, determine which step or steps it belongs to. A single rich final message may
match multiple decision/prose steps when it clearly contains multiple required behaviors.

Steps:
{steps_description}

Events (numbered):
{tool_calls}

Respond with ONLY a JSON object mapping step_id to a list of matching event numbers.
Include only steps that have at least one match. If no events match a step, omit it.

Example response:
{"write_test": [0, 1], "run_test_red": [2], "write_impl": [3, 4]}

Rules:
- Match based on the MEANING of the tool call, not just keywords
- Final assistant messages can satisfy prose/decision steps such as extracting a decision question,
  stating an initial position, synthesizing disagreement, or presenting a verdict.
- If the expected step requires subagents or independent voices but the trace has no subagent
  telemetry, a final assistant message with clearly separated role sections (for example
  Skeptic, Pragmatist, Critic) can count as evidence for that role-voice step.
- A Write to "test_calculator.py" is a test file write, even if the content is implementation-like
- A Write to "calculator.py" is an implementation write, even if it contains test helpers
- A Bash running "pytest" that outputs "FAILED" is a RED phase test run
- A Bash running "pytest" that outputs "passed" is a GREEN phase test run
- Tool calls usually match at most one step; final assistant messages may match multiple steps
  when they contain multiple required sections.
- If an event doesn't match any step, don't include it
