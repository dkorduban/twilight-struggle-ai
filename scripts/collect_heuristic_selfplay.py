"""
Collect self-play games using the MinimalHybrid heuristic policy for both sides.

Writes decision-point rows to a single Parquet file using the same schema as
the MCTS collector (python/tsrl/selfplay/collector.py).

Usage::

    nice -n 10 uv run python scripts/collect_heuristic_selfplay.py \\
        --n-games 1000 --workers 4 --seed 42 \\
        --out data/selfplay/heuristic_1000games.parquet

Each row is one decision point; schema is identical to MCTS-produced files so
train_baseline.py can consume both together.
"""
from __future__ import annotations

import argparse
import datetime
import logging
import multiprocessing
import os
import random
import sys
from copy import copy
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Single-game collector (mirrors mcts.py collect_self_play_game structure)
# ---------------------------------------------------------------------------


def _collect_heuristic_game(seed: int) -> tuple[list[dict], dict]:
    """Play one complete heuristic-vs-heuristic game, return (rows, summary).

    Uses choose_minimal_hybrid for both sides.  Falls back to a random action
    if the heuristic returns None (should not happen in practice).

    Returns a list of row dicts ready for polars + a summary dict.
    """
    from tsrl.engine.game_loop import (
        GameResult,
        DecisionRequest,
        _run_game_gen,
    )
    from tsrl.engine.game_state import reset
    from tsrl.engine.legal_actions import sample_action
    from tsrl.engine.mcts import SelfPlayStep
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid
    from tsrl.selfplay.collector import _step_to_row, _encode_result, _GAME_RESULT_STR
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    rng = random.Random(seed)
    gs = reset(seed=seed)
    steps: list[SelfPlayStep] = []
    pending_step: SelfPlayStep | None = None

    def _snapshot_pub(pub: PublicState) -> PublicState:
        snap = copy(pub)
        snap.milops = list(pub.milops)
        snap.space = list(pub.space)
        snap.space_attempts = list(pub.space_attempts)
        snap.ops_modifier = list(pub.ops_modifier)
        snap.influence = pub.influence.copy()
        return snap

    gen = _run_game_gen(gs, rng, max_turns=10)

    try:
        req = next(gen)
    except StopIteration as exc:
        result = exc.value
    else:
        while True:
            assert isinstance(req, DecisionRequest)
            action = choose_minimal_hybrid(req.pub, req.hand, req.holds_china)
            if action is None:
                action = sample_action(
                    req.hand,
                    req.pub,
                    req.side,
                    holds_china=req.holds_china,
                    rng=rng,
                )
            if action is None and req.pub.ar == 0 and req.hand:
                action = ActionEncoding(
                    card_id=rng.choice(sorted(req.hand)),
                    mode=ActionMode.EVENT,
                    targets=(),
                )
            if action is not None:
                recorded_action = action
                if req.pub.ar == 0:
                    recorded_action = ActionEncoding(
                        card_id=action.card_id,
                        mode=ActionMode.EVENT,
                        targets=(),
                    )

                current_step = SelfPlayStep(
                    pub_snapshot=_snapshot_pub(req.pub),
                    side=req.side,
                    hand=req.hand,
                    holds_china=req.holds_china,
                    action=recorded_action,
                )
                steps.append(current_step)
                pending_step = current_step

            try:
                req = gen.send(action)
            except StopIteration as exc:
                result = exc.value
                if pending_step is not None:
                    pending_step.post_pub = _snapshot_pub(gs.pub)
                    pending_step = None
                break

            if pending_step is not None:
                pending_step.post_pub = _snapshot_pub(gs.pub)
                pending_step = None

    if pending_step is not None:
        pending_step.post_pub = _snapshot_pub(gs.pub)
        pending_step = None

    if not isinstance(result, GameResult):
        raise RuntimeError("game generator ended without a GameResult")

    # Annotate all steps with game result.
    for step in steps:
        step.game_result = result

    # Build row dicts
    game_id = f"heuristic_{seed}"
    rows = []
    for step_idx, step in enumerate(steps):
        try:
            row = _step_to_row(step, game_id, step_idx)
            rows.append(row)
        except Exception as exc:
            log.warning("step %d row build failed: %s", step_idx, exc)

    summary = {
        "game_id": game_id,
        "steps": len(rows),
        "result": _GAME_RESULT_STR[result.winner],
        "vp": result.final_vp,
        "end_turn": result.end_turn,
    }
    return rows, summary


# ---------------------------------------------------------------------------
# Worker (top-level for multiprocessing pickling)
# ---------------------------------------------------------------------------


def _worker(args: tuple[int, int]) -> tuple[list[dict], dict]:
    """Worker: (game_idx, seed) -> (rows, summary)."""
    try:
        os.nice(10)
    except OSError:
        pass
    game_idx, seed = args
    try:
        rows, summary = _collect_heuristic_game(seed)
        log.info(
            "game %-35s  steps=%d  result=%-10s  vp=%+d  end_turn=%d",
            summary["game_id"],
            summary["steps"],
            summary["result"],
            summary["vp"],
            summary["end_turn"],
        )
        return rows, summary
    except Exception as exc:
        log.warning("game seed=%d idx=%d failed: %s", seed, game_idx, exc)
        return [], {}


# ---------------------------------------------------------------------------
# Parquet writer
# ---------------------------------------------------------------------------


def _write_parquet(rows: list[dict], out_path: Path) -> None:
    import polars as pl

    if not rows:
        log.warning("No rows to write; skipping %s", out_path)
        return
    df = pl.DataFrame(rows)
    df.write_parquet(str(out_path))
    log.info("Wrote %d rows  (%d columns)  ->  %s", len(rows), len(df.columns), out_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collect heuristic-vs-heuristic self-play games.",
    )
    parser.add_argument("--n-games", type=int, default=500,
                        help="Number of games to collect (default: 500)")
    parser.add_argument("--out", default="data/selfplay/heuristic_games.parquet",
                        help="Output Parquet file path")
    parser.add_argument("--seed", type=int, default=42,
                        help="Base RNG seed (default: 42)")
    parser.add_argument("--workers", type=int, default=1,
                        help="Parallel worker processes (default: 1)")
    args = parser.parse_args(argv)

    try:
        os.nice(10)
    except OSError:
        pass

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    log.info(
        "Collecting %d heuristic games  |  workers=%d  |  base_seed=%d  ->  %s",
        args.n_games, args.workers, args.seed, out_path,
    )

    work_items = [
        (game_idx, args.seed + game_idx)
        for game_idx in range(args.n_games)
    ]

    all_rows: list[dict] = []
    summaries: list[dict] = []

    if args.workers > 1:
        with multiprocessing.Pool(processes=args.workers) as pool:
            for rows, summary in pool.imap_unordered(_worker, work_items):
                all_rows.extend(rows)
                if summary:
                    summaries.append(summary)
    else:
        for item in work_items:
            rows, summary = _worker(item)
            all_rows.extend(rows)
            if summary:
                summaries.append(summary)

    if not all_rows:
        log.error("No rows collected; check errors above.")
        return 1

    # Summary statistics
    n_games_ok = len(summaries)
    if summaries:
        import statistics
        step_counts = [s["steps"] for s in summaries if s.get("steps")]
        results = [s["result"] for s in summaries if s.get("result")]
        result_counts: dict[str, int] = {}
        for r in results:
            result_counts[r] = result_counts.get(r, 0) + 1
        log.info(
            "Completed %d/%d games  |  steps: min=%d  median=%d  max=%d  |  outcomes: %s",
            n_games_ok, args.n_games,
            min(step_counts), int(statistics.median(step_counts)), max(step_counts),
            result_counts,
        )

    _write_parquet(all_rows, out_path)
    log.info("Done.  Total rows: %d  ->  %s", len(all_rows), out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
