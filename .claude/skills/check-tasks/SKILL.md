---
name: check-tasks
description: "Show status of all background tasks in .codex_tasks/. Triggers on: /check-tasks, task status, what's running, check background tasks."
---

# Check-Tasks — Background Task Status

Read `.codex_tasks/*/status.md` and `.codex_tasks/*/result.md` and display a summary.

## Execution (main agent, 1-2 turns)

```bash
find .codex_tasks -name "status.md" 2>/dev/null | sort
```

For each `status.md` found, read it and extract: STATUS, AGENT, TASK, NOTE, CODEX_THREAD.
For DONE/FAILED tasks, also read `result.md` for the outcome summary.

## Output format

```
BACKGROUND TASKS
================
task_id                          | status     | agent                 | note
---------------------------------|------------|----------------------|---------------------------
impl_20260328_1530_taiwan-scoring | DONE       | bg-codex-implementer | 816 passing
impl_20260328_1545_space-race-l8  | RUNNING    | bg-codex-implementer | Codex implementing — iter 1/3
analyze_20260328_1600_parquet-qa  | VERIFYING  | bg-codex-analyzer    | running pytest
rules_20260328_1610_comecon-pool  | FAILED     | bg-rules-lawyer      | PDF section not found

Total: N tasks  (done=X  running=Y  failed=Z)
```

For DONE tasks, append result summary on next line (indented):
```
  → Files: foo.py, bar.py  |  Tests: 816 passing
```

For FAILED tasks, append the blocker:
```
  → Blocker: task requires schema change outside allowed files
```

## If .codex_tasks/ is empty or missing

```
No background tasks found. Use /dispatch to start one.
```
