"""Collect self-play games using the learned policy for both sides.

Uses the trained TSBaselineModel checkpoint to drive both USSR and US.
Writes decision-point rows to a Parquet file using the same schema as
collect_heuristic_selfplay.py (and the MCTS collector).

Usage::

    uv run python scripts/collect_learned_selfplay.py \\
        --checkpoint data/checkpoints/baseline_epoch20.pt \\
        --n-games 10000 \\
        --out data/selfplay/learned_10k.parquet \\
        --seed 42 \\
        --workers 4
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
# Single-game collector
# ---------------------------------------------------------------------------


def _collect_learned_game(seed: int, ussr_policy, us_policy) -> tuple[list[dict], dict]:
    """Play one complete learned-vs-learned game, return (rows, summary)."""
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
    )
    from tsrl.engine.legal_actions import sample_action
    from tsrl.engine.mcts import SelfPlayStep
    from tsrl.selfplay.collector import _step_to_row, _encode_result, _GAME_RESULT_STR
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))
    steps: list[SelfPlayStep] = []
    _pending: list[SelfPlayStep | None] = [None]

    def _snapshot_pub(p: PublicState) -> PublicState:
        c = copy.copy(p)
        c.milops = list(p.milops)
        c.space = list(p.space)
        c.space_attempts = list(p.space_attempts)
        c.ops_modifier = list(p.ops_modifier)
        c.influence = dict(p.influence)
        return c

    def _make_policy(base_policy):
        def _policy(pub: PublicState, hand: frozenset[int], holds_china: bool):
            if _pending[0] is not None:
                _pending[0].post_pub = _snapshot_pub(gs.pub)
                _pending[0] = None

            _side = pub.phasing
            action = base_policy(pub, hand, holds_china)

            if action is None:
                action = sample_action(hand, pub, _side, holds_china=holds_china, rng=rng)

            if action is not None:
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
        return _policy

    ussr_wrapped = _make_policy(ussr_policy)
    us_wrapped = _make_policy(us_policy)

    result = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, rng)
        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)
        result = _run_headline_phase(gs, ussr_wrapped, us_wrapped, rng)
        if result is not None:
            break
        result = _run_action_rounds(gs, ussr_wrapped, us_wrapped, rng, _ars_for_turn(turn))
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

    if _pending[0] is not None:
        _pending[0].post_pub = _snapshot_pub(gs.pub)

    for step in steps:
        step.game_result = result

    game_id = f"learned_{seed}"
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
# Worker (top-level for pickling)
# ---------------------------------------------------------------------------

_USSR_POLICY = None
_US_POLICY = None
_GAMES_PER_PART = 50


def _worker_init(checkpoint: str) -> None:
    global _USSR_POLICY, _US_POLICY
    from tsrl.policies.learned_policy import make_learned_policy
    from tsrl.schemas import Side

    _USSR_POLICY = make_learned_policy(checkpoint, Side.USSR)
    _US_POLICY = make_learned_policy(checkpoint, Side.US)
    try:
        os.nice(10)
    except OSError:
        pass


def _worker(args: tuple[int, int]) -> tuple[list[dict], dict]:
    game_idx, seed = args
    try:
        if _USSR_POLICY is None or _US_POLICY is None:
            raise RuntimeError("worker policies not initialized")
        rows, summary = _collect_learned_game(seed, _USSR_POLICY, _US_POLICY)
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


def _concat_part_parquets(part_paths: list[Path], out_path: Path) -> None:
    import polars as pl

    pl.concat([pl.scan_parquet(str(path)) for path in part_paths], how="vertical").sink_parquet(
        str(out_path)
    )
    log.info("Merged %d part files -> %s", len(part_paths), out_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collect learned-vs-learned self-play games.",
    )
    parser.add_argument("--checkpoint", default="data/checkpoints/baseline_epoch20.pt",
                        help="Path to model checkpoint (default: data/checkpoints/baseline_epoch20.pt)")
    parser.add_argument("--n-games", type=int, default=5000,
                        help="Number of games to collect (default: 5000)")
    parser.add_argument("--out", default=None,
                        help="Output Parquet file path (default: auto-named in data/selfplay/)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Base RNG seed (default: 42)")
    parser.add_argument("--workers", type=int, default=4,
                        help="Parallel worker processes (default: 4)")
    args = parser.parse_args(argv)

    try:
        os.nice(10)
    except OSError:
        pass

    if args.out is None:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        args.out = f"data/selfplay/learned_{args.n_games}games_{ts}_seed{args.seed}.parquet"

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    log.info(
        "Collecting %d learned games  |  workers=%d  |  checkpoint=%s  |  seed=%d  ->  %s",
        args.n_games, args.workers, args.checkpoint, args.seed, out_path,
    )

    work_items = [(i, args.seed + i) for i in range(args.n_games)]
    batch_rows: list[dict] = []
    batch_games = 0
    part_idx = 0
    part_paths: list[Path] = []
    total_rows = 0

    def _flush_batch() -> None:
        nonlocal batch_rows, batch_games, part_idx, total_rows
        if not batch_rows:
            batch_games = 0
            return
        part_path = Path(f"{out_path}.part_{part_idx:04d}.parquet")
        _write_parquet(batch_rows, part_path)
        part_paths.append(part_path)
        total_rows += len(batch_rows)
        batch_rows = []
        batch_games = 0
        part_idx += 1

    if args.workers > 1:
        with multiprocessing.Pool(
            processes=args.workers,
            initializer=_worker_init,
            initargs=(args.checkpoint,),
        ) as pool:
            for rows, summary in pool.imap_unordered(_worker, work_items, chunksize=4):
                batch_rows.extend(rows)
                batch_games += 1
                if batch_games >= _GAMES_PER_PART:
                    _flush_batch()
    else:
        _worker_init(args.checkpoint)
        for item in work_items:
            rows, _ = _worker(item)
            batch_rows.extend(rows)
            batch_games += 1
            if batch_games >= _GAMES_PER_PART:
                _flush_batch()

    _flush_batch()

    if not part_paths:
        log.error("No rows collected; check errors above.")
        return 1

    _concat_part_parquets(part_paths, out_path)
    for part_path in part_paths:
        part_path.unlink()

    log.info("Done. %d rows total from %d games.", total_rows, args.n_games)
    return 0


if __name__ == "__main__":
    sys.exit(main())
