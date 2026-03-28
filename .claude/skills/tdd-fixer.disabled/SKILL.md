---
name: tdd-fixer
description: "Codex fixes failing tests. Happy path is entirely Codex-driven — Claude only orchestrates. Escalates to Claude subagent only after 3 Codex failures. Triggers on: /tdd-fixer, fix failing tests, make tests green, tests are failing."
---

# TDD-Fixer — Codex Makes Tests Green

**Happy path Claude cost: minimal (~4 main-session turns).**
Claude runs tests, calls Codex with failures, verifies GREEN. That's it.
Claude subagent escalation only if Codex fails 3 times.

## Input

One of:
1. A spec file path (`.claude/plan/<name>.md`) — extract test cases from it
2. A test file path — run that file only
3. No argument — run `uv run pytest tests/python/ -q` and fix all failures

## Tool Requirements

- `mcp__codex__codex`, `mcp__codex__codex-reply` — Codex fix loop (MANDATORY)
- `Bash` — run tests
- `Task` — escalation subagent only (general-purpose, Claude)

## Execution

### Step 1: Capture failures (Claude, 1 turn)

Run tests and capture output:
```bash
uv run pytest <scope> -q --tb=short 2>&1 | tail -60
```

If all green → print "All tests already passing." and stop.

### Step 2: Codex fix loop (max 3 iterations)

**MANDATORY Codex check**: `mcp__codex__codex` must be available. If absent, skip to Escalation.

**Call `mcp__codex__codex`** (iteration 1):

```
The following tests are failing. Read the relevant source files and fix the implementation (not the tests).

FAILING TESTS:
{full pytest output, trimmed to 60 lines max}

RULES:
- Do NOT modify any test file
- Run the failing tests after each change to verify
- Fix root causes, not symptoms
- Use `uv run pytest <failing_test_ids> -q` to verify after each fix
- Report: files changed, final test result
```

- `sandbox`: `"workspace-write"`
- `approval-policy`: `"on-failure"` if running in **foreground**; `"never"` if inside a **background Agent** — approval prompts can't reach a background agent and will cause it to hang indefinitely
- `developer-instructions`: `"Fix only what the failing tests require. Do not refactor. Do not touch test files. Verify with pytest after each change."`

Save `threadId`.

**After Codex returns:** run tests again (Claude, 1 turn).

**If GREEN** → proceed to Step 3.

**If still failing** → call `mcp__codex__codex-reply` with:
```
Still failing. Here is the current test output:
{new failure output}

Please fix the remaining failures.
```

Repeat up to 3 total Codex iterations.

### Step 3: Verify (Claude, 1 turn)

Run full test suite:
```bash
uv run pytest tests/python/ -q 2>&1 | tail -5
```

If clean → deliver. If new regressions → add to Codex reply as additional failures (counts as another iteration).

### Escalation (only if 3 Codex iterations failed)

Launch Task agent (subagent_type: "general-purpose") with:
```
Codex attempted to fix failing tests 3 times and did not succeed.

ORIGINAL FAILURES:
{original failure output}

CODEX CHANGES MADE (git diff):
{git diff output}

CURRENT FAILURES:
{latest failure output}

Please diagnose and fix. Do NOT modify test files.
After fixing, run `uv run pytest tests/python/ -q` and confirm green.
```

### Delivery

```
Tests fixed.

{N} failures resolved in {M} Codex iterations.
Files changed: {list}
Full suite: {pass count} passing
```
