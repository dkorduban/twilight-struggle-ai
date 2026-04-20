---
# Opus Analysis: Off-Policy Architecture Ranking Review
Date: 2026-04-16
Question: What do you think about long-prompts/off-policy-architecture-ranking.md?

## Executive Summary

The document provides methodologically sound advice for using AWR-style weighted imitation as an architecture ranking proxy, and its core recommendation -- frozen dataset + fixed advantage weights + weighted NLL -- is well-matched to this project's needs. The existing implementation (collect_awr_data.py, train_awr.py, arch_sweep_awr.py) already follows the document's recommended approach at tiers 1-3, but uses GAE-based advantages from model value heads rather than the document's preferred teacher/search-derived advantages. This is the single largest gap: the document's strongest recommendation -- use teacher-local advantages rather than episode-return-based weights -- is exactly right for TS, yet the current pipeline has no mechanism to collect or use teacher signals. The five-tier ladder (BC -> distillation -> AWR-lite -> CRR-lite -> IQL-lite) is pragmatic and correctly ordered, though tiers 4-5 are unlikely to be needed given this project's data quality.

## Findings

### 1. Methodology Assessment: Sound Core, Reasonable Caveats

The document correctly identifies the central tension: TS has delayed rewards that make raw return-based weighting noisy, but there is plenty of local/medium-horizon signal (VP swings, DEFCON tempo, regional position) that can be captured with better advantage estimates. The recommendation to avoid raw Monte Carlo returns as AWR weights is correct and important.

The five-tier ladder is well-structured:
- **Tier 1 (Uniform BC)** -- already implicitly available as tau -> infinity in train_awr.py
- **Tier 2 (Teacher distillation)** -- not implemented; would require logging MCTS visit counts during data collection
- **Tier 3 (AWR-lite with local advantages)** -- this is what the current pipeline implements, but using GAE rather than teacher-derived advantages
- **Tier 4 (CRR-lite)** -- straightforward to add as a filtering step; likely unnecessary given data quality
- **Tier 5 (IQL-lite)** -- correctly identified as too heavy for architecture ranking; the critic-architecture interaction confound is real

The document's ranking of methods (AWR > CRR > IQL > AWAC > CQL for this use case) is defensible. The reasoning that heavier offline RL methods introduce more confounds for architecture ranking -- because you are partly measuring critic quality rather than policy trunk quality -- is correct.

### 2. Gap Analysis: What the Document Recommends vs What's Built

**What's already implemented well:**
- Frozen dataset collection from multiple checkpoints (collect_awr_data.py)
- GAE computation with per-side, per-game boundaries
- AWR training loop with exponential advantage weighting and clipping (train_awr.py)
- Architecture sweep harness with cross-architecture comparison (arch_sweep_awr.py)
- Per-turn-bucket validation metrics (early/mid/late)
- Advantage-weighted card accuracy as the primary ranking metric
- Round-robin model-vs-model data collection mode

**What's missing, ordered by impact:**

1. **Teacher/search-derived advantages (HIGH IMPACT)**. The document's strongest recommendation is to use teacher Q-values, visit counts, or teacher logits as the advantage source rather than GAE from a model's own value head. The current pipeline computes GAE from the rollout model's value predictions, which means:
   - Advantages reflect the quality of each model's value head, not an objective quality signal
   - When collecting from multiple checkpoints of varying quality, the advantage scale and meaning varies
   - The advantage is essentially model-return-based, exactly what the document warns against

   To fix this: the C++ rollout infrastructure would need to optionally run MCTS at each decision point and log visit counts. This is expensive but the document correctly notes that even a few hundred MCTS simulations per decision would produce much better weights than GAE.

2. **Macro-action weighting (MEDIUM IMPACT)**. The document recommends computing a single macro weight per composite action (e.g., 4-ops placement) and using average token NLL. The current pipeline sums log-probs over country targets (line 176-183 of train_awr.py), which gives multi-point placements more weight in the loss. This is a subtle but real bias -- architectures that happen to handle single-point decisions better may score higher than ones that handle placement bundles better, without the ranking reflecting play strength.

3. **Teacher top-k agreement metrics (LOW-MEDIUM IMPACT)**. The document recommends evaluating not just top-1 accuracy but also top-k teacher mass captured and KL to teacher distribution. The current pipeline only tracks top-1 card/mode accuracy and advantage-weighted accuracy. Adding KL-to-teacher or top-3 agreement would give richer ranking signal, but requires teacher distributions to be available.

4. **Decision-type-stratified evaluation (LOW IMPACT)**. The document hints at per-decision-type analysis (headline, coup target, placement, etc.). The current pipeline only stratifies by turn bucket (early/mid/late). Adding decision-type stratification would help identify architectures that excel at specific decision types, which is useful for targeted improvements.

5. **Online audit calibration (LOW IMPACT)**. The document recommends "periodically audit only the top few architectures with small online self-play." The current pipeline does not include this step, but it is straightforward -- run 200-400 games for the top-2 architectures from the sweep and compare win rates.

### 3. Quality of the Advantage Signal in the Current Pipeline

The current pipeline uses GAE with gamma=0.99, lambda=0.95 and terminal game reward (+/- 1.0, or -1.2 for DEFCON-1 losses). This is essentially a bootstrapped return estimate using the rollout model's own value predictions.

Strengths:
- GAE is a well-understood estimator
- Per-side, per-game computation is correct
- The DEFCON-1 penalty (-1.2 vs -1.0) adds some domain-specific signal

Weaknesses:
- The value head quality varies across the source checkpoints (v56 through v309+)
- Terminal reward only (no intermediate reward shaping), so early-game advantages are noisy
- Lambda=0.95 with ~60 steps per game means significant credit smearing for early decisions
- When mixing data from multiple generator strengths, advantage scales are not comparable

The document's concern about delayed returns is directly applicable here. A practical improvement without full MCTS teacher data: add **intermediate reward shaping** based on VP changes, scoring card outcomes, or DEFCON events. This would give GAE much more local signal to work with, addressing the document's core concern at low implementation cost.

### 4. What's Actionable vs Speculative

**Immediately actionable (no new infrastructure):**
- Add tau sweep to arch_sweep_awr.py (test tau=0.5, 1.0, 2.0, 5.0)
- Add uniform BC baseline (tau -> infinity or a --bc-only flag)
- Normalize advantages per-model-source before combining multi-model datasets
- Add macro-action weighting: divide country_log_prob by max(country_lengths, 1)
- Add CRR-lite mode: binary filter on advantage > 0 (or top-q% per decision type)
- Add intermediate reward shaping to GAE computation (VP delta, scoring events)

**Actionable with moderate effort:**
- Log MCTS visit counts during data collection (requires C++ rollout API extension)
- Add teacher KL / top-k metrics to eval_epoch
- Add decision-type column to parquet and stratify evaluation
- Add mini-rollout validation step to arch_sweep_awr.py (top-N candidates -> 200 games)

**Speculative / unlikely to be needed:**
- IQL-lite implementation (tier 5) -- data quality is high enough that this adds complexity without likely benefit
- AWAC / CQL -- wrong tools for this use case, as the document correctly notes
- Bootstrap FQE for offline policy evaluation -- interesting theoretically but fragile in practice

### 5. Comparison to Prior Analysis (opus_analysis_20260417_054500)

The prior analysis reached similar conclusions but focused more on practical pipeline gaps (missing masks in rollout parquet). The current document provides a more theoretically grounded framework, especially the five-tier ladder and the emphasis on teacher-derived advantages. The two analyses are complementary:
- Prior analysis: "use AWR with GAE, add mini-rollout validation" (practical)
- Current document: "use AWR but upgrade the advantage source from GAE to teacher-local" (strategic)

Both are correct. The practical path is: start with what's built (GAE-based AWR), add reward shaping for better local signal, and upgrade to teacher-derived advantages when the MCTS data collection infrastructure is ready.

### 6. The Macro-Action Weighting Formula

The document's recommendation (equation in section on what each decision should store) is:

    L_macro = -w(s,a) * (1/K) * sum_i log pi(t_i | s, t_{<i})

This is specifically important for TS because placement actions can have 1-4 country targets, while card/mode choices are single tokens. Without averaging over K, a 4-ops placement contributes 4x the gradient of a card choice, biasing the architecture comparison toward placement accuracy. The current code sums rather than averages:

    country_log_prob = country_log_prob + lp_t * active.float()  (line 183, train_awr.py)

This should be divided by country_lengths (clamped to min 1) before adding to the total log_prob.

## Conclusions

1. The document's core thesis -- AWR-style weighted imitation is the right proxy for architecture ranking on frozen TS data -- is correct and well-supported. The existing pipeline already implements this approach.

2. The single most important gap is the advantage source: the current pipeline uses GAE from rollout model value heads, which the document correctly identifies as a weak signal for TS due to delayed rewards. Teacher/search-derived advantages would be a significant upgrade.

3. The five-tier ladder (BC -> distillation -> AWR-lite -> CRR-lite -> IQL-lite) is well-ordered for this use case. Only tiers 1-3 are likely needed given the project's data quality.

4. The macro-action weighting recommendation is concrete and immediately actionable -- the current code sums rather than averages country target log-probs, which biases architecture comparisons.

5. Adding intermediate reward shaping (VP deltas, scoring events) to the GAE computation is a practical middle-ground improvement that does not require MCTS infrastructure but addresses the document's core concern about delayed returns.

6. The recommendation to avoid online-style off-policy actor-critic methods (IMPALA/APPO/ACER) for this proxy use case is correct and saves the project from a significant complexity trap.

7. CRR-lite (binary advantage filtering) is a useful robustness check that takes ~10 lines to implement and should be added as an option.

## Recommendations

1. **Fix macro-action weighting now.** In train_awr.py, divide country_log_prob by max(country_lengths, 1) before combining with card and mode log-probs. This is a 2-line change that removes a real bias.

2. **Add intermediate reward shaping to collect_awr_data.py.** VP changes between steps, scoring card outcomes, and DEFCON events can provide local reward signal that dramatically improves GAE quality for early-game decisions.

3. **Add tau sweep and BC baseline to arch_sweep_awr.py.** Test tau in {0.5, 1.0, 2.0, 10.0, 1e6} where the last value approximates uniform BC. This calibrates how much the advantage weighting actually helps rank architectures.

4. **Normalize advantages per source model** before combining multi-model datasets. Currently, mixing v56 and v309 data means advantages from weaker models (with worse value heads) may dominate.

5. **Add CRR-lite filtering as an option** in train_awr.py: keep only examples with advantage > 0, or top-q% per decision type. ~10 lines of code, useful robustness check.

6. **Plan for teacher data collection.** The long-term quality ceiling for this pipeline depends on logging MCTS visit counts during data collection. This requires extending the C++ rollout API to optionally run N simulations per decision point and return visit distributions. Not urgent, but the highest-value upgrade path.

7. **Add a mini-rollout validation step** to arch_sweep_awr.py: after the sweep, run 200-400 games for the top-2 candidates to calibrate whether AWR ranking matches actual play strength. This is the document's "online audit" recommendation and is the ultimate sanity check.

## Open Questions

1. **How well does GAE-based AWR ranking actually correlate with PPO play strength?** This should be measured empirically: run an AWR sweep and a PPO sweep on the same 3-4 architectures and compute rank correlation. If Spearman rho > 0.8, GAE-based AWR is good enough; if not, the advantage source upgrade becomes urgent.

2. **What is the right reward shaping for intermediate TS rewards?** VP delta is obvious, but DEFCON changes, military ops, and space race advancement could also be included. Over-shaping risks biasing toward tactical play at the expense of strategic positioning.

3. **Is the current dataset large enough?** The log shows collection was started for 11 models x 1400 games (~924K rows expected). For architecture ranking, the document implicitly assumes the dataset is large enough that overfitting is not the primary concern. With ~900K rows and 5 epochs, this is likely fine for discriminating architectures, but a learning curve analysis (train on 100K, 300K, 600K, 900K) would confirm whether more data helps.

4. **Should the advantage normalization be per-game or global?** The document does not address this explicitly. Per-game normalization ensures each game contributes equally regardless of its terminal reward magnitude. Global normalization preserves the information that some games are more decisive. For architecture ranking, per-game is probably safer.
---
