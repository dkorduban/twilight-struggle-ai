# Python Engine — Deprecated

The Python engine in this directory reimplements game logic that now lives
authoritatively in the C++ engine under `cpp/tscore/`.

**Status:** Deprecated as of 2026-04. Do not add new features here.
**Replacement:** Use the `tscore` pybind11 module from `build-ninja/bindings`.

## What the C++ bindings expose

- Whole-game APIs:
  `play_game`, `play_random_game`, `play_matchup`, `play_traced_game`,
  `play_traced_game_from_seed_words`, `play_traced_game_with_callback`,
  `play_callback_matchup`, `play_dual_callback_matchup`,
  `play_from_public_state`
- Search / rollout / benchmark APIs:
  `benchmark_batched`, `benchmark_mcts`, `benchmark_ismcts`,
  `benchmark_ismcts_vs_model`, `benchmark_ismcts_vs_model_both_sides`,
  `benchmark_mcts_vs_greedy`, `benchmark_model_vs_model_batched`,
  `rollout_games_batched`, `rollout_self_play_batched`,
  `rollout_model_vs_model_batched`, `mcts_search_from_state`,
  `search_from_public_state`
- State / legality helpers added for Python-engine migration:
  `ars_for_turn`, `hand_size_for_turn`, `load_adjacency`,
  `accessible_countries`, `effective_ops`, `legal_cards`, `legal_modes`,
  `legal_countries`, `enumerate_actions`, `has_legal_action`
- Types / summaries:
  `ActionEncoding`, `ActionMode`, `Side`, `GameResult`, `MatchSummary`,
  `Observation`, `StepTrace`, `TracedGame`, `make_observation`,
  `summarize_results`

## Direct replacement paths available now

These files only depend on engine entrypoints that now have direct `tscore`
replacements and can be migrated without waiting for new binding surface:

- `python/tsrl/policies/baseline_iter12.py`
- `python/tsrl/policies/iter10_policy.py`
- `python/tsrl/policies/iter12_policy.py`
- `python/tsrl/policies/measure_end_reasons.py`
- `python/tsrl/policies/minimal_hybrid.py`
- `python/tsrl/policies/tests/test_minimal_hybrid.py`
- `tests/python/test_cpp_events.py`

## Still missing from the Python-friendly C++ surface

Do not remove the Python engine until remaining callers are migrated or the
missing bindings below are added:

- Live-loop internals used by old tests and scripts:
  `_apply_action_with_hands`, `_run_headline_phase`, `_run_action_rounds`,
  `_run_extra_ar`, `_end_of_turn`, `_run_game_gen`, `run_game_cb`
- Python-side mutable state helpers:
  `GameState`, `reset`, `clone_game_state`, `deal_cards`, `_build_era_deck`
- Event / step / scoring primitives:
  `apply_event_card`, `apply_action`, `score_region`,
  `score_southeast_asia`, `apply_scoring_card`
- Python MCTS / vectorized runner / RNG APIs:
  `flat_mcts`, `uct_mcts`, `interleaved_uct_mcts`, `collect_self_play_game`,
  `run_games_vectorized`, `make_rng`
- Adjacency helpers not yet mirrored exactly:
  `neighbors`

## Remaining callers that still need migration

Audit query result: 51 Python files outside `python/tsrl/engine/`.

### `python/tsrl/policies`

- `python/tsrl/policies/autotune_minimal_hybrid.py`
- `python/tsrl/policies/baseline_iter12.py`
- `python/tsrl/policies/benchmark_hybrid_vs_random.py`
- `python/tsrl/policies/benchmark_winrate_symmetric.py`
- `python/tsrl/policies/generate_minimal_hybrid_rollout_logs.py`
- `python/tsrl/policies/iter10_policy.py`
- `python/tsrl/policies/iter12_policy.py`
- `python/tsrl/policies/learned_policy.py`
- `python/tsrl/policies/measure_end_reasons.py`
- `python/tsrl/policies/minimal_hybrid.py`
- `python/tsrl/policies/tests/test_benchmark_hybrid_vs_random.py`
- `python/tsrl/policies/tests/test_minimal_hybrid.py`
- `python/tsrl/policies/tune_minimal_hybrid.py`

### `scripts`

- `scripts/bench_rollout_heuristic.py`
- `scripts/benchmark.py`
- `scripts/benchmark_simple.py`
- `scripts/benchmark_suite.py`
- `scripts/benchmark_throughput.py`
- `scripts/benchmark_vf_mcts.py`
- `scripts/collect_heuristic_selfplay.py`
- `scripts/collect_learned_selfplay.py`
- `scripts/collect_learned_selfplay_batched.py`
- `scripts/collect_learned_vs_heuristic.py`
- `scripts/collect_selfplay.py`
- `scripts/diag_game_trace.py`
- `scripts/diagnose_defcon_causes.py`
- `scripts/diagnose_defcon_failures.py`
- `scripts/diagnose_defcon_v2.py`
- `scripts/investigate_ismcts_defcon.py`
- `scripts/play_server.py`
- `scripts/run_mcts_game.py`
- `scripts/trace_brush_war_coup.py`
- `scripts/validate_defcon_rate.py`
- `scripts/validate_heuristic_defcon.py`

### `tests/python`

- `tests/python/conftest.py`
- `tests/python/test_correctness_fixes.py`
- `tests/python/test_cpp_events.py`
- `tests/python/test_engine.py`
- `tests/python/test_events.py`
- `tests/python/test_events_cat_c.py`
- `tests/python/test_events_cat_f.py`
- `tests/python/test_events_phase2.py`
- `tests/python/test_game_loop.py`
- `tests/python/test_heuristic_defcon_safety.py`
- `tests/python/test_learned_policy.py`
- `tests/python/test_learned_policy_dp.py`
- `tests/python/test_mcts.py`
- `tests/python/test_milops_penalty.py`
- `tests/python/test_policies.py`
- `tests/python/test_scoring.py`
- `tests/python/test_vec_runner.py`

## Notes on `test_engine.py` and `test_game_loop.py`

Those two suites are still primarily Python-engine regression tests against
Python-only helpers and live-loop internals. They were not rewritten in this
phase because there is no one-for-one `tscore` replacement yet for most of the
APIs they exercise, and rewriting them prematurely would reduce current
coverage rather than preserve it.
