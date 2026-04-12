# Opus Analysis: Fixing Sonnet Autonomy Regression
Date: 2026-04-12T06:30:00Z
Question: The main Sonnet agent's autonomy has regressed after a policy change landed. In the past it could work overnight without asking the human and mostly not get stuck. Now it often does something and stops. The desired behavior is: follow the plan, use /askopus if something is suspicious or requires judgment, then follow what Opus says — but never stop and wait for the human. How do we fix this?

## Executive Summary

The autonomy regression is caused by several "hard stop" rules in the standing policy (feedback_standing_policy.md) that were added in §2 and §12 during the WS11 Sonnet-Opus escalation protocol work. Specifically, three rules tell Sonnet to "DO NOT launch the next experiment until Opus responds" — which in practice means Sonnet stops ALL work and waits, because it interprets "do not launch" as "do not do anything." The fix is surgical: change the hard-stop rules to "do not launch the next experiment *in the same training lineage*" (already partially stated in §12 but contradicted by §2), and add an explicit "continue orthogonal work while waiting" directive that is unambiguous and mandatory.

## Findings

### What changed in the policy

The WS11 work (2026-04-11) added §12 "Sonnet-Opus Coordination Protocol" and strengthened §2 "Experiment Governance Rules" with hard-stop escalation triggers. Three specific sentences create "escalation traps" where Sonnet stops and becomes idle:

**Trap 1 — §2, line 101:**
> `**Do NOT launch the next experiment until Opus responds.**`

This is the most damaging rule. It appears immediately after the mandatory escalation trigger list. Sonnet reads this as a blanket prohibition on doing ANYTHING, not just "don't launch the next experiment in the affected lineage." The rule doesn't say "continue other work" — it just says stop.

**Trap 2 — §2, line 121 (Aggressive plateau response):**
> `3. Only resume after Opus provides a concrete, novel change to try`

Same pattern: "only resume" with no carve-out for orthogonal work.

**Trap 3 — §12, line 541:**
> `**DO NOT launch the next experiment until Opus has responded to the escalation.**`

This is a duplicate of Trap 1, placed in the new §12. It reinforces the stop behavior.

### Root cause analysis

**The core problem is contradictory instructions.** The policy has two competing directives:

1. §7 (line 398-399): "**Default mode is autonomous. The system must NEVER be idle.** Don't stop to ask the user what to do next."
2. §2 (line 101) + §12 (line 541): "**Do NOT launch the next experiment until Opus responds.**"

When an escalation trigger fires, Sonnet faces an impossible choice: §7 says never be idle, but §2/§12 says stop until Opus responds. In practice, the more specific rule (§2/§12) wins, and Sonnet stops.

**§12's "Waiting protocol" (lines 563-567) partially addresses this:**
> "After dispatching /askopus: continue unrelated background work if available"
> "If Opus takes >20 min: check if there is orthogonal work to do"

But this is buried in a subsection, uses hedging language ("if available"), and is contradicted by the absolute language of the hard-stop rules above it. Sonnet gives priority to the explicit "DO NOT" over the softer "continue if available."

**The /askopus skill itself is non-blocking** — it launches Opus as a background agent and returns immediately. The skill is correctly designed. The problem is entirely in the policy text that tells Sonnet what to do AFTER calling /askopus.

**The continuation_plan.json mechanism is working.** The SessionStart hook correctly injects it. The plan has `next_tasks` and `blocked_on: null`. This is fine and not part of the problem.

**Additional contributing factor — "ask only if" in §7 (line 439):**
> "Ask only if: about to do something destructive/irreversible (delete data, force-push), or the plan is exhausted and no clear next step exists"

The phrase "plan is exhausted and no clear next step exists" can be over-applied. If Sonnet just hit an escalation trigger and the plan's remaining items are all experiments, it may conclude the plan is "exhausted for things I'm allowed to do" and stop. The fix should explicitly state that infrastructure work (WS2-WS10), code cleanup, tests, and Codex implementation tasks are always available as orthogonal work.

### What the ideal behavior loop looks like

The correct autonomous loop should be:

1. **Read continuation_plan.json** at session start — pick up where we left off.
2. **Execute the highest-priority task** from the plan.
3. **If an escalation trigger fires** (Elo regression, plateau, unexpected result):
   a. Call `/askopus` with the mandatory format (a-e).
   b. `/askopus` launches a background Opus agent — returns immediately.
   c. **Mark only the affected training lineage as blocked** in continuation_plan.json (`blocked_on: "awaiting Opus on v66_sc regression"`).
   d. **Immediately switch to orthogonal work**: infrastructure workstreams (WS2-WS10), Codex implementation tasks, code quality, tests, benchmark analysis, documentation updates.
   e. **Never idle.** If truly nothing orthogonal exists (unlikely), work on the lowest-risk item from the plan with a note that it may be revised by Opus.
4. **When Opus responds** (background task notification):
   a. Read the analysis file.
   b. Update continuation_plan.json with Opus's recommendation.
   c. Resume the previously-blocked training lineage.
   d. Report to the user in 1-3 lines only if the Opus recommendation changes the plan.
5. **Commit often.** Every completed task or meaningful intermediate result.
6. **Never present options, never ask questions, never stop.**

### Specific policy text that needs changing

#### Change 1 — §2 Mandatory Opus escalation triggers (line 101)

**Current text:**
```
**Do NOT launch the next experiment until Opus responds.**
```

**Proposed replacement:**
```
**Do NOT launch the next experiment in the same training lineage until Opus responds.**
While waiting for Opus, immediately switch to orthogonal work: infrastructure workstreams,
Codex implementation tasks, tests, code cleanup, or any plan item that does not depend on
the escalation answer. NEVER be idle while waiting for Opus — the /askopus skill is
non-blocking by design.
```

#### Change 2 — §2 Aggressive plateau response (line 121)

**Current text:**
```
3. Only resume after Opus provides a concrete, novel change to try
Never train >2 versions past a plateau without analysis.
```

**Proposed replacement:**
```
3. Only resume training in the plateaued lineage after Opus provides a concrete change.
   While waiting, work on orthogonal tasks (infrastructure, tests, other workstreams).
Never train >2 versions past a plateau without analysis.
```

#### Change 3 — §12 line 541

**Current text:**
```
**DO NOT launch the next experiment until Opus has responded to the escalation.**
```

**Proposed replacement:**
```
**Do NOT launch the next experiment in the affected training lineage until Opus responds.**
This does NOT mean stop all work — continue orthogonal tasks immediately (see §7).
```

#### Change 4 — §12 Waiting protocol (lines 563-567)

**Current text:**
```
### Waiting protocol
- After dispatching `/askopus`: continue unrelated background work if available (e.g., run WS5/WS6 tasks)
- Do NOT start the next experiment in the same training lineage until Opus responds
- If Opus takes >20 min: check if there is orthogonal work to do (different subsystem, tests, docs)
- When Opus finishes (notification): immediately read its output, update continuation_plan, resume
```

**Proposed replacement:**
```
### Waiting protocol (MANDATORY — never idle while waiting for Opus)
- After dispatching `/askopus`: **immediately** start orthogonal work. Examples: infrastructure
  workstreams (WS2-WS10), Codex implementation tasks, tests, code cleanup, benchmark analysis.
  "No orthogonal work available" is almost never true — check the workstream list.
- Do NOT start the next experiment in the same training lineage until Opus responds.
- When Opus finishes (background task notification): immediately read output, update
  continuation_plan.json, unblock the affected lineage, and resume.
- **The only acceptable reason to be idle is if the machine is fully saturated (GPU + CPU at
  >95%) AND there is no code/test/doc work to do.** This should essentially never happen.
```

#### Change 5 — §7 "When to proceed vs. when to ask" (add after line 441)

**Add this new bullet:**
```
- **NEVER stop working because of an Opus escalation.** `/askopus` is non-blocking.
  After calling it, continue orthogonal work. The escalation only blocks the specific
  training lineage that triggered it, not the entire session.
```

#### Change 6 — feedback_autonomous_night.md (add to the end)

**Add:**
```
**Opus escalation does NOT mean stop.** If an escalation trigger fires overnight,
call `/askopus`, then continue on orthogonal workstreams. Never wait idle for Opus.
The user cannot respond overnight either, so stopping is the worst possible outcome.
```

## Conclusions

1. The autonomy regression is caused by three "hard stop" sentences in §2 and §12 of the standing policy that tell Sonnet to not proceed until Opus responds, without explicitly requiring orthogonal work during the wait.
2. The §12 "Waiting protocol" partially addresses this but uses hedging language ("if available") that is overridden by the absolute "DO NOT" commands above it.
3. The /askopus skill itself is correctly designed as non-blocking — the problem is purely in the post-escalation behavioral rules.
4. The continuation_plan.json mechanism and SessionStart hook are working correctly and are not contributing to the problem.
5. The fix requires six targeted text edits across two files (feedback_standing_policy.md and feedback_autonomous_night.md) that add "continue orthogonal work" as a mandatory companion to every "do not proceed" rule.
6. The key insight is: escalation should block **one training lineage**, not **all work**. This distinction is currently missing from the policy.

## Recommendations

1. Apply all six text changes listed above to `feedback_standing_policy.md` and `feedback_autonomous_night.md`. These are the minimum viable fix.
2. After applying, do a quick grep for any other "wait", "stop", "do not proceed", or "do not launch" phrases in the policy that might create additional traps. Fix any found.
3. Add a "Never Idle" invariant check: consider adding a line to the SessionStart hook that reminds Sonnet: "If you find yourself about to stop and wait, re-read §7 — you must always be doing something."
4. Consider adding a concrete "orthogonal work menu" to continuation_plan.json (a field like `"orthogonal_tasks": [...]`) so Sonnet always has an explicit fallback list when the main lineage is blocked.
5. Test the fix by running an overnight session and verifying the agent continues working after an escalation trigger fires.

## Open Questions

1. Are there other files beyond feedback_standing_policy.md and feedback_autonomous_night.md that contain stop-and-wait rules? A grep for "until Opus" across all memory files would confirm.
2. Does the `defaultMode: "acceptEdits"` in settings.json interact with this? If Sonnet hits a permission prompt during autonomous work, that could also cause a stop. The `skipDangerousModePermissionPrompt: true` in the global config helps, but the `ask` list (git push, gh, rm, mv, cp -r) could still block overnight.
3. Should the policy explicitly pre-authorize certain "ask" operations for autonomous overnight mode? For example, git push after committing results.
