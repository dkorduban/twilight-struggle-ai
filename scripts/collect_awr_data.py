#!/usr/bin/env python3
"""Collect off-policy rollout data for AWR architecture evaluation.

Plays games using scripted checkpoints vs heuristic (or self-play), collects
all steps with features, masks, actions, rewards, and GAE advantages, then
saves directly to parquet. No JSONL intermediate.

Usage:
    # Collect 1M rows from best panel + specialists
    python scripts/collect_awr_data.py \
        --models data/checkpoints/scripted_for_elo/v309_sc_scripted.pt \
                 results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
                 results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
        --games-per-model 200 \
        --out data/awr_eval/awr_data.parquet

    # Collect from top-N Elo checkpoints automatically
    python scripts/collect_awr_data.py \
        --top-n 10 \
        --games-per-model 100 \
        --out data/awr_eval/awr_data.parquet
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

# Ensure project imports work
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))

import tscore


# ---------------------------------------------------------------------------
# GAE computation (standalone, no Step class dependency)
# ---------------------------------------------------------------------------

def compute_gae_arrays(
    values: np.ndarray,
    rewards: np.ndarray,
    dones: np.ndarray,
    side_ints: np.ndarray,
    game_boundaries: list[tuple[int, int]],
    gamma: float = 0.99,
    lam: float = 0.95,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute GAE advantages and returns for all steps.

    Per-side GAE within each game (self-play games have mixed sides).
    Returns (advantages, returns) arrays of same length as values.
    """
    N = len(values)
    advantages = np.zeros(N, dtype=np.float32)
    returns = np.zeros(N, dtype=np.float32)

    for start, end in game_boundaries:
        if start >= end:
            continue
        seg_sides = side_ints[start:end]
        seg_values = values[start:end]
        seg_rewards = rewards[start:end]
        seg_dones = dones[start:end]

        # Find terminal reward
        terminal_side = seg_sides[-1]
        terminal_reward = seg_rewards[-1]

        unique_sides = np.unique(seg_sides)
        for target_side in unique_sides:
            mask = seg_sides == target_side
            indices = np.nonzero(mask)[0]
            if len(indices) == 0:
                continue

            # Reward from this side's perspective
            reward = terminal_reward if target_side == terminal_side else -terminal_reward

            T = len(indices)
            gae = 0.0
            for t in reversed(range(T)):
                idx = indices[t]
                v = seg_values[idx]
                if t == T - 1:
                    delta = reward - v
                else:
                    next_v = seg_values[indices[t + 1]]
                    delta = gamma * next_v - v
                gae = delta + gamma * lam * gae
                advantages[start + idx] = gae
                returns[start + idx] = gae + v

    return advantages, returns


# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------

def _empty_data() -> dict[str, list]:
    return {
        "influence": [],
        "cards": [],
        "scalars": [],
        "card_mask": [],
        "mode_mask": [],
        "country_mask": [],
        "card_idx": [],
        "mode_idx": [],
        "country_targets": [],
        "old_log_prob": [],
        "value": [],
        "side_int": [],
        "reward": [],
        "done": [],
        "turn": [],
        "ar": [],
        "defcon": [],
        "vp": [],
        "hand_card_ids": [],
        "model_name": [],
    }


def _process_rollout(
    all_data: dict[str, list],
    results: list,
    steps: list,
    bnd: list[int],
    learned_side,
    model_name: str,
    boundaries: list[tuple[int, int]],
    total_steps: int,
) -> int:
    """Process raw rollout results into all_data lists. Returns new total_steps."""
    game_rewards = []
    for result in results:
        won = result.winner == learned_side
        end_reason = getattr(result, "end_reason", "")
        if end_reason == "defcon1" and not won:
            game_rewards.append(-1.2)
        else:
            game_rewards.append(1.0 if won else -1.0)

    for i, result in enumerate(results):
        g_start = bnd[i]
        g_end = bnd[i + 1] if i + 1 < len(bnd) else len(steps)
        boundaries.append((total_steps + g_start, total_steps + g_end))

        for j in range(g_start, g_end):
            s = steps[j]
            all_data["influence"].append(s["influence"])
            all_data["cards"].append(s["cards"])
            all_data["scalars"].append(s["scalars"])
            all_data["card_mask"].append(s["card_mask"])
            all_data["mode_mask"].append(s["mode_mask"])
            all_data["country_mask"].append(s["country_mask"])
            all_data["card_idx"].append(s["card_idx"])
            all_data["mode_idx"].append(s["mode_idx"])
            all_data["country_targets"].append(list(s["country_targets"]))
            all_data["old_log_prob"].append(float(s["log_prob"]))
            all_data["value"].append(float(s["value"]))
            all_data["side_int"].append(int(s["side_int"]))
            all_data["turn"].append(int(s["raw_turn"]) if "raw_turn" in s else 0)
            all_data["ar"].append(int(s["raw_ar"]) if "raw_ar" in s else 0)
            all_data["defcon"].append(int(s["raw_defcon"]) if "raw_defcon" in s else 5)
            all_data["vp"].append(int(s["raw_vp"]) if "raw_vp" in s else 0)
            all_data["hand_card_ids"].append(
                list(s["hand_card_ids"]) if "hand_card_ids" in s else []
            )
            all_data["model_name"].append(model_name)

            is_terminal = j == g_end - 1
            all_data["reward"].append(game_rewards[i] if is_terminal else 0.0)
            all_data["done"].append(is_terminal)

    return total_steps + len(steps)


def _finalize_data(
    all_data: dict[str, list],
    boundaries: list[tuple[int, int]],
    gamma: float,
    lam: float,
) -> dict[str, np.ndarray]:
    """Convert collected lists to numpy arrays and compute GAE."""
    N = len(all_data["card_idx"])
    influence = np.stack(all_data["influence"])
    cards = np.stack(all_data["cards"])
    scalars = np.stack(all_data["scalars"])
    card_mask = np.stack(all_data["card_mask"])
    mode_mask = np.stack(all_data["mode_mask"])
    country_mask = np.stack(all_data["country_mask"])
    values = np.array(all_data["value"], dtype=np.float32)
    rewards = np.array(all_data["reward"], dtype=np.float32)
    dones = np.array(all_data["done"], dtype=bool)
    side_ints = np.array(all_data["side_int"], dtype=np.int8)

    advantages, gae_returns = compute_gae_arrays(
        values, rewards, dones, side_ints, boundaries, gamma=gamma, lam=lam
    )

    return {
        "influence": influence,
        "cards": cards,
        "scalars": scalars,
        "card_mask": card_mask,
        "mode_mask": mode_mask,
        "country_mask": country_mask,
        "card_idx": np.array(all_data["card_idx"], dtype=np.int16),
        "mode_idx": np.array(all_data["mode_idx"], dtype=np.int8),
        "country_targets": all_data["country_targets"],
        "old_log_prob": np.array(all_data["old_log_prob"], dtype=np.float32),
        "value": values,
        "side_int": side_ints,
        "reward": rewards,
        "done": dones,
        "advantage": advantages,
        "returns": gae_returns,
        "turn": np.array(all_data["turn"], dtype=np.int8),
        "ar": np.array(all_data["ar"], dtype=np.int8),
        "defcon": np.array(all_data["defcon"], dtype=np.int8),
        "vp": np.array(all_data["vp"], dtype=np.int16),
        "hand_card_ids": all_data["hand_card_ids"],
        "model_name": all_data["model_name"],
    }


def collect_from_model(
    model_path: str,
    n_games: int,
    seed: int,
    pool_size: int = 64,
    temperature: float = 1.0,
    gamma: float = 0.99,
    lam: float = 0.95,
) -> dict[str, np.ndarray]:
    """Collect rollout data from a single scripted model vs heuristic."""
    all_data = _empty_data()
    model_name = Path(model_path).stem
    games_per_side = n_games // 2
    boundaries = []
    total_steps = 0

    for side in [tscore.Side.USSR, tscore.Side.US]:
        side_games = games_per_side if side == tscore.Side.USSR else (n_games - games_per_side)
        if side_games <= 0:
            continue

        results, steps, bnd = tscore.rollout_games_batched(
            model_path=model_path,
            learned_side=side,
            n_games=side_games,
            pool_size=min(side_games, pool_size),
            seed=seed + (0 if side == tscore.Side.USSR else 50000),
            device="cpu",
            temperature=temperature,
            nash_temperatures=True,
        )

        total_steps = _process_rollout(
            all_data, results, steps, bnd, side, model_name, boundaries, total_steps
        )

    return _finalize_data(all_data, boundaries, gamma, lam)


def collect_from_pair(
    model_a_path: str,
    model_b_path: str,
    n_games: int,
    seed: int,
    pool_size: int = 64,
    temperature: float = 1.0,
    gamma: float = 0.99,
    lam: float = 0.95,
) -> dict[str, np.ndarray]:
    """Collect rollout data from model_a vs model_b (steps from model_a only).

    model_a plays as USSR for n_games/2 and as US for n_games/2.
    """
    all_data = _empty_data()
    model_name = f"{Path(model_a_path).stem}_vs_{Path(model_b_path).stem}"
    games_per_side = n_games // 2
    boundaries = []
    total_steps = 0

    for side in [tscore.Side.USSR, tscore.Side.US]:
        side_games = games_per_side if side == tscore.Side.USSR else (n_games - games_per_side)
        if side_games <= 0:
            continue

        results, steps, bnd = tscore.rollout_model_vs_model_batched(
            model_a_path=model_a_path,
            model_b_path=model_b_path,
            n_games=side_games,
            pool_size=min(side_games, pool_size),
            seed=seed + (0 if side == tscore.Side.USSR else 50000),
            device="cpu",
            temperature=temperature,
            nash_temperatures=False,
            learned_side=side,
        )

        total_steps = _process_rollout(
            all_data, results, steps, bnd, side, model_name, boundaries, total_steps
        )

    return _finalize_data(all_data, boundaries, gamma, lam)


def arrays_to_table(data: dict[str, np.ndarray]) -> pa.Table:
    """Convert collected data dict to an Arrow table."""
    arrays = {}
    for key, val in data.items():
        if isinstance(val, np.ndarray):
            if val.ndim == 2:
                # Store 2D arrays as fixed-size lists for efficiency
                arrays[key] = pa.FixedSizeListArray.from_arrays(
                    pa.array(val.ravel(), type=pa.from_numpy_dtype(val.dtype)),
                    list_size=val.shape[1],
                )
            else:
                arrays[key] = pa.array(val)
        elif isinstance(val, list):
            # Variable-length lists (country_targets, hand_card_ids)
            if val and isinstance(val[0], list):
                arrays[key] = pa.array(val, type=pa.list_(pa.int32()))
            else:
                arrays[key] = pa.array(val)
    return pa.table(arrays)


def find_top_models(n: int, scripted_dir: str = "data/checkpoints/scripted_for_elo") -> list[str]:
    """Find top-N models by version number (proxy for Elo progression)."""
    p = Path(scripted_dir)
    if not p.exists():
        print(f"ERROR: {scripted_dir} not found", file=sys.stderr)
        return []

    models = []
    for f in p.glob("*_scripted.pt"):
        m = re.search(r"v(\d+)", f.name)
        if m:
            models.append((int(m.group(1)), str(f)))

    models.sort(key=lambda x: x[0], reverse=True)
    return [path for _, path in models[:n]]


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect AWR evaluation data")
    parser.add_argument("--models", nargs="*", default=[], help="Scripted model paths")
    parser.add_argument("--top-n", type=int, default=0, help="Use top-N Elo models from scripted_for_elo")
    parser.add_argument("--specialists", action="store_true",
                        help="Include USSR/US v5 specialists")
    parser.add_argument("--games-per-model", type=int, default=200,
                        help="Games per model (split across sides)")
    parser.add_argument("--out", required=True, help="Output parquet path")
    parser.add_argument("--seed", type=int, default=42000, help="Base random seed")
    parser.add_argument("--pool-size", type=int, default=64, help="Game pool size")
    parser.add_argument("--temperature", type=float, default=1.0, help="Rollout temperature")
    parser.add_argument("--gamma", type=float, default=0.99, help="Discount factor")
    parser.add_argument("--gae-lambda", type=float, default=0.95, help="GAE lambda")
    parser.add_argument("--round-robin", action="store_true",
                        help="Also collect model-vs-model games for all pairs")
    parser.add_argument("--games-per-pair", type=int, default=200,
                        help="Games per model pair in round-robin mode")
    parser.add_argument("--append", action="store_true",
                        help="Append to existing parquet file instead of overwriting")
    args = parser.parse_args()

    # Build model list
    model_paths = list(args.models)
    if args.top_n > 0:
        model_paths.extend(find_top_models(args.top_n))
    if args.specialists:
        for sp in [
            "results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt",
            "results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt",
        ]:
            if Path(sp).exists():
                model_paths.append(sp)
            else:
                print(f"WARNING: specialist not found: {sp}")

    # Deduplicate by resolved path
    seen = set()
    unique = []
    for p in model_paths:
        rp = str(Path(p).resolve())
        if rp not in seen:
            seen.add(rp)
            unique.append(p)
    model_paths = unique

    if not model_paths:
        print("ERROR: no models specified. Use --models, --top-n, or --specialists")
        sys.exit(1)

    n_pairs = len(model_paths) * (len(model_paths) - 1) // 2 if args.round_robin else 0
    heuristic_rows = len(model_paths) * args.games_per_model * 60
    pair_rows = n_pairs * args.games_per_pair * 60 if args.round_robin else 0
    print(f"Collecting from {len(model_paths)} models, {args.games_per_model} games each vs heuristic")
    if args.round_robin:
        print(f"Round-robin: {n_pairs} pairs, {args.games_per_pair} games each")
    print(f"Expected: ~{heuristic_rows + pair_rows} rows")
    print()

    all_tables = []
    total_rows = 0
    t0 = time.time()

    for i, model_path in enumerate(model_paths):
        if args.games_per_model <= 0:
            break
        name = Path(model_path).stem
        print(f"[{i+1}/{len(model_paths)}] {name} ({args.games_per_model} games)...", end=" ", flush=True)

        t1 = time.time()
        data = collect_from_model(
            model_path=model_path,
            n_games=args.games_per_model,
            seed=args.seed + i * 100000,
            pool_size=args.pool_size,
            temperature=args.temperature,
            gamma=args.gamma,
            lam=args.gae_lambda,
        )

        table = arrays_to_table(data)
        n_rows = len(table)
        total_rows += n_rows
        elapsed = time.time() - t1

        # Advantage stats
        adv = data["advantage"]
        print(f"{n_rows:,} rows, adv=[{adv.min():.2f}, {adv.max():.2f}], {elapsed:.1f}s")

        all_tables.append(table)

    # Round-robin model-vs-model collection
    if args.round_robin and len(model_paths) >= 2:
        from itertools import combinations
        pairs = list(combinations(range(len(model_paths)), 2))
        print(f"\nRound-robin: {len(pairs)} pairs, {args.games_per_pair} games each")

        for pi, (a, b) in enumerate(pairs):
            name_a = Path(model_paths[a]).stem
            name_b = Path(model_paths[b]).stem
            print(f"  [{pi+1}/{len(pairs)}] {name_a} vs {name_b}...", end=" ", flush=True)

            t1 = time.time()
            data = collect_from_pair(
                model_a_path=model_paths[a],
                model_b_path=model_paths[b],
                n_games=args.games_per_pair,
                seed=args.seed + 500000 + pi * 100000,
                pool_size=args.pool_size,
                temperature=args.temperature,
                gamma=args.gamma,
                lam=args.gae_lambda,
            )

            table = arrays_to_table(data)
            n_rows = len(table)
            total_rows += n_rows
            elapsed = time.time() - t1
            adv = data["advantage"]
            print(f"{n_rows:,} rows, adv=[{adv.min():.2f}, {adv.max():.2f}], {elapsed:.1f}s")
            all_tables.append(table)

    # Merge all tables
    merged = pa.concat_tables(all_tables)

    # Save
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.append and out_path.exists():
        existing = pq.read_table(out_path)
        merged = pa.concat_tables([existing, merged])
        print(f"\nAppended to existing: {len(existing):,} + {total_rows:,} = {len(merged):,} rows")
        total_rows = len(merged)

    pq.write_table(merged, out_path, compression="zstd")

    elapsed_total = time.time() - t0
    file_size = out_path.stat().st_size / (1024 * 1024)
    print(f"\nSaved {total_rows:,} rows to {out_path} ({file_size:.1f} MB)")
    print(f"Total time: {elapsed_total:.0f}s ({elapsed_total/60:.1f} min)")

    # Print summary stats
    print(f"\nColumn shapes:")
    for col in merged.column_names[:5]:
        arr = merged.column(col)
        print(f"  {col}: {arr.type}")


if __name__ == "__main__":
    main()
