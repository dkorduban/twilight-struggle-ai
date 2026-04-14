# Architecture Refactor Audit — 2026-04-14

## Phase Status Table
| Phase | Description | Status | Evidence |
|---|---|---|---|
| Phase 1 | Shared decode helper | PARTIAL | `cpp/tscore/decode_helpers.hpp:1-392` exists and `learned_policy.cpp:84-104` plus `mcts_batched.cpp:3605-3630` use it, but `mcts_batched.cpp:3362-3575` still re-implements rollout decode logic. |
| Phase 2 | Shared search-support layer | PARTIAL | `cpp/tscore/search_common.hpp:1-157` exists with value/scoring helpers, but `ModeDraft`, `CardDraft`, `apply_tree_action`, `AccessibleCache`, card-draft collection, and country-logit resolution remain local in `mcts.cpp`, `ismcts.cpp`, and `mcts_batched.cpp`. |
| Phase 3 | Observation boundary | PARTIAL | `Observation`, `make_observation()`, and `determinize()` exist in `game_state.hpp/.cpp`, and `ismcts_search()` now takes `Observation`, but `mcts_search()` still takes `GameState`, `mcts_batched.cpp` is still full-state shaped, and `PolicyFn` remains `(PublicState, CardSet, bool, Pcg64Rng&)`. |
| Phase 4 | `game_loop.cpp` cleanup | PARTIAL | `apply_ops_randomly_impl`, `apply_hand_event`, and `apply_action_with_hands` are no longer defined in `game_loop.cpp`; they moved to `hand_ops.cpp`, but not into `step.cpp`, and `game_loop.cpp` still owns several rule helpers. |
| Phase 5 | `mcts_batched_fast` handling | PARTIAL | `cpp/mcts_batched_fast/` still exists and has its own build file, but the root build excludes it (`CMakeLists.txt:118-119`). |
| Phase 6 | Python engine removal | PARTIAL | `python/tsrl/engine/DEPRECATED.md` exists and `scripts/train_ppo.py:81` uses `tscore`, but active Python modules such as `python/tsrl/policies/minimal_hybrid.py:22-30` and `python/tsrl/selfplay/collector.py:35-36` still import `tsrl.engine.*`. |

## Detailed Findings

### Phase 1 — Shared decode helper

Implemented:

- `cpp/tscore/decode_helpers.hpp` now exists. It contains shared decode utilities:
  - `requires_defcon_fallback()` at `cpp/tscore/decode_helpers.hpp:38-54`
  - `accessible_countries_filtered()` at `cpp/tscore/decode_helpers.hpp:56-68`
  - `build_action_from_country_logits()` at `cpp/tscore/decode_helpers.hpp:70-139`
  - `build_action_from_marginal_logits()` at `cpp/tscore/decode_helpers.hpp:141-217`
  - `build_random_target_action()` at `cpp/tscore/decode_helpers.hpp:219-242`
  - `choose_action_from_outputs()` at `cpp/tscore/decode_helpers.hpp:244-389`
- `TorchScriptPolicy::choose_action()` no longer contains its own card/mode/country decode path. It forwards to `decode::choose_action_from_outputs()` at `cpp/tscore/learned_policy.cpp:84-104`.
- `mcts_batched.cpp` no longer contains the old "exact mirror of `TorchScriptPolicy::choose_action`" comment. The current comment at `cpp/tscore/mcts_batched.cpp:3323-3325` says greedy decode shares semantics through `decode_helpers.hpp`.
- `mcts_batched.cpp` greedy decode now calls the shared helper in `greedy_action_from_outputs()` at `cpp/tscore/mcts_batched.cpp:3578-3630`.

Still missing:

- The rollout/training path in `mcts_batched.cpp` still has a separate decode implementation. `rollout_action_from_outputs()` at `cpp/tscore/mcts_batched.cpp:3362-3575` rebuilds:
  - playable-card masking (`3415-3434`)
  - legal-mode filtering (`3440-3459`)
  - DEFCON/event fallback logic (`3464-3472`)
  - accessible-country masking (`3485-3508`)
  - influence allocation (`3528-3567`)
  - log-prob bookkeeping (`3436-3438`, `3460-3462`, `3515-3517`, `3574`)
- So the duplication was reduced, not eliminated. The shared helper is authoritative for `learned_policy.cpp` and greedy decode, but rollout decode is still bespoke.
- There is also residual helper duplication: `decode_helpers.hpp:56-68` carries its own `accessible_countries_filtered()`, while `search_common.hpp:114-125` defines the same helper separately.

Bottom line: Phase 1 is only partially complete relative to the April 13 goal of making both greedy and rollout decode thin wrappers around one shared implementation.

### Phase 2 — Shared search-support layer

Implemented:

- `cpp/tscore/search_common.hpp` exists and currently provides:
  - `kVirtualLossPenalty` and `kSpaceShuttleArs` at `cpp/tscore/search_common.hpp:23-27`
  - `count_scoring_cards()` at `cpp/tscore/search_common.hpp:28-37`
  - `remaining_action_decisions_for_side()` at `cpp/tscore/search_common.hpp:39-49`
  - `scoring_card_prior_multiplier()` at `cpp/tscore/search_common.hpp:51-64`
  - `winner_value()` at `cpp/tscore/search_common.hpp:67-75`
  - `calibrate_value()` at `cpp/tscore/search_common.hpp:77-84`
  - `holds_china_for()` at `cpp/tscore/search_common.hpp:86-88`
  - `sync_china_flags()` at `cpp/tscore/search_common.hpp:90-93`
  - `softmax_inplace()` at `cpp/tscore/search_common.hpp:95-112`
  - `accessible_countries_filtered()` at `cpp/tscore/search_common.hpp:114-125`
  - `rollout_value()` at `cpp/tscore/search_common.hpp:128-135`
  - `evaluate_leaf_value_raw()` at `cpp/tscore/search_common.hpp:137-155`
- `ismcts.cpp` and `mcts_batched.cpp` now use `evaluate_leaf_value_raw()`:
  - `cpp/tscore/ismcts.cpp:924`, `945`
  - `cpp/tscore/mcts_batched.cpp:1317`, `1353`, `1553`, `1635`
- All three search files use helpers such as `holds_china_for()`, `sync_china_flags()`, `count_scoring_cards()`, and `scoring_card_prior_multiplier()`.

Still local / still triplicated:

- `ModeDraft` and `CardDraft` remain local structs in all three search files:
  - `cpp/tscore/mcts.cpp:45-53`
  - `cpp/tscore/ismcts.cpp:50-58`
  - `cpp/tscore/mcts_batched.cpp:49-57`
- `ExpansionResult` remains local in all three:
  - `cpp/tscore/mcts.cpp:55-58`
  - `cpp/tscore/ismcts.cpp:60-63`
  - `cpp/tscore/mcts_batched.cpp:203-206`
- `SelectionResult` is still local in `ismcts.cpp` and `mcts_batched.cpp`:
  - `cpp/tscore/ismcts.cpp:65-68`
  - `cpp/tscore/mcts_batched.cpp:208-211`
- `apply_tree_action` is not shared:
  - `cpp/tscore/mcts.cpp:231-247`
  - `cpp/tscore/ismcts.cpp:380-440`
  - `cpp/tscore/mcts_batched.cpp:308-324`
- `AccessibleCache` is still duplicated, not shared:
  - `cpp/tscore/ismcts.cpp:444-510`
  - `cpp/tscore/mcts_batched.cpp:326-408`
  - `mcts.cpp` has no shared cache layer at all.
- Card-draft / legal-card collection is still local:
  - `cpp/tscore/mcts.cpp:265-340`
  - `cpp/tscore/ismcts.cpp:520-640`
  - `cpp/tscore/mcts_batched.cpp:419-502`
  - batched fast-path compact legality also remains local at `cpp/tscore/mcts_batched.cpp:524-582`
- Country-logit action resolution is still local:
  - `cpp/tscore/mcts.cpp:71-229`
  - `cpp/tscore/ismcts.cpp:774-880`
  - `mcts_batched.cpp` has separate decode/action-resolution logic in `rollout_action_from_outputs()` and `greedy_action_from_outputs()`.
- `mcts.cpp` still has its own `evaluate()` wrapper over `GenericDict` outputs at `cpp/tscore/mcts.cpp:249-263`, so leaf-evaluation sharing is incomplete there too.

Bottom line: `search_common.hpp` is real, but it extracted a narrow utility layer, not the broader semantic adapter layer described in Phase 2. The highest-risk semantic duplication is still present.

### Phase 3 — Observation boundary

Implemented:

- `Observation` exists in `cpp/tscore/game_state.hpp:143-149` with these fields:
  - `PublicState pub`
  - `CardSet own_hand`
  - `bool holds_china`
  - `int opp_hand_size`
  - `Side acting_side`
- `make_observation()` exists at `cpp/tscore/game_state.cpp:160-171`. It copies public state, records the acting side, copies the acting player's hand, copies that side's China ownership flag, and derives `opp_hand_size` from the hidden opponent hand.
- `determinize(const Observation&, Pcg64Rng&)` exists at `cpp/tscore/game_state.cpp:174-208`. It rebuilds a partial `GameState` by:
  - copying `obs.pub`
  - keeping `obs.own_hand`
  - sampling the hidden pool into opponent hand + deck
  - restoring China ownership flags
  - setting `current_side` / `phase`
- `ismcts_search()` now takes `Observation` at the root:
  - declaration: `cpp/tscore/ismcts.hpp:37-42`
  - definition: `cpp/tscore/ismcts.cpp:1945-2013`
- The pooled ISMCTS path also roots itself from observation snapshots: `start_search()` calls `make_observation()` and `determinize()` at `cpp/tscore/ismcts.cpp:1797-1805`.

Still missing:

- Plain MCTS still consumes full state directly:
  - declaration: `cpp/tscore/mcts.hpp:64-69`
  - implementation: `cpp/tscore/mcts.cpp:657-663`
- `mcts_batched.cpp` is still full-state shaped. Examples:
  - `collect_card_drafts_cached(const GameState&)` at `cpp/tscore/mcts_batched.cpp:419-423`
  - `collect_compact_legal_cards(const GameState&)` at `cpp/tscore/mcts_batched.cpp:524-528`
  - `rollout_action_from_outputs(const GameState&, ...)` at `cpp/tscore/mcts_batched.cpp:3362-3377`
  - `greedy_action_from_outputs(const GameState&, ...)` at `cpp/tscore/mcts_batched.cpp:3578-3587`
- `PolicyFn` still uses the legacy boundary:
  - signature: `cpp/tscore/game_loop.hpp:17-22`
  - the ref-based traced-play escape hatch explicitly documents that policies may still need full `GameState` access: `cpp/tscore/game_loop.hpp:121-123`
- Even in the ISMCTS matchup wrapper, the policy lambda still closes over `GameState& gs` and builds the `Observation` on demand:
  - `cpp/tscore/ismcts.cpp:2048-2054`

Bottom line: the `Observation` type and determinization boundary landed, and ISMCTS uses them at the root. The rest of the search/read path is not yet observation-shaped.

### Phase 4 — `game_loop.cpp` cleanup

Implemented:

- `game_loop.cpp` no longer defines the three named helpers:
  - `apply_ops_randomly_impl`
  - `apply_hand_event`
  - `apply_action_with_hands`
- Instead, `game_loop.cpp` now includes `hand_ops.hpp` at `cpp/tscore/game_loop.cpp:9` and calls `apply_action_with_hands()` from the loop/orchestration code:
  - `cpp/tscore/game_loop.cpp:254`
  - `cpp/tscore/game_loop.cpp:360`
  - `cpp/tscore/game_loop.cpp:468`
  - `cpp/tscore/game_loop.cpp:623`
- Those helpers moved into a new engine-side module:
  - declarations in `cpp/tscore/hand_ops.hpp:13-33`
  - `apply_ops_randomly_impl()` in `cpp/tscore/hand_ops.cpp:74-169`
  - `apply_hand_event()` in `cpp/tscore/hand_ops.cpp:171-607`
  - `apply_action_with_hands()` in `cpp/tscore/hand_ops.cpp:744-806`
- `hand_ops.cpp` is part of the main `tscore` target: `cpp/tscore/CMakeLists.txt:4-17`.

What did not happen:

- This logic did not move into `step.cpp`. `step.cpp` only contains the note that `EventFirst` ordering is handled before `apply_action()` at `cpp/tscore/step.cpp:1281-1284`.
- `game_loop.cpp` is cleaner, but it is not "schedules only". It still owns rule/mechanic helpers including:
  - `apply_influence_budget_impl()` at `cpp/tscore/game_loop.cpp:100-131`
  - `resolve_norad()` at `cpp/tscore/game_loop.cpp:133-151`
  - turn cleanup / scoring-card-held loss in `end_of_turn()` at `cpp/tscore/game_loop.cpp:514-599`

Bottom line: the biggest hand-aware helpers are out of `game_loop.cpp`, but the long-term engine/runtime split is not fully resolved. The cleanup happened through `hand_ops.cpp`, not through `step.cpp`.

### Phase 5 — `mcts_batched_fast`

Current state:

- `cpp/mcts_batched_fast/` still exists and is not archived away.
- It still has an active standalone build script: `cpp/mcts_batched_fast/CMakeLists.txt:1-107`.
- That standalone build still produces an executable target, `ts_fast_mcts_bench`, at `cpp/mcts_batched_fast/CMakeLists.txt:72-105`.

Mainline build impact:

- The root build does not include it. `CMakeLists.txt:118-119` adds only:
  - `cpp/tscore`
  - `cpp/tools`
- There is no root `add_subdirectory(cpp/mcts_batched_fast)`.

Bottom line: this fork remains architectural debt, but it is excluded from the default product build. It is still live debt if someone configures that subtree manually.

### Phase 6 — Python engine removal

Implemented:

- `python/tsrl/engine/DEPRECATED.md` exists and clearly marks the Python engine deprecated at `python/tsrl/engine/DEPRECATED.md:1-8`.
- The deprecation note explicitly points callers to the `tscore` bindings and lists the exposed replacement APIs at `python/tsrl/engine/DEPRECATED.md:9-30`.
- The main PPO training script is already on the C++ binding path:
  - it prepends the bindings directory to `sys.path` at `scripts/train_ppo.py:53-67`
  - it imports `tscore` directly at `scripts/train_ppo.py:81`
  - a repo-wide search found no `tsrl.engine` imports in `scripts/train_ppo.py`

Still missing:

- `python/tsrl/policies/minimal_hybrid.py` still imports deprecated Python-engine helpers:
  - `tsrl.engine.adjacency` at `python/tsrl/policies/minimal_hybrid.py:22`
  - `tsrl.engine.game_state` at `python/tsrl/policies/minimal_hybrid.py:23`
  - `tsrl.engine.legal_actions` at `python/tsrl/policies/minimal_hybrid.py:24-30`
- Other active Python modules still depend on `tsrl.engine`, including self-play collection:
  - `python/tsrl/selfplay/collector.py:35-36`
- The deprecation note itself admits the migration is incomplete and lists many remaining callers at `python/tsrl/engine/DEPRECATED.md:64-127`.
- A repo search over `python/tsrl/train`, `python/tsrl/selfplay`, and `python/tsrl/policies` still returns many `tsrl.engine.*` imports.

Bottom line: the authoritative direction is now C++-first, and `train_ppo.py` is already migrated. The Python engine is still actively depended on by policy/self-play utilities, so Phase 6 is not complete.

## GAP-005 Status

Search results:

- `results/continuation_plan.json:19-20` marks `GAP-005a` and `GAP-005b` as done.
- `results/analysis/engine_rule_gaps.md:39-44` marks `GAP-005` as `[DONE]` and ties it to commits `d0e328c` and `4326635`.
- The master plan assigns `GAP-005` to Phase 1C and treats it as a closable engine gap: `results/analysis/opus_analysis_20260413_202000_engine_refactor_master_plan.md:158-180`.
- The one file still talking about GAP-005 as potentially open is `results/analysis/codex_analysis_20260413_clean_architecture_status.md`, at:
  - `53`
  - `243`
  - `358`

Live-code check:

- Influence access is now 1-hop adjacency plus home-anchor reach in `cpp/tscore/adjacency.cpp:85-120`.
- Enemy-controlled influence placement costs 2 ops in legal-action generation at `cpp/tscore/legal_actions.cpp:342-351`.

Nuance:

- `cpp/tscore/step.cpp:1285-1289` still trusts the encoded `ActionEncoding.targets` and does not itself recompute the enemy-control surcharge at execution time. The surcharge is therefore enforced by legal-action generation, not by executor-side validation.

Conclusion:

- GAP-005 is closed in the live codebase and in the current tracker.
- The "still open" language in `codex_analysis_20260413_clean_architecture_status.md` is stale relative to the code and the later tracker.

## WIP ISMCTS Status

Evidence that the three named WIP fixes are present in current code:

- Tree-advance-state fix:
  - `cpp/tscore/ismcts.cpp:178-440` now has explicit tree-state progression helpers:
    - `advance_tree_action_round_to_decision_or_done()`
    - `advance_tree_extra_round_to_decision_or_done()`
    - `advance_tree_post_round_to_decision_or_done()`
    - `resolve_tree_headlines_and_advance()`
  - `apply_tree_action(TreeState&, ...)` at `cpp/tscore/ismcts.cpp:380-440` now advances through real headline/action-round/extra-round/cleanup flow instead of only mutating the immediate node state.
- Pooled tree cloning fix:
  - selection clones determinization root state at `cpp/tscore/ismcts.cpp:961-976`
  - pooled root-expansion path clones state in `play_ismcts_matchup_pooled()` at `cpp/tscore/ismcts.cpp:2150-2161`
  - pooled-vs-model path also clones state in `play_ismcts_vs_model_pooled()` at `cpp/tscore/ismcts.cpp:2336-2346`
- Loop guard:
  - `advance_until_search_or_done()` now has `kMaxAdvanceSteps = 50000` and a forced draw exit with `end_reason = "loop_guard"` at `cpp/tscore/ismcts.cpp:1555-1580`

Current assessment:

- The code looks complete for the three WIP items. I do not see an obvious partially-updated branch where one pooled path still uses pre-fix behavior.
- I also do not see inline `TODO`/`FIXME` markers indicating the fixes are known-incomplete.
- The latest tracker also records these as fixed:
  - `results/continuation_plan.json:75`
  - `results/continuation_plan.json:96`
  - `results/continuation_plan.json:122`
  - `results/continuation_plan.json:129`

Residual risk:

- The pooled ISMCTS code still duplicates large control-flow blocks across `play_ismcts_matchup_pooled()` and `play_ismcts_vs_model_pooled()`, so the fixes are present but still sit on a high-regression surface.
- I would treat the WIP work as code-complete, but not yet "architecturally retired" until those paths have direct regression tests around cloning, AR advancement, and loop-guard behavior.

## Recommended Next Steps (ordered by value)

1. Finish Phase 1 for real by pulling `mcts_batched.cpp:3362-3575` onto the same decode kernel as `learned_policy.cpp:84-104` and `mcts_batched.cpp:3605-3630`. Right now the rollout path is still a semantic fork.
2. Add focused ISMCTS regression tests that lock the three recent WIP fixes: pooled-root cloning, real AR/cleanup advancement inside `apply_tree_action(TreeState&, ...)`, and the `loop_guard` escape path.
3. Extract the highest-risk Phase 2 duplication next, not the whole backend: shared `AccessibleCache` + card-draft collection for `ismcts.cpp` and `mcts_batched.cpp`, and shared country-logit action resolution for `mcts.cpp` and `ismcts.cpp`.
4. Push the Observation boundary into `mcts_batched.cpp` read-only entrypoints. The best first cut is feature filling / decision snapshots, not changing `PolicyFn`.
5. Decide whether `hand_ops.cpp` is the intended long-term hand-aware transition layer. If yes, codify that. If no, move it behind a clearer engine module boundary before more logic accumulates there.
6. Keep `cpp/mcts_batched_fast/` excluded from the root build until it is either explicitly archived or rebased on the shared semantic helpers from Phases 1-2.
7. Continue Python-engine retirement on live callers that still matter operationally. `scripts/train_ppo.py` is already migrated; `python/tsrl/policies/minimal_hybrid.py` and `python/tsrl/selfplay/collector.py` are better next targets than broad repo-wide churn.
