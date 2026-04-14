# ISMCTS Budget Sweep — 2026-04-14
Model: `ppo_v132_sc_league/ppo_iter0010_scripted.pt` (2128 Elo)
Config requested: 8 determinizations, 50 games/side/point

## Summary

- Attempted the requested ISMCTS budget sweep for `ppo_v132_sc_league/ppo_iter0010_scripted.pt`.
- No trustworthy sweep result could be produced for that checkpoint in the current repo state.
- `build-ninja/bindings` is the intended runtime, but older scripted checkpoint families are currently broken there.
- On a newer compatible 6-mode checkpoint (`v210_sc`), raw greedy is plausible while ISMCTS collapses into `scoring_card_held`, so there is a real ISMCTS bug in addition to legacy-checkpoint compatibility issues.

## Status

There is not yet a trustworthy benchmark result for this checkpoint in the current repo state.

The investigation found two different native bindings:

| Binding | Timestamp | Size | MD5 |
|---------|-----------|------|-----|
| `build/bindings/tscore...so` | 2026-04-07 23:47 | 38.5 MB | `1e1b0662790478bbb5ad82e033e48e16` |
| `build-ninja/bindings/tscore...so` | 2026-04-14 00:33 | 42.5 MB | `17a49317136aee42a4b93a9f45c55302` |

These binaries produce radically different and both-suspicious results on the same checkpoint and seeds.

I also attempted to recover a valid sweep using a newer 6-mode checkpoint that matches the current runtime better:

- Candidate: `data/checkpoints/ppo_v210_sc_league/ppo_best_scripted.pt`
- Ladder rating: `v210_sc` Elo `1872.0`
- Raw greedy vs deterministic heuristic on current `build-ninja`: `60.5%` combined (`USSR 70.0%`, `US 51.0%`, `scoring_card_held=14/200`)
- ISMCTS on the same checkpoint, same binary, `8 det × 50 sims`: `0.0%` combined with `97/100` `scoring_card_held` losses

That result is important because it shows the current canonical runtime can produce plausible **raw** benchmark numbers on a newer checkpoint, while the **ISMCTS** path is still catastrophically broken on that same checkpoint.

## Results Snapshot

| Target checkpoint | Binding | Method | Games | Result | Validity | Notes |
|-------------------|---------|--------|-------|--------|----------|-------|
| `ppo_v132_sc_league/ppo_iter0010_scripted.pt` | `build/bindings` | Raw greedy vs deterministic heuristic | `100/side` | `92.5%` combined | Unreliable | Suspiciously strong; stale binary |
| `ppo_v132_sc_league/ppo_iter0010_scripted.pt` | `build/bindings` | ISMCTS `8 det × 50/100/200/400 sims` | `50/side/point` | `76.0%` to `79.0%` combined | Unreliable | Same stale binary |
| `ppo_v132_sc_league/ppo_iter0010_scripted.pt` | `build-ninja/bindings` | Raw greedy vs deterministic heuristic | `20/side` smoke | `0.0%` combined | Invalid | Early `scoring_card_held` pathology |
| `scripted_for_elo/v45_scripted.pt` | `build-ninja/bindings` | Raw greedy / ISMCTS smoke | `small smoke` | `0.0%` raw, pathological ISMCTS | Invalid | Previously healthy family now regressed |
| `ppo_v210_sc_league/ppo_best_scripted.pt` | `build-ninja/bindings` | Raw greedy vs deterministic heuristic | `100/side` | `60.5%` combined | Plausible | Best current sanity-check baseline |
| `ppo_v210_sc_league/ppo_best_scripted.pt` | `build-ninja/bindings` | ISMCTS `8 det × 50 sims` | `50/side` | `0.0%` combined | Invalid | `97/100` `scoring_card_held` losses |

The only currently plausible benchmark number in this document is the raw greedy `v210_sc` baseline. All ISMCTS results should be treated as invalid until the native ISMCTS bug is fixed.

## Which Binary Is Intended

The repo intent is clearly to use `build-ninja/bindings`, not `build/bindings`.

Evidence:
- Shell benchmark/pipeline scripts export `PYTHONPATH=build-ninja/bindings`, including [scripts/run_ismcts_diagnostic.sh](/home/dkord/code/twilight-struggle-ai/scripts/run_ismcts_diagnostic.sh:21).
- Training code explicitly prefers `build-ninja/bindings` and breaks on first match so `build/` cannot shadow it: [scripts/train_ppo.py](/home/dkord/code/twilight-struggle-ai/scripts/train_ppo.py:54).
- Multiple scripts and C++ tools reference `build-ninja` as the standard location.

However, there is at least one import-order footgun:
- [scripts/run_elo_tournament.py](/home/dkord/code/twilight-struggle-ai/scripts/run_elo_tournament.py:40) inserts `build-ninja/bindings` and then immediately inserts `build/bindings` at index 0, which makes the stale `build/` binary win if both exist.

So the intended answer is "use `build-ninja`", but the repo currently has enough path-order ambiguity that some Python entrypoints may silently use the stale `build/` binary instead.

## Benchmark Semantics

- `benchmark_batched(...)` is learned policy vs heuristic by default, or vs greedy NN if `greedy_opponent=True`.
- `benchmark_batched(...)` also has `nash_temperatures=True` by default, which makes the heuristic opponent sample per-game temperatures.
- `benchmark_ismcts(...)` is ISMCTS vs heuristic and does not expose a `nash_temperatures` parameter.
- `benchmark_model_vs_model_batched(...)` is the separate model-vs-model entrypoint.

Relevant source:
- [bindings/tscore_bindings.cpp](/home/dkord/code/twilight-struggle-ai/bindings/tscore_bindings.cpp:994)
- [bindings/tscore_bindings.cpp](/home/dkord/code/twilight-struggle-ai/bindings/tscore_bindings.cpp:1194)
- [cpp/tscore/mcts_batched.hpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/mcts_batched.hpp:171)
- [cpp/tscore/ismcts.hpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.hpp:44)

## ISMCTS Implementation Findings

- ISMCTS uses `determinize(obs, rng)` for each determinization. Hidden cards are sampled by shuffling the unknown-card pool, dealing `opp_hand_size` cards to the opponent, and leaving the remainder as deck.
- ISMCTS does not use rollout backup by default. Leaf evaluation comes from the model value head via `evaluate_leaf_value_raw(...)`.
- The underlying search inside each determinization is full-state PUCT MCTS with `q + u` edge selection.
- Root actions across determinizations are aggregated by action identity and then ranked primarily by total visit count, then prior.

Relevant source:
- [cpp/tscore/game_state.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/game_state.cpp:174)
- [cpp/tscore/search_common.hpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/search_common.hpp:97)
- [cpp/tscore/mcts.hpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/mcts.hpp:44)
- [cpp/tscore/mcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/mcts.cpp:591)
- [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1023)
- [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1477)
- [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1511)
- [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1613)

## Root Cause Investigation

The current evidence points to **two separate problems**:

1. a native backward-compatibility regression for older scripted checkpoints, and
2. a genuine ISMCTS search-path bug on current 6-mode checkpoints.

### 1. What `scoring_card_held` means

`scoring_card_held` is not an internal error string. It is a real game-loss condition emitted when a side reaches cleanup still holding a scoring card:

- [cpp/tscore/game_loop.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/game_loop.cpp:573)
- [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:804)

So the pathological `build-ninja` results mean the runtime is making the model fail to play scoring cards correctly, often immediately in turn 1.

### 2. Recent regression window

Recent C++/binding changes in the likely window:

- `770c6d4` `fix: OpsFirst mode=5 bounds crash when 5-mode fixtures vs 6-mode model`
- `e5ee39c` `fix: backward-compat for old 11-scalar checkpoints with new 32-scalar feature extraction`
- `d0211e1` `WIP: route game loop through hand ops`

Two especially relevant facts:

1. `770c6d4` changed native decode to skip mode index `5` for old 5-mode checkpoints instead of crashing:
   - [cpp/tscore/decode_helpers.hpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/decode_helpers.hpp:301)
   - [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1091)

2. `e5ee39c` only fixed backward compatibility in Python/export paths, not in the native C++ runtime used by `tscore.benchmark_*`:
   - [python/tsrl/policies/learned_policy.py](/home/dkord/code/twilight-struggle-ai/python/tsrl/policies/learned_policy.py:190)
   - [cpp/tools/export_baseline_to_torchscript.py](/home/dkord/code/twilight-struggle-ai/cpp/tools/export_baseline_to_torchscript.py:44)

That means native `tscore` is still exposed to checkpoint-family mismatches that Python learned-policy code now handles explicitly.

### 3. Checkpoint-family pattern

The failing/succeeding pattern is highly structured:

| Checkpoint family | Example | Mode head | Native result on current `build-ninja` |
|------------------|---------|-----------|----------------------------------------|
| Legacy 5-mode, 74-scalar-extended | `ppo_v132_sc_league/ppo_iter0010_scripted.pt` | `(5, 256)` | Runs, but pathological early `scoring_card_held` losses |
| Legacy 5-mode, 74-scalar-extended | `scripted_for_elo/v45_scripted.pt` | `(5, 256)` | Runs, but pathological early `scoring_card_held` losses |
| Older 11-scalar family | `v99_saturation_2x_47ep/baseline_best_scripted.pt` | older arch | Crashes with scalar shape mismatch `4x32 @ 11x64` |
| Newer 6-mode family | `ppo_v205_sc_league/ppo_best_scripted.pt` | `(6, 256)` | Runs without the universal early-loss pathology |

Concrete probes:

- `ppo_v132_sc_league/ppo_iter0010_scripted.pt`
  - `mode_head.weight = (5, 256)`
  - `scalar_encoder.weight = (64, 74)`
- `scripted_for_elo/v45_scripted.pt`
  - `mode_head.weight = (5, 256)`
  - `scalar_encoder.weight = (64, 74)`
- `ppo_v205_sc_league/ppo_best_scripted.pt`
  - `mode_head.weight = (6, 256)`
  - `scalar_encoder.weight = (64, 74)`

This strongly suggests:

- 11-scalar compatibility is still broken in native C++.
- 5-mode compatibility was changed from "hard crash" to "soft but pathological behavior" by the mode=5 skip guard.
- Newer 6-mode scripted checkpoints are the only family that currently appears compatible with the current native runtime.

### 4. Legacy-checkpoint compatibility root cause

Most likely compatibility root cause: **the current `build-ninja` binary is only partially backward-compatible with older scripted checkpoints after the 6-mode `EventFirst` migration and scalar-feature migration.**

This is an inference from the source and the checkpoint-family pattern:

- The old 5-mode crash (`index 5 out of bounds for dimension 0 with size 5`) was explicitly "fixed" by skipping the new mode in native decode.
- But skipping the new mode is a minimal safety guard, not a full compatibility layer.
- Older checkpoints were trained before the new action-mode / hand-op routing semantics, so they can now decode legal-but-behaviorally-wrong moves often enough to hold scoring cards and lose immediately.
- Separately, the 11-scalar fix landed only in Python/export code, so native `tscore` still feeds incompatible scalar tensors to that older family.

In short:

1. **11-scalar models**: still natively incompatible.
2. **5-mode legacy models**: no longer crash, but native compatibility is behaviorally broken.
3. **6-mode newer models**: appear to be the intended compatible target for the current binary.

### 5. ISMCTS bug: `scoring_card_held`

On newer 6-mode checkpoints like `v210_sc`, the source now points to a real ISMCTS bug rather than just a checkpoint-format mismatch.

The root action apply path itself looks reasonable:

- `benchmark_ismcts(...)` calls `play_ismcts_matchup_pooled(...)`: [bindings/tscore_bindings.cpp](/home/dkord/code/twilight-struggle-ai/bindings/tscore_bindings.cpp:1194)
- finished searches are aggregated with `aggregate_result(...)`, which selects `best_action` from `det.root->applied_actions`: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1506)
- the chosen live action is applied through `commit_selected_action(...)` and then `apply_action_live(...)`: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:935)

That means the catastrophic `scoring_card_held` losses are not primarily caused by a broken final handoff from search to live play.

The deeper problem is the **tree transition model** used inside ISMCTS:

- `select_to_leaf(...)` repeatedly advances search states via `apply_tree_action(...)`: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:658)
- `apply_tree_action(...)` only:
  - removes the card from hand,
  - calls `apply_action_live(...)`,
  - flips `pub.phasing` to the other side: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:150)

What it does **not** do is run the real game-loop machinery that exists in the live benchmark path:

- no AR progression via `advance_after_action_pair(...)`: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:853)
- no headline/extra-AR/cleanup stage progression via `advance_until_search_or_done(...)`: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1251)
- no `finish_turn(...)` cleanup and therefore no in-tree `scoring_card_held` terminal detection: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:743)

So the live benchmark loop enforces "play your scoring cards before cleanup", but the ISMCTS tree does not model that obligation inside search. Search is evaluating a simplified alternating-action process instead of the real turn structure. That makes it entirely plausible for search to prefer lines that postpone scoring cards, which then lose immediately when the real outer game loop reaches cleanup.

This matches the observed discriminator:

- raw greedy on `v210_sc` is plausible on the same current binary (`60.5%` combined)
- ISMCTS on `v210_sc` collapses into `97/100` `scoring_card_held` losses at `8 det × 50 sims`

### 6. Secondary 6-mode mismatch: `EventFirst` is missing from ISMCTS drafts

There is also a current-model action-space mismatch that specifically hurts 6-mode checkpoints:

- the canonical legal-mode helper includes `ActionMode::EventFirst = 5`: [cpp/tscore/types.hpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/types.hpp:23), [cpp/tscore/legal_actions.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/legal_actions.cpp:210)
- raw greedy decoding uses `legal_modes(...)` and therefore sees `EventFirst` when legal: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:1079)
- but ISMCTS `collect_card_drafts(...)` only builds `Influence`, `Coup`, `Realign`, `Space`, and `Event`; it never adds `EventFirst`: [cpp/tscore/ismcts.cpp](/home/dkord/code/twilight-struggle-ai/cpp/tscore/ismcts.cpp:260)

So current 6-mode checkpoints are being searched under a 5-mode draft space in ISMCTS even when the live engine and raw greedy path support the 6th mode. That is a separate search-quality bug and likely compounds the transition-model problem above.

## Smoke Results

### `build/bindings` (older binary)

This older binary produces implausibly strong results for the checkpoint.

- `benchmark_batched(..., nash_temperatures=False)` on 100 games/side:
  - USSR `98.0%`
  - US `87.0%`
  - Combined `92.5%`
- Previous full ISMCTS sweep on this binary:
  - `50` sims: `78.0%` combined
  - `100` sims: `79.0%` combined
  - `200` sims: `78.0%` combined
  - `400` sims: `76.0%` combined

Per-game sanity checks on this binary:

```text
benchmark_batched, learned_side=USSR, n_games=10, seed=50000, nash_temperatures=False
Side.USSR 24 5 europe_control
Side.USSR 20 5 europe_control
Side.USSR 23 5 europe_control
Side.USSR 23 6 europe_control
Side.USSR 22 6 europe_control
Side.USSR 21 7 vp
Side.USSR 21 7 vp
Side.USSR 20 7 vp
Side.USSR 20 7 vp
Side.US -5 10 turn_limit
```

```text
benchmark_ismcts, learned_side=USSR, n_games=5, seed=50000, n_det=8, n_sim=50
Side.USSR 21 6 europe_control
Side.USSR 23 6 europe_control
Side.USSR 20 8 europe_control
Side.USSR 21 8 europe_control
Side.US -13 10 turn_limit
```

### `build-ninja/bindings` (current rebuilt binary)

This binary produces the opposite pathology: the same checkpoint loses essentially every game and often terminates early with `scoring_card_held`.

- `benchmark_batched(..., nash_temperatures=False)` on 20 games/side:
  - USSR `0.0%`
  - US `0.0%`
  - Combined `0.0%`

Per-game sanity checks on this binary:

```text
benchmark_batched, learned_side=USSR, n_games=10, seed=50000, nash_temperatures=False
Side.US 4 1 scoring_card_held
Side.US 10 1 scoring_card_held
Side.US 0 1 scoring_card_held
Side.US 3 1 scoring_card_held
Side.US 12 1 scoring_card_held
Side.US 1 1 scoring_card_held
Side.US 7 1 scoring_card_held
Side.US -1 2 scoring_card_held
Side.US -2 3 scoring_card_held
Side.US 5 3 scoring_card_held
```

```text
benchmark_ismcts, learned_side=USSR, n_games=5, seed=50000, n_det=8, n_sim=50
Side.US 9 1 scoring_card_held
Side.US 0 1 scoring_card_held
Side.US -1 1 scoring_card_held
Side.US -15 3 scoring_card_held
Side.US -4 4 scoring_card_held
```

### `build-ninja` on a previously known-good checkpoint

The breakage is not limited to the new league checkpoint. A small smoke test on `data/checkpoints/scripted_for_elo/v45_scripted.pt` also fails under the current `build-ninja` binary:

```text
v45 build-ninja raw: USSR=0.0% US=0.0% Combined=0.0%
ussr_games [(Side.US, 4, 1, scoring_card_held), ...]
us_games   [(Side.USSR, 1, 1, scoring_card_held), ...]
```

```text
benchmark_ismcts(v45), learned_side=USSR, n_games=3
[(Side.US, 0, 1, scoring_card_held),
 (Side.US, -5, 3, scoring_card_held),
 (Side.US, -20, 4, europe_control)]
```

That is especially suspicious because earlier analysis artifacts in this repo report sane `build-ninja` behavior for `v45`:
- [ismcts_retest_post_fix.md](/home/dkord/code/twilight-struggle-ai/results/analysis/ismcts_retest_post_fix.md:1) reports `94.5%` combined for `v45` ISMCTS on 2026-04-12.
- [opus_analysis_20260411_041000_ismcts_v45_readiness.md](/home/dkord/code/twilight-struggle-ai/results/analysis/opus_analysis_20260411_041000_ismcts_v45_readiness.md:1) reports plausible smoke results for `v45` on 2026-04-11.

This strongly suggests a regression in the current native runtime rather than a problem unique to `ppo_v132_sc_league`.

### Current `build-ninja` on a newer 6-mode checkpoint (`v210_sc`)

This is the most useful current discriminator because it separates raw-policy behavior from ISMCTS behavior on the same checkpoint.

- Checkpoint: `data/checkpoints/ppo_v210_sc_league/ppo_best_scripted.pt`
- Ladder Elo: `1872.0`
- Quick raw screen on current `build-ninja`:
  - `USSR 8/10`, `US 4/10`, combined `60.0%`, `0/20` `scoring_card_held` in the initial smoke
- Full raw baseline on current `build-ninja`:
  - `USSR 70.0%`
  - `US 51.0%`
  - `Combined 60.5%`
  - `scoring_card_held=14/200`

So the raw benchmark path is at least plausibly usable on this newer family.

But ISMCTS on that same checkpoint is still broken:

```text
benchmark_ismcts(v210_sc), 8 det × 50 sims, 50 games/side
USSR: 0.0%  US: 0.0%  Combined: 0.0%  scoring_card_held=97/100  (3.7min)
```

Per-game sanity check:

```text
benchmark_ismcts(v210_sc), learned_side=USSR, n_games=5, seed=50000, n_det=8, n_sim=50
[(Side.US, 1, 1, scoring_card_held),
 (Side.US, -13, 2, scoring_card_held),
 (Side.US, -1, 1, scoring_card_held),
 (Side.US, -3, 4, scoring_card_held),
 (Side.US, 5, 6, scoring_card_held)]
```

This means the current blocker is now more specific:
- older checkpoints are broadly incompatible with the native runtime
- newer 6-mode checkpoints can benchmark raw policy plausibly
- but the ISMCTS path itself still fails catastrophically even on a newer compatible checkpoint

## Interpretation

This now looks like a genuine ISMCTS implementation bug, not a simple benchmark-configuration mistake.

- The benchmark API meanings are now clear and are not the source of ambiguity.
- ISMCTS is using the model value head, standard determinization, and PUCT-style root search as expected.
- But the search tree is not simulating the real turn/cleanup mechanics, so forced scoring-card losses are invisible during search.
- On current 6-mode models, ISMCTS also omits the legal `EventFirst` mode from its draft action space.
- The runtime inconsistency problem still exists for legacy checkpoints: the older `build/bindings` binary gives unrealistically strong raw-policy results, while the current `build-ninja/bindings` binary regresses older scripted families badly.

Because both bindings behave implausibly and disagree dramatically on older checkpoint families, the current repo still does not have a reliable native benchmark path for `ppo_v132_sc_league`. But for newer 6-mode checkpoints like `v210_sc`, the evidence is now specific enough to say the ISMCTS path itself is broken even when the raw greedy path is plausible.

The timing also lines up with a likely regression window:
- `build/bindings` was built on 2026-04-07, before the Apr 14 head-shape / backward-compat changes.
- `build-ninja/bindings` was rebuilt on 2026-04-14 after commits such as:
  - `fffb3f2` 2026-04-14 01:03:33 `fix: update test expectations and dataset for 6-mode head (EventFirst=5)`
  - `e5ee39c` 2026-04-14 01:34:12 `fix: backward-compat for old 11-scalar checkpoints with new 32-scalar feature extraction`

So the likely situation is:
1. `build-ninja` is the intended binary.
2. The current `build-ninja` runtime has regressed older scripted checkpoints.
3. Some Python benchmark scripts may accidentally import stale `build/`, which can hide that regression and produce misleadingly different numbers.
4. Even for newer 6-mode checkpoints where raw greedy behaves plausibly, the current ISMCTS path still appears broken.

## Blocker

What blocks a valid sweep right now:

1. **Canonical runtime is broken for legacy checkpoints.**
   The intended binding is `build-ninja/bindings`, but it currently produces pathological early `scoring_card_held` losses even on previously healthy legacy checkpoints like `v45_scripted.pt`.

2. **ISMCTS is broken even on a newer compatible checkpoint.**
   On `v210_sc`, raw greedy is plausible but ISMCTS collapses into `scoring_card_held`, which points to a search-path defect rather than just checkpoint incompatibility.

3. **Fallback runtime is stale and not trustworthy.**
   `build/bindings` predates the recent engine/head changes and gives implausibly strong raw-policy results. It is useful as a contrast signal, but not safe as the final benchmark backend.

4. **Script import order can silently select the wrong binary.**
   At least one benchmark/tournament script can accidentally prefer `build/bindings`, which contaminates confidence in any result produced without explicitly printing `tscore.__file__`.

What needs to be fixed before rerunning the sweep:

1. Fix the native ISMCTS tree transition model so search states advance through real AR/cleanup semantics instead of simple side alternation.
2. Add `EventFirst` to the ISMCTS draft/action construction path so 6-mode checkpoints are searched under the correct legal mode space.
3. Make `build-ninja/bindings` healthy again for legacy scripted checkpoints (`v45`, `ppo_v132_sc_league`, likely other 5-mode / older-scalar families).
4. Remove or fix path-order ambiguity so scripts cannot silently import stale `build/`.
5. Add a mandatory sanity check to benchmark scripts that prints `tscore.__file__` and a 1-2 game smoke result before launching long runs.

## Action Items

1. Fix the ISMCTS tree transition model so search states follow real turn structure, including AR progression, cleanup, and `scoring_card_held` terminal handling.
2. Add `ActionMode::EventFirst` to ISMCTS draft/action construction so 6-mode checkpoints are searched under the correct legal mode space.
3. Restore explicit native compatibility for legacy 5-mode and 11-scalar scripted checkpoints, or reject them loudly instead of running broken benchmarks.
4. Fix script import order so `build/bindings` cannot shadow `build-ninja/bindings`.
5. Rerun a tiny smoke on `v210_sc` after the ISMCTS fix, then rerun the full budget sweep only if the smoke is sane.

## Next Step

Before rerunning any ISMCTS budget sweep, the search-path bug needs to be fixed first. The strongest current evidence is:

- raw greedy on `v210_sc` is plausible (`60.5%` combined),
- ISMCTS on that same checkpoint is not (`0.0%` combined, `97/100` `scoring_card_held` losses at 50 sims).

So the next debugging target should be the native ISMCTS tree transition/action-space logic on compatible 6-mode checkpoints, while separately restoring explicit backward compatibility or hard rejection for older checkpoint families.
