# Spec: Sub-frame row emission in self-play collector

## Goal
The self-play collector (`collect_selfplay_rows_jsonl.cpp`) currently emits one
JSONL row per top-level AR action. Sub-frame decisions (country picks, card
selects, forced discards, small choices, Free-Ops influence, Norad, Deferred-Ops)
are made inside `apply_frame_ops_or_resolve` but (a) the trace harness passes
neither `policy_cb` nor `frame_log` so those decisions are RNG-driven in
collection mode, and (b) even if logged, nothing flows back to the collector.
This makes sub-frame targets invisible or actively misleading for BC/AWR
training.

This spec closes the gap with three commits, scope-bounded to the self-play
collector only:
1. Extend `DecisionFrame` with a `FrameAction chosen_action` field and populate
   it in `logged_frame_copy`.
2. Plumb `policy_cb` + `frame_log` through `play_game_traced_from_state_with_rng`
   and the three `apply_action_with_hands` / `apply_headline_event_with_hands`
   call sites, then attach the logged frames to each `StepTrace`.
3. In the self-play collector, construct a `PolicyCallbackFn` that wraps the
   same neural policy used as the top-level `PolicyFn`, and emit one additional
   JSONL row per logged sub-frame.

MCTS collector, validator trace, Python training code, and reducers are out of
scope.

## Files to create
- `tests/cpp/test_subframe_logging.cpp` — Catch2 tests for DecisionFrame
  `chosen_action`, `play_game_traced` sub-frame capture, and the collector's
  policy-callback wrapper.

## Files to modify
- `cpp/tscore/decision_frame.hpp` — add `FrameAction chosen_action` field to
  `DecisionFrame` (no reordering of existing fields).
- `cpp/tscore/hand_ops.cpp` — in `logged_frame_copy` (line 304) populate
  `logged.chosen_action = action`; keep existing `criteria_bits` SmallChoice
  encoding for backward compatibility.
- `cpp/tscore/game_loop.hpp` — add `std::vector<DecisionFrame> sub_frames` to
  `StepTrace`; extend `play_game_traced_fn` / related signatures to accept an
  optional `const PolicyCallbackFn*` and propagate it down.
- `cpp/tscore/game_loop.cpp` — update the three trace push-back sites (lines
  ~378, ~498, ~628) to (a) allocate a local `std::vector<DecisionFrame>
  frame_log`, (b) pass `policy_cb` and `&frame_log` to
  `apply_action_with_hands` / `apply_headline_event_with_hands`, and (c) move
  `frame_log` into `step.sub_frames` before push-back. Update
  `play_game_traced_from_state_with_rng` (~line 3783) to accept and forward the
  new `policy_cb` arg; keep a default-null overload so existing callers are
  unaffected.
- `cpp/tools/collect_selfplay_rows_jsonl.cpp` — construct a `PolicyCallbackFn`
  `subframe_cb` that wraps the same neural policy used for `base_policy`
  (lines 328–341 region); pass it into `play_game_traced_fn`; in the emission
  loop (~line 434), after emitting the top-level row, iterate
  `step.sub_frames` and emit one JSONL row per frame with the fields listed
  below.
- `tests/cpp/CMakeLists.txt` — register `test_subframe_logging.cpp` in the
  `test_tscore` executable source list.

## Interfaces / signatures

### 1. DecisionFrame extension
`cpp/tscore/decision_frame.hpp`:
```cpp
struct DecisionFrame {
    FrameKind kind = FrameKind::TopLevelAR;
    Side acting_side = Side::USSR;
    CardId source_card = 0;
    uint8_t step_index = 0;
    uint8_t total_steps = 1;
    int16_t budget_remaining = -1;
    uint8_t stack_depth = 0;
    CardId parent_card = 0;
    CardSet eligible_cards;
    std::bitset<kCountrySlots> eligible_countries;
    uint8_t eligible_n = 0;
    uint16_t criteria_bits = 0;
    FrameAction chosen_action{};   // NEW — populated by logged_frame_copy
};
```

`FrameAction` itself is unchanged (decision_frame.hpp:46–50):
```cpp
struct FrameAction {
    int option_index = 0;
    CardId card_id = 0;
    CountryId country_id = 0;
};
```

### 2. logged_frame_copy population
`cpp/tscore/hand_ops.cpp` (replace existing body, keep signature):
```cpp
DecisionFrame logged_frame_copy(
    const DecisionFrame& frame,
    std::vector<DecisionFrame>* frame_log,
    const FrameAction& action
) {
    auto logged = frame;
    if (frame_log != nullptr) {
        logged.stack_depth = frame_count(frame_log->size());
    }
    logged.chosen_action = action;  // NEW — always record chosen action

    if (logged.kind == FrameKind::SmallChoice) {
        const auto ops = std::max(0, static_cast<int>(logged.budget_remaining));
        const auto mode_index = std::clamp(
            action.option_index, 0,
            std::max(0, static_cast<int>(logged.eligible_n) - 1));
        const auto country_steps = mode_index == 2 ? 1 : ops;
        logged.step_index = 0;
        logged.total_steps = frame_count(
            static_cast<size_t>(std::max(1, country_steps + 1)));
        logged.criteria_bits = static_cast<uint16_t>(mode_index);
    }
    return logged;
}
```

### 3. StepTrace extension
`cpp/tscore/game_loop.hpp`:
```cpp
struct StepTrace {
    int turn = 0;
    int ar = 0;
    Side side = Side::USSR;
    bool holds_china = false;
    PublicState pub_snapshot;
    CardSet hand_snapshot;
    ActionEncoding action;
    int vp_before = 0;
    int vp_after = 0;
    int defcon_before = 0;
    int defcon_after = 0;
    CardSet opp_hand_snapshot;
    InlineDeck deck_snapshot;
    bool ussr_holds_china_snapshot = false;
    bool us_holds_china_snapshot = false;
    std::vector<DecisionFrame> sub_frames;  // NEW — logged sub-frames for this AR
};
```

### 4. play_game_traced signature extension
`cpp/tscore/game_loop.hpp`:
```cpp
// Existing overload kept; new parameter added with nullptr default so existing
// callers continue to work unchanged.
using PolicyCallbackFn = ::ts::PolicyCallbackFn;  // if not already in scope

TracedGame play_game_traced_from_state_with_rng(
    const GameState& start_state,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    const PolicyCallbackFn* subframe_cb = nullptr);
```

And `play_game_traced_fn` similarly.

### 5. Trace harness wiring (game_loop.cpp)
At each of the three `apply_action_with_hands` / `apply_headline_event_with_hands`
call sites inside the tracing loop:
```cpp
std::vector<DecisionFrame> frame_log;
auto [new_pub, over, winner] = apply_action_with_hands(
    gs, *action, side, rng, subframe_cb, &frame_log);
...
StepTrace step;
... // existing population
step.sub_frames = std::move(frame_log);
steps.push_back(std::move(step));
```

### 6. Collector PolicyCallbackFn construction
`cpp/tools/collect_selfplay_rows_jsonl.cpp`. The same neural-policy context
(model + features) that builds the top-level `base_policy` must build a
`PolicyCallbackFn` with the signature from `policy_callback.hpp:30`:
```cpp
using PolicyCallbackFn = std::function<int(const PublicState&, const EventDecision&)>;
```

Sketch (alongside the existing `base_policy` block, ~lines 328–341):
```cpp
PolicyCallbackFn subframe_cb =
    [&model, &features_ctx, &rng_ref](const PublicState& pub,
                                      const EventDecision& decision) -> int {
        // Build sub-frame feature tensor (reuse same feature extractor the
        // top-level policy uses, conditioned on decision.kind and eligible_ids).
        const auto scores = model.score_subframe(pub, decision, features_ctx);
        return argmax_over_eligible(scores, decision.eligible_ids,
                                    decision.eligible_n);
    };
```
Pass `&subframe_cb` into `play_game_traced_fn`. If the neural policy wrapper
does not already expose a `score_subframe` entry point, thread one through the
same way `base_policy` threads its top-level scorer (read the existing top-
level policy construction — do NOT invent a parallel scoring path).

### 7. Sub-frame JSONL row schema
For each frame in `step.sub_frames` (emitted immediately after the parent
AR row), write a new JSONL row with the parent AR's global state fields
(turn, ar, phasing, VP, DEFCON, MilOps, Space, influence, hands, etc.)
inherited unchanged, plus:
- `"row_kind": "subframe"` (top-level rows get `"row_kind": "ar"`)
- `"frame_kind"`: integer value of `DecisionFrame::kind`
- `"source_card"`: int
- `"parent_card"`: int
- `"step_index"`, `"total_steps"`, `"budget_remaining"`, `"stack_depth"`: int
- `"criteria_bits"`: int
- `"eligible_cards"`: array of card ids (expanded from `CardSet`)
- `"eligible_countries"`: array of country ids (expanded from bitset)
- `"eligible_n"`: int
- `"chosen_option_index"`, `"chosen_card"`, `"chosen_country"`: from
  `chosen_action`
- `"vp_after"`: inherited from parent AR's `vp_after` (sub-frames don't score)
- `"defcon_after"`: inherited from parent AR's `defcon_after`

Reuse the existing `targets_csv`, mask-writing, and state-snapshot helpers;
do NOT duplicate formatting code.

## Test cases (required)
File: `tests/cpp/test_subframe_logging.cpp`, Catch2 `TEST_CASE` pattern.

- `test_decision_frame_chosen_action_smallchoice`: construct a `SmallChoice`
  frame with `eligible_n = 3`, call `logged_frame_copy` with
  `FrameAction{option_index=2}`; assert `logged.chosen_action.option_index ==
  2` AND `logged.criteria_bits == 2` (backward-compat encoding preserved).
- `test_decision_frame_chosen_action_countrypick`: construct a `CountryPick`
  frame, call `logged_frame_copy` with `FrameAction{country_id=42}`; assert
  `logged.chosen_action.country_id == 42` AND other fields zeroed.
- `test_decision_frame_chosen_action_cardselect`: construct a `CardSelect`
  frame, call `logged_frame_copy` with `FrameAction{card_id=17}`; assert
  `logged.chosen_action.card_id == 17`.
- `test_traced_game_captures_subframes`: set up a `GameState` where the
  current AR is Free-Ops influence (forces a country-pick frame), call
  `play_game_traced_from_state_with_rng` with a deterministic
  `PolicyCallbackFn` that always returns 0; assert at least one
  `StepTrace.sub_frames` vector is non-empty for that AR and its first frame
  has `kind == FrameKind::CountryPick`.
- `test_policy_cb_is_invoked_per_subframe`: pass a `PolicyCallbackFn` that
  increments an atomic counter; run a full short game; assert counter >= 1
  (i.e. the callback was actually reached at least once during sub-frames).
- `test_backcompat_no_cb_still_runs`: call the traced harness with
  `subframe_cb = nullptr`; assert the game still completes and sub_frames
  vectors are empty (RNG path still works as before — no regression).

## Acceptance criteria
- [ ] All six listed test cases pass: `ctest --test-dir build-ninja --output-on-failure -R subframe_logging`
- [ ] Full C++ suite green: `ctest --test-dir build-ninja --output-on-failure` (95 pre-existing tests still pass)
- [ ] Python suite green: `uv run pytest tests/python/ -q -n 0`
- [ ] Engine v1.0 ceiling unchanged: `scripts/engine_v1_certify.sh` passes at 74 violations
- [ ] Collector JSONL line count per game is strictly `>=` pre-change count (sub-frame rows are additive; top-level rows are byte-identical except for the new `"row_kind":"ar"` field)
- [ ] Three separate commits, one per sub-task, in this order: DecisionFrame ext → trace wiring → collector emit

## Constraints
- **Scope is the self-play collector only.** Do NOT touch
  `cpp/tools/collect_mcts_games_jsonl.cpp`, `cpp/tscore/mcts.cpp`, the replay
  validator trace, or any Python code. The Python dataset schema update is a
  separate follow-up task.
- **Single `FrameAction chosen_action` struct field, not parallel vectors.**
  Parallel vectors desync under exception paths; a single struct stays
  coherent.
- **`PolicyCallbackFn` must wrap the SAME neural policy** that constructs the
  top-level `PolicyFn` (`base_policy`). If sub-frame targets come from a
  different distribution than AR targets, the collected BC/AWR data is
  self-contradictory. Read the existing top-level policy wiring (~lines
  328–341 of `collect_selfplay_rows_jsonl.cpp`) and mirror it — do not
  introduce a second inference path.
- **Backwards-compatible defaults.** New function parameters default to
  `nullptr`; existing non-collector call sites (`play_game` variants without
  tracing, plus tests) must compile and pass unchanged.
- **No new dependencies.** Pure C++20; `std::vector<DecisionFrame>` in
  `StepTrace` uses the existing `decision_frame.hpp` type.
- **Commit discipline.** One commit per sub-task; each commit must build and
  pass its own subset of tests before the next starts.
- **No `rm` inside the repo** — if stale artifacts appear, `mv` them aside
  (repo rule, see CLAUDE.md).
