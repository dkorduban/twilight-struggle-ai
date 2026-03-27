# tsrl.policies

This directory holds rollout-policy material for the Twilight Struggle AI repo.

## What belongs here

- executable rollout-policy code that works with the current engine API
- focused policy tests under `python/tsrl/policies/tests`
- long-form heuristic strategy notes in markdown

## Current engine contract

Policy implementations in this directory must fit the current live-play interface:

`Policy(pub, hand, holds_china) -> ActionEncoding | None`

That means policies may rely on:

- `PublicState`
- the acting player's hand
- China ownership / playability
- legal action generation from `tsrl.engine.legal_actions`
- card and country metadata from `tsrl.etl.game_data`

They must not invent new action or state interfaces from inside this directory.

## Directory contents

- `minimal_hybrid.py`
  The current executable rollout policy. It is a small deterministic heuristic that ranks legal `ActionEncoding` candidates.
- `benchmark_hybrid_vs_random.py`
  A standalone micro benchmark that compares policy-call latency for `minimal_hybrid` versus the random rollout policy on a fixed corpus of legal decision states.
- `tune_minimal_hybrid.py`
  A local SPSA-based tuner for the first-pass `minimal_hybrid` parameter block, with cheap `proxy` / `smoke` modes and more expensive paired-self-play evaluation when needed.
- `proxy_corpus.py`
  The richer deterministic proxy corpus used by the tuning tooling for fast policy-local scoring.
- `autotune_minimal_hybrid.py`
  An autonomous campaign runner that logs parameter snapshots and evaluation history under `python/tsrl/policies/runs/`, then validates shortlisted candidates with paired mini-match and full-game checks.
- `minimal_hybrid.md`
  The implementation-oriented spec for `minimal_hybrid.py`.
- `classic.md`
  A large strategy pseudocode document derived from Twilight Strategy ideas. It is intentionally broader than the current engine contract.
- `sankt.md`
  A large strategy pseudocode document derived from Sankt / Aragorn-style heuristics. It is also broader than the current engine contract.
- `tests/`
  Focused tests for policy modules in this directory.
- `AGENTS.md`
  Local implementation rules for policy work.

## Why `minimal_hybrid` exists

`classic.md` and `sankt.md` contain richer concepts than the current engine exposes, such as setup hooks, richer action descriptions, and other assumptions that do not map directly onto today's `ActionEncoding`-based interface.

`minimal_hybrid` is the intentionally reduced policy that does fit today’s engine. It keeps only the parts that are currently implementable, including:

- ops-first bias
- stage-based regional weighting
- Early War Asia / Thailand emphasis
- Mid War Africa / South America emphasis
- conservative China use
- deterministic tie-breaking

## Typical next steps

- improve `minimal_hybrid.py` while preserving the current engine contract
- add focused tests for legality, determinism, and specific heuristic preferences
- wire the policy into rollout or self-play callers when explicitly requested

## Non-goals in this directory

- changing `ActionEncoding`
- changing the game loop policy interface
- adding setup-only policy actions
- adding hidden-information interfaces not already exposed by the engine

If a policy task needs any of those, escalate instead of expanding the contract locally.
