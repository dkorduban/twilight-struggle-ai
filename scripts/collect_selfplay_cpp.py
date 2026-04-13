#!/usr/bin/env python3
"""Collect self-play games using the C++ engine (rollout_self_play_batched).

Both sides use the same learned model (TorchScript scripted checkpoint).
Output is a Parquet file with the same schema as PPO rollout data.

Usage:
    uv run python scripts/collect_selfplay_cpp.py \\
        --checkpoint data/checkpoints/scripted_for_elo/v55_scripted.pt \\
        --n-games 1000 \\
        --seed 42 \\
        --out data/selfplay/v55_selfplay_1k.parquet

    # Collect 500 games per GPU batch (pool_size=64 is good for 4GB VRAM)
    uv run python scripts/collect_selfplay_cpp.py \\
        --checkpoint data/checkpoints/scripted_for_elo/v55_scripted.pt \\
        --n-games 5000 --batch-size 200 --seed 42 \\
        --out data/selfplay/v55_selfplay_5k.parquet
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _p in (
    _REPO_ROOT / "build-ninja" / "bindings",
    _REPO_ROOT / "build" / "bindings",
):
    if any(_p.glob("tscore*.so")):
        sys.path.insert(0, str(_p))
        break
sys.path.insert(0, str(_REPO_ROOT / "python"))

import tscore  # noqa: E402
import polars as pl  # noqa: E402


def collect_batch(
    model_path: str,
    n_games: int,
    seed: int,
    pool_size: int,
    device: str,
    temperature: float,
) -> list[dict]:
    """Run one batch of n_games and return list of step dicts."""
    log.info("Collecting %d games (pool=%d, device=%s, seed=%d) ...", n_games, pool_size, device, seed)
    results, steps, boundaries = tscore.rollout_self_play_batched(
        model_path=model_path,
        n_games=n_games,
        pool_size=pool_size,
        seed=seed,
        device=device,
        temperature=temperature,
        nash_temperatures=True,
    )
    n_defcon1 = sum(1 for r in results if getattr(r, "end_reason", None) and "defcon" in str(r.end_reason).lower())
    log.info(
        "  Collected %d steps from %d games (DEFCON-1: %d/%.0f%%)",
        len(steps), len(results), n_defcon1, 100.0 * n_defcon1 / max(len(results), 1),
    )
    return steps


def steps_to_dataframe(steps: list[dict], iteration: int = 0) -> pl.DataFrame:
    """Convert step dicts from rollout_self_play_batched to a Polars DataFrame."""
    if not steps:
        return pl.DataFrame()

    rows = {
        "influence":           [],
        "cards":               [],
        "scalars":             [],
        "card_id":             [],
        "mode_id":             [],
        "country_targets":     [],
        "side_int":            [],
        "reward":              [],
        "value":               [],
        "gae_return":          [],
        "iteration":           [],
        "raw_ussr_influence":  [],
        "raw_us_influence":    [],
        "raw_turn":            [],
        "raw_ar":              [],
        "raw_defcon":          [],
        "raw_vp":              [],
        "raw_milops":          [],
        "raw_space":           [],
        "hand_card_ids":       [],
    }

    for s in steps:
        rows["influence"].append(s["influence"].tolist())
        rows["cards"].append(s["cards"].tolist())
        rows["scalars"].append(s["scalars"].tolist())
        rows["card_id"].append(int(s["card_idx"]) + 1)   # card_id = card_idx + 1
        rows["mode_id"].append(int(s["mode_idx"]))
        rows["country_targets"].append(list(s["country_targets"]))
        rows["side_int"].append(int(s["side_int"]))
        rows["reward"].append(float(s.get("reward", 0.0)))
        rows["value"].append(float(s["value"]))
        rows["gae_return"].append(float(s.get("gae_return", 0.0)))
        rows["iteration"].append(iteration)
        rows["raw_ussr_influence"].append(s["raw_ussr_influence"].tolist() if "raw_ussr_influence" in s else None)
        rows["raw_us_influence"].append(s["raw_us_influence"].tolist() if "raw_us_influence" in s else None)
        rows["raw_turn"].append(int(s["raw_turn"]) if "raw_turn" in s else None)
        rows["raw_ar"].append(int(s["raw_ar"]) if "raw_ar" in s else None)
        rows["raw_defcon"].append(int(s["raw_defcon"]) if "raw_defcon" in s else None)
        rows["raw_vp"].append(int(s["raw_vp"]) if "raw_vp" in s else None)
        rows["raw_milops"].append(list(s["raw_milops"]) if "raw_milops" in s else None)
        rows["raw_space"].append(list(s["raw_space"]) if "raw_space" in s else None)
        rows["hand_card_ids"].append(list(s["hand_card_ids"]) if "hand_card_ids" in s else None)

    return pl.DataFrame(rows)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--checkpoint", required=True,
        help="Path to TorchScript scripted checkpoint (.pt)",
    )
    p.add_argument("--n-games", type=int, default=1000, help="Total games to collect")
    p.add_argument("--batch-size", type=int, default=200, help="Games per C++ batch")
    p.add_argument("--pool-size", type=int, default=64, help="Concurrent game slots in C++ pool")
    p.add_argument("--seed", type=int, default=42, help="Base random seed")
    p.add_argument("--device", default="cpu", help="'cpu' or 'cuda'")
    p.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature")
    p.add_argument(
        "--out", required=True,
        help="Output parquet path (e.g. data/selfplay/v55_selfplay.parquet)",
    )
    p.add_argument("--force", action="store_true", help="Overwrite output if exists")
    args = p.parse_args()

    out_path = Path(args.out)
    if out_path.exists() and not args.force:
        log.error("Output %s already exists. Use --force to overwrite.", out_path)
        sys.exit(1)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    ckpt = Path(args.checkpoint)
    if not ckpt.exists():
        log.error("Checkpoint not found: %s", ckpt)
        sys.exit(1)

    log.info("Model: %s", ckpt)
    log.info("Collecting %d games in batches of %d ...", args.n_games, args.batch_size)

    all_dfs = []
    collected = 0
    batch_idx = 0

    while collected < args.n_games:
        batch = min(args.batch_size, args.n_games - collected)
        seed = args.seed + batch_idx * 10000
        steps = collect_batch(
            model_path=str(ckpt),
            n_games=batch,
            seed=seed,
            pool_size=min(batch, args.pool_size),
            device=args.device,
            temperature=args.temperature,
        )
        df = steps_to_dataframe(steps, iteration=batch_idx)
        all_dfs.append(df)
        collected += batch
        batch_idx += 1
        log.info("Progress: %d / %d games (%d steps so far)", collected, args.n_games,
                 sum(len(d) for d in all_dfs))

    final_df = pl.concat(all_dfs, how="vertical") if len(all_dfs) > 1 else all_dfs[0]
    final_df.write_parquet(out_path)
    log.info("Saved %d rows → %s", len(final_df), out_path)
    log.info("Columns: %s", final_df.columns)


if __name__ == "__main__":
    main()
