"""
Self-play data collection script.

Plays N games using MCTS policies and writes the resulting decision-point
rows to Parquet files in the output directory.

Usage::

    uv run python scripts/collect_selfplay.py [--n-games N] [--n-sim S] \\
        [--out-dir DIR] [--seed SEED] [--workers W] [--flat]

The output directory will contain one or more files named::

    selfplay_<timestamp>_<seed>.parquet

Each file holds all rows from one invocation.
"""
from __future__ import annotations

import argparse
import datetime
import logging
import multiprocessing
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Worker function (top-level for multiprocessing pickling)
# ---------------------------------------------------------------------------


def _worker(args: tuple[int, int, int, bool]) -> list[dict]:
    """Collect a single game; used by multiprocessing.Pool workers.

    Args:
        args: (game_idx, game_seed, n_sim, use_uct)
    """
    import os
    try:
        os.nice(10)  # Run at reduced priority to avoid blocking the OS
    except OSError:
        pass
    game_idx, game_seed, n_sim, use_uct = args
    from tsrl.engine.mcts import collect_self_play_game
    from tsrl.selfplay.collector import _encode_result, _step_to_row, _GAME_RESULT_STR

    game_id = f"selfplay_{game_seed}_{game_idx:04d}"
    try:
        steps, result = collect_self_play_game(
            n_sim=n_sim,
            use_uct=use_uct,
            seed=game_seed,
        )
    except Exception as exc:
        log.warning("game %s failed: %s", game_id, exc)
        return []

    rows = []
    for step_idx, step in enumerate(steps):
        try:
            row = _step_to_row(step, game_id, step_idx)
            rows.append(row)
        except Exception as exc:
            log.warning("game %s step %d failed: %s", game_id, step_idx, exc)

    log.info("game %-35s  steps=%d  result=%s  vp=%d",
             game_id, len(steps),
             _GAME_RESULT_STR[result.winner], result.final_vp)
    return rows


# ---------------------------------------------------------------------------
# Parquet writer
# ---------------------------------------------------------------------------


def _write_parquet(rows: list[dict], out_path: Path) -> None:
    """Write row dicts to Parquet via pyarrow."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    if not rows:
        log.warning("No rows to write; skipping %s", out_path)
        return

    # Build column-oriented dict.
    columns: dict[str, list] = {k: [] for k in rows[0]}
    for row in rows:
        for k, v in row.items():
            columns[k].append(v)

    table = pa.table(columns)
    pq.write_table(table, str(out_path))
    log.info("Wrote %d rows to %s", len(rows), out_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collect self-play games and write Parquet dataset.",
    )
    parser.add_argument("--n-games", type=int, default=100,
                        help="Number of games to collect (default: 100)")
    parser.add_argument("--n-sim", type=int, default=20,
                        help="MCTS simulations per move (default: 20)")
    parser.add_argument("--out-dir", default="data/selfplay",
                        help="Output directory (default: data/selfplay)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Base RNG seed (default: 42)")
    parser.add_argument("--workers", type=int, default=1,
                        help="Parallel worker processes (default: 1)")
    parser.add_argument("--flat", action="store_true",
                        help="Use flat Monte Carlo instead of UCT")
    args = parser.parse_args(argv)

    # Lower process priority so data collection doesn't block the OS.
    import os
    try:
        os.nice(10)
    except OSError:
        pass

    use_uct = not args.flat
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    log.info(
        "Collecting %d games | n_sim=%d | uct=%s | workers=%d | seed=%d",
        args.n_games, args.n_sim, use_uct, args.workers, args.seed,
    )

    # Build per-game argument tuples.
    work_items = [
        (game_idx, args.seed + game_idx, args.n_sim, use_uct)
        for game_idx in range(args.n_games)
    ]

    all_rows: list[dict] = []

    if args.workers > 1:
        with multiprocessing.Pool(processes=args.workers) as pool:
            for game_rows in pool.imap_unordered(_worker, work_items):
                all_rows.extend(game_rows)
    else:
        for item in work_items:
            all_rows.extend(_worker(item))

    if not all_rows:
        log.error("No rows collected; check for errors above.")
        return 1

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"selfplay_{timestamp}_seed{args.seed}.parquet"
    out_path = out_dir / fname

    _write_parquet(all_rows, out_path)

    log.info("Done.  Total rows: %d  →  %s", len(all_rows), out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
