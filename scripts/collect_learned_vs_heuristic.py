"""Collect learned-vs-heuristic games using batched threaded inference.

The learned model (from checkpoint) plays one side, and the MinimalHybrid heuristic
plays the other. Games are split 50-50:
  - game_idx % 2 == 0: learned plays USSR, heuristic plays US
  - game_idx % 2 == 1: learned plays US, heuristic plays USSR

This breaks learned-model policy collapse by adding diversity via heuristic play.

Usage::

    uv run python scripts/collect_learned_vs_heuristic.py \\
        --checkpoint data/checkpoints/retrain_v10/baseline_best.pt \\
        --n-games 2000 \\
        --workers 14 \\
        --batch-size 8 \\
        --seed 15000 \\
        --out data/selfplay/learned_v10_vs_heuristic_2k_seed15000.parquet
"""
from __future__ import annotations

import argparse
import copy
import datetime
import logging
import os
import queue
import random
import sys
import threading
from pathlib import Path

import torch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

_GAMES_PER_PART = 50
_MID_WAR_TURN = 4
_LATE_WAR_TURN = 8
_MAX_TURNS = 10


class BatchInferenceServer:
    """Batches model inference across concurrent game threads."""

    def __init__(self, model, batch_size: int, flush_timeout: float = 0.005):
        self.model = model
        self.batch_size = batch_size
        self.flush_timeout = flush_timeout
        self._queue: queue.Queue[tuple[torch.Tensor, torch.Tensor, torch.Tensor, queue.Queue]] = (
            queue.Queue()
        )
        self._stop = threading.Event()
        self._batcher_thread = threading.Thread(target=self._batcher, daemon=True)
        self._batcher_thread.start()

    def request(self, influence, cards, scalars):
        """Submit one inference request and block until its result is ready."""
        result_q: queue.Queue[dict[str, torch.Tensor]] = queue.Queue(maxsize=1)
        self._queue.put((influence, cards, scalars, result_q))
        return result_q.get()

    def stop(self):
        self._stop.set()
        self._batcher_thread.join(timeout=2.0)

    def _batcher(self):
        pending = []
        while not self._stop.is_set():
            try:
                item = self._queue.get(timeout=self.flush_timeout)
                pending.append(item)
                while len(pending) < self.batch_size:
                    try:
                        pending.append(self._queue.get_nowait())
                    except queue.Empty:
                        break
                if len(pending) >= self.batch_size:
                    self._flush(pending)
                    pending = []
            except queue.Empty:
                if pending:
                    self._flush(pending)
                    pending = []
        if pending:
            self._flush(pending)

    def _flush(self, items):
        influence = torch.cat([x[0] for x in items], dim=0)
        cards_t = torch.cat([x[1] for x in items], dim=0)
        scalars = torch.cat([x[2] for x in items], dim=0)
        with torch.no_grad():
            outputs = self.model(influence, cards_t, scalars)
        for i, (*_, result_q) in enumerate(items):
            result_q.put({k: v[i : i + 1] for k, v in outputs.items()})


def _sample_index_from_probs(probs: torch.Tensor, rng: random.Random) -> int:
    values = probs.tolist()
    total = float(sum(values))
    if total <= 0.0:
        raise ValueError("probabilities must sum to > 0")
    target = rng.random() * total
    cumulative = 0.0
    for idx, value in enumerate(values):
        cumulative += float(value)
        if target <= cumulative or idx == len(values) - 1:
            return idx
    raise RuntimeError("failed to sample from probability vector")


def _extract_features(pub, hand: frozenset[int], holds_china: bool, side):
    from tsrl.policies.learned_policy import _extract_features as _base_extract_features

    return _base_extract_features(pub, hand, holds_china, side)


def _normalize_influence_features(
    influence: torch.Tensor,
    expected_dim: int,
) -> torch.Tensor:
    actual_dim = int(influence.shape[1])
    if actual_dim == expected_dim:
        return influence
    if actual_dim == expected_dim + 2 and expected_dim % 2 == 0:
        half = actual_dim // 2
        return torch.cat([influence[:, 1:half], influence[:, half + 1 :]], dim=1)
    if actual_dim > expected_dim:
        return influence[:, :expected_dim]
    pad = torch.zeros(
        (influence.shape[0], expected_dim - actual_dim),
        dtype=influence.dtype,
        device=influence.device,
    )
    return torch.cat([influence, pad], dim=1)


def _build_random_targets(card_id, mode, pub, side, adj, rng):
    from tsrl.engine.legal_actions import accessible_countries, effective_ops
    from tsrl.schemas import ActionEncoding, ActionMode

    accessible = sorted(accessible_countries(side, pub, adj, mode=mode))
    if not accessible:
        return None
    if mode in (ActionMode.COUP, ActionMode.REALIGN):
        return ActionEncoding(card_id=card_id, mode=mode, targets=(rng.choice(accessible),))
    ops = effective_ops(card_id, pub, side)
    targets = tuple(rng.choice(accessible) for _ in range(ops))
    return ActionEncoding(card_id=card_id, mode=mode, targets=targets)


def _build_action_from_country_logits(
    card_id,
    mode,
    country_logits: torch.Tensor,
    pub,
    side,
    adj,
    rng: random.Random,
    strategy_logits: torch.Tensor | None = None,
    country_strategy_logits: torch.Tensor | None = None,
):
    from tsrl.engine.legal_actions import accessible_countries, effective_ops
    from tsrl.schemas import ActionEncoding, ActionMode

    accessible = sorted(accessible_countries(side, pub, adj, mode=mode))
    if not accessible:
        return None

    valid_accessible = [c for c in accessible if 1 <= c <= 84]
    if not valid_accessible:
        return None
    indices = torch.tensor([c - 1 for c in valid_accessible], dtype=torch.long)
    source_logits = country_logits
    if strategy_logits is not None and country_strategy_logits is not None:
        strategy_idx = int(strategy_logits.argmax().item())
        source_logits = country_strategy_logits[strategy_idx]

    masked = torch.full_like(source_logits, float("-inf"))
    masked[indices] = source_logits[indices]
    probs = torch.softmax(masked, dim=0)

    if mode in (ActionMode.COUP, ActionMode.REALIGN):
        target = _sample_index_from_probs(probs, rng) + 1
        return ActionEncoding(card_id=card_id, mode=mode, targets=(target,))

    ops = effective_ops(card_id, pub, side)
    accessible_probs = probs[indices]
    alloc = accessible_probs * ops
    floor_alloc = torch.floor(alloc).to(dtype=torch.long)
    remainder = ops - int(floor_alloc.sum().item())

    if remainder > 0:
        fractional = alloc - floor_alloc.to(dtype=alloc.dtype)
        order = sorted(
            range(len(valid_accessible)),
            key=lambda idx: (-float(fractional[idx].item()), valid_accessible[idx]),
        )
        for idx in order[:remainder]:
            floor_alloc[idx] += 1

    targets_list: list[int] = []
    for country_id, count in zip(valid_accessible, floor_alloc.tolist()):
        targets_list.extend([country_id] * count)
    return ActionEncoding(card_id=card_id, mode=mode, targets=tuple(targets_list))


def _load_model(checkpoint_path: str):
    from tsrl.policies.model import TSBaselineModel

    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    model = TSBaselineModel()
    model.load_state_dict(state_dict, strict=False)
    has_strategy_heads = all(
        key in state_dict
        for key in (
            "strategy_heads.weight",
            "strategy_heads.bias",
            "strategy_mixer.weight",
            "strategy_mixer.bias",
        )
    )
    model.eval()
    return model, has_strategy_heads, model.influence_encoder.in_features


def _make_thread_policy(
    server: BatchInferenceServer,
    side,
    has_strategy_heads: bool,
    expected_influence_dim: int,
    rng,
):
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency
    from tsrl.schemas import ActionEncoding, ActionMode

    adj = load_adjacency()

    def _policy(pub, hand: frozenset[int], holds_china: bool):
        hand_set = frozenset(hand)
        playable = legal_cards(hand_set, pub, side, holds_china=holds_china)
        if not playable:
            return None

        influence, cards, scalars = _extract_features(pub, hand_set, holds_china, side)
        influence = _normalize_influence_features(influence, expected_influence_dim)
        outputs = server.request(influence, cards, scalars)
        card_logits = outputs["card_logits"][0]
        country_logits = outputs.get("country_logits")
        if country_logits is not None:
            country_logits = country_logits[0]
        strategy_logits = outputs.get("strategy_logits")
        if strategy_logits is not None:
            strategy_logits = strategy_logits[0]
        country_strategy_logits = outputs.get("country_strategy_logits")
        if country_strategy_logits is not None:
            country_strategy_logits = country_strategy_logits[0]

        legal_card_ids = sorted(playable)
        masked_card = torch.full_like(card_logits, float("-inf"))
        legal_indices = torch.tensor([c - 1 for c in legal_card_ids], dtype=torch.long)
        masked_card[legal_indices] = card_logits[legal_indices]
        card_probs = torch.softmax(masked_card, dim=0)
        sampled_card_id = _sample_index_from_probs(card_probs, rng) + 1

        modes = list(legal_modes(sampled_card_id, pub, side, adj=adj))
        if not modes:
            return None
        mode = rng.choice(modes)

        if mode in (ActionMode.SPACE, ActionMode.EVENT):
            return ActionEncoding(card_id=sampled_card_id, mode=mode, targets=())

        if has_strategy_heads and country_logits is not None:
            action = _build_action_from_country_logits(
                sampled_card_id,
                mode,
                country_logits,
                pub,
                side,
                adj,
                rng,
                strategy_logits=strategy_logits,
                country_strategy_logits=country_strategy_logits,
            )
            if action is not None:
                return action

        return _build_random_targets(sampled_card_id, mode, pub, side, adj, rng)

    return _policy


def _make_heuristic_policy(side, rng):
    """Create a heuristic policy wrapper for the given side."""
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid

    def _policy(pub, hand: frozenset[int], holds_china: bool):
        return choose_minimal_hybrid(pub, hand, holds_china)

    return _policy


def _collect_learned_game(seed: int, learned_policy, heuristic_policy, learned_side):
    from tsrl.engine.game_loop import (
        GameResult,
        _end_of_turn,
        _run_action_rounds,
        _run_headline_phase,
    )
    from tsrl.engine.game_state import (
        _ars_for_turn,
        advance_to_late_war,
        advance_to_mid_war,
        deal_cards,
        reset,
    )
    from tsrl.engine.legal_actions import sample_action
    from tsrl.engine.mcts import SelfPlayStep
    from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Side
    from tsrl.selfplay.collector import _GAME_RESULT_STR, _step_to_row

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))
    steps: list[SelfPlayStep] = []
    pending: list[SelfPlayStep | None] = [None]

    def _snapshot_pub(p: PublicState) -> PublicState:
        c = copy.copy(p)
        c.milops = list(p.milops)
        c.space = list(p.space)
        c.space_attempts = list(p.space_attempts)
        c.ops_modifier = list(p.ops_modifier)
        c.influence = p.influence.copy()
        return c

    def _wrap(base_policy):
        def _policy(pub: PublicState, hand: frozenset[int], holds_china: bool):
            if pending[0] is not None:
                pending[0].post_pub = _snapshot_pub(gs.pub)
                pending[0] = None

            side = pub.phasing
            action = base_policy(pub, hand, holds_china)
            if action is None:
                action = sample_action(hand, pub, side, holds_china=holds_china, rng=rng)

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
                    side=side,
                    hand=hand,
                    holds_china=holds_china,
                    action=recorded_action,
                )
                steps.append(step)
                pending[0] = step

            return action

        return _policy

    learned_wrapped = _wrap(learned_policy)
    heuristic_wrapped = _wrap(heuristic_policy)

    # Assign USSR/US args in the order the game loop expects
    if learned_side == Side.USSR:
        ussr_arg, us_arg = learned_wrapped, heuristic_wrapped
    else:
        ussr_arg, us_arg = heuristic_wrapped, learned_wrapped

    result = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, rng)
        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)
        result = _run_headline_phase(gs, ussr_arg, us_arg, rng)
        if result is not None:
            break
        result = _run_action_rounds(gs, ussr_arg, us_arg, rng, _ars_for_turn(turn))
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

    if pending[0] is not None:
        pending[0].post_pub = _snapshot_pub(gs.pub)

    for step in steps:
        step.game_result = result

    game_id = f"learned_vs_heuristic_{seed}"
    rows = []
    for step_idx, step in enumerate(steps):
        try:
            rows.append(_step_to_row(step, game_id, step_idx))
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


def _worker_loop(
    *,
    worker_id: int,
    seed_base: int,
    n_games: int,
    counter_lock: threading.Lock,
    next_game_idx: list[int],
    completed_games: list[int],
    results_q: queue.Queue,
    server: BatchInferenceServer,
    has_strategy_heads: bool,
    expected_influence_dim: int,
):
    from tsrl.schemas import Side

    try:
        os.nice(10)
    except OSError:
        pass

    while True:
        with counter_lock:
            if next_game_idx[0] >= n_games:
                return
            game_idx = next_game_idx[0]
            next_game_idx[0] += 1
        seed = seed_base + game_idx
        rng = random.Random(seed ^ ((worker_id + 1) * 1_000_003))

        # Determine which side the learned model plays
        # game_idx % 2 == 0: learned plays USSR
        # game_idx % 2 == 1: learned plays US
        learned_side = Side.USSR if game_idx % 2 == 0 else Side.US
        heuristic_side = Side.US if learned_side == Side.USSR else Side.USSR

        learned_policy = _make_thread_policy(
            server, learned_side, has_strategy_heads, expected_influence_dim, rng
        )
        heuristic_policy = _make_heuristic_policy(heuristic_side, rng)

        try:
            rows, summary = _collect_learned_game(seed, learned_policy, heuristic_policy, learned_side)
            log.info(
                "game %-35s  steps=%d  result=%-10s  vp=%+d  end_turn=%d",
                summary["game_id"],
                summary["steps"],
                summary["result"],
                summary["vp"],
                summary["end_turn"],
            )
        except Exception as exc:
            log.warning("game seed=%d idx=%d failed: %s", seed, game_idx, exc)
            rows, summary = [], {}
        with counter_lock:
            completed_games[0] += 1
        results_q.put((game_idx, rows, summary))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collect learned-vs-heuristic games with batched inference.",
    )
    parser.add_argument("--checkpoint", required=True, help="Path to model checkpoint.")
    parser.add_argument(
        "--n-games",
        type=int,
        default=2000,
        help="Number of games to collect (default: 2000)",
    )
    parser.add_argument("--out", default=None, help="Output Parquet file path.")
    parser.add_argument("--seed", type=int, default=42, help="Base RNG seed (default: 42)")
    parser.add_argument(
        "--workers",
        type=int,
        default=16,
        help="Parallel game threads (default: 16)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=8,
        help="Inference batch size (default: 8)",
    )
    args = parser.parse_args(argv)

    if args.n_games <= 0:
        raise ValueError("--n-games must be > 0")
    if args.workers <= 0:
        raise ValueError("--workers must be > 0")
    if args.batch_size <= 0:
        raise ValueError("--batch-size must be > 0")

    try:
        os.nice(10)
    except OSError:
        pass

    if args.out is None:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        args.out = (
            f"data/selfplay/learned_vs_heuristic_{args.n_games}games_{ts}_seed{args.seed}.parquet"
        )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    log.info(
        "Collecting %d learned-vs-heuristic games  |  workers=%d  |  batch_size=%d  |  checkpoint=%s"
        "  |  seed=%d  ->  %s",
        args.n_games,
        args.workers,
        args.batch_size,
        args.checkpoint,
        args.seed,
        out_path,
    )

    model, has_strategy_heads, expected_influence_dim = _load_model(args.checkpoint)
    server = BatchInferenceServer(model, batch_size=args.batch_size)
    counter_lock = threading.Lock()
    next_game_idx = [0]
    completed_games = [0]
    results_q: queue.Queue[tuple[int, list[dict], dict]] = queue.Queue()
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

    threads = [
        threading.Thread(
            target=_worker_loop,
            kwargs={
                "worker_id": worker_id,
                "seed_base": args.seed,
                "n_games": args.n_games,
                "counter_lock": counter_lock,
                "next_game_idx": next_game_idx,
                "completed_games": completed_games,
                "results_q": results_q,
                "server": server,
                "has_strategy_heads": has_strategy_heads,
                "expected_influence_dim": expected_influence_dim,
            },
            daemon=True,
        )
        for worker_id in range(args.workers)
    ]

    for thread in threads:
        thread.start()

    try:
        received_games = 0
        while received_games < args.n_games:
            _, rows, _ = results_q.get()
            batch_rows.extend(rows)
            batch_games += 1
            received_games += 1
            if batch_games >= _GAMES_PER_PART:
                _flush_batch()
    finally:
        for thread in threads:
            thread.join()
        server.stop()

    _flush_batch()

    if not part_paths:
        log.error("No rows collected; check errors above.")
        return 1

    _concat_part_parquets(part_paths, out_path)

    if out_path.exists() and out_path.stat().st_size > 0:
        for part_path in part_paths:
            part_path.unlink()
        log.info(
            "Done. %d rows total from %d games. completed_games=%d",
            total_rows,
            args.n_games,
            completed_games[0],
        )
        return 0

    log.error(
        "Merge output missing or empty; part files kept for recovery: %s",
        [str(p) for p in part_paths],
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
