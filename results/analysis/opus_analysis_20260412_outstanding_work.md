# Opus Analysis: Outstanding Work & Priorities
Date: 2026-04-12T08:30:00Z
Question: What is the current outstanding work and priorities? WSx completeness? continuation_plan status?

## Executive Summary

The project has made substantial infrastructure progress since the WS1-WS11 workstreams were defined on 2026-04-11. Of the 11 workstreams, 4 are DONE (WS1, WS2, WS3, WS11), 3 are PARTIAL (WS5, WS7, WS9), and 4 are NOT STARTED (WS4, WS6, WS8, WS10). The continuation_plan.json is current (last updated 2026-04-11T17:15Z) and focuses on Phase 2 of the Pragmatic Heads plan (DP decoder integration), with v66_sc confirmed at 1982 Elo. The main training lineage is healthy and automated (ppo_loop_step.sh handles auto-chaining), but the biggest remaining gaps are experiment tracking discipline (WS4 -- experiments.jsonl is empty), tech debt extraction (WS6 -- constants.py not created), and ISMCTS validation (WS10 -- the largest remaining strength lever).

## Findings

### WS1-WS11 Status Table

| WS | Title | Status | What's Done | What Remains |
|----|-------|--------|-------------|--------------|
| WS1 | Meta-Algorithm OODA Loop | **DONE** | Per-iteration health check in standing_policy SS2+SS7, session-start OODA checklist | Nothing |
| WS2 | Revive Snakemake Pipeline | **DONE** | `Snakefile.ppo` fully implemented: ppo_train, ppo_export, ppo_bench_side, ppo_bench_merge, ppo_confirm rules. `experiments_ppo.yaml` config. Commit d8b7dc7 | Nothing critical. Could add more experiments to YAML. |
| WS3 | Checkpoint Identity + SQLite DB | **DONE** | `checkpoint_db.py` has 7 tables: checkpoints (123 rows), tournaments (1), match_results (1545), elo_ladder (35), rollout_stats (40). `log_checkpoint()`, `log_rollout_wr()`, `log_rollout_opponent_stats()`, `log_tournament()` all wired into train_ppo.py and run_elo_tournament.py. Historical matches migrated (commit 672e089). `rollout_opponent_stats` table defined in code but not yet created in DB (schema migration needed on next _get_db() call). | Minor: `benchmarks` table (0 rows) and `elo_ratings` table (0 rows) are unused -- benchmark results go through match_results/elo_ladder instead. Consider removing dead tables or wiring them. |
| WS4 | Experiment Tracking Discipline | **NOT STARTED** | `experiment_log.py` module exists with `log_experiment_start`/`log_experiment_end`. train_ppo.py imports and calls them. | **experiments.jsonl does not exist** (0 bytes/missing). The module likely has a bug preventing writes, or hypothesis strings are never passed. This is the #1 gap in experiment governance -- every run should have a logged hypothesis per policy SS2. |
| WS5 | Regression Prevention / Binary Freshness Hook | **PARTIAL** | `.claude/hooks/check_binary_freshness.py` exists. | Need to verify it's registered in `.claude/settings.json` and actually fires before train_ppo/benchmark commands. The original workstream also called for a binary-age check in CI -- not done. |
| WS6 | Tech Debt -- Shared Library Extraction | **NOT STARTED** | Neither `constants.py` nor `model_factory.py` exist. | Extract shared constants (ACTION_DIM, NUM_COUNTRIES, etc.) to `python/tsrl/constants.py`. Extract model creation logic to `model_factory.py`. Extract feature utilities to `features.py`. Low urgency but growing tech debt. |
| WS7 | Overlapping Confirmation Games | **DONE** | train_ppo.py launches `post_train_confirm.sh --incremental` non-blocking at milestone iterations (commit 936137f). post_train_confirm.sh supports incremental (default) and full modes, 5-opponent pool from selected_fixtures.json, dry-run, scope guard. Snakefile.ppo has ppo_confirm rule. | Nothing critical. The milestone confirmation is wired and working (confirmed by smoke test logs in autonomous_decisions.log at 04:51-04:59 UTC). |
| WS8 | CPU Saturation Audit | **NOT STARTED** | Resource profiles documented in standing_policy SS3. | No actual audit of CPU utilization during training/benchmark overlap. No profiling data collected. Low priority -- pipeline works well enough. |
| WS9 | Automated Watchdogs + Hooks | **PARTIAL** | `check_stale_training.py` exists (commit d8ed59f). Cron installed: runs every 15 minutes. health_check.sh runs every 30 minutes via cron. | Log output goes to results/logs/stale_training_alerts.log -- should verify it's actually catching stale runs. SessionStart/Stop hooks for continuation_plan are mentioned in policy but not verified as Claude Code hooks. |
| WS10 | ISMCTS Validation + Min Search Budget | **NOT STARTED** | ISMCTS code exists but no systematic validation sweep. Prior analysis (opus_analysis_20260411_041000) showed "no benefit at 100sim". | Need search budget sweep (100/200/400/800 sims), verify DEFCON-aware plays, measure Elo gain from ISMCTS during evaluation. This is the largest remaining strength lever per CLAUDE.md (30% of Month-3 time). |
| WS11 | Sonnet-Opus Escalation Protocol | **DONE** | Formal SS12 in standing_policy: escalation triggers, mandatory format (a-e), waiting protocol, output storage convention. | Nothing |

### continuation_plan.json status

Last updated: 2026-04-11T17:15:00Z (approximately 15 hours old).

**current_task**: "v66_sc PPO training running (PID 402749). Phase 2 DP decoder dispatched to Codex agent."

**next_tasks** (in order):
1. When v66_sc completes: benchmark vs v65_sc; if Elo improves, Phase 2 is confirmed working
2. When Codex finishes dp_decoder.py: review tests, wire into model inference (Phase 2b)
3. Phase 2b: replace proportional allocation in mcts_batched.cpp with DP decoder call
4. After v66 benchmark: run compute_elo.py to update Elo ladder with v66_sc
5. WS6: extract shared constants to python/tsrl/constants.py

**blocked_on**: null

**active_background**: v66_sc PPO training (PID 402749), Codex agent for dp_decoder.py

**Status assessment**: The plan is partially stale. v66_sc training has COMPLETED and been benchmarked (Elo 1982, placed on ladder per autonomous_decisions.log at 04:00 UTC). Task #1 and #4 are done. The plan needs updating to reflect that v66_sc is confirmed and the focus should shift to Phase 2b (DP decoder integration) or next training run.

### Recent work (from git log + autonomous_decisions.log)

**Last 24 hours of commits (newest first):**
- `841a076` Per-opponent rollout stats in SQL + move analysis files to results/analysis/
- `672e089` Migrate 1545 cached match JSONs + 35-model Elo ladder into metadata.sqlite3
- `6a752c6` SQL matchup provenance: tournaments + match_results + elo_ladder + aggregate view
- `01fadd2` Restore full 35-model Elo ladder; fix post_train_confirm.sh to merge not overwrite
- `061faf2` Per-side league fixtures: --ussr-league-fixtures and --us-league-fixtures args
- `90e467b` ppo_loop_step.sh: load per-side fixture sets from selected_fixtures.json
- `d5b4410` Apply JSD fixture deduplication
- `936137f` WS3/WS7: rollout_stats table + log_rollout_wr() + milestone Elo confirmation
- `d8ed59f` WS9: stale training watchdog + cron installer
- `d8b7dc7` WS2: add ppo_confirm rule for post-training Elo placement

**Autonomous work log (last entries):**
- Smoke test of WS3+WS7 (rollout_stats DB + milestone Elo confirmation) completed at ~05:00 UTC
- Fixture-pool-only Elo tournament launched at 06:43 UTC for sanity check
- v66_sc placed on Elo ladder: combined 1982 (USSR 2079 / US 1881)

### Gaps and risks

1. **WS4 experiments.jsonl missing**: The experiment tracking module is wired but produces no output. Every PPO run since the module was added should have a logged hypothesis, but the file does not exist. This means experiment governance (SS2) is not actually enforced.

2. **continuation_plan.json is stale by ~15 hours**: v66_sc completed and was benchmarked hours ago, but the plan still lists it as "running". The next session will read stale context.

3. **rollout_opponent_stats table not created in DB**: The schema is in checkpoint_db.py but the actual SQLite DB doesn't have the table yet. It will be auto-created on next `_get_db()` call from train_ppo.py, but existing data (from v66_sc run) was likely lost due to the missing table causing a silent exception.

4. **WS10 (ISMCTS) untouched**: This is flagged as the biggest strength lever (30% of Month-3 time per CLAUDE.md) but has zero progress. Prior analysis concluded "no benefit at 100sim" which may indicate either too-low budget or implementation issues.

5. **Phase 2 DP decoder status unknown**: The Codex agent was dispatched but there's no evidence it completed. The dp_decoder.py commit (`59d0386`) exists, so it may be done but needs review and integration.

6. **Dead tables in metadata.sqlite3**: `benchmarks` (0 rows) and `elo_ratings` (0 rows) are defined but unused. All Elo data flows through `match_results` + `elo_ladder` tables instead.

## Conclusions

1. **Infrastructure workstreams are largely complete.** WS1, WS2, WS3, WS7, WS11 are done. WS5 and WS9 are partial but functional. The PPO pipeline is fully automated with auto-chaining (ppo_loop_step.sh), milestone Elo confirmation, SQL provenance, and stale training detection.

2. **Experiment tracking (WS4) is the most critical gap.** The experiments.jsonl file does not exist despite the module being wired. This undermines experiment governance (SS2 of standing policy) and means there is no hypothesis log for any run.

3. **The continuation_plan needs immediate update.** v66_sc is complete and confirmed at Elo 1982. The plan should advance to Phase 2b (DP decoder wire-in) or next PPO generation.

4. **ISMCTS (WS10) is the biggest untouched strength lever.** CLAUDE.md allocates 30% of Month-3 time to ISMCTS + exploration noise, but there has been zero systematic work on ISMCTS validation or search budget tuning.

5. **Tech debt (WS6) is growing but not blocking.** No shared constants.py, no model_factory.py. This creates duplication risk but is not urgent.

6. **Phase 2 (Pragmatic Heads) is the current active development thread.** The bounded-knapsack DP decoder and straight-through proxy are committed. Next step is wiring the DP decoder into C++ inference (Phase 2b), which is a cross-boundary change (Python + C++).

7. **The training lineage is healthy.** v66_sc at 1982 Elo (2079 USSR / 1881 US) represents continued progress. The SmallChoiceHead bug (sc_loss was 0) was found and fixed this session.

## Recommendations

1. **Fix WS4 immediately**: Debug why `experiments.jsonl` is not being written. Check `python/tsrl/experiment_log.py` for the `log_experiment_start` bug mentioned in the workstreams memory. Likely a path issue or silent exception. This is 15 minutes of work with high governance value.

2. **Update continuation_plan.json**: Advance to Phase 2b tasks. Mark v66_sc as complete. Set next_tasks to: (a) review dp_decoder.py + tests, (b) wire DP decoder into mcts_batched.cpp, (c) train v67 with DP decoder, (d) WS6 constants extraction.

3. **Wire rollout_opponent_stats into DB**: Run a single training iteration or call `_get_db()` to trigger schema migration. Verify the table is created. This ensures per-opponent granular stats are captured for future runs.

4. **Start WS10 (ISMCTS validation)**: Design a search budget sweep (100/200/400/800 sims) against the current best model. This is the highest-impact strength work remaining. Delegate to Codex for the sweep script.

5. **Complete WS5 (binary freshness hook)**: Verify the hook is in `.claude/settings.json` and fires correctly. Run a test to confirm it blocks on stale binaries.

6. **Phase 2b DP decoder integration**: Review the committed dp_decoder.py, run its tests, then wire into C++ inference. This is the next step in the Pragmatic Heads plan.

7. **WS6 constants extraction**: Low effort, prevents future duplication bugs. Extract ACTION_DIM, NUM_COUNTRIES, HAND_SIZE constants to `python/tsrl/constants.py`.

## Open Questions

1. Did the Codex agent for dp_decoder.py complete successfully? Commits 59d0386 and dbdc798 suggest it did, but the continuation_plan still lists it as active_background.

2. Is the binary freshness hook (WS5) actually registered in Claude Code settings and firing? Need to check `.claude/settings.json`.

3. Why does experiments.jsonl not exist? Is it a bug in log_experiment_start, or is the --experiment flag never passed to train_ppo.py?

4. What is the next training version? v67? Is the auto-chaining watcher from ppo_loop_step.sh still running, or did v66_sc's completion not trigger it (since v66_sc was launched manually, not via ppo_loop_step.sh)?

5. Should the dead tables (benchmarks, elo_ratings) in metadata.sqlite3 be removed or repurposed?
