"""Collect learned self-play games using multiprocessing + vectorized runner.

Each worker process loads its own TSBaselineModel checkpoint and runs a slice of
games via run_games_vectorized(). Results are written as partial Parquet files,
then concatenated into the requested output path.

Usage::

    nice -n 10 uv run python scripts/collect_learned_selfplay_batched.py \
        --checkpoint data/checkpoints/retrain_v5/baseline_best.pt \
        --n-games 100 \
        --workers 8 \
        --seed 42
"""
from __future__ import annotations

import argparse
import datetime
import logging
import multiprocessing
import os
import random
import sys
from pathlib import Path
from typing import Any

import torch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

_MAX_TURNS = 10


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

    valid_accessible = [c for c in accessible if 0 <= c <= 85]
    if not valid_accessible:
        return None
    indices = torch.tensor([c for c in valid_accessible], dtype=torch.long)
    source_logits = country_logits
    if strategy_logits is not None and country_strategy_logits is not None:
        strategy_idx = int(strategy_logits.argmax().item())
        source_logits = country_strategy_logits[strategy_idx]

    masked = torch.full_like(source_logits, float("-inf"))
    masked[indices] = source_logits[indices]
    probs = torch.softmax(masked, dim=0)

    if mode in (ActionMode.COUP, ActionMode.REALIGN):
        target = _sample_index_from_probs(probs, rng)
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
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model = TSBaselineModel(hidden_dim=hidden_dim)
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


def _infer_batch(
    requests,
    model,
    has_strategy_heads: bool,
    expected_influence_dim: int,
    rng: random.Random,
):
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency
    from tsrl.schemas import ActionEncoding, ActionMode

    adj = load_adjacency()

    influence_list = []
    cards_list = []
    scalars_list = []
    for req in requests:
        inf, crd, scl = _extract_features(req.pub, req.hand, req.holds_china, req.side)
        inf = _normalize_influence_features(inf, expected_influence_dim)
        influence_list.append(inf)
        cards_list.append(crd)
        scalars_list.append(scl)

    influence_batch = torch.cat(influence_list, dim=0)
    cards_batch = torch.cat(cards_list, dim=0)
    scalars_batch = torch.cat(scalars_list, dim=0)

    with torch.no_grad():
        outputs = model(influence_batch, cards_batch, scalars_batch)

    card_logits_batch = outputs["card_logits"]
    country_logits_batch = outputs.get("country_logits")
    strategy_logits_batch = outputs.get("strategy_logits")
    country_strategy_logits_batch = outputs.get("country_strategy_logits")

    actions = []
    for i, req in enumerate(requests):
        side = req.side
        pub = req.pub
        hand_set = frozenset(req.hand)
        playable = legal_cards(hand_set, pub, side, holds_china=req.holds_china)

        if not playable:
            from tsrl.engine.legal_actions import sample_action

            action = sample_action(hand_set, pub, side, holds_china=req.holds_china, rng=rng)
            actions.append(action)
            continue

        card_logits = card_logits_batch[i]
        legal_card_ids = sorted(playable)
        masked_card = torch.full_like(card_logits, float("-inf"))
        legal_indices = torch.tensor([c - 1 for c in legal_card_ids], dtype=torch.long)
        masked_card[legal_indices] = card_logits[legal_indices]
        card_probs = torch.softmax(masked_card, dim=0)
        sampled_card_id = _sample_index_from_probs(card_probs, rng) + 1

        modes = list(legal_modes(sampled_card_id, pub, side, adj=adj))
        if not modes:
            from tsrl.engine.legal_actions import sample_action

            action = sample_action(hand_set, pub, side, holds_china=req.holds_china, rng=rng)
            actions.append(action)
            continue

        mode = rng.choice(modes)

        if mode in (ActionMode.SPACE, ActionMode.EVENT):
            actions.append(ActionEncoding(card_id=sampled_card_id, mode=mode, targets=()))
            continue

        country_logits = country_logits_batch[i] if country_logits_batch is not None else None
        strategy_logits = strategy_logits_batch[i] if strategy_logits_batch is not None else None
        cs_logits = (
            country_strategy_logits_batch[i]
            if country_strategy_logits_batch is not None
            else None
        )

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
                country_strategy_logits=cs_logits,
            )
            if action is not None:
                actions.append(action)
                continue

        action = _build_random_targets(sampled_card_id, mode, pub, side, adj, rng)
        if action is None:
            from tsrl.engine.legal_actions import sample_action

            action = sample_action(hand_set, pub, side, holds_china=req.holds_china, rng=rng)
        actions.append(action)

    return actions


def _worker_fn(args: dict[str, Any]) -> dict[str, Any]:
    try:
        os.nice(10)
    except OSError:
        pass

    worker_id: int = args["worker_id"]
    seed_base: int = args["seed_base"]
    game_indices: list[int] = args["game_indices"]
    checkpoint: str = args["checkpoint"]
    out_path_str: str = args["out_path"]

    logging.basicConfig(
        level=logging.INFO,
        format=f"%(asctime)s %(levelname)s worker{worker_id}: %(message)s",
    )
    wlog = logging.getLogger(f"worker{worker_id}")

    from tsrl.engine.game_state import reset
    from tsrl.engine.vec_runner import run_games_vectorized
    from tsrl.schemas import Side
    from tsrl.selfplay.collector import _GAME_RESULT_STR, _step_to_row

    model, has_strategy_heads, expected_influence_dim = _load_model(checkpoint)
    model.eval()
    rng = random.Random(seed_base ^ (worker_id * 1_000_003 + 7))

    n_local = len(game_indices)
    game_counter = [0]

    def make_game_fn():
        global_idx = game_indices[game_counter[0]]
        gs = reset(seed=seed_base + global_idx)
        game_counter[0] += 1
        return gs

    def learned_side_fn(local_game_idx: int) -> Side:
        return Side.USSR if (game_indices[local_game_idx] % 2 == 0) else Side.US

    def learned_infer_fn(requests):
        return _infer_batch(requests, model, has_strategy_heads, expected_influence_dim, rng)

    def heuristic_fn(req):
        return _infer_batch(
            [req], model, has_strategy_heads, expected_influence_dim, rng
        )[0]

    all_rows: list[dict] = []
    completed = [0]

    def on_game_done(local_game_idx, steps, result):
        global_idx = game_indices[local_game_idx]
        game_id = f"learned_{seed_base + global_idx}"
        rows = []
        for step_idx, step in enumerate(steps):
            try:
                rows.append(_step_to_row(step, game_id, step_idx))
            except Exception as exc:
                wlog.warning("step %d row build failed: %s", step_idx, exc)
        all_rows.extend(rows)
        completed[0] += 1
        wlog.info(
            "game %s  steps=%d  result=%-10s  vp=%+d  end_turn=%d  (%d/%d)",
            game_id,
            len(rows),
            _GAME_RESULT_STR[result.winner],
            result.final_vp,
            result.end_turn,
            completed[0],
            n_local,
        )

    run_games_vectorized(
        n_games=n_local,
        make_game_fn=make_game_fn,
        learned_side_fn=learned_side_fn,
        learned_infer_fn=learned_infer_fn,
        heuristic_fn=heuristic_fn,
        seed_base=seed_base,
        max_turns=_MAX_TURNS,
        on_game_done=on_game_done,
    )

    if all_rows:
        import polars as pl

        df = pl.DataFrame(all_rows)
        df.write_parquet(out_path_str)
        wlog.info("Wrote %d rows -> %s", len(all_rows), out_path_str)
    else:
        wlog.warning("No rows collected for worker %d", worker_id)

    return {
        "worker_id": worker_id,
        "rows": len(all_rows),
        "games": completed[0],
        "out_path": out_path_str if all_rows else None,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collect learned-vs-learned self-play games with multiprocessing.",
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
        help="Number of worker processes (default: 16)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=None,
        dest="batch_size",
        help="[deprecated] Use --workers instead. If provided, workers=min(batch_size, 16).",
    )
    args = parser.parse_args(argv)

    if args.n_games <= 0:
        raise ValueError("--n-games must be > 0")

    n_workers = args.workers
    if args.batch_size is not None:
        n_workers = min(args.batch_size, 16)
        log.info("--batch-size %d -> --workers %d", args.batch_size, n_workers)

    n_workers = min(n_workers, args.n_games)

    try:
        os.nice(10)
    except OSError:
        pass

    if args.out is None:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        args.out = (
            f"data/selfplay/learned_batched_{args.n_games}games_{ts}_seed{args.seed}.parquet"
        )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    log.info(
        "Collecting %d learned self-play games  |  workers=%d  |  checkpoint=%s"
        "  |  seed=%d  ->  %s",
        args.n_games,
        n_workers,
        args.checkpoint,
        args.seed,
        out_path,
    )

    all_indices = list(range(args.n_games))
    chunks = [[] for _ in range(n_workers)]
    for i, idx in enumerate(all_indices):
        chunks[i % n_workers].append(idx)

    worker_args = []
    for wid, chunk in enumerate(chunks):
        if not chunk:
            continue
        part_path = out_path.parent / f"part_{wid:04d}.parquet"
        worker_args.append(
            {
                "worker_id": wid,
                "seed_base": args.seed,
                "game_indices": chunk,
                "checkpoint": args.checkpoint,
                "out_path": str(part_path),
            }
        )

    ctx = multiprocessing.get_context("spawn")
    total_rows = 0
    produced_parts: list[str] = []

    with ctx.Pool(processes=n_workers) as pool:
        for result in pool.imap_unordered(_worker_fn, worker_args):
            wid = result["worker_id"]
            log.info(
                "Worker %d done: %d games, %d rows",
                wid,
                result["games"],
                result["rows"],
            )
            total_rows += result["rows"]
            if result["out_path"]:
                produced_parts.append(result["out_path"])

    if not produced_parts:
        log.error("No rows collected; check worker errors above.")
        return 1

    import polars as pl

    pl.concat([pl.scan_parquet(p) for p in produced_parts], how="vertical").sink_parquet(
        str(out_path)
    )

    if out_path.exists() and out_path.stat().st_size > 0:
        for p in produced_parts:
            try:
                Path(p).unlink()
            except OSError:
                pass
        log.info(
            "Done. %d rows total from %d games. -> %s",
            total_rows,
            args.n_games,
            out_path,
        )
        return 0

    log.error(
        "Merge output missing or empty; part files kept: %s",
        produced_parts,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
