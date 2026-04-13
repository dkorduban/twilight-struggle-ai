---
# Opus Analysis: Move Correctness Plan
Date: 2026-04-13T09:45:00Z
Question: Scoring cards played for ops (coup etc) — fix plan

## Executive Summary

The engine has a critical bug: **scoring cards are deliberately excluded from the draw deck** in `build_era_deck()` (both C++ `game_state.cpp:20` and Python `game_state.py:228`), meaning no scoring card is ever dealt to either player. This completely removes regional scoring — a core mechanic of Twilight Struggle — from all self-play games. The external analysis confirms that "no regional scoring card appears anywhere in the game record" across an entire 10-turn game. A secondary concern is that the model (v55) shows severe strategic weaknesses (USSR never coups, excessive realignment into Nigeria/Argentina, no global strategy), but these are downstream consequences of training without scoring cards rather than engine bugs in move legality. The legal-action generation itself is correct: `legal_modes()` properly prevents scoring cards (ops=0) from being played as ops, and opponent events fire correctly when playing opponent cards for ops.

## Findings

### 1. Scoring Card Issue

**Root cause**: `build_era_deck()` in both C++ and Python explicitly skips all cards with `is_scoring=true`:

- **C++ `cpp/tscore/game_state.cpp:20`**:
  ```cpp
  if (spec.is_scoring || static_cast<int>(spec.era) > static_cast<int>(era_max)) {
      continue;
  }
  ```
- **Python `python/tsrl/engine/game_state.py:228`**:
  ```python
  and not spec.is_scoring
  ```

This means the 7 scoring cards (Asia=1, Europe=2, Middle East=3, Central America=40, Southeast Asia=41, Africa=80, South America=82) are **never placed in the draw deck**, never dealt, and never appear in any hand. The comments even say "non-scoring draw-deck cards" as if this were intentional design.

**Impact**: Without scoring cards:
- Regional scoring never happens mid-game; only final scoring at Turn 10 applies.
- The "held scoring card = loss" rule is dead code.
- The strategic landscape is fundamentally different from real TS: there is no incentive to establish regional positions before scoring fires, no "scoring card held" pressure, no timing/hand management around scoring.
- All models trained on this engine have learned a game that is NOT Twilight Struggle.

### 2. Other Incorrect Moves from External Analysis

The external analysis (`long-prompts/game_log_v55_seed3_T1.txt-analysis.md`) identifies these issues:

**a) USSR never coups (policy weakness, not engine bug)**
- All 8 coups in the game are by the US. The USSR never coups once.
- The analysis correctly notes: "In the entire log, the USSR never spends an action round on a normal coup. Not once. That is crippling."
- This is a model/policy issue, not an engine legality bug. The engine correctly offers Coup as a legal mode.

**b) Excessive realignment into Nigeria and Argentina**
- Nigeria is targeted 27 times, Argentina 26 times.
- Both sides waste enormous action economy on two countries.
- This is a model/policy quality issue exacerbated by the absence of scoring cards (no incentive to diversify regionally).

**c) No scoring events at all**
- The analyst notes: "no regional scoring card appears anywhere in the game record."
- This is the direct result of Bug #1 above.

**d) Bizarre headline play**
- CIA Created (US card) in USSR hand, played via UN Intervention (correct usage of UN Intervention to cancel opponent event).
- Nuclear Test Ban played as headline for 3 VP (legal, but strategically questionable).

**e) Starred cards played for ops then reappearing**
- Warsaw Pact Formed played as Realignment T1, then reappears as Event T10.
- Fidel played as Place Influence T1, then reappears as Event T10.
- This is **correct behavior**: starred cards are only removed when played as EVENT. Playing for ops sends them to discard, where they get reshuffled. `handle_card_played()` at `step.cpp:213` confirms: `if (mode == ActionMode::Event && spec.starred)` removes, else discards.

### 3. Engine Legal Action Logic

The legal action generation is **mostly correct** for the cards that do appear:

- `legal_modes()` (`legal_actions.cpp:136-191`): Correctly gates ops modes behind `spec.ops > 0`, so scoring cards (ops=0) would only get `Event` mode. This is correct TS rules.
- `legal_cards()` (`legal_actions.cpp:123-134`): Returns all cards in hand (excluding unplayable China Card). No filtering by card type.
- Bear Trap/Quagmire handling (`legal_actions.cpp:170-177`): Correctly exempts scoring cards from trap restrictions (a trapped player MUST still play scoring cards).
- DEFCON restriction (`legal_actions.cpp:67-78`): Correctly restricts coup/realignment targets by region at lower DEFCON levels.
- `learned_policy.cpp:243`: Uses `legal_modes()` to mask model output, so legality is enforced even when the model predicts illegal modes.
- `apply_action_with_hands()` (`game_loop.cpp:718-726`): Correctly fires opponent events when playing opponent cards for ops.

**One potential issue**: Headline resolution order at `game_loop.cpp:852-858` uses raw `card.ops` for priority. If both headlines have equal ops, the tiebreaker is `static_cast<int>(lhs.side) > static_cast<int>(rhs.side)`, meaning US (side=1) goes before USSR (side=0). In official TS rules, **USSR always goes first in headline ties**. This is a minor bug.

### 4. Root Causes

1. **Scoring cards excluded from deck**: Likely an early development decision to simplify the engine before event implementations were ready. The comment in Python says "non-scoring draw-deck cards" as if it were by design. Never reverted.

2. **Model strategic weakness**: The model was trained on a game without scoring cards, so it never learned the fundamental TS strategy of building regional positions before scoring fires. Without scoring pressure, the optimal strategy degenerates to VP-event fishing and local skirmishes.

3. **Headline tiebreak**: Minor coding error — `>` comparison on Side enum gives wrong ordering.

## Conclusions

1. **CRITICAL**: Scoring cards are excluded from the draw deck in both C++ and Python engines. This is the single most impactful correctness bug in the engine — it removes a core game mechanic entirely.
2. **CORRECT**: The `legal_modes()` function properly prevents scoring cards from being played as ops. The user's initial hypothesis (scoring cards played as ops for coups) is not an engine legality bug — the real issue is that scoring cards never appear at all.
3. **CORRECT**: Opponent events fire correctly when playing opponent cards for ops.
4. **CORRECT**: Starred cards played for ops go to discard (not removed), and can reappear after reshuffle.
5. **MINOR BUG**: Headline tiebreak gives US priority instead of USSR when ops are equal.
6. **POLICY WEAKNESS**: USSR never coups, excessive Nigeria/Argentina fixation — downstream of training without scoring cards.
7. **All models trained to date (v1-v55+) have been trained on a fundamentally different game** that lacks regional scoring. Fixing this bug will require retraining from scratch, as the entire learned value landscape will change.

## Recommendations / Fix Plan

### Fix 1: Include scoring cards in draw deck (CRITICAL)

**C++ `cpp/tscore/game_state.cpp:20`** — Remove the `spec.is_scoring` exclusion:
```cpp
// BEFORE:
if (spec.is_scoring || static_cast<int>(spec.era) > static_cast<int>(era_max)) {
    continue;
}
// AFTER:
if (static_cast<int>(spec.era) > static_cast<int>(era_max)) {
    continue;
}
```

**Python `python/tsrl/engine/game_state.py:225-231`** — Remove `not spec.is_scoring`:
```python
# BEFORE:
return [
    cid for cid, spec in cards.items()
    if cid != _CHINA_CARD_ID
    and not spec.is_scoring
    and int(spec.era) <= era_max
    and cid not in exclude
]
# AFTER:
return [
    cid for cid, spec in cards.items()
    if cid != _CHINA_CARD_ID
    and int(spec.era) <= era_max
    and cid not in exclude
]
```

Also update the docstring on line 217-222 to remove "non-scoring".

### Fix 2: Fix headline tiebreak (MINOR)

**`cpp/tscore/game_loop.cpp:858`** — Change tiebreak to favor USSR:
```cpp
// BEFORE: US (side=1) goes first
return static_cast<int>(lhs.side) > static_cast<int>(rhs.side);
// AFTER: USSR (side=0) goes first
return static_cast<int>(lhs.side) < static_cast<int>(rhs.side);
```

### Fix 3: Verify scoring card event implementations exist

Check that `apply_event()` in `step.cpp` and `apply_scoring_card()` in `scoring.cpp` correctly handle all 7 scoring cards. Current code at `step.cpp:241-252` delegates to `apply_scoring_card()` which appears functional. Verify with tests.

### Fix 4: Verify mid-war / late-war scoring card injection

`advance_to_mid_war()` and `advance_to_late_war()` both call `build_era_deck()` which currently excludes scoring cards. After Fix 1, mid-war scoring cards (Central America=40, Southeast Asia=41, Africa=80, South America=82) will correctly enter the deck at turn 4.

### Fix 5: Add scoring-card-held end-of-turn enforcement tests

The end-of-turn check at `game_loop.cpp:1167-1181` exists but was previously dead code. After Fix 1, this path needs test coverage.

### Fix 6: Retrain all models

After fixing the engine, all existing checkpoints are invalid. The training pipeline must restart from BC on heuristic games that now include scoring cards, then PPO self-play. This is a full reset of the model lineage.

## Regression Tests to Add

1. **test_scoring_cards_in_deck**: After `reset_game()`, verify that Early War scoring cards (1, 2, 3) appear in the combined deck+hands. After `advance_to_mid_war()`, verify Mid War scoring cards (40, 41, 80, 82) are in deck+hands+discard.

2. **test_scoring_card_only_event**: For each scoring card, call `legal_modes()` and verify the only returned mode is `ActionMode::Event`.

3. **test_scoring_card_not_ops**: Attempt to create an `ActionEncoding` with a scoring card and `ActionMode::Coup` / `Influence` / `Realign` / `Space`, and verify it is not in `enumerate_actions()` output.

4. **test_scoring_card_held_loss**: Set up a game state where one side holds a scoring card at end of turn. Call `end_of_turn()` and verify the holding side loses.

5. **test_scoring_card_fires_correctly**: For each scoring card, set up a board position and verify `apply_scoring_card()` returns the correct VP delta.

6. **test_scoring_card_trap_exemption**: With Bear Trap active for USSR, put a scoring card in USSR hand. Verify `legal_modes()` returns `[Event]` for the scoring card (exemption from trap).

7. **test_headline_tiebreak_ussr_first**: Set up two headlines with equal ops. Verify USSR's headline resolves first.

8. **test_full_game_with_scoring**: Run a full 10-turn game with heuristic policies and verify at least one scoring event fires during the game (not just final scoring).

9. **test_scoring_card_count_in_deck**: Verify exactly 3 Early War scoring cards in initial deck, exactly 7 total after late-war transition.

10. **test_reshuffle_includes_scoring**: Play a scoring card (goes to discard since non-starred... wait, scoring cards should go to discard after event). Verify it reappears after reshuffle. Note: Southeast Asia Scoring (41) is starred, so it should be removed after play.

## Open Questions

1. **Was the scoring-card exclusion intentional?** The comment says "non-scoring" explicitly. Was there a known issue with scoring card event implementations that prompted this? Need to verify `apply_scoring_card()` handles all 7 cards correctly before enabling.

2. **Shuttle Diplomacy interaction**: Card 74 (Shuttle Diplomacy) modifies next Asia/ME scoring. With scoring cards now in the game, verify this flag is correctly handled in `scoring.cpp`.

3. **Formosan Resolution + Asia Scoring**: Taiwan should count as a battleground for Asia Scoring when Formosan Resolution is active. Verify `is_scoring_battleground()` at `scoring.cpp:33` handles this (it does: `country_id == kTaiwanId && pub.formosan_active`).

4. **Training impact**: How much of the existing self-play data, match results, and Elo ratings are invalidated? Answer: all of it. Every model from v1 to v55+ was trained on a scoring-card-free game.

5. **DEFCON-1 rate**: Adding scoring cards changes the game dynamics significantly. The current DEFCON-1 rate (~6%) may change. Monitor after retraining.
---
