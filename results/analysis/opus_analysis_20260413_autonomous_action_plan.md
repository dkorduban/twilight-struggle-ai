---
# Opus Analysis: Autonomous Action Plan
Date: 2026-04-13
Question: Translate user instructions into concrete autonomous action plan

## Executive Summary

The user wants fully autonomous work on four fronts: (1) engine correctness / DEFCON-1 prevention, (2) WS6 code deduplication and supporting workstreams, (3) new model architecture via BC-then-PPO, and (4) pipeline robustness. The DEFCON engine fix is already merged (commit f6800e3+55e792a) but the C++ binary has not been rebuilt, so **Step 0 is cmake rebuild**. After that, measure DEFCON-1 rate to confirm <5% and suicide rate <2%. Then proceed to WS6 (kDefconLoweringCards consolidation into a single header), BC training on v55 self-play data, short-iteration PPO, and infrastructure hardening. The critical path is: rebuild -> measure DEFCON -> WS6 dedup -> BC data collection -> BC training -> PPO iterations. Infrastructure tasks (WS5/WS3) can run in parallel with BC data collection.

## Findings

### Current State
- **Best model**: v55 at Elo 2118.5 (full ladder anchor v14=2015.0)
- **Best checkpoint path**: `data/checkpoints/scripted_for_elo/v55_scripted.pt`
- **DEFCON fix**: Merged in commits f6800e3 and 55e792a. Three changes: random coup guard, HLSTW defcon floor, additional safety. **Binary NOT rebuilt yet.**
- **Build system**: `build-ninja/` exists (CMakeCache.txt present). No `build/` directory.
- **kDefconLoweringCards duplication**: Found in **7 files** with **inconsistent contents**:
  - `mcts.cpp`: 15 cards `{4,11,13,20,24,39,48,49,50,52,53,68,83,92,105}`
  - `ismcts.cpp`: 15 cards (same as mcts.cpp)
  - `mcts_batched.cpp`: 15 cards (same)
  - `mcts_search_impl.hpp`: 15 cards (same)
  - `learned_policy.cpp`: 15 cards (same, with comments)
  - `policies.cpp`: **9 cards** `{4,11,13,24,52,53,68,92,105}` + separate `kDefconProbLoweringCards` (20) + `kDefconRandomCoupCards` (39,52,68,83) — **DIFFERENT DECOMPOSITION**
  - `fast_mcts_batched.cpp`: **13 cards** `{4,11,13,20,24,39,48,49,50,53,83,92,105}` — **MISSING card 52 and 68 from the 15-card set**
- **BC training**: `scripts/train_baseline.py` exists and handles offline imitation learning with advantage weighting
- **Self-play collection**: `scripts/collect_selfplay_cpp.py` exists — can collect Parquet data from v55 vs itself
- **PPO training**: `scripts/train_ppo.py` exists with full league self-play pipeline
- **WS5 binary freshness hook**: `.claude/hooks/check_binary_freshness.py` already exists and is wired in `.claude/settings.json`
- **Phase 1 (SmallChoiceHead)**: COMPLETE as of 2026-04-11
- **Phase 2 (DP Allocation)**: Not started. Next architecture target.

### Critical Bug Found
The `fast_mcts_batched.cpp` has only 13 cards in its kDefconLoweringCards — it is **missing cards 52 (CIA Created) and 68 (Grain Sales to Soviets)**. The `policies.cpp` uses a 3-way decomposition (certain, probabilistic, random-coup) totaling a different set. This inconsistency is exactly the kind of duplication hazard WS6 aims to fix and could be contributing to residual DEFCON-1 deaths.

## Concrete Action Plan

### Step 0: C++ Engine Rebuild [P1, IMMEDIATE]
**Goal**: Rebuild C++ bindings so Python uses the merged DEFCON fixes.
**Dependencies**: None (fix already on main).
**Commands**:
```bash
cd /home/dkord/code/twilight-struggle-ai
cmake --build build-ninja -j
```
**Verification**:
```bash
ctest --test-dir build-ninja --output-on-failure
```
Then quick Python smoke test:
```bash
uv run python -c "
import sys; sys.path.insert(0, 'build-ninja/bindings')
import tscore; print('tscore loaded, version attrs:', dir(tscore))
"
```
**Success criterion**: Build succeeds, all C++ tests pass, tscore imports in Python.
**Duration**: 2-5 minutes.

### Step 1: Measure DEFCON-1 Rate Post-Fix [P1]
**Goal**: Confirm DEFCON-1 rate <5% and DEFCON-1 suicide rate <2% with the rebuilt binary.
**Dependencies**: Step 0 complete.
**Commands**:
```bash
cd /home/dkord/code/twilight-struggle-ai
uv run python scripts/investigate_ismcts_defcon.py \
    --checkpoint data/checkpoints/scripted_for_elo/v55_scripted.pt \
    --n-games 500 --seed 42
```
If that script doesn't support those flags directly, use a quick inline measurement:
```bash
uv run python -c "
import sys, json
sys.path.insert(0, 'build-ninja/bindings')
sys.path.insert(0, 'python')
import tscore
results = tscore.benchmark_self_play(
    'data/checkpoints/scripted_for_elo/v55_scripted.pt',
    500, 42
)
defcon1 = sum(1 for r in results if r.end_reason == 'defcon1')
suicide = sum(1 for r in results if r.end_reason == 'defcon1' and r.end_turn <= 2)
print(f'DEFCON-1 rate: {defcon1}/{len(results)} = {100*defcon1/len(results):.1f}%')
print(f'DEFCON-1 suicide rate (turn<=2): {suicide}/{len(results)} = {100*suicide/len(results):.1f}%')
print(json.dumps({'defcon1_rate': defcon1/len(results), 'suicide_rate': suicide/len(results), 'n': len(results)}))
" 2>&1 | tee results/logs/defcon1_post_fix_measurement.log
```
**Note**: The exact API may differ. Adapt based on what `tscore` exposes. The key is 500 self-play games with v55, measuring `defcon1` end-reason rate. If the C++ benchmark API doesn't expose end_reason, use `scripts/benchmark.py`:
```bash
uv run python scripts/benchmark.py \
    --model data/checkpoints/scripted_for_elo/v55_scripted.pt \
    --opponent heuristic \
    --n-games 500 --seed 50000 \
    2>&1 | tee results/logs/defcon1_post_fix_benchmark.log
```
Then grep the output for defcon1 counts.
**Success criterion**: DEFCON-1 rate <5%, suicide rate <2%. Log result to `results/autonomous_decisions.log`.
**Duration**: 5-15 minutes (500 games).

### Step 2: WS6 — kDefconLoweringCards Consolidation [P1, FIRST CODE TASK]
**Goal**: Create a single canonical header `cpp/tscore/card_properties.hpp` with the DEFCON card sets, replace all 7 duplicate definitions.
**Dependencies**: Step 0 complete (need working build to verify).

**Implementation plan**:

Create `cpp/tscore/card_properties.hpp`:
```cpp
#pragma once
#include <algorithm>
#include <array>
#include "game_data.hpp"  // for CardId

namespace ts {

// Cards whose event CERTAINLY lowers DEFCON by 1 or more.
// Canonical source — all other files must #include this header.
inline constexpr std::array<int, 9> kDefconCertainLoweringCards = {
    4,   // Duck and Cover
    11,  // Korean War
    13,  // Arab-Israeli War
    24,  // Indo-Pakistani War
    52,  // CIA Created
    53,  // Lone Gunman (Promo, not in play but in list for safety)
    68,  // Grain Sales to Soviets
    92,  // Shuttle Diplomacy... wait — need to verify each card
    105, // Aldrich Ames Remix... need to verify
};

// Cards whose event PROBABILISTICALLY lowers DEFCON (e.g., war cards
// that roll dice — may or may not trigger a coup).
inline constexpr std::array<int, 1> kDefconProbLoweringCards = {
    20,  // Olympic Games (boycott triggers DEFCON-lowering coup)
};

// Cards whose event triggers a random coup (not certain DEFCON drop
// but dangerous at DEFCON 2 if coup target is battleground).
inline constexpr std::array<int, 4> kDefconRandomCoupCards = {
    39,  // Brush War
    52,  // CIA Created (also in certain list — coup is part of effect)
    68,  // Grain Sales (also certain — ops after reveal can coup)
    83,  // Iran-Contra Scandal... need to verify
};

// UNION of all three sets — the broadest "dangerous at DEFCON 2" list.
// This is what most MCTS/ISMCTS/batched search files currently use.
inline constexpr std::array<int, 15> kDefconLoweringCards = {
    4, 11, 13, 20, 24, 39, 48, 49, 50, 52, 53, 68, 83, 92, 105,
};

[[nodiscard]] inline bool is_defcon_lowering_card(int card_id) {
    return std::find(kDefconLoweringCards.begin(), kDefconLoweringCards.end(), card_id) !=
        kDefconLoweringCards.end();
}

[[nodiscard]] inline bool is_defcon_lowering_card(CardId card_id) {
    return is_defcon_lowering_card(static_cast<int>(card_id));
}

}  // namespace ts
```

**CRITICAL**: Before writing the header, verify the exact card IDs by cross-referencing `data/spec/cards.csv` and the rules. The card comments in `learned_policy.cpp` (lines 165-190) have the best annotations. The 3-way decomposition in `policies.cpp` may be more correct than the flat 15-card union.

**Files to modify** (replace local definition with `#include "card_properties.hpp"`):
1. `cpp/tscore/mcts.cpp` — remove lines 61-83, add include, use `ts::is_defcon_lowering_card`
2. `cpp/tscore/ismcts.cpp` — remove lines 45-47 and 172-176, add include
3. `cpp/tscore/mcts_batched.cpp` — remove lines 41-43 and 303-307, add include
4. `cpp/tscore/mcts_search_impl.hpp` — remove lines 26-53, add include (keep `is_card_blocked_by_defcon` but call `ts::is_defcon_lowering_card`)
5. `cpp/tscore/learned_policy.cpp` — remove lines 165-190 definition, add include
6. `cpp/tscore/policies.cpp` — keep the 3-way decomposition but reference canonical sets from header; or unify
7. `cpp/mcts_batched_fast/fast_mcts_batched.cpp` — **FIX THE BUG** (only 13 cards), replace with include

**Verification**:
```bash
cmake --build build-ninja -j && ctest --test-dir build-ninja --output-on-failure
```
**Success criterion**: Build passes, all tests pass, `grep -r 'kDefconLoweringCards' cpp/` shows only `card_properties.hpp` as the definition site.
**Duration**: 30-60 minutes.

### Step 3: WS6 — search_common dedup audit [P2]
**Goal**: Identify remaining duplication between MCTS variants beyond kDefconLoweringCards.
**Dependencies**: Step 2 complete.

The `mcts_search_impl.hpp` already extracts shared code (ModeDraft, CardDraft, expand_from_outputs, select_to_leaf, backpropagate, etc.). Check whether `mcts.cpp`, `ismcts.cpp`, `mcts_batched.cpp`, and `fast_mcts_batched.cpp` have remaining copy-pasted logic that should use search_impl.

**Commands**:
```bash
# Count lines in each search file to gauge duplication scope
wc -l cpp/tscore/mcts.cpp cpp/tscore/ismcts.cpp cpp/tscore/mcts_batched.cpp cpp/tscore/mcts_search_impl.hpp cpp/mcts_batched_fast/fast_mcts_batched.cpp
```

**Action**: If significant duplication remains (>100 lines shared), create a follow-up dedup task. If minimal, mark WS6-search as done. Do NOT attempt a large refactor in this session — the user said "short iterations."
**Duration**: 15-30 minutes (audit only).

### Step 4: BC Data Collection from v55 [P1]
**Goal**: Collect self-play games from v55 for BC warmup of next architecture.
**Dependencies**: Step 0 complete (rebuilt binary).
**Commands**:
```bash
cd /home/dkord/code/twilight-struggle-ai
uv run python scripts/collect_selfplay_cpp.py \
    --checkpoint data/checkpoints/scripted_for_elo/v55_scripted.pt \
    --n-games 2000 \
    --batch-size 200 \
    --seed 42 \
    --out data/selfplay/v55_bc_2k.parquet \
    2>&1 | tee results/logs/collect_v55_bc.log
```
**Note**: 2000 games is enough for BC warmup. At ~200 steps/game, that's ~400k training samples. Can run in parallel with Step 2 (WS6 dedup) since it only reads the binary, doesn't modify code.
**Success criterion**: Parquet file exists, >300k rows, no crashes.
**Duration**: 10-30 minutes depending on throughput.

### Step 5: BC Training on v55 Data [P1]
**Goal**: Train a BC checkpoint from v55 self-play data to use as PPO init.
**Dependencies**: Step 4 complete (data collected).
**Commands**:
```bash
cd /home/dkord/code/twilight-struggle-ai
uv run python scripts/train_baseline.py \
    --data-dir data/selfplay \
    --train-files v55_bc_2k.parquet \
    --out-dir data/checkpoints/bc_v55_warmup \
    --epochs 10 \
    --batch-size 256 \
    --lr 3e-4 \
    --seed 42 \
    --advantage-weight 0.5 \
    2>&1 | tee results/logs/bc_v55_warmup.log
```
**Note**: If `--train-files` is not a valid flag, use `--data-dir data/selfplay` and ensure only v55_bc_2k.parquet is in that directory (or move it to a dedicated subdir first):
```bash
mkdir -p data/selfplay/v55_bc_only
cp data/selfplay/v55_bc_2k.parquet data/selfplay/v55_bc_only/
uv run python scripts/train_baseline.py \
    --data-dir data/selfplay/v55_bc_only \
    --out-dir data/checkpoints/bc_v55_warmup \
    --epochs 10 \
    --batch-size 256 \
    --lr 3e-4 \
    --seed 42 \
    2>&1 | tee results/logs/bc_v55_warmup.log
```
**Success criterion**: 10 epochs complete, final card_top1 > 40%, checkpoint saved.
**Duration**: 10-20 minutes (GPU training).

### Step 6: Export BC Checkpoint for PPO [P1]
**Goal**: Convert best BC epoch to TorchScript for PPO init.
**Dependencies**: Step 5 complete.
**Commands**:
```bash
# Find best epoch (lowest val loss or highest card_top1 in logs)
# Then export:
uv run python -c "
import torch, sys
sys.path.insert(0, 'python')
from tsrl.policies.model import TSBaselineModel
# Load best epoch
state = torch.load('data/checkpoints/bc_v55_warmup/baseline_epoch10.pt', map_location='cpu')
# The train_ppo.py expects a raw .pt state dict, not TorchScript
# Just use the .pt file directly as --checkpoint for train_ppo.py
print('BC checkpoint ready:', 'data/checkpoints/bc_v55_warmup/baseline_epoch10.pt')
"
```
**Note**: `train_ppo.py` can load raw `.pt` state dicts directly. No TorchScript export needed for PPO init — only for Elo benchmarking.
**Duration**: 1 minute.

### Step 7: Short-Iteration PPO from BC Warmup [P1]
**Goal**: Run 10-15 PPO iterations from BC checkpoint, measure rollout_wr.
**Dependencies**: Step 6 complete + Step 2 complete (so the rebuilt binary has the dedup fix).
**Commands**:
```bash
cd /home/dkord/code/twilight-struggle-ai

# Use the BC best epoch as init
uv run python scripts/train_ppo.py \
    --checkpoint data/checkpoints/bc_v55_warmup/baseline_epoch10.pt \
    --out-dir data/checkpoints/ppo_v80_bc \
    --n-iterations 15 \
    --games-per-iter 200 \
    --rollout-workers 5 \
    --seed 99800 \
    --ent-coef 0.01 \
    --lr 1e-4 \
    --wandb-project twilight-struggle-ai \
    --wandb-run v80_bc \
    2>&1 | tee results/logs/ppo/ppo_v80_bc.log
```
**Key flags**:
- `--rollout-workers 5` for 3x throughput (confirmed in prior session)
- `--n-iterations 15` for short iteration (user: "short iterations, don't aim hard for Elo wins")
- `--games-per-iter 200` — standard
- `--ent-coef 0.01` — standard entropy regularization
- `--lr 1e-4` — conservative for fine-tuning from BC

**Monitoring**: Check W&B for `rollout_wr` (primary metric). Do NOT launch Elo tournament — user explicitly said "don't waste time on slow Elo tournaments."
**Success criterion**: 15 iterations complete without crash, rollout_wr reported each iteration.
**Duration**: 15 iterations * ~3 min/iter = ~45-60 minutes.

### Step 8: WS5 — Binary Freshness Hook Verification [P2]
**Goal**: Verify the existing `.claude/hooks/check_binary_freshness.py` is actually working.
**Dependencies**: None (can run in parallel with Steps 4-7).
**Commands**:
```bash
# Test the hook
uv run python .claude/hooks/check_binary_freshness.py
```
**Action**: If it exits 0, it's working. If it fails or has bugs, fix them. The hook should compare `.so` modification time vs latest C++ source modification time and warn if stale.
**Duration**: 5 minutes.

### Step 9: WS3 — Checkpoint Identity DB [P2]
**Goal**: Ensure `log_checkpoint()` in `train_ppo.py` is working and populating `results/metadata.sqlite3`.
**Dependencies**: None (can run in parallel with other steps).
**Commands**:
```bash
# Check if metadata.sqlite3 has any checkpoint records
uv run python -c "
import sqlite3
conn = sqlite3.connect('results/metadata.sqlite3')
cursor = conn.execute('SELECT name FROM sqlite_master WHERE type=\"table\"')
tables = [row[0] for row in cursor]
print('Tables:', tables)
for t in tables:
    count = conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    print(f'  {t}: {count} rows')
conn.close()
"
```
**Action**: If `checkpoints` table exists and has records, WS3 is partially done. If not, verify the import path in `train_ppo.py` (lines 33-39) and ensure `_TRACKING_AVAILABLE` is True.
**Duration**: 10 minutes.

### Step 10: Measure DEFCON-1 Rate After PPO [P1]
**Goal**: After PPO training completes, measure DEFCON-1 rate on the new model.
**Dependencies**: Step 7 complete.
**Commands**: Same as Step 1 but with the new PPO checkpoint:
```bash
# Export to TorchScript first
uv run python -c "
import torch, sys
sys.path.insert(0, 'python')
from tsrl.policies.model import TSBaselineModel
# ... load and script the model
"
# Then benchmark
uv run python scripts/benchmark.py \
    --model data/checkpoints/ppo_v80_bc/ppo_best_scripted.pt \
    --opponent heuristic \
    --n-games 500 --seed 50000 \
    2>&1 | tee results/logs/defcon1_v80_bc_benchmark.log
```
**Success criterion**: DEFCON-1 rate <5%, suicide rate <2%.
**Duration**: 10-15 minutes.

### Step 11: Conditional — Continue PPO or Architecture Change [P2]
**Goal**: If Elo is growing (rollout_wr improving), continue PPO. If plateaued, start Phase 2 (DP Allocation Head).
**Dependencies**: Step 10 complete.
**Decision logic**:
- If rollout_wr improved over 15 iterations: run another 15 iterations (`--n-iterations 15 --checkpoint ppo_best.pt`)
- If rollout_wr plateaued (delta < 1% over last 5 iters): start Phase 2 architecture work
- Phase 2 = DP decoder (`python/tsrl/policies/dp_decoder.py`) per `docs/plan_pragmatic_heads.md`

### Step 12: Pipeline Robustness Audit [P3]
**Goal**: Quick wins from WS2/WS7/WS9 that cost <30 minutes each.
**Dependencies**: Can start after Step 7 (while waiting for results).

**WS9 — Stale training watchdog**: Check if a cron job detects stuck PPO runs (no new checkpoint for >30 min). If not:
```bash
# Add to scripts/health_check.sh:
# Check if train_ppo.py is running but hasn't written a checkpoint in 30 min
```

**WS7 — Overlapping confirmation**: After each PPO checkpoint save, kick off a background benchmark (100 games) without waiting. This is already partially done by the panel eval in `ppo_loop_step.sh`. Verify it works.

**WS2 — Snakemake**: Low priority. The shell scripts work. Only add Snakemake if the pipeline gets more complex.

## Critical Path

```
Step 0 (rebuild, 5min)
├── Step 1 (measure DEFCON, 15min) ──── if rate >5%, investigate further before training
├── Step 2 (WS6 dedup, 60min) ──── must complete before Step 7 (so PPO uses fixed binary)
├── Step 4 (collect BC data, 30min) ──── can run IN PARALLEL with Step 2
│   └── Step 5 (BC training, 20min)
│       └── Step 6 (export, 1min)
│           └── Step 7 (PPO 15 iters, 60min) ──── BLOCKED on Step 2 + Step 6
│               └── Step 10 (measure DEFCON on new model, 15min)
│                   └── Step 11 (continue or pivot, varies)
├── Step 8 (WS5 verify, 5min) ──── PARALLEL with anything
├── Step 9 (WS3 verify, 10min) ──── PARALLEL with anything
└── Step 12 (pipeline audit, 30min) ──── PARALLEL with Steps 7-11
```

**Total wall time estimate**: ~3-4 hours for the full critical path.

**Parallelism opportunities**:
- Steps 2 + 4 can overlap (dedup is code editing; data collection is GPU work)
- Steps 8 + 9 + 12 can run anytime as background
- Step 1 is quick and blocks nothing except confirming the fix works

## Conclusions

1. The DEFCON-1 engine fix is merged but not built. Step 0 is strictly blocking.
2. The `fast_mcts_batched.cpp` has a **bug**: its kDefconLoweringCards list has only 13 cards (missing 52 and 68). This is a real correctness issue that WS6 dedup will fix.
3. The `policies.cpp` uses a more nuanced 3-way decomposition of DEFCON-dangerous cards. The consolidated header should preserve this decomposition while also exporting the union set for search files.
4. v55 is the current best at Elo 2118.5. BC training on v55 self-play data before PPO is the user's explicit instruction for architecture changes.
5. The user strongly prefers short iterations and high throughput over Elo tournament precision. Monitor `rollout_wr` on W&B, skip Elo tournaments.
6. WS5 (binary freshness hook) already exists. WS3 (checkpoint DB) needs verification.
7. The Phase 2 architecture change (DP Allocation Head) is the next arch upgrade per `docs/plan_pragmatic_heads.md`, but should only start after confirming BC+PPO works on the current architecture.

## Recommendations

1. **IMMEDIATE**: Run `cmake --build build-ninja -j` and `ctest` to unblock everything.
2. **Within 15 minutes**: Measure DEFCON-1 rate with 500 v55 self-play games. Log result.
3. **First code task (30-60 min)**: Create `cpp/tscore/card_properties.hpp` and fix the `fast_mcts_batched.cpp` bug (missing cards 52, 68). This is the highest-leverage single change.
4. **Start BC data collection in parallel with WS6 dedup**: `collect_selfplay_cpp.py --n-games 2000` from v55. This runs on GPU and doesn't conflict with code editing.
5. **BC training (10 epochs)**: Use `train_baseline.py` on collected data. 10 epochs, batch 256, lr 3e-4.
6. **PPO from BC init (15 iters)**: Use `train_ppo.py` with `--rollout-workers 5 --n-iterations 15`. Monitor rollout_wr only. Skip Elo tournament.
7. **After PPO**: Re-measure DEFCON-1 rate. If <5% and <2% suicide, the user's target is met. If not, investigate which cards are causing the remaining deaths and add targeted guards.
8. **If Elo growing**: Continue PPO iterations in batches of 15. If plateaued: start Phase 2 (DP decoder).
9. **Infrastructure**: Verify WS5 hook works, check WS3 sqlite has records, add stale-training watchdog to health_check.sh.
10. **Do NOT**: Launch slow Elo tournaments, do large architecture refactors, or work on replay parsing / play server / dataset schema changes.

## Open Questions

1. **Card ID verification needed**: The exact card IDs in kDefconLoweringCards need cross-referencing with `data/spec/cards.csv`. Some card IDs in the comments (e.g., "Lone Gunman" at 53, but 53 might be something else in the actual card list) may be wrong. This must be verified before writing `card_properties.hpp`.
2. **policies.cpp 3-way decomposition**: Should the canonical header keep the 3-way split (certain/probabilistic/random-coup) or just the flat union? The 3-way is more correct for the heuristic policy (which needs different penalty weights), but the search files only need the union. Recommendation: export both.
3. **BC checkpoint format**: Does `train_ppo.py --checkpoint` accept raw `.pt` state dicts from `train_baseline.py`, or does it need a specific format? Need to verify by reading the checkpoint loading code in `train_ppo.py`.
4. **v79_sc/v80_sc**: The continuation_plan mentions v79_sc was running and a watcher would auto-launch v80_sc. What happened to these? Check if they completed and what Elo they achieved before starting new training.
5. **DEFCON-1 rate measurement**: The exact API for measuring end_reason in the C++ benchmark bindings is uncertain. Need to check what `tscore.benchmark_self_play` returns or whether `scripts/benchmark.py` logs DEFCON-1 counts.
---
