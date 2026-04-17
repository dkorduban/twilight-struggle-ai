# Opus Analysis: Distilling Side Specialists into Single Model
Date: 2026-04-17T04:04:00Z
Question: Should we distill best USSR and best US specialist checkpoints into a single larger model?

## Executive Summary

The idea has merit but the expected gain is small relative to simpler alternatives, and the infrastructure cost is non-trivial. The v5 capacity test shows USSR-only training improves rollout WR from ~0.558 to ~0.63-0.65 (as USSR) and US-only improves from ~0.325 to ~0.48-0.52 (as US), confirming that freed capacity from single-side focus does help. However, the current model is only ~530K parameters with hidden_dim=256 -- it is not capacity-starved in the traditional sense. The gains likely come from removing the optimization conflict between sides (shared trunk, shared value head, contradictory gradient signals), not from running out of parameters. A simpler path to capture most of this gain is to adopt `TSControlFeatGNNSideModel` (which already has separate value heads + side embedding) and train both sides jointly with the panel-only setup from v5, rather than building a multi-teacher distillation pipeline.

## Findings

### 1. Current Model Architecture and Capacity

The base model (`TSControlFeatGNNSideModel`, used as v56) has **532,635 parameters**:

| Component | Parameters (approx) |
|-----------|-------------------|
| Influence encoder (flat + GNN) | ~75K |
| Card encoder | ~60K |
| Scalar encoder (11+42 dims) | ~4K |
| Side embedding (2x32) | 64 |
| Trunk projection (352->256) | ~90K |
| 2x ResidualBlock (256) | ~132K |
| Card head (256->111) | ~28K |
| Mode head (256->6) | ~1.5K |
| Strategy heads (256->4x86) | ~88K |
| Strategy mixer (256->4) | ~1K |
| Value branches (2x: 256->128->1) | ~66K |
| Small choice head (256->8) | ~2K |

With hidden_dim=384: **~836K params**. With hidden_dim=512: **~1.2M params**.

The model is small by modern standards. Doubling hidden_dim to 512 would roughly 2.3x the parameter count but remain well within GPU memory on the RTX 3050 (4GB).

### 2. What the v5 Capacity Test Shows

**v56 baseline (both sides, same model):**
- USSR vs heuristic: 0.558
- US vs heuristic: 0.325

**USSR-only v5 (50 iters, panel-only, constant LR):**
- Rollout WR progression: iter 1=0.556, iter 10=0.601, iter 20=0.616, iter 30=0.566, iter 39=0.717, iter 43=0.717, iter 50=0.581
- 5-iter rolling average peaks around iter 39-45 at ~0.65
- PFSP table at iter 20: WR vs heuristic=0.405, vs v20=0.619, vs v44=0.616, vs v54=0.568, vs v55=0.545, vs v56=0.614
- Clear improvement over v56 baseline (0.558 -> 0.61+ vs heuristic as USSR)

**US-only v5 (in progress, 35 iters so far):**
- Rollout WR progression: iter 1=0.470, iter 12=0.495, iter 19=0.586, iter 25=0.556, iter 32=0.566, iter 33=0.551, iter 35=0.480
- Very noisy but trending upward from 0.325 baseline
- PFSP at iter 35: WR vs heuristic=0.20, vs v44=0.52, vs iter_0001=0.51
- US side is harder to improve (inherent game asymmetry) but showing gains

### 3. The Distillation Proposal: Two Teachers -> One Student

The proposal: take best USSR checkpoint (e.g., iter ~40-45) and best US checkpoint (e.g., iter ~35-50 when complete), then distill both into a single model with more capacity.

**What this would require:**

1. **Data generation**: Run each specialist playing its side against the panel pool, collect rollout data with action logits. Need ~500K-1M steps per side.

2. **Multi-teacher KD loss**: For each training sample, determine which side is acting, then use the corresponding specialist's soft targets:
   ```
   L = L_hard + alpha * (KL(student_card || teacher_card) + KL(student_mode || teacher_mode))
   ```
   Where teacher is selected based on acting side.

3. **Student model**: A larger model (e.g., hidden_dim=384 or 512) to have enough capacity for both sides.

4. **Infrastructure**: The existing `teacher_targets` path in `train_baseline.py` supports teacher KL loss with soft card/mode/value targets. However, it is keyed by `(game_id, step_idx)` for joining with base data, not designed for PPO rollout data. Adapting it would require either:
   - Saving PPO rollout data as Parquet with teacher logits annotated
   - Or building a new distillation script

### 4. Why the Gains from Side-Specific Training Exist

The improvement is NOT primarily about parameter count. Key evidence:

1. **The model has ~530K params -- small but not tiny.** A 256-dim trunk with 2 residual blocks has decent expressivity. The model already has separate value heads per side (`TSControlFeatGNNSideModel`).

2. **The shared policy heads are the bottleneck.** Card head, mode head, and strategy heads are shared. When training on USSR data, gradients push card preferences toward USSR-favorable plays (e.g., playing Decolonization for event). When training on US data, gradients push the opposite direction. These contradictory gradients create an interference pattern in the shared weights.

3. **The trunk representation faces the same conflict.** The 256-dim hidden representation must encode features useful for BOTH sides' decisions. Features important for USSR play (e.g., detecting coup opportunities in contested regions) may compete with US-relevant features (e.g., detecting containment opportunities).

4. **The value head is already split**, so this is not the bottleneck. The policy side is.

### 5. Risk Analysis

**Risks of multi-teacher distillation:**

1. **Interference at the trunk level is the exact problem we are trying to solve.** If the student model trains on both sides' data simultaneously with teachers providing conflicting soft targets for similar board states, the trunk will face the same representational conflict -- just with teacher guidance. More capacity helps, but does not eliminate the fundamental tension.

2. **Catastrophic forgetting during distillation.** If we train USSR steps first then US steps (or interleave with uneven ratios), the model may forget one side while learning the other. This requires careful interleaving and possibly side-balanced batches.

3. **Teacher quality ceiling.** The specialists are only ~50 PPO iterations from v56. Their improvement is real but modest (USSR: 0.558->0.61, US: 0.325->0.48). The soft targets from these teachers are only slightly better than v56 itself. The knowledge-distillation "dark knowledge" (inter-class probabilities) may not contain much signal beyond what harder targets provide.

4. **Complexity cost.** Building a multi-teacher distillation pipeline for marginal gains over simpler approaches is engineering time that could go toward other improvements (exploration noise, ISMCTS, better opponents).

### 6. Alternative Approaches (Simpler, Likely Sufficient)

**Alternative A: Side-conditioned policy heads (recommended)**

Instead of shared policy heads, use side-conditional policy:
- Add FiLM (Feature-wise Linear Modulation) after the trunk, conditioned on side embedding
- Or simply use 2 sets of policy heads (card_head_ussr, card_head_us, etc.), selected at forward time like the value heads
- This directly addresses the gradient conflict without needing distillation
- Can be trained with the exact same v5 setup (panel-only, constant LR, both sides)
- Estimated cost: ~200K additional params for duplicated heads, zero new infrastructure

**Alternative B: Continue v5-style training with `--side both` but separate heads**

Train the model on both sides simultaneously with:
- Separate policy heads per side (as in Alternative A)
- Panel-only opponents (no self-play inflation)
- Constant LR (avoid v4's premature death)
- This is essentially what distillation would achieve, but simpler

**Alternative C: Inference-time ensemble**

At inference time, load both specialist checkpoints and select the appropriate one based on which side is playing. This is:
- Zero training cost
- 2x model memory at inference (trivial at 530K params)
- Captures 100% of the specialist improvement
- The simplest possible approach

**Alternative D: Weighted averaging of specialist weights**

Average the two specialist models' weights: `w_combined = alpha * w_ussr + (1-alpha) * w_us`. This sometimes works when models are close in weight space (both fine-tuned from the same v56 base). Quick to test (10 minutes) but may produce a worse model if the weight landscapes have diverged significantly.

### 7. Capacity Scaling Assessment

If we do want more capacity (regardless of distillation), the options:

| Config | Params | Training Speed Impact | Expected Benefit |
|--------|--------|----------------------|------------------|
| hidden=256 (current) | 530K | baseline | baseline |
| hidden=384 | 836K | ~1.3x slower | moderate if trunk is bottleneck |
| hidden=512 | 1.2M | ~1.8x slower | uncertain -- may need more data |
| 3 residual blocks | ~660K | ~1.15x slower | marginal depth increase |
| hidden=256 + duplicate heads | ~730K | ~1.1x slower | directly addresses interference |

Given the RTX 3050 (4GB) and the ~30s/iteration training speed, hidden=384 is feasible. Hidden=512 might push against memory limits with the current batch size of 2048.

## Conclusions

1. **The distillation idea is sound in principle but overkill for the current situation.** The specialist checkpoints are only modestly better than v56 (5-15 percentage points of rollout WR improvement), which means the "dark knowledge" in their soft targets is limited.

2. **The root cause of side-specific improvement is gradient interference in shared policy heads**, not parameter count. More capacity helps but does not fix the architectural conflict.

3. **Inference-time ensemble (Alternative C) captures 100% of the specialist gain with zero training cost.** If the goal is simply "play both sides as well as the specialists," just load the right checkpoint per side.

4. **For a single unified model, duplicate policy heads per side (Alternative A) is strictly better than distillation.** It directly removes the gradient conflict, requires no new infrastructure, and can be trained with the existing v5 setup.

5. **If distillation is pursued anyway, the existing `train_baseline.py` teacher infrastructure is 80% of the way there.** The main gap is generating Parquet rollout data from each specialist with annotated teacher logits and side labels.

6. **A modest capacity increase to hidden_dim=384 (~836K params) is worthwhile regardless**, as the model will soon face harder opponents and more complex game situations. This is orthogonal to the side-specialist question.

7. **Weight averaging (Alternative D) is worth a 10-minute test** before investing in anything more complex. Both specialists descend from v56, so their weight spaces may overlap enough for linear interpolation to work.

## Recommendations

1. **Immediate (10 min): Test weight averaging.** Load both specialist ppo_best.pt checkpoints, average their state dicts with alpha=0.5, benchmark the result. If it works, this is free strength.

2. **Short-term (1-2 hours): Implement side-conditional policy heads.** Duplicate card_head, mode_head, strategy_heads per side in `TSControlFeatGNNSideModel` (which already has separate value heads). Select at forward time based on `scalars[:, 10]`. Train with `--side both` using the v5 panel-only setup.

3. **Short-term (0 hours): Use inference-time ensemble for immediate deployment.** Load USSR specialist when playing as USSR, US specialist when playing as US. This is the zero-cost option that gives 100% of the specialist improvement.

4. **Medium-term: Increase hidden_dim to 384.** This is orthogonal and beneficial regardless. Requires BC warm-start (per standing rules: BC before PPO for arch changes) on the best-model games.

5. **Skip multi-teacher distillation** unless the weight-averaging and side-conditional-heads approaches fail to close the gap. The infrastructure cost is not justified given the alternatives.

## Open Questions

1. **How much do the specialist weights diverge from v56?** If the L2 distance is small, weight averaging will work well. If large, it will fail. A quick `torch.norm(w_ussr - w_us)` per layer would answer this.

2. **Does the US-only v5 run (still in progress) plateau or continue improving?** If US improvement stalls at ~0.48 while USSR reaches 0.65, the asymmetry suggests the US side needs more than just freed capacity -- it may need fundamentally different strategic patterns that the current feature set does not support well.

3. **Would side-conditional policy heads hurt the model's ability to predict opponent behavior?** If the model uses different card preferences per side, it may lose the implicit "what would my opponent play here?" information that shared heads provide. This could matter for value prediction quality.

4. **Is the v5 improvement from capacity or from the constant LR fix?** The v4 run used cosine LR and froze by iteration 50. The v5 improvement might be entirely from avoiding premature LR death, not from single-side focus. A `--side both` run with v5's constant LR setup would isolate this.
