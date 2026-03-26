# Claude Code instructions for the Twilight Struggle AI repo

## Goal
Build a strong Twilight Struggle AI with a plausible path to top-1%-human strength on a modest budget using:
- replay warm-start from human logs
- exact C++ state/engine core
- Python/PyTorch training
- selective stronger search / distillation later
- minimum unnecessary complexity in Month 1

Preferred strategy:
- learn a strong offline baseline first
- make public-state reconstruction exact before chasing model quality
- handle hidden information with exact support masks before probabilistic belief machinery
- use local self-play and stronger search only after the reducer/data path is trustworthy
- use cloud bursts only when they buy clear strength per dollar

## Current focus
We are in **Month 1: foundations + offline baseline**.

Highest-priority deliverables, in order:
1. replay grammar and parser
2. exact `PublicState` reducer
3. causal `HandKnowledge` reducer
4. offline smoother for actor-hand labels
5. exact unseen-card support masks
6. dataset builder
7. first small PyTorch policy/value baseline

Do **not** spend time on fancy search, distributed training, architecture experiments, or UI/deployment work until the reducer and dataset path are trustworthy.

## Default working style
- Keep changes small, layer-local, and reversible.
- Prefer one clear interface change over broad rewrites.
- Do not mix parser, engine, dataset, and trainer changes in one pass unless the task explicitly requires it.
- Before editing multiple layers or crossing ownership boundaries, first summarize the intended interface boundary in 3-8 bullets.
- Prefer deterministic scripts and tests over notebooks for anything that will be reused.
- Prefer C++/Python/PyTorch. Do not introduce JAX or Rust unless asked or unless there is a specific, quantified benefit.
- Prefer explicit data models over implicit conventions.
- Prefer boring exact code over clever fragile code.
- Keep online-safe state and offline labels strictly separated.

Before non-trivial changes:
1. restate the task in 2-5 bullets
2. list assumptions / open questions briefly
3. propose the smallest useful implementation slice

When implementing:
- prefer one subsystem at a time
- write tests alongside code, not afterward
- explain non-obvious rule interpretations in comments or docs
- do not refactor unrelated files "while here"
- do not introduce new dependencies without a concrete need

When blocked by ambiguity:
- show the exact ambiguity
- propose the safest assumption
- isolate it behind a test, comment, or config point

When in doubt:
- choose the cheaper, simpler path that preserves future options
- if a change is likely to create hidden bugs, prefer a validator, invariant, or golden test first
- if a task becomes mostly log parsing, dataset QA, or test output triage, delegate to a subagent instead of filling the main context with noise

## Delegation rules
Use built-in agents proactively:
- **Explore** for repo scanning, file discovery, and read-only codebase understanding.
- **Plan** in plan mode for research before proposing a multi-step implementation.

Use project agents proactively:
- **replay-forensics** for replay/log grammar, parser failures, unknown lines, and data-quality audits.
- **rules-lawyer** for official-rules interpretation, edge cases, and regression-test ideas.
- **cpp-engine-builder** for `cpp/`, `include/`, `bindings/`, and `CMakeLists.txt`.
- **dataset-plumber** for ETL, schemas, feature generation, splits, and dataset QA.
- **pytorch-trainer** for dataloaders, models, losses, metrics, and offline/self-play training scripts.
- **eval-referee** for tests, benchmark runs, checkpoint comparisons, and concise failure summaries.
- **architecture-skeptic** only before major design pivots or when complexity is increasing too fast.

## File ownership
Treat these as default ownership boundaries:
- `cpp/`, `include/`, `bindings/`, `CMakeLists.txt` -> `cpp-engine-builder`
- `python/etl/`, `schemas/`, `data_tools/`, `notebooks/` -> `dataset-plumber`
- `python/train/`, `configs/`, `metrics/` -> `pytorch-trainer`
- `docs/rules*`, `docs/rules_decisions.md` -> `rules-lawyer` (read-only unless asked)
- `reports/`, `benchmarks/` -> `eval-referee`

If a task crosses boundaries, name the boundary explicitly before editing.

## Project principles and constraints
- Correctness first.
- Determinism first.
- Small vertical slices.
- Public-state correctness is more important than clever modeling in Month 1.
- Hidden-information features should start with exact support masks before probabilistic belief machinery.
- Preserve reproducibility: deterministic seeds, explicit config files, stable dataset splits, and hashable state snapshots.
- Raw logs are immutable inputs.
- Normalized events and datasets are derived artifacts.
- Prefer flat files / Parquet over unnecessary infra.
- Never vendor or copy GPL parser code directly into the repo.
- Replay/log tooling may be used as a reference oracle, validator, or external preprocessing step, but not copied blindly.

## Game / rules ground truth
Assume competitive / ITS-style Twilight Struggle rules unless explicitly overridden.

Important constants:
- game length is up to 10 turns
- players refill to hand size **8** on turns 1-3
- players refill to hand size **9** on turns 4-10
- the China Card does **not** count toward hand size
- the China Card **does** count as one of the actions taken that turn

If implementation behavior conflicts with rules or replay evidence, stop and surface the conflict clearly.

## Architecture
### Language split
- **C++20**: exact game core, replay reduction, hashing, legality, dataset extraction hot paths
- **Python 3.11+**: ETL, training, evaluation, orchestration
- **PyTorch 2.x**: baseline learning stack
- **pybind11**: C++/Python boundary
- **Parquet / Arrow**: datasets

### Repository shape
Prefer this layout:
- `cpp/tscore/` - exact C++ core
- `python/tsrl/` - Python ETL / training / eval
- `data/raw_logs/` - immutable raw replay logs
- `data/golden_logs/` - curated regression corpus
- `data/parquet/` - derived datasets
- `tests/cpp/`
- `tests/python/`
- `docs/` - specs, replay grammar, notes

Important data files to create early:
- `docs/replay_grammar.md`
- `data/spec/cards.csv`
- `data/spec/countries.csv`
- `data/spec/effects.yaml`

### Core state layers
Maintain three distinct layers:

1. `PublicState`
   - public board state only
   - influence, VP, DEFCON, MilOps, Space, China, discard/removed/public reveals, public effects

2. `HandKnowledge`
   - online-safe hidden-information state for one player
   - derived only from the replay prefix so far
   - known-in-hand, known-not-in-hand, possible-hidden support, hand size, China ownership

3. `OfflineSmoothedLabels`
   - offline-only reconstruction using future observations
   - used for supervised training labels only

**Never leak offline smoother information into online inference state, legality, self-play, or evaluation.**

### Reducer rule
Use event-driven reducers:

`next_state = reduce(prev_state, event)`

Do not encode hand reconstruction as shortcut arithmetic identities. Twilight Struggle has too many special cases; use an explicit event/state machine.

### Core schema expectations
Create explicit schemas early for:
- `ReplayEvent`
- `PublicState`
- `HandKnowledge`
- `OfflineSmoothedLabels`
- `ActionEncoding`
- dataset row / sample schema

Keep `ReplayEvent` explicit and versioned if the schema changes.
Preserve raw replay text alongside normalized events for debugging.

### Model shape for Month 1
Keep the first model simple.

Inputs:
- per-country features
- global game-state features
- actor hand labels from smoother
- opponent hidden-card support mask

Outputs:
- card head
- mode head
- target / allocation head
- value head

Use a **factorized action model**, not one giant flat action vocabulary.

## Out of scope for now
Do not build these in the Month-1 critical path:
- full teacher / root search
- particle filtering in the training loop
- distributed actor fleet
- cloud orchestration
- SQL backends / service infra
- large architecture search
- premature UI / deployment work

## Coding standards
### General
- Prefer explicit names over abbreviations unless the term is standard in TS (`VP`, `DEFCON`, `MilOps`, `AR`).
- Keep functions small and testable.
- Surface invariants with assertions close to the logic.
- When behavior is uncertain, add a TODO plus a failing or xfail test instead of silently guessing.

### C++
- Small structs, explicit enums, pure functions where possible, minimal globals.
- Deterministic serialization and hashing.
- Avoid template-heavy abstractions unless they buy clear value.
- Make hot-path data layouts predictable and simple.
- Keep reducer code branch-explicit and readable.

### Python
- Typed function signatures where practical.
- Scripts runnable from CLI; no notebook-only logic.
- Prefer dataclasses / typed containers for schemas.
- Prefer Polars over pandas when convenient, but do not churn code just for that.

### PyTorch
- Clear input / output contracts.
- Legal-action masking.
- Config-driven training.
- Compact metrics.

### Tests
- Add or update the smallest meaningful test with each change.
- When changing reducers, add or update:
  - at least one focused unit test
  - at least one golden-log or integration regression if behavior changes on real replays

## Replay / data rules
- Split train / val / test by **game**, not by row.
- Avoid leakage across splits from the same game or obviously related duplicates.
- Keep unknown-line bucketing explicit; do not silently drop lines.
- Hand reconstruction must preserve the invariant that `support_mask_false_exclusion_rate == 0`.

Hand-relevant event classes that matter early:
- `headline(card)`
- `play(card)`
- `forced_discard(card)`
- `reveal_hand(cards...)`
- `transfer(card, A -> B)`
- `draw / refill`
- `end_turn_held_reveal(card...)`
- `reshuffle`

## Testing and validation
Every meaningful change should preserve or improve determinism and replay correctness.

Minimum required checks:
- parser tests for known line patterns
- unknown-line bucketing without silent drops
- golden-log replay regression tests
- deterministic state-hash checks
- hand-size accounting checks
- support-mask false exclusion rate must stay **0**
- illegal-action rate after masking must stay **0**

## Metrics that matter early
Track these first.

Parser / reducer:
- `line_parse_coverage`
- `game_ingest_success_rate`
- `unknown_line_count`
- `deterministic_replay_hash_match`
- `public_state_reconstruction_accuracy`

Hand reconstruction:
- `exact_hand_label_rate`
- `partial_hand_label_rate`
- `ambiguous_hand_label_rate`
- `support_mask_false_exclusion_rate`
- `support_mask_avg_size`

Model:
- `card_top1`
- `card_top3`
- `mode_accuracy`
- `target_exact_match` / `target_F1`
- `value_brier`
- `value_calibration`
- `illegal_action_rate_after_masking`

## Optimization order
Optimize for these in order:
1. correct replay ingestion
2. deterministic public-state reconstruction
3. exact unseen-card support masks
4. stable dataset generation
5. simple offline baseline
6. later: search and stronger belief modeling

## First tasks if the repo is still empty
1. create repo skeleton and build / test plumbing
2. freeze card / country / effect dictionaries
3. define `ReplayEvent` schema and replay grammar doc
4. ingest a small golden corpus of replay logs
5. implement parser + parser coverage report
6. implement `PublicState` + deterministic replay hashing
7. implement `HandKnowledge` + exact unseen-card support mask
8. implement offline smoother + label quality tags
9. build first Parquet dataset
10. train first baseline and compare against trivial heuristics

## Definition of done for Month 1
Month 1 is successful only if we have all of the following:
- reliable replay ingestion on a golden corpus
- exact public-state reconstruction
- deterministic state hashing
- causal hand knowledge at every replay prefix
- offline-smoothed actor-hand labels with quality tags
- exact unseen-card support masks
- clean offline dataset
- first baseline model that beats trivial heuristics

## Preferred commands
Target commands for the initial repo:
- configure: `cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo`
- build: `cmake --build build -j`
- C++ tests: `ctest --test-dir build --output-on-failure`
- Python env setup: `uv sync` (installs all deps including dev group)
- Python tests: `uv run pytest`
- Python lint / format: `uv run ruff check . && uv run ruff format .`
- C++ format: `clang-format -i <files>`
- Run a script: `uv run python -m tsrl.etl.parser <args>` or `uv run python scripts/foo.py`

Use `uv` for all Python dependency and environment management:
- Add a runtime dep: `uv add <package>`
- Add a dev dep: `uv add --group dev <package>`
- Never use `pip install` directly; always go through uv

## When this file grows
Keep this file concise. If project guidance becomes too large, move topic-specific instructions into:
- `.claude/rules/` for scoped rules
- `.claude/skills/` for reusable workflows
- `docs/` for detailed specs
