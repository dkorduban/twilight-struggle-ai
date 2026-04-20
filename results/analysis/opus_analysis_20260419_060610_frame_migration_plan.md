# Opus Analysis: Frame Migration Plan
Date: 2026-04-19T06:06:10Z
Question: What is left in terms of complete migration to the frame model? Write a good robust plan that guards against regressions.

## Executive Summary

The frame-stack API covers ~35 cards today (all the big CountryPick / CardSelect / SmallChoice patterns), but the migration is still visibly incomplete on four fronts: (1) ~8 card events still fall through to `choose_*` without the `frame_stack_mode` bail-out guard (cards 39, 78, 83, 84, 90, 91, 97, 102); (2) the non-card resolvers (Quagmire/Bear Trap, CMC cancel, NORAD follow-on, Glasnost free ops) still run synchronously and the matching `ForcedDiscard` / `CancelChoice` / `NoradInfluence` / `FreeOpsInfluence` / `DeferredOps` FrameKinds are declared but dormant; (3) `apply_ops_randomly_impl` (used by cards 32, 52, 68 and potentially more) is the single biggest shared-infra gap — until it becomes frame-aware, those three cards can at best push their first sub-choice and then leak their nested ops placement; (4) the Headline and Setup phases use whole-action PolicyFns, not the sub-frame path, so the `Headline` and `SetupPlacement` kinds are also dormant. The `engine_peek` / `engine_step_subframe` API is also **not exposed in `bindings/tscore_bindings.cpp`**, which means the migration is internally usable but externally invisible to Python callers. The robust regression guard is a seeded two-path parity harness: run identical games through `apply_action_live(policy_cb=…)` and `engine_step_toplevel + engine_step_subframe(sub_policy=…)` with a deterministic tie-broken sub_policy, and require exact post-state hash equality and identical `GameResult` every AR.

## Findings

### 1. Current state of the frame API

#### Frame kinds declared in `cpp/tscore/decision_frame.hpp`
- `TopLevelAR` — default kind stamped on `DecisionFrame`; never pushed as a sub-frame.
- `SmallChoice` — used (cards 16, 20, 48, 49, 97 effectively, 103).
- `CountryPick` — used (majority of migrated cards).
- `CardSelect` — used (5, 10, 46, 52, 68, 88, 95, 98, 101).
- `ForcedDiscard` — **declared, never pushed**. Only referenced in `tests/cpp/test_frame_regression.cpp`.
- `CancelChoice` — **declared, never pushed**.
- `FreeOpsInfluence` — **declared, never pushed**.
- `NoradInfluence` — **declared, never pushed**.
- `DeferredOps` — **declared, never pushed**.
- `SetupPlacement` — **declared, never pushed**.
- `Headline` — **declared, never pushed**.

(Confirmed by `Grep "FrameKind::(Headline|SetupPlacement|FreeOpsInfluence|NoradInfluence|DeferredOps|CancelChoice|ForcedDiscard)"` — only hits are in `test_frame_regression.cpp`.)

#### API entry points
- `engine_peek(gs)` — returns `gs.frame_stack.back()` or `nullopt` (`cpp/tscore/game_loop.cpp:662`).
- `engine_step_toplevel(gs, action, side, rng, sub_policy)` — sets `frame_stack_mode = !sub_policy`, calls `apply_action_live` with `cb_ptr` populated from a `sub_policy` adapter or `nullptr`. If the action pushes a sub-frame, the stack is non-empty afterward; otherwise the action fully resolved (`game_loop.cpp:669`).
- `engine_step_subframe(gs, action, rng)` — pops the back frame and dispatches through `resume_card_subframe`, then runs `complete_parent_frame_if_ready` (`game_loop.cpp:1843`).
- `resume_card_subframe` switch covers cards: 5, 7, 10, 14, 16, 19, 20, 23, 26, 28, 29, 30, 33, 36, 37, 46, 48, 49, 50, 52, 56, 59, 60, 67, 68, 71, 75, 76, 77, 88, 94, 95, 98, 101 (`game_loop.cpp:1732-1838`).
- **Bindings**: `bindings/tscore_bindings.cpp` contains **no references** to `engine_peek`, `engine_step_subframe`, `engine_step_toplevel`, `frame_stack`, or `DecisionFrame`. The frame API is C++-only.

#### How the `choose_*` helpers cooperate with frames
`choose_option`, `choose_country`, `choose_card` in `cpp/tscore/step.cpp:102-206` share the same pattern:

```cpp
if (policy_cb == nullptr && frame_stack_mode && frame_log != nullptr) {
    record_*_frame(card_id, side, …, frame_log);
    return 0;  // or -1 for SmallChoice
}
```

This pushes a frame and returns a sentinel so the caller can bail out. A card is "migrated" if it (a) receives `frame_stack_mode` at all three helper calls, (b) checks for the sentinel and returns early, and (c) has a matching `resume_card_N` function registered in `resume_card_subframe`.

### 2. Card-by-card migration status

#### Already migrated (resume handler present + frame_stack bail-out)

| Card | Pattern | Notes |
|------|---------|-------|
| 5    | 1-step CardSelect | Five Year Plan |
| 7    | 3-step CountryPick | Socialist Governments |
| 10   | 1-step CardSelect | Blockade counter |
| 14   | N-step CountryPick loop | Romanian Abdication |
| 16   | SmallChoice → CountryPick | Warsaw Pact |
| 19   | 1-step CountryPick | Truman Doctrine |
| 20   | SmallChoice → 4-step CountryPick | NATO-style event |
| 23   | 7-step CountryPick | Marshall Plan (old var) |
| 26   | 1-step CountryPick | Middle East Scoring prep |
| 28   | 2-step CountryPick | Suez Crisis |
| 29   | 3-step CountryPick | East-European Unrest |
| 30   | N-step CountryPick | Decolonization |
| 33   | 2N-step src/dst CountryPick (criteria_bits carries src) | Willy Brandt |
| 36   | region-indexed CountryPick loop | Marshall Plan region variant |
| 37   | 2-step CountryPick | Allende |
| 46   | 1-step CardSelect | SALT (reclaim from discard) |
| 48   | SmallChoice | Summit |
| 49   | SmallChoice (DEFCON level) | How I Learned to Stop Worrying |
| 50   | 2-step CountryPick | US/Iran Hostage Crisis |
| 52   | 1-step CardSelect + nested ops | Junta — nested ops still uses `apply_ops_randomly_impl` (partial) |
| 56   | 1-step CountryPick | South African Unrest |
| 59   | 2-step CountryPick | Flower Power-ish |
| 60   | 2-step CountryPick | Camp David |
| 67   | 1-step CountryPick | Portuguese Empire Crumbles |
| 68   | 1-step CardSelect + nested ops | Lone Gunman — same partial as 52 |
| 71   | 1-step CountryPick | OAS Founded |
| 75   | 1-step CountryPick | Colonial Rear Guards |
| 76   | 1-step CountryPick | Shuttle Diplomacy / Liberation Theology |
| 77   | 4-step CountryPick | PRC-related |
| 88   | 1-step CardSelect (discard → fire event) | Terrorism / Star Wars |
| 94   | 1-step CountryPick | Lone Gunman (free coup) |
| 95   | 2-step CardSelect | Aldrich Ames Remix |
| 98   | 2-step CardSelect (criteria_bits carries first) | Grain Sales to Soviets |
| 101  | 1-step CardSelect | Aldrich Ames discard |

#### NOT migrated — card events in `step.cpp`/`hand_ops.cpp`

These cards still call `choose_*` without the `frame_stack_mode` bail-out (or call it via `resolve_event_country_choice` which does not record a suspension):

| Card | File | Pattern | Effort |
|------|------|---------|--------|
| 24   | `step.cpp:659` | `resolve_event_country_choice` (India/Pakistan war) | Easy (1-step CountryPick; `resolve_event_country_choice` bypasses bail-out) |
| 39   | `step.cpp:893` | `resolve_event_country_choice` over full stability-≤2 pool (Brush War) | Easy (single pick, large pool) |
| 83   | `step.cpp:1343` | 2 free coups, second pool depends on first (region must differ) | Medium (criteria_bits carries first region) |
| 90   | `step.cpp:1402` | 4 or 6 loose CountryPick steps (The Reformer) | Easy (dynamic total_steps) |
| 91   | `step.cpp:1424` | 2-step CountryPick (Marine Barracks — remove US infl) | Easy |
| 97   | `step.cpp:1500` | 1-step `choose_option` over 6 regions (Chernobyl) | Easy (SmallChoice) |
| 102  | `step.cpp:1542` | 3-step CountryPick over W.Europe with US infl ≥ 1 | Easy |
| 105  | `step.cpp:1564` | 1-step CountryPick (Iran-Iraq War via `resolve_event_country_choice`) | Easy |
| 32   | `hand_ops.cpp:198` | CardSelect (opp-side card to discard) + `apply_ops_randomly_impl` | **Hard** (needs frame-aware ops helper) |
| 52   | `hand_ops.cpp:284` | CardSelect migrated; nested `apply_ops_randomly_impl` NOT frame-aware | Hard |
| 68   | `hand_ops.cpp:353` | CardSelect migrated; nested `apply_ops_randomly_impl` NOT frame-aware | Hard |
| 78   | `hand_ops.cpp:386` | `choose_option` (count) + N×CardSelect then redraw | Medium (option-count pattern) |
| 84   | `hand_ops.cpp:429` | `choose_option` (keep count) + N×CardSelect among drawn | Medium (same pattern) |
| 43   | `hand_ops.cpp:824` | CMC cancel resolver — `choose_option` opt-in + `choose_card` | Medium (new CancelChoice + ForcedDiscard kinds) |
| 45/47| `hand_ops.cpp:771` | Quagmire / Bear Trap — `choose_card` (forced discard ≥2 ops) | Medium (ForcedDiscard kind) |

Note on card 8 (Fidel), 17 (De Gaulle), 18, 21 (NATO), 22 (Independent Reds), 31 (Decolonization variant), 34, 35, 38 etc. — these have no decision points at all (no `choose_*` call) and need no migration work.

#### Non-card decision points still synchronous

| Site | File | Pattern | Frame kind needed |
|------|------|---------|-------------------|
| `resolve_trap_ar` (Quagmire card 45, Bear Trap card 47) | `hand_ops.cpp:771` | `choose_card` over ≥2-ops non-scoring hand | `ForcedDiscard` |
| `resolve_cuban_missile_crisis_cancel` (card 43) | `hand_ops.cpp:824` | `choose_option(2)` opt-in then `choose_card` | `CancelChoice` → `ForcedDiscard` |
| `resolve_norad` (post-coup NORAD influence) | `game_loop.cpp:138` | `choose_country` over any US-infl country | `NoradInfluence` |
| `resolve_glasnost_free_ops_live` (card 93 follow-on) | `game_loop.cpp:608` → `apply_influence_budget_impl:105` | budgeted `choose_country` loop | `FreeOpsInfluence` |
| `execute_deferred_ops` (opponent-scheduled ops after event) | `hand_ops.cpp:585` | Enumerates ops action modes + ops placement | `DeferredOps` |
| Setup / bid placement | `game_loop.cpp:1986 run_setup_phase` | Uses whole-action `PolicyFn`, not `policy_cb` | `SetupPlacement` (requires different plumbing) |
| Headline phase | `game_loop.cpp:171 run_headline_phase` | Uses whole-action `PolicyFn` | `Headline` (requires different plumbing) |

### 3. `apply_ops_randomly_impl` — the shared-infra gap

`cpp/tscore/hand_ops.cpp:673`. Used by cards **32, 52, 68** (grep of `apply_ops_randomly_impl` in step.cpp/hand_ops.cpp returns three call sites). The function:

1. Picks one of `{Influence, Influence, Coup, Realign}` via `choose_option` over 4.
2. Depending on mode, loops `choose_country` `ops` times.

There is already a **random-RNG-only** twin `apply_frame_ops_randomly_impl` (`game_loop.cpp:825`) that takes no `policy_cb`. That twin is used by the frame path as a placeholder, but it hard-wires choices to the RNG and therefore does **not** surface sub-frames to the sub_policy.

To properly migrate, a frame-aware variant is needed that:
- Pushes a `SmallChoice` frame (4 options) for the mode pick.
- Pushes N `CountryPick` frames (where N = ops) for Influence.
- Pushes `CountryPick` once for Coup / Realign target (plus N-1 realigns for Realign mode).
- All nested under the same parent_card (32 / 52 / 68).

This is the single largest piece of shared infrastructure; do it once before touching 32/52/68 end-to-end. Card 52 and 68 already half-migrate (their CardSelect is visible), so the nested placement is silently resolved via `apply_frame_ops_randomly_impl` (random) in frame-stack mode — a **current behavior mismatch vs the policy-cb path**, and a regression risk right now.

### 4. Python bindings gap

`bindings/tscore_bindings.cpp` contains zero references to `engine_peek`, `engine_step_subframe`, `engine_step_toplevel`, `frame_stack`, or `DecisionFrame`. The frame API is not exposed to Python. Self-play / MCTS code that consumes Python bindings cannot currently drive the frame path. This has to be wired before any downstream training or search component depends on the frame model.

### 5. Existing regression coverage

`tests/cpp/test_frame_regression.cpp` tests:
- First-frame-kind checks for cards 5, 16, 28 (not really — Korean War has no sub-decision so it's a soft check), 103, 101, 7, 22, 56, 68, 76, 88, 56 again, 27, 88 (two variants), 101.
- End-to-end `engine_step_subframe` drive of cards 7, 56, 5, 68, 88 (Star Wars selecting Romania-touching card), 101.

Gaps:
- No parity test comparing policy_cb path vs sub_policy path on identical seeds.
- No multi-frame-step tests for 33 (Willy Brandt src/dst), 98 (Grain Sales 2-step), 14/23/29/30 multi-step loops.
- No test that `resume_card_subframe` default-case (unknown card) behaves sanely.
- No test for cards 32/52/68 that their `apply_ops_randomly_impl` path either pushes frames or is consistent with the policy_cb path.
- No end-to-end "play N games both ways" regression.

## Conclusions

1. **~12 card events still need migration**: 24, 32, 39, 43 (CMC cancel), 45/47 (traps), 52 (partial), 68 (partial), 78, 83, 84, 90, 91, 97, 102, 105.
2. **Five non-card resolvers** (trap, CMC, NORAD, Glasnost, deferred ops) are entirely synchronous and the five matching `FrameKind`s are dormant.
3. **`apply_ops_randomly_impl` is the single highest-leverage shared gap** — it silently undercuts the frame paths of cards 32/52/68, which currently use `apply_frame_ops_randomly_impl` (pure RNG) as a fallback, producing behavior that differs from the policy_cb path.
4. **Setup and Headline phases are not part of the frame API** and would require different plumbing (they use `PolicyFn`, not `policy_cb`). The `SetupPlacement` / `Headline` kinds are essentially placeholders.
5. **No Python bindings exist** for the frame API. Any training / MCTS / play-server consumer of the frame model must be unblocked by exposing `engine_peek` / `engine_step_toplevel` / `engine_step_subframe` via pybind11 first.
6. **Existing tests are first-frame-kind only** — they do not guarantee two-path behavioral parity. A new test harness is the biggest regression-guard lever.
7. **Migration is ~65-70% done by card count**, but the behavioral-parity and shared-infra risk is concentrated in the remaining 30%.

## Recommendations

### Migration plan, ordered lowest-risk → highest-risk

Each slice adds tests **before** modifying production code; each slice is independently revertable.

#### Slice A — Regression harness (must come first)

1. Add `tests/cpp/test_frame_parity.cpp`:
   - Fixture `play_with_policy_cb(seed)` → runs a game via `apply_action_live` with a deterministic `policy_cb` that picks the first legal option (lowest index).
   - Fixture `play_with_sub_policy(seed)` → same game via `engine_step_toplevel` / `engine_step_subframe` with a `sub_policy` that converts first-legal-option into a `FrameAction` matching what the cb would return (use `event_decision_to_frame` / `frame_action_to_index` semantics to guarantee bit-identical choices).
   - Assert `GameResult.winner`, `GameResult.final_vp`, `GameResult.end_turn`, and the deterministic public-state hash at every AR boundary match exactly.
   - Run 500 games with RNG seeds 0..499.
2. Add `tests/cpp/test_frame_per_card.cpp`:
   - Parameterised test: for each card ID that is in scope, construct a minimal GameState that exercises the card's sub-decisions, then assert:
     - `engine_step_toplevel` returns `pushed_subframe = true` when decisions are pending;
     - iterating `engine_peek` + `engine_step_subframe` empties the stack;
     - final public state equals the result of running the same setup through `apply_action_live` with a matching policy_cb.
3. Land Slice A before any card migration. The parity harness must be green before each subsequent slice and re-run after.

#### Slice B — Unmigrated single-pick cards (low risk, mechanical)

Order: 24, 39, 105 (all route through `resolve_event_country_choice`), then 97, 91, 102, 90, 83.

**Signatures** (for `game_loop.cpp`):
- `void resume_card_24(GameState&, const DecisionFrame&, const FrameAction&, Pcg64Rng&)` — apply war card after target pick.
- `void resume_card_39(GameState&, const DecisionFrame&, const FrameAction&, Pcg64Rng&)` — same.
- `void resume_card_105(…)` — same.
- `void resume_card_97(GameState&, const DecisionFrame&, const FrameAction&)` — SmallChoice → set `chernobyl_blocked_region`.
- `void resume_card_91(…)` — 2-step CountryPick loop, self-dispatching.
- `void resume_card_102(…)` — 3-step CountryPick, W.Europe + US infl filter refreshed each step.
- `void resume_card_90(…)` — variable total_steps (4 or 6) stored in total_steps field at first push.
- `void resume_card_83(…)` — 2-step CountryPick; criteria_bits = region_key of first pick, second pool filters region != criteria_bits.

Also: fix `resolve_event_country_choice` (`step.cpp:308`) to honor `frame_stack_mode` — either pass through to `choose_country` (which already supports bail-out) and propagate the sentinel, or inline the bail-out. Without this, cards 24/39/105 cannot be migrated cleanly.

Regression guard: each card's parity case added to Slice A harness **before** code change. Land together with code change.

#### Slice C — Dormant FrameKinds for non-card resolvers

Order: trap (`ForcedDiscard`), CMC cancel (`CancelChoice` + `ForcedDiscard`), NORAD (`NoradInfluence`), Glasnost free ops (`FreeOpsInfluence`).

Plan:
1. Add `push_forced_discard_frame`, `push_cancel_choice_frame`, `push_norad_frame`, `push_free_ops_frame` helpers in `game_loop.cpp`, symmetric to the existing `push_country_frame` / `push_card_frame`.
2. Convert each resolver to push a frame under `frame_stack_mode` and return early, just like the cards.
3. Add resume functions and plumb them into the engine-step loop. The resolver paths are **not** inside `apply_action_live` — they are invoked from `run_action_rounds` / `run_extra_action_round`. So the top-level step API needs an explicit hook: the `engine_step_toplevel` caller must drain pending resolvers the same way it drains card sub-frames. Most likely this means: after any AR ends, call a new `engine_drain_side_hooks(gs)` that may push new frames (trap, CMC, NORAD), and the test harness must iterate those too.
4. Add per-resolver parity tests.

This slice is moderate risk because it changes the shape of the main action-round loop. Keep the old synchronous path callable via `apply_action_live` and gate the new behavior strictly on `frame_stack_mode`.

#### Slice D — Option-count driven cards 78 & 84

Pattern: one `SmallChoice` frame for count (0..N), then N `CardSelect` frames for picks. Criteria_bits can store the remaining count or the already-picked bitmask if needed. Both cards follow the same shape.

Resume signatures:
- `void resume_card_78(GameState&, const DecisionFrame&, const FrameAction&, Pcg64Rng&)` — if SmallChoice: record count, push N CardSelect frames (or push one and rely on `total_steps = N, step_index = 0`). If CardSelect: record pick, advance step, push next or finalize redraw.
- `void resume_card_84(…)` — same shape, but pick subset of previously-drawn cards; criteria_bits tracks which drawn cards remain candidate.

Shared infra: a `push_card_count_sequence` helper would simplify both. But don't generalize until both cards are migrated — prefer duplication over premature abstraction.

#### Slice E — `apply_ops_randomly_impl` → frame-aware helper

This is the load-bearing shared-infra change.

1. Build `push_ops_randomly_frames(GameState& gs, Side, int ops, CardId parent_card)` that pushes:
   - One `SmallChoice` frame for mode (4 options).
   - The resume function then, depending on mode, pushes 1 `CountryPick` (Coup) or N `CountryPick` (Influence / Realign) frames.
2. Introduce a new source_card tag (use `parent_card`, keep `source_card = 0` to distinguish from a real card event) for those frames.
3. Migrate cards 32, 52, 68 to call the new helper instead of the random twin when in `frame_stack_mode`.
4. Parity-test the three cards explicitly under Slice A, including hand compositions that force the all-scoring / no-hand edge cases.

Risk: any bug here propagates to three cards simultaneously. Insist on 2000-game parity runs for each card individually before landing.

#### Slice F — `execute_deferred_ops` (`DeferredOps` kind)

Opponent-event + own-ops flow. This path is the meatiest of the lot because it nests a card event (possibly with its own sub-frames) inside the sub-decision stream of the current AR. Use `parent_card` on all child frames to disambiguate during resume.

Implementation: push a `DeferredOps` frame that encapsulates the enumerated ops actions, and on resume rebuild the chosen `ActionEncoding` and call `apply_action` under `frame_stack_mode`. Any sub-frames the inner event pushes will automatically be below the `DeferredOps` frame on the stack.

#### Slice G — Python bindings

Expose to pybind11 in `bindings/tscore_bindings.cpp`:
- `DecisionFrame` with all fields read-only (esp. `kind`, `source_card`, `acting_side`, `eligible_countries`, `eligible_cards`, `step_index`, `total_steps`, `criteria_bits`, `parent_card`).
- `FrameAction` with writable fields.
- `StepResult`.
- `engine_peek(gs)` → Python `Optional[DecisionFrame]`.
- `engine_step_toplevel(gs, action, side, rng, sub_policy=None)` — `sub_policy` optional Python callable.
- `engine_step_subframe(gs, action, rng)`.
- Set `gs.frame_stack_mode` exposed as property.

Only expose after Slice F is green; otherwise Python callers will stumble on the silently-incorrect ops cards.

#### Slice H — Setup and Headline (optional)

These need different plumbing because they do not go through `apply_action_live` / `policy_cb`. If there is no concrete consumer need, consider **removing** the `SetupPlacement` and `Headline` FrameKinds to avoid misleading dead enum values. Otherwise, wire them as their own `engine_step_headline_card` / `engine_step_setup_placement` entry points with matching `engine_peek_phase` overloads.

### Regression guard strategy (independent of slices)

1. **Two-path parity harness** (Slice A) — 500+ seeds, policy_cb vs sub_policy with identical tie-broken choices. Must be green before and after every slice.
2. **Per-card / per-resolver parity test** — one fixture per migrated site; keep them exhaustive, not sampled.
3. **Unknown-source-card guard** — assert that `resume_card_subframe`'s default branch is unreachable for any card with a pushable sub-decision. Add a compile-time/runtime registry and a test that iterates all CardIds and fails if a card pushes a frame in `frame_stack_mode` without a matching resume handler.
4. **Hash-stability check** — every migrated card's Slice A case snapshots the state hash pre/post and compares to a golden value committed under `tests/cpp/fixtures/frame_hashes/`. A hash change fails the test and forces explicit re-blessing.
5. **Benchmark smoke** — after each card slice, run `/bench` for 2000 games per side at one fixed seed pair; require winrate delta ≤ ±1.5 pp vs the pre-slice baseline. This catches subtle ordering / RNG consumption regressions.
6. **Legal-action API sanity** — if `choose_country` silently bailed out without pushing a frame (eligible list empty but caller expected one), we would see `illegal_action_rate_after_masking > 0` at the Python layer. Assert 0 for every slice.

### Suggested ordering summary

1. Slice A (harness) — 1 day.
2. Slice B (single-pick cards) — 2 days, can parallelise card-by-card.
3. Slice C (trap / CMC / NORAD / Glasnost resolvers) — 2 days; requires main-loop change (drain hooks).
4. Slice D (cards 78 / 84) — 1 day.
5. Slice E (`apply_ops_randomly_impl` + 32/52/68) — 2 days; biggest correctness risk.
6. Slice F (`execute_deferred_ops` / `DeferredOps`) — 2 days.
7. Slice G (Python bindings) — 1 day.
8. Slice H (headline / setup, or deletion of dormant kinds) — 1-2 days, optional depending on downstream need.

Total ≈ 12 engineer-days with strong guard rails at each step.

## Open Questions

1. **Is the frame model intended for online MCTS / self-play rollouts, or purely for observability + potential distillation targets?** This changes priority:
   - If MCTS/rollouts: Slice E (ops-randomly) is blocking — those cards run in every game and currently diverge between paths.
   - If observability only: Slice G (Python bindings) is the gate; Slice E can be deferred as long as policy_cb remains the runtime path.
2. **Will `SetupPlacement` and `Headline` ever be needed, or should they be deleted?** Current code uses `PolicyFn` for those phases; retrofitting requires a different API surface entirely (whole-action decisions rather than sub-action decisions).
3. **How should nested events interact with `parent_card`?** Card 88 (Star Wars) fires a nested event from the discard pile — it uses `resolve_frame_selected_event` + `tag_new_frames_with_parent`. Is this the model for card 32 (forced discard + opponent-card ops) and card 68 (similar)? Confirm one canonical pattern before Slice E/F.
4. **Cards 78 / 84 option-count semantics** — is the 0..N+1 range actually `0..N` (no upper bound chosen) or `0..N+1` (including "discard none / keep all")? The code uses `static_cast<int>(discardable.size()) + 1` which includes 0. Confirm this is correct per rules before enshrining the SmallChoice width.
5. **`resolve_event_country_choice` (step.cpp:308)** — it short-circuits on `action.targets.front()` being in the pool. Under `frame_stack_mode`, the targets vector is usually empty, so it falls through to `choose_country`. Should we keep this short-circuit (and treat pre-supplied targets as a "policy already decided" signal that bypasses the frame) or force everything through frames for uniformity? The former is cheaper, the latter is more predictable.
6. **Do any other sites use `apply_ops_randomly_impl`?** Grep shows only cards 32, 52, 68. Confirm there are no future callers planned (e.g., Asia Scoring bonuses, ABM Treaty-like events) that would require the helper to be upgraded anyway.
7. **Subframe dispatch is a switch-on-source-card.** At some point this should become a registry (card_id → resume_fn) so adding a card is a one-line change and the "unknown source_card" test becomes automatic. Is this worth doing now, or defer?
