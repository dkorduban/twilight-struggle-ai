---
# Opus Analysis: Never-Idle Agent Policy
Date: 2026-04-12
Question: Create a policy for autonomous agents that ensures they never idle/stop but always do something reasonable.

## Executive Summary

Autonomous agents in this project must follow a strict "always productive" invariant: at no point should an agent sit idle waiting for input, permission, or a background task to complete. This document provides a concrete decision tree that agents execute whenever they finish a task, encounter an error, or run out of explicit instructions. The core mechanism is a priority-ordered fallback ladder -- when the current task ends, the agent walks the ladder top-to-bottom until it finds actionable work, then immediately starts it. "I'm done" is never an acceptable terminal state; the only valid terminal state is "machine resources are fully saturated AND I have updated continuation_plan.json for the next session."

## Findings

### 1. The Never-Idle Invariant

**Statement:** At every decision point, the agent MUST be either (a) actively executing a task, or (b) actively selecting the next task from the fallback ladder. The gap between (a) ending and (b) starting must be zero turns.

**What this means in practice:**
- Never end a response with "Done. What next?"
- Never end a response with a question to the user
- Never present a menu of options
- Never wait for a background task without starting parallel work
- After every tool call that returns, immediately evaluate what to do next

### 2. The Fallback Ladder (Decision Tree)

When the current task completes, errors out, or the agent is at a decision point, walk this ladder top-to-bottom. Execute the FIRST item that applies.

```
STEP 1: Is there unfinished work from the current task?
  YES -> Complete it. (e.g., commit results, update continuation_plan.json, log to experiments.jsonl)
  NO  -> Step 2

STEP 2: Are there pending results from background tasks?
  YES -> Process them. (Read output, check for errors, log results, trigger next steps)
  NO  -> Step 3

STEP 3: Does continuation_plan.json have next_tasks?
  YES -> Pop the highest-priority task and start it.
        (If it requires Opus and budget allows -> /askopus, then immediately go to Step 4 for parallel work)
        (If it requires GPU and GPU is busy -> skip to Step 4)
        (If it's a code task -> start it or delegate to Codex)
  NO  -> Step 4

STEP 4: Is there orthogonal workstream work available? (Check WS2-WS10 list)
  YES -> Pick the highest-priority incomplete workstream and start it.
  NO  -> Step 5

STEP 5: Are there known speedup opportunities? (Standing policy section 8)
  YES -> Pick one and implement it (or delegate to Codex).
  NO  -> Step 6

STEP 6: Are there code quality improvements available?
  YES -> Run tests, fix failing tests, add missing tests, fix TODOs in code.
  NO  -> Step 7

STEP 7: Is there tech debt to reduce? (WS6: shared library extraction, etc.)
  YES -> Pick the smallest useful slice and implement it.
  NO  -> Step 8

STEP 8: Can you update documentation or analysis based on recent results?
  YES -> Write the analysis (only if results exist that haven't been analyzed).
  NO  -> Step 9

STEP 9: TERMINAL — All resources saturated, no actionable work found.
  -> Update continuation_plan.json with "all_clear: true" timestamp
  -> Log to autonomous_decisions.log: "No actionable work found at <timestamp>. Resources: GPU=<status>, CPU=<status>."
  -> This state should essentially NEVER be reached. If you reach it, re-read
     the workstream list and continuation_plan — you almost certainly missed something.
```

### 3. Handling Specific Blocking Scenarios

#### Scenario A: Current task completed successfully, no obvious next step

**Decision tree:**
```
1. Update continuation_plan.json (mark task done, remove from next_tasks)
2. Log result to autonomous_decisions.log (1-3 lines)
3. If result changes priorities (e.g., Elo regression) -> handle per standing policy section 2
4. Walk the Fallback Ladder from Step 3
```

**Example:** You just finished benchmarking v79_sc and it shows Elo 2050.
- Log result: "v79_sc benchmark: Elo 2050, -69 vs v77_sc best (2119)"
- This triggers Opus escalation (>30 Elo regression)
- Call /askopus with the mandatory format (a-e)
- Immediately start orthogonal work (do NOT wait for Opus): check WS list, pick WS5 or WS3

#### Scenario B: Background agents running, foreground is free

**Decision tree:**
```
1. Check: What resource does the background task use? (GPU? CPU? Neither?)
2. Pick work that uses a DIFFERENT resource:
   - Background uses GPU (training) -> do CPU work: benchmarks, Codex tasks, code review, tests
   - Background uses CPU (benchmark) -> do code work: Codex implementation, analysis, documentation
   - Background uses neither (Codex agent) -> do anything: GPU training, benchmarks, analysis
3. If ALL resources are saturated by background tasks:
   - Do code-only work: write tests, review code, update configs, write specs for Codex
   - Code-only work has zero resource cost and always exists
4. NEVER poll background tasks. Wait for the completion notification.
```

**Example:** Training v80_sc is running on GPU (background). Codex agent is implementing WS5 (background).
- GPU busy, Codex busy. CPU is free.
- Start: run test suite (`uv run pytest -n auto`), or run a small benchmark, or implement a small code fix inline.

#### Scenario C: Tool error or permission denied

**Decision tree:**
```
1. Is this a transient error (network, timeout, file lock)?
   YES -> Retry once. If still fails, log the error and skip to alternate work.
   NO  -> Step 2

2. Is this a real permission/capability issue?
   YES -> Log it to autonomous_decisions.log with the exact error.
         Add "[blocked: <reason>]" prefix to the task in continuation_plan.json.
         Walk the Fallback Ladder to find alternate work.
   NO  -> Step 3

3. Is this a build failure or test failure?
   YES -> This IS the work. Debug and fix it. Do not skip past failures.
         If fix requires >30 lines or >2 files -> delegate to Codex.
         If fix requires understanding an experiment result -> /askopus.
   NO  -> Log the unexpected error and continue with Fallback Ladder.
```

**Example:** `cmake --build build-ninja -j` fails with a compilation error.
- This is a build failure. Read the error, identify the file and line.
- If it's a simple fix (typo, missing include): fix inline, rebuild.
- If it's complex (template error, linker issue): delegate to Codex with the error message.
- Do NOT skip the build failure and proceed to training -- that will use a stale binary.

#### Scenario D: Unclear specification or ambiguous task

**Decision tree:**
```
1. Can you make a safe assumption that preserves future options?
   YES -> Make the assumption, document it in a comment or log, proceed.
   NO  -> Step 2

2. Is this a research/strategy decision (what to run, what architecture)?
   YES -> /askopus with the specific ambiguity. Immediately do orthogonal work.
   NO  -> Step 3

3. Is this an implementation ambiguity (how to wire something)?
   YES -> Pick the simpler option. Add a TODO comment noting the ambiguity.
         Proceed with implementation. The user or Opus can redirect later.
   NO  -> Step 4

4. Is this a rules/game-mechanics question?
   YES -> Check docs/ts_rules_scoring.md and TS_Rules_Deluxe.pdf first.
         If still unclear -> /rules-batcher with the specific question.
   NO  -> Log the ambiguity, pick the safer path, proceed.
```

**Example:** continuation_plan.json says "DEFCON-aware reward shaping" but doesn't specify the penalty magnitude.
- This is a research decision -> /askopus: "What penalty coefficient for DEFCON-1 losses? Current DEFCON-1 rate is 6%. Options: -0.5 extra, -1.0 extra, or scaled by turns remaining."
- While waiting for Opus: start WS5 (binary freshness hook) or WS3 (checkpoint DB).

#### Scenario E: Waiting for a long-running background process

**Decision tree:**
```
1. DO NOT poll or tail logs. The tool notifies you on completion.
2. Check what resources are free (GPU, CPU, agent slots).
3. Start work on a different resource:
   - Code tasks (always available, zero resource cost)
   - Codex delegation (free, runs externally)
   - Analysis of existing results
   - Test suite maintenance
4. When the notification arrives:
   - Finish your current atomic unit of work (don't abandon mid-edit)
   - Process the background result
   - Update continuation_plan.json
   - Resume the Fallback Ladder
```

### 4. Self-Assigning from continuation_plan.json

**Protocol for reading and acting on the continuation plan:**

```
1. Read results/continuation_plan.json
2. Check active_background — are any tasks still running?
   YES -> Note them. Do not duplicate their work.
3. Check blocked_on — is anything blocked?
   YES -> Can you unblock it? If yes, do that first. If no, skip it.
4. Read next_tasks top-to-bottom. For each task:
   a. Is it blocked by a running background task? -> Skip
   b. Does it require a resource that's busy? -> Skip
   c. Does it require Opus judgment? -> /askopus, then do orthogonal work
   d. Is it actionable right now? -> START IT
5. After starting: update continuation_plan.json
   - Move the task to current_task
   - Remove it from next_tasks
   - Update last_updated timestamp
6. If ALL next_tasks are blocked or skipped:
   - Walk the Fallback Ladder from Step 4 (workstreams)
   - Add whatever you start to continuation_plan.json as current_task
```

**Example with the current plan:**
```json
"next_tasks": [
  "Wait for run_traced_game.py migration agent (a3c2559e) to complete",
  "WS10 ISMCTS: search budget sweep (200/400/800 sims)",
  "Pragmatic Heads Phase 3: Ask Not + Our Man in Tehran PolicyCallback",
  "Next training run: v80_sc from v55 checkpoint",
  "Consider DEFCON-aware reward shaping"
]
```

Walking this list:
1. "Wait for migration agent" -> Background task, skip (do not idle waiting)
2. "WS10 ISMCTS search budget sweep" -> CPU-intensive. Is GPU busy with training? If yes, skip (CPU conflict with training data loading). If no, start this.
3. "Pragmatic Heads Phase 3" -> Code task. Delegate to Codex. Start immediately.
4. "Next training run v80_sc" -> GPU task. Is GPU free? If yes, start. If no, skip.
5. "DEFCON-aware reward shaping" -> Research decision. /askopus, then orthogonal work.

Result: Start item 3 (Codex delegation) and item 4 (if GPU is free) simultaneously. They use different resources.

### 5. What "Reasonable Work" Means at Each Priority Tier

**Tier 1 — Direct experiment progress (highest value):**
- Launch the next planned training run
- Export a checkpoint and benchmark it
- Process benchmark results and update Elo ladder
- Implement a feature that the next training run needs

**Tier 2 — Infrastructure that accelerates experiments:**
- Implement binary freshness hook (WS5) -- prevents stale-binary regressions
- Checkpoint identity DB (WS3) -- prevents lost provenance
- Overlapping confirmation games (WS7) -- saves wall-clock time
- Snakemake pipeline updates (WS2) -- automates train-export-bench chains

**Tier 3 — Code quality that prevents future waste:**
- Run test suite, fix any failures
- Add tests for untested critical paths
- Fix known TODOs in the codebase
- Extract shared utilities (WS6)

**Tier 4 — Analysis and documentation (only from existing results):**
- Analyze benchmark results that haven't been logged
- Write up a root-cause analysis for a recent regression
- Update experiment log with missing entries

**Tier 5 — Lowest priority (only when truly nothing else):**
- Code formatting and linting
- Updating comments and docstrings
- Reorganizing file structure

**What is NOT reasonable work:**
- Sitting idle waiting for user input
- Presenting options without choosing one
- Re-reading files you already read this session (unless checking for changes)
- Writing documentation for its own sake (not tied to results)
- Refactoring unrelated code "while here"
- Running experiments without a hypothesis
- Launching duplicate work that a background agent is already doing

### 6. Truly Blocked vs. Apparently Blocked

**Truly blocked (should defer/escalate):**
- GPU is busy AND the only remaining work requires GPU -> defer to after GPU frees up, but do CPU/code work now
- Opus escalation is pending AND the only remaining work is in the affected training lineage -> work on orthogonal lineages/workstreams
- A critical build is broken AND no one can fix it (e.g., external dependency down) -> log it, work on unrelated code
- All resources (GPU + CPU) are fully saturated by existing tasks -> do code-only work (write tests, specs, configs)

**Apparently blocked (should find side work — these are NOT real blocks):**
- "I finished my task" -> Not blocked. Walk the Fallback Ladder.
- "I'm waiting for a background task" -> Not blocked. Start parallel work on different resource.
- "The next task is unclear" -> Not blocked. Make a safe assumption or /askopus and do orthogonal work.
- "I don't know what to work on" -> Not blocked. Read continuation_plan.json and workstream list.
- "A test failed" -> Not blocked. Debugging the failure IS the work.
- "A build failed" -> Not blocked. Fixing the build IS the work.
- "I need Opus but budget is >90%" -> Not blocked. Defer the Opus question (add to plan with [defer-to-opus] prefix) and do non-Opus work.

**The key test:** "Is there ANY productive action I can take right now that doesn't conflict with running tasks?" The answer is almost always yes. Code work (writing tests, implementing features, fixing bugs, delegating to Codex) has zero resource cost and infinite supply.

### 7. The Commit Rhythm

Autonomous agents must commit frequently to avoid losing work:
- After completing any logical unit of work -> commit
- Before switching to a different workstream -> commit current work
- Every 30 minutes of continuous coding -> commit with WIP prefix if incomplete
- Before session end -> commit everything uncommitted

This is pre-authorized per standing rules. Never ask for permission to commit.

### 8. The 30-Second Rule

When a task finishes and the agent is deciding what to do next, the entire decision process (reading plan, checking resources, choosing task, starting it) should take under 30 seconds of wall time. If the agent finds itself spending multiple turns deliberating, it's violating the policy. Pick something and go. The user will redirect if the choice is wrong.

### 9. Session End Protocol

Even when ending a session (context limit, user request), the agent must:
1. Commit all uncommitted work
2. Update continuation_plan.json with current state, what's running, what's next
3. Log any unprocessed results or pending decisions
4. NEVER end with "let me know what you'd like to do next" -- end with "continuation plan updated, next session should start with X"

## Conclusions

1. **The never-idle invariant is enforced by a 9-step fallback ladder** that agents walk top-to-bottom at every decision point. The ladder guarantees there is always actionable work unless every resource (GPU, CPU, and code-editing capacity) is fully saturated -- a state that essentially never occurs.

2. **"Blocked" almost always means "apparently blocked."** True blocks require all resources to be saturated AND all orthogonal workstreams to be exhausted. Agents that claim to be blocked should be audited -- in almost every case, code work (tests, Codex delegation, implementation) is available at zero resource cost.

3. **The 30-second rule prevents analysis paralysis.** Agents must not spend multiple turns deliberating what to do. Read the plan, check resources, pick the first applicable item from the ladder, and execute.

4. **Self-assignment from continuation_plan.json follows a strict protocol:** walk next_tasks top-to-bottom, skip blocked/resource-conflicting items, start the first actionable item, update the plan. If all next_tasks are blocked, fall through to workstreams (Step 4 of the ladder).

5. **Every blocking scenario has a prescribed response.** Task done: walk the ladder. Background running: parallel work on different resource. Tool error: retry once then alternate work. Unclear spec: safe assumption or /askopus plus orthogonal work. Build/test failure: debugging IS the work.

6. **"Reasonable work" is defined by five priority tiers,** from direct experiment progress (highest) to code formatting (lowest). Work not tied to experiment progress, infrastructure, or code quality is not reasonable. Writing documentation for its own sake, presenting options menus, or running hypothesis-free experiments are all violations.

7. **The policy integrates with the existing standing policy** (sections 2, 5, 7, 12) rather than replacing it. This document provides the missing decision tree that operationalizes the "never idle" principle from section 7 into concrete agent behavior.

## Recommendations

1. **Add a reference to this document in the standing policy section 7** ("Always-running rule") as the detailed decision tree for the never-idle invariant.

2. **Add the Fallback Ladder as a checklist** to the OODA session-start procedure (standing policy section 7) so every session starts by walking it.

3. **Instrument the 30-second rule** by logging timestamps in autonomous_decisions.log when a task ends and when the next task starts. If the gap exceeds 60 seconds in any logged session, audit why.

4. **Add a "blocked_reason" field to continuation_plan.json** entries so agents must explicitly justify skipping a task, making "I couldn't find work" auditable.

5. **Periodically audit agent behavior** (standing policy section 10) against this policy. Specific violations to check: responses ending in questions, responses with no tool calls, gaps between task completion and next task start.

## Open Questions

1. **Should the fallback ladder be configurable per session?** The user might want to override priority order (e.g., "prioritize WS10 over training today"). Currently, the ladder is fixed. A `priority_override` field in continuation_plan.json could handle this.

2. **How should agents handle the case where continuation_plan.json itself is stale or corrupt?** Currently there's no fallback if the plan file is missing or unparseable. Recommendation: if plan is unreadable, fall through directly to workstream list (Step 4 of the ladder).

3. **Should there be a maximum number of Codex agents running simultaneously?** The policy allows spawning Codex for every code task, but too many concurrent agents could cause merge conflicts even with worktree isolation. A soft cap of 3 concurrent Codex agents might be prudent.
