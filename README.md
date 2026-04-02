# twilight-struggle-ai

Twilight Struggle AI research and engineering repo.

The project is building toward a strong Twilight Struggle agent with exact
public-state handling, exact legality, causal hidden-information tracking,
replay ingestion from curated human logs, and training/self-play loops on top
of that foundation.

Today, the repo is primarily a Python codebase with a small C++ core scaffold.
The live engine, replay pipeline, search, policies, and most tests currently
run in Python.

## What Is In This Repository

This repo has four main layers:

1. Replay ETL
   Parse raw Twilight Struggle logs, normalize them into structured events,
   resolve names to canonical IDs, reduce them into state, and build Parquet
   datasets for training and analysis.

2. Live game engine
   Represent public state, generate legal actions, apply actions/events,
   compute scoring, and drive full games for rollouts and self-play.

3. Search and policy code
   Run random rollouts, heuristic rollouts, Monte Carlo / UCT search, and
   learned-policy inference through the current engine API.

4. Training and self-play
   Convert replay and self-play games into a shared row schema, then train a
   small policy/value model for card, mode, target, and value prediction.

## Project Priorities

The codebase is optimized more for correctness and determinism than for model
complexity.

Important design constraints that show up throughout the code:

- Public online state is separate from hidden-information state.
- Offline smoothed labels are separate from online inference state.
- Replay parsing is deterministic.
- Unknown replay lines are preserved instead of silently dropped.
- Legality and action encoding are explicit and testable.
- Human-log rows and self-play rows share one main dataset schema.

## Architecture Overview

### 1. Core schemas

The main contracts live in `python/tsrl/schemas.py`.

Key types:

- `ReplayEvent`
  Normalized event extracted from a replay log.
- `ActionEncoding`
  Factorized move representation: `card_id`, `mode`, and ordered `targets`.
- `PublicState`
  Board-visible information only.
- `HandKnowledge`
  Causal, observer-safe hidden-information state.
- `OfflineLabels`
  Offline-only training labels reconstructed from the full replay.

This separation is central to the project:

- `PublicState` is safe for online inference and legality.
- `HandKnowledge` is safe for online inference under imperfect information.
- `OfflineLabels` are not allowed to leak into online play.

### 2. Replay pipeline

The replay path is:

`raw log -> parser -> resolver -> reducer -> smoother -> dataset rows`

Main modules:

- `python/tsrl/etl/parser.py`
  Parses TSEspionage / ACTS-style logs into `ReplayEvent` objects.
- `python/tsrl/etl/resolver.py`
  Resolves card and country names to canonical IDs from `data/spec/`.
- `python/tsrl/etl/reducer.py`
  Replays normalized events into `PublicState` and `HandKnowledge`.
- `python/tsrl/etl/smoother.py`
  Uses full-game future information to reconstruct better actor-hand labels
  for supervised training.
- `python/tsrl/etl/dataset.py`
  Builds Parquet rows from reduced state plus smoothed labels.
- `python/tsrl/etl/validator.py`
  Cross-checks replay decisions against engine legality and state formulas.

This is one of the most mature parts of the repo and acts as a correctness
anchor for the rest of the system.

### 3. Live engine

The live engine is under `python/tsrl/engine/`.

Important modules:

- `game_state.py`
  Full mutable game state for live play, including hands and deck.
- `legal_actions.py`
  Legal card/mode/target generation.
- `step.py`
  Applies one `ActionEncoding` to public state.
- `events.py`
  Event handlers for standard cards.
- `cat_c_events.py`
  Event handlers that need access to hands and deck.
- `scoring.py`
  Region scoring logic.
- `game_loop.py`
  Full game driver for headline, action rounds, turn transitions, and endgame.
- `mcts.py`
  Flat Monte Carlo, standard UCT, and interleaved batched UCT.
- `vec_runner.py`
  Runs multiple games concurrently while batching learned-side decisions.

The engine currently lives mostly in Python, even though a C++ state core
exists in parallel.

### 4. Policies, training, and self-play

Policy code lives in `python/tsrl/policies/`.

Current policy interface:

`Policy(pub, hand, holds_china) -> ActionEncoding | None`

Main pieces:

- `minimal_hybrid.py`
  Deterministic heuristic rollout policy constrained to the current engine API.
- `learned_policy.py`
  Inference wrapper around a trained model checkpoint.
- `model.py`
  Baseline factorized policy/value network.
- tuning and benchmark scripts
  Local search and diagnostics for rollout-policy quality and speed.

Self-play and training:

- `python/tsrl/selfplay/collector.py`
  Converts self-play games into row dicts matching the replay dataset schema.
- `scripts/train_baseline.py`
  Trains the baseline model on Parquet data.

The shared schema means replay data and self-play data can be mixed more
easily in downstream experiments.

### 5. C++ core status

The C++ side currently provides foundational structs under `cpp/tscore/`:

- `public_state.hpp`
- `hand_knowledge.hpp`
- `types.hpp`

The Python bindings under `bindings/` are still a stub, so the active runtime
path is still Python-first. The C++ layer is better thought of as an exact
engine foundation under construction rather than the main execution backend.

## Data Flow

There are two main data flows in the repo.

### Human replay data

1. Read curated raw logs from `data/raw_logs/`
2. Parse logs into normalized replay events
3. Resolve names against canonical card/country specs
4. Reduce events into public state and hand knowledge
5. Smooth actor hands offline using future observations
6. Emit Parquet rows under `data/parquet/`
7. Train / validate models on those rows

### Self-play data

1. Start from a live `GameState`
2. Choose actions using heuristic policy, learned policy, or MCTS
3. Record decision snapshots
4. Convert snapshots into the same row schema used by replay data
5. Train or evaluate on the generated Parquet rows

## Repository Layout

Top-level directories you will touch most often:

- `python/tsrl/engine/`
  Live engine, action application, legality, scoring, search, vectorized play.
- `python/tsrl/etl/`
  Replay parsing, normalization, reduction, smoothing, dataset building.
- `python/tsrl/policies/`
  Heuristic and learned policy code plus tuning/benchmark helpers.
- `python/tsrl/selfplay/`
  Self-play collection and row emission.
- `python/tsrl/train/`
  Training package area.
- `cpp/tscore/`
  C++ exact-state core scaffold.
- `bindings/`
  pybind11 extension stub for the C++ core.
- `tests/python/`
  Main regression and behavior tests.
- `tests/cpp/`
  Narrow C++ struct sanity tests.
- `data/spec/`
  Canonical cards, countries, and adjacency definitions.
- `data/raw_logs/`
  Curated replay corpus.
- `data/parquet/`
  Derived datasets.
- `scripts/`
  Training, benchmarks, diagnostics, collection, and data-processing entrypoints.
- `docs/`
  Rule notes and replay grammar documentation.

## Setup

### Prerequisites

- Python 3.11+
- `uv`
- CMake 3.21+ and a C++20 compiler if you want to build the C++ targets

### Python environment

Use `uv` for environment management and execution:

```bash
uv sync
```

Common Python commands:

```bash
uv run pytest
uv run pytest tests/python/test_parser.py
uv run ruff check .
uv run ruff format .
```

### C++ configure/build

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build -j
ctest --test-dir build --output-on-failure
```

Note: the pybind11 bindings are not yet functionally meaningful even though the
build system has a bindings target.

## Common Workflows

### Build replay-derived datasets

The ETL code lives in `python/tsrl/etl/`. Depending on the exact script or
entrypoint you are using, the normal sequence is:

1. parse logs
2. resolve names
3. reduce state
4. smooth labels
5. write Parquet

The core dataset builder is `python/tsrl/etl/dataset.py`.

### Validate replay legality

Use `python/tsrl/etl/validator.py` to compare logged human decisions against
the engine's legal action generation and consistency checks.

This is useful when changing:

- legality rules
- scoring formulas
- reducer logic
- replay parsing behavior

### Run a self-play collection pass

The repo includes scripts for both heuristic and learned self-play, for
example under `scripts/collect_selfplay.py`,
`scripts/collect_heuristic_selfplay.py`, and
`scripts/collect_learned_selfplay.py`.

### Train the baseline model

The main training entrypoint is:

```bash
uv run python scripts/train_baseline.py --data-dir data/selfplay --out-dir checkpoints
```

The baseline model predicts:

- card choice
- action mode
- target-country distribution
- state value

## Testing

The Python test suite is the main confidence layer for the repo.

Coverage includes:

- parser behavior
- resolver behavior
- reducer invariants
- scoring
- engine step logic
- event effects
- game loop behavior
- MCTS
- policies
- self-play collection
- dataset and validator logic

Representative commands:

```bash
uv run pytest tests/python/test_engine.py
uv run pytest tests/python/test_parser.py
uv run pytest tests/python/test_mcts.py
```

The C++ tests are currently much smaller in scope and mainly validate default
construction and basic constant assumptions.

## Current Status

The repository is beyond a toy prototype, but it is not yet a finished
production-strength TS engine.

Reasonable description of current maturity:

- replay ETL and state-contract work are relatively mature
- Python engine and legality/event handling are substantial and heavily tested
- heuristic rollout and MCTS infrastructure exist and are usable
- self-play and baseline training loops exist
- C++ core and bindings are still early compared with the Python path

## Development Notes

Some repo conventions are worth knowing up front:

- Prefer small, local, reversible changes.
- Correctness and determinism currently matter more than sophistication.
- Do not silently drop unknown replay lines.
- Keep replay-derived offline labels separate from online inference state.
- Prefer `uv` over ad hoc Python environment management.

## Useful Files To Read First

If you are orienting yourself in the codebase, start with:

- `python/tsrl/schemas.py`
- `python/tsrl/etl/parser.py`
- `python/tsrl/etl/reducer.py`
- `python/tsrl/engine/legal_actions.py`
- `python/tsrl/engine/game_loop.py`
- `python/tsrl/policies/README.md`
- `scripts/train_baseline.py`

## Related Docs

- `docs/replay_grammar.md`
- `docs/event_scope.md`
- `docs/ts_rules_scoring.md`

These complement the code when replay semantics or scoring behavior need to be
checked carefully.
