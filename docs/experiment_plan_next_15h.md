# Experiment Plan: Next 10-15 Hours

Written: 2026-04-04
Author: Opus experiment lead
Base: experiment_log_phase1.md (901 lines), elo_ratings.json

---

## 1. Analysis

### What we know

The best greedy model is **v99_cf_1x95_s7** at 32.4% combined (51.1% USSR, 13.7% US), using the control_feat architecture trained on nash_c heuristic data with 95 epochs and a lucky seed. The mean across 3 seeds for that configuration is 29.4%, which equals the baseline architecture's best single-seed result (29.5% for saturation_1x_95ep). This means the architecture edge is real but small (+4pp mean vs baseline's 25.3% mean), and dominated by seed variance (5.4pp range for cf_1x95).

MCTS with 400 sims adds **+5.7pp combined** over greedy policy vs heuristic (37.0% vs 31.3%), after the double-softmax fix. This is the single largest improvement lever we have found. MCTS vs greedy-NN head-to-head shows +15pp, confirming the value head and priors are good enough for search to help substantially.

### What has been ruled out

1. **BC self-play data mixing**: Gen1 (-1pp), Gen2 (-11pp), AWR (-3.7pp), fine-tune (-3.8pp). The model's self-play data is too similar to heuristic data to provide novel signal. Self-play from BC models is dead.
2. **actor_relative value target**: -7.3pp. Requires actor-relative input encoding (not implemented).
3. **Teacher distillation with mixed data**: v101 (-11pp) and v103 (overfitting, val_loss 6.0+). Mixing MCTS rows into BC training data confuses the behavior cloning loss. The teacher KL needs to be applied to heuristic positions, not MCTS-trajectory positions.
4. **2x data at 95 epochs**: -4.4pp from 1x@95ep. Severe overfitting. The one-cycle schedule length must match data scale.
5. **More than 95 epochs on 1x**: 120ep is -3.6pp. Already past the optimum.

### What is most promising

The highest-leverage path is **making the greedy policy stronger**, because MCTS amplifies policy quality. A 2pp greedy improvement could yield 3-4pp with MCTS. The avenues are:

1. **Nash_c data instead of nash_b**: Nash_c has higher mean (26.3% vs 23.7%) and dramatically lower seed variance (1.2pp vs 11.7pp range). The best models (v99_cf_1x95_s7) were trained on nash_b. Retraining on nash_c could yield a more stable and possibly stronger base.

2. **Multi-seed selection**: Training 3-5 seeds and picking the best is a legitimate strategy given the 5pp seed variance. With 5 seeds, the expected best is ~mean + 1.2*sigma, yielding ~2-3pp uplift over mean.

3. **Teacher KL on heuristic rows only**: Instead of mixing MCTS data into training, generate MCTS teacher targets for existing heuristic positions and train BC+KL on the same heuristic data. This avoids the data mixing problem that killed v101 and v103.

4. **MCTS at inference time**: Already proven at +5.7pp. Optimize sim count and evaluate whether ISMCTS (hidden info) captures the same benefit.

---

## 2. Experiment Sequence

### Experiment 0: Benchmark v103 (pending)
**Description**: v103_mcts_teacher_w05 finished training. Export best checkpoint and benchmark vs heuristic.
**Command**:
```bash
cd /home/dkord/code/twilight-struggle-ai
# Export
uv run python -c "
import torch
from tsrl.policies.model import TSControlFeatModel
ckpt = torch.load('data/checkpoints/v103_mcts_teacher_w05/baseline_best.pt', map_location='cpu', weights_only=False)
model = TSControlFeatModel(hidden_dim=256)
model.load_state_dict(ckpt['model_state_dict'])
model.eval()
sm = torch.jit.script(model)
sm.save('data/checkpoints/v103_mcts_teacher_w05/baseline_best_scripted.pt')
"
# Benchmark
PYTHONPATH=build-ninja/bindings nice -n 19 uv run python scripts/benchmark_batched.py \
  --model data/checkpoints/v103_mcts_teacher_w05/baseline_best_scripted.pt \
  --games 1000 --pool-size 32 --seed 42000 --label v103_mcts_teacher_w05
```
**Expected outcome**: v103 likely regresses vs v99_cf_s7 (32.4%) given val_loss plateau at 6.0. If combined < 25%, confirms MCTS-data-mixing approach is broken. If > 30%, teacher KL on high-coverage data has promise.
**Decision**: If v103 < 28%, abandon MCTS-data-mixing entirely. Proceed to Exp 1.
**Time**: 0.5h

### Experiment 1: Nash_c control_feat baseline (3 seeds)
**Description**: Train v99_cf on nash_c data (instead of nash_b) to test whether the more stable dataset produces a stronger or more reliable base model.
**Command**:
```bash
for SEED in 42 7 123; do
  uv run python scripts/train_baseline.py \
    --data-dir data/selfplay \
    --out-dir data/checkpoints/v104_cf_nashc_s${SEED} \
    --model-type control_feat --hidden-dim 256 \
    --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
    --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
    --one-cycle --deterministic-split \
    --value-target final_vp --seed ${SEED}
    # NOTE: --data-dir must point to a directory containing ONLY nash_c parquet
done
```
**Data prep**: Create a symlink directory containing only `heuristic_10k_setup_bid2_nash_c.parquet`.
**Expected outcome**: Mean combined ~27-29%. If nash_c seed variance is <3pp (vs nash_b's 11.7pp), it confirms nash_c as the better training set. Best single seed could match or exceed 32.4%.
**Decision criteria**: If mean > 28% AND variance < 4pp, switch all future training to nash_c. If best seed > 32%, use that as new base for MCTS teacher experiments.
**Time**: 3 x 15min training + 3 x 30min benchmark = 2.5h

### Experiment 2: MCTS sim count sweep (post double-softmax fix)
**Description**: The previous sim sweep (100/200/400/800 at 100 games/side) had the double-softmax bug. Rerun with the fix to establish the correct sim count curve and determine optimal sims for teacher data collection and inference.
**Command**:
```bash
for SIMS in 50 100 200 400; do
  PYTHONPATH=build-ninja/bindings nice -n 19 uv run python scripts/benchmark_vf_mcts.py \
    --model data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt \
    --sims ${SIMS} --games 100 --pool-size 32 --seed 42000 \
    --label "mcts_${SIMS}sim_fixed"
done
```
**Expected outcome**: Monotonic improvement from 50->400 sims (unlike the pre-fix bug where 800 regressed). Combined WR: 50sim ~33%, 100sim ~35%, 200sim ~36%, 400sim ~37%.
**Decision criteria**: If 200sim >= 36% and 400sim adds <1pp, use 200sim for teacher data (2x faster collection). If 400sim > 200sim by >2pp, use 400sim.
**Time**: 50sim=20min, 100sim=40min, 200sim=80min, 400sim=160min. Total ~5h if sequential. Run 50+100 in parallel vs 200, then 400.

### Experiment 3: Teacher KL on heuristic positions (no data mixing)
**Description**: The key insight from v101/v103 failures is that mixing MCTS trajectory rows into BC data hurts. Instead: (a) collect MCTS teacher targets for a subset of *heuristic* game positions, (b) train BC on the full heuristic dataset with KL loss applied only to rows that have teacher targets. This keeps the BC distribution intact while nudging the policy toward search-quality decisions.
**Command** (teacher target collection):
```bash
# Collect MCTS teacher targets for nash_c heuristic positions
# Select ~10% of nash_c positions (every 10th row by game_id) and run 200-sim MCTS
PYTHONPATH=build-ninja/bindings nice -n 19 uv run python scripts/collect_mcts_targets.py \
  --model data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt \
  --data data/selfplay/heuristic_10k_setup_bid2_nash_c.parquet \
  --sims 200 --sample-rate 0.10 --output data/selfplay/mcts_teacher_nashc_200sim.parquet \
  --seed 42
```
**Note**: `collect_mcts_targets.py` may not exist yet. If not, this requires implementation (1-2h via Codex). The script would: load heuristic positions, run MCTS from each position to get visit count distributions, save as teacher targets.
**Command** (training with teacher KL):
```bash
uv run python scripts/train_baseline.py \
  --data-dir <nash_c_only_dir> \
  --out-dir data/checkpoints/v105_teacher_heur_kl_s42 \
  --model-type control_feat --hidden-dim 256 \
  --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
  --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
  --one-cycle --deterministic-split \
  --value-target final_vp --seed 42 \
  --teacher-targets data/selfplay/mcts_teacher_nashc_200sim.parquet \
  --teacher-weight 0.5
```
**Expected outcome**: +1-3pp over pure BC baseline if teacher targets are meaningful. The KL loss should make the policy sharper on the ~10% of positions where MCTS disagrees with BC, without degrading the other 90%.
**Decision criteria**: If combined > 31% (single seed), run 2 more seeds. If combined > 33%, this is the new best approach. If combined < 29%, teacher targets at 10% coverage are too sparse.
**Time**: Target collection ~3-5h (depends on sample rate). Training ~15min. Implementation if needed ~2h. Total: 3-7h.

### Experiment 4: Multi-seed selection tournament
**Description**: Train 5 seeds of the best configuration (whichever of Exp 1 or Exp 3 wins) and pick the best. With 5.4pp seed range observed for cf_1x95, the expected best-of-5 is ~mean + 1.5pp.
**Command**: Same as winning config with seeds 42, 7, 123, 999, 2024.
**Expected outcome**: Best-of-5 should be 1-2pp above 3-seed mean.
**Decision**: Use the best seed as the final release candidate model.
**Time**: 5 x 15min training + 5 x 30min benchmark = 3.5h

### Experiment 5: ISMCTS vs heuristic at optimal sim count
**Description**: Once Exp 2 establishes optimal full-info MCTS sims, run ISMCTS at that sim count (8 dets) to quantify the hidden-info penalty.
**Command**:
```bash
PYTHONPATH=build-ninja/bindings nice -n 19 uv run python scripts/benchmark_vf_mcts.py \
  --model <best_model_scripted.pt> \
  --sims <optimal> --dets 8 --ismcts --games 200 --pool-size 32 --seed 42000 \
  --label "ismcts_<optimal>sim_best"
```
**Expected outcome**: ISMCTS should be 2-5pp below full-info MCTS. If the gap is <3pp, ISMCTS is viable for online play.
**Time**: 2-4h depending on sim count.

---

## 3. Priority Reasoning

**Exp 0 first** because v103 results are pending and take only 30min. We need to close the loop before planning further teacher experiments.

**Exp 1 second** because it is cheap (3 training runs, ~2.5h total), addresses the largest source of uncertainty (dataset choice), and directly improves the base model that everything else builds on. Nash_c's dramatically lower seed variance could make all subsequent experiments more reliable.

**Exp 2 third** because it establishes the MCTS sim count curve post-fix, which informs both inference-time search strength and teacher data collection cost. This runs on CPU and can overlap with GPU training.

**Exp 3 fourth** because it is the highest-risk/highest-reward experiment. Teacher distillation on heuristic positions is the theoretically correct approach that was never properly tested (v101/v103 failed due to data mixing, not due to KL loss itself). This may require implementation work.

**Exp 4 last** because it is a pure consolidation step -- only worth running after we know which configuration is best.

**Exp 5 is optional** -- only if time remains after Exp 3 results are in.

### Parallelism plan

| Hour | GPU | CPU |
|------|-----|-----|
| 0-0.5 | Exp 0 export | Exp 0 benchmark |
| 0.5-1.5 | Exp 1 seed=42 train | Exp 2: 50sim + 100sim MCTS sweep |
| 1.5-2.5 | Exp 1 seed=7 train | Exp 2: 200sim MCTS sweep |
| 2.5-3.5 | Exp 1 seed=123 train | Exp 2: 400sim MCTS sweep (start) |
| 3.5-5.0 | Exp 1 benchmarks (CPU) | Exp 2: 400sim MCTS sweep (finish) |
| 5.0-7.0 | Exp 3 teacher collection (if script exists) OR Codex implementation | |
| 7.0-8.0 | Exp 3 training | |
| 8.0-10.0 | Exp 3 benchmark + analysis | |
| 10.0-13.5 | Exp 4 (if warranted) | Exp 5 ISMCTS (if time) |

---

## 4. What NOT To Do

1. **Do not collect more BC self-play data.** Gen1 (-1pp), Gen2 (-11pp), AWR (-3.7pp), fine-tune (-3.8pp). This approach is exhaustively proven dead. Self-play from BC models does not provide novel signal.

2. **Do not mix MCTS trajectory data into BC training.** v101 (-11pp) and v103 (overfitting) prove that MCTS-generated game trajectories have different action distributions that poison the BC loss. The correct approach is teacher KL on heuristic positions (Exp 3), not data mixing.

3. **Do not implement actor-relative input encoding.** This is a large architecture change (flip VP sign, swap actor/opponent influence) that would invalidate all existing data and checkpoints. The potential payoff (better US play) is unclear and the cost is high. US WR is structurally stuck at 8-14% for all approaches -- this is likely a game-level asymmetry, not a modeling failure.

4. **Do not try country_attn architecture.** It showed no benefit over baseline at h256 (23.0% vs 22.4%) and needs huge capacity to work. Control_feat is simpler and at least as good.

5. **Do not try 2x data.** 2x@47ep (26.9%) < 1x@95ep (29.5%). 2x@95ep (22.5%) is catastrophic. The lesson is clear: less data, more epochs, better learning.

6. **Do not increase hidden_dim beyond 256.** The model has ~1M params at h256 and trains in 15min. Larger models would slow iteration without evidence of capacity bottleneck (the model achieves 65% card_top1, suggesting features matter more than capacity).

7. **Do not spend time on online play server, parallel MCTS threading, or benchmark report.** These are polish items that don't improve win rate.

8. **Do not run single-seed experiments and draw conclusions.** Seed variance is 3-5pp. Always run 3 seeds minimum for architecture/data comparisons. Multi-seed for hyperparameter changes is acceptable if the expected effect is >5pp.
