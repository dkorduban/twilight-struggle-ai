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

## Step 2b: Complex path — dispatch to background agent

1. Generate task ID: `impl_{YYYYMMDD}_{HHMM}_{3-word-slug}`
   - slug = 3 lowercase words from the task, hyphenated (e.g. `taiwan-scoring-fix`)

2. Create task file:
   ```
   mkdir -p .codex_tasks/<task_id>
   ```
   Write `.codex_tasks/<task_id>/task.md`:
   ```
   # Task: <task_id>

   MODE: <implement|fix-tests|debug>
   SUBMITTED: <timestamp>

   ## Description
   <full task description or spec content>

   ## Constraints
   - Do not touch: .claude/, CLAUDE.md, docs/replay_grammar.md, data/spec/, data/raw_logs/, uv.lock
   - Run uv run pytest tests/python/ -q -n 0 after changes
   ```

3. Launch background agent:
   ```
   Agent(
     subagent_type: "bg-codex-implementer",
     run_in_background: true,
     prompt: "TASK_ID: <task_id>\nMODE: <mode>\nTASK:\n<full task description>"
   )
   ```

4. Report immediately (don't wait):
   ```
   Dispatched: <task_id>
   Mode: <mode>
   Monitor: /check-tasks  or  Read .codex_tasks/<task_id>/status.md
   ```

---

## Parallel dispatch

For N independent tasks, dispatch all in one message:
```
# One message with N Agent tool calls, all run_in_background=true
Agent(bg-codex-implementer, task_1)
Agent(bg-codex-implementer, task_2)
Agent(bg-codex-implementer, task_3)
```

All run concurrently. Main agent is free immediately.

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
