# Opus Analysis: Hand-written hooks/policy vs Tasks mechanism
Date: 2026-04-18 UTC
Question: Which approach better handles staleness, forgetting, and context usage?

## Executive Summary

The project currently relies on a hand-written memory/hook infrastructure (MEMORY.md
index + ~40 feedback/project markdown files + `results/continuation_plan.json`
injected by a SessionStart hook) to carry state across sessions. The developer-
supported Todo/Tasks mechanism (TaskCreate/TaskUpdate/TaskList) is session-local
only and invisible to future sessions.

On the three axes, the systems are specialized rather than competing:

- **Staleness**: Hand-written loses decisively. MEMORY.md and the feedback/project
  corpus accumulate stale pointers with no GC. The 2-days-old banner on
  `feedback_standing_policy.md` and the 6-days-old banner on `project_workstreams.md`
  are explicit admissions by the runtime that the content may not match reality.
  `continuation_plan.json` is updated every session (last_updated = today), so the
  narrow hand-written artifact that IS maintained is fine. Tasks are auto-GC'd at
  session end — they cannot go stale because they do not persist.

- **Forgetting**: Hand-written wins decisively. A Stop hook reminds the agent to
  update `continuation_plan.json`; a SessionStart hook re-injects its contents.
  The JSON file is a durable, structured handoff. Tasks are purely in-RAM for the
  session; a context compaction, a crash, or a summarization silently erases them.
  For a multi-week autonomous agent, Tasks are inadequate as the primary handoff.

- **Context usage**: Tasks win decisively in absolute terms. The hand-written
  system costs ~74 lines of MEMORY.md plus ~685 lines of master policy plus ~224
  lines of continuation plan — roughly 1 000+ lines / several thousand tokens
  loaded at session start — before any task-specific file is opened on demand.
  Tasks appear only in a compact system-reminder of recent activity and carry
  near-zero fixed cost. However, much of the hand-written cost is paying for
  cross-session durability that Tasks do not provide, so the comparison is not
  apples-to-apples.

The two systems answer different questions:
- Tasks = "what am I doing in THIS session?" (ephemeral, fine-grained, zero
  persistence cost)
- Hand-written memory + continuation_plan = "what does the project remember
  across sessions and what were we doing when the last one ended?"
  (persistent, coarse-grained, non-trivial context cost, requires active GC)

The right answer is to use both and keep them in their lanes, plus fix the
staleness problem in MEMORY.md that neither system addresses today.

## Findings

### Axis 1: Staleness

**Hand-written system:**

- **MEMORY.md** is an index of ~40 bullets pointing at individual
  `feedback_*.md` / `project_*.md` files. Entries include "Phase 4 architecture
  sweep state" tagged "historical" and "Self-play pipeline state" tagged
  "mostly historical now" — these are already admitting they are stale but have
  not been removed. There is no automated removal mechanism; entries linger
  until someone (usually Opus during an analysis turn) decides to prune them.
  The result is a slow monotonic accumulation of pointers whose truth value
  decays over time.

- **Individual memory files** carry explicit staleness banners. The runtime
  prepended this to `feedback_standing_policy.md`:
  > This memory is 2 days old. Memories are point-in-time observations, not
  > live state — claims about code behavior or file:line citations may be
  > outdated. Verify against current code before asserting as fact.
  And this to `project_workstreams.md`:
  > This memory is 6 days old. [...]
  The system *knows* the files are stale but does not prune them; it merely
  warns. Because the warning is about the whole file, the agent cannot tell
  which lines within the file are still current.

- **`continuation_plan.json`** is the one part of the hand-written system that
  does not suffer from staleness in practice. `last_updated` is today's date,
  and a Stop hook reminds the agent to update it. But the same file mixes
  live in-flight work (`current_task`, `active_background`, `next_tasks`) with
  long-lived historical keys (`critical_discovery_20260416`,
  `awr_iteration_plan_20260418`, `value_calibration_finding_20260418`,
  `ppo_v1_final_results`, `ismcts_investigation_closed`, etc.). Those keys
  persist across sessions forever unless explicitly deleted. A future session
  will still see `critical_discovery_20260416` a month later, and staleness
  accumulates here too, just more slowly than in the memory corpus.

- **Decision rule for removal** is implicit: the user or Opus notices an
  entry is stale during a session and deletes it. There is no scheduled GC,
  no TTL, no "last-referenced" tracking. Policy files like
  `feedback_standing_policy.md` are 685 lines long and carry years of
  accumulated rules that no one has audited.

- **Content-level drift**: MEMORY.md bullets reference "Month 3: strength
  push", CLAUDE.md also says "Month 3". But the directory already contains
  `results/analysis/opus_analysis_20260418_*.md` and the project has clearly
  been running for longer than 3 months of wall-clock from Month-1 foundations.
  The Month 1/2/3 arc is itself stale framing that the memory index has
  not updated.

**Tasks system:**

- Tasks have status = pending/in_progress/completed. Completed tasks stay
  in the list until session ends.
- At session start, the list is empty (new session).
- There is literally no way for a task to be stale across sessions because
  tasks do not cross session boundaries.
- Within a session, completed tasks do accumulate and add noise to the system-
  reminder, but the scope is small (one session) and they are gone at the next
  session-start.

**Verdict on Axis 1:** Tasks are immune to staleness by construction. The
hand-written system is vulnerable and the runtime is aware enough to issue
warnings, but pruning is manual and has not happened for multiple files that
are explicitly marked historical. `continuation_plan.json` is the one
hand-written artifact that stays fresh because a Stop hook enforces the
update discipline — the pattern to copy.

### Axis 2: Forgetting

**Hand-written system:**

- SessionStart hook in `/home/dkord/code/twilight-struggle-ai/.claude/settings.json`
  reads `continuation_plan.json` and injects a systemMessage containing
  `current_task`, first 5 `next_tasks`, and `active_background`. This is the
  single most important piece of cross-session memory machinery in the project.
- Stop hook issues: "REMINDER: Update results/continuation_plan.json before
  session ends."
- Combined with the OODA §7 checklist, this means when a session starts, the
  agent sees what was in flight. When a session ends, it is reminded to
  write what is now in flight.
- MEMORY.md itself is NOT auto-injected; rather, individual memory files are
  loaded on demand (MEMORY.md points at them; CLAUDE.md surfaces MEMORY.md
  content verbatim in the project prompt).
- Because `continuation_plan.json` is a single JSON blob on disk, context
  compaction / summarization does not destroy it — it survives anything short
  of the file being deleted.
- Weaknesses: the SessionStart hook only injects 5 next_tasks and 1 current
  task. Long-tail state (partially-finished multi-step refactors, half-ported
  experiments, reasons-why-not-to-do-X) lives in sibling JSON keys that are
  NOT injected by the hook, only loaded if the agent reads the file directly.
  It depends on the agent actually reading `continuation_plan.json` after
  seeing the injected summary.

**Tasks system:**

- Tasks are in-session only.
- A crash, a hitting-context-window-limit, a `/compact`, or even a slow enough
  summarization pass can silently erase task state.
- Tasks are visible to the agent only through system-reminders about recent
  tool use; once they fall out of the reminder window (or the session ends),
  the agent has no record of what was pending.
- There is no persistence at all. By design.

**Verdict on Axis 2:** Hand-written wins decisively for the multi-session,
multi-day autonomous workflow this project runs. A task list that forgets
everything every session is dangerous when sessions end on compaction /
wakeup cycles rather than on human instruction. Tasks are safe for
within-session "remember the 5 steps of this feature" work. They are unsafe
as the primary handoff. The project correctly uses `continuation_plan.json`
as the primary handoff and Tasks (if at all) as within-session scratch.

### Axis 3: Context Usage

**Hand-written system (rough accounting at session start):**

- CLAUDE.md: large — embedded verbatim in the system prompt (project rules).
  Already part of the prompt, not counted as incremental cost.
- MEMORY.md: 74 lines, auto-injected by the Claude Code runtime as part of
  the userMemory feature. Estimated ~900 tokens.
- `feedback_standing_policy.md`: 685 lines (~7 000 tokens). NOT auto-injected,
  but CLAUDE.md says "read first", so a conscientious agent often does read
  it; in any case it is referenced by every other memory file.
- `continuation_plan.json`: 224 lines (~2 000 tokens). Injected by
  SessionStart hook as a short systemMessage (just current/next/active_bg,
  so the hook itself injects maybe 200 tokens). The full file costs ~2 000
  tokens only if the agent reads it explicitly.
- Sibling memory files (~40 files, 2 946 total lines): ~30 000 tokens if all
  loaded, but they are loaded on demand — most sessions touch maybe 3–5 of
  them (~3 000 tokens).

Realistic cost per session at start: MEMORY.md (auto) + hook injection +
1–2 memory files agent reads = **~2 000–5 000 tokens**. If the agent reads
the full standing policy (often), add 7 000. Upper bound for a careful
session-start: ~10–12k tokens before work starts.

**Tasks system:**

- System-reminder shows recent tasks when TaskList/TaskCreate/TaskUpdate
  have been called recently. Each task is one line (~20 tokens). A typical
  list of 5–10 tasks is ~200 tokens.
- Fixed overhead: near zero when tasks are not in use.
- Peak overhead: maybe 500 tokens even with a long task list.

**Verdict on Axis 3:** Tasks are 10–100× cheaper in raw tokens. But a fair
comparison must include what Tasks do NOT do: they do not persist, they
do not explain rationale, they do not carry warnings about known pitfalls,
they do not link to analysis documents. The hand-written system spends
thousands of tokens buying things Tasks cannot provide at any price. Per
unit of cross-session durability + rationale retention, the hand-written
system is competitive. Per unit of "help me remember the 5 steps of this
feature in this session", Tasks win.

A concrete waste in the hand-written system: the 685-line
`feedback_standing_policy.md` contains both live rules (Opus Budget Gate,
§13) and historical incident narratives (§9 "Implement both or neither" from
a fixed bug). The historical narratives are useful ~once; they cost tokens
every time the file is read. Extracting live-rule-only vs historical-
narrative sections would cut load by ~30–50% with no loss.

## Conclusions

1. The two systems are complements, not substitutes. Tasks are a within-
   session structuring device; hand-written memory + continuation_plan.json
   is a cross-session durability device. Using Tasks as the primary handoff
   would lose all project state on the first compaction.

2. The continuation_plan.json + SessionStart/Stop hooks is the single most
   effective part of the hand-written infrastructure. It is fresh (updated
   today), durable (survives compaction), and cheap (small JSON). Its
   existence is why the project runs autonomously across sessions at all.

3. MEMORY.md and the feedback_*.md corpus suffer from unmanaged staleness.
   The runtime's "memory is N days old" banner is a symptom, not a fix;
   it warns but does not prune. Several entries are self-tagged "historical"
   yet remain in the index.

4. continuation_plan.json is starting to accumulate long-lived keys
   (`critical_discovery_20260416`, `ismcts_investigation_closed`,
   `value_calibration_finding_20260418`, etc.) that are not current-session
   state. Over time this file will itself drift into staleness if historical
   keys are not migrated out.

5. Context cost of the hand-written system is 10–100× Tasks, but much of it
   buys services Tasks cannot provide. The waste is concentrated in long
   policy files that mix live rules with incident narratives, not in the
   continuation plan.

6. Tasks have a blind spot on this project: an autonomous agent that gets
   wakeup-cycled every 30 minutes (see policy §14 last bullet) will lose
   task state every cycle. The project wisely does not depend on Tasks.

7. The hand-written system lacks any GC or TTL mechanism. Every removal is
   manual, which under autonomous operation means "rare" in practice.

## Recommendations

1. **Add a staleness TTL to individual memory files.** Memory files older
   than 30 days should either (a) be re-read by the agent and restated as
   current fact, or (b) be moved to `memory/archive/`. Implement as a
   SessionStart hook check that lists files where `mtime` is older than
   30 days and emits a systemMessage: "Memory audit: N files older than
   30 days. Review and prune or archive."

2. **Split continuation_plan.json into two files.** Put live in-flight state
   (`current_task`, `next_tasks`, `active_background`, `last_updated`) in
   `results/continuation_plan.json`. Move long-lived discovery/finding keys
   into `results/analysis/findings_log.json` or similar. The hand-written
   handoff file should be a handoff file, not a knowledge base. This makes
   the handoff smaller and cheaper to read, and gives the knowledge-base
   half a natural home where it can be audited separately.

3. **Split `feedback_standing_policy.md` into live-rules and
   incidents-log.** The 685-line file currently mixes §1–§8 live rules with
   §9 incident narratives and §10+ meta-rules. Extract §9 into
   `project_incidents_log.md` (rarely needed; agent can load on demand).
   Keep the live rules file under 400 lines. Expected saving: ~30% of
   the most-loaded policy file's tokens.

4. **Use Tasks for within-session step tracking on multi-step work.** When
   the main agent is doing a 3+-step sequence inside one session (e.g.,
   "build → test → commit → dispatch next phase"), Tasks are the correct
   tool — cheaper than writing to continuation_plan.json for ephemeral
   steps. MEMORY.md already endorses this (`feedback_todo_tracking.md`);
   just ensure Tasks are never promoted to cross-session status without
   first being written to continuation_plan.json.

5. **Do NOT replace the hand-written infrastructure with Tasks.** Tasks
   cannot survive the autonomous-wakeup loop that this project relies on.
   The cross-session durability is the whole point and Tasks do not
   provide it.

6. **Add an explicit "history" section to MEMORY.md and sort entries by
   last-referenced date rather than creation date.** This would make
   pruning easier: anything not referenced in 60 days is a pruning
   candidate. Could be done by parsing Claude Code session transcripts
   for file reads, but a simpler heuristic is `mtime` of the pointed-at
   file.

7. **Keep the SessionStart/Stop hook pair. Extend it to also warn if
   `continuation_plan.json` `last_updated` is older than 24h at session
   start** — that is a signal the previous session ended improperly
   (crash, compaction) and the plan may not reflect reality.

## Open Questions

- Does context compaction preserve system-reminder blocks that hold Task
  state, or does it discard them the same way it discards tool results?
  If preserved, Tasks might carry further than assumed here.

- Is there a way to hook TaskUpdate so that every task completion also
  writes a line to an append-only log? That would give Tasks some
  cross-session durability for audit purposes without losing their
  cheapness.

- Should the auto-memory (MEMORY.md) be regenerated periodically by an
  Opus session from a scan of `results/experiments.jsonl` and recent
  `results/analysis/*.md` files? That would fight staleness at the
  source rather than annotating it after the fact.

- What fraction of sessions actually read `feedback_standing_policy.md`
  in full vs. rely on MEMORY.md bullet summaries? If most sessions only
  read the bullets, the 685-line file is mostly dead weight that costs
  tokens on the few sessions that do read it.
