# Claude Code instructions for the Twilight Struggle AI repo

## Goal
Build a strong Twilight Struggle AI with a plausible path to top-1%-human strength on a modest budget using:
- a small replay warm-start from human logs when available
- an exact C++ state / engine core
- Python / PyTorch training
- earlier self-play and selective stronger search / distillation
- minimum unnecessary complexity in Month 1

Preferred strategy:
- be **engine-first**, not replay-first
- make public-state reconstruction and legality exact before chasing model quality
- treat human logs as a small, high-value seed dataset, not the backbone
- handle hidden information with exact support masks before probabilistic belief machinery
- prepare play-mode / self-play scaffolding in Month 1 so Month 2 does not depend on a large replay corpus
- use teacher search selectively on curated hard states, not everywhere
- use cloud bursts only when they buy clear strength per dollar

## Strategic assumptions
Assume these unless explicitly overridden:
- there is **no guaranteed public bulk replay archive** to rely on
- human logs are **helpful but optional**
- the core long-term strength sources are exact engine quality, self-play, and teacher-generated targets
- replay data is best used for parser validation, opening / headline priors, hand-reconstruction experiments, and eval suites
- the project should build a **private data flywheel** over time:
  - collect every local game log
  - accept opt-in contributed logs
  - parse and deduplicate all logs
  - mine hard positions
  - run teacher search on those positions later
  - distill those targets back into the student

## 3-month arc
### Month 1
Foundations + offline baseline + play-mode scaffold.

### Month 2
Earlier autonomous self-play, sparse teacher search on curated hard states, teacher-target cache, and online evaluation ladder.

### Month 3
Strength push: better distillation quality, league stability, evaluation quality, benchmark report, and release-candidate bot.

## Current focus
We are in **Month 3: strength push, league stability, evaluation quality, and release-candidate bot**.

Highest-priority deliverables, in order:
1. Dirichlet noise at MCTS root + temperature-based action sampling in self-play
2. Self-play exploration noise (epsilon-greedy or policy noise injection)
3. Elo / BayesElo rating system for stable cross-generation evaluation
4. Information-set MCTS (determinization-based) for online play under hidden information
5. Architecture evaluation: benchmark attention model (`TSCountryAttnModel`) vs MLP baseline
6. Parallel MCTS (virtual loss already scaffolded, need multi-threaded search)
7. Online play server (HTTP/WebSocket interface for human or bot opponents)
8. Formal benchmark report vs known baselines

Suggested Month-3 time allocation:
- 30% ISMCTS + exploration noise (biggest strength lever)
- 25% league / Elo evaluation infrastructure
- 20% architecture experiments + distillation quality
- 15% parallel MCTS + online play server
- 10% benchmark report + release polish

Do **not** spend Month-3 time on replay parsing, engine reducer rewrites, or dataset schema changes — those are stable from Month 1-2.

## Default working style
- Keep changes small, layer-local, and reversible.
- Prefer one clear interface change over broad rewrites.
- Do not mix parser, engine, dataset, and trainer changes in one pass unless the task explicitly requires it.
- Before editing multiple layers or crossing ownership boundaries, first summarize the intended interface boundary in 3-8 bullets.
- Prefer deterministic scripts and tests over notebooks for anything that will be reused.
- Prefer C++ / Python / PyTorch. Do not introduce JAX or Rust unless asked or unless there is a specific, quantified benefit.
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

### Skills (preferred paths for implementation and debugging work)
Use these slash-command workflows for most implementation, debugging, and rules work.
They delegate to Codex on the happy path and only escalate to Claude subagents on failure.

- **/spec-writer** — explore codebase + synthesize a tight spec file before coding. Output feeds `/feature-coder` or `/tdd-fixer`.
- **/feature-coder** — implement a spec via Codex (reads spec → Codex implements → verify → code-review).
- **/tdd-fixer** — make failing tests green via Codex without a spec. Happy path ≈4 main turns.
- **/autonomous-debugger** — diagnose and fix a failure or regression via Codex. No spec needed.
- **/rules-batcher** — answer 5-20 rules/card questions in one Haiku agent call (reads PDF + code once).

### Built-in agents
- **Explore** for repo scanning, file discovery, and read-only codebase understanding.
- **Plan** in plan mode for research before proposing a multi-step implementation.

### Project agents (used internally by skills, or directly for specialized work)
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
- Engine / reducer correctness matters more than clever modeling in Month 1.
- Public-state correctness is more important than model quality in Month 1.
- Hidden-information features should start with exact support masks before probabilistic belief machinery.
- Preserve reproducibility: deterministic seeds, explicit config files, stable dataset splits, and hashable state snapshots.
- Raw logs are immutable inputs.
- Normalized events and datasets are derived artifacts.
- Prefer flat files / Parquet over unnecessary infra.
- Never vendor or copy GPL parser code directly into the repo.
- Replay / log tooling may be used as a reference oracle, validator, or external preprocessing step, but not copied blindly.
- Avoid assumptions that depend on having a large human corpus.

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
- **C++20**: exact game core, replay reduction, hashing, legality, play-mode stepping, dataset extraction hot paths
- **Python 3.11+**: ETL, training, evaluation, orchestration
- **PyTorch 2.x**: baseline learning stack
- **pybind11**: C++ / Python boundary
- **Parquet / Arrow**: datasets

### Repository shape
Prefer this layout:
- `cpp/tscore/` - exact C++ core
- `python/tsrl/` - Python ETL / training / eval
- `data/raw_logs/` - immutable raw replay logs
- `data/raw_logs/` - curated regression corpus
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
   - influence, VP, DEFCON, MilOps, Space, China, discard / removed / public reveals, public effects

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

Do not encode hand reconstruction as shortcut arithmetic identities. Twilight Struggle has too many special cases; use an explicit event / state machine.

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

## Replay / data strategy
Treat replay data as a **small boutique dataset**.

Use logs mainly for:
- opening / headline priors
- parser validation
- action-factorization debugging
- actor-hand smoothing experiments
- eval suites

Preferred data tiers:
1. your own logged Playdek / TSEspionage games
2. parser test logs and public sample logs
3. opt-in contributed logs from collaborators / stronger players
4. weakly structured human material only later, if clearly worth it

Do not design the repo around the assumption that tens of thousands of clean logs will appear.

## Permanently out of scope / not supported
- **Promo cards** (Lone Gunman #109, Colonial Rear Guards #110, Panama Canal Returned #111): IDs exist in cards.csv for log-parsing completeness, but their event effects are **not implemented** and they are excluded from self-play and training. Do not implement promo card events.

## Out of scope for now
Do not build these in the Month-1 critical path:
- full teacher / root search
- particle filtering in the training loop
- distributed actor fleet
- cloud orchestration
- SQL backends / service infra
- large architecture search
- premature UI / deployment work

But do build enough for Month 2:
- legal-action API
- play-mode stepping / transition scaffold
- clean interfaces for later self-play and teacher labeling

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
- Tests run in parallel by default (`-n auto`).  Keep tests
  stateless and side-effect free.  Use `@pytest.mark.serial` only for tests
  that truly require serial execution (shared filesystem writes, ordering
  dependencies).  Use `tmp_path` (pytest fixture) for any test that writes
  files so workers get isolated directories automatically.

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
Every meaningful change should preserve or improve determinism, legality, and replay correctness.

Minimum required checks:
- parser tests for known line patterns
- unknown-line bucketing without silent drops
- golden-log replay regression tests
- deterministic state-hash checks
- hand-size accounting checks
- support-mask false exclusion rate must stay **0**
- illegal-action rate after masking must stay **0**
- legal-action API consistency checks for play-mode scaffolding

## Metrics that matter early
Track these first.

Parser / reducer:
- `line_parse_coverage`
- `game_ingest_success_rate`
- `unknown_line_count`
- `deterministic_replay_hash_match`
- `public_state_reconstruction_accuracy`
- `legal_action_api_consistency`

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
1. exact engine / reducer correctness
2. deterministic replay ingestion and public-state reconstruction
3. exact unseen-card support masks and causal hand knowledge
4. stable dataset generation from a small curated corpus
5. simple offline baseline
6. legal-action / play-mode readiness for self-play
7. later: teacher-generated targets, self-play league, and stronger belief modeling

## First tasks if the repo is still empty
1. create repo skeleton and build / test plumbing
2. freeze card / country / effect dictionaries
3. define `ReplayEvent` schema and replay grammar doc
4. ingest a **small golden corpus** of replay logs
5. implement parser + parser coverage report
6. implement `PublicState` + deterministic replay hashing
7. implement `HandKnowledge` + exact unseen-card support mask
8. implement offline smoother + label quality tags
9. build first Parquet dataset
10. train first baseline and compare against trivial heuristics
11. implement legal-action API + minimal play-mode step interface

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
- enough play-mode / legality scaffolding to start Month-2 self-play and selective teacher search without rebuilding the core

## Preferred commands
Target commands for the initial repo:
- configure: `cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo`
- build: `cmake --build build -j`
- C++ tests: `ctest --test-dir build --output-on-failure`
- Python env setup: `uv sync` (installs all deps including dev group)
- Python tests: `uv run pytest`  (parallel: `-n auto` is the default)
- Python tests (serial / debug): `uv run pytest -n 0`
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

## Long-form design documents
`long-prompts/` contains extended conversations (human ↔ external LLM) about architecture, action spaces, and analysis. These are food-for-thought documents — directionally useful but may need adaptation. Check them when facing a design decision in the relevant area. They are **not** authoritative — the codebase and `docs/` take precedence.

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `uv run python -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('python/')); _rebuild_code(Path('cpp/')); _rebuild_code(Path('scripts/'))"` to keep the graph current
