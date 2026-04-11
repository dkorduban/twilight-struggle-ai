---
# Opus Analysis: Workstreams and Policy for Sonnet
Date: 2026-04-11
Question: Based on feedback-20260411.md, what workstreams + policy changes should Sonnet follow?

## Executive Summary

The user's feedback identifies a pattern of preventable failures: training runs regress silently, GPU idles while agents wait, the pipeline is fragile and ad-hoc, experiment tracking is incomplete, and tech debt accumulates unchecked. The root cause is not individual bugs but the absence of a systematic meta-algorithm — Sonnet reacts to symptoms instead of following a disciplined loop. The fix is to codify a tight observe-orient-decide-act (OODA) loop for the main agent, add automated guardrails (hooks, watchdogs, DB logging), and make the pipeline deterministic and self-healing through proper orchestration and checkpoint identity.

## Findings

### Theme 1: Meta-algorithm failure (feedback §1)
The main agent juggles too many responsibilities without a priority-driven loop. Specific symptoms:
- Training dies and the agent does not notice for 30+ minutes.
- Models plateau for 5+ versions (v56-v62 all regressed from v55, yet the loop kept launching new versions).
- When regression is detected, agent tries quick fixes (restart, kill, restart again — see v64's five restarts in autonomous_decisions.log) instead of escalating to Opus for root-cause analysis.
- User questions derail ongoing work because there is no continuation plan.

### Theme 2: Pipeline fragility (feedback §2)
- Training crashes require manual restart with carefully reconstructed args (ppo_restart.sh helps but is reactive).
- No unique checkpoint identity — models can overwrite each other, and it is hard to trace how a checkpoint was created.
- W&B run IDs are not enforced as unique — runs can append to existing ones, corrupting metrics.
- No relational metadata store — win counts, lineage, hyperparams scattered across JSON files, log files, and W&B.
- Snakemake was tried with "relative success" but abandoned. The pipeline reverted to ad-hoc bash.

### Theme 3: Experiment tracking gaps (feedback §3)
- Experiment log is incomplete — missing git SHA, exact command, W&B ID, hypothesis for many runs.
- Model lineage is lost after branching (e.g., adding SmallChoiceHead = new lineage, but numbering continued from old).
- Plateau detection is too conservative — v56-v62 were all near-identical models below v55's Elo.

### Theme 4: Regressions (feedback §4)
- Unrebuilt C++ binary caused v65 to crash three times before the root cause (stale tscore.so) was found.
- Incomplete cross-codebase changes: Python code updated but C++ bindings not rebuilt, or model architecture changed but checkpoint loading code not updated.
- Not enough tests, especially pre-change regression tests.

### Theme 5: Tech debt (feedback §5)
- Code duplication across train_ppo.py, train_baseline.py, and benchmark scripts (constants, model loading, feature encoding).
- Ambiguous terminology: "tournament" means both Elo round-robin and candidate confirmation match.
- Interfaces not clean enough to swap agents/models without surgery.

### Theme 6: Performance underinvestment (feedback §6)
- Agents accept long wait times (30min benchmark, 2hr ISMCTS) without analyzing speedup opportunities.
- Confirmation/candidate games could overlap with training but are run sequentially.
- CPU parallelism underutilized — machine has 20 vCPUs but many tasks use <10.

### Theme 7: High-level direction (feedback §7-8)
- Engine completeness (100% rules, all cards, mid-AR side changes).
- Agent expressiveness (head design for all choice types).
- Strength (inputs, trunk, search).
- ISMCTS validation: find minimum search budget that exploits DEFCON, verify correctness, then train against it.

## Workstreams

### WS1: Meta-Algorithm — OODA Loop for Sonnet
**Goal:** Replace reactive firefighting with a disciplined observe-orient-decide-act cycle that prevents silent failures.

**Steps:**
1. Define a "health check" protocol that Sonnet runs after every PPO iteration completes (not just at session start). Check: (a) did Elo improve vs previous version? (b) is Elo above the current best? (c) did training loss diverge? (d) is GPU utilized?
2. Define escalation triggers: if Elo drops >30 points from best, or 2 consecutive versions below best, or any crash/restart — immediately /askopus before launching next version.
3. Define a "continuation plan" data structure: a TODO list stored in `results/continuation_plan.json` that survives context resets. Sonnet reads it at session start and after every background task completes.
4. User questions do NOT clear the continuation plan — Sonnet answers the question, then resumes the plan.

**Success metric:** Zero instances of 3+ consecutive versions below best without Opus escalation. Continuation plan always has next steps.

### WS2: Pipeline Orchestration — Revive and Extend Snakemake
**Goal:** Make the train > export > benchmark > Elo-update chain declarative, resumable, and crash-resilient.

**Steps:**
1. Revive the existing Snakefile. Add rules for: train_ppo (one iteration batch), export_scripted, benchmark_side, elo_update.
2. Add a `confirm` rule that runs candidate confirmation games overlapping with the next training iteration (not sequentially).
3. Add crash recovery: if a rule fails, Snakemake retries once with `--restart-times 1`, then logs the failure and halts that chain (not the whole pipeline).
4. All Snakemake invocations run via `run_in_background=true`.
5. Deprecate manual `nohup ... &` launches for PPO training.

**Success metric:** All PPO runs launched via Snakemake. Zero manual restarts needed for recoverable crashes.

### WS3: Checkpoint Identity and Metadata DB
**Goal:** Every checkpoint is uniquely identifiable and traceable.

**Steps:**
1. Define checkpoint ID = `{name}_{git_short_sha}_{wandb_run_id}_{file_sha256[:8]}`.
2. Create `results/metadata.sqlite3` with tables: `checkpoints` (id, name, git_sha, wandb_id, parent_id, file_hash, created_at), `benchmarks` (checkpoint_id, opponent, side, games, wins, draws), `elo_ratings` (checkpoint_id, elo, timestamp).
3. Write a `log_checkpoint()` Python function called at checkpoint save time in train_ppo.py. Logs all hyperparams + ID to both SQLite and W&B.
4. Write a `log_benchmark()` function called at benchmark completion. Logs results to SQLite.
5. Backup: `results/metadata.sqlite3` is committed to git after every Elo update.

**Success metric:** `SELECT * FROM checkpoints WHERE name LIKE 'v%'` returns every checkpoint ever created with full lineage.

### WS4: Experiment Tracking Discipline
**Goal:** Experiment log is always complete and machine-readable.

**Steps:**
1. Create `results/experiments.jsonl` as the canonical machine-readable log. Each line: `{name, hypothesis, git_sha, command, wandb_id, started_at, finished_at, result_summary}`.
2. Add a `log_experiment_start()` call at PPO launch and `log_experiment_end()` at completion.
3. Sonnet must write a 1-sentence hypothesis before launching any experiment. If it cannot articulate why the experiment should help, it must /askopus first.
4. Enforce lineage: when a branch point occurs (new head, new features, new data), reset version numbering with a prefix (e.g., `sc_v0` for SmallChoiceHead branch).
5. Plateau rule: if 2 consecutive versions fail to beat current best Elo, stop the current approach and /askopus.

**Success metric:** Every experiment in experiments.jsonl has all fields populated. Zero "orphan" runs not in the log.

### WS5: Regression Prevention — Pre-Change Validation
**Goal:** Catch regressions before they waste GPU hours.

**Steps:**
1. Add a `SessionStart` hook that runs: `cmake --build build-ninja -j 2>/dev/null && python -c "import tscore; print(tscore.__file__)"` — ensures C++ bindings are fresh at session start.
2. Add a pre-training smoke test in train_ppo.py: before the first iteration, run 10 games with the checkpoint and verify they complete without error. Log the 10-game win rate as a sanity check.
3. Before any architecture change (new head, new features), run the existing benchmark (100 games) as a pre-change baseline. Store in `results/pre_change_baseline.json`.
4. After the change + first training, run the same benchmark. If result is >5pp worse than baseline, halt and /askopus.
5. Add `uv run pytest -x -q tests/` to the PostToolUse hook for `.py` files (extend run-targeted-checks.py to run pytest on relevant test files, not just py_compile).

**Success metric:** Zero regressions from stale binaries. Zero regressions shipped without a pre-change baseline.

### WS6: Tech Debt Reduction — Shared Library Extraction
**Goal:** Reduce code duplication and clarify interfaces without breaking anything.

**Steps:**
1. Extract shared constants (CARD_SLOTS, COUNTRY_SLOTS, SCALAR_DIM, MODE_*, DEFCON_LOWERING_CARDS, VALID_COUNTRY_IDS) into `python/tsrl/constants.py`. Import everywhere.
2. Extract model loading/creation into `python/tsrl/model_factory.py` — single function that takes a config dict and returns a model. Used by train_ppo.py, train_baseline.py, benchmark scripts.
3. Extract feature encoding into `python/tsrl/features.py` — shared between training and inference.
4. Create a terminology glossary in `docs/glossary.md`: define "league tournament" vs "confirmation tournament" vs "Elo round-robin" vs "candidate selection".
5. Do this incrementally: one extraction per commit, with tests passing after each.

**Success metric:** Zero duplicated constant definitions. Model creation has a single entry point.

### WS7: Performance — Overlapping Confirmation Games with Training
**Goal:** Cut PPO iteration wall-clock by overlapping confirmation/candidate games with the next training iteration.

**Steps:**
1. After each PPO iteration saves a checkpoint, immediately launch confirmation games in background (CPU-only) while the next iteration trains (GPU).
2. Confirmation results are read at the start of the iteration after next (or when they finish, whichever is later).
3. Implement this in the Snakemake pipeline as a parallel rule dependency.
4. Tune CPU parallelism: confirmation games should use `nice -n 15` and pool_size=16 (leaving 4 cores for training data loading).
5. Profile the current bottleneck: is it GPU (training), CPU (rollout collection), or sequential confirmation? Act on the actual bottleneck.

**Success metric:** Confirmation games add <2 minutes to the total PPO iteration time (currently they add 10+ minutes sequentially).

### WS8: Performance — CPU Saturation Audit
**Goal:** Ensure all CPU-heavy tasks utilize available cores.

**Steps:**
1. Profile current rollout collection: how many of the 20 vCPUs are used? If <16, increase `--rollout-workers`.
2. Profile benchmark: current pool_size=32 processes — are they all active? Check with `htop` during a benchmark run.
3. Profile Elo tournament: how many concurrent games? Increase if CPU is not saturated.
4. Document the resource profile of each task in a table (like standing_policy §3 but updated with current numbers).

**Success metric:** All CPU-heavy tasks use >80% of available CPU during their peak phase.

### WS9: Automated Watchdogs and Hooks
**Goal:** Automate the policies that Sonnet currently must remember manually.

**Steps:**
1. Add a `Stop` hook that writes the continuation plan to `results/continuation_plan.json` before the session ends.
2. Add a `SessionStart` hook that reads `results/continuation_plan.json` and injects it as a system message.
3. Extend the memory watchdog to also check for stale training (no checkpoint written in >45 minutes = possible hang).
4. Add a cron job that checks `results/autonomous_decisions.log` for repeated "ended without ppo_final.pt" entries (>2 in 1 hour = alert).

**Success metric:** Zero cases of Sonnet "forgetting" the continuation plan across sessions. Stale training detected within 45 minutes.

### WS10: ISMCTS Validation and Minimum Search Budget
**Goal:** Find the smallest ISMCTS configuration that exploits DEFCON weaknesses, validate correctness, then use as training opponent.

**Steps:**
1. Run ISMCTS at 16x100, 8x50, 4x25, 2x10, 1x50 against best model. Record win rates and DEFCON exploitation frequency.
2. For the configurations that win via DEFCON plays, manually inspect 5-10 game logs to verify the DEFCON plays are correct (not engine bugs).
3. Find the smallest config that still reliably exploits DEFCON (target: >60% win rate from DEFCON plays alone).
4. Add that ISMCTS config as a league fixture opponent for PPO training.

**Success metric:** Identified minimum ISMCTS budget. Verified DEFCON plays are correct. ISMCTS fixture integrated into PPO league.

### WS11: Opus-Sonnet Coordination Protocol
**Goal:** Formalize when and how Sonnet escalates to Opus.

**Steps:**
1. Define mandatory escalation triggers (add to standing policy):
   - Elo regression >30 points from best
   - 2+ consecutive versions below best
   - Any training crash that requires >1 restart
   - Unexpected benchmark result (>5pp from prediction)
   - Architecture or data change that affects >3 files
2. Define Opus request format: always include (a) what happened, (b) what was tried, (c) current hypothesis, (d) specific question.
3. Sonnet must wait for Opus response before launching the next experiment after an escalation trigger.
4. Opus analyses are stored in `results/analysis/` and referenced in the experiment log.

**Success metric:** Every regression gets an Opus root-cause analysis before the next experiment launches.

## Policy Changes

### Change 1: Add to standing_policy.md §2 — Mandatory Escalation Triggers
Add after "When NOT to run an experiment":
```
### Mandatory Opus escalation triggers
Sonnet MUST /askopus before launching the next experiment when ANY of these occur:
- Elo regression: current version >30 points below best, OR 2+ consecutive versions below best
- Training crash requiring >1 restart attempt
- Benchmark result >5pp worse than predicted
- Architecture or data change affecting >3 files
- Plateau: 3+ consecutive versions with Elo within 20 points of each other
Format for escalation: (a) what happened, (b) what was tried, (c) current hypothesis, (d) specific question for Opus.
Do NOT launch the next experiment until Opus responds.
```

### Change 2: Add to standing_policy.md §5 — Continuation Plan
Add new subsection:
```
### Continuation plan (MANDATORY)
Maintain `results/continuation_plan.json` with format:
{"current_task": "...", "next_tasks": ["...", "..."], "blocked_on": "...", "last_updated": "ISO8601"}
Update after every task completion and before every session end.
Read at session start. If file exists and has tasks, resume from it.
User questions do NOT clear the plan — answer, then resume.
```

### Change 3: Add to standing_policy.md §2 — Hypothesis Requirement
Add to "Pre-launch checklist":
```
7. **Is there a written hypothesis?** Write a 1-sentence hypothesis in the experiment log BEFORE launching. If you cannot articulate why this experiment should improve strength, /askopus first.
```

### Change 4: Add to standing_policy.md §3 — Binary Freshness Check
Add to "Pre-launch checks":
```
### C++ binding freshness (before any training or benchmark)
Run: cmake --build build-ninja -j && python -c "import tscore; print(tscore.__file__)"
If build fails or tscore loads from wrong path, fix before proceeding. NEVER skip this.
```

### Change 5: Add to standing_policy.md §2 — Plateau Aggression
Replace current plateau handling with:
```
### Aggressive plateau response
If 2 consecutive PPO versions fail to beat the current best Elo:
1. STOP launching more versions of the same config
2. /askopus with the Elo trajectory and training curves
3. Only resume after Opus provides a concrete change to try
Never train >2 versions past a plateau without analysis.
```

### Change 6: Add to standing_policy.md §8 — Overlapping Confirmation
Add:
```
### Overlapping confirmation games
After each PPO checkpoint save, immediately launch confirmation tournament in background (CPU-only, nice -n 15).
Do NOT wait for confirmation to finish before starting the next PPO iteration.
Read confirmation results when available (may be 1-2 iterations later).
```

### Change 7: Update standing_policy.md §2 — Checkpoint Identity
Add:
```
### Checkpoint identity (MANDATORY)
Every checkpoint must be logged to results/metadata.sqlite3 with: name, git_sha, wandb_run_id, parent_checkpoint_id, file_sha256, all hyperparams.
W&B run IDs must be unique — never append to an existing run. Use wandb.init(resume="never").
```

## Automation Proposals

### Hook 1: SessionStart — Load Continuation Plan
Add to `.claude/settings.json` under `hooks`:
```json
"SessionStart": [
  {
    "matcher": "",
    "hooks": [
      {
        "type": "command",
        "command": "python3 -c \"import json, pathlib; p=pathlib.Path('results/continuation_plan.json'); print(json.dumps({'systemMessage': 'CONTINUATION PLAN: ' + p.read_text()})) if p.exists() else None\""
      }
    ]
  }
]
```

### Hook 2: Stop — Save Continuation Plan Reminder
Add to `.claude/settings.json` under `hooks`:
```json
"Stop": [
  {
    "matcher": "",
    "hooks": [
      {
        "type": "command",
        "command": "python3 -c \"import json; print(json.dumps({'systemMessage': 'REMINDER: Update results/continuation_plan.json with current state before session ends.'}))\""
      }
    ]
  }
]
```

### Hook 3: PreToolUse/Bash — Binary Freshness Before Training
Add to `.claude/settings.json` under `hooks.PreToolUse`:
```json
{
  "matcher": "Bash",
  "hooks": [
    {
      "type": "command",
      "command": "python3 /home/dkord/code/twilight-struggle-ai/.claude/hooks/check_binary_freshness.py"
    }
  ]
}
```
Where `check_binary_freshness.py` checks if the bash command contains `train_ppo` or `train_baseline`, and if so, verifies that `build-ninja/bindings/tscore*.so` is newer than the newest `.cpp` or `.h` file in `cpp/` or `include/`. If stale, emits a warning system message.

### Hook 4: Cron — Stale Training Detector
Add to crontab (`crontab -e`):
```
*/15 * * * * python3 /home/dkord/code/twilight-struggle-ai/scripts/check_stale_training.py >> /home/dkord/code/twilight-struggle-ai/results/stale_training_alerts.log 2>&1
```
Script checks: if a `ppo_v*_league` directory exists with a `latest_checkpoint.txt` older than 45 minutes AND a training process is still running, log an alert.

### Hook 5: PostToolUse — Run Relevant Tests After Python Edits
Extend `.claude/hooks/run-targeted-checks.py` to also run:
```python
# After py_compile check, also run relevant test file if it exists
test_file = Path("tests/python") / f"test_{p.stem}.py"
if test_file.exists():
    code, out = run([sys.executable, "-m", "pytest", str(test_file), "-x", "-q", "--no-header", "--tb=short"], timeout=60)
    emit(f"Tests {'passed' if code == 0 else 'FAILED'} for {test_file}: {out[:1200]}")
```

## Conclusions

1. **The biggest single improvement is a formal escalation protocol.** Most wasted GPU hours (v23+ epic, v56-v62 plateau) could have been avoided by escalating to Opus after the second failed version instead of the tenth.

2. **The continuation plan is the second-highest priority.** Sonnet loses context across sessions and after user questions. A persistent JSON file solves this mechanically.

3. **Checkpoint identity and metadata DB prevent the "how was this created?" problem permanently.** SQLite is simple, reliable, and committable to git.

4. **Snakemake should be revived, not replaced.** It was tried with success but abandoned — the issue was not Snakemake itself but lack of commitment to using it consistently. Dagster is overkill for a single-machine project.

5. **Overlapping confirmation games with training is a free latency win** that requires only modest pipeline changes (background launch + deferred result reading).

6. **The C++ binary staleness problem is fully automatable** via a PreToolUse hook that checks `.so` timestamps against source file timestamps.

7. **Tech debt reduction (WS6) should be done incrementally** — one extraction per commit, never as a big-bang refactor. The risk of regression from a large refactor outweighs the benefit.

8. **Performance investment has been systematically undervalued.** The user correctly notes that agents overestimate implementation time for speedups. A standing rule should require Sonnet to attempt any speedup with expected >2x improvement before accepting a slow process.

## Recommendations

1. **First: Implement WS1 (meta-algorithm OODA loop) and Policy Changes 1, 2, 5.** These are pure policy — no code changes, just discipline. Add to standing_policy.md and results/continuation_plan.json today.

2. **Second: Implement WS5 (regression prevention) and Hook 3 (binary freshness check).** Write the hook script and update settings.json. This prevents the #1 most common regression (stale C++ binary).

3. **Third: Implement WS3 (checkpoint identity + SQLite DB).** Write the log_checkpoint() and log_benchmark() functions, create the DB schema, integrate into train_ppo.py. This is a one-time investment that pays off permanently.

4. **Fourth: Implement WS7 (overlapping confirmation games).** Modify the PPO loop to launch confirmation in background immediately after checkpoint save. This is a direct latency improvement the user specifically requested.

5. **Fifth: Implement WS2 (revive Snakemake).** Update the Snakefile to cover the current PPO pipeline. Deprecate manual nohup launches.

6. **Sixth: Implement WS6 (tech debt — shared library extraction).** Start with constants.py, then model_factory.py, then features.py. One commit each.

7. **Seventh: Implement WS10 (ISMCTS validation).** Run the search budget sweep, validate DEFCON plays, integrate as league fixture.

8. **Eighth: Implement WS9 (automated hooks and cron).** SessionStart/Stop hooks for continuation plan, stale training detector cron.

## Open Questions

1. **SQLite vs alternatives for metadata DB.** SQLite is simplest and git-committable, but grows unboundedly. Should we cap it (e.g., archive old entries)? Or is the expected size (<100MB over the project lifetime) small enough to not worry?

2. **Snakemake vs custom Python orchestrator.** Snakemake is proven but has its own complexity (DAG resolution, conda envs). The alternative is a simple Python script that manages the pipeline state machine. Which does the user prefer?

3. **Version numbering after branch points.** The feedback suggests resetting numbering (e.g., `sc_v0` for SmallChoiceHead). But this creates fragmentation — should there instead be a single monotonic version number with a "branch" field in metadata?

4. **ISMCTS as training opponent.** If ISMCTS wins via DEFCON exploitation, training against it might just teach the model to avoid DEFCON situations rather than play better overall. Should ISMCTS be a fixture (always present) or a periodic evaluation opponent?

5. **How aggressive should plateau detection be?** Current proposal is 2 versions. But if each version is only 30 minutes of training, 2 versions might be too conservative (normal variance). Should the threshold be Elo-based (e.g., <20 points improvement) rather than count-based?

6. **W&B run uniqueness enforcement.** Currently runs use `wandb.init(resume="allow")` or similar. Changing to `resume="never"` could break restart behavior where we want to append to an existing run after a crash. Need to decide: unique run per launch attempt, or unique run per logical experiment?
