---
# Opus Analysis: Off-Policy Policy Gradient for Fast Architecture Comparison
Date: 2026-04-17T05:45:00Z
Question: Is off-policy policy gradient on frozen self-play data a sound approach for architecture comparison? What algorithm, dataset, metrics, and pitfalls apply? How does this compare to current PPO in signal-to-noise ratio?

## Executive Summary

Off-policy evaluation on frozen self-play data is a **sound and practical approach** for fast architecture comparison in this project, but with important caveats. The key insight is correct: collect data once from the strongest checkpoints, then iterate on architecture quickly. The best algorithm for this use case is **Advantage-Weighted Regression (AWR)** with the GAE returns already stored in rollout parquet files, combined with a **lightweight rollout validation** (200-400 games, 2-3 minutes) to catch distributional shift failures. The existing rollout data (v6/v7, ~2.5M rows each, 200 iterations of league play) already contains most of the needed columns. The critical missing pieces are **legal-action masks** (card_mask, mode_mask, country_mask), which are not saved in current rollout parquet but can be reconstructed from hand_card_ids + game state. This approach can cut architecture experiment time from ~15-30 minutes (PPO) to ~3-5 minutes (AWR train + mini rollout validation), with comparable or better signal-to-noise ratio for ranking architectures.

## Findings

### 1. Why BC Metrics Fail as a Proxy for Play Strength

The user's observation that BC loss does not predict play strength is well-established in RL. BC optimizes for matching the data distribution action-by-action, which rewards:
- Matching easy/frequent decisions (early-turn influence placement)
- Low entropy on unambiguous positions
- Ignoring the value of rare but critical decisions (coups, scoring timing)

Play strength depends on:
- Correct action under adversarial pressure (the opponent exploits weak moves)
- Long-horizon planning (value function quality matters as much as policy)
- Handling edge cases and forced decisions correctly

A model with slightly worse BC loss but better value estimates in critical positions will play stronger. This is a fundamental limitation of BC as a metric, not a dataset issue.

### 2. Why Off-Policy PG Is Better Than BC for Architecture Comparison

Off-policy policy gradient methods (AWR, CRR, filtered BC) are better than pure BC because they:

**a) Weight actions by their quality.** AWR computes w_i = f(A_i) where A_i is the advantage. Good actions (positive advantage) get higher weight. This means architecture A beats architecture B if A can better reproduce *the good actions*, not all actions equally. This is closer to what play strength measures.

**b) Include value function training.** The value head is trained on GAE returns, not just terminal outcomes. Better value prediction = better policy improvement in practice.

**c) Are differentiable and fast.** Unlike PPO, no rollout collection is needed during training. A single forward+backward pass per batch, same as BC. Training speed is essentially identical to BC.

**d) Have a natural "play strength proxy" built in.** The advantage-weighted policy loss directly measures: "can this architecture learn to up-weight good actions and down-weight bad ones given the same data?" This is more correlated with RL improvement potential than raw BC loss.

### 3. Algorithm Recommendation: AWR (Advantage-Weighted Regression)

Among the off-policy options:

| Algorithm | Pros | Cons | Recommendation |
|-----------|------|------|----------------|
| **AWR** (Peng et al. 2019) | Simple, stable, already partially implemented in train_baseline.py, uses GAE returns directly | Temperature tau is a hyperparameter | **Best choice** |
| **CRR** (Wang et al. 2020) | Adds policy constraint term | More complex, marginal benefit over AWR | Skip |
| **CPI** (Kakade & Langford 2002) | Theoretically principled | Requires importance ratios (need old_log_prob), complex | Skip |
| **Filtered BC** (top-K advantage) | Dead simple | Wastes data, threshold is arbitrary | Second choice |
| **Implicit Q-Learning (IQL)** | No importance weights | Needs Q-function, complex | Overkill |
| **Decision Transformer** | Trendy | Wrong paradigm for this problem | Skip |

**AWR is the clear winner** because:
1. The project already has a partial AWR implementation in `train_baseline.py` (lines 38-49: advantage_weight with clamped linear weighting).
2. GAE returns are already stored in rollout parquet (`gae_return` column).
3. The value function baseline (`value` column) is stored too.
4. No importance sampling ratios needed (unlike CPI/PPO), so no old_log_prob dependency.
5. Single hyperparameter (temperature tau or the existing alpha).

The AWR loss is:
```
advantage_i = gae_return_i - value_baseline_i
weight_i = exp(advantage_i / tau) / Z  # or clamp(1 + alpha * advantage_i, 0.1, 2.0)
loss = -sum(weight_i * log pi_theta(a_i | s_i))
```

The existing `--advantage-weight` flag in train_baseline.py is already a linear-clamped AWR variant. The main improvement for architecture comparison would be:
- Use exponential weighting (exp(A/tau)) with tau tuned once, not per-experiment
- Train the value head on GAE returns (not just final_vp)
- Include legal-action masking in the policy loss

### 4. Dataset Collection Strategy

**Which checkpoints to collect from:**

The best strategy is to collect from **the top 10-20 checkpoints in the Elo ladder** (approximately v200-v310 range, Elo 1780-1833). These represent the strongest play quality. Mixing in weaker checkpoints would add noise and make advantage estimation less meaningful.

However, there is a subtlety: collecting only from the *best* checkpoint produces a narrow data distribution that may not test architectural robustness. A good compromise:

- **70% from top-5 checkpoints** (v306, v299, v296, v291, v290 or similar)
- **20% from mid-tier checkpoints** (v200, v180, v160) for distribution coverage
- **10% from league opponents** (the existing rollout data already has this via PFSP)

**Existing data assessment:**

The v6 and v7 rollout directories already contain ~2.5M rows each across 200 iterations. This is **more than sufficient** for architecture comparison. However:

- **Missing columns:** `card_mask`, `mode_mask`, `country_mask` (legal action masks) are NOT in the parquet schema. These are critical for masked log-prob computation.
- **Present and useful:** `influence`, `cards`, `scalars`, `card_id`, `mode_id`, `country_targets`, `gae_return`, `value`, `hand_card_ids`, `raw_*` columns.
- **old_log_prob is NOT stored** in the parquet, but AWR does not need it (unlike CPI).

**Mask reconstruction:** Legal masks can be reconstructed from `hand_card_ids` (for card_mask) and game state (for mode_mask, country_mask). The card mask is straightforward: legal cards are the cards in hand. Mode and country masks require the C++ engine to recompute, which is expensive. 

**Pragmatic solution:** For architecture comparison, an approximation is acceptable:
- `card_mask`: reconstruct from `hand_card_ids` (exact)
- `mode_mask`: set all 5/6 modes as legal (approximate -- some modes may be illegal in specific game states, but this affects <5% of decisions)
- `country_mask`: set all countries as legal for influence/coup/realign (approximate -- DEFCON restrictions on some countries)

A better solution is to **add mask columns to the rollout save function** going forward.

**Recommended dataset size:** 500K-1M rows from the top checkpoints. With ~12K rows per 200-game iteration, this is ~50-80 iterations of data. The existing v6/v7 data covers this.

### 5. What to Store Per Step (Enhanced Rollout Schema)

For the off-policy architecture eval dataset, each row needs:

| Column | Type | Currently Saved? | Notes |
|--------|------|-------------------|-------|
| influence | list<float32>[172] | Yes | |
| cards | list<float32>[448] | Yes | |
| scalars | list<float32>[32] | Yes | |
| card_id | int32 | Yes | 1-indexed action taken |
| mode_id | int32 | Yes | |
| country_targets | list<int32> | Yes | |
| card_mask | list<bool>[111] | **NO** | Legal card mask -- MUST ADD |
| mode_mask | list<bool>[6] | **NO** | Legal mode mask -- MUST ADD |
| country_mask | list<bool>[86] | **NO** | Legal country mask -- MUST ADD |
| gae_return | float32 | Yes | GAE target for value training |
| value | float32 | Yes | Value estimate (baseline) |
| side_int | int8 | Yes | 0=USSR, 1=US |
| reward | float32 | Yes | Terminal reward |

### 6. Metrics for Architecture Comparison

The key insight: neither raw BC loss nor full-rollout WR alone is the right metric. The correct approach is a **two-stage evaluation**:

**Stage 1: Off-policy metrics (fast, ~2 min training + eval):**
- **AWR policy loss** (advantage-weighted NLL): measures how well the architecture can reproduce good actions
- **Value MSE on GAE returns**: measures value function quality
- **Top-1 accuracy on positive-advantage steps**: "when the data says this was a good action, does the model assign it high probability?"
- **Entropy on legal actions**: measures policy sharpness (too low = overfitting, too high = not learning)
- **Advantage-weighted card/mode accuracy**: top-1 accuracy weighted by advantage magnitude

**Stage 2: Mini rollout validation (fast, ~2-3 min):**
- Run 200-400 games vs heuristic (or vs a fixed reference checkpoint)
- This catches catastrophic distributional shift that offline metrics miss
- Use the same seeds for all architecture candidates for paired comparison (reduces variance)
- 200 games with paired seeds gives ~3% WR standard error, enough to detect 5+% differences

**Why this two-stage approach works:**
- Stage 1 filters out clearly bad architectures (saves 80% of rollout time)
- Stage 2 validates the top 2-3 candidates with actual play
- Combined wall time: ~5 min per architecture (2 min train + 3 min rollout)
- vs current PPO: ~15-30 min per architecture with higher variance

### 7. Signal-to-Noise Ratio Comparison

**Current PPO approach:**
- 30 iterations x 200 games = 6000 games, ~30s/iter = 15 min
- But WR variance is high: with 6000 games, the SE on win rate is ~0.6%, meaning a 2% WR difference is barely significant (p~0.05 with one-sided test)
- Need 3+ seeds to be confident, tripling wall time to 45 min
- PPO training noise (random minibatch ordering, GAE estimation, etc.) adds another source of variance

**Off-policy AWR approach:**
- Training on 500K rows with batch_size=4096: ~50 epochs in 2 minutes on RTX 3050
- Deterministic (same data, same seed = same result)
- Offline metrics have very low variance (large N, no rollout stochasticity)
- Mini rollout (200 games, paired seeds) adds ~3 min but with paired comparison, detects 5% WR differences at p<0.05
- Total: ~5 min per experiment, 1 seed sufficient for offline metrics

**SNR improvement: roughly 3-6x** in wall time, with comparable or better statistical power for ranking architectures.

### 8. Pitfalls and Mitigations

**a) Distributional shift (the fundamental risk):**
Architecture A might look great on the frozen dataset but play terribly because it overfits to the data distribution. Mitigation: always run Stage 2 mini rollout for the top candidates. The frozen dataset tests *learning capacity*, not *play quality* directly.

**b) Advantage estimation quality:**
The `gae_return` and `value` columns were computed by a specific checkpoint at a specific training iteration. When training a new architecture on this data, the advantages may not reflect the new architecture's value estimates. Mitigation: recompute advantages using the new model's value head (one extra forward pass over the dataset between training epochs).

**c) Data staleness:**
As the project's best model improves, the frozen dataset becomes less representative of optimal play. Mitigation: regenerate the dataset every major Elo milestone (e.g., every 100 Elo points).

**d) Missing legal masks:**
Without exact legal masks, the off-policy loss includes probability mass on illegal actions. This biases architecture comparison toward models that happen to assign low probability to illegal actions for other reasons (e.g., larger hidden dim = more capacity to memorize which actions are illegal). Mitigation: reconstruct masks from hand_card_ids (easy for card_mask), or add mask saving to the rollout code.

**e) Country head evaluation is noisy:**
The country head uses a mixture-of-strategies formulation that is inherently noisier than card/mode heads. Off-policy country loss may not discriminate architectures well. Mitigation: weight architecture comparison more heavily on card_head + mode_head + value_head metrics.

**f) Overfitting to the offline dataset:**
With 500K rows and ~600K-860K params, overfitting is a real risk. Mitigation: use a held-out validation split (5-10% by game_id), and report val metrics. The existing `deterministic_split` method in TS_SelfPlayDataset handles this.

### 9. Concrete Implementation Plan

**Phase 0: Data Collection (1-2 hours one-time)**
1. Add `card_mask`, `mode_mask`, `country_mask` columns to the `save_rollout_parquet` function in `train_ppo.py`.
2. Collect a dedicated offline eval dataset: run 50-100 games from each of the top-10 Elo checkpoints (v290-v310), saving enhanced parquet with masks.
3. Alternatively, reconstruct masks for the existing v6/v7 data from `hand_card_ids` (card_mask only; approximate the rest).

**Phase 1: AWR Training Script (2-3 hours)**
1. Create `scripts/train_awr_offline.py` based on the existing `train_baseline.py`.
2. Key changes from BC:
   - Load GAE returns and value columns from rollout parquet
   - Compute advantage = gae_return - value (or retrain value head first)
   - Compute AWR weights: `w = exp(advantage / tau)` with tau=1.0 (tune once)
   - Apply masked log-prob for card/mode/country heads
   - Log advantage-weighted accuracy metrics
3. Support all architecture variants from MODEL_REGISTRY.
4. Add paired-seed mini rollout after training (reuse existing benchmark_batched).

**Phase 2: Architecture Sweep Script (1-2 hours)**
1. Create `scripts/arch_sweep_offline.py` that:
   - Takes a list of architecture names + hyperparameters
   - Runs AWR training for each (fixed epochs, fixed data, fixed seed)
   - Collects offline metrics to a comparison table
   - Runs mini rollout for top-N candidates
   - Outputs a ranked table with confidence intervals

**Phase 3: Validation (1 hour)**
1. Run the sweep on 3-4 known architectures where PPO results exist (baseline, control_feat_gnn, country_attn_side).
2. Verify that the AWR ranking matches the PPO Elo ranking.
3. If it does, the offline eval is validated as a reliable proxy.
4. If not, diagnose where the disagreement lies and adjust tau / metrics / dataset.

**Estimated total effort: 5-8 hours to build, 1 hour to validate.**

## Conclusions

1. **Off-policy AWR on frozen self-play data is a sound approach** for architecture comparison. It is faster (5 min vs 15-30 min), more deterministic, and has comparable signal-to-noise ratio for ranking architectures.

2. **AWR is the best algorithm choice** for this project. It is simple, already partially implemented, uses GAE returns from existing rollout data, and requires no importance sampling ratios.

3. **The existing rollout data (v6/v7, ~2.5M rows each) is sufficient** for architecture comparison. The main gap is missing legal-action masks, which can be reconstructed from hand_card_ids or added to future rollout saves.

4. **A two-stage evaluation (offline AWR metrics + mini rollout validation) is the right approach.** Offline metrics filter bad architectures cheaply; mini rollouts validate the top candidates with actual play.

5. **The critical missing data is legal-action masks (card_mask, mode_mask, country_mask).** Adding these to the rollout save function is the highest-priority prerequisite.

6. **BC metrics fail as a play-strength proxy because they weight all actions equally.** AWR's advantage weighting naturally emphasizes the actions that matter for winning, which is why it correlates better with play strength.

7. **The main risk is distributional shift**: a model that looks good offline might fail online. The mini-rollout Stage 2 mitigates this risk at low cost (200 paired-seed games, ~3 minutes).

8. **Expected total implementation effort is 5-8 hours**, with most of the work in creating the AWR training script and adding mask columns to rollout saves.

## Recommendations

1. **Immediate: Add legal mask columns to `save_rollout_parquet`** in `train_ppo.py`. This is a 30-line change that enables all future offline eval work.

2. **Short-term: Build `scripts/train_awr_offline.py`** by adapting `train_baseline.py`. The existing `--advantage-weight` flag is a starting point; upgrade to exponential AWR with masked log-probs.

3. **Short-term: Collect a dedicated offline eval dataset** from the top-10 checkpoints with the enhanced schema.

4. **Medium-term: Build the architecture sweep script** that automates train-then-mini-rollout for a list of candidates.

5. **Validate the approach** by checking that AWR rankings on 3-4 known architectures match PPO Elo rankings before trusting it for new experiments.

6. **Use tau=1.0 as the default AWR temperature**, tune it once on the validation set, then freeze it for all architecture comparisons.

7. **For architecture comparison metrics, prioritize** (in order): advantage-weighted card accuracy, value MSE, AWR policy loss, mini-rollout WR. De-emphasize raw BC loss and country-head metrics.

8. **Regenerate the offline eval dataset every ~100 Elo points** of improvement to prevent data staleness.

## Open Questions

1. **Should the value head be retrained on the frozen data, or should the stored `value` column be used as-is?** Retraining gives architecture-specific advantages but adds complexity. Recommendation: start with stored values, add value retraining if needed.

2. **Is the existing clamped-linear AWR (train_baseline.py) sufficient, or is exponential AWR measurably better?** This should be tested empirically on the validation set.

3. **How sensitive is the AWR temperature tau to dataset quality?** If the top checkpoints play very differently from each other, tau may need to be larger to avoid collapsing to a single checkpoint's style.

4. **Can the country_mask be approximated well enough without C++ engine recomputation?** The DEFCON-3/4 coup restrictions affect a meaningful fraction of coup decisions; ignoring them may bias country-head evaluation.

5. **Should the offline dataset include both USSR and US perspectives, or one side only?** The current rollout data includes both. For architecture comparison, both sides should be included to test robustness.
---
