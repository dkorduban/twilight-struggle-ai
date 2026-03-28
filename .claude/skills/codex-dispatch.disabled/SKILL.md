---
name: codex-dispatch
description: "Route any implementation, test-fix, or debug task to Codex with domain-appropriate context. Haiku classifies the task type and injects domain constraints; Claude calls Codex. Replaces direct subagent calls for cpp-engine-builder, dataset-plumber, pytorch-trainer, eval-referee. Triggers on: /codex-dispatch, dispatch to codex, codex this task, implement/fix/debug with context."
---

# Codex-Dispatch — Haiku Classifies, Codex Executes

**Happy path Claude cost: ~5 main-session turns.**
1 Haiku subagent classifies → Claude builds prompt → Codex implements → Claude verifies.
No full Claude subagent unless Codex fails 3 times.

## Input

Any of:
1. A free-form task description (most common)
2. A spec file path (`.claude/plan/<name>.md`) — for implementation tasks
3. Raw pytest failure output — for fix tasks
4. An error/traceback — for debug tasks

Optional domain hint: `engine | cpp | etl | train | eval | general`
If omitted, Haiku infers it from file paths and keywords in the task.

## Tool Requirements

- `mcp__codex__codex`, `mcp__codex__codex-reply` — Codex execution (MANDATORY)
- `Bash` — run tests and capture output
- `Task` — Haiku classification subagent (step 1), escalation subagent (step 5 only)

---

## Execution

### Step 1: Haiku classifies (1 Haiku subagent)

Launch `Task` agent (subagent_type: `general-purpose`, model: `haiku`) with:

```
You are a task router for a Twilight Struggle AI repository. Read the task below and
output a JSON object ONLY (no prose, no markdown fences).

TASK:
{task description or truncated failure/error, max 80 lines}

Output this exact JSON:
{
  "mode": "implement" | "fix-tests" | "debug",
  "domain": "engine" | "cpp" | "etl" | "train" | "eval" | "general",
  "allowed_files": ["<glob patterns for files Codex should focus on>"],
  "invariants": ["<2-5 critical constraints to inject into Codex prompt>"],
  "verify_cmd": "<pytest command to verify the fix, e.g. uv run pytest tests/python/test_engine.py -q>"
}

Domain guide:
- engine: python/tsrl/engine/, tests/python/test_engine.py, test_game_loop.py, test_mcts.py
- cpp: cpp/tscore/, bindings/, tests/cpp/
- etl: python/tsrl/etl/, tests/python/test_parser.py, test_reducer.py, test_resolver.py, test_dataset.py
- train: python/tsrl/policies/, python/tsrl/train/, python/tsrl/selfplay/, scripts/
- eval: reports/, benchmarks/, tests/ (read-only analysis, no production edits)
- general: anything else or cross-cutting

Invariant pool (pick the 2-5 most relevant):
- Do NOT modify test files
- Preserve deterministic state hashing
- Do not silently drop unknown replay lines
- support_mask_false_exclusion_rate must stay 0
- illegal-action rate after masking must stay 0
- train/val/test splits are by game, not by row
- offline-smoothed labels must never appear in online inference state
- Do not add dependencies; use uv
- Raw logs in data/raw_logs/ are immutable
- Run uv run pytest tests/python/ -q after changes
```

Parse the JSON from the Haiku response.

### Step 2: Build Codex prompt (Claude, 1 turn)

Assemble prompt using the classification output:

```
{MODE-SPECIFIC HEADER — see below}

TASK:
{original task / spec / failures / error — full text}

DOMAIN CONSTRAINTS:
{invariants list from Haiku, one per line with "- " prefix}

FOCUS FILES:
{allowed_files list}

AFTER MAKING CHANGES:
- Run: {verify_cmd}
- Then run: uv run pytest tests/python/ -q 2>&1 | tail -5
- Report: files changed, test result summary
```

**Mode-specific headers:**

`implement`:
```
Implement the following task exactly. Do not add features beyond the spec.
Do not refactor unrelated code. Minimal diff.
```

`fix-tests`:
```
The following tests are failing. Read the relevant source files and fix the
IMPLEMENTATION (not the tests). Do not modify any test file. Fix root causes.
```

`debug`:
```
The following failure or error needs to be diagnosed and fixed. Read the
relevant source files, identify the root cause, and apply a minimal targeted fix.
```

### Step 3: Call Codex (max 3 iterations)

**MANDATORY check**: `mcp__codex__codex` must be available. If absent, skip to step 5.

**Call `mcp__codex__codex`**:
- `prompt`: assembled prompt from step 2
- `sandbox`: `"workspace-write"`
- `approval-policy`: `"on-failure"` if running in **foreground** (user can see prompts); `"never"` if running inside a **background Agent** (`run_in_background=true`) — background tasks hang forever waiting for approval that never arrives
- `developer-instructions`: `"Minimal targeted changes only. Verify with pytest. Report changed files and test result."`

Save `threadId`.

**After Codex returns:** run `{verify_cmd}` (Claude, 1 turn).

**If tests pass** → Step 4.

**If still failing** → call `mcp__codex__codex-reply`:
```
Still failing. Current output:
{new failure or test output, max 40 lines}
Fix the remaining issues.
```

Repeat up to 3 total Codex iterations.

### Step 4: Full suite check (Claude, 1 turn)

```bash
uv run pytest tests/python/ -q 2>&1 | tail -5
```

If regressions appear, add them to a final `mcp__codex__codex-reply` (counts as iteration 3 if not already used).

If C++ changes were made:
```bash
cmake --build build -j 2>&1 | tail -10 && ctest --test-dir build --output-on-failure 2>&1 | tail -10
```

### Step 5: Escalation (only if all 3 Codex iterations failed)

Launch Task agent (subagent_type: `general-purpose`) with:
```
Codex attempted 3 times and failed. Please diagnose and fix.

ORIGINAL TASK:
{task}

DOMAIN: {domain}

CODEX CHANGES (git diff):
{git diff output, max 100 lines}

CURRENT FAILURES:
{latest failure output, max 60 lines}

Do NOT modify test files. Verify with: uv run pytest tests/python/ -q
```

### Delivery

```
Task complete via Codex.

Mode: {implement|fix-tests|debug}
Domain: {domain}
Codex iterations: {N}/3
Files changed: {list}
Tests: {N} passing
```

---

## Domain quick-reference (injected context by domain)

| Domain | Primary files | Key invariants always included |
|--------|--------------|-------------------------------|
| engine | python/tsrl/engine/ | illegal-action rate=0, deterministic hash |
| cpp | cpp/tscore/, bindings/ | run ctest after cmake build |
| etl | python/tsrl/etl/ | no silent unknown-line drops, support_mask exclusion=0 |
| train | python/tsrl/policies/, selfplay/ | splits by game not row, offline labels offline-only |
| eval | reports/, tests/ | read-only analysis, no production file edits |
| general | inferred | run full pytest suite |
