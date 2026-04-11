# Archive Manifest

Archived: 2026-04-11
Reason: Reduce agent confusion from stale results/plans that are superseded by current Elo ladder and PPO training infrastructure.

---

## results/archive/ (117 JSON + 3 MD files moved)

### rebench_v23.json through rebench_v85.json (63 files)
- **Why**: Per-model heuristic benchmarks from BC era (v23-v85). All compiled into `results/benchmark_history.json` by `scripts/compile_rebenchmark.py`. Superseded by Elo ladder for model comparison.

### bench_v69.json through bench_v87_provenance.json (26 files)
- **Why**: Per-model benchmarks from BC era. None of these model versions appear in the current Elo ladder (which starts at v8). Superseded by `results/elo_full_ladder.json`.

### modal_h128_fast.json, modal_h256_fast.json, modal_h512_fast.json
- **Why**: Early hidden-size architecture comparison from Mar 30. Conclusions applied; superseded by GNN/Attn architecture work.

### platt_v71.json, value_calibration_v65.json, value_calibration_params_auto.json, value_calibration_check_auto.json
- **Why**: Platt scaling/calibration experiments from Apr 1. Pre-PPO era; value head has been retrained many times since.

### benchmark_history_pre_defcon_fix.json
- **Why**: Explicitly superseded by `benchmark_history.json` (post-DEFCON-fix corrected history).

### heuristic_temperature_sweep*.json, heuristic_temperature_matrix_bid2.json (6 files)
- **Why**: Heuristic temperature parameter search from Apr 2. Results already applied (Nash-temp is the standard heuristic config).

### elo_v789.json, elo_v7_v10.json, elo_v9_v11.json, elo_v10_v12.json, elo_v11_v13.json
- **Why**: Early pairwise Elo matchups. All pairs are now covered by `elo_full_ladder.json` round-robin.

### elo_ppo_ladder.json, elo_ratings.json, elo_full_ladder_backup_pre_cleanup.json
- **Why**: Superseded by current `elo_full_ladder.json` (Apr 11, 34 models, round-robin).

### v108_h384_s42_bench.json, v108_h384_s7_bench.json
- **Why**: Architecture sweep benchmarks from Apr 5. Results captured in memory files; models not in current ladder.

### ab_test_warmstart_v73.md
- **Why**: BC warm-start A/B test from Apr 1. BC era; superseded by PPO training.

### next_phase_plan.md
- **Why**: Apr 7 "next phase" plan. All items either completed or superseded by later plans.

### bc_dataset_and_arch_plan.md
- **Why**: BC dataset re-encoding plan for 32-dim scalars. Already executed; 32-dim is standard now.

---

## docs/archive/ (9 files moved)

### experiment_plan_next_15h.md
- **Why**: Apr 4 BC-era experiment plan. All experiments completed or ruled out. Superseded by PPO training.

### saturation_analysis.md
- **Why**: Apr 3 analysis of 1x@95ep vs 2x@47ep. Conclusions applied; BC era is over.

### us_bias_analysis.md
- **Why**: Apr 3 US-side bias analysis. The US-side problem was solved by PPO (US WR went from 14% to 74%+).

### model_architecture_analysis.md
- **Why**: Describes original 5 BC model architectures. Superseded by GNN/Attn work and PPO models.

### analysis_defcon_toxicity_regressions.md
- **Why**: Apr 2 DEFCON-1 bug analysis. Bug fixed; conclusions captured in memory/project_defcon_rate.md.

### ppo_next_steps.md
- **Why**: Apr 7 PPO v1 era "next steps". All items completed (self-play, league, Elo). Superseded by later plans.

### plan_2026_04_07.md
- **Why**: Apr 7 forward plan. Superseded by plan_next_steps.md which was itself superseded.

### plan_ppo_v4.md
- **Why**: PPO v4 implementation plan. PPO v4 completed; we are far past v4 now.

### plan_next_steps.md
- **Why**: Apr 8 overnight plan for PPO v4/v5 + architecture sweep. All completed. Superseded by pragmatic_heads plan.

---

## Not archived (kept in place)

### Current results/
- `elo_full_ladder.json` — current 34-model round-robin Elo ladder
- `jsd_matrix.json` — current JSD divergence matrix
- `benchmark_history.json` — compiled benchmark history (used by scripts)
- `checkpoint_elo.json` — checkpoint-level Elo data
- `per_side_wr_matrix.json` — per-side win rate matrix
- `elo_v64_checkpoint_selection.json`, `elo_v64_confirmation.json` — recent (Apr 11)
- `selected_fixtures.json` — current tournament fixtures

### Current docs/
- `plan_pragmatic_heads.md` — active priority
- `experiment_log_phase1.md`, `experiment_log_phase2.md` — historical logs (useful reference)
- `replay_grammar.md`, `ts_rules_scoring.md`, `event_scope.md` — reference docs
- `spec_exploration_noise.md`, `spec_setup_influence.md` — active/future specs
- `specs/`, `notes/` — reference material
