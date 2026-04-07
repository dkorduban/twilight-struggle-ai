# Spec: Self-Play PPO Rollout

## Goal

Add `rollout_self_play_batched()` C++ function and Python binding so that PPO
can train against itself (both sides use the same learned model) rather than
a fixed heuristic opponent.

---

## Background

Current `rollout_games_batched(learned_side, ...)`:
- Plays N games: learned model as `learned_side`, heuristic on the other side
- Records steps for `learned_side` only
- Returns (results, steps_for_learned_side, game_boundaries)

Self-play needs:
- Both sides use the learned model
- Steps for BOTH sides are recorded
- Rewards assigned per-side from the same game outcome
- USSR steps: +1 if USSR wins, -1 if US wins
- US steps: +1 if US wins, -1 if USSR wins

---

## C++ Changes: `cpp/tscore/mcts_batched.cpp` + `cpp/tscore/mcts_batched.hpp`

### New function signature in `mcts_batched.hpp`

```cpp
// Self-play rollout: both sides use the learned model.
// Steps for both USSR and US are recorded.
// game_boundaries[i] = offset of game i's first step in the flat steps array.
// steps are ordered: all of game 0's steps, then game 1's, etc.
// Within each game, steps are in chronological order (alternating USSR/US).
RolloutResult rollout_self_play_batched(
    const std::string& model_path,
    int n_games,
    int pool_size,
    uint64_t seed,
    const std::string& device,
    float temperature,
    bool nash_temperatures
);
```

`RolloutResult` is already defined:
```cpp
struct RolloutResult {
    std::vector<GameResult> results;      // one per game
    std::vector<RolloutStep> steps;       // flat, chronological within each game
    std::vector<int> game_boundaries;     // first step offset for each game
};
```

`RolloutStep` already has `side_int` (0=USSR, 1=US), so no struct changes needed.

### Implementation in `mcts_batched.cpp`

Copy `rollout_games_batched()` as the starting point. The key differences:

1. **No `learned_side` parameter** — both sides use the NN.

2. **Both sides' steps are recorded** — remove the `if (pub.phasing == learned_side)` guard
   around step recording. Record every step regardless of which side is moving.

3. **Both sides use NN for action selection** — remove the heuristic policy branch.
   At every decision point (any side), push to the NN evaluation queue.

4. **`side_int` is set correctly** — already set from `pub.phasing` in the existing code.

The game loop structure inside `rollout_games_batched` (roughly):
```
while (pending games):
    for each game needing action:
        push (game_idx, state, hand, holds_china, side_int) to eval_queue
    batch_eval(eval_queue) -> outputs
    for each game:
        sample action from outputs
        record RolloutStep (if learned_side matches)
        apply action to game state
    handle terminals
```

For self-play, change to:
```
while (pending games):
    for each game needing action:
        push to eval_queue (ALWAYS, both sides)
    batch_eval(eval_queue) -> outputs
    for each game:
        sample action from outputs
        record RolloutStep (ALWAYS, both sides)
        apply action to game state
    handle terminals
```

The `rollout_action_from_outputs()` helper (already exists) handles sampling + log_prob.

---

## Python Binding: `bindings/tscore_bindings.cpp`

Add `tscore.rollout_self_play_batched()` binding alongside `rollout_games_batched`:

```python
tscore.rollout_self_play_batched(
    model_path: str,
    n_games: int,
    pool_size: int,
    seed: int,
    device: str = "cpu",
    temperature: float = 1.0,
    nash_temperatures: bool = True,
) -> tuple[list[GameResult], list[dict], list[int]]
# Same return format as rollout_games_batched
```

The binding implementation is identical to `rollout_games_batched`'s binding, just calling
`rollout_self_play_batched` instead. Steps dict format is unchanged (uses `rollout_step_to_dict`).

---

## Python Changes: `scripts/train_ppo.py`

### New function: `collect_rollout_self_play()`

```python
def collect_rollout_self_play_batched(
    model: nn.Module,
    n_games: int,
    base_seed: int,
    device: str,
) -> list[Step]:
    """Collect PPO rollout steps from self-play (both sides use learned model)."""
    script_path = _export_temp_model(model)
    try:
        results, steps, boundaries = tscore.rollout_self_play_batched(
            model_path=script_path,
            n_games=n_games,
            pool_size=min(n_games, 64),
            seed=base_seed,
            device="cpu",
            temperature=1.0,
            nash_temperatures=True,
        )
    finally:
        try:
            os.remove(script_path)
        except OSError:
            pass

    all_steps: list[Step] = []
    for s in steps:
        country_mask = torch.from_numpy(s["country_mask"])
        step = Step(
            influence=torch.from_numpy(s["influence"]).unsqueeze(0),
            cards=torch.from_numpy(s["cards"]).unsqueeze(0),
            scalars=torch.from_numpy(s["scalars"]).unsqueeze(0),
            card_mask=torch.from_numpy(s["card_mask"]),
            mode_mask=torch.from_numpy(s["mode_mask"]),
            country_mask=country_mask if bool(country_mask.any()) else None,
            card_idx=s["card_idx"],
            mode_idx=s["mode_idx"],
            country_targets=list(s["country_targets"]),
            old_log_prob=float(s["log_prob"]),
            value=float(s["value"]),
            side_int=int(s["side_int"]),
        )
        all_steps.append(step)

    # Recompute log_probs with real PyTorch model (TorchScript trace bug workaround)
    _recompute_log_probs_and_values(all_steps, model, device)

    # Assign rewards: per-side from game outcome
    for i, result in enumerate(results):
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start >= end:
            continue
        for step_idx in range(start, end):
            s = all_steps[step_idx]
            if step_idx == end - 1:
                # Terminal step: assign reward based on this step's side
                if s.side_int == 0:  # USSR
                    s.reward = 1.0 if result.winner == tscore.Side.USSR else -1.0
                else:  # US
                    s.reward = 1.0 if result.winner == tscore.Side.US else -1.0
                s.done = True

    return all_steps
```

### CLI argument: `--self-play`

Add `--self-play` flag to `parse_args()`:
```python
p.add_argument("--self-play", action="store_true",
               help="Train via self-play (both sides use learned model) instead of vs heuristic")
p.add_argument("--self-play-heuristic-mix", type=float, default=0.2,
               help="Fraction of games to play vs heuristic when --self-play is active (collapse anchor)")
```

### Training loop changes

When `args.self_play` is True:
- Use `collect_rollout_self_play_batched()` for the main rollout
- Optionally mix in heuristic games: play `int(args.games_per_iter * args.self_play_heuristic_mix)`
  additional games vs heuristic (alternating sides), combine with self-play steps

For the heuristic mix in self-play mode:
```python
if args.self_play:
    all_steps = collect_rollout_self_play_batched(model, args.games_per_iter, seed, device)
    if args.self_play_heuristic_mix > 0:
        n_heur = max(1, int(args.games_per_iter * args.self_play_heuristic_mix))
        # Half as USSR, half as US vs heuristic
        heur_steps_ussr = collect_rollout_batched(
            model, n_heur // 2, tscore.Side.USSR, seed + 1000000, device, card_specs
        )
        heur_steps_us = collect_rollout_batched(
            model, n_heur // 2, tscore.Side.US, seed + 2000000, device, card_specs
        )
        all_steps = all_steps + heur_steps_ussr + heur_steps_us
else:
    # existing heuristic rollout (unchanged)
    ...
```

The GAE, PPO update, and logging code are unchanged — they work on `list[Step]` regardless of source.

### W&B logging additions for self-play mode

Log additional metrics during rollout stats computation:
```python
if args.self_play:
    ussr_sp_steps = [s for s in terminal_sp_steps if s.side_int == 0]
    us_sp_steps = [s for s in terminal_sp_steps if s.side_int == 1]
    sp_ussr_wr = sum(1 for s in ussr_sp_steps if s.reward > 0) / max(1, len(ussr_sp_steps))
    sp_us_wr = sum(1 for s in us_sp_steps if s.reward > 0) / max(1, len(us_sp_steps))
    # sp_ussr_wr should be ~0.5 at equilibrium (bid+2 makes game balanced)
```
Log as `sp_rollout_wr_ussr` and `sp_rollout_wr_us`.

---

## Files to Modify

1. `cpp/tscore/mcts_batched.hpp` — add `rollout_self_play_batched` declaration
2. `cpp/tscore/mcts_batched.cpp` — implement `rollout_self_play_batched`
3. `bindings/tscore_bindings.cpp` — add Python binding
4. `scripts/train_ppo.py` — add `collect_rollout_self_play_batched()`, `--self-play` arg,
   training loop integration

---

## Acceptance Criteria

1. `cmake --build build -j` succeeds with no errors
2. `python -c "import tscore; print(hasattr(tscore, 'rollout_self_play_batched'))"` prints True
3. Quick smoke test (5 games, pool_size=2):
   ```python
   import tscore
   results, steps, boundaries = tscore.rollout_self_play_batched(
       "data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt",
       n_games=5, pool_size=2, seed=42, device="cpu",
       temperature=1.0, nash_temperatures=False
   )
   assert len(results) == 5
   assert len(boundaries) == 5
   # Steps should include BOTH sides
   sides = set(s["side_int"] for s in steps)
   assert sides == {0, 1}, f"expected both sides, got {sides}"
   print("PASS: self-play rollout OK")
   ```
4. `python -c "import ast; ast.parse(open('scripts/train_ppo.py').read())"` passes
5. `uv run python scripts/train_ppo.py --help` shows `--self-play` flag

---

## Notes

- Do NOT change `RolloutStep`, `RolloutResult`, or `rollout_step_to_dict` — they already support `side_int`
- The `rollout_action_from_outputs()` helper is reusable as-is
- Keep `rollout_games_batched` unchanged — it's used for heuristic-mix games
- The `--side both` argument in PPO (existing) is for alternating heuristic games each iter;
  `--self-play` is a different mode that replaces that with self-play
- GAE advantage normalization is already per-side in the main training loop — no changes needed
