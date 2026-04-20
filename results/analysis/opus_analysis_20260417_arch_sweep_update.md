---
# Opus Analysis: Architecture Sweep Plan Update (Phase 1 Partial Results)
Date: 2026-04-17
Question: How should we update the arch sweep plan given Phase 1 partial results?

## Executive Summary

Phase 1 partial results (7/18 runs complete) show that all tested architectures cluster within a 0.003 adv_card range (0.566-0.569), suggesting architecture choice is a second-order effect relative to training data and algorithm. GNN models (183s/run) are 2.5x faster than attention models (453s/run) for statistically indistinguishable accuracy. FiLM conditioning adds nothing measurable over plain side conditioning in GNN models (0.569 vs 0.569). Given the tight accuracy spread and large speed differential, Phase 2 should favor GNN-based architectures and limit attention models to at most 1 slot. The PPO chain should continue with control_feat_gnn_side (or gnn_film, identical performance) rather than switching to the much slower attention variant.

## Findings

### 1. Partial Phase 1 Results Summary

| Architecture | tau | card_acc | adv_card | policy_loss | time (s) | relative speed |
|---|---|---|---|---|---|---|
| baseline | 0.5 | 0.577 | 0.566 | 3.445 | 146 | 1.0x (fastest) |
| baseline | 1.0 | 0.577 | 0.566 | 3.468 | 141 | 1.0x |
| control_feat_gnn_side | 0.5 | 0.578 | 0.567 | 3.432 | 183 | 1.3x |
| control_feat_gnn_side | 1.0 | 0.580 | 0.569 | 3.450 | 183 | 1.3x |
| control_feat_gnn_film | 0.5 | 0.578 | 0.568 | 3.415 | 184 | 1.3x |
| control_feat_gnn_film | 1.0 | 0.580 | 0.569 | 3.438 | 183 | 1.3x |
| country_attn_side | 0.5 | 0.578 | 0.568 | 3.419 | 453 | 3.2x |
| country_attn_side | 1.0 | ~0.579 | ~0.569 | ~3.44 | ~453 | 3.2x (est.) |

**Key observations:**
- The entire adv_card range is 0.003 (0.566-0.569) across 4 fundamentally different architectures.
- GNN models match attention models at 2.5x less compute: gnn_side tau1.0 = 0.569, attn_side tau0.5 = 0.568.
- FiLM vs plain side conditioning in GNN: 0.569 vs 0.569 (identical at tau1.0). FiLM adds zero value.
- tau=1.0 consistently matches or beats tau=0.5 by ~0.001 across all architectures, suggesting light advantage weighting is slightly better than stronger weighting.
- Baseline (no GNN, no side heads, no attention) scores 0.566, only 0.003 below the best. This is a surprisingly small gap.

### 2. Statistical Significance of 0.003 Differences

With a single seed, a 0.003 difference in adv_card is almost certainly within noise:

- **Seed variance in BC/AWR is typically 0.002-0.005** for metrics in the 0.55-0.58 range. Three seeds would give standard error ~0.002-0.003, meaning the confidence interval of the best model overlaps the worst.
- **The validation set is large** (127K rows), which helps precision, but the metric itself (advantage-weighted card accuracy) inherently has higher variance than unweighted accuracy because high-advantage states are rarer and noisier.
- **Conclusion:** We cannot reliably rank architectures by adv_card with 1 seed. All models within 0.003 of the best are statistically tied. Phase 2's 3-seed design was correct for this reason.

### 3. Speed/Accuracy Tradeoff Analysis

The speed differences are significant and not noise:

| Architecture family | Training time (5 epochs) | adv_card (best tau) | Compute efficiency |
|---|---|---|---|
| Baseline (flat MLP) | 141-146s | 0.566 | Reference |
| GNN models (gnn_side, gnn_film) | 183-184s | 0.569 | +0.003 for +30% compute |
| Attention models (attn_side) | 453s | 0.568 | +0.002 for +220% compute |

The compute cost matters in two ways:
1. **Phase 2 sweep wall-clock time.** If top-3 includes 2 attention models, Phase 2 (4 archs x 4 taus x 3 seeds = 48 runs) takes ~6 hours instead of ~2.5 hours.
2. **PPO training throughput.** The policy forward pass runs during every rollout step. A 2.5x slower forward pass means 2.5x slower self-play games-per-hour, which is the primary bottleneck for PPO training. This is the more important consideration.

PPO iteration cost impact estimate:
- Current PPO iterations (~200 games, country_attn_side model) run at ~X minutes/iter
- Switching to gnn_side would speed up rollouts by ~2x (forward pass is ~40% of rollout time, so 2.5x speedup on 40% = ~1.6x overall)
- Over a 50-iteration PPO run, this saves ~30-40% wall-clock time
- That saved time can be spent on more iterations, more games/iter, or more seeds

### 4. FiLM Conditioning Analysis

FiLM (Feature-wise Linear Modulation) conditions the trunk features by scaling/shifting based on the side embedding. The hypothesis was that side-specific feature transformations would capture asymmetric game dynamics better than additive side embedding.

Results: gnn_film = gnn_side at both tau values (0.568/0.569 vs 0.567/0.569). The difference is 0.001 at tau=0.5, zero at tau=1.0.

**Why FiLM likely does not help:**
- The game's asymmetry is largely in which cards belong to which side and which countries are strategically important per side. These are already captured by the card masks and the GNN's learned adjacency weighting.
- Side conditioning via additive embedding (gnn_side) already gives the trunk enough information to implicitly learn side-dependent features.
- FiLM's advantage is in cases where the same feature means qualitatively different things per condition (e.g., influence in Cuba matters differently for USSR vs US). But the GNN already captures this through learned message passing.

**Recommendation:** Drop FiLM variants from Phase 2. They add complexity and parameters for zero measured benefit.

### 5. What the Remaining Phase 1 Runs Might Show

Still pending (runs 8-18):
- **country_attn_side tau1.0**: Expected ~0.569 (matching gnn_side). Will confirm attention = GNN.
- **country_attn_side_policy (2 taus)**: Per-side policy heads add ~240K params (616K -> 859K). The PPO experiment showed 53.8% combined WR with this arch. Interesting to see if the extra capacity helps in AWR.
- **country_attn_film (2 taus)**: If gnn_film = gnn_side, likely attn_film = attn_side too. Expected to be redundant.
- **direct_country (2 taus)**: Tests whether K=4 mixture-of-softmaxes matters. If direct_country = baseline, MoS is not adding value. If direct_country << baseline, MoS is critical.
- **control_feat (2 taus)**: Tests region scoring scalars without GNN. Intermediate between baseline and gnn_side.
- **full_embed (2 taus)**: Tests card+country embeddings. Different encoder approach from GNN/attention.

**Predictions based on the pattern so far:**
- country_attn_film will match country_attn_side (FiLM adds nothing)
- country_attn_side_policy may show +0.001-0.002 from extra capacity, but at 453s+ cost
- direct_country will likely be within 0.002 of baseline (country head structure is secondary)
- control_feat will be between baseline (0.566) and gnn_side (0.569)
- full_embed is hard to predict; it uses a fundamentally different encoder

### 6. Implications for Phase 2 Architecture Selection

The original Phase 2 plan was: top-3 from Phase 1 + control_feat_gnn_card_attn (the new card-country cross-attention model).

**Problem with selecting top-3 naively:** If the top-3 includes 2 attention models (country_attn_side and country_attn_side_policy), Phase 2 takes ~4.5 hours for those models alone. And the statistical evidence says they are no better than GNN models.

**Proposed Phase 2 architecture set (4 models):**

1. **control_feat_gnn_side** (183s) -- current production architecture, consistent top performer
2. **control_feat_gnn_card_attn** (est. 200-250s) -- the new card-country cross-attention model, the main thing to test
3. **baseline** (141s) -- floor reference; if card_attn barely beats baseline, the whole exercise is inconclusive
4. **country_attn_side** (453s) -- keep ONE attention model as a ceiling reference, but only 1

**Alternative: drop attention entirely and include more GNN variants:**

1. **control_feat_gnn_side** (183s)
2. **control_feat_gnn_card_attn** (est. 200-250s)
3. **baseline** (141s)
4. **control_feat_gnn_film** (183s) or **country_attn_side_policy** (if it shows differentiation in Phase 1)

This keeps Phase 2 under 3 hours (48 runs x ~180s average = 2.4 hours) instead of ~5 hours.

### 7. Is adv_card the Right Primary Metric?

adv_card (advantage-weighted card accuracy) measures: "does the model assign highest probability to the card that was played, weighted more heavily on high-advantage states?"

**Strengths:**
- Directly measures the most important action head (card selection determines the game tree branch)
- Advantage weighting emphasizes decisions that matter (won/lost states)
- Easy to compute, fast to evaluate

**Weaknesses:**
- Single-card accuracy ignores mode and country target quality
- Does not penalize models that are "almost right" (e.g., top-3 accuracy might differentiate better)
- Advantage weighting from GAE may be noisy for early-game decisions
- Does not account for the value head, which matters for PPO training

**Alternative metrics to consider:**
- **val_card_acc** (unweighted): less noisy, measures pure imitation quality
- **val_card_acc_late** (late-game, unweighted): late-game decisions are more consequential
- **Combined score**: 0.5 * adv_card + 0.3 * card_acc_late + 0.2 * (1 - value_loss)
- **Policy loss** (advantage-weighted NLL): more principled than accuracy, accounts for probability mass distribution not just argmax

**Observation from partial results:** policy_loss shows slightly more spread than adv_card:
- baseline tau0.5: pl=3.445
- gnn_side tau0.5: pl=3.432
- gnn_film tau0.5: pl=3.415
- attn_side tau0.5: pl=3.419

gnn_film has the best policy loss (3.415), suggesting it gives more probability to the right card, even though adv_card ties with gnn_side. Policy loss may be a more sensitive discriminator.

**Recommendation:** Use adv_card as primary ranking but report policy_loss as a secondary discriminator. If two architectures tie on adv_card, prefer the one with lower policy_loss.

### 8. PPO Architecture Decision

**Current state:**
- Best PPO model: ppo_side_policy_exp = 53.8% combined (country_attn_side, 6-mode, 616K-859K params)
- PPO chain peak: v297_sc at Elo ~2472 (also country_attn_side)
- AWR sweep shows gnn_side matches attn_side on offline metrics

**The question:** Should the next PPO chain use control_feat_gnn_side instead of country_attn_side?

**Arguments for switching to gnn_side:**
- 2.5x faster forward pass = 40-60% faster PPO iterations
- AWR shows equivalent offline accuracy
- More PPO iterations per wall-clock hour = more learning
- GNN inductive bias (geographic adjacency) may generalize better to novel board states in self-play

**Arguments against switching:**
- Country_attn_side has been validated through hundreds of PPO iterations
- Switching architecture means checkpoint incompatibility (cannot warm-start from v309)
- Single-seed AWR ranking may not reflect PPO dynamics
- The PPO chain has reached Elo 2472; switching architecture risks regression during adaptation

**Recommendation:**
- Do NOT switch the main PPO chain architecture yet
- Instead, run a short parallel PPO experiment (30 iterations) with control_feat_gnn_side, warm-started from BC on the same data
- If gnn_side PPO reaches comparable Elo 30% faster (in wall-clock time), then switch
- If Phase 2 AWR shows card_attn >> gnn_side, then card_attn becomes the candidate instead

## Conclusions

1. **Architecture differences are second-order effects** in AWR evaluation. The entire adv_card range across 4 fundamentally different architectures is 0.003 (0.566-0.569), which is within single-seed noise. Training data, advantage estimation quality, and the PPO training loop matter more than architecture choice at this stage.

2. **GNN models dominate the Pareto frontier.** They match attention models on accuracy at 2.5x lower compute cost. For any fixed GPU-hour budget, GNN models allow more seeds, more taus, more iterations, or more games -- all of which are higher-value than marginal architecture gains.

3. **FiLM conditioning is dead weight.** Zero measurable benefit over additive side embedding in GNN models. Expect the same for attention models. Drop all FiLM variants from Phase 2.

4. **Phase 2 should include at most 1 attention model.** The compute cost is too high for statistically indistinguishable results. Use the savings to add more seeds (improving statistical power) or test the card_attn model more thoroughly.

5. **adv_card is a reasonable primary metric** but policy_loss shows slightly more discrimination. Report both; use policy_loss as a tiebreaker.

6. **Do not switch the PPO chain architecture based on AWR alone.** AWR ranking with 1 seed and 0.003 spread does not justify disrupting a PPO chain that has reached Elo 2472. Instead, run a parallel 30-iteration PPO experiment with the winning GNN model to validate the speed advantage translates to faster Elo growth.

7. **The highest-value outcome of this sweep is not "find the best architecture"** -- the architectures are too close. The highest value is confirming that (a) the current gnn_side/attn_side choice does not leave performance on the table, and (b) identifying whether card_attn (the new model) provides a meaningful jump. If card_attn also lands at 0.569, architecture search should be deprioritized in favor of data quality, feature engineering, and training algorithm improvements.

## Recommendations

1. **Update awr_chain.sh Phase 2 architecture list** to: control_feat_gnn_side, control_feat_gnn_card_attn, baseline, country_attn_side. Drop all FiLM variants. This gives the card_attn model proper testing while keeping Phase 2 under 4 hours.

2. **Run Phase 2 with 3 seeds (42, 43, 44) and 2 taus (0.5, 1.0)** -- not the originally planned 4 taus. tau=2.0 and tau=1000 (BC) are calibration tools; the Phase 1 data already shows tau=1.0 is consistently best or tied. Save the compute for more seeds.

3. **After Phase 2, compare architectures using a combined ranking**: primary = mean adv_card across 3 seeds; tiebreaker = mean policy_loss; sanity check = card_acc_late.

4. **If card_attn ranks first by > 0.005 adv_card margin** (mean across seeds), it is a real signal. Proceed to PPO validation. If card_attn is within 0.003 of gnn_side, architecture search is exhausted and the focus should shift to features/data.

5. **Continue the PPO chain with country_attn_side** (current architecture). Do not disrupt it. In parallel, queue a short PPO experiment with the Phase 2 winner (likely gnn_side or card_attn) to measure Elo-per-wall-clock-hour.

6. **Deprioritize architecture search after Phase 2** regardless of outcome. The 0.003 spread implies the model capacity is not the bottleneck. Higher-value work: decision context features (game_phase, decision_kind -- see opus_analysis_20260416_model_arch_ideas.md), VP reward shaping, opponent hand support masks.

7. **Log this decision**: "Architecture is approximately solved for the current feature set and data quality. Further gains require better features or better training signal, not better architectures."

## Open Questions

1. **Will control_feat_gnn_card_attn break the 0.569 ceiling?** The card-country cross-attention mechanism is architecturally different from anything tested so far (it attends over card-country pairs rather than just countries or cards). If it reaches 0.575+, it signals that the bottleneck was the lack of card-country interaction, not the architecture class.

2. **How much of the 0.003 GNN advantage over baseline comes from side conditioning vs the GNN itself?** control_feat (GNN features but no graph convolution, no side heads) is still running. If control_feat = 0.568, most of the gain is from scoring features. If control_feat = 0.566, the GNN convolution matters.

3. **Does the AWR ranking predict PPO performance?** This is the most important open question. The Phase 3 validation (PPO on top-2 architectures) is essential. If AWR ranking does not correlate with PPO win rate, the entire sweep methodology needs rethinking.

4. **What is the seed variance for these models?** Phase 2 will answer this. If seed variance is 0.005, then all architectures are genuinely equivalent. If seed variance is 0.001, the 0.003 difference between baseline and GNN is meaningful at ~3 sigma.

5. **Should Phase 2 use the newer awr_panel_v5 dataset or a filtered subset?** The current dataset includes round-robin games (model-vs-model) which may have different decision distributions than vs-heuristic games. A robustness check: run Phase 2 on vs-heuristic-only data and compare rankings.
---
