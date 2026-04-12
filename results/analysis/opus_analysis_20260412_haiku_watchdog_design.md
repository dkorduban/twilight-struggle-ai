---
# Opus Analysis: Haiku watchdog self-restart design
Date: 2026-04-12T12:00:00Z
Question: Can we have a watchdog of this sort — a Haiku agent that runs `sleep 600` in background, then returns and reminds the main agent to do something if it's idle? And starts itself again?
---

## Executive Summary

A self-restarting Haiku subagent that sleeps and then "nudges" the main agent is **not architecturally feasible** in Claude Code as it exists today. The fundamental blocker is that subagents (spawned via the Agent tool) are **one-way, fire-and-forget**: they run, produce a text result, and terminate. They cannot inject messages into the parent conversation after the parent has moved on to its next turn. There is no mechanism — hooks, tools, or otherwise — for a background process to "interrupt" or "inject a prompt into" a running Claude Code session.

However, the **actual goal** (prevent the main agent from going idle overnight) can be achieved through three alternative approaches, listed from simplest to most robust:

1. **Stop hook with auto-continuation prompt** — a `Stop` hook that detects idle conditions and injects a systemMessage reminding the agent to continue. This is the simplest and already partially implemented.
2. **`/loop` skill with self-pacing** — run the main agent itself in a recurring loop that checks for idle state.
3. **External cron watchdog** — a shell script (cron every 10 min) that checks whether the Claude session is active and, if not, sends a signal via a file that the `SessionStart` hook reads on the next interaction.

Recommendation: Implement approach #1 (enhance the existing `Stop` hook) as the primary mechanism, with approach #3 as a safety net for cases where the Claude process itself dies.

## Findings

### 1. Can a subagent "message" the main agent after the parent has moved on?

**No.** The Agent tool in Claude Code spawns a subagent that:
- Runs in a separate conversation context
- Produces a text result when it finishes
- If `run_in_background=true`, the main agent gets a notification when the subagent completes

The critical limitation: the subagent's result is delivered **once**, at completion. There is no mechanism for a subagent to:
- Send multiple messages over time
- "Push" a message to the parent at an arbitrary future time
- Keep running after returning its result
- Re-spawn itself

A Haiku agent that does `sleep 600` would simply block for 10 minutes (likely hitting the Bash timeout of 120s or 600s), then return its result. If the main agent has already moved on to user interaction, the background completion notification would arrive — but only as a passive notification, not an active prompt injection. The main agent would need to already be in its processing loop to act on it.

More critically: if the main agent is truly "idle" (waiting for user input, not processing), a background agent completion notification does NOT wake it up or cause it to act. The agent only processes notifications when it is already generating a response.

### 2. Can ScheduleWakeup be used?

**Partially, but only in `/loop` mode.** The `/loop` skill allows the main agent to run a command or prompt on a recurring interval. When the loop fires, the agent gets a turn to execute. This is the closest thing to a "wake up and check" mechanism.

However, `/loop` has limitations:
- It is designed for the **main agent itself**, not a subagent
- It requires the Claude Code session to remain alive and connected
- It replaces the normal interactive mode — you cannot have both a loop running and normal interactive use simultaneously
- If the session dies (WSL crash, terminal disconnect), the loop dies too

### 3. Can CronCreate run a command that injects into the current session?

**No.** Cron runs shell commands. There is no IPC channel from a cron job into a running Claude Code session. The cron job has no way to:
- Send a message to the Claude API session
- Inject text into the conversation
- Trigger a hook in the running Claude process

What cron CAN do:
- Write a file (e.g., `results/watchdog_nudge.txt`) that the agent could read at its next turn
- Kill/restart processes
- Send desktop notifications (if a notification daemon is running)

### 4. Is there a hook event that fires when Claude is about to idle?

**Yes — the `Stop` hook.** The `Stop` hook fires when the agent finishes processing and is about to return control to the user. This is the closest thing to an "about to idle" event.

The current `Stop` hook already injects a reminder to update `continuation_plan.json`. This mechanism could be enhanced to also:
- Check if there are pending tasks in the continuation plan
- Check if background processes are still running
- Inject a systemMessage like: "You have N pending tasks. Do not wait for user input — start the next task immediately."

**Limitation:** The `Stop` hook injects a systemMessage that the agent sees, but if the agent has already decided to stop (e.g., it asked a question and is waiting for user input), the systemMessage may not prevent the stop. The systemMessage is advice, not a forced action.

### 5. Analysis of the actual problem

The real problem is: during autonomous overnight work, the main agent sometimes:
- Finishes a task and asks "Want me to start X?" instead of just starting it
- Completes a background task notification but doesn't chain to the next task
- Gets into a state where it's waiting for user input that won't come for hours

The standing policy (section 7: "NEVER BE IDLE") already addresses this at the prompt level. The question is whether there's a **structural enforcement** beyond prompt instructions.

### 6. Design options ranked

#### Option A: Enhanced Stop hook (recommended, simplest)

```json
{
  "matcher": "",
  "hooks": [{
    "type": "command",
    "command": "python3 /path/to/idle_nudge_hook.py"
  }]
}
```

The hook script would:
1. Read `results/continuation_plan.json`
2. Check if there are pending `next_tasks`
3. Check if any background processes are running (`pgrep -f train_ppo`)
4. If tasks remain and no blocking process, return a systemMessage:
   `"AUTONOMOUS MODE: You have N pending tasks. Do NOT wait for user input. Start the highest-priority task immediately. Tasks: [list]"`

**Pros:** Zero infrastructure, uses existing hook system, fires at exactly the right moment.
**Cons:** Only fires when the agent is about to stop — cannot wake a truly idle session.

#### Option B: /loop with idle detection

Run: `/loop 10m "Check if you're making progress. If idle, read continuation_plan.json and start the next task."`

**Pros:** Actually wakes the agent on a timer. Agent gets a full turn every 10 minutes.
**Cons:** Replaces normal interactive mode. Cannot be used alongside normal conversation. If the session dies, the loop dies.

#### Option C: External cron + sentinel file

A cron job every 10 minutes that:
1. Checks if any `claude` process is running
2. Checks if `results/continuation_plan.json` has pending tasks
3. Checks if `results/last_activity.txt` (written by the agent at each turn) is older than 10 minutes
4. If idle: writes `results/idle_nudge.txt` with a timestamp and task list
5. The `SessionStart` hook (or a custom `PreToolUse` hook) reads this file and injects the nudge

**Pros:** Survives session crashes. Can detect truly dead sessions.
**Cons:** Cannot inject into a live session that's waiting for user input. Only helps on session restart. Most complex to implement.

#### Option D: Haiku agent with run_in_background (the original proposal)

Spawn a Haiku agent with `run_in_background=true` that sleeps, then returns a nudge message.

**Pros:** Conceptually simple.
**Cons:** The completion notification only works if the main agent is already processing. If the agent is idle/waiting for input, the notification sits unprocessed. The agent cannot re-spawn itself. Sleep would likely hit Bash timeouts. This is architecturally the wrong approach.

## Conclusions

1. **The original proposal (self-restarting Haiku watchdog) is not feasible.** Claude Code's agent model is request-response, not actor-based. Subagents cannot push messages to the parent, cannot persist, and cannot re-spawn themselves.

2. **The best available mechanism is the `Stop` hook** (Option A). It fires at exactly the moment when the agent is about to go idle, and it can inject a systemMessage with the continuation plan. This is the lowest-effort, most reliable approach.

3. **The `/loop` skill** (Option B) is a viable alternative for dedicated overnight sessions where interactive use is not needed, but it occupies the entire session.

4. **An external cron watchdog** (Option C) is a useful safety net for session crashes but cannot inject into a live idle session.

5. **The root problem is prompt-level, not architectural.** The standing policy already says "never be idle" and "never ask permission." When the agent violates this, it is because the instruction was insufficiently forceful or the agent's reasoning overrode it. The Stop hook can add structural reinforcement, but ultimately the model's tendency to ask questions before acting is a model behavior issue, not an infrastructure gap.

6. **A combination of Options A + C covers both failure modes:** Option A prevents the agent from choosing to idle within a live session; Option C detects and recovers from session death.

## Recommendations

### Immediate (5 minutes of work)

Enhance the existing `Stop` hook in `.claude/settings.json` to read the continuation plan and inject a stronger nudge. Replace the current Stop hook command with a script that:

```python
#!/usr/bin/env python3
"""Stop hook: inject continuation nudge if autonomous tasks remain."""
import json, pathlib, subprocess, sys

plan_path = pathlib.Path("/home/dkord/code/twilight-struggle-ai/results/continuation_plan.json")
msg_parts = []

# Check continuation plan
if plan_path.exists():
    plan = json.loads(plan_path.read_text())
    tasks = plan.get("next_tasks", [])
    current = plan.get("current_task", "")
    if tasks:
        msg_parts.append(f"AUTONOMOUS MODE ACTIVE. {len(tasks)} tasks pending.")
        msg_parts.append(f"Next: {tasks[0]}")
        msg_parts.append("Do NOT wait for user input. Start immediately.")

# Check if training is running (don't nudge if GPU is busy)
try:
    subprocess.check_output(["pgrep", "-f", "train_ppo"], timeout=5)
    msg_parts.append("Training is running in background — work on orthogonal tasks.")
except subprocess.CalledProcessError:
    pass

# Also remind about continuation_plan update
msg_parts.append("Update results/continuation_plan.json before session ends.")

out = {"systemMessage": " | ".join(msg_parts)} if msg_parts else {}
print(json.dumps(out))
```

### Short-term (for overnight autonomous sessions)

Before going to sleep, the user can invoke `/loop 10m` with a prompt like:
```
/loop 10m "Check continuation_plan.json. If tasks remain, execute the next one. If all done, generate new tasks from the workstream list."
```

This gives the agent a guaranteed wake-up every 10 minutes, preventing indefinite idle.

### Medium-term (cron safety net for session death)

Add a cron job that monitors session liveness:
```bash
*/10 * * * * /home/dkord/code/twilight-struggle-ai/scripts/session_watchdog.sh
```

The script would check if a Claude process is running and if the continuation plan has tasks. If the session is dead and tasks remain, it could:
- Log a warning to `results/logs/misc/session_watchdog.log`
- Optionally restart a Claude session in headless mode (if `claude --headless` or similar exists)

### Not recommended

- Do not implement the Haiku self-restart watchdog. It fights the architecture.
- Do not build complex IPC between cron and the Claude session. The hook system already provides the right injection point.

## Open Questions

1. **Does the Stop hook systemMessage actually prevent the agent from stopping?** The hook injects a message, but can the agent still choose to stop and wait for user input despite the message? Testing needed.

2. **Can `/loop` coexist with the normal session?** If not, it is only suitable for dedicated overnight sessions, not general use.

3. **Does `claude --headless` or `claude --resume` exist?** If so, the cron safety net could auto-restart dead sessions. If not, session death requires manual user intervention.

4. **Is there a `Notification` hook type** that fires when a background agent completes? If so, it could be used to chain: background agent completes -> hook fires -> systemMessage injected -> agent acts on it. This would be more targeted than the Stop hook.

5. **Could a custom `PreToolUse` hook on all tools serve as a heartbeat?** Every time the agent uses any tool, a hook could check for nudge files and inject reminders. This would only work while the agent is actively using tools, not when idle.
