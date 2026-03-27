---
name: autonomous-debugger
description: "Codex diagnoses and fixes a broken test, error, or regression. Happy path: Codex only, Claude orchestrates in ~4 turns. Escalates to Claude subagent only after 3 Codex failures. Triggers on: /autonomous-debugger, debug this, fix this error, something is broken, regression."
---

# Autonomous-Debugger — Codex Diagnoses and Fixes

**Happy path Claude cost: minimal (~4 main-session turns).**
Claude captures the failure, sends it to Codex, verifies the fix. Done.
No Explore subagent, no Plan agent, no spec. Codex reads the codebase itself.

## Input

One of:
1. A test name or test file: `/autonomous-debugger tests/python/test_engine.py::test_realign_foo`
2. An error description: `/autonomous-debugger scoring gives wrong VP in South America`
3. No argument: run the full suite and fix all failures

## Tool Requirements

- `mcp__codex__codex`, `mcp__codex__codex-reply` — debug loop (MANDATORY)
- `Bash` — run tests, capture output
- `Task` — escalation Claude subagent only

## Execution

### Step 1: Capture the failure (Claude, 1-2 turns)

```bash
uv run pytest <scope> -q --tb=short 2>&1 | tail -60
```

If no failures → print "No failures found." and stop.

If error description (not a test): also run `uv run pytest tests/python/ -q --tb=line 2>&1 | tail -30` to find related failures.

### Step 2: Codex debug loop (max 3 iterations)

**MANDATORY Codex check**: `mcp__codex__codex` must be available. If absent, skip to Escalation.

**Call `mcp__codex__codex`** (iteration 1):

```
Diagnose and fix the following failure. Read whatever source files are needed.

FAILURE:
{pytest output or error description — 60 lines max}

INSTRUCTIONS:
1. Read the failing test to understand what it expects
2. Read the implementation it calls to find the root cause
3. Fix the implementation (NOT the test)
4. Run `uv run pytest <failing_test_ids> -q` to verify fix
5. Run `uv run pytest tests/python/ -q 2>&1 | tail -5` to check for regressions
6. Report: root cause (1 sentence), files changed, final test output
```

- `sandbox`: `"workspace-write"`
- `approval-policy`: `"on-failure"`
- `developer-instructions`: `"Diagnose root cause before fixing. Do not modify test files. Verify fix with pytest."`

Save `threadId`.

### Step 3: Verify (Claude, 1 turn)

```bash
uv run pytest tests/python/ -q 2>&1 | tail -5
```

**If GREEN** → deliver.

**If still failing or new regressions** → call `mcp__codex__codex-reply`:
```
Still failing (or new regressions introduced). Current output:
{test output}

Please fix the remaining issues. Do not modify test files.
```

Repeat up to 3 total Codex iterations.

### Escalation (only after 3 failed Codex iterations)

Launch Task agent (subagent_type: "general-purpose") with:
```
Codex failed to fix the following after 3 attempts.

ORIGINAL FAILURE:
{original failure}

CODEX CHANGES (git diff):
{git diff}

CURRENT STATE:
{latest test output}

Diagnose the root cause carefully. Fix the implementation only (not tests).
Run `uv run pytest tests/python/ -q` and confirm green before finishing.
```

### Delivery

```
Fixed.

Root cause: {1-sentence diagnosis from Codex}
Files changed: {list}
Codex iterations: {N}/3
Suite: {pass count} passing, 0 new failures
```

If escalated to Claude subagent:
```
Fixed (required Claude escalation after 3 Codex attempts).
Root cause: {diagnosis}
...
```
