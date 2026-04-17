# Opus Analysis: Side-Aligned Representation with Learned Side Embedding
Date: 2026-04-16 UTC
Question: What are the prospects of flipping representation to side-aligned, but increasing side signal from single bit to a side embedding?

## Executive Summary

Full side-alignment (flipping VP sign, swapping milops/space order, swapping trap booleans when acting as US) combined with a learned side embedding is a sound idea in principle but carries significant implementation risk for modest expected gain. The current hybrid encoding creates a genuine representational burden — the model must learn to conditionally negate/swap ~10 scalar features based on a single bit — but (a) the `TSControlFeatGNNSideModel` already implements the learned side embedding + separate value heads and is available for use, (b) the side anti-correlation in PPO is more likely caused by training dynamics (PFSP weighting, shared advantage normalization batches) than feature encoding, and (c) full side-alignment requires synchronized C++ and Python changes, breaks all checkpoints, and introduces a subtle bug surface in the feature pipeline. The recommended path is to adopt `TSControlFeatGNNSideModel` as the default (it already has the side embedding), add FiLM conditioning to modulate the trunk (cheap 512-param addition), and defer full feature flipping until a BC ablation proves it helps.

## Findings

### 1. Current Feature Encoding: The Hybrid Problem

The current encoding mixes three conventions:

**Side-relative (acting-side-first):**
- Influence: `fill_influence_array` in `BatchInputs::fill_slot` always fills USSR first, US second (lines 122-127 of `nn_features.cpp`). However, the `CountryEmbedEncoder` and `CountryAttnEncoder` in `model.py` process these as `ussr_inf = influence[:, :86]`, `us_inf = influence[:, 86:]` without any side-aware reordering. So influence is actually **absolute (USSR-first)**, not side-relative.
- **Correction to the task description**: Influence is NOT side-relative in the C++ `BatchInputs::fill_slot`. It always fills `Side::USSR` first regardless of acting side. The Python dataset similarly concatenates `[ussr_influence, us_influence]`. The task description states "Influence features: already side-relative (acting side first, opponent second)" but this is incorrect based on the code.

**Absolute (USSR-positive/first):**
- `scalar[0]` = VP/20 — positive means USSR ahead
- `scalar[2]` = milops_ussr/6, `scalar[3]` = milops_us/6
- `scalar[4]` = space_ussr/9, `scalar[5]` = space_us/9
- `scalar[11]` = bear_trap_active (USSR-specific trap)
- `scalar[12]` = quagmire_active (US-specific trap)
- `scalar[14]` = iran_hostage_crisis_active (anti-US)
- `scalar[20]` = vietnam_revolts_active (pro-USSR)
- `scalar[30]` = ops_modifier_ussr, `scalar[31]` = ops_modifier_us
- All 86+86 influence values (USSR first, US second)

**Actor-relative:**
- `scalar[7]` = actor_holds_china (relative to acting side)
- Cards: actor_known_in, actor_possible (relative to acting side)

**Side indicator:**
- `scalar[10]` = 0 for USSR, 1 for US — the sole signal

This hybrid creates a genuine representational challenge. When the model acts as US, it must learn that:
- Positive VP is bad for it (USSR leads)
- `milops[0]` is the opponent's milops, not its own
- `bear_trap_active` refers to the opponent being trapped, not itself
- But `actor_holds_china` already refers to itself

The model must learn different conditional interpretations for ~20 features based on a single binary scalar buried in a 32-dim input vector. A 256-dim hidden network CAN learn this — it is equivalent to learning two separate linear projections gated by the side bit — but it wastes capacity on what is essentially a routing/interpretation problem rather than strategic reasoning.

### 2. What Full Side-Alignment Would Look Like

To make all features "acting-side-positive," the C++ `fill_scalars` and `fill_influence_array` (or the Python dataset code) would need these changes:

**Influence (172 dims):**
```
When acting as USSR: [ussr_inf, us_inf]  (unchanged)
When acting as US:   [us_inf, ussr_inf]  (swapped)
```

**Scalars:**
```
[0]  VP: negate for US (positive = acting side ahead)
[2]  milops_acting / 6  (swap for US)
[3]  milops_opponent / 6
[4]  space_acting / 9  (swap for US)
[5]  space_opponent / 9
[6]  china_held_by: reinterpret (0 = acting side holds it)
[11] acting_side_trap_active  (bear_trap if USSR, quagmire if US)
[12] opponent_trap_active     (quagmire if USSR, bear_trap if US)
[14] iran_hostage_crisis: only relevant when US is acting
[20] vietnam_revolts: only relevant when USSR is acting
[30] ops_modifier_acting / 3  (swap for US)
[31] ops_modifier_opponent / 3
```

**Effect booleans pose a problem**: Some effects are side-specific by game design, not by acting-side convention. `bear_trap_active` affects USSR, `quagmire_active` affects US. Swapping these to "my_trap_active" / "opponent_trap_active" makes semantic sense. But `flower_power_active` (triggers when US plays war cards) and `vietnam_revolts_active` (+1 ops for USSR in SE Asia) are inherently side-specific. Converting them to "helps_me" / "hurts_me" requires knowing which effects help which side, which is game-rule-specific logic embedded in the feature pipeline.

**Estimated changes:**
- `nn_features.cpp`: ~40 lines in `fill_scalars`, ~5 lines in `fill_slot` to swap influence order
- `dataset.py`: ~30 lines to replicate the same swapping in Python
- All downstream code that reads specific scalar indices must be audited
- The `ControlFeatCountryEncoder` and `ControlFeatGNNEncoder` both hardcode `ussr_inf = influence[:, :86]`, `us_inf = influence[:, 86:]` — they would need to interpret the first 86 as "acting side" instead
- Region scoring scalars (42 dims from ControlFeatCountryEncoder) also compute USSR/US control separately and would need reordering

### 3. What a Side Embedding Would Look Like

**Already implemented**: `TSControlFeatGNNSideModel` (line 1429 of `model.py`) already has:
```python
self.side_embed = nn.Embedding(2, SIDE_EMBED_DIM)  # SIDE_EMBED_DIM = 32
# Concatenated to trunk input:
trunk_input = torch.cat([h_inf, h_card, h_scalar, h_side], dim=-1)
# Trunk proj is TRUNK_IN + SIDE_EMBED_DIM = 352 -> hidden_dim
```

This is concatenation-based conditioning. The side embedding provides 32 learnable dimensions (vs the single scalar[10] bit) that the trunk can use to modulate its behavior.

**FiLM conditioning (not yet implemented, would be stronger):**
```python
# After trunk projection but before residual blocks:
side_idx = scalars[:, 10].long()
gamma = self.film_gamma(self.side_embed(side_idx))  # (B, hidden_dim)
beta = self.film_beta(self.side_embed(side_idx))     # (B, hidden_dim)
trunk_base = gamma * trunk_base + beta  # Feature-wise modulation
```

FiLM is strictly more expressive than concatenation: it can multiplicatively gate every feature in the trunk, effectively giving each side its own linear transformation of the shared representation. Cost: 2 * (32 * 256) = 16K additional parameters (vs current ~500K total), negligible.

**Comparison:**

| Approach | Extra Params | Expressiveness | Complexity |
|----------|-------------|----------------|------------|
| Single scalar[10] bit | 0 | Low — one dimension to condition 256-dim trunk | None |
| Concat embedding (current SideModel) | 32 (embed) + 32*256 (trunk proj expansion) = ~8K | Medium — 32 dims concatenated before trunk | Low |
| FiLM conditioning | 32 + 2*(32*256) = ~16K | High — multiplicative per-neuron modulation | Medium |
| Separate trunks per side | ~250K (doubled trunk) | Maximal — completely independent | High, loses transfer |

### 4. Would This Help the Observed Side Anti-Correlation in PPO?

**The anti-correlation (USSR WR 57%->21%, US 27%->39%) is unlikely caused by feature encoding.**

Evidence:

1. **The encoding has been constant throughout training.** The anti-correlation appeared during a specific PPO iteration window (v299-v305), not from the beginning. If the feature encoding were the root cause, the problem would be persistent, not episodic.

2. **PFSP weighting was identified as the cause.** Per `project_ppo_chain_state.md` in memory: `pfsp_exp=1.5` was accidentally changed to `pfsp_exp=0.5`, which caused the plateau/regression. When one side's opponents become too easy (low PFSP exponent = more uniform opponent selection), that side stops improving while the other side's training signal degrades.

3. **Per-side advantage normalization already exists.** The `pack_steps` function (line 2054-2060 of `train_ppo.py`) normalizes advantages independently for USSR and US steps. This prevents one side's gradient from dominating in magnitude, but it does NOT prevent the shared trunk from being pulled in contradictory directions.

4. **The shared trunk gradient conflict is real but architectural, not representational.** Even with perfect side-aligned features, a shared trunk receiving USSR-positive gradients and US-positive gradients in the same batch will experience conflicting updates. The solution is per-side conditioning (embedding/FiLM) or separate components, not feature flipping.

**Where feature alignment COULD help (modest benefit):**
- The value head must learn V(state) from features where VP sign depends on which side is asking. With side-aligned VP, the value head can directly learn "positive VP = I'm winning" without conditional interpretation. This reduces the effective complexity of the value function.
- With 256 hidden dims and 2 residual blocks, the model has enough capacity to learn the conditional interpretation, but it uses some of that capacity on routing logic instead of strategic reasoning. Side-alignment frees this capacity.
- Estimated benefit: 1-3 Elo points from cleaner gradient signal on value, unlikely more.

### 5. Interaction with C++ Feature Extraction

The C++ pipeline (`nn_features.cpp`) is used in:
- `BatchInputs::fill_slot` for MCTS/ISMCTS inference
- `collect_selfplay_rows_jsonl.cpp` for self-play data collection
- `forward_model` / `forward_model_batched` for any C++ model calls

Changing to side-aligned features requires:

1. **`fill_scalars`**: Add conditional logic based on `side` parameter (already available). ~15 additional branches.
2. **`fill_slot`**: Change `Side::USSR` / `Side::US` to `side` / `opposite(side)` for influence filling. 2-line change.
3. **`fill_influence_array`**: No change needed (already takes `side` parameter).
4. **Python dataset**: Must replicate the same conditional logic when building tensors from Parquet columns. The `phasing` column already indicates which side is acting.

**Risk surface:**
- Any mismatch between C++ and Python feature encoding creates silent training/inference distribution shift — the model trains on Python-encoded data but infers with C++ features.
- The current code has exactly this risk surface: if C++ `fill_slot` and Python `TS_SelfPlayDataset` ever disagree on normalization, ordering, or feature semantics, the model silently degrades.
- Adding conditional side-flipping to both codepaths doubles the chance of a mismatch bug.

**Mitigation:** A cross-validation test that extracts features from the same game state in both C++ and Python and asserts exact equality. This test should exist regardless of whether side-alignment is adopted.

### 6. Precedent from Other Game AIs

**AlphaZero / AlphaGo:** Uses fully side-aligned representation. The board is always from the perspective of the player to move. In Go/Chess, this is trivial because the games are symmetric (just flip colors). The value head predicts "probability current player wins." This is the gold standard approach.

**OpenSpiel:** Implements `InformationStateTensor` per player, which is inherently side-relative. The standard approach in OpenSpiel is that each player's observation is from their own perspective.

**Pluribus (Poker):** Side-aligned — each player's features are relative to their own position. No shared "absolute" encoding.

**Asymmetric games (StarCraft, Dota):** These typically use fully side-relative encoding WITH a race/hero indicator. The trunk sees "my_units, enemy_units" not "terran_units, zerg_units." The race/faction information is provided as a separate embedding, analogous to our side embedding.

**Key insight from the literature:** Symmetric encoding (side-relative features) is universally preferred when possible because:
1. It halves the effective sample complexity (both sides' experiences teach the same policy)
2. It simplifies the value function (always predicting "my" probability of winning)
3. It eliminates the conditional interpretation problem

**However, Twilight Struggle is fundamentally asymmetric.** USSR and US have different card pools, different early-game advantages, different optimal strategies. Unlike Chess/Go, you cannot simply swap colors and get an equivalent position. This means:
- Side-relative features still help (cleaner representation)
- But the model MUST still know which side it is (hence the side embedding)
- The value function IS different per side (hence separate value heads)
- Perfect weight sharing across sides is not possible or desirable

### 7. Risk Assessment

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| Checkpoint incompatibility (all existing checkpoints break) | High | 100% | Must retrain from scratch. BC on frozen corpus first. |
| C++/Python feature mismatch bug | High | Medium | Cross-validation test between C++ and Python encoders |
| Effect booleans have ambiguous side-relative semantics | Medium | High | Some effects (flower_power, vietnam_revolts) are inherently one-sided |
| Minimal actual improvement for the cost | Medium | Medium-High | The model may already handle the conditional interpretation adequately |
| Breaks ControlFeatCountryEncoder region scoring | Medium | High | Hardcoded USSR/US control computation needs rewriting |
| Training instability during transition | Medium | Medium | New feature distribution may require LR tuning |

### 8. Incremental Alternative: Side Embedding + FiLM Without Feature Flipping

A cheaper approach that captures most of the benefit:

1. **Adopt `TSControlFeatGNNSideModel` as default** (already has side embedding + separate value heads)
2. **Add FiLM conditioning** to the trunk (16K params, ~20 lines of code)
3. **Keep features absolute** — the FiLM layer can learn to "virtually flip" features by learning gamma=-1, beta=0 for the appropriate neurons when acting as US

The FiLM layer is universal: given enough capacity, it can learn any affine transformation of the trunk conditioned on side. This includes the "flip VP sign, swap milops order" operation that full side-alignment would hardcode. The advantage is zero changes to the C++ feature pipeline, zero checkpoint format changes, and the model can learn whatever conditional processing is optimal rather than having it hardcoded.

**Expected benefit vs full side-alignment:** ~80-90% of the representational benefit with ~10% of the implementation cost.

### 9. Ablation Design (If We Want to Measure the Effect)

The cleanest way to test is a BC ablation on frozen corpus:

**Experiment A (baseline):** Current features + current `TSControlFeatGNNSideModel` with concat side embedding
**Experiment B (FiLM):** Current features + FiLM conditioning instead of concat
**Experiment C (side-aligned + FiLM):** Fully side-aligned features + FiLM conditioning

Compare card_top1, mode_accuracy, value_brier across experiments. If C is not meaningfully better than B, the feature flipping is not worth the implementation cost.

This requires only Python-side changes (modify the dataset to flip features) and can be done in 1 day. No C++ changes needed for the ablation — just modify `TS_SelfPlayDataset` to conditionally swap features for US rows.

## Conclusions

1. **The hybrid encoding IS a real problem** — the model wastes trunk capacity learning conditional feature interpretation from a single bit. However, the 256-dim trunk with 2 residual blocks has sufficient capacity to learn this, so the practical cost is modest (estimated 1-5 Elo).

2. **The side anti-correlation in PPO is NOT caused by feature encoding.** It was caused by PFSP weight misconfiguration (pfsp_exp changed from 1.5 to 0.5). Feature encoding changes will not fix PPO training dynamics.

3. **`TSControlFeatGNNSideModel` already implements the side embedding and separate value heads.** The infrastructure exists. The question is whether it is being used in the active PPO chain.

4. **FiLM conditioning (side embedding modulating trunk via gamma/beta) would be the highest-value addition** — 16K params, ~20 lines of code, no C++ changes, no checkpoint format changes. It gives the model a learnable "virtual feature flip" that subsumes most of the benefit of hardcoded side-alignment.

5. **Full side-alignment is high-cost, medium-risk, low-incremental-benefit over FiLM.** It requires synchronized C++/Python changes, breaks all checkpoints, introduces bug surface in the feature pipeline, and the ambiguous semantics of asymmetric effect booleans create design complexity.

6. **Influence is NOT currently side-relative** (contrary to the task description). The C++ `BatchInputs::fill_slot` always fills USSR first, US second, regardless of acting side. This is a larger feature misunderstanding to correct.

7. **Game AI precedent strongly favors side-relative encoding**, but Twilight Struggle's fundamental asymmetry limits the benefits. The model must still know which side it is and learn side-specific strategies.

8. **A Python-only BC ablation can measure the effect in 1 day** without touching C++. Modify the dataset to conditionally flip features for US rows and compare BC metrics.

## Recommendations

1. **Immediate (0 effort):** Verify that the active PPO chain uses `TSControlFeatGNNSideModel` (with side embedding + separate value heads), not `TSBaselineModel`. If not, switch. This is the single most impactful change.

2. **Short-term (1 day):** Add FiLM conditioning to `TSControlFeatGNNSideModel`. Replace the simple side embedding concatenation with multiplicative+additive modulation of the trunk. This is ~20 lines of Python, 16K extra params, and gives the model a learnable feature-flip mechanism.

3. **Short-term (1 day):** Run the BC ablation: modify `TS_SelfPlayDataset` to optionally produce side-aligned features (flip VP, swap milops/space/influence/ops_modifier for US rows). Compare BC metrics for (a) current features + concat embedding, (b) current features + FiLM, (c) side-aligned features + FiLM. If (c) is not meaningfully better than (b), do not pursue C++ side-alignment.

4. **Defer:** Full C++ side-alignment (`nn_features.cpp` changes). Only pursue if the BC ablation shows clear benefit (>2pp on any BC metric) AND you are willing to retrain from scratch.

5. **Regardless:** Add a cross-validation test that extracts features from the same game state via both C++ and Python and asserts exact numerical equality. This catches silent feature mismatches that could already exist.

## Open Questions

1. **Which model class is the active PPO chain currently using?** If it is `TSBaselineModel` or `TSControlFeatGNNModel` (without side embedding), switching to `TSControlFeatGNNSideModel` is the first priority.

2. **Has the `actor_relative` value target mode been adopted in PPO?** The dataset supports it, but the PPO training loop collects value targets from the C++ engine. The sign convention at collection time must match what the model expects.

3. **How does `ControlFeatCountryEncoder.forward()` interact with side-aligned features?** It hardcodes `ussr_inf = influence[:, :86]` and `us_inf = influence[:, 86:]`. Under side-aligned encoding, this becomes `acting_inf = influence[:, :86]` and `opponent_inf = influence[:, 86:]`. The control status computation (`ussr_controls`, `us_controls`) and region scoring scalars would need renaming and reinterpretation. The 42 region scalars are currently returned in USSR/US order — they would need to be in acting/opponent order.

4. **Is there a feature parity test between C++ `fill_scalars` and Python `TS_SelfPlayDataset` scalar construction?** The two codepaths independently implement the same normalization. Any divergence causes silent model degradation.

5. **What fraction of the model's capacity is actually spent on side-conditional interpretation?** A probing experiment (freeze trunk, train a linear probe to predict side from trunk activations) would quantify how much the trunk encodes side information. If it is a small fraction, the feature encoding is not the bottleneck.
