# Experimental PPO Workbench

This subtree is an isolated sandbox for performance experiments that do not
change the production training path.

Ownership:
- This directory is controlled by an independent Codex agent.
- The main Claude control-plane agent must not commit changes in this subtree.
- Codex is responsible for commits that touch files under `experimental/`.

Scope:
- Prototype rollout and PPO-update speedups.
- Benchmark them against the current implementation in `scripts/train_ppo.py`.
- Keep all code, notes, and generated helper modules inside `experimental/`.

Non-goals:
- No production changes.
- No edits outside `experimental/`.

Current structure:
- `experimental/ppo/` reusable experiment helpers
- `experimental/scripts/` runnable benchmark entrypoints
- `experimental/FINDINGS.md` detailed benchmark notes and code walkthrough

Benchmark entrypoint:
- `uv run python experimental/scripts/bench_ppo_speedups.py --games 200 --ppo-epochs 2 --minibatch-size 2048`

Suggested reading order:
- Start with [`FINDINGS.md`](/home/dkord/code/twilight-struggle-ai/experimental/FINDINGS.md) for the results and rationale.
- Then read [`experimental/scripts/bench_ppo_speedups.py`](/home/dkord/code/twilight-struggle-ai/experimental/scripts/bench_ppo_speedups.py) for the experiment driver.
- Then read [`experimental/ppo/rollout.py`](/home/dkord/code/twilight-struggle-ai/experimental/ppo/rollout.py) and [`experimental/ppo/update.py`](/home/dkord/code/twilight-struggle-ai/experimental/ppo/update.py) for the prototype implementations.
