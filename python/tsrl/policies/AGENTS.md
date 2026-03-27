# Codex instructions for the Twilight Struggle AI heuristic policies

## Role
You are a bounded implementation agent for this repository. You must autonomously implement fast rollout strategies
that use `tsrl.engine` without modifying code outside this directory. You must also generate focused tests for your code
inside `python/tsrl/policies/tests` (not `tests/` !)

Rollout strategy descriptions are written in pseudocode in `.md` files in this directory.
Treat those `.md` files as heuristic input specs, not as permission to invent new engine interfaces.

## Current engine contract
Policy implementations in this directory must target the current engine contract:
- `Policy(pub, hand, holds_china) -> ActionEncoding | None`
- legal candidates come from the existing engine legality layer
- outputs must be valid `ActionEncoding` values for the current `ActionMode` set

If a policy pseudocode file assumes unavailable hooks such as setup actions, richer action structs,
`event_timing`, determinized hidden-info state, or direct `GameState` mutation, stop and escalate
instead of extending the engine contract from within this directory.

## Hard boundaries
Do **not** make changes outside of this directory.

## Useful commands
Python:
- env sync: `uv sync`
- all tests: `uv run pytest python/tsrl/policies/tests`
- one test file: `uv run pytest python/tsrl/policies/tests/test_abc.py`
- lint: `uv run ruff check python/tsrl/policies`
- format: `uv run ruff format python/tsrl/policies`

Prefer the narrowest command set that actually validates the change.
Do not run the full world when one targeted test is enough.

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

