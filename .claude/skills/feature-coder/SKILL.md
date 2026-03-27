---
name: feature-coder
description: "Codex implements a spec. Claude reads spec, calls Codex, verifies tests, runs code-reviewer. Happy path is ~6 main-session turns. Triggers on: /feature-coder, implement this spec, codex implement, implement the plan."
---

# Feature-Coder — Spec In, Codex Implements

**Happy path Claude cost: minimal (~6 main-session turns).**
Claude reads spec → calls Codex → verifies → code-reviewer → done.
No Plan agent, no audit loop, no Explore subagent.

## Input

One of:
1. A spec file path (`.claude/plan/<name>.md`) — produced by `/spec-writer`
2. A direct task description (Claude inlines it as the spec)

## Tool Requirements

- `mcp__codex__codex`, `mcp__codex__codex-reply` — implementation (MANDATORY)
- `Read` — read spec
- `Bash` — run tests, git diff
- `Task` — code-reviewer subagent after implementation

## Execution

### Step 1: Read spec (Claude, 1 turn)

Read the spec file. Extract:
- Files to create/modify
- Interfaces/signatures
- Test cases (if listed)
- Constraints

Record `$START_SHA` via `git rev-parse HEAD`.

### Step 2: Codex implements (max 3 iterations)

**MANDATORY Codex check**: `mcp__codex__codex` must be available. If absent, stop and tell user.

**Call `mcp__codex__codex`** (iteration 1):

```
Implement the following spec exactly. Do not add extra features or refactor unrelated code.

SPEC:
{full spec content}

CONSTRAINTS:
- Follow existing code conventions in the files you touch
- Run `uv run pytest tests/python/ -q` after implementation and confirm passing
- Report: files created/modified, final test result
```

- `sandbox`: `"workspace-write"`
- `approval-policy`: `"on-failure"`
- `developer-instructions`: `"Implement the spec as written. Minimal changes. No refactoring outside scope. Verify with pytest."`

Save `threadId`.

### Step 3: Verify (Claude, 1 turn)

```bash
uv run pytest tests/python/ -q 2>&1 | tail -10
```

**If GREEN** → Step 4.

**If failing** → call `mcp__codex__codex-reply`:
```
Tests are failing after your implementation. Fix the failures.

CURRENT TEST OUTPUT:
{failure output}

Do NOT modify test files. Fix the implementation.
```

Retry up to 3 total Codex iterations. If still failing after 3, stop and report to user with `git diff $START_SHA` and failure output.

### Step 4: Code review (1 subagent)

```bash
git add -N . && git diff $START_SHA
```

Launch Task agent (subagent_type: "feature-dev:code-reviewer") with diff + original spec.

**If no CRITICAL/HIGH** → deliver.

**If CRITICAL/HIGH** → call `mcp__codex__codex-reply` (reuse threadId):
```
Code reviewer flagged the following issues. Please fix them.

ISSUES:
{accepted CRITICAL/HIGH findings verbatim}
```

Re-run tests, re-review (max 1 additional review round).

### Delivery

```
Implementation complete.

Files: {list}
Tests: {N} passing, no regressions
Codex iterations: {N}/3
Review: passed / {N} issues resolved
```
