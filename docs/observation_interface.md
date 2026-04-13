# Observation Interface Contract

## Problem Statement

`mcts.cpp`, `mcts_batched.cpp`, and `ismcts.cpp` currently read
`GameState.hands[]` directly inside the search layer. That is acceptable for
full-information self-play, but it leaks hidden information into any path that
is supposed to model partial observability. In particular:

- Full-information MCTS wants exact opponent hands.
- ISMCTS wants only the acting player's observation plus a sampled hidden-state
  completion.
- The current code mixes those concerns by letting search code reach through to
  the full `GameState`.

The refactor target is to make the search layer depend on an observation object
first, and opt into full hidden state only in the places that explicitly need
it.

## Target Interface

```cpp
// What any agent can observe — no hidden state
struct Observation {
    PublicState pub;           // Full public board state
    HandKnowledge own_hand;    // Own hand (known to self)
    CardSet opponent_support;  // Opponent card support mask
};

// Full-info extension (for full-information MCTS/self-play)
struct FullStateView : Observation {
    CardSet opponent_hand;     // Complete opponent hand (hidden in real play)
};
```

The design intent is:

- Policy ranking, legal-action generation, and feature extraction should accept
  `Observation`.
- Full-information rollout and teacher-search tooling can opt into
  `FullStateView`.
- Determinization code should be the only layer that converts
  `Observation + support mask` into a sampled hidden hand.

## `hands[]` Access Audit

### `cpp/tscore/mcts_batched.cpp`

- `383`: `apply_tree_action()` removes the played card from the acting hand
  before calling `apply_action_live()`.
  Replacement: mutate `Observation.own_hand` for the acting side, and only use
  `FullStateView` when a full hidden-state transition is truly required.

- `528`, `633`: `collect_card_drafts_cached()` and
  `collect_compact_legal_cards()` feed `state.hands[to_index(side)]` into
  `legal_cards(...)`.
  Replacement: take `obs.own_hand` as an explicit input instead of reaching
  through `GameState`.

- `1408`, `1644`: expansion fallback paths call `choose_action(...)` with the
  acting side's full hand.
  Replacement: pass `obs.own_hand` for ordinary search, or
  `full_view.opponent_hand` only in the full-information branch.

- `1746`: `has_any_model_action_cached_exact()` scans the acting hand directly.
  Replacement: scan `obs.own_hand`.

- `2280`, `2296`, `2300`: cleanup logic checks for held scoring cards, discards
  every remaining hand card, and resets both hands.
  Replacement: keep cleanup at the state-transition layer, then expose updated
  observations after the transition rather than letting search inspect hidden
  hands directly.

- `2349`: `queue_decision()` snapshots the acting player's hand into
  `PendingDecision.hand_snapshot`.
  Replacement: snapshot `Observation.own_hand`.

- `2420`, `2509`: headline/action-round control flow calls
  `has_legal_action(slot.root_state.hands[...], ...)`.
  Replacement: use the acting observation's `own_hand`.

- `2458`, `2709`: trace recording writes the opponent hand snapshot into
  `StepTrace`.
  Replacement: keep this only in teacher/full-state tracing code, and separate
  it from the observation passed into search.

- `2522`, `2669`, `2688`, `3828`, `3848`: live decision resolution and greedy
  benchmark resolution remove the chosen card from the acting hand.
  Replacement: update `Observation.own_hand` in the decision pipeline, with the
  full-state mutation hidden behind a transition helper.

- `3160`, `3190`: batched NN expansion fills model inputs from the acting
  player's hand.
  Replacement: feature extraction should accept `Observation`.

- `3437`, `3640`: rollout / greedy action decoders enumerate playable cards from
  the acting hand.
  Replacement: decode from `obs.own_hand`.

- `3980`, `3991`, `4144`, `4154`, `4302`, `4311`, `4517`: matchup and rollout
  collection paths batch model inputs from `slot.root_state.hands[...]`.
  Replacement: batch `Observation` objects instead of whole `GameState`
  snapshots.

- `4348`, `4573`, `4718`, `4753`: rollout collectors serialize hand card IDs for
  training rows.
  Replacement: serialize `Observation.own_hand` for the actor, and treat any
  opponent-hand serialization as a deliberate full-state label path.

### `cpp/tscore/ismcts.cpp`

- `173`: `apply_tree_action()` removes the acting card from
  `state.hands[to_index(side)]`.
  Replacement: mutate the acting observation's `own_hand`, not raw search
  state.

- `303`: `collect_card_drafts()` calls `legal_cards(...)` on the acting hand.
  Replacement: use `obs.own_hand`.

- `398`, `645`: search fallback paths call `choose_action(...)` with the acting
  hand.
  Replacement: pass `obs.own_hand`.

- `839`, `855`, `859`: cleanup checks for scoring cards, discards all remaining
  hand cards, and clears both hands.
  Replacement: keep this logic in the full-state transition layer and rebuild
  observations after cleanup.

- `932`: `queue_decision()` snapshots the acting hand into
  `PendingDecision.hand_snapshot`.
  Replacement: snapshot `Observation.own_hand`.

- `997`, `1015`: committed actions remove the chosen card from the acting hand.
  Replacement: apply a transition helper that consumes `Observation.own_hand`
  for the actor.

- `1317`, `1386`: stage control checks `has_legal_action(...)` against the full
  hand.
  Replacement: use the acting observation's `own_hand`.

- `1402`: extra-action-round flow reads the acting hand to decide whether the
  side can act at all.
  Replacement: inspect `obs.own_hand`.

- `1473`: determinization setup reads the exact opponent hand size from the live
  game state.
  Replacement: derive the size from observation-safe metadata, for example an
  explicit public hand-size counter carried alongside `Observation`.

- `1590`: pending NN batch fill uses the acting full hand.
  Replacement: batch `Observation`.

- `1618`: `sample_determinization()` reads and rewrites the exact opponent hand.
  Replacement: this remains one of the few legitimate `FullStateView` /
  determinization-only call sites.

- `1760`, `1761`: the benchmark wrapper counts opponent cards directly from the
  full game state before launching ISMCTS.
  Replacement: pass the opponent hand size as explicit metadata derived outside
  the generic search interface.

## Migration Plan

Phase 3 can move this safely in small steps:

1. Introduce `Observation` and `FullStateView` as passive structs with no
   behavior changes.
2. Add helper constructors that derive `Observation` from `GameState` for the
   acting side, and `FullStateView` only where full hidden state is intentional.
3. Convert legal-action generation, feature extraction, and policy ranking
   helpers to take `Observation` instead of `GameState + hands[...]`.
4. Replace `PendingDecision.hand_snapshot` writes with observation snapshots.
5. Update batched MCTS and rollout batching to fill NN inputs from
   `Observation`.
6. Narrow ISMCTS determinization so that direct opponent-hand access lives only
   inside determinization helpers and teacher/full-state tracing.
7. Once all search-time reads are observation-mediated, make any remaining
   `hands[]` access a deliberate transition-layer or label-generation exception.
