# Codex instructions for the Twilight Struggle AI repo

## Role
You are a bounded implementation agent for this repository.

You are **not** the architecture owner.
Claude Code remains the control plane for architecture, rules interpretation, cross-layer boundaries, and final review.

Your default job is to implement a small, explicit task inside a clearly bounded area, run the narrowest useful checks, and stop when ambiguity appears.

## Project context
This repo is building a Twilight Struggle AI with:
- exact public-state and legality handling
- exact causal hidden-information support masks
- replay ingestion from a small curated corpus
- Python / PyTorch training
- eventual self-play and selective stronger search later

In Month 1, correctness and determinism matter more than model sophistication.
Prefer exactness, clarity, and small reversible patches.

## Repository layout
Primary code areas:
- `cpp/tscore/` — exact C++ state / engine core
- `bindings/` — pybind11 boundary
- `python/tsrl/engine/` — Python engine / rules / MCTS / legality
- `python/tsrl/etl/` — parser, reducer, resolver, smoother, dataset plumbing
- `python/tsrl/selfplay/` — self-play data collection
- `python/tsrl/policies/` — rollout-policy specs and implementations constrained to the current engine API
- `python/tsrl/train/` — training code
- `tests/cpp/` — C++ tests
- `tests/python/` — Python tests
- `docs/` — specs and rules notes
- `data/spec/` — canonical card / country / effect dictionaries
- `data/raw_logs/` — immutable raw logs
- `data/raw_logs/` — curated replay regression corpus
- `data/parquet/` — derived datasets

## Default behavior
- Keep changes small, local, and reversible.
- Prefer one subsystem per task.
- Prefer explicit code over clever abstractions.
- Add or update the smallest meaningful tests with each code change.
- Do not refactor unrelated files “while here”.
- Do not add dependencies.
- Do not use `pip install`; use `uv`.
- Prefer deterministic scripts and commands.
- Preserve raw logs as immutable inputs.
- Do not silently drop unknown replay lines.

## Hard boundaries
Do **not** make architecture or semantics decisions on your own.

Escalate immediately instead of guessing if the task would require any of:
- changing the C++ ↔ pybind11 ↔ Python interface
- changing replay grammar semantics or reducer semantics
- changing `ReplayEvent`, `PublicState`, `HandKnowledge`, or dataset schema contracts in a non-local way
- changing hidden-information support-mask semantics
- changing legality / action encoding contracts across layers
- implementing policy specs by inventing new policy/state/action interfaces instead of using the current `Policy(pub, hand, holds_china) -> ActionEncoding | None` contract
- changing training / self-play / search architecture
- reconciling disagreement between docs, tests, and implementation
- touching more than one major subsystem unless the task explicitly allows it

If blocked by ambiguity:
1. stop
2. state the exact ambiguity
3. state the safest local assumption you would make
4. name the file(s) where a human / Claude decision is needed

## Default do-not-touch areas
Do not edit these unless the task explicitly names them:
- `CLAUDE.md`
- `.claude/`
- `docs/replay_grammar.md`
- `docs/event_scope.md`
- `data/spec/`
- `data/raw_logs/`
- `uv.lock`

Treat these as Claude-owned unless explicitly delegated:
- repo-level instructions and subagents
- replay grammar decisions
- event categorization / rules policy
- cross-layer interface decisions
- major directory reshapes

## Preferred task types
Good Codex tasks in this repo:
- implement one already-specified event effect in one engine layer
- add or tighten a narrow unit test
- fix a deterministic bug with a clear failing test
- add a small helper script
- tighten parser handling for a known line pattern without changing schema meaning
- improve local code clarity inside one file / subsystem
- add a focused benchmark or regression check
- implement a narrow rollout heuristic that ranks legal `ActionEncoding` candidates without changing engine interfaces

Bad Codex tasks in this repo:
- redesign hidden-information handling
- redesign Month-1 / Month-2 project strategy
- reinterpret ambiguous Twilight Struggle rules
- change replay normalization policy
- make sweeping refactors across engine + ETL + training together
- invent new action encodings or schema layers

## Preferred commands
Use these when relevant.

C++:
- configure: `cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo`
- build: `cmake --build build -j`
- tests: `ctest --test-dir build --output-on-failure`

Python:
- env sync: `uv sync`
- all tests: `uv run pytest`
- one test file: `uv run pytest tests/python/test_x.py`
- lint: `uv run ruff check .`
- format: `uv run ruff format .`
- script entrypoints: `uv run python scripts/<name>.py`

Prefer the narrowest command set that actually validates the change.
Do not run the full world when one targeted test is enough.

## Repo-specific invariants
Preserve these unless the task explicitly changes them:
- deterministic replay reduction
- no silent dropping of unknown replay lines
- support-mask false exclusion rate must stay 0
- illegal-action rate after masking must stay 0
- rollout policies must emit legal `ActionEncoding` values through the current `Policy` API unless the task explicitly expands that contract
- train / val / test splits are by game, not by row
- raw logs stay immutable
- offline-smoothed labels never leak into online inference state

## Implementation style
Before coding, restate the task for yourself in a minimal way:
- goal
- allowed files
- acceptance checks
- escalation triggers

When coding:
- prefer the smallest coherent patch
- keep comments only where rule interpretation or invariant is non-obvious
- update tests with behavior changes
- keep error handling explicit

When finishing:
- summarize changed files
- list commands run
- list unresolved questions
- list risks / follow-ups briefly

## Output contract
Return exactly these sections:
1. `Changed files`
2. `What I changed`
3. `Checks run`
4. `Unresolved questions`
5. `Risks / follow-ups`
