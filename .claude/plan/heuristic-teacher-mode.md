# Spec: Heuristic Teacher Mode — collect_mcts_targets.py

## Goal

Add `heuristic_teacher_mode` to `BatchedMctsConfig` so that `collect_games_batched`
plays games with the MinimalHybrid heuristic (not MCTS) while simultaneously running
MCTS at each decision to record visit count distributions as teacher targets. This lets
Exp3 collect teacher targets that match existing heuristic BC rows by `(game_id, step_idx)`.

The key invariant: **game trajectories must be bit-identical to pure heuristic games**
with the same seed, so teacher targets can be joined to nash_c parquet rows by game_id.
This requires the MCTS measurement to not perturb the game RNG.

## Files to create

- `scripts/collect_mcts_targets.py` — CLI wrapper: runs C++ tool in heuristic_teacher_mode
  then converts JSONL → teacher target Parquet

## Files to modify

- `cpp/tscore/mcts_batched.hpp` — add `heuristic_teacher_mode` field + `game_id_prefix`
  to `BatchedMctsConfig`; add `rng_before_mcts` to `GameSlot`
- `cpp/tscore/mcts_batched.cpp` — save/restore slot RNG around MCTS + use heuristic
  for action selection; use `game_id_prefix` in `game_id_for()`
- `cpp/tools/collect_mcts_games_jsonl.cpp` — add `--heuristic-teacher-mode` and
  `--game-id-prefix` flags

## Interfaces / signatures

### BatchedMctsConfig additions (mcts_batched.hpp, after line 100)
```cpp
struct BatchedMctsConfig {
    // ... existing fields ...
    bool heuristic_teacher_mode = false;
    // Prefix for game_id. Default "mcts". Set to "selfplay" when in
    // heuristic_teacher_mode to match existing heuristic dataset game_ids.
    std::string game_id_prefix = "mcts";
};
```

### GameSlot addition (mcts_batched.hpp, inside GameSlot struct)
```cpp
struct GameSlot {
    // ... existing fields ...
    // Saved RNG state before MCTS search starts, for heuristic_teacher_mode.
    // Restored before the heuristic action is selected so game trajectory
    // matches a pure-heuristic game with the same seed.
    std::optional<Pcg64Rng> rng_before_mcts;
};
```

### game_id_for() change (mcts_batched.cpp ~line 1167)
```cpp
std::string game_id_for(const std::string& prefix, uint32_t base_seed, int game_index) {
    std::ostringstream out;
    out << prefix << "_" << base_seed << "_";
    // ... zero-padding unchanged ...
    return out.str();
}
```
All callers: `game_id_for(config.game_id_prefix, base_seed, game_index)`.

### commit_best_action() change (mcts_batched.cpp ~line 1602)

In `heuristic_teacher_mode`, after `build_search_result(slot)`:
1. Restore `slot.rng` from `slot.rng_before_mcts` (so game RNG is back to pre-MCTS state)
2. Clear `slot.rng_before_mcts`
3. Select action with `choose_action(PolicyKind::MinimalHybrid, ...)` **only** (skip epsilon/temp)
4. Skip the `action.card_id == 0` fallback check (heuristic should always succeed)

Normal mode (`heuristic_teacher_mode == false`): no change.

### Where to save slot.rng_before_mcts

In `start_mcts_for_slot()` (or wherever MCTS is initialized for a pending decision),
when `config.heuristic_teacher_mode == true`, save: `slot.rng_before_mcts = slot.rng;`

### collect_mcts_games_jsonl.cpp additions
```
--heuristic-teacher-mode    (flag, no value)  sets config.heuristic_teacher_mode = true
                                              and defaults game_id_prefix to "selfplay"
--game-id-prefix PREFIX     (string, optional) overrides the game_id prefix
```

### collect_mcts_targets.py CLI
```
uv run python scripts/collect_mcts_targets.py \
  --model MODEL.pt           required: TorchScript model
  --games N                  default: 1000
  --n-sim N                  default: 100
  --pool-size N              default: 32
  --seed N                   default: 77700 (matches nash_c base seed)
  --output OUTPUT.parquet    required: teacher target parquet path
  --jsonl-path PATH          optional: keep intermediate JSONL (default: tmpfile)
```

The script:
1. Locates `build-ninja/cpp/tools/ts_collect_mcts_games_jsonl` binary
2. Runs it with `--heuristic-teacher-mode --game-id-prefix selfplay` and the given args
3. Converts JSONL → teacher target Parquet using `convert_mcts_to_teacher.convert_row()`
   (reuse that function directly, or copy its logic)
4. Prints row count and output path

### Teacher target Parquet schema (unchanged from convert_mcts_to_teacher.py)
```python
pa.schema([
    ("game_id",              pa.string()),
    ("step_idx",             pa.int64()),
    ("teacher_card_target",  pa.list_(pa.float32())),  # 111 entries
    ("teacher_mode_target",  pa.list_(pa.float32())),  # 5 entries
    ("teacher_value_target", pa.float32()),
])
```

## Test cases (required)

- **test_heuristic_teacher_mode_game_id_prefix**: Run 2 games in heuristic_teacher_mode
  with seed=1000 and default prefix. Verify game_ids start with `selfplay_1000_`.
  Setup: requires built `ts_collect_mcts_games_jsonl` binary + scripted model.
  Mark `@pytest.mark.serial`.

- **test_heuristic_teacher_mode_trajectory_matches_pure_heuristic**: Run 2 games
  in heuristic_teacher_mode with seed=1000. Also run 2 pure heuristic games via
  `tscore.play_traced_game_from_seed_words` (no MCTS) with same seeds. Verify
  `action_card_id` and `action_mode` match at every step_idx. This validates the
  RNG save/restore is correct.
  Setup: requires built binary + scripted model. Mark `@pytest.mark.serial`.

- **test_heuristic_teacher_mode_has_visit_counts**: Run 2 games in heuristic_teacher_mode.
  Parse JSONL output. Verify every row has `mcts_visit_counts` as a non-empty list
  and `mcts_root_value` is a finite float. (Proves MCTS measured even though heuristic
  played.)

- **test_collect_mcts_targets_script_output_schema**: Run `collect_mcts_targets.py` with
  2 games, n_sim=5. Load output parquet with pyarrow. Assert schema matches expected:
  columns {game_id, step_idx, teacher_card_target, teacher_mode_target, teacher_value_target}.
  Assert teacher_card_target has length 111 for all rows.

- **test_collect_mcts_targets_game_id_join**: Run `collect_mcts_targets.py` with
  seed=77700, games=2. Load output parquet. Assert all game_ids start with `selfplay_77700_`.
  Confirms produced game_ids will join to nash_c parquet.

- **test_normal_mode_unaffected**: Run 2 games without `--heuristic-teacher-mode`.
  Parse JSONL. Verify game_ids start with `mcts_` (default prefix unchanged).
  This validates backward compat.

## Acceptance criteria

- [ ] All 6 test cases above pass
- [ ] No regressions: `cmake --build build-ninja -j && ctest --test-dir build-ninja -q`
- [ ] No regressions: `uv run pytest tests/python/ -q -n 0`
- [ ] Game trajectories in heuristic_teacher_mode are bit-identical to pure heuristic
      (verified by trajectory-match test)
- [ ] `collect_mcts_targets.py --help` works
- [ ] Running full Exp3 collection command succeeds:
  ```bash
  uv run python scripts/collect_mcts_targets.py \
    --model data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt \
    --games 10 --n-sim 5 --seed 77700 \
    --output /tmp/test_teacher.parquet
  ```

## Constraints

- Do NOT change behavior when `heuristic_teacher_mode=false` (default). All existing
  callers unaffected. Default `game_id_prefix="mcts"` preserves existing output.
- The RNG save/restore must happen at the slot level, before MCTS tree construction
  begins, and be restored before `choose_action(MinimalHybrid)` is called.
- Do NOT add `--heuristic-teacher-mode` to `collect_selfplay_rows_jsonl.cpp` —
  only to `collect_mcts_games_jsonl.cpp`.
- `collect_mcts_targets.py` must NOT import torch or tscore directly — it shells out
  to the C++ binary. This keeps it lightweight and avoids binding version issues.
- Output Parquet from `collect_mcts_targets.py` must be compatible with
  `train_baseline.py --teacher-targets` (left-joined on game_id + step_idx).
- No new Python dependencies beyond what's already in `pyproject.toml`.

## Usage for Exp3

```bash
# 1. Collect teacher targets for 1000 heuristic games (10% of nash_c)
uv run python scripts/collect_mcts_targets.py \
  --model data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt \
  --games 1000 --n-sim 100 --pool-size 32 --seed 77700 \
  --output data/selfplay/mcts_teacher_nashc_100sim_1k.parquet

# 2. Train BC on full nash_c + teacher KL on 1k matched games
uv run python scripts/train_baseline.py \
  --data-dir data/nash_c_only \
  --out-dir data/checkpoints/v105_teacher_heur_kl_s42 \
  --model-type control_feat --hidden-dim 256 \
  --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
  --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
  --one-cycle --deterministic-split --value-target final_vp --seed 42 \
  --teacher-targets data/selfplay/mcts_teacher_nashc_100sim_1k.parquet \
  --teacher-weight 0.5
```

The join will match ~1k × ~140 steps = ~140k teacher rows to the same rows in
nash_c (which has 1.37M rows). Coverage ~10%.

## Implementation order

1. `cpp/tscore/mcts_batched.hpp` — struct additions (trivial)
2. `cpp/tscore/mcts_batched.cpp` — `game_id_for()` signature, RNG save/restore,
   heuristic action selection branch in `commit_best_action()`
3. `cpp/tools/collect_mcts_games_jsonl.cpp` — two new CLI flags
4. Build: `cmake --build build-ninja -j` — must succeed
5. `scripts/collect_mcts_targets.py` — Python wrapper
6. `tests/python/test_collect_mcts_targets.py` — all 6 test cases
