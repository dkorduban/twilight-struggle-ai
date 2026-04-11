# Opus Analysis: Autoregressive Country Selection

Date: 2026-04-11T12:00:00Z
Question: How to make country predictions dependent on the card played without losing inference efficiency?

## Executive Summary

The current factored architecture computes card, mode, and country logits independently from a shared trunk hidden state, meaning the country distribution is identical regardless of which card is actually played. This is architecturally wrong for ~40% of game actions where eligible countries are card-specific (event targets, Junta follow-ups, war cards, card-ops-dependent accessibility). The most practical fix is **card-conditioned country logits via a lightweight bilinear or FiLM layer** that modulates the country head using a card embedding, computed in a single forward pass with no autoregressive overhead. A full autoregressive approach (predict card first, then run a second forward pass for countries) is unnecessary because the trunk already encodes the full game state -- the missing piece is just the card->country interaction term, not a second full inference step.

## Findings

### 1. Current Architecture: Independent Factored Heads

The model (`TSBaselineModel` and variants in `python/tsrl/policies/model.py`) computes:

```
trunk_input = cat(h_inf, h_card, h_scalar)   # (B, 320)
hidden = trunk_block2(trunk_block1(proj(trunk_input)))  # (B, 256)

card_logits = card_head(hidden)               # (B, 111)  -- Linear(256, 111)
mode_logits = mode_head(hidden)               # (B, 5)    -- Linear(256, 5)
country_strategy_logits = strategy_heads(hidden)  # (B, 4, 86) -- Linear(256, 4*86)
strategy_logits = strategy_mixer(hidden)      # (B, 4)    -- Linear(256, 4)
country_logits = softmax_mix(strategy, country_strategy)  # (B, 86)
```

All heads read the same `hidden` vector. The country distribution is **unconditional on the chosen card or mode**. During MCTS tree expansion and PPO rollout, the joint action probability is computed as:

```
P(card, mode, country) = P(card) * P(mode) * P(country)
```

This factorization assumes independence, which is violated for most non-influence actions.

### 2. Why Independence Is Wrong

Card-country dependence falls into several categories:

**Hard constraints (different legal sets):**
- Brush War: only stability <= 2 countries
- Arab-Israeli War: only Israel
- Korean War: only South Korea
- Indo-Pakistani War: only India/Pakistan
- Junta: only Central/South America
- Decolonization: only Africa/Southeast Asia
- Marshal Plan: only West Europe

The MCTS expansion code (line 1287-1306 of `mcts_batched.cpp`) already handles this at the **masking level** -- it intersects the country logits with the legal country set for each (card, mode) combination. So the hard constraints are satisfied. The problem is **soft preferences**: the model cannot express "if I play card X, I prefer country Y; if I play card Z, I prefer country W" because the country distribution is the same tensor regardless.

**Soft preferences (same legal set, different optimal targets):**
- 3-ops influence vs 4-ops influence: different allocation patterns (4 ops can break control in tougher countries)
- Coup with 2-ops card vs 4-ops card: prefer higher-stability targets with higher ops
- Event-triggered follow-up placements (Decolonization places in different countries than COMECON)

**Impact quantification:** The current system only loses accuracy when multiple cards are played for ops/influence in the same game state AND those cards would optimally target different countries. For coup/realign (single target), the legal mask already handles most of the differentiation. The biggest loss is in influence placement where 2-ops, 3-ops, and 4-ops cards want meaningfully different allocation patterns.

### 3. Approach A: Full Autoregressive (Two-Pass)

**Design:** Predict card first. Then feed the chosen card embedding into a second pass (or second head) that produces card-conditioned country logits.

**Pros:**
- Fully correct: country distribution is perfectly conditioned on the selected card
- Clean mathematical formulation: P(card) * P(mode|card) * P(country|card, mode)

**Cons:**
- **2x inference latency** for every action during MCTS tree expansion. The batched MCTS does one forward pass per expansion batch (typically 64-256 states). A second pass would double GPU time.
- **Speculative execution** (run top-K cards in parallel) requires K forward passes for the country head, increasing latency proportionally. Even with K=3, this is a 4x slowdown over the current single pass.
- **PPO log-prob recomputation** becomes more complex: need to re-derive the card-conditioned country distribution during training, matching the rollout's sampling.
- **Backward compatibility**: existing TorchScript models and C++ inference code would need significant rework.

**Verdict:** Overkill. The two-pass latency cost is not justified by the marginal accuracy gain.

### 4. Approach B: Card-Conditioned Country Head (FiLM / Bilinear)

**Design:** In a single forward pass, compute `hidden` as before. Then modulate the country head using the card identity:

```python
# Card embedding lookup (shared with card_encoder or separate)
card_embed = self.card_cond_embed(card_id_onehot)  # (B, embed_dim)

# FiLM: feature-wise linear modulation
gamma = self.film_gamma(card_embed)  # (B, hidden_dim)
beta = self.film_beta(card_embed)    # (B, hidden_dim)
conditioned_hidden = gamma * hidden + beta  # (B, hidden_dim)

country_logits = self.country_head(conditioned_hidden)  # (B, 86)
```

**Problem:** At inference time during MCTS expansion, we don't know which card will be selected yet -- we're computing priors for ALL (card, mode, country) combinations simultaneously. The FiLM approach requires knowing the card first.

**However**, during MCTS tree expansion (lines 1268-1330 of `mcts_batched.cpp`), the code already iterates over each card in the draft set. The country logits are used per-card to compute `card_prob * mode_prob * country_prob`. So we could compute **card-conditioned country logits for each card** if we had a lightweight card-conditioning layer.

**Efficient implementation:**
```python
# In forward(), output a card-conditioning matrix instead of single country logits:
card_embed_matrix = self.card_embed(torch.arange(111))  # (111, embed_dim)
# Bilinear: country_logits[c, card] = hidden @ W @ card_embed[card] + bias
# Or: output (B, 111, 86) tensor = card-conditioned country logits for all cards
```

This is too expensive as a dense (B, 111, 86) tensor. But a **factored bilinear**:
```python
# hidden: (B, H), card_embed: (111, E)
# W: (H, rank, E) factored as W1 @ W2^T with rank << H
proj_h = self.proj_hidden(hidden)  # (B, rank)
proj_c = self.proj_card(card_embed_matrix)  # (111, rank)
card_country_bias = proj_h @ proj_c.T  # (B, 111) -- per-card adjustment
# country_logits_per_card[b, card, country] = base_country_logits[b, country] + card_country_bias[b, card] * ...
```

This still doesn't give per-country modulation per card efficiently.

### 5. Approach C: Strategy Mixture Conditioned on Card (Recommended)

**Key insight:** The model already has a **4-strategy mixture** for country logits:
```
country_logits = sum_s( softmax(strategy_mixer(hidden))[s] * softmax(strategy_heads(hidden))[s, :] )
```

The 4 strategies implicitly capture different "placement patterns" (e.g., strategy 0 = Europe focus, strategy 1 = Asia focus, etc.). The missing link is that the **strategy mixing weights** should depend on which card is played.

**Design:**
```python
# Current: strategy_logits = self.strategy_mixer(hidden)  # (B, 4)
# New: strategy_logits = self.strategy_mixer(hidden) + self.card_strategy_bias(card_onehot)
# Or more expressively:
# strategy_logits = self.strategy_mixer(cat(hidden, card_embed))  # (B, 4)
```

**Why this works:**
- The 4 strategies already parameterize 4 different country distributions
- Card-dependent mixing lets "Brush War" select the strategy that concentrates mass on low-stability countries, while "Marshall Plan" selects the Europe-heavy strategy
- Only adds ~450 parameters (111 x 4 bias matrix, or a small Linear)
- **No change to inference shape**: still outputs (B, 4, 86) strategy logits + (B, 4) mixing weights
- C++ MCTS code already supports strategy selection via argmax or mixing
- Single forward pass, negligible latency overhead

**Limitation:** 4 strategies may not be enough to capture all card-country patterns. But it's already a large improvement over zero card-conditioning, and NUM_STRATEGIES can be increased to 8 if needed.

### 6. Approach D: Per-Card Country Bias Vector (Simplest)

**Design:** Learn a (111, 86) bias matrix. At action construction time (not in the model forward pass), add the card's bias row to the country logits:

```python
# In model:
self.card_country_bias = nn.Embedding(111, 86)  # ~9.5K params

# In forward():
# Don't apply here -- return raw country_logits as before

# At action construction (C++ or Python):
# country_logits_for_card_c = country_logits + card_country_bias[c]
```

**Pros:**
- Trivially simple
- No change to the forward pass or trunk
- Card-specific country adjustments
- Can be applied per-card during MCTS expansion with negligible cost
- Only 9,546 new parameters

**Cons:**
- The bias is context-independent (same bias for card X regardless of game state)
- This is essentially a lookup table, not a learned interaction
- Cannot capture "card X prefers country Y when opponent controls Z"

**But:** As a first step, this captures the dominant effect (card identity -> country preference) without any architectural disruption. The game-state-dependent interactions are already captured by the trunk hidden state feeding into the base country logits.

### 7. Approach E: Cross-Attention from Country Head to Card Logits

**Design:** Country head attends to the card logit distribution as a soft "which card am I likely playing" signal.

This is mathematically similar to the expected value of card-conditioned country logits:
```
E_card[country_logits(card)] = sum_c P(card=c) * country_logits_given_c
```

**Problem:** This marginalizes over cards, which is exactly what the current independent model already does implicitly. It doesn't solve the problem -- we want country logits conditioned on a SPECIFIC card, not averaged over all possible cards.

### 8. Interaction with Current Pipeline

**PolicyCallback system:** The `choose_country` callback in C++ is called AFTER the card and mode are decided. This means the C++ action-construction path already knows which card was selected. Approaches C, D, and B are all compatible with this -- they just need the card identity passed to the country selection step.

**MCTS tree expansion:** Lines 1268-1330 iterate over `(card, mode)` pairs and compute per-edge priors. The country logits are currently shared across all cards. Approaches C and D can be applied here per-card with minimal overhead:
- Approach C: select strategy based on card identity (already nearly possible with current code)
- Approach D: add card bias vector to country logits per card (cheap array addition)

**PPO training:** The log_prob computation (line 1671) sums `log_prob_card + log_prob_mode + log_prob_country`. If country logits become card-dependent, the training code needs to:
1. Know which card was sampled (already stored in `step.card_idx`)
2. Recompute card-conditioned country logits for that card
3. Use those for the PPO ratio

This is straightforward for all approaches.

### 9. Speculative Execution Analysis

Running inference for top-K most probable cards in parallel is technically feasible but complex:
- Requires K separate country-head evaluations (or one batched evaluation with K card contexts)
- The trunk computation (the expensive part) is shared, only the country head differs
- For K=3, the country head is ~10% of total FLOPS, so overhead is ~30% of the cheap part = ~3% total
- BUT the C++ implementation would need significant refactoring to support this

**Assessment:** Speculative execution for country logits is not worth the implementation complexity given that Approaches C and D achieve the same goal more simply.

## Conclusions

1. **The current factored independence assumption is the primary architectural deficiency for country selection.** The model produces identical country preferences regardless of which card is played, losing information that is critical for ~40% of actions (non-influence modes and event follow-ups).

2. **A full autoregressive two-pass approach is unnecessary and too expensive.** The 2x inference latency in MCTS (the dominant compute bottleneck) is not justified when lighter alternatives exist.

3. **The recommended first step is Approach D: a learned (111, 86) card-country bias matrix** (~9.5K parameters). This is the simplest change that captures the dominant card->country relationship, requires no trunk changes, and can be applied per-card during MCTS expansion with negligible overhead.

4. **The recommended second step is Approach C: card-conditioned strategy mixing weights.** This lets the 4-strategy mixture adapt to the card being played, providing game-state-dependent card-country interactions. It builds naturally on the existing strategy mixture architecture and adds minimal parameters.

5. **Speculative top-K execution and cross-attention approaches are not recommended.** They either don't solve the problem (cross-attention marginalizes over cards) or add unjustified complexity (speculative execution).

6. **The C++ MCTS expansion loop already iterates per-card**, so card-specific country logits can be injected at the point where priors are computed (line 1287-1306 in `mcts_batched.cpp`) without restructuring the expansion.

7. **PPO training is straightforward to adapt**: `step.card_idx` is already stored, so card-conditioned country log-probs can be recomputed using the correct card identity during the PPO update.

## Recommendations

1. **Phase 1 (1-2 days):** Add `card_country_bias = nn.Embedding(111, 86)` to the model. In the forward pass, output it as a new key `card_country_bias`. In C++ MCTS expansion, add `bias[card_idx]` to `country_logits_arr` before computing per-card country priors. In PPO training, apply the bias for the sampled card before computing country log-probs.

2. **Phase 2 (2-3 days):** Extend the strategy mixer to accept card identity: `strategy_logits = strategy_mixer(hidden) + card_strategy_bias[card_id]`. This lets the 4 strategies be card-selected. Measure Elo impact vs Phase 1.

3. **Phase 3 (optional, if Elo gain is clear):** Replace the fixed (111, 86) bias with a FiLM-conditioned country head: `conditioned_hidden = gamma(card_embed) * hidden + beta(card_embed)`, then `country_logits = country_head(conditioned_hidden)`. This captures game-state x card interactions but requires per-card forward through the country head.

4. **Do not pursue** full autoregressive two-pass inference or speculative K-card execution at this time. Revisit only if Phase 1-2 show clear gains but plateau.

5. **Benchmark each phase** with 2000-game Elo tournaments. The expected signal is strongest for coup/realign target selection (where card ops determine which targets are worth hitting) and event follow-up placements.

## Open Questions

1. **How much of the country-selection error is actually due to independence vs other factors?** A diagnostic: measure how often the top-1 country prediction changes when the card identity is provided vs withheld. If the change rate is <10%, the independence assumption may not be the binding constraint.

2. **Should the card-country bias be applied additively (logit space) or multiplicatively (probability space)?** Logit-space addition is simpler and more numerically stable; start there.

3. **Does the 4-strategy mixture already implicitly capture some card-country dependence?** The trunk `hidden` state encodes the full game state including the hand composition. If the trunk has learned to adjust strategy weights based on hand composition, some card conditioning is already present. Measure strategy selection variance across different card choices to assess this.

4. **Should mode-country interaction also be conditioned?** The mode determines the legal country set (influence vs coup have very different accessible sets), but the model already handles this via legal masking. Mode-specific country preferences beyond legality (e.g., "for coups prefer high-stability BGs, for influence prefer low-stability frontier countries") may warrant a separate mode-country bias term.

5. **How does this interact with Phase 3 of the pragmatic heads plan (event country targets via PolicyCallback)?** The PolicyCallback system already provides card identity to the country selection. The bias/FiLM approach is complementary: PolicyCallback handles event-specific decisions, while card-conditioned country logits handle the main-AR ops/coup/realign country selection.
