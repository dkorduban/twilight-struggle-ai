# Clean Architecture Status and Pragmatic Path Forward

Date: 2026-04-13

## Scope

This assessment reconciles:

- `docs/architecture-refactoring.md`
- `results/analysis/opus_analysis_20260413_180300_ws6_coupling.md`
- `results/analysis/opus_analysis_20260413_ws6_arch_refactor_plan.md`
- `results/analysis/opus_analysis_20260413_202000_engine_refactor_master_plan.md`
- `results/analysis/opus_analysis_20260413_220000_decoupling_first_vs_gaps.md`
- `docs/observation_interface.md`
- `results/continuation_plan.json`
- recent commits around `c97a431`, `93df7db`, `a83e79e`, `39c346a`
- live code in `cpp/tscore/`, `bindings/`, and the benchmark-only `cpp/mcts_batched_fast/`

The question is not whether the repo matches a textbook clean architecture ideal. The useful question is:

1. how clean the live production path already is
2. where the remaining responsibility leaks and duplication actually are
3. what sequence improves separation without destabilizing the corrected engine

## Executive Summary

The repo is materially closer to a clean architecture than `docs/architecture-refactoring.md` implies, because that document was inspired by a different upstream codebase with heavier OO coupling. In this repo, the state model is already value-based, `ActionEncoding` is already the de facto action ABI, legality is mostly centralized, the Python engine is now explicitly deprecated, and `Observation` has already landed.

It is still not close to "perfect concern separation / zero duplication". The live `tscore` path is roughly halfway to a pragmatic clean architecture:

- strong on state representation and deterministic transition primitives
- mixed on runtime orchestration ownership
- weak on search-layer deduplication and observation-typed boundaries

The main architectural debt is no longer "invent a whole new architecture". The main debt is:

1. `game_loop.cpp` still owns hand-dependent rule logic that should live behind the engine transition boundary
2. search backends and greedy NN decode paths still duplicate substantial semantic logic
3. `Observation` exists, but most search and policy helpers still operate on `GameState` or ad hoc `(PublicState, CardSet, bool)` tuples instead of an explicit observed view

The lowest-regression path is to finish remaining correctness work first, then deduplicate semantic helper code, then push `Observation` through read-only search/policy paths, and only after that move the remaining hand-dependent event logic out of `game_loop.cpp`.

## Reality Check vs Earlier Analyses

Some April 13 analyses are already stale relative to the code that shipped later that day.

### Things that are now true in live code

- `Observation` exists in `cpp/tscore/game_state.hpp`, with `make_observation()` implemented in `cpp/tscore/game_state.cpp`.
- ISMCTS now uses that support mask for opponent-hand-size and determinization setup (`c97a431`, `93df7db`).
- the old `mcts_search_impl.hpp` is not live code anymore; it was archived as `results/archive/mcts_search_impl.hpp.dead` in `39c346a`
- the Python engine is no longer the intended authority; `python/tsrl/engine/DEPRECATED.md` points callers to `tscore`, and bindings were expanded in `a83e79e`
- `results/continuation_plan.json` says engine refactor phases 0-5 are effectively complete and only `GAP-005` remains open

### Earlier findings that still hold

- `game_loop.cpp` still mixes orchestration with rule execution
- `mcts.cpp`, `ismcts.cpp`, and `mcts_batched.cpp` still duplicate search-support logic
- learned-policy decode logic is still mirrored inside batched search rollout / greedy code
- the observation boundary is still only partially adopted

## Current Architecture: What Is Already Clean

### 1. Core state and action model are in good shape

The repo already has several of the properties that the inspiration document wanted:

- `PublicState` is a compact public board snapshot
- `GameState` extends that with hidden hands, deck, phase, and loop state
- `ActionEncoding` is a stable value type with equality, not a polymorphic move hierarchy
- `Pcg64Rng` is explicit and deterministic instead of hidden global randomness

That means this repo does not need an `ActionId` / `ActionCodec` project just to escape pointer-heavy move plumbing. `ActionEncoding` already fills most of that role.

### 2. Transition logic is mostly centralized in `step.cpp`

`step.cpp` is already the closest thing to a clean engine core:

- `choose_option`, `choose_country`, `choose_card`
- `apply_war_card`
- `apply_event`
- `apply_action`
- `check_vp_win`

That file is large, but its responsibility is coherent: apply one action or event against state and RNG. It is not the main architectural problem.

### 3. Legality and heuristic policy are mostly separated

`legal_actions.cpp` is a distinct legality layer. `policies.cpp` consumes legality plus public state and hand to rank actions. That is a healthy direction:

- legality does not depend on concrete search backends
- heuristic policy is runtime-selected through `PolicyKind` / `choose_action`
- the action ABI exposed to policy code is already plain `ActionEncoding`

### 4. Cross-language direction is now correct

The live architectural direction is "C++ engine first, Python bindings as surface", not "two engines in parallel". That is the right direction for maintainability:

- `python/tsrl/engine/` is deprecated
- `bindings/tscore_bindings.cpp` exposes `Observation`, legality helpers, whole-game APIs, traced play, and search entrypoints

This migration is incomplete, but the direction is correct.

## Current Architecture: Where Separation Still Leaks

### 1. `game_loop.cpp` still owns engine semantics

This is the biggest live concern-separation problem.

`game_loop.cpp` still contains:

- `apply_ops_randomly_impl`
- `apply_hand_event`
- `apply_action_with_hands`
- extra-AR / NORAD / Glasnost mechanics that reach into state mutation

This means the runtime loop is still doing more than scheduling phases. It is also acting as a second transition layer for hand-dependent or loop-sensitive effects.

The clearest symptom is the split between:

- `step.cpp::apply_event` for most events
- `game_loop.cpp::apply_hand_event` for Cat-C and other hand-sensitive event handling

That split may be necessary mechanically right now, but architecturally it is still a leak. A clean runtime loop should orchestrate turns and ask the engine to apply stateful transitions; it should not itself be a rules module.

### 2. Search support logic is still triplicated

Across `mcts.cpp`, `ismcts.cpp`, and `mcts_batched.cpp`, the repo still repeats the same categories of logic:

- `ModeDraft`, `CardDraft`, `ExpansionResult`, `SelectionResult`
- `apply_tree_action`
- `rollout_value`
- `evaluate_leaf_value_raw`
- `AccessibleCache`
- card-draft / compact-legal-card collection
- country-logit to action-resolution logic

This is not harmless boilerplate. It is semantic duplication in the search adapter layer.

The production risk is not that the node layouts differ. Specialized node layouts are fine. The risk is that legal-card filtering, DEFCON safety, accessible-country masking, and decode semantics drift across files.

### 3. `learned_policy.cpp` and `mcts_batched.cpp` duplicate the same NN decode semantics

This is the clearest live duplication.

`mcts_batched.cpp` explicitly says its greedy decode path is an "Exact mirror of `TorchScriptPolicy::choose_action` logic from `learned_policy.cpp`". That is useful for proving intent, but it is still duplication of semantic logic:

- masked card selection
- DEFCON safety filtering
- mode filtering
- country-head decoding
- influence allocation decoding
- heuristic fallback behavior

This should not live in two active implementations.

### 4. `Observation` exists, but the repo is not observation-shaped yet

`Observation` is real now, but it is still mostly a stepping stone.

Today:

- policies still consume `(PublicState, CardSet, bool, rng)` through `PolicyFn`
- `mcts.cpp` still directly consumes `GameState`
- `ismcts.cpp` only uses `Observation` to compute a support mask before rebuilding a determinization
- `mcts_batched.cpp` still snapshots and batches directly from `GameState`

There is also an explicit boundary leak in the public runtime API: `game_loop.hpp` keeps a ref-based traced-play entrypoint documented for cases where `PolicyFn` "needs access to the same GameState being played". That is pragmatic, but it confirms that full-state reach-through is still a supported pattern rather than a rare escape hatch.

So the information-regime split exists conceptually, but it is not yet the dominant type boundary in the search layer.

There is also one practical gap: `Observation` carries support, but not an explicit hidden-count summary. ISMCTS still derives the opponent hand size from full state plus support/deck information. That is better than before, but not a fully observation-driven root API.

### 5. There is still runtime duplication outside the core loop

The repo has multiple orchestration layers:

- `game_loop.cpp` whole-game loop
- `ismcts.cpp` pooled benchmark state machine
- `mcts_batched.cpp` pooled self-play / benchmark state machine
- `cpp/mcts_batched_fast/fast_mcts_batched.cpp` benchmark-only fork

This does not mean all of them should be collapsed into one generic runner. Batched search needs specialized control flow. But there is repeated turn/headline/action-round/cleanup logic that still leaks runtime responsibility across modules.

### 6. `cpp/mcts_batched_fast/` is real debt, but not live-product debt

The fast subtree is not built into the root `tscore` target. Root `CMakeLists.txt` includes `cpp/tscore`, tools, and bindings, but not `cpp/mcts_batched_fast/`.

That makes `cpp/mcts_batched_fast/` a lower-priority architectural concern:

- it is real duplication
- it is not on the default production path
- it should not drive the first round of refactoring

If revived later, it should either be clearly labeled as experimental or rebased on the shared search-support layer built for `tscore`.

## How Close Is the Repo Today?

Using "perfect concern separation / clean API / zero duplication" as the bar:

| Area | Status | Notes |
|---|---|---|
| State model and action ABI | Strong | `PublicState`, `GameState`, `ActionEncoding`, explicit RNG are already clean |
| Pure transition core | Moderate-strong | `step.cpp` is coherent, but not the only transition path |
| Runtime orchestration | Moderate-weak | `game_loop.cpp` still owns hand/event semantics |
| Search backend layering | Weak | heavy duplication across `mcts`, `ismcts`, `mcts_batched`, and greedy decode paths |
| Observation boundary | Moderate-weak | type exists, but is not yet the dominant search boundary |
| Python/C++ ownership | Moderate-strong | direction is correct, migration still incomplete |
| Whole-repo duplication including benchmark fork | Weak | live path is better than total tree |

Overall judgment:

- live `tscore` path: about 5.5/10 against a pragmatic clean-architecture target
- whole repo including side forks and mirrored decode logic: about 4.5/10

That is not close to "perfect". It is, however, much better than the inspiration document's starting point and does not call for a full architectural rewrite.

## What Still Needs To Be Done

### Highest-value live work

1. reduce duplicated search semantics
2. make `Observation` the read-only search boundary
3. move the remaining hand-dependent event logic behind the engine transition layer

### Lower-value or already-solved work

- introducing a new `ActionId` layer: low value here; `ActionEncoding` already works
- splitting the project into many CMake libraries: low value for current scale
- building a generic `MatchRunner` / service framework first: too much blast radius for too little gain
- forcing all fast backends into one node layout: wrong target

## Best Pragmatic Path Forward

The right target is not "zero duplication everywhere". The right target is:

- one authoritative semantics path
- one clear observation boundary for read-only search/policy work
- specialized hot-path storage/layout where it buys speed

### Phase 0: Keep correctness and architecture work separate

If `GAP-005` is still genuinely open, finish it before structural cleanup or at least do not mix it into the same patch series.

Reason:

- recent engine correctness work is still settling
- structural refactors are easier to verify when behavior is frozen
- separating them preserves bisectability and keeps regressions diagnosable

### Phase 1: Deduplicate the learned-action decode path first

First target:

- `cpp/tscore/learned_policy.cpp`
- greedy / rollout decode in `cpp/tscore/mcts_batched.cpp`

Why this first:

- it is explicit live duplication
- it is narrow enough to refactor without touching search tree layout
- it removes one of the most bug-prone "mirror logic" seams

Practical shape:

- extract a small shared helper for masked card/mode/country decode
- keep `TorchScriptPolicy` and batched rollout callers as thin wrappers
- preserve exact fallback behavior and DEFCON safety rules

### Phase 2: Extract a shared search-support layer for semantic helpers only

Do not try to unify the whole search backends. Only unify the semantic adapter layer.

Candidates:

- `apply_tree_action`
- `rollout_value`
- `evaluate_leaf_value_raw`
- `AccessibleCache`
- legal-card / card-draft collection
- country-logit action resolution

Do not unify:

- node structs
- compact edge storage
- batching strategy
- pending-expansion scheduling
- pool management

This follows the right compromise: common protocol, specialized kernels.

### Phase 3: Push `Observation` through read-only interfaces

Do not change the public `PolicyFn` surface first. That would ripple through tools, bindings, benchmarks, and tests.

Instead:

1. add a small internal observation-view helper
2. make legality/search/feature helpers accept that observation-shaped input
3. keep `PolicyFn(const PublicState&, const CardSet&, bool, Pcg64Rng&)` as an adapter at the boundary

This gives most of the separation benefit without destabilizing callers.

Immediate goals:

- root decision snapshots become observation-based
- batched feature filling reads from observation-shaped inputs
- ISMCTS root code stops depending on full `GameState` except for determinization
- remaining full-state search access becomes deliberate and obvious

### Phase 4: Move hand-dependent event execution out of `game_loop.cpp`

Only after the observation/read-path cleanup should the repo attack the remaining runtime/engine split.

Target outcome:

- `game_loop.cpp` becomes mostly phase scheduling, tracing, and turn cleanup
- hand-sensitive event execution moves into a stateful engine transition module
- `apply_action_with_hands` stops being a second engine core hidden inside the loop

This is the highest-value concern-separation win, but it should happen after the read-only boundaries are clearer.

### Phase 5: Decide what to do with `cpp/mcts_batched_fast/`

After the live `tscore` path is cleaner:

- either keep `cpp/mcts_batched_fast/` clearly experimental and out of mainline architecture accounting
- or rebase it on the shared semantic helpers from Phases 1-2

Do not refactor it in parallel with live-path cleanup.

### Phase 6: Continue Python-engine removal, but keep it out of core refactors

The binding surface is now broad enough that migration can continue incrementally. That is worth doing, but it should not be tied to search/runtime cleanup patches.

Reason:

- cross-language migration has many callers
- it increases patch size without improving architecture inside `tscore`
- it is easier once the C++ surface stops moving

## Regression-Minimizing Rules

These rules matter more than the exact refactor shape.

1. Never mix correctness changes and structural cleanup in one patch.
2. Lift duplicated code verbatim first; simplify only after tests prove parity.
3. Refactor live `tscore` first, ignore `cpp/mcts_batched_fast/` until the end.
4. Keep `PolicyFn` stable while introducing internal observation-shaped adapters.
5. Preserve `ActionEncoding` as the action ABI; do not invent a new action-id layer now.
6. Add fixed-seed trace comparisons around headline, Cat-C events, extra AR, and batched greedy decode before moving code.

## Recommended Next Concrete Steps

In order:

1. confirm `GAP-005` status and keep architecture work separate from it
2. extract the shared learned-action decode helper used by `learned_policy.cpp` and `mcts_batched.cpp`
3. extract shared search semantic helpers without touching node layouts
4. convert read-only search helper signatures to observation-shaped inputs
5. move `apply_hand_event` and `apply_ops_randomly_impl` behind the engine transition boundary
6. decide whether the benchmark-only fast fork should be archived, ignored, or rebased

## Bottom Line

The repo does not need a top-down architecture rewrite. It already has the right raw ingredients:

- value-type state
- stable action encoding
- deterministic RNG
- mostly centralized legality
- clear C++ ownership direction

What it still lacks is a consistently enforced runtime/search boundary.

The biggest remaining issue is not the absence of grand abstractions. It is that a few critical semantic responsibilities are still duplicated or split across the wrong files:

- hand-sensitive event execution in `game_loop.cpp`
- search-support semantics across `mcts.cpp`, `ismcts.cpp`, and `mcts_batched.cpp`
- learned-policy decode logic mirrored inside batched runtime code

Fix those first, and the repo becomes substantially cleaner without risking a regression-heavy rewrite.
