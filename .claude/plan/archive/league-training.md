# Spec: League Training (Checkpoint Pool Self-Play)

## Goal

Prevent catastrophic forgetting and rock-paper-scissors cycles in self-play by maintaining
a pool of past model checkpoints. Each PPO iteration samples an opponent from the pool
(biased toward recent checkpoints) rather than always fighting the current model.

## Motivation

PPO v2 observation: after 20 self-play iters, combined WR vs heuristic dropped from 83.2% → 65.4%.
The model is replacing heuristic-exploitation skills with self-play skills. League training would
ensure the model is also rewarded for beating earlier versions of itself, preventing regression.

## C++ requirement: `rollout_model_vs_model_batched`

League training needs to TRAIN on games between two different models, which means recording
steps (not just game outcomes). This requires extending `benchmark_model_vs_model_batched`
into a rollout variant.

### New function signature (`mcts_batched.hpp`)

```cpp
/// Rollout where model_a plays against model_b.
/// Steps recorded ONLY for model_a (the "learning" model).
/// Half games: model_a=USSR, model_b=US. Other half: model_a=US, model_b=USSR.
RolloutResult rollout_model_vs_model_batched(
    int n_games,
    torch::jit::script::Module& model_a,   // learning model (steps recorded)
    torch::jit::script::Module& model_b,   // opponent model (no steps recorded)
    int pool_size,
    uint32_t base_seed,
    float temperature = 1.0f,
    bool nash_temperatures = false
);
```

### Implementation

Copy `rollout_games_batched` structure. Key differences:
1. Two models instead of one + heuristic
2. `model_a_side[game_idx]` stores which side model_a plays (alternates)
3. When game needs action:
   - If phasing side == model_a_side[game]: push to model_a eval queue
   - Else: push to model_b eval queue
4. Eval model_a batch, then model_b batch (separate calls)
5. Record step ONLY if phasing side == model_a_side[game]
6. Apply action for current game

---

## Python: League management

### League pool directory: `data/checkpoints/league/`

Copy scripted checkpoints here as they're saved during PPO:
```
data/checkpoints/league/
  iter_020.pt
  iter_040.pt
  iter_060.pt
  ...
  current.pt → (symlink or copy of latest scripted checkpoint)
```

### Opponent sampling strategy

```python
def sample_league_opponent(league_dir: str, iteration: int) -> str | None:
    """Sample an opponent from the league pool.
    
    Returns None → use heuristic opponent.
    Probability distribution:
      - 20% heuristic (always anchor)
      - 50% latest league checkpoint
      - 30% uniformly random from all checkpoints
    """
    import random
    pts = sorted(Path(league_dir).glob("iter_*.pt"))
    
    r = random.random()
    if r < 0.20 or not pts:
        return None  # heuristic
    elif r < 0.70 and pts:  # 50%: latest
        return str(pts[-1])
    else:  # 30%: random past
        return str(random.choice(pts))
```

### Python: `collect_rollout_league_batched()`

```python
def collect_rollout_league_batched(
    model: nn.Module,
    league_dir: str,
    n_games: int,
    base_seed: int,
    device: str,
    vp_reward_coef: float = 0.0,
) -> list[Step]:
    """Collect rollout steps against a league-sampled opponent.
    
    Each iteration samples a different opponent. Steps recorded for `model` only.
    """
    opponent_path = sample_league_opponent(league_dir, 0)
    
    script_path = _export_temp_model(model)
    try:
        if opponent_path is None:
            # Fall back to heuristic
            return collect_rollout_batched(
                model, n_games, tscore.Side.USSR, base_seed, device, {}, vp_reward_coef
            )
        
        results, steps, boundaries = tscore.rollout_model_vs_model_batched(
            model_a_path=script_path,
            model_b_path=opponent_path,
            n_games=n_games,
            pool_size=min(n_games, 64),
            seed=base_seed,
            device="cpu",
            temperature=1.0,
            nash_temperatures=False,
        )
    finally:
        os.remove(script_path)
    
    # Parse steps (same as collect_rollout_batched)
    ...
    
    # Assign rewards
    side_int_for_game = [0 if i < n_games // 2 else 1 for i in range(n_games)]
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start >= end: continue
        all_steps[end - 1].reward = _compute_reward(result, side_int_for_game[i], vp_reward_coef)
        all_steps[end - 1].done = True
    
    return all_steps
```

### CLI flags

```python
p.add_argument("--league", type=str, default=None,
               help="League directory with opponent checkpoints (enables league training)")
p.add_argument("--league-save-every", type=int, default=20,
               help="Save current checkpoint to league pool every N iterations")
```

### League integration in training loop

When `--league` is set, replace self-play rollout with league rollout:

```python
if args.league:
    all_steps = collect_rollout_league_batched(
        model, args.league, args.games_per_iter, seed, device, args.vp_reward_coef
    )
    # Save to league pool every N iters
    if iteration % args.league_save_every == 0:
        pool_path = Path(args.league) / f"iter_{iteration:04d}.pt"
        _export_scripted_model(model, str(pool_path))
        print(f"  Saved to league pool: {pool_path}")
```

---

## Files to Create/Modify

| File | Change |
|------|--------|
| `cpp/tscore/mcts_batched.hpp` | Add `rollout_model_vs_model_batched` declaration |
| `cpp/tscore/mcts_batched.cpp` | Implement the function |
| `bindings/tscore_bindings.cpp` | Add Python binding `tscore.rollout_model_vs_model_batched` |
| `scripts/train_ppo.py` | Add `collect_rollout_league_batched()`, `--league`, `--league-save-every` flags |

---

## Dependencies

- `benchmark_model_vs_model_batched` (already being built by C++ agent) — not needed for training,
  but the same pattern. The league rollout variant is a copy with step recording added.
- `rollout_self_play_batched` already exists — the league variant is similar but uses two models.

---

## Acceptance Criteria

1. Build succeeds
2. `tscore.rollout_model_vs_model_batched` importable
3. Smoke test: 5 games, same model vs itself → WR ≈ 50%, steps recorded for model_a only
4. `train_ppo.py --league data/checkpoints/league --league-save-every 20` runs without error
5. After iter 20, league pool has `iter_0020.pt`

---

## Notes

- Start with an empty league pool. The first iter uses heuristic (no checkpoints yet).
  Add current checkpoint to pool BEFORE running rollout (so iter 1 can play vs iter 0).
- Only the learning model's steps are recorded. The opponent's moves are just "environment".
- This is strictly better than pure self-play (vs current self) because:
  - Prevents forgetting earlier skills
  - Creates diverse opponents with different skill levels
  - More stable gradient signal
