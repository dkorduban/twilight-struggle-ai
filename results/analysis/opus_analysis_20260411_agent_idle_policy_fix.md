# Opus Analysis: Agent Idle / Policy Gap on post_train_confirm
Date: 2026-04-11
Question: Why did Sonnet idle after launching post_train_confirm.sh, and what policy changes prevent recurrence?

## Executive Summary

Sonnet launched `post_train_confirm.sh` as a shell background process (`&`) instead of using `run_in_background=true` on the Bash tool, then immediately polled the log with `tail`. This violated existing policy Section 5 ("ALL benchmarks: `run_in_background=true`", "Don't sleep/poll") and Section 6 ("don't poll -- wait for notification"). The script itself ran a full round-robin Elo tournament across 38 models (703 pairs, 137 new matches at 400 games each = ~54,800 games), because the script unconditionally enumerates every model in `scripted_for_elo/` with no scope limit. Two policy gaps enabled this: (1) no rule requiring script review before first execution, and (2) no rule capping the scope of post-training confirmation tournaments.

## Findings

### What post_train_confirm.sh actually does (and why 137 matches)

The script (`scripts/post_train_confirm.sh`) has three stages:

1. **Confirmation tournament** (via `ppo_confirm_best.py`): Picks the best checkpoint from a training run by playing it against 3 fixture models + heuristic. This was SKIPPED for v66_sc because `panel_eval_history.json` was missing.

2. **Copy scripted checkpoint**: Copies `ppo_best_scripted.pt` into `data/checkpoints/scripted_for_elo/`.

3. **Full Elo ladder update** (via `run_elo_tournament.py`): Dynamically builds a model list from ALL `*_scripted.pt` files in `scripted_for_elo/`, filters out corrupted-era models (v27-v41) and pre-v8, then runs `--schedule round_robin --games 400` across the entire pool.

The 137 new matches come from the math: 38 models in round-robin = C(38,2) = 703 total pairs. With 566 cached from prior runs, 137 pairs were new. The new models (`bc_wide384`, `v55_sc`, `v66_sc`) each needed to play every existing model. At 400 games per match: 137 * 400 = 54,800 games, which takes roughly 1 hour on this hardware.

The script's design is fundamentally flawed for post-training use: it runs a FULL ladder update when only incremental Elo placement of the new model is needed.

### What policy rules were violated

**Section 5, Rule 1**: "ALL benchmarks: `run_in_background=true`. No exceptions." The Elo tournament is functionally a benchmark. Sonnet ran it with shell `&` instead of the Bash tool's `run_in_background=true` parameter, which would have provided a proper completion notification.

**Section 5, Rule 5**: "After launching background work, immediately respond to the user with what was launched and estimated time. Don't sleep/poll." Sonnet immediately ran `tail -20` on the log file -- this is polling, not waiting for notification.

**Section 6, Rule 3**: "Background agents must be non-blocking. Use `run_in_background=true` and don't poll -- wait for notification."

**Section 7, Rule "Never be idle"**: The agent was stuck in a poll loop instead of doing productive work while the tournament ran.

### What policy rules were missing

1. **No "review before first run" rule.** The policy has a pre-launch checklist for training runs (Section 2) but nothing requiring the agent to READ a script before executing it for the first time. Sonnet wrote `post_train_confirm.sh` earlier in the session and then ran it without re-reading it to verify what it would do. A rule requiring `cat` or `Read` of any script before first execution would have caught the 38-model round-robin scope issue.

2. **No scope cap on confirmation tournaments.** The post-training Elo check (Section 2, "Post-training Elo check") says: "Run candidate confirmation tournament vs previous best + 2 fixture models (200 games/match)." This correctly limits scope to ~3-5 opponents. But the SCRIPT ignores this and runs a full round-robin across ALL models. There is no policy rule that says "confirmation scope must match what Section 2 specifies" or "never run full-ladder round-robin as a post-training step."

3. **No dry-run / scope-check rule for tournament scripts.** There should be a rule: before running any Elo/tournament script, first check how many matches it will schedule (e.g., run with `--dry-run` or inspect the model list). 137 matches should have been flagged as excessive for a post-training confirmation.

4. **No "shell & is banned" rule.** The policy says to use `run_in_background=true` but does not explicitly prohibit the shell `&` workaround. Sonnet may have used `&` to technically "not block" while retaining the ability to poll, which defeats the purpose.

### Root cause chain

```
Root cause 1: Script scope
  post_train_confirm.sh unconditionally runs full round-robin on ALL models in scripted_for_elo/
  -> 38 models -> 703 pairs -> 137 new matches -> ~1 hour runtime
  -> The script should have done INCREMENTAL Elo (new model vs N nearest neighbors)

Root cause 2: No script review
  Sonnet did not re-read the script before running it
  -> Did not notice the full round-robin scope
  -> No policy rule required reviewing a script before first execution

Root cause 3: Shell & instead of run_in_background
  Sonnet used `bash ... &` (shell background) instead of run_in_background=true
  -> No automatic completion notification
  -> Agent resorted to log polling (tail) to check status
  -> Polling left the agent stuck, unable to do useful work

Root cause 4: No kill-on-scope-surprise
  When the log showed "137 new matches", the agent should have recognized this as excessive
  -> Should have killed the process and re-run with smaller scope
  -> No policy rule about scope validation after launch
```

## Conclusions

1. **Three existing policy rules were violated**: background tool usage (Section 5), no-polling (Sections 5 and 6), and the non-idle mandate (Section 7). These are clear, unambiguous rules that Sonnet bypassed.

2. **The script itself is the deeper problem**: `post_train_confirm.sh` runs a full O(N^2) round-robin on the entire model zoo when it should do an incremental placement (~5-8 targeted matches for the new model only). Even if Sonnet had used `run_in_background=true` correctly, 54,800 games is still a ~1 hour CPU monopoly for what should be a 5-minute spot check.

3. **No rule required reading the script before running it.** This is a significant gap. The pre-launch checklist (Section 2) covers hyperparameters, architecture, data, seeds, and hypotheses for training runs, but has no analog for "verify what a script will do before executing it for the first time."

4. **Shell `&` is a policy-evasion vector.** Using shell backgrounding instead of the tool's `run_in_background=true` removes the notification mechanism and encourages polling. The policy should explicitly ban `&` for long-running processes.

5. **The 137-match scope should have been caught even after launch.** The log clearly printed "137 new" before starting. A scope-aware agent would have killed the process immediately.

## Recommendations

Add the following to `feedback_standing_policy.md`:

### Addition to Section 2 (Experiment Governance): new subsection "Script review before first execution"

```
### Script review before first execution (MANDATORY)
Before running ANY script for the first time (or after modifying it), the agent MUST:
1. Read the script with the Read tool to understand what it will do
2. Verify the scope: how many games, how many models, how many matches, estimated runtime
3. If scope exceeds the intended use case (e.g., full round-robin when only incremental
   placement is needed), fix the script or add flags to limit scope BEFORE running it
4. Log the expected scope to autonomous_decisions.log BEFORE launching

"I wrote this script earlier so I know what it does" is NOT an acceptable excuse to skip
the read. Scripts may have been modified by other agents, or the data they enumerate
(model directories, fixture lists) may have grown since writing.
```

### Addition to Section 5 (Non-Blocking Main Agent): new rule "Shell & is banned"

```
### Shell backgrounding (&) is banned for long-running processes
NEVER use shell `&` to background a long-running process. ALWAYS use
`run_in_background=true` on the Bash tool call. Shell `&` removes the automatic
completion notification and forces polling, which blocks the main agent.

The ONLY acceptable use of `&` is inside a script that the Bash tool itself runs with
`run_in_background=true` (i.e., the outer call uses the tool parameter, inner `&` is
for process management within the script).
```

### Addition to Section 5: explicit polling ban

```
### No log polling (NEVER tail/cat/grep a log to check if a background process finished)
After launching a background task with `run_in_background=true`, do NOT:
- `tail -f` or `tail -N` the log file
- `cat` the log file repeatedly
- `grep` for completion markers
- `sleep` + check loops

The tool provides a completion notification. Wait for it. While waiting, do other
productive work (different resource, different subsystem).
```

### Addition to Section 2: post-training Elo scope cap

```
### Post-training Elo confirmation scope
Post-training Elo confirmation (§2 "Post-training Elo check") MUST use incremental
placement, NOT full round-robin:
- New model plays ONLY: previous best, 2 fixture models, heuristic (= 4-5 matches max)
- 200 games per match (not 400)
- Estimated runtime: <5 minutes, not >1 hour
- Full-ladder round-robin updates are a SEPARATE, explicitly-requested task, never
  triggered automatically after training

If post_train_confirm.sh or run_elo_tournament.py would schedule >20 new matches,
STOP and verify scope before proceeding. >20 new matches is ALWAYS wrong for a
post-training confirmation.
```

### Script fix: post_train_confirm.sh

The script itself should be fixed to support incremental mode. Recommendation:
- Add a `--incremental` flag (default for post-training) that only plays the new model
  vs the top-5 nearest models + heuristic
- Reserve `--full` for explicit full-ladder updates requested by the user
- Add `--dry-run` to print the match schedule without executing

## Open Questions

1. **Should the full round-robin ever run automatically?** Current recommendation: no. Full ladder updates should be explicit user requests or scheduled tasks, never triggered by post-training hooks.

2. **Should the policy mandate `--dry-run` for all tournament scripts?** This would add friction but catch scope issues reliably. Alternative: just mandate reading the script + checking model count before launch.

3. **Is there value in a "scope guard" that kills any tournament scheduling >N matches without explicit override?** This could be implemented in `run_elo_tournament.py` itself (e.g., `--max-new-matches 20` with `--force` to override).
