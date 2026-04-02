# Spec: Exploration Noise for MCTS Self-Play (Month 3, Priority 1-2)

## Context

Current self-play win rate is ~12%, near the imitation-learning ceiling.
Breaking through requires diverse self-play data via: (1) Dirichlet noise at
MCTS root, (2) temperature-based action sampling, (3) epsilon-greedy.

## What Already Exists

| Component | File | Status |
|---|---|---|
| `MctsConfig.dir_alpha / dir_epsilon` | `mcts.hpp:41-51` | Exists |
| `apply_root_dirichlet_noise()` | `mcts.cpp:484-512` | Complete |
| Noise called in single-game MCTS | `mcts.cpp:594` | Working |
| `BatchedMctsConfig.temperature` | `mcts_batched.hpp:89` | Exists |
| Temperature sampling | `mcts_batched.cpp:553` | Complete |
| `--temperature` CLI flag | `collect_mcts_games_jsonl.cpp:63` | Exists |
| `TorchScriptPolicy` epsilon-greedy | `learned_policy.cpp:148` | Working |

**Primary gap:** `mcts_batched.cpp:1472-1473` expands root but never calls
`apply_root_dirichlet_noise`. All batched MCTS self-play runs with zero noise.

## Dirichlet Noise Parameters

Alpha: `0.2f` (k=10, E[n_legal]=50 edges in TS). Compare AlphaZero chess: 0.3 over ~35 moves.
Epsilon: `0.25f` (existing default, matches AlphaZero).

## Temperature Schedule

```
if move_number <= 10:  temperature = 1.0   # full stochasticity, early game
elif move_number <= 30: temperature = 0.5  # moderate exploration, mid game
else:                   temperature = 0.0  # greedy, late game
```

## Code Changes Required

### Change 1: Fix missing Dirichlet noise in batched root expansion
File: `cpp/tscore/mcts_batched.cpp` line ~1473
After `slot.root = std::move(expansion.node);`, add:
`apply_root_dirichlet_noise(*slot.root, config.mcts, slot.rng);`
Requires making the function externally linkable in `mcts.hpp`/`mcts.cpp`.

### Change 2: Fix default alpha
File: `cpp/tscore/mcts.hpp` line 44
Change `float dir_alpha = 0.3f;` to `float dir_alpha = 0.2f;`

### Change 3: Piecewise temperature schedule
File: `cpp/tscore/mcts_batched.cpp`
Replace hardcoded temp cutoff at move 30 with `effective_temperature()` helper.

### Change 4: Add epsilon-greedy to BatchedMctsConfig
Add `float epsilon_greedy = 0.0f;` to config. In `commit_best_action()`,
add random-legal-action branch with probability `epsilon_greedy`.

### Change 5: CLI flags
Add `--dir-alpha`, `--dir-epsilon`, `--epsilon-greedy` to `collect_mcts_games_jsonl.cpp`.

## Build Sequence

1. Fix batched root Dirichlet (Change 1+2) — most important
2. Temperature schedule (Change 3)
3. Epsilon-greedy (Change 4)
4. CLI flags (Change 5)
5. Collect 500 MCTS games with noise, measure diversity, retrain
