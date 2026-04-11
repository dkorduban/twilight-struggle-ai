# Opus Analysis: Recursive Turn Structure Modeling
Date: 2026-04-11 03:00:00 UTC
Question: How best to model nested/recursive decisions inside opponent's turn?

## Executive Summary

The current engine resolves ALL nested/mid-event player decisions randomly via `rng.choice_index()`. This affects 17 "Category C" cards that require hand access, plus Bear Trap/Quagmire discard, NORAD placement, and Olympic Games participate/boycott. The feature vector at these random-resolution points does NOT reach the neural network at all -- the decisions are fully resolved inside `apply_hand_event()` / `resolve_trap_ar()` / `resolve_norad()` before control returns to the game loop.

The recommended path is **Option B (continuation context) with Option E prioritization** -- a phased approach:

1. **Phase 1 (high Elo impact, moderate effort):** Surface Bear Trap/Quagmire discard and NORAD placement as real decision points in the game loop, using the existing model with a small `decision_context` feature addition (1 scalar or small embedding). These are the most frequent nested decisions and have the highest competitive impact.

2. **Phase 2 (medium impact):** Surface Missile Envy card selection and Grain Sales to Soviets card selection as decision points. These involve choosing from the opponent's hand, which is competitively important but less frequent.

3. **Phase 3 (low priority):** Everything else -- Olympic Games, Star Wars, Aldrich Ames, Blockade, etc. -- either has correct forced resolution, low competitive impact, or both. Keep random resolution indefinitely for these.

The existing flat decision sequence architecture (Option A) is nearly sufficient. The model already sees `bear_trap_active`, `quagmire_active`, `norad_active` in scalars[11-15]. The main gap is that these decisions never reach the model at all because they are resolved inside C++ helper functions before any policy function is called.

## Findings

### Current Engine State

The engine has two parallel game loops:

1. **Sequential game loop** (`run_action_rounds` in `game_loop.cpp`): Uses `PolicyFn` callbacks. Bear Trap/Quagmire are resolved randomly in `resolve_trap_ar()` (line 227-276). NORAD is resolved randomly in `resolve_norad()` (line 707-721). Category C card events are resolved randomly in `apply_hand_event()` (line 278-700).

2. **Batched MCTS/PPO game loop** (`advance_until_decision` in `mcts_batched.cpp`): Uses `BatchedGameStage` state machine. Bear Trap/Quagmire call `resolve_trap_ar_live()` which delegates to the same random resolver (line 2577). NORAD calls `resolve_norad_live()` which also uses random resolution (line 1161-1166).

**Critical observation:** In both loops, nested decisions are fully resolved before `queue_decision()` or `choose_action_with_config()` is ever called. The neural network is never consulted for these decisions. They are invisible in both training data and inference.

In the batched MCTS loop (lines 2562-2600), the ActionRound stage does:
```
1. Check trap -> resolve_trap_ar_live() -> random resolution, skip to next side
2. Check legal actions -> queue_decision() -> THIS is where NN is consulted
```

The trap resolution at step 1 happens BEFORE the decision is queued, so the trapped player never gets a decision point at all -- their entire AR is consumed by a random card discard.

### Decision Types That Need Nesting

Sorted by competitive impact and frequency:

| Card | ID | Decision | Current Impl | Impact | Frequency |
|---|---|---|---|---|---|
| **Bear Trap** | 47 | USSR discards 2+ ops card | Random from eligible | **HIGH** | ~15% of mid-war games |
| **Quagmire** | 45 | US discards 2+ ops card | Random from eligible | **HIGH** | ~15% of mid-war games |
| **NORAD** | 38 | US places 1 influence | Random from countries w/ US inf | **MEDIUM** | ~10% of games, triggers every USSR AR at DEFCON 2 |
| **Missile Envy** | 52 | Opponent reveals highest-ops card | Random among tied max-ops | **MEDIUM** | Opponent chooses which tied card, then plays it for ops |
| **Grain Sales to Soviets** | 68 | USSR selects card from hand | Random non-scoring card | **MEDIUM** | USSR gets ops from chosen card |
| **Olympic Games** | 20 | Both choose participate/boycott | `rng.bernoulli(0.5)` | **LOW** | Resolved as coin flip; real game is simultaneous |
| **Star Wars** | 88 | US picks card from discard | Random eligible discard | **LOW** | Choice of which event to replay |
| **Five Year Plan** | 5 | Random USSR discard | Random | **NONE** | Correctly random -- opponent has no choice |
| **Blockade** | 10 | US discards 3+ ops or loses W.Germany | Random from eligible | **LOW** | Usually forced (often only one eligible card) |
| **Aldrich Ames** | 95 | USSR sees US hand, discards card(s) | Random | **LOW** | Information gain is already modeled by hand masks |
| **CIA Created** | 84 | USSR hand revealed, US gets ops | Random ops allocation | **LOW** | US ops allocation, not card selection |
| **Lone Gunman** | 101 | US hand revealed, USSR gets ops | Random ops allocation | **LOW** | USSR ops allocation |
| **Kitchen Debates** | 98 | VP for controlled BGs | No player choice | **NONE** | Deterministic |
| **SALT Negotiations** | 46 | Player picks card from discard | Random | **LOW** | Happens once, moderate impact |
| **Shuttle Diplomacy** | 36 | USSR places inf in scored regions | Random | **LOW** | Random is reasonable |
| **UN Intervention** | 32 | Play opponent card for ops | Random ops allocation | **LOW** | The card PLAY is already a decision; the ops allocation is nested |

### Option Analysis

#### Option A: Flat Decision Sequence (current implicit approach)

**How it would work:** All decisions, including nested ones, appear as sequential steps in the trajectory. The `phasing` field tells the model whose turn it is.

**Implementation cost:** LOW for the concept, but MEDIUM to actually surface nested decisions as real decision points. The main work is modifying `resolve_trap_ar()`, `resolve_norad()`, etc. to yield back to the game loop instead of resolving inline.

**Pros:**
- No new model architecture needed
- The model already has `bear_trap_active`, `quagmire_active`, `norad_active` features (scalars[11-15])
- Legal action masking already handles which cards can be discarded
- PPO trajectory construction works as-is (just more steps per game)
- MCTS compatibility is natural (just more nodes in the tree)

**Cons:**
- Model sees the same feature vector for "normal card play" and "Bear Trap forced discard" -- no explicit context about WHY this decision is happening
- However, the presence of `bear_trap_active=1.0` in scalars IS distinguishing context
- Mode masking would need adjustment (trap discard doesn't have Influence/Coup/etc modes)

**Expected Elo impact:** +10-30 Elo from Bear Trap/Quagmire alone (currently losing ~3-5% EV from random discard of potentially critical cards). +5-10 from NORAD placement. Total ~+15-40 Elo.

**Verdict:** This is the RIGHT base approach. The flat sequence is architecturally sound because the model can already distinguish nested decision contexts via the effect-active features.

#### Option B: Continuation Context / Decision Stack

**How it would work:** Add a `decision_context` enum to the feature vector. Values like: NORMAL_AR=0, HEADLINE=1, BEAR_TRAP_DISCARD=2, QUAGMIRE_DISCARD=3, NORAD_PLACEMENT=4, MISSILE_ENVY_PLAY=5, GRAIN_SALES_SELECT=6, etc. Encoded as a small integer or one-hot in the scalar features.

**Implementation cost:** LOW on top of Option A. Adds 1-8 scalar features. Requires the engine to pass the context type through to `queue_decision()` or `fill_scalars()`.

**Pros:**
- Model can immediately distinguish decision types without learning to infer them from effect flags
- Composable: works even when multiple effects are active simultaneously
- Natural fit with the existing scalar feature vector (just extend from 32 to 33-40)
- Provides clean signal for future autoregressive sub-step decisions

**Cons:**
- Need to enumerate all nested decision types (finite, ~10-15 values)
- Minor schema change for training data (add decision_context column)

**Expected Elo impact:** +5-10 Elo on top of Option A's gains from better context discrimination.

**Verdict:** Best incremental improvement over Option A. Cheap to implement, clear signal.

#### Option C: Separate Policy Heads or Sub-Policies

**How it would work:** Dedicated heads for each nested decision type. E.g., a "trap discard" head that outputs card probabilities over 2+ ops eligible cards. A "NORAD placement" head that outputs country probabilities.

**Pros:**
- Clean specialization
- Each head has focused, interpretable inputs
- Can have different masking logic per head

**Cons:**
- Proliferation of heads (5-10 additional heads)
- Much less training data per head (trap discard happens ~2-5 times per game where it's active, vs ~14-16 normal action rounds)
- Model architecture grows; JIT export complexity increases
- Adds branching logic to both C++ and Python inference code
- MCTS node expansion needs to know which head to use

**Expected Elo impact:** Similar to Option B but with much higher implementation cost.

**Verdict:** Overkill. The card head already outputs probabilities over all cards; masking to 2+-ops cards for trap discard is trivial. A shared trunk with context features (Option B) achieves the same specialization through learned conditioning.

#### Option D: Full Game Tree with Alternating Players

**How it would work:** Model the game as a proper extensive-form game. When a nested decision occurs, the game tree branches for the opponent's choice, then returns to the current player.

**Pros:**
- Theoretically correct for imperfect-information games
- Handles any depth of nesting
- Compatible with CFR/MCCFR if we ever go that direction

**Cons:**
- Massive implementation complexity
- PPO is designed for single-agent trajectories; multi-agent alternating trajectories require fundamental changes to advantage estimation
- Credit assignment across player boundaries is hard (who gets credit for a trap discard outcome?)
- The game tree branching factor is already ~200-500 for normal play; adding mid-event branches explodes it further
- Most nested decisions are low-branching (trap discard: ~3-6 eligible cards) -- the overhead of full game-tree modeling isn't justified

**Expected Elo impact:** Potentially highest ceiling but years of implementation work away.

**Verdict:** Wrong tool for the job at this stage. Revisit only if pursuing MCCFR or perfect play research.

#### Option E: Random Resolution for Low-Impact, Full for High-Impact

**How it would work:** Only surface the 3-4 highest-impact nested decisions as real decision points. Everything else stays random.

**Pros:**
- 80/20 solution
- Minimal complexity increase
- Focused Elo gains from the decisions that matter most

**Cons:**
- Still inaccurate for some situations
- Need to identify the correct threshold

**Expected Elo impact:** +15-40 Elo from doing Bear Trap/Quagmire + NORAD correctly.

**Verdict:** This is the right PRIORITIZATION strategy, combined with Option A+B for implementation.

### Feature Vector Gap Analysis

**What the model sees at nested decision points today:**

Nothing. Nested decisions are invisible to the model. They are resolved entirely inside C++ helper functions (`resolve_trap_ar`, `resolve_norad`, `apply_hand_event`) before the model is ever consulted.

**What the model WOULD see if we surfaced these decisions (Option A):**

The existing feature vector already contains strong contextual signals:

| Feature | Index | Information |
|---|---|---|
| `bear_trap_active` | scalar[11] | 1.0 when USSR is trapped |
| `quagmire_active` | scalar[12] | 1.0 when US is trapped |
| `norad_active` | scalar[15] | 1.0 when NORAD is active |
| `phasing` | scalar[10] | Which side is deciding |
| `ar` | scalar[9] | Current action round (normalized) |
| `actor_known_in` | cards[0:112] | Which cards the actor holds |

**Gap 1: No explicit decision_type signal.** The model must infer from `bear_trap_active=1` + `phasing=USSR` that this is a trap discard, not a normal play. This is learnable but adds burden.

**Gap 2: Mode masking for trap discard.** A trap discard doesn't have the normal mode choices (Influence/Coup/Realign/Event/Space). The card head should produce a probability over eligible cards (2+ ops, non-scoring), and the mode head should be masked to a single "Discard" mode or ignored entirely. The current mode vocabulary (`ActionMode` 0-4) doesn't include a "Discard" option.

**Gap 3: NORAD placement is influence-only.** The decision is "which country to place 1 US influence on" -- this is exactly the country head output. But the card head and mode head are irrelevant. Need to either add a dummy card/mode or mask them out.

**Gap 4: Legal mask differences.** Trap discard eligible cards are: in-hand, non-China, non-scoring, 2+ ops. This is a different mask than normal play legality. The engine's `legal_cards()` function doesn't cover this case.

**Recommended feature additions for Phase 1:**

1. Add `decision_context` scalar (index 32 or extend to 33): integer enum {0=normal_ar, 1=headline, 2=trap_discard, 3=norad_placement}
2. Add `ActionMode::Discard = 5` for trap discard steps (or reuse Event mode with special masking)
3. Modify `resolve_trap_ar_live()` to yield a decision to the game loop instead of resolving inline
4. Modify `resolve_norad_live()` similarly
5. Add `legal_trap_discard_cards()` helper for proper masking

## Conclusions

1. **The current architecture (flat decision sequence) is fundamentally correct for this problem.** Twilight Struggle's nested decisions are shallow (max depth 2, rarely 3) and always involve a single player making a single choice. There is no deep recursion or simultaneous play that requires a tree-structured representation.

2. **The highest-priority fix is not architectural but operational: surface nested decisions as real decision points.** Currently, Bear Trap/Quagmire discard, NORAD placement, and Missile Envy are resolved by `rng.choice_index()` inside C++ helpers, completely bypassing the neural network. This is the #1 source of suboptimal play in these situations.

3. **The existing feature vector is ~80% sufficient.** The active-effect booleans (scalars 11-27) already encode the context needed to distinguish nested decisions from normal play. Adding a single `decision_context` scalar would close the remaining 20% gap and allow the model to specialize without separate heads.

4. **Option B (context features) on top of Option A (flat sequence) with Option E (phased prioritization) is the clear winner.** It requires:
   - Modest C++ changes: modify `resolve_trap_ar_live` and `resolve_norad_live` to yield decisions instead of resolving
   - Modest feature changes: add 1 scalar for decision_context
   - Modest Python changes: add decision_context to Parquet schema and dataset loader
   - Zero model architecture changes (the trunk and heads work as-is)

5. **Separate policy heads (Option C) and full game tree (Option D) are overkill.** The card head + legal mask already handles "which card to discard" naturally. The country head + legal mask already handles "where to place influence" naturally. No new heads are needed.

6. **Bear Trap/Quagmire discard is the single highest-value target** because: (a) it happens multiple times when active (every AR until escaped), (b) the choice of which card to burn has huge EV implications (discarding a scoring card vs a low-value card), and (c) it's currently purely random.

## Recommendations (ordered by impact/effort)

### 1. Surface Bear Trap / Quagmire as real decision points [HIGH impact, MEDIUM effort]

**Elo estimate:** +10-30

Modify `resolve_trap_ar_live()` in `mcts_batched.cpp` to:
- Set a new `BatchedGameStage::TrapDiscard` stage
- Queue a decision with the trapped player as the deciding side
- Mask cards to: in-hand, non-China, non-scoring, 2+ ops
- After the model picks a card, proceed with the d6 roll to escape

This requires adding a `TrapDiscard` stage to the `BatchedGameStage` enum and handling it in `advance_until_decision()`. The sequential game loop (`run_action_rounds`) needs similar changes to call the policy function instead of random selection.

Files to modify:
- `cpp/tscore/mcts_batched.cpp` -- add TrapDiscard stage, queue decision
- `cpp/tscore/game_loop.cpp` -- modify `resolve_trap_ar()` to accept a PolicyFn
- `cpp/tscore/game_loop.hpp` -- add BatchedGameStage::TrapDiscard
- `cpp/tscore/nn_features.cpp` -- optionally add decision_context scalar

### 2. Surface NORAD as a real decision point [MEDIUM impact, LOW effort]

**Elo estimate:** +5-10

Modify `resolve_norad_live()` to queue a decision for the US player. The decision is: which country (with existing US influence) to add +1 to. This maps directly to the country head output.

Files to modify: same as #1 plus a `NORADPlacement` stage.

### 3. Add decision_context feature [LOW-MEDIUM impact, LOW effort]

**Elo estimate:** +5-10 (improves learning speed for nested decisions)

Add scalar[32] = decision_context enum value. Update `fill_scalars()` in `nn_features.cpp`. Update `SCALAR_DIM` from 32 to 33. Update Parquet schema and Python dataset loader.

This is a breaking change for existing checkpoints but is worth doing alongside #1/#2 since those already require retraining.

### 4. Surface Missile Envy card selection [LOW-MEDIUM impact, MEDIUM effort]

**Elo estimate:** +3-8

Missile Envy (card 52): opponent must reveal and play their highest-ops non-scoring card. When there are ties, the opponent chooses which tied card to reveal. Currently random among ties. Making this a real decision for the opponent would improve play quality in ~5% of games.

### 5. Surface Grain Sales to Soviets card selection [LOW impact, MEDIUM effort]

**Elo estimate:** +2-5

Card 68: US shows USSR their hand, USSR picks a card, US plays that card's ops for any purpose. Currently the USSR card selection is random. Making this a real decision for USSR would marginally improve play.

### 6. Keep everything else random [indefinitely]

Olympic Games (simultaneous choice), Star Wars (pick from discard), Five Year Plan (truly random), Blockade (usually forced), Aldrich Ames (information gain, not action), Kitchen Debates (no choice), and all ops-allocation sub-decisions within events. The competitive impact of modeling these is negligible (<1 Elo each) and not worth the implementation complexity.

## Open Questions

1. **Mode vocabulary for trap discard:** Should we add `ActionMode::Discard = 5`, or reuse the card head output with mode masked to a single value (e.g., Event)? Adding a new mode is cleaner but changes the action encoding schema.

2. **PPO trajectory accounting:** When Bear Trap consumes an AR, the trapped player's AR count should still decrement. Currently the trap resolution is invisible in trajectories. How should this step be counted for PPO value estimation -- is it a "wasted" step or does it carry its own value estimate?

3. **MCTS handling of nested decisions:** In MCTS, a Bear Trap discard should be a decision node in the tree. But whose perspective is the value estimate from? The trapped player's value head should evaluate the resulting state. This is straightforward if we treat it as a normal decision for the trapped side.

4. **Opponent modeling in PPO self-play:** When the learned side is USSR and Bear Trap fires, the model must act as the trapped USSR. When the learned side is US and Quagmire fires, same thing. But what about when the OPPONENT is trapped? If we use `greedy_nn_opponent` mode, the opponent model handles it. If using heuristic opponent, we need a heuristic for trap discard (currently random, should at least prefer discarding low-value cards).

5. **Training data retrocompatibility:** Surfacing trap/NORAD decisions changes the step count per game and adds new decision types to training data. Old self-play data won't have these steps. This is fine for PPO (which retrains from scratch each iteration) but affects BC/distillation datasets.

6. **decision_context vs effect flags:** Is the explicit `decision_context` scalar actually needed, or can the model infer the context from `bear_trap_active + phasing + legal_mask`? Empirically testing with and without the context feature would answer this, but the feature is so cheap to add that the question may not be worth running an experiment over.
