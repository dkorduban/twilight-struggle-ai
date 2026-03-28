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
import copy
import datetime
import logging
import multiprocessing
import os
import sys
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
    import random

    from tsrl.engine.game_loop import (
        GameResult,
        _MID_WAR_TURN,
        _LATE_WAR_TURN,
        _MAX_TURNS,
        _run_headline_phase,
        _run_action_rounds,
        _end_of_turn,
    )
    from tsrl.engine.game_state import (
        reset,
        deal_cards,
        _ars_for_turn,
        advance_to_mid_war,
        advance_to_late_war,
        clone_game_state,
    )
    from tsrl.engine.legal_actions import sample_action
    from tsrl.engine.mcts import SelfPlayStep
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid
    from tsrl.selfplay.collector import _step_to_row, _encode_result, _GAME_RESULT_STR
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))
    steps: list[SelfPlayStep] = []
    _pending: list[SelfPlayStep | None] = [None]

    def _snapshot_pub(p: PublicState) -> PublicState:
        c2 = copy.copy(p)
        c2.milops = list(p.milops)
        c2.space = list(p.space)
        c2.space_attempts = list(p.space_attempts)
        c2.ops_modifier = list(p.ops_modifier)
        c2.influence = dict(p.influence)
        return c2

    def _heuristic_policy(pub: PublicState, hand: frozenset[int], holds_china: bool):
        # Fill post_pub for the previous step now that gs.pub is updated.
        if _pending[0] is not None:
            _pending[0].post_pub = _snapshot_pub(gs.pub)
            _pending[0] = None

        _side = pub.phasing
        action = choose_minimal_hybrid(pub, hand, holds_china)

        if action is None:
            # Fallback: random action
            action = sample_action(hand, pub, _side, holds_china=holds_china, rng=rng)

        if action is not None:
            # During headline phase (ar == 0), game_loop forces the played card
            # to EVENT mode with no targets.  Record the mode-forced action.
            recorded_action = action
            if pub.ar == 0:
                recorded_action = ActionEncoding(
                    card_id=action.card_id,
                    mode=ActionMode.EVENT,
                    targets=(),
                )
            step = SelfPlayStep(
                pub_snapshot=copy.copy(pub),
                side=_side,
                hand=hand,
                holds_china=holds_china,
                action=recorded_action,
            )
            steps.append(step)
            _pending[0] = step

        return action

    # Run full game loop
    result = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, rng)
        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)
        result = _run_headline_phase(gs, _heuristic_policy, _heuristic_policy, rng)
        if result is not None:
            break
        result = _run_action_rounds(gs, _heuristic_policy, _heuristic_policy, rng, _ars_for_turn(turn))
        if result is not None:
            break
        result = _end_of_turn(gs, rng, turn)
        if result is not None:
            break

    if result is None:
        winner = None
        if gs.pub.vp > 0:
            winner = Side.USSR
        elif gs.pub.vp < 0:
            winner = Side.US
        result = GameResult(winner, gs.pub.vp, _MAX_TURNS, "turn_limit")

    # Fill post_pub for the last step.
    if _pending[0] is not None:
        _pending[0].post_pub = _snapshot_pub(gs.pub)

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
