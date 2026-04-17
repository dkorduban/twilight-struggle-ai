# Opus Analysis: Model Architecture Ideas for TS AI
Date: 2026-04-16 UTC
Question: What model-related ideas could improve the Twilight Struggle AI?

## Executive Summary

The current ~500K-parameter factorized policy model has meaningful architectural gaps that likely cap playing strength. The highest-leverage improvements are: (1) adding decision context features so the model knows *what kind of decision* it is making (headline vs action round vs mid-event choice), (2) adopting a frozen-corpus iteration strategy to cheaply test architecture changes before committing to expensive PPO runs, and (3) splitting value heads per side (already implemented in `TSControlFeatGNNSideModel` but apparently not used in the PPO chain that regressed). Model distillation, auxiliary world-model heads, and side-specific policies each have roles but are lower priority than fixing the information deficit in the current feature set.

## Findings

### 1. Model Distillation

**Current situation:** The model is already small (~500K params, hidden_dim=256). There is no larger teacher model to distill from -- the strongest model IS the current model.

**Would distilling into a smaller model help?**
No, not in the traditional sense. The model is not large enough that inference speed is a bottleneck. The C++ batched MCTS pipeline already processes thousands of positions per second. A smaller model would be weaker without compensating speed gains.

**Where distillation DOES help (and is already partially implemented):**
- The codebase already has `teacher_targets_path` support in `TS_SelfPlayDataset`, with soft teacher card/mode/value targets joined by `(game_id, step_idx)`.
- Teacher search (MCTS with more simulations) on curated hard positions, distilled back into the student, is the right distillation direction. This is "search distillation" (AlphaZero-style), not model compression.

**Tradeoffs:**
- Pro: Search distillation improves quality at no inference cost.
- Con: Teacher search is expensive per position. Must be selective (hard states only).
- Pro: The infrastructure for it already exists in the dataset code.

**Recommendation:** Continue the search-distillation path. Do NOT compress the model smaller.

### 2. Auxiliary World-Model Head

**Proposed:** Add H_a(a) -> z_a encoding the action, then H_next(s, z_a) -> s' predicting the next state.

**Feasibility analysis:**

The idea is sound in principle -- it would force the trunk to learn representations that understand how actions change board state. However, there are significant practical challenges specific to Twilight Struggle:

1. **Target definition is non-trivial.** After an action, the next state depends on:
   - Dice rolls (coup outcomes, war cards, realignment)
   - Opponent's response (event choices, Bear Trap/Quagmire rolls)
   - Event side effects (chain events like Decolonization -> independence)
   - Hidden information (opponent's hand for Cat C events)

   The model would need to predict the *expected* next state or a distribution, not a deterministic successor. This makes the loss function complicated.

2. **What COULD be predicted deterministically:**
   - Influence placement outcomes (fully deterministic)
   - Space race advancement (deterministic)
   - Which card goes to discard/removed (deterministic given the action)
   - VP changes from scoring cards (deterministic)

3. **A simpler version that captures most value:**
   Rather than full next-state prediction, predict *specific strategic consequences*:
   - Delta VP from this action (scalar)
   - Delta DEFCON from this action (scalar)
   - Delta MilOps from this action (scalar)
   - Whether this action triggers opponent event (binary)
   - Region control changes (7x3: for each region, change in {presence, domination, control})

   This is much cheaper to implement and supervise (ground truth from the engine), and captures the key "game rules understanding" the auxiliary head would provide.

4. **Action encoding challenge:** The factorized action (card_id, mode, country_targets) needs a fixed-size embedding. Options:
   - Concatenate card embedding + mode one-hot + country allocation vector (86-dim) -> MLP -> z_a
   - This is straightforward but adds ~50K params and a non-trivial training target.

**Recommendation:** A lightweight "consequence predictor" auxiliary head (predict delta-VP, delta-DEFCON, delta-MilOps, opponent-event-fires as 4 scalars) would be higher value-per-complexity than full next-state prediction. It can be trained from engine ground truth available in the rollout data.

### 3. Context for Mid-Opponent-AR Decisions

**This is the single biggest information gap in the current model.**

**What the model currently sees:**
From `nn_features.cpp::fill_scalars()` and `dataset.py`, the scalar features are:
- `[0]` VP/20
- `[1]` (DEFCON-1)/4
- `[2-3]` milops_ussr/6, milops_us/6
- `[4-5]` space_ussr/9, space_us/9
- `[6]` china_held_by (0 or 1)
- `[7]` actor_holds_china
- `[8]` turn/10
- `[9]` ar/8
- `[10]` side (0=USSR, 1=US)
- `[11-27]` 17 active effect booleans (bear_trap, quagmire, CMC, etc.)
- `[28-29]` Chernobyl active + blocked region
- `[30-31]` ops_modifier per side

**What the model does NOT know:**

1. **GamePhase:** The model cannot distinguish headline decisions from action round decisions. The `ar` scalar is 0 during headlines AND during setup. The `GamePhase` enum (Setup=0, Headline=1, ActionRound=2, Cleanup=3, GameOver=4) is never passed to the model. This is critical because optimal play differs dramatically between headlines and action rounds (e.g., scoring cards in headlines vs action rounds, DEFCON risk calculus).

2. **Decision type (DecisionKind):** When the `SmallChoice` head fires during event resolution, the model does not know WHICH event triggered the decision. The `EventDecision` struct has `source_card` and `kind` (SmallChoice/CountrySelect/CardSelect), but these are not encoded in the features. The model sees the same board state regardless of whether it's choosing its main action or responding to an opponent's Grain Sales to Soviets.

3. **Whether this is the actor's own AR or a mid-opponent-event choice:** There is no feature distinguishing "it's your turn, pick a card+mode+targets" from "your opponent played a card and its event requires you to make a choice." The `acting_side` and `current_side` in the game state could differ during event resolution.

4. **Remaining actions this turn:** The model knows `ar` (current action round index) and could infer remaining actions from `turn`, but it doesn't explicitly know how many cards remain to play. Cards played so far this turn would be useful context.

5. **Headline context:** During headline phase, both players choose simultaneously. The model doesn't know if the opponent has already been assigned a headline (in the simultaneous structure, both choose before either fires). It doesn't know whether it's choosing a headline or responding to a headline event.

**Impact:** This information gap means the model applies the same policy regardless of whether it's picking a headline card, making its 3rd action round play, or responding to an opponent event that gives it a choice. This almost certainly costs significant playing strength, especially for:
- Headline card selection (should heavily weight scoring cards and high-impact events)
- Bear Trap/Quagmire escape decisions (need to know it's a trap escape, not a normal play)
- Grain Sales / Lone Gunman style decisions (selecting cards to reveal/give)
- Event-triggered country selections (Brush War target, Junta target, etc.)

**Recommended new features (4-6 scalars):**
- `game_phase`: {0=setup, 0.25=headline, 0.5=action_round, 0.75=cleanup, 1.0=gameover}
- `is_event_decision`: binary, 1 when choosing inside event resolution
- `source_card_id / 112`: which card triggered this decision (0 if normal AR)
- `decision_kind`: {0=normal_action, 0.33=small_choice, 0.67=country_select, 1.0=card_select}
- `cards_played_this_turn / 9`: how many cards actor has played already
- `opponent_cards_played_this_turn / 9`: same for opponent (public info)

### 4. Current Feature Inventory and Gaps

**Influence features (172 dims):**
- 86 USSR influence counts + 86 US influence counts (raw integers as float)
- Processed by: flat Linear(172, 128) or CountryEmbedEncoder (per-country MLP with regional pooling) or ControlFeatGNNEncoder (adds control status + 2-hop GNN)
- The GNN variant adds per-country binary control features and 42 region scoring scalars

**Card features (448 dims):**
- 4 x 112 binary masks: actor_known_in, actor_possible, discard_mask, removed_mask
- Processed by: flat Linear(448, 128) or CardEmbedEncoder (DeepSet with static card features: ops, side, era, scoring, starred)

**Scalar features (32 dims):**
- 11 core game state + 17 active effects + 2 Chernobyl + 2 ops modifiers

**Missing features that could help:**

| Feature | Dims | Priority | Rationale |
|---------|------|----------|-----------|
| Game phase | 1 | **HIGH** | Headline vs AR vs event-decision completely changes optimal play |
| Decision context (source_card, kind) | 3 | **HIGH** | Model needs to know what question it's answering |
| Cards played this turn (both sides) | 2 | MEDIUM | Helps reason about tempo and remaining actions |
| Opponent hand size | 1 | MEDIUM | Already in Observation struct, not passed to model |
| Headline opponent card (when revealed) | 1 | MEDIUM | After headlines fire, both cards are known |
| Cards remaining in deck (estimated) | 1 | LOW | Helps probability reasoning about draws |
| Previous action taken (card_id, mode) | 2 | LOW | Useful for event chains but adds complexity |
| Scoring card presence in discard | 7 | LOW | Which scoring cards have fired this turn |

**The actor_possible mask is duplicated as actor_known_in.** Looking at `fill_cards()` in `nn_features.cpp`, both `ptr[0:112]` and `ptr[112:224]` are filled with the same `hand` mask. The C++ `fill_cards` code uses `fill_card_mask(ptr, hand); fill_card_mask(ptr + kCardMaskLen, hand);` -- both slots get the actor's hand. In the Python learned_policy, similarly: `hand_mask + hand_mask + discard + removed`. The "actor_possible" slot (designed for the opponent's possible cards in hand knowledge) is currently just a copy of actor_known_in. This wastes 112 input dimensions. If opponent hand support masks were computed and passed here, the model would gain meaningful hidden-information reasoning capability.

### 5. Frozen Corpus Approach

**Proposal:** Generate a large corpus of self-play games between the best per-side models (best USSR model vs best US model), then iterate model architecture purely on this frozen dataset via BC (behavioral cloning) before doing expensive PPO.

**Pros:**
1. **Drastically faster iteration.** BC training on frozen data takes minutes on the RTX 3050. PPO iterations with 200 games/iter take much longer due to C++ rollout overhead.
2. **Controlled experiments.** Architecture changes (GNN vs Attn, hidden_dim, aux heads) can be compared on identical data. No confounding from different self-play opponents or exploration noise.
3. **Reproducible.** Same data, same splits, deterministic training -- perfect for ablation studies.
4. **Cheaper feature engineering.** New features can be added to the Parquet files and tested in BC without touching the C++ rollout pipeline.
5. **The infrastructure already exists.** `TS_SelfPlayDataset` + `train_baseline.py` patterns are well-established.

**Cons:**
1. **Distribution mismatch.** BC on frozen data optimizes for imitating a fixed policy, not for winning. The BC-best architecture may not be the PPO-best architecture because PPO explores off-policy states.
2. **Ceiling effect.** The frozen corpus quality caps the BC model's strength. If the best models play at Elo 1800, BC cannot exceed 1800.
3. **Feature not in corpus.** New features (decision context, phase) require re-generating the corpus if they weren't recorded during collection.
4. **BC -> PPO transfer gap.** Architecture that trains well in BC (low loss) may not fine-tune well in PPO (gradient dynamics differ). This was partially observed in the project history.

**Recommended hybrid approach:**
1. Generate a large frozen corpus (50K+ games) from the strongest checkpoint, recording ALL features including the proposed new ones.
2. Use this corpus for architecture A/B testing via BC: measure card_top1, mode_accuracy, value_brier.
3. Take the top 2-3 architectures and run short PPO chains (50 iterations each) to validate that BC ranking transfers.
4. Commit to the winner for the long PPO chain.

This is essentially the "BC before PPO for arch changes" rule from memory, applied systematically.

### 6. Side-Specific Models

**The problem:** PPO v299-v305 showed USSR WR collapsing from 57% to 21% while US WR rose from 27% to 39%. This anti-correlation suggests the shared trunk is being pulled in contradictory directions by the two sides' gradients.

**Current architecture options that address this:**
- `TSControlFeatGNNSideModel`: Already has separate value heads for USSR/US + a 32-dim learned side embedding. This is the most mature per-side architecture.
- `TSCountryAttnSideModel`: Same per-side value heads with attention country encoder.
- Side is only a scalar input `[10]` in the base model -- clearly insufficient.

**Analysis of fully separate models:**

| Approach | Pros | Cons |
|----------|------|------|
| Fully separate USSR/US models | No gradient interference; each side can specialize | 2x params, 2x training cost, no knowledge transfer |
| Shared trunk + separate heads (current SideModel) | Some specialization, knowledge transfer | Trunk gradients still mixed |
| Shared trunk + gradient scaling per side | Can weight-balance side contributions | Doesn't address trunk representation conflict |
| Shared trunk + per-side LayerNorm (like FiLM conditioning) | Trunk features adapt to side cheaply | Adds minimal params |

**The real question:** Is the anti-correlation a fundamental architectural problem or a PPO training dynamics problem?

Evidence suggests training dynamics:
- The anti-correlation appeared during a specific PPO chain (v299-v305), not consistently across all training.
- PFSP weight configuration (pfsp_exp) was identified as a cause of plateau/regression in earlier analysis.
- Self-play opponent selection heavily influences which side gets better training signal.

**Recommendation:**
1. First verify the SideModel variant (separate value heads) fixes the anti-correlation. The code exists but may not be in the active PPO chain.
2. If anti-correlation persists with SideModel, try **per-side advantage normalization** (normalize USSR and US advantages independently, not jointly). This is a 5-line change in the PPO update.
3. Fully separate models are overkill and lose knowledge transfer. The SideModel approach is the right middle ground.

### 7. Other Model-Level Ideas

#### 7a. Attention Over Cards (already exists as CardEmbedEncoder)

The `CardEmbedEncoder` uses a DeepSet (shared projection + masked sum per mask type). This is a reasonable starting point but could be extended:
- **Cross-attention between hand cards and board state:** Let card embeddings attend to country embeddings. This would let the model learn card-country affinity (e.g., De Gaulle -> France, Truman Doctrine -> Europe).
- **Card-to-card attention within hand:** Let cards in hand attend to each other. This captures combinatorial value (holding multiple scoring cards, card synergies).
- Cost: ~30K extra params, moderate complexity.

#### 7b. Graph Neural Networks Over Countries (already exists as ControlFeatGNNEncoder)

The 2-hop GNN with adjacency matrix is already implemented. The GNN showed +4-8pp vs counterfactual in earlier experiments (per memory `project_gnn_arch_results.md`). The key insight is that geographic adjacency matters for:
- Coup/realignment access
- Influence placement connectivity
- Domino-theory cascading control

The current GNN uses row-normalized adjacency. A potential improvement: **edge-typed GNN** where superpower connections have different weights than regular adjacency, or where BG-to-BG edges are weighted differently.

#### 7c. Transformer-Based Sequence Models

**Not recommended for the current setup.** The decision is not sequential within a single forward pass -- the model sees one board state and produces one action. Sequence modeling would only help if:
- The model saw a history of recent states/actions (trajectory transformer)
- The model autoregressively decoded the action (card, then mode, then country sequence)

Autoregressive decoding of the factorized action is interesting but adds significant inference complexity and latency, which conflicts with the batched MCTS pipeline.

#### 7d. PopArt or Adaptive Value Normalization

The value head predicts in [-1, 1] via tanh. With `final_vp/20` targets, most values cluster near 0. **PopArt normalization** (adaptive mean/variance tracking for the value head) could help the value function learn more precise predictions in the common range while still handling extreme outcomes.

#### 7e. Legal Action Embedding in Trunk

Currently the model produces logits and then external code masks to legal actions. The model trunk does not know which actions are legal. Passing the legal mask (or a summary of it) as an input feature could help the model concentrate representational capacity on distinguishing between legal options rather than wasting capacity predicting logits for illegal actions.

For example, a "num_legal_cards" scalar and "num_legal_modes" scalar would tell the model whether this is a forced play (1 legal card) or a wide-open choice.

#### 7f. Opponent Modeling / Hand Estimation Head

The `actor_possible` mask slot is currently wasted (duplicate of `actor_known_in`). An auxiliary head that predicts what cards the opponent holds (using the discard, removed, and own-hand masks as input) would:
1. Provide useful auxiliary loss signal for representation learning.
2. Eventually enable information-set reasoning (the model "imagines" opponent hands).
3. The target is available in self-play data (both hands are known to the collector).

This is a lightweight addition: `opponent_hand_head = nn.Linear(hidden_dim, 112)` with binary cross-entropy loss against the true opponent hand mask.

## Conclusions

1. **The biggest immediate win is adding decision context features** (game phase, decision kind, source card). The model currently cannot distinguish headline choices from action round plays from mid-event responses. This is a 3-6 scalar addition to `nn_features.cpp::fill_scalars()` and likely the single highest-value feature change.

2. **The `actor_possible` card mask slot is wasted** -- it duplicates `actor_known_in`. Replacing it with the opponent hand support mask would add meaningful hidden-information reasoning at zero extra dimensions.

3. **The frozen-corpus approach is strongly recommended** for architecture iteration. BC on frozen data is 10-100x faster than PPO for comparing architectures. Use it to screen candidates, then validate top picks with short PPO runs.

4. **The side-specific value head (SideModel) should be the default** for PPO training, not the baseline model. The code exists in `TSControlFeatGNNSideModel`. Verify it is being used in the active training chain.

5. **A lightweight "consequence predictor" auxiliary head** (predicting delta-VP, delta-DEFCON, delta-MilOps, opponent-event-fires) would teach the model game rules implicitly, at much lower cost than full next-state prediction.

6. **Model distillation in the compression sense is not useful** -- the model is already small. Search distillation (teacher MCTS -> student) is useful and partially implemented.

7. **Fully separate USSR/US models are not recommended.** The SideModel approach (shared trunk + per-side value heads + side embedding) is the right balance. If anti-correlation persists, per-side advantage normalization in PPO is a simpler fix.

8. **An opponent hand prediction auxiliary head** would provide useful representation learning signal and could be added cheaply (1 linear layer + BCE loss on opponent hand mask from self-play ground truth).

9. **Sequence/transformer models add latency without clear benefit** given the single-state-in, single-action-out inference pattern. Not recommended.

10. **Attention over cards (cross-attention to board state)** is a promising medium-term enhancement that could capture card-country affinities, but is lower priority than fixing the feature gaps in conclusions 1-2.

## Recommendations

1. **Immediate (1-2 days):** Add decision context features to `nn_features.cpp::fill_scalars()` and `dataset.py`:
   - game_phase (1 scalar)
   - is_event_decision (1 scalar)
   - source_card_id / 112 (1 scalar)
   - decision_kind (1 scalar)
   This requires extending SCALAR_DIM from 32 to 36 and regenerating training data.

2. **Immediate (1 day):** Replace the duplicated `actor_possible` mask with the actual opponent hand support mask in `fill_cards()`. This requires the support mask to be computed and available at feature extraction time.

3. **Short-term (3-5 days):** Generate a large frozen corpus (50K+ games) with ALL features including the new decision context. Use it to A/B test:
   - Baseline vs ControlFeatGNNSide (confirm GNN+Side is still best)
   - With vs without decision context features
   - With vs without opponent hand prediction auxiliary head
   - With vs without consequence predictor auxiliary head

4. **Short-term (1 day):** Verify that the active PPO training chain uses `TSControlFeatGNNSideModel` (separate value heads), not the base `TSBaselineModel`. If not, switch.

5. **Medium-term (1 week):** Add per-side advantage normalization to the PPO update loop. This is a simple change that may prevent the USSR/US anti-correlation observed in v299-v305.

6. **Medium-term (1 week):** Implement the opponent hand prediction auxiliary head and the consequence predictor head. Train on frozen corpus to validate they improve trunk representations.

## Open Questions

1. **Which model class is currently active in the PPO chain?** The `load_model()` function reads `model_type` from checkpoint args, but if the chain was started from a `baseline` checkpoint, it may still be using `TSBaselineModel` despite `TSControlFeatGNNSideModel` being available.

2. **Why is `actor_possible` a duplicate of `actor_known_in`?** Was there a plan to fill it with the opponent support mask that was never completed, or is this intentional for backward compatibility?

3. **Does the v299-v305 regression correlate with a specific model class switch?** The anti-correlation might be an artifact of switching architectures mid-chain rather than a fundamental problem.

4. **What is the actual distribution of decision types in self-play data?** How many steps are headline decisions, how many are mid-event choices (SmallChoice), and how many are normal AR decisions? This affects the priority of decision-context features.

5. **Has PopArt value normalization been tried?** The current tanh value head with final_vp/20 targets may have resolution issues near 0.
