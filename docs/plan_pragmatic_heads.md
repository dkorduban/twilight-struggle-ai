# Plan: Pragmatic Head Architecture — Policy-Driven Event Decisions

**Status:** Active — current main priority as of 2026-04-11
**Goal:** Replace random event resolution with policy-driven decisions, and upgrade
the country allocation head from K=4 MoS to score[c,k]+DP decoding.
**Time estimate:** 4-6 weeks total, staged
**Backward compatibility:** Required at every phase — new models must play old models

---

## Motivation

The engine resolves ~60% of event cards randomly (`rng.choice_index`). This is the
single largest expressiveness gap. The current model has card+mode+country+value heads
but **no head for event-specific decisions** (binary choices, event country targets,
card selections from discard). The country head's K=4 mixture-of-softmaxes also
cannot represent stacking (3+ ops in one country) or variable-cost placement.

Evidence: v44-v46 plateau at Elo ~2106; no further gains from PPO alone. Architecture
is the bottleneck, not training signal.

---

## Architecture Target (4 Head Families)

1. **CardHead** — choose one card from a masked candidate set
   - Existing: already works for AR hand choice, headline
   - Extend to: Bear Trap/Quagmire discard, SALT/Star Wars recovery, Aldrich Ames,
     Missile Envy, UN Intervention ops-card pairing, Grain Sales/Ask Not card choices

2. **SmallChoiceHead** — `Linear(hidden_dim, MAX_CHOICES)` with legal mask
   - NEW head, lightweight (~100 params)
   - Covers: Warsaw Pact (add vs remove), Olympic Games (boycott), Summit (DEFCON dir),
     How I Learned (DEFCON level), Wargames (invoke Y/N), Chernobyl (region),
     war targets (Brush War, Arab-Israeli, Korean, Indo-Pakistani)
   - `MAX_CHOICES = 8` (covers all known decision types)

3. **CountryAllocHead** — `score[c, k]` with bounded-knapsack DP decoding
   - UPGRADE from K=4 MoS (existing TSMarginalValueModel is 70% done)
   - Handles: influence placement, influence removal, event country targets
   - DP decoder: O(86 × budget × T_MAX) ≈ 1700 ops, negligible vs trunk
   - Existing `marginal_head = Linear(hidden_dim, 86 * T_MAX)` stays

4. **CardSubsetHead** — DEFERRED (only needed for Ask Not; use repeated CardHead)

### Resolution Frame Context

Each decision node carries:
- `source_card_id` (which event triggered this)
- `decision_kind` enum (SMALL_CHOICE, COUNTRY_ALLOC, CARD_SELECT)
- `budget` (ops count or max selections)
- Legal mask, per-country caps, cost curves
- Phase (headline/AR/event)

Encoded as a small context vector concatenated to trunk hidden state before the
decision-specific head. This lets the same head distinguish "place influence from
Marshall Plan" vs "place influence from main AR ops."

---

## Backward Compatibility Contract

**Hard requirement:** At every phase, the model must:
1. Produce all existing output keys (`card_logits`, `mode_logits`, `country_logits`,
   `country_strategy_logits`, `strategy_logits`, `value`)
2. Play against old models that use heuristic/random for event decisions
3. Work with existing benchmark, PPO, MCTS, and Elo pipelines

**Mechanism:**
- New output keys are added alongside existing ones (never removed)
- C++ engine gains a `PolicyCallback` interface: when present, calls the policy
  for event decisions; when absent, falls back to `rng.choice_index` (current behavior)
- Old TorchScript models don't produce new keys → engine uses random fallback
- New TorchScript models produce new keys → engine uses policy decisions

---

## Phase 1: SmallChoiceHead + Engine Callbacks ✅ COMPLETE (2026-04-11)

### Why first
- Highest ROI: 8 binary/option events become policy-driven
- Smallest engine change: replace `rng.choice_index(N)` with callback
- No new training data format needed — choices can be trained from self-play
- Measurable: each card's decision quality is directly testable

### 1a. Engine: Add PolicyCallback interface

**File: `cpp/tscore/policy_callback.hpp`** (NEW)
```cpp
// Callback interface for policy-driven decisions during event resolution.
// When null, engine falls back to random (backward compat).
struct EventDecision {
    CardId source_card;      // which card triggered this
    DecisionKind kind;       // SMALL_CHOICE, COUNTRY_SELECT, CARD_SELECT
    std::vector<int> legal;  // legal choice indices
    // Context fields for country selections:
    int budget = 0;
    std::vector<CountryId> eligible_countries;
};

enum class DecisionKind { SmallChoice, CountrySelect, CardSelect };

using PolicyCallbackFn = std::function<int(const GameState&, const EventDecision&)>;
```

**File: `cpp/tscore/step.cpp`** — Modify 4 `rng.choice_index` sites:
- Card 16 (Warsaw Pact): `rng.choice_index(2)` → callback(SMALL_CHOICE, {0,1})
- Card 48 (Summit): `rng.choice_index(2)` → callback(SMALL_CHOICE, {0,1})
  - 0 = DEFCON -1, 1 = DEFCON +1
- Card 49 (How I Learned): `rng.uniform_int(1,5)` → callback(SMALL_CHOICE, {1,2,3,4,5})
- Card 55 (Olympic Games): already in game_loop.cpp

**File: `cpp/tscore/game_loop.cpp`** — Modify select sites:
- Olympic Games boycott decision
- Chernobyl region choice
- War card target selections (Brush War, Arab-Israeli, Korean, Indo-Pakistani)
- Wargames invoke decision

Each site follows the pattern:
```cpp
// Before:
const auto choice = rng.choice_index(options.size());
// After:
const auto choice = policy_callback
    ? (*policy_callback)(gs, EventDecision{card_id, DecisionKind::SmallChoice, legal_indices})
    : rng.choice_index(options.size());
```

**Thread policy_callback through:**
- `apply_event(pub, card_id, side, rng)` → `apply_event(pub, card_id, side, rng, callback=nullptr)`
- `apply_action_live(gs, action, side, rng)` → add optional callback
- All callers that don't need policy (MCTS rollouts, heuristic) pass nullptr → random

### 1b. Model: Add SmallChoiceHead

**File: `python/tsrl/policies/model.py`**
```python
class SmallChoiceHead(nn.Module):
    MAX_CHOICES = 8
    def __init__(self, hidden_dim):
        super().__init__()
        self.proj = nn.Linear(hidden_dim, self.MAX_CHOICES)
    def forward(self, hidden):
        return self.proj(hidden)  # (B, MAX_CHOICES)
```

Add to TSBaselineModel (and TSMarginalValueModel):
```python
self.small_choice_head = SmallChoiceHead(hidden_dim)
# In forward():
out["small_choice_logits"] = self.small_choice_head(hidden)
```

### 1c. C++ inference: Read SmallChoiceHead output

**File: `cpp/tscore/nn_features.hpp`** — Add `small_choice_logits` to BatchOutputs
**File: `cpp/tscore/nn_features.cpp`** — Extract from model output dict (with fallback if key missing → backward compat)

### 1d. Wire PolicyCallback in self-play and MCTS

**Self-play/PPO rollout path:**
- `play_ismcts_matchup_pooled` / `play_mcts_vs_greedy` / `rollout_games_batched`:
  pass a PolicyCallback that does batch-1 inference on `small_choice_logits` +
  argmax with legal mask
- Record the choice in the Step (new field: `small_choice_target`, `small_choice_logprob`)

**Heuristic/benchmark path:**
- Pass nullptr → random (unchanged)

### 1e. Training: Add SmallChoice loss

**File: `scripts/train_ppo.py`**
- When step has `small_choice_target` field: compute cross-entropy loss on
  `small_choice_logits` masked to legal choices
- Weight: same as card_loss initially (can tune later)
- PPO advantage: use same advantage as other heads

### 1f. Tests and Verification

- **Unit test**: Warsaw Pact with callback always choosing "add" vs always "remove" —
  verify different game states result
- **Regression**: Run `ctest --test-dir build-ninja --output-on-failure` — all existing tests pass
- **Integration**: Train 20 iterations on existing pipeline — verify no crash, same
  loss trajectory on card/mode/value heads
- **Benchmark**: 200 games new-model vs old-model (old uses random for events) —
  verify it runs and new model doesn't regress

### Acceptance Criteria Phase 1
- [x] `ctest` passes (no C++ regressions) — 10/10 pass
- [x] `uv run pytest tests/python/ -q -n 0` passes — test_small_choice 14/14 pass
- [x] PPO training runs 20 iters without crash — v65 and v65_v55sc both completed 80 iters
- [x] New model plays old model (random fallback works) — panel eval v65 ≈ v55 (~51% H2H WR)
- [x] SmallChoice decisions visible in W&B logs — fixed bug: rollout_model_vs_model_batched was missing SmallChoice callback; now fires at ~0.92% of steps

---

## Phase 2: CountryAllocHead DP Upgrade (1-2 weeks)

### Why second
- Improves main-AR influence placement (every game, every turn)
- TSMarginalValueModel already predicts `delta[c, t]` for t=1..4
- Only missing piece: DP decoding replaces proportional allocation

### 2a. DP Decoder (Python, for training/inference)

**File: `python/tsrl/policies/dp_decoder.py`** (NEW)
```python
def bounded_knapsack_dp(
    scores: Tensor,     # (B, 86, T_MAX)
    budget: Tensor,     # (B,) — ops count
    legal_mask: Tensor, # (B, 86) — accessible countries
    cap: Tensor,        # (B, 86) — per-country max (default T_MAX)
    cost: Tensor,       # (B, 86) — per-country cost (1 or 2 for overcontrol)
) -> Tensor:            # (B, 86) — allocation per country
    """Differentiable bounded-knapsack via straight-through estimator."""
```

Two variants:
- **Inference**: exact integer DP, O(86 × budget × T_MAX) per sample
- **Training**: soft relaxation with straight-through gradient

### 2b. Wire DP into model inference path

**File: `cpp/tscore/learned_policy.cpp`** or `mcts_batched.cpp`
- Replace `build_action_from_country_logits()` (proportional allocation) with DP
- C++ DP implementation for inference speed

### 2c. Training target format

Currently: country_target is a list of country IDs (with repeats for multi-ops)
Stays the same — DP decoder produces the same format, just better allocation

### 2d. Tests
- **Unit test**: DP decoder produces valid allocations (sums to budget, respects caps)
- **Regression**: Train 20 iters, verify loss trajectory comparable or better
- **Benchmark**: 200 games DP-model vs MoS-model — expect DP wins

### Acceptance Criteria Phase 2
- [ ] DP decoder unit tests pass
- [ ] Influence placement quality measurably improves (A/B benchmark)
- [ ] No throughput regression >10% in PPO rollouts

---

## Phase 3: Event Country Targets via PolicyCallback (2-4 weeks)

### Why third
- Largest scope: ~30 `rng.choice_index` calls in game_loop.cpp for country selections
- Needs Phase 1 callback infrastructure + Phase 2 allocation head
- Each card needs individual attention to get the legal mask right

### 3a. Categorize all game_loop.cpp random country selections

Priority order (by frequency in typical games):
1. **High frequency**: Socialist Governments, Decolonization, COMECON, Marshall Plan,
   Voice of America, Junta follow-up, De-Stalinization, Truman Doctrine
2. **Medium frequency**: CIA Created, Puppet Governments, ABM Treaty,
   Alliance for Progress, Pershing II, Tear Down This Wall
3. **Low frequency**: South African Unrest, Ask Not, Our Man in Tehran, Star Wars,
   Aldrich Ames

### 3b. For each card, add EventDecision with COUNTRY_SELECT

Follow Phase 1 pattern but with `DecisionKind::CountrySelect`:
```cpp
const auto target = policy_callback
    ? eligible[(*policy_callback)(gs, EventDecision{card_id, DecisionKind::CountrySelect, ...})]
    : eligible[rng.choice_index(eligible.size())];
```

### 3c. Model side: condition CountryAllocHead on source_card_id

Add resolution-frame context:
```python
# Context embedding: card_id one-hot (110) + decision_kind (3) + budget (5)
self.context_encoder = nn.Linear(118, hidden_dim)
# In forward: hidden_conditioned = hidden + context_encoder(frame)
```

### 3d. Training: event-specific country labels from self-play

Self-play with Phase 1+2 model already makes policy-driven country choices.
Record (card_id, decision_kind, chosen_country, legal_mask) → train on these.

### Acceptance Criteria Phase 3
- [ ] All priority-1 cards use policy callback
- [ ] Elo gain measurable (+20 Elo or more vs Phase 2 model)
- [ ] No regression on existing benchmarks

---

## Phase 4: CardHead Extensions (1 week, low priority)

### 4a. Bear Trap/Quagmire card discard
- Currently: random card from hand
- Change: use existing card_head with hand mask (already works!)
- Engine change: add CardSelect callback to Bear Trap/Quagmire resolution

### 4b. SALT/Star Wars recovery from discard
- CardHead with discard pile mask

### 4c. Ask Not
- Repeated CardHead with STOP token (no CardSubsetHead needed)

---

## Verification Protocol (Every Phase)

1. **C++ regression**: `ctest --test-dir build-ninja --output-on-failure`
2. **Python regression**: `uv run pytest tests/python/ -q -n 0`
3. **Build**: `cmake --build build-ninja -j`
4. **Backward compat**: new model vs old model (200 games), both directions work
5. **Training**: 20-iter PPO run, verify loss curves on W&B
6. **Benchmark**: 200-game Elo vs previous best (v45)
7. **Specific card test**: for each modified card, unit test that callback overrides random

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| PolicyCallback overhead slows rollouts | LOW | MEDIUM | Profile; callback is one dict lookup per event |
| SmallChoice decisions don't improve Elo | MEDIUM | LOW | Even if Elo-neutral, removes randomness = better data |
| DP decoder training instability | MEDIUM | MEDIUM | Compare soft vs hard DP; fall back to proportional |
| Phase 3 scope creep (50 cards) | HIGH | HIGH | Strict priority order; batch in groups of 5-8 |
| Breaking existing checkpoints | LOW | HIGH | Never remove output keys; always fall back to random |
| MCTS tree explosion from multi-step events | MEDIUM | MEDIUM | Events are leaf-level in MCTS (resolve after action); not mid-search |

---

## Files To Create/Modify Summary

| Phase | File | Action |
|-------|------|--------|
| 1 | `cpp/tscore/policy_callback.hpp` | CREATE — EventDecision struct, callback typedef |
| 1 | `cpp/tscore/step.cpp` | MODIFY — 4 rng sites → callback |
| 1 | `cpp/tscore/game_loop.cpp` | MODIFY — ~8 rng sites → callback |
| 1 | `cpp/tscore/nn_features.hpp` | MODIFY — add small_choice_logits to BatchOutputs |
| 1 | `cpp/tscore/nn_features.cpp` | MODIFY — extract small_choice_logits |
| 1 | `python/tsrl/policies/model.py` | MODIFY — add SmallChoiceHead to models |
| 1 | `scripts/train_ppo.py` | MODIFY — add small_choice loss |
| 1 | `tests/cpp/test_small_choice.cpp` | CREATE — unit tests |
| 1 | `tests/python/test_small_choice.py` | CREATE — Python tests |
| 2 | `python/tsrl/policies/dp_decoder.py` | CREATE — DP allocation decoder |
| 2 | `cpp/tscore/dp_decoder.hpp` | CREATE — C++ DP for inference |
| 2 | `tests/python/test_dp_decoder.py` | CREATE — DP unit tests |
| 3 | `cpp/tscore/game_loop.cpp` | MODIFY — ~30 more rng sites |
| 3 | `python/tsrl/policies/model.py` | MODIFY — context conditioning |
| 4 | `cpp/tscore/game_loop.cpp` | MODIFY — Bear Trap, SALT, Star Wars |

---

## Current State

- PPO pipeline running autonomously (v54 from v45 checkpoint)
- v44-v46 plateau at Elo ~2106
- TSMarginalValueModel exists (70% of Phase 2 allocation head)
- Engine is 85% rules-accurate; 15% gap is player agency on events
- Phase 1 can start immediately — no blockers
