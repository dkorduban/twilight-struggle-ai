# Stale Content Audit & Archival Report

**Date**: 2026-04-11 15:20 UTC
**Author**: Opus 4.6 cleanup agent
**Scope**: docs/, results/, .claude/plan/, memory files

---

## Executive Summary

Archived 126 files (117 JSON + 9 MD) that were causing agent confusion by presenting superseded benchmarks, completed plans, and BC-era analyses as current information. The primary cleanup was moving 89 per-model benchmark JSON files (rebench_v23-v85, bench_v69-v87) into `results/archive/` since they are all superseded by the round-robin Elo ladder in `elo_full_ladder.json`. Nine docs files describing completed BC-era work, solved problems, and executed plans were moved to `docs/archive/`.

Conservative approach: no code files touched, no memory files modified, no files deleted. All moves preserve git history via `git mv`.

---

## Phase 1: What Was Archived

### results/archive/ (117 JSON + 3 MD)

| Category | Count | Reason |
|----------|-------|--------|
| rebench_v23 through rebench_v85 | 63 | Compiled into benchmark_history.json; superseded by Elo ladder |
| bench_v69 through bench_v87_provenance | 26 | BC-era per-model benchmarks; none in current Elo ladder |
| modal_h{128,256,512}_fast | 3 | Early arch comparison (Mar 30); conclusions applied |
| value_calibration_*, platt_v71 | 4 | Pre-PPO calibration experiments |
| benchmark_history_pre_defcon_fix | 1 | Explicitly superseded by corrected benchmark_history.json |
| heuristic_temperature_sweep_* | 6 | Temperature tuning complete; Nash-temp is standard |
| elo_v789, elo_v7_v10, etc. | 5 | Pairwise Elo subsets; all in elo_full_ladder.json |
| elo_ppo_ladder, elo_ratings, elo_backup | 3 | Superseded by elo_full_ladder.json |
| v108_h384_s{42,7}_bench | 2 | Arch sweep bench; results captured in memory |
| ab_test_warmstart_v73.md | 1 | BC-era A/B test |
| next_phase_plan.md | 1 | Apr 7 plan; all items completed |
| bc_dataset_and_arch_plan.md | 1 | 32-dim scalar plan; already executed |

### docs/archive/ (9 MD)

| File | Reason |
|------|--------|
| experiment_plan_next_15h.md | Apr 4 BC-era plan; all experiments done or ruled out |
| saturation_analysis.md | Apr 3 1x vs 2x analysis; conclusions applied, BC era over |
| us_bias_analysis.md | Apr 3 US-side analysis; solved by PPO (14% -> 74%+ US WR) |
| model_architecture_analysis.md | Describes 5 original BC models; superseded by GNN/Attn |
| analysis_defcon_toxicity_regressions.md | Apr 2 DEFCON bug analysis; bug fixed, captured in memory |
| ppo_next_steps.md | Apr 7 PPO v1 era; all items completed |
| plan_2026_04_07.md | Apr 7 plan; superseded by later plans |
| plan_ppo_v4.md | PPO v4 plan; PPO v4 completed |
| plan_next_steps.md | Apr 8 PPO v4/v5 plan; all completed |

---

## Phase 2: What Was Kept (and why)

### results/ (8 JSON remaining)
- `elo_full_ladder.json` — current 34-model Elo ladder (primary evaluation artifact)
- `jsd_matrix.json` — current JSD divergence matrix (Apr 11)
- `benchmark_history.json` — compiled history used by scripts
- `checkpoint_elo.json` — checkpoint-level data used by Elo tracker
- `per_side_wr_matrix.json` — per-side analysis (Apr 9)
- `elo_v64_checkpoint_selection.json`, `elo_v64_confirmation.json` — recent (Apr 11)
- `selected_fixtures.json` — current tournament fixtures

### docs/ (kept)
- `plan_pragmatic_heads.md` — ACTIVE priority per MEMORY.md
- `experiment_log_phase1.md`, `experiment_log_phase2.md` — historical logs, valuable reference for understanding project trajectory
- `replay_grammar.md`, `ts_rules_scoring.md`, `event_scope.md` — stable reference docs
- `spec_exploration_noise.md` — Month 3 exploration spec, partially implemented
- `spec_setup_influence.md` — rules reference, still active
- `specs/`, `notes/` subdirectories — reference material

### results/ MD files (kept)
- All `opus_analysis_*` files — historical record per instructions
- `experiment_log.md` — running experiment log
- `benchmark_model_vs_model_analysis.md` — recent analysis (Apr 7)
- `game_analysis_expert.md`, `human_game_stats.md` — human game analysis
- `mcts_throughput_matrix.md`, `mcts_gpu_vs_cpu.md` — MCTS perf reference
- `mode_distribution_analysis.md`, `model_distribution_analysis.md` — policy analysis
- `n_steps_investigation.md` — PPO debugging reference
- `league_composition_advice.md` — league tuning reference
- `ismcts_vs_model_v45_200g.md` — ISMCTS evaluation
- `ppo_autonomous_mistake_analysis.md` — lessons learned
- `game_log_readable.md` — sample readable game

### .claude/plan/ (kept)
- `restartable-benchmark.md` — implemented feature spec, still useful reference
- `mcts-perf-deepdive.md` — MCTS threading investigation, still relevant
- `policy-stats-and-oom.md` — policy stats spec, partially implemented
- `jsd-probe-eval.md` — JSD probe spec, implemented and active
- `ismcts-vs-model.md` — ISMCTS benchmark spec, recently implemented

---

## Phase 3: Memory File Audit

### Files NOT in MEMORY.md index (orphaned but not harmful)
These memory files exist but are not referenced from MEMORY.md. They still contain valid standing rules:
- `feedback_arch_sweep_sequencing.md` — GPU sequencing rule (still valid)
- `feedback_autonomous_work.md` — autonomous work rules (still valid)
- `feedback_bench_both_sides.md` — benchmark both sides (still valid)
- `feedback_benchmark_2000.md` — 2000 games/side (still valid)
- `feedback_benchmark_display.md` — display format (still valid)
- `feedback_bid_convention.md` — +2 bid convention (still valid)
- `feedback_continuation_prompt.md` — CONTINUATION PROMPT convention (still valid)
- `feedback_data_collection.md` — nice priority rule (still valid)
- `feedback_deterministic_split.md` — deterministic split rule (still valid)
- `feedback_haiku_mechanical.md` — Haiku delegation rule (still valid)
- `feedback_oom_wsl.md` — OOM/pytest rules (still valid)
- `project_defcon_data_quality_analysis.md` — DEFCON analysis (historical, valid)

### Flagged: describe completed/stale state

1. **project_month1_state.md** — Describes Month 1 state as of Mar 26. Says "142/142 tests passing" and lists Month 1 infrastructure. We are now in Month 3. This file describes work as if it is the frontier state. **Misleading but not harmful** — the age header ("12 days old") helps, and the information is factually correct as historical record.

2. **project_pipeline_state.md** — Says "v22 era pipeline config (mostly historical now)" in MEMORY.md index. File describes v99 clean sweep (Apr 3), gen1 self-play, and pipeline config from the BC era. The "Currently running" section references PIDs and processes that no longer exist. **Stale but MEMORY.md already flags it as historical**.

3. **project_ppo_v1_results.md** — Describes PPO v1-v2b-v3 results as if v3 is "queued". We are far past v3 (current models go up to v61). The v3 launch command references `/tmp/launch_v3_league.sh`. **Stale but contains valuable historical data**.

4. **project_phase4_state.md** — Describes phase 4 arch sweep as actively running. MEMORY.md flags it as "historical; Attn 16x slower per epoch". **Appropriately flagged in MEMORY.md**.

5. **project_scoring_vp_regressions.md** — Marked RESOLVED. **No action needed**.

### Recommendation for memory files
No files should be deleted (per project preference for mv/rename). The MEMORY.md index already flags `project_pipeline_state.md` as historical. The main concern is `project_month1_state.md` and `project_ppo_v1_results.md` which describe old state without being flagged in the index. Suggest adding "(historical)" to their MEMORY.md descriptions.

---

## Phase 4: CLAUDE.md Deprecation Check

### Observations
1. **Month 1 focus language persists**: CLAUDE.md has extensive Month 1 guidance ("Definition of done for Month 1", "Out of scope for now" listing Month 1 items, "First tasks if the repo is still empty"). We are in Month 3. This creates confusion: agents may follow Month 1 constraints (e.g., "do not build full teacher/root search") when those are now appropriate Month 3 work.

2. **Specific stale references in CLAUDE.md**:
   - "Definition of done for Month 1" section — all items completed
   - "First tasks if the repo is still empty" — repo is not empty, all tasks done
   - "Out of scope for now" list includes items that are now in scope (e.g., "full teacher / root search" is done; "distributed actor fleet" still out of scope)
   - "Optimization order" lists steps 1-4 as priorities but all are complete
   - Section "Current focus" lists "Dirichlet noise at MCTS root" as #1 priority — this is already implemented

3. **No broken file references found**: All docs paths referenced in CLAUDE.md still exist (replay_grammar.md, etc.).

### Proposed CLAUDE.md changes (for human review, NOT applied)

Suggest consolidating the Month 1/2 sections into a brief "Completed milestones" summary, and updating "Current focus" to reflect actual Month 3 state. Specifically:
- Mark "Definition of done for Month 1" as COMPLETED
- Mark "First tasks if the repo is still empty" as COMPLETED
- Update "Out of scope for now" to distinguish completed items from still-deferred items
- Update "Current focus" deliverables 1-3 (Dirichlet, exploration noise, Elo) as DONE
- Update the "Optimization order" to reflect that steps 1-6 are complete

---

## Conclusions

1. **126 files archived** — primarily superseded benchmark JSONs and completed plan documents
2. **8 current JSON files remain** in results/ — all actively used by tournament/evaluation scripts
3. **No code files or active config touched**
4. **Memory files are mostly valid** — 3 files describe old state without clear "historical" flagging in MEMORY.md index
5. **CLAUDE.md has significant stale Month 1/2 language** that could mislead agents into following outdated constraints; recommend human review and update
6. **Archive manifest** written to `docs/archive/ARCHIVE_MANIFEST.md`
