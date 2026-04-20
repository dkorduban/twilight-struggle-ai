# Opus Analysis: Engine Step Design for Mid-AR Side Changes
Date: 2026-04-18 UTC
Question: Design a clean engine.step(state, policy) interface that replaces callbacks, handles all choices until side change, supports sub-choices with sequential policy calls, and encodes sub-AR context for the model.

## Executive Summary
Replace the in-place `PolicyCallbackFn` with an explicit **DecisionFrame stack** carried on `GameState`, driven by a resumable **state-machine `engine.step(state, action)`** rather than C++ coroutines. Every decision — top-level AR card choice, event sub-choices, forced discards, setup placements, Norad, Quagmire, CMC cancel, Glasnost budget, headline — becomes a `DecisionFrame` popped and pushed by the engine; the model always consumes a uniform `(Observation, DecisionFrame)` pair. Keep the output-reuse optimisation by letting a single `BatchOutputs` tensor bundle (card, mode, country, card-select, small-choice, value) be reused across consecutive frames of the same AR when the observation cache is still valid; when a frame changes the acting side or mutates the public state, emit a new NN forward. Autoregressive card→mode→country remains a *policy-head factorisation* for a single top-level frame, not a sub-choice — that distinction must be preserved to keep the engine free of model concerns.

## Findings

### 1. Current architecture and its pain points

**Callback wiring.** `PolicyCallbackFn` (`cpp/tscore/policy_callback.hpp`) is a `std::function<int(const PublicState&, const EventDecision&)>` threaded *downward* through every engine routine:

- `apply_action` (`step.cpp:1270`) → `apply_event` (`step.cpp:266`) → ~50 `choose_option/choose_country/choose_card` call sites inside the giant card switch.
- `apply_action_with_hands` (`hand_ops.cpp:788`) → `apply_hand_event` (`hand_ops.cpp:200`) for Cat-C cards (Five Year Plan, Blockade, Missile Envy, Our Man in Tehran, Aldrich Ames, Ask Not, AWACS, etc.).
- `execute_deferred_ops` (`hand_ops.cpp:610`) for EventFirst ops-action picking, which **overloads** `DecisionKind::SmallChoice` to mean "pick an index into an enumerated `ActionEncoding` list" — a fragile semantic hack.
- `resolve_trap_ar` (`hand_ops.cpp:697`), `resolve_cuban_missile_crisis_cancel` (`hand_ops.cpp:749`), `resolve_norad` (`game_loop.cpp:134`), `resolve_glasnost_free_ops_live` (`game_loop.cpp:604`), `run_setup_phase` (`game_loop.cpp:738`).

**Data-flow pain points** (concrete, observed in code):

1. **Sub-choice context is lossy.** `EventDecision` carries only `source_card`, `kind`, `n_options`, `acting_side`, `eligible_ids[]`. There is no "step index within event", no "ops budget remaining", no "why am I being asked", no "which card/event triggered the parent". The model has to infer sub-AR context from the pre-action `PublicState` alone. E.g. for Chernobyl (`step.cpp:1168`), the callback sees only `{source_card=97, kind=SmallChoice, n_options=6}` — no label that options 0-5 are Europe/Asia/ME/CentralAm/SA/Africa. That mapping lives implicitly in whichever side the head emits.
2. **Observation staleness.** `make_commit_policy_callback` (`mcts_batched.cpp:3489`) caches a single top-level forward; if a sub-choice lands on a head that wasn't emitted (e.g. Country head during a SmallChoice that is actually a deferred-ops chooser), it runs a *lazy* re-forward on the mutated `PublicState`. Semantically correct but the mechanism is ad-hoc.
3. **MCTS doesn't expand sub-choice nodes.** `FastNode` / `apply_tree_action` (`mcts_batched.cpp:311`) assumes one decision per AR; sub-choices are resolved *inside* `apply_action_live` via the commit callback, so the tree collapses entire event-resolution chains into a single edge with deterministic-looking results that actually hide several masked argmaxes. Dirichlet noise / UCB only operates at top level. For ISMCTS (priority-4 Month-3 item) this is a blocker: the tree must reveal sub-choice nodes.
4. **Serialization is broken.** The callback is a `std::function` closure referencing `slot`, `model`, `small_choice_logits`. There is no way to pickle a mid-event state, checkpoint self-play, resume on another worker, or teacher-search a sub-choice node.
5. **Hand/deck access during callbacks is unsafe.** Inside `apply_hand_event` (Cat-C), the callback receives only `PublicState`, not the acting player's hand — but the *decision itself* often depends on the hand (e.g. Missile Envy = choose my own hand's highest-ops card). The model currently gets no hand view at sub-choice time because `pending_observation` (`mcts_batched.cpp:239`) is snapshot at the top level.
6. **Explicit nesting is invisible.** Missile Envy (card 32) fires an opponent-event via `apply_hand_event` → the opponent's event's *own* sub-choices also route through the same callback. There is no "frame depth" or "parent frame" for the model to condition on.
7. **Logging / trace is single-edge per AR.** `StepTrace` captures one pre-state + one `ActionEncoding`. Sub-choices are invisible in `TracedGame.steps`, which means AWR/PPO datasets currently learn sub-choice behaviour only through the top-level value signal, not through supervised sub-choice targets.

### 2. Sub-choice taxonomy in Twilight Struggle

The engine today elides these into one callback protocol; a principled design names them:

| Frame kind | Trigger site | Current signature | What model actually needs |
|---|---|---|---|
| `TopLevelAR` | `advance_until_decision` queues `PendingDecision` | card × mode × countries | legal-action mask, full hand |
| `Headline` | `HeadlineChoiceUSSR/US` stages | card only, mode=Event | legal card mask, headline phase flag |
| `SetupPlacement` | `run_setup_phase` | 1 influence per iteration | remaining budget, valid region mask |
| `CountryPick` (event) | `choose_country` inside `apply_event` | eligible CountryIds | ops-remaining, step-index, "place/remove" |
| `SmallChoice` (direction) | `choose_option` — Warsaw Pact, Olympics, HIL, Chernobyl, Summit | n options | explicit option labels |
| `CardSelectFromHand` | `choose_card` — Missile Envy, Aldrich Ames, Our Man, Ask Not, Five Year Plan | eligible CardIds | criteria mask (ops ≥ 3, opponent side, non-scoring...), hand visible |
| `ForcedDiscard` | Quagmire, Bear Trap, CMC cancel-discard | eligible CardIds matching criteria | discard criteria, hand visible |
| `CancelChoice` | CMC cancel (yes/no) | 2 options | VP/DEFCON context |
| `FreeOpsInfluence` | Glasnost, The Reformer's influence loop | country choice per point | remaining points, "per-country ≤N" mask |
| `NoradInfluence` | Norad after USSR coup → DEFCON 2 | country with US influence | |
| `CoupTarget` / `RealignTarget` free-coup | OAS, Junta, Che, Yuri, Grain Sales | eligible CountryId | |
| `DeferredOps` (EventFirst) | opponent-event-then-my-ops | enumerated `ActionEncoding` indices | this is currently abused `SmallChoice` |
| `NestedEvent` (Missile Envy, Aldrich, Five Year Plan → opponent-event) | `fire_event_with_state` recursion | any of above, one level deeper | parent-frame card id, depth |

A principled refactor gives each its own `FrameKind` value plus shared scalar payload: `budget_remaining, step_index, parent_card_id, stack_depth, criteria_bits`.

### 3. Design options

**Option A — enriched callback.** Keep `PolicyCallbackFn`, fatten `EventDecision` with a `FrameKind` enum, budgets, criteria masks, parent. Low refactor cost; preserves perf. But it entrenches the impossible-to-serialize closure, blocks sub-choice MCTS nodes, and leaves logging single-edge.

**Option B — C++20 coroutines.** `engine.step` becomes `co_yield DecisionFrame`. Feels elegant for sequential narration but fights the rest of the codebase: MCTS clones `GameState` on every simulation (`sim_state` in `PendingExpansion`), and copying a live coroutine frame is awkward (you'd need stackless frames with their locals mirrored in the GameState). Makes pybind11 boundary harder. Reject.

**Option C — DecisionFrame stack on GameState + resumable state machine (RECOMMENDED).** This generalises the pattern already proven by `BatchedGameStage` in `mcts_batched.cpp`. Add:

```cpp
struct DecisionFrame {
    FrameKind kind;                  // TopLevelAR | SmallChoice | CountryPick | CardSelect | ...
    Side acting_side;
    CardId source_card;              // 0 for setup / headline
    uint8_t step_index;              // which of the N sub-steps
    uint8_t total_steps;             // for "pick 3 of 5"
    int16_t budget_remaining;        // ops / influence left, or -1
    uint8_t stack_depth;             // parent frame depth (nested events)
    CardId parent_card;              // card_id of the enclosing frame, 0 if top
    SubChoicePurpose purpose;        // place_inf / remove_inf / coup_target / direction / ...
    CardSet eligible_cards;          // bitset — O(1) mask, cheaper than vector<CardId>
    std::bitset<kCountrySlots> eligible_countries;
    uint8_t eligible_n;              // for SmallChoice, number of enum options
    uint16_t criteria_bits;          // "ops>=3", "opponent side", "non-scoring", "in-hand", ...
};

struct GameState {
    ...
    std::vector<DecisionFrame> frame_stack;   // top = next decision
    ...
};
```

The engine exposes:

```cpp
// Inspect the next decision without acting. None = game over or side-clean AR boundary.
const DecisionFrame* engine::peek(const GameState&);

// Apply the policy's chosen option.  For TopLevelAR this is a full
// ActionEncoding.  For sub-frames it's FrameAction { option_index OR card_id OR country_id }.
// Engine may push *more* frames onto the stack; may pop; may transition stage.
StepResult engine::step(GameState&, const FrameAction&, Pcg64Rng&);

struct StepResult {
    bool pushed_subframe = false;   // same side, another policy call needed
    bool side_changed = false;      // phasing flipped; caller may want to rebatch NN
    bool game_over = false;
    std::optional<Side> winner;
    PublicStateDelta delta;         // what changed (for incremental obs update)
};
```

Policies become `FrameAction policy(const GameState&, const DecisionFrame&, Pcg64Rng&)`. The outer driver is uniform:

```cpp
while (auto* frame = engine::peek(state)) {
    auto action = (frame->acting_side == Side::USSR ? ussr_policy : us_policy)(state, *frame, rng);
    auto result = engine::step(state, action, rng);
    if (result.game_over) break;
}
```

**Why this beats A and B:**

- Every decision — event sub-choice, Quagmire discard, Norad, CMC, setup, headline, top-level AR — goes through *one* interface. There is no privileged callback path.
- Frame stack is **part of state**: serialisable, cloneable, MCTS-compatible. `sim_state.frame_stack` is a `std::vector<DecisionFrame>` — trivially copyable.
- Sub-choice MCTS nodes fall out naturally: each `DecisionFrame` is one tree level. `FastNode` becomes frame-kind-aware; edges enumerate `FrameAction` options instead of top-level `ActionEncoding`. Dirichlet noise at root works unchanged.
- Logging becomes per-frame: `StepTrace` extends to `FrameTrace { frame, action, pub_before, pub_after }`. AWR/PPO datasets gain supervised sub-choice targets.
- The random / heuristic fallback is trivially default: a null policy → `uniform_random_frame_action(frame, rng)` helper that reads `frame.eligible_*` and picks.

**Frame-stack mechanics (the only genuinely tricky part):**

`apply_event` no longer resolves sub-choices inline. Instead, a card's event handler is a small state machine that *pushes* frames and reads previously-resolved ones. Two implementation patterns exist:

(i) **Resumable handler with "event program counter"**: each card gets a handler function + a small `EventCursor` (a few bytes on the GameState saying "Warsaw Pact, at step 2 of 4, already chose option 0 = remove"). The engine pops a sub-frame result, calls `resume_event(state, cursor, result)` which either resolves, pushes another frame, or completes. Requires rewriting every multi-choice event.

(ii) **Plan-expansion**: when an event first fires, precompute the *maximum* sequence of sub-frames it will need (Warsaw Pact: 1 direction frame + up-to-4 country frames). The engine iterates; each sub-frame is resolved one at a time; conditional branches (e.g. Warsaw Pact's branch on direction) are handled by having the direction frame's handler *truncate* and *replace* the subsequent frame plan. Simpler for the common "N countries from pool" shape but needs escape hatches for dynamic pools (pool shrinks as you remove influence).

Recommendation: **(i)**, with a per-card `EventHandler` trait that implements `std::optional<DecisionFrame> next_frame(const PublicState&, const EventCursor&)` and `void apply_frame_result(GameState&, EventCursor&, const FrameAction&)`. Verbose but matches the reducer-rule from CLAUDE.md: `next_state = reduce(prev_state, event)` — here `(prev_state, frame_cursor) → (next_state, new_cursor)`.

### 4. Encoding sub-AR context for the model

Extend `make_observation` (`nn_features.cpp`) to produce a per-frame feature block appended to the existing observation. Concrete additions:

**Categorical (one-hot or embedding):**
- `frame_kind` (~14 kinds) — lets the model learn specialised heads.
- `frame_purpose` (~10 values: place/remove/coup/realign/direction/discard/keep/draw/target_war/target_space).
- `source_card_id` (≤112) — embedding shared with discard/hand card embeddings.
- `parent_card_id` — 0 for top level.

**Scalar (continuous, appended to the 11 existing scalars in `fill_batch_slot_no_count`):**
- `step_index / total_steps` (normalised).
- `total_steps` raw (normalised).
- `budget_remaining / initial_budget` (influence/ops budget, for multi-point frames).
- `stack_depth` normalised (0, 0.5, 1.0 — rarely >2).
- `is_forced` flag (Quagmire/Bear Trap/CMC-cancel must-pay or pay-penalty).
- `matches_criteria_ratio` (#eligible / #hand or #accessible) — gives a legality-pressure signal.

**Mask tensors (already partially present):**
- `card_eligible_mask[kCardSlots]` — already plumbed via `eligible_cards`.
- `country_eligible_mask[kCountrySlots]` — already plumbed.
- `small_choice_mask[kMaxSmallChoiceOptions]` — new; currently implicit.
- `option_label_embedding[kMaxSmallChoiceOptions]` — new; encodes "option 0 = lower DEFCON, option 1 = raise" for HIL / Summit / Chernobyl / Warsaw Pact direction.

**Criteria bits (16-bit field):** `ops_ge_2, ops_ge_3, opponent_card, own_card, non_scoring, in_hand, in_discard, starred, battleground, is_war, region_europe, ...`. Fed as a dense 16-wide vector to the card-select head.

**Model-side implication:** the policy network needs a routing layer — given `frame_kind`, gate which head emits the output:
- `TopLevelAR` → card head + mode head + country head (autoregressive as today).
- `CardSelectFromHand / ForcedDiscard` → card head only, masked to `frame.eligible_cards`.
- `CountryPick / FreeOpsInfluence / NoradInfluence / CoupTarget` → country head, masked.
- `SmallChoice` → small-choice head (same as today), dimension = frame's `total_steps`.
- `CancelChoice` → small-choice head, 2-way, with forced-yes-no interpretation.

This matches the heads already present in `nn::BatchOutputs` (country_logits, card_logits, small_choice_logits, mode, value). The refactor doesn't need new heads; it needs clean routing.

### 5. Preserving the output-reuse optimisation

This is a non-trivial performance constraint the advisor flagged. The current commit-time callback reuses the top-level NN forward's slices across sub-choices (`mcts_batched.cpp:3519-3591`). A naïve re-run of the NN on every sub-frame multiplies inference cost by ~2-4× on event-heavy turns.

Proposed reuse rule:

```cpp
struct CachedInference {
    PublicStateHash obs_hash;   // includes pub + hand + holds_china + acting_side
    CardSet own_hand;
    BatchOutputs outputs;       // card_logits, country_logits, small_choice_logits, mode_logits, value
};
```

Invalidation contract:
- `pushed_subframe && !side_changed && !obs.pub changed materially` → reuse cache. (Sub-frames from the same event that don't mutate observable state: e.g. Warsaw Pact's direction frame → first country frame.)
- `side_changed` → invalidate, rebatch.
- `frame.acting_side != prior_frame.acting_side` → invalidate (hand changes).
- `delta.affects_features(obs)` → invalidate. Conservative default: any influence or DEFCON change.

In practice most multi-step events mutate `PublicState` *between* country-pick frames (because each pick applies influence), which means the cache hits less often than today. Two mitigations:

1. **Delayed-apply mode for multi-pick frames**: batch the influence application at the *end* of the multi-pick sequence. Pool-contraction is then deterministic on step_index, not on state mutation. Works for "pick K distinct from pool" but not for cost-sensitive influence placement (Glasnost).
2. **Explicit reuse_cache flag on the frame**: handler asserts "my next sub-frame's decision depends only on the same observation". Opt-in, conservative.

Combined effect: Warsaw Pact's 4 country picks cost 1 forward (direction) + 1 forward (countries, since pool mutates). Same as today. Chernobyl's 6-way direction costs 1 forward. Glasnost's 4 influence costs 4 forwards unless we enable delayed-apply — acceptable given Glasnost fires once per game.

**Net perf:** ≤10% more NN forwards per game on average (rough estimate from event frequency). Offset by removing the callback's `make_observation` allocation and the lambda capture overhead. Empirical validation required post-implementation.

### 6. Compatibility with MCTS tree search

The frame-stack design is **more** MCTS-compatible than the status quo, not less:

- Tree nodes map 1-1 to frames. `FastNode::edges` enumerate `FrameAction` options (for a `CountryPick` frame, edges are countries; for `SmallChoice`, edges are option indices). The existing K-sample expansion (`expand_from_raw_fast`, `mcts_batched.cpp:1217`) works unchanged — it already produces edges from a policy distribution over (card, mode, country) triples; it just needs to special-case by `frame_kind`.
- Virtual loss, PUCT, UCB — all operate on edges, no change needed.
- Dirichlet root noise only applies at the tree root; the root is whatever frame the search was invoked on (top-level AR today; can be any frame tomorrow).
- ISMCTS (Month-3 priority 4) becomes feasible: determinisations sample opponent hand, then MCTS runs over the frame stack including hidden-card reveals. Today, hidden-card sub-choices (Missile Envy picking opponent's hand) are invisible to MCTS.

**Policy-target question the refactor forces:** should MCTS visit counts at sub-choice nodes produce supervised targets for training, or only top-level visit counts? Recommend: **yes, train on all frames** — the model already has per-frame heads; this gives dense signal on sub-choice behaviour where today AWR/PPO only touches sub-choices through value gradient. But this changes dataset schema: `SearchResult` becomes per-frame not per-AR.

### 7. Autoregressive heads vs sub-choices — not the same thing

One top-level AR action `ActionEncoding{card_id, mode, targets[]}` factorises internally as P(card) · P(mode | card) · P(country1 | card, mode) · P(country2 | card, mode, country1). That is a **policy-head decomposition inside a single engine frame**. It exists so the action space is tractable (~10M flat) without conditioning ordering.

Sub-choices are **engine-visible branching**: between two sub-choice decisions the engine (a) mutates state, (b) may flip control to opponent (Missile Envy fires opponent event → opponent now picks from their options), (c) may draw RNG. The same card's event may push 0 sub-frames (Truman → deterministic) or 6 (Warsaw Pact → direction + 4 countries or 5 countries).

Keep them separate in the codebase:
- Policy heads and autoregressive decomposition live in `python/tsrl/models/` and in the TorchScript module's forward pass.
- Engine frames live in C++ `engine::step` and know nothing about heads.
- The bridge is: `frame_kind` tells the Python side which head to read; head outputs are masked by `frame.eligible_*`.

If future work wants card→mode→country as three engine frames (for MCTS to expand mode-choice and country-choice as separate tree levels), that is a *policy-configurable* refactor — the engine would gain three frame kinds `CardFrame, ModeFrame, CountryFrame` and `TopLevelAR` becomes their composition. Defer until ISMCTS forces the issue.

## Conclusions

1. The `PolicyCallbackFn` approach is the single largest structural obstacle to three Month-3 priorities: ISMCTS, league evaluation quality, and sub-choice behaviour cloning. Replacing it is worth one dedicated refactor.
2. A **DecisionFrame stack on `GameState`** driven by a resumable state machine (Option C) dominates enriched-callback (Option A) and C++ coroutines (Option B) on serialisation, cloneability, MCTS tree shape, and interface uniformity.
3. The new unified interface is `FrameAction policy(GameState&, DecisionFrame&, rng)` + `StepResult engine::step(GameState&, FrameAction, rng)`. The outer driver becomes a single `while (peek) step` loop for self-play, evaluation, and MCTS rollout.
4. Sub-AR context for the model needs exactly: `frame_kind`, `frame_purpose`, `source_card`, `parent_card`, `stack_depth`, `step_index/total_steps`, `budget_remaining`, `criteria_bits`, plus the eligible-entity masks. These extend `Observation`/`BatchInputs` by roughly 4-6 scalars + 3 categorical embeddings + one 16-bit criteria field.
5. Output-reuse must be explicit, not implicit. Introduce a `CachedInference` keyed on (obs_hash, hand, acting_side) and an opt-in `reuse_cache` flag on frames that provably don't mutate observation-affecting state.
6. Every existing sub-choice site reduces to one of ~10 frame kinds; `execute_deferred_ops`'s abuse of `SmallChoice` semantics gets its own `DeferredOps` kind.
7. Autoregressive action-head decomposition and engine sub-choices are orthogonal. Keep head factorisation in the Python policy module; keep sub-choice branching in the engine frame stack. Don't conflate.
8. MCTS visit counts at sub-choice nodes should become supervised training targets, which forces `SearchResult` and the dataset schema to become per-frame instead of per-AR.

## Recommendations

1. **Slice 1 (interface, no behaviour change).** Introduce `DecisionFrame`, `FrameAction`, `FrameKind` enum. Make `engine::peek` / `engine::step` wrappers around the existing `apply_action_live` + callback path. The callback internally adapts between old and new shapes. Ship behind a feature flag. Validate on golden-log replay hash.
2. **Slice 2 (frame stack plumbing).** Add `GameState::frame_stack`. Convert the *trivial* sub-choice sites first: setup placement (one frame per point), Glasnost (one frame per ops), Norad, CMC cancel, Quagmire discard. These have no nested events.
3. **Slice 3 (event handlers).** Rewrite the `apply_event` switch as per-card `EventHandler` traits with `next_frame` / `apply_frame_result`. Do this in groups of ~10 cards with parity tests comparing against the old path on a golden corpus. Budget: ~1 week of focused work given ~60 cards touch sub-choices.
4. **Slice 4 (model features).** Extend `Observation` with frame scalars + frame-kind embedding; update `fill_batch_slot_no_count`. Retrain baseline BC on frame-aware observation; confirm no regression vs current checkpoint.
5. **Slice 5 (MCTS alignment).** Make `FastNode::edges` frame-kind-aware. Re-enable Dirichlet noise at the root of whatever frame the search opens on. Verify parity with current top-level-only behaviour when frames are all TopLevelAR. This unblocks ISMCTS.
6. **Slice 6 (dataset schema).** Extend `StepTrace` → `FrameTrace` and the Parquet schema. Version bump. Keep old rows readable for one release cycle.
7. **Delete the callback.** Once all slices land, remove `PolicyCallbackFn` and `EventDecision` entirely. No silent shim.

## Open Questions

1. **Do headline frames appear on the stack simultaneously (both sides) or sequentially?** Today the batched MCTS queues `HeadlineChoiceUSSR` then `HeadlineChoiceUS` as two stages; the choices are hidden-at-choice-time but the engine reveals them together at resolution. The frame stack model most naturally handles this with two consecutive `Headline` frames whose observations *hide* the other side's pending choice — matches current semantics. Confirm this is what we want for Defector (108) which needs USSR's choice already committed before US chooses.
2. **Space race + pass semantics.** Is "pass" (no legal action, or choose not to play) a frame with `eligible_n=1` (the-empty-action), or do we keep the current "skip silently if no legal action" path? The latter breaks uniformity. Recommend explicit Pass frame.
3. **Output-reuse safety boundary.** What exact `PublicState` bits count as "affecting the observation"? Conservative (invalidate on any VP/DEFCON/influence/flag change) vs. aggressive (only invalidate on influence-topology change)? Needs a small test.
4. **Should the frame stack be a `std::vector` or a fixed-size `std::array` with depth bound?** Missile Envy → opponent event → that event's sub-choice → space-race drop = depth 3 worst case observed. A `std::array<DecisionFrame, 8>` + size is trivially cloneable and avoids heap allocation per frame push. Recommend fixed-size.
5. **Training signal at sub-choice frames during PPO.** PPO advantage estimation assumes one reward per timestep; with variable-count sub-frames per AR, do we credit each frame with the AR-level advantage or split? Recommend split by visit-count weight (MCTS) or uniform (BC), but validate empirically.
6. **Backward compatibility for existing checkpoints.** Frame-kind embedding adds input channels → state-dict mismatch. Need a BC re-train on the new observation before PPO can resume. This is a known cost, flagged here so it isn't surprising.
