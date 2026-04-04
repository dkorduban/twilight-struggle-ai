---
name: dispatch
description: "Master task dispatcher. Simple tasks (≤2 files, ≤30 lines, clear spec) are done inline by the main agent. Complex tasks are routed to bg-codex-implementer as a background agent. Triggers on: /dispatch, implement this, fix this, debug this, dispatch task."
---

# Dispatch — Simple Inline, Complex Background

**Main agent overhead: 1-3 turns regardless of task complexity.**

## Input

Any of:
1. Free-form task description
2. Spec file path (from `/spec-writer`)
3. Failing test output
4. Error/traceback

Optional mode hint: `implement` | `fix-tests` | `debug`
If omitted, infer from input.

---

## Step 1: Classify complexity (main agent, 1 turn)

**SIMPLE** (do inline) — ALL of these must be true:
- ≤ 2 files need changing
- Change is < 30 lines total
- Spec is crystal-clear with no ambiguity
- No need to read more than 3 files to understand context
- Failure is a typo, off-by-one, missing import, or trivially obvious bug

**COMPLEX** (dispatch background) — ANY of these:
- ≥ 3 files, or unclear which files
- Requires reading 5+ files to understand
- Multi-step implementation with interdependencies
- Test failure with non-obvious root cause
- New feature with >30 lines of new code
- Task spans multiple subsystems

---

## Step 2a: Simple path — do it inline

Use Edit/Bash/Read directly. Run `uv run pytest tests/python/ -q -n 0 2>&1 | tail -5` after.

Report:
```
Done inline.
Files: {list}
Tests: {N} passing
```

---

## Step 2b: Complex path — dispatch to background Codex agent

Launch a **general-purpose Sonnet agent** with a Codex-dispatcher prompt.

**Why Sonnet, not a custom Haiku agent?** General-purpose Sonnet subagents inherit
MCP tools (including `mcp__codex__codex`) from the parent session. Custom agent types
with `mcpServers:` in YAML frontmatter do NOT get MCP tools properly registered.

**Always use `isolation: "worktree"`** to prevent conflicts with main work.

```
Agent(
  model: "sonnet",
  isolation: "worktree",
  run_in_background: true,
  prompt: "<Codex dispatcher prompt — see template below>"
)
```

Report immediately:
```
Dispatched: <slug>
Agent: Sonnet → Codex (worktree)
```

### Codex dispatcher prompt template

```
You are a Codex dispatcher. Your primary job is to call mcp__codex__codex to delegate
implementation work to Codex, then resume with mcp__codex__codex-reply until done.

Codex does the heavy implementation. You may use other tools lightly when needed
(e.g., read a spec file, check build output), but do NOT implement code yourself.

Call mcp__codex__codex with:
- approval-policy: "never"
- sandbox: "workspace-write"
- developer-instructions: "Be concise. After each file change, run: git add <file> && git commit -m 'WIP: <what>'. After all changes, build and test. Report files changed + build/test result."

Resume with mcp__codex__codex-reply(threadId, "continue implementing") until done. Up to 15 calls.
```

### Build/test commands by language
**C++:** `cmake --build build-ninja -j` then `ctest --test-dir build-ninja --output-on-failure`
**Python:** `uv run pytest tests/python/ -q -n 0`

---

## Parallel dispatch

For N independent tasks, dispatch all in one message:
```
Agent(model: "sonnet", isolation: "worktree", run_in_background: true, prompt: task_1)
Agent(model: "sonnet", isolation: "worktree", run_in_background: true, prompt: task_2)
```

All run concurrently in separate worktrees. Main agent is free immediately.

---

## Rules/analysis tasks

For rules questions → dispatch to `bg-rules-lawyer`:
```
Agent(
  subagent_type: "bg-rules-lawyer",
  run_in_background: true,
  prompt: "TASK_ID: <task_id>\nQUESTIONS:\n<questions>"
)
```

For data analysis → dispatch to `bg-codex-analyzer`:
```
Agent(
  subagent_type: "bg-codex-analyzer",
  run_in_background: true,
  prompt: "TASK_ID: <task_id>\nTASK:\n<analysis request>"
)
```
