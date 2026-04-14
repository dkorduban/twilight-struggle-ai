# PPO Restart: v205_sc_league from v132_sc (2092 Elo)

**Date:** 2026-04-14  
**Author:** autonomous agent

## Motivation

The sc-lineage (v200–v203_sc, ~1732–1754 Elo) had stagnated due to fixture saturation —
training only against weak sc-lineage models (v138/v140/v142_sc at 1944–1979 Elo) caused
policy specialization and loss of generalization.

The best checkpoint in the full lineage was `ppo_v132_sc_league` at 2092 Elo.
Restarting from this checkpoint with the already-correct fixture pool (v55/v54/v44/v45
at 2096–2118 Elo) should break the plateau.

## Root causes diagnosed and fixed

### 1. NUM_MODES 5→6 mismatch (commit 37bdd01, 2026-04-13)

Commit `37bdd01` added `OpsFirst = 5` to `ActionMode`, bumping `NUM_MODES` from 5 to 6.
Old scripted fixture checkpoints (v55, v54, v44, etc.) have `mode_head` of size 5.
When the new 6-mode model plays vs an old fixture, `legal_modes()` can return `OpsFirst`
(index=5) for opponent cards, crashing C++ with `index 5 is out of bounds for dim 0 size 5`.

**Fix:** Added bounds guard `if (index >= n_mode_logits) continue` in three C++ paths:
- `cpp/tscore/decode_helpers.hpp` — single-inference path (TorchScriptPolicy, learned_policy.cpp)
- `cpp/tscore/mcts_batched.cpp` — batched rollout path (rollout_model_vs_model_batched)
- `cpp/tscore/ismcts.cpp` — ISMCTS batched eval path

Also fixed `mode_mask` size in `mcts_batched.cpp` rollout step: was hardcoded `{5}`,
now sized dynamically from `mode_logits.size(0)` so the Python PPO update
`mode_logits.masked_fill(~mode_masks)` sees compatible shapes for both 5- and 6-mode models.

### 2. Smoke test always fails for 5-mode → 6-mode restarts

The pre-training smoke test loads the `_scripted.pt` sibling of the checkpoint.
`ppo_best_scripted.pt` from v132 was compiled with the old 5-mode model.
`--skip-smoke-test` is now always written to the snakemake YAML config by `ppo_loop_step.sh`,
and supported via a new `skip_smoke_test` field in `Snakefile.ppo`'s `_DYNAMIC_TRAIN_DEFAULTS`.

### 3. Stale WR table from sc-lineage decline

v204 would have inherited v203's WR table with only stale sc-lineage entries
(v138/v140/v142_sc) — no signal for the strong panel models.  
Pre-seeded v205's WR table from v132's WR table (0.5× decay) which has real
win-rate estimates against v55, v45, v48, v19, v20, v21, v22.

### 4. ppo_loop_step.sh: WR table skip-if-exists

Added guard: if `${NEXT_DIR}/wr_table.json` already exists (pre-seeded), skip the
copy from `${FINISHED_DIR}` so manual pre-seeding isn't overwritten.

## Launch summary

| Item | Value |
|------|-------|
| New lineage | `ppo_v205_sc_league` |
| Starting checkpoint | `data/checkpoints/ppo_v132_sc_league/ppo_best.pt` (2092 Elo) |
| Fixture pool | v55(2118), v54(2102), v44(2101), v45(2096), v48(2095), v22, v57, v20, v21, v19 + heuristic |
| Panel eval | v55, v54, v44, v45, v48 |
| WR table seed | from v132 (0.5× decay) |
| Hyperparams | same as current loop: 30 iters, lr=5e-5, clip=0.12, ent=0.01→0.003, UPGO, k=6, pfsp=1.5 |
| skip_smoke_test | true (5-mode checkpoint, scripted sibling would crash) |

## Files changed

- `cpp/tscore/decode_helpers.hpp` — bounds guard in `build_masked_mode`
- `cpp/tscore/mcts_batched.cpp` — bounds guard in rollout mode loop; dynamic `mode_mask` size
- `cpp/tscore/ismcts.cpp` — bounds guard in batched ISMCTS mode selection
- `Snakefile.ppo` — add `skip_smoke_test` field to `_DYNAMIC_TRAIN_DEFAULTS` and `_dynamic_ppo_train_args`
- `scripts/ppo_loop_step.sh` — always write `skip_smoke_test: true` in YAML; skip WR table copy if target exists

## Status

Training launched and confirmed running as of 2026-04-14T06:46:xx.  
Iteration 1 completed: `rollout_wr=0.710` (ussr=0.680, us=0.740).  
Auto-watcher will chain v206_sc on completion.
