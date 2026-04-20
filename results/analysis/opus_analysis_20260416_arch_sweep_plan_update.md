---
# Opus Analysis: Updated Architecture Sweep Plan
Date: 2026-04-16
Question: Given the off-policy ranking analysis, what is the updated architecture sweep plan?

## Executive Summary

The AWR architecture sweep infrastructure is built and data collection is actively running (4/7 models complete, ~880K rows expected from 7 models x 2100 games vs heuristic, with 21 round-robin pairs x 300 games to follow). The off-policy ranking analysis identified three concrete improvements to make before running the sweep: (1) fix macro-action weighting by averaging country log-probs instead of summing them, (2) add intermediate reward shaping (VP deltas) to GAE computation for better early-game advantage signal, and (3) add a tau sweep and uniform BC baseline to calibrate how much advantage weighting helps. The 12 architectures in MODEL_REGISTRY should be narrowed to 6-7 high-value candidates for the initial sweep, prioritizing the architectures that differ on the dimensions most likely to matter for play strength: country encoder type (flat vs GNN vs attention), side-conditioning (shared vs per-side heads), and country head structure (mixture-of-softmaxes vs direct vs marginal-value).

## Findings

### 1. Current State of the Pipeline

**Data collection (running now):**
- 7 source models: v56, v54, v44, v20, v55, ppo_ussr_only_v5, ppo_us_only_v5
- 2100 games per model vs heuristic (14,700 total games)
- ~880K expected rows (60 steps/game average)
- Models 1-3 complete (v56: 126K rows, v54: 127K rows, v44: 127K rows), model 4 (v20) in progress
- Round-robin phase follows: 21 pairs x 300 games = 6,300 more games
- Output: `data/awr_eval/awr_panel_v5.parquet`
- Estimated total: ~1.26M rows (880K heuristic + 378K round-robin)

**Scripts built:**
- `scripts/collect_awr_data.py` — multi-model rollout collection with GAE, supports vs-heuristic and model-vs-model modes
- `scripts/train_awr.py` — AWR training loop with advantage-weighted NLL, per-turn-bucket evaluation, 5/6-mode compatibility
- `scripts/arch_sweep_awr.py` — sweep harness that trains N architectures on the same frozen data and ranks by val_adv_card_acc

**What works well:**
- Frozen dataset ensures fair comparison across architectures
- GAE computation is per-side, per-game with correct boundary handling
- 5-mode vs 6-mode mask padding handles checkpoint compatibility
- Per-turn-bucket metrics (early/mid/late) provide useful stratification
- Advantage-weighted card accuracy as primary ranking metric is sound

### 2. Pre-Sweep Fixes Required (from off-policy analysis)

#### Fix 1: Macro-action weighting (CRITICAL, 2-line change)

In `train_awr.py`, line 182, country log-probs are summed over multi-point allocations:
```python
country_log_prob = country_log_prob + lp_t * active.float()
```

This gives a 4-ops placement 4x the loss contribution of a card choice, biasing architecture ranking toward placement accuracy. The fix is to divide by `max(country_lengths, 1)` after the loop:

```python
country_log_prob = country_log_prob / country_lengths.clamp(min=1).float()
```

This implements the document's recommended formula: `L_macro = -w(s,a) * (1/K) * sum_i log pi(t_i | s, t_{<i})`.

**Impact:** Without this fix, architectures that handle single-point decisions better will score higher than ones that handle placement bundles better, regardless of actual play strength. This directly corrupts the ranking signal.

#### Fix 2: Intermediate reward shaping in GAE (HIGH VALUE, moderate effort)

Current GAE uses terminal reward only (+/- 1.0, -1.2 for DEFCON-1 loss). With ~60 steps per game and gamma=0.99, lambda=0.95, early-game advantages are dominated by noise.

The collected parquet already stores per-step `vp` values. A VP-delta reward shaping term can be added during GAE computation:

```
r_shaped(t) = alpha * (vp[t+1] - vp[t]) + r_terminal(t)
```

where alpha is a small coefficient (e.g., 0.02-0.05) that scales VP swings relative to terminal reward. This gives GAE local signal without requiring MCTS teacher data.

**Implementation:** Either recompute GAE from stored parquet data (post-hoc, no re-collection needed since vp is stored), or add it to `compute_gae_arrays` in collect_awr_data.py for future collections.

**Impact:** Addresses the off-policy document's core concern about delayed returns. Early-game decisions currently receive near-uniform advantage weights, which dilutes the architecture ranking signal for the most strategically important decisions.

#### Fix 3: Advantage normalization per source model (MEDIUM VALUE, easy)

Mixing data from v20 (weak) and v56 (strong) means advantage scales differ because value heads have different quality. Advantages from weaker models may have higher variance, dominating the weighting.

**Fix:** After loading the parquet, normalize advantages per `model_name` column to zero mean and unit variance before training.

### 3. Architectures to Compare

MODEL_REGISTRY contains 12 architectures. For a tractable sweep, these should be grouped by the dimensions they vary on:

| Architecture | Country Encoder | Card Encoder | Side Conditioning | Country Head | Notable |
|---|---|---|---|---|---|
| `baseline` | Flat Linear | Flat Linear | None | K=4 MoS | Reference |
| `card_embed` | Flat Linear | DeepSet+Flat | None | K=4 MoS | Card inductive bias |
| `country_embed` | Embed+Flat | Flat Linear | None | K=4 MoS | Country inductive bias |
| `full_embed` | Embed+Flat | DeepSet+Flat | None | K=4 MoS | Both embeddings |
| `direct_country` | Flat Linear | Flat Linear | None | Direct Linear | Simplest country head |
| `marginal_value` | Flat Linear | Flat Linear | None | Marginal (B,86,4) | Per-threshold country |
| `control_feat` | ControlFeat+Flat | Flat Linear | None | K=4 MoS | Region scoring scalars |
| `control_feat_gnn` | GNN+Flat | Flat Linear | None | K=4 MoS | 2-hop graph conv |
| `control_feat_gnn_side` | GNN+Flat | Flat Linear | Side embed + per-side V | K=4 MoS | GNN + side heads |
| `country_attn` | Attn+Flat | DeepSet+Flat | None | K=4 MoS | Self-attention countries |
| `country_attn_side` | Attn+Flat | Flat Linear | Side embed + per-side V | K=4 MoS | Attn + side heads |
| `country_attn_side_policy` | Attn+Flat | Flat Linear | Side embed + per-side ALL | K=4 MoS | Attn + per-side policy |

**Recommended sweep set (7 architectures):**

1. **`baseline`** — the floor; all other architectures must beat this
2. **`control_feat_gnn_side`** — current production architecture (GNN + side), the reference "best known"
3. **`country_attn_side`** — the main challenger (attention vs GNN, matched features)
4. **`country_attn_side_policy`** — tests whether per-side policy heads add value over shared policy + per-side value
5. **`direct_country`** — tests whether K=4 mixture-of-softmaxes is necessary vs a single linear country head
6. **`control_feat`** — tests whether region scoring scalars help without GNN or side conditioning
7. **`full_embed`** — tests whether both card and country embeddings help without attention/GNN

**Architectures to skip in initial sweep:**
- `card_embed`, `country_embed` — subsumed by `full_embed` and attention/GNN variants
- `country_attn` — subsumed by `country_attn_side` (same encoder + side conditioning)
- `control_feat_gnn` — subsumed by `control_feat_gnn_side` (same encoder + side conditioning)
- `marginal_value` — interesting but requires different loss code (per-threshold BCE), not compatible with current train_awr.py without modifications

### 4. Sweep Configuration

**Hyperparameter grid:**
- Hidden dims: [256] (fixed for initial sweep, vary later for top candidates)
- Tau (AWR temperature): [0.5, 1.0, 2.0, 1e6] where 1e6 approximates uniform BC
- Epochs: 5 (fast convergence observed in prior tests)
- LR: 3e-4 (AdamW with weight decay 1e-4)
- Batch size: 2048
- Seeds: [42, 43, 44] (3 seeds per config for error bars)

**Total experiments:** 7 archs x 4 taus x 3 seeds = 84 runs at ~2-5 min each = 3-7 hours on GPU.

**Ranking metrics (in priority order):**
1. `val_adv_card_acc` — advantage-weighted card accuracy (primary)
2. `val_card_acc` — unweighted card accuracy (secondary, correlates with BC quality)
3. `val_policy_loss` — advantage-weighted NLL (lower is better)
4. `val_card_acc_late` — late-game card accuracy (most strategically relevant)
5. `val_value_loss` — value head quality (secondary signal)

### 5. Extended Experiments (after initial sweep)

**CRR-lite mode (add after initial sweep):**
Add a `--crr-filter` flag to train_awr.py that drops examples with advantage < 0 (or keeps only top 50% per decision). This tests whether filtering out mediocre moves improves architecture discrimination. Implementation: ~10 lines in train_epoch and eval_epoch.

**Hidden dim sweep for top-2 candidates:**
After identifying the top-2 architectures by val_adv_card_acc, run those with hidden_dims [128, 256, 384] to find the capacity sweet spot.

**Mini-rollout validation (calibration step):**
For the top-2 candidates from the AWR sweep, train a full checkpoint and run 200-400 games vs heuristic per side. Compare AWR rank order with actual win rate rank order. If they agree, the AWR proxy is validated. If they disagree, investigate why.

### 6. Priority-Ordered Action Plan

**Phase 0: Pre-sweep fixes (do before any sweep runs)**
1. Fix macro-action weighting in train_awr.py (2-line change)
2. Add per-model advantage normalization to AWRDataset (add during __init__)
3. Add tau parameter to arch_sweep_awr.py sweep grid
4. Add BC baseline mode (tau=1e6 or a --bc flag)

**Phase 1: Initial sweep (after data collection completes)**
1. Wait for awr_panel_v5.parquet collection to finish (~3-4 more hours for remaining models + round-robin)
2. Run 7-architecture sweep with tau in {0.5, 1.0, 2.0, 1e6}, 3 seeds each
3. Analyze results: rank architectures, check tau sensitivity, identify clear winners/losers
4. Drop architectures that are clearly dominated (>2pp below best on val_adv_card_acc across all taus)

**Phase 2: Refinements (after Phase 1 results)**
1. Add intermediate reward shaping and recompute advantages (can be done post-hoc from stored vp column)
2. Re-run sweep for top-3 candidates with shaped advantages
3. Add CRR-lite filtering and test on top-3 candidates
4. Compare CRR-lite vs AWR-lite rankings for robustness

**Phase 3: Validation (after Phase 2 results)**
1. Select top-2 architectures
2. Train PPO checkpoints for each (5 iterations, sufficient for signal)
3. Benchmark 2000 games/side vs heuristic
4. Compare AWR rank order with PPO win rate rank order
5. If agreement: AWR proxy validated, adopt winning architecture
6. If disagreement: investigate which AWR metric best predicts PPO strength

### 7. What NOT to Do

- Do NOT add IQL-lite or AWAC implementations. The data is high-quality (from best models), so heavier offline RL methods add complexity without likely benefit.
- Do NOT attempt teacher/MCTS data collection for the sweep. The MCTS infrastructure change is valuable long-term but would delay the sweep by days. Use reward-shaped GAE instead.
- Do NOT run all 12 architectures. The 5 excluded architectures are either subsumed by included ones or require different loss code.
- Do NOT spend time on per-decision-type stratification yet. Per-turn-bucket (early/mid/late) is sufficient for Phase 1.
- Do NOT vary hidden_dim in the initial sweep. Fix it at 256 to isolate architecture effects.

## Conclusions

1. The AWR sweep pipeline is ready to run modulo three concrete fixes: macro-action weighting (sum->average), per-model advantage normalization, and tau sweep support in the sweep harness.

2. The macro-action weighting bug is the most important fix. Without it, architectures are ranked partly on how well they handle multi-point vs single-point decisions, which is an artifact of the loss weighting, not a reflection of play strength.

3. Seven architectures from MODEL_REGISTRY should be included in the initial sweep: baseline, control_feat_gnn_side, country_attn_side, country_attn_side_policy, direct_country, control_feat, and full_embed. These cover the key variation axes (country encoder, side conditioning, country head structure) without redundancy.

4. The tau sweep (0.5, 1.0, 2.0, 1e6) serves double duty: it calibrates how much advantage weighting helps rank architectures, and tau=1e6 provides a pure BC baseline that validates whether AWR adds signal beyond supervised imitation.

5. Intermediate reward shaping using VP deltas (already stored in parquet) is the highest-value improvement to the advantage signal that does not require new infrastructure. It should be tested in Phase 2 after the initial sweep establishes baseline rankings.

6. The sweep should take 3-7 GPU-hours total (84 experiments at 2-5 min each) once data collection completes. This is 10-50x cheaper than equivalent PPO-based architecture comparison.

7. A mini-rollout validation step (200-400 games for top-2 candidates) is essential to confirm that AWR ranking correlates with actual play strength before committing to an architecture choice.

## Recommendations

1. **Implement the three pre-sweep fixes now** (macro-action weighting, per-model advantage normalization, tau sweep grid). These are small changes that directly improve ranking quality.

2. **Run the 7-architecture, 4-tau, 3-seed sweep** as soon as data collection completes. Target ~84 runs, ~4 hours GPU time.

3. **Use val_adv_card_acc as the primary ranking metric**, with val_card_acc_late as a tiebreaker. Policy loss is useful but less interpretable.

4. **Add reward-shaped GAE in Phase 2**, recomputing advantages from stored vp column. Test alpha in {0.02, 0.05, 0.1} and compare ranking stability vs unshapen advantages.

5. **Validate top-2 candidates with mini-rollout** (200 games/side vs heuristic) before adopting the winning architecture for the PPO chain.

6. **Plan teacher data collection as a separate workstream.** Logging MCTS visit counts during future data collection would upgrade the advantage source from GAE to teacher-local, which is the off-policy document's strongest recommendation. This is a C++ API extension and should not block the current sweep.

## Open Questions

1. **How noisy is GAE-based AWR ranking for TS?** The tau sweep partially answers this: if rankings are stable across tau values, GAE is good enough. If rankings flip between tau=0.5 and tau=2.0, the advantage signal is too noisy and reward shaping or teacher advantages become urgent.

2. **Is the round-robin data useful for architecture ranking?** Model-vs-model games may have different advantage distributions than vs-heuristic games. Should the sweep use only vs-heuristic data, only round-robin data, or both? A quick test: run the sweep on each subset and compare rankings.

3. **Does marginal_value deserve its own loss code?** The per-threshold BCE approach is architecturally interesting but incompatible with the current train_awr.py. Worth adding if the initial sweep shows K=4 MoS is consistently worse than direct_country, suggesting the country head structure matters.

4. **What is the right alpha for VP reward shaping?** Too high biases toward tactical VP-grabbing moves; too low provides negligible signal. Empirical sweep needed, but 0.02-0.05 is a reasonable starting range based on typical VP swings (1-4 VP per scoring card vs 20 VP game outcome).

5. **Should the sweep warm-start from a checkpoint or train from scratch?** Warm-starting from a shared checkpoint (e.g., v56) tests "which architecture best fine-tunes from current best." Training from scratch tests "which architecture learns fastest on this data." Both are useful signals, but from-scratch is cleaner for architecture ranking because warm-start quality depends on checkpoint-architecture compatibility.
---
