"""Collect learned-vs-heuristic games using multiprocessing + vectorized runner.

The learned model (from checkpoint) plays one side, and the MinimalHybrid heuristic
plays the other. Games are split 50-50:
  - game_idx % 2 == 0: learned plays USSR, heuristic plays US
  - game_idx % 2 == 1: learned plays US, heuristic plays USSR

This breaks learned-model policy collapse by adding diversity via heuristic play.

Each worker process runs run_games_vectorized() for its slice of games — no threads,
no barriers, no GIL contention. The model is loaded on CPU in each worker.

Usage::

    uv run python scripts/collect_learned_vs_heuristic.py \\
        --checkpoint data/checkpoints/retrain_v10/baseline_best.pt \\
        --n-games 2000 \\
        --workers 8 \\
        --seed 15000 \\
        --out data/selfplay/learned_v10_vs_heuristic_2k_seed15000.parquet
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
from typing import Any

import numpy as np
import torch

from tsrl.engine.rng import RNG, make_rng

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

_GAMES_PER_PART = 50
_MAX_TURNS = 10


# ---------------------------------------------------------------------------
# Feature extraction helpers (unchanged from previous version)
# ---------------------------------------------------------------------------

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


def _sample_index_from_probs(probs: torch.Tensor, rng: RNG) -> int:
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


def _build_random_targets(card_id, mode, pub, side, adj, rng):
    from tsrl.engine.legal_actions import accessible_countries, effective_ops
    from tsrl.schemas import ActionEncoding, ActionMode

    accessible = sorted(accessible_countries(side, pub, adj, mode=mode))
    if not accessible:
        return None
    if mode in (ActionMode.COUP, ActionMode.REALIGN):
        return ActionEncoding(card_id=card_id, mode=mode, targets=(int(rng.choice(accessible)),))
    ops = effective_ops(card_id, pub, side)
    targets = tuple(int(rng.choice(accessible)) for _ in range(ops))
    return ActionEncoding(card_id=card_id, mode=mode, targets=targets)


def _build_action_from_country_logits(
    card_id,
    mode,
    country_logits: torch.Tensor,
    pub,
    side,
    adj,
    rng: RNG,
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


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Vectorized inference for a batch of DecisionRequests
# ---------------------------------------------------------------------------

def _infer_batch_value_guided(
    requests,
    model,
    has_strategy_heads: bool,
    expected_influence_dim: int,
    rng: RNG,
    top_k: int = 4,
):
    """1-ply value-guided action selection.

    For each request, take the top-k cards by policy logit, apply each to a
    cloned state, batch-evaluate the resulting states with the value head, and
    pick the candidate with the best predicted value for our side.

    Falls back to policy-only for SPACE/EVENT modes (no board-state change
    worth evaluating) and whenever lookahead fails.
    """
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency
    from tsrl.engine.step import apply_action
    from tsrl.schemas import ActionEncoding, ActionMode

    adj = load_adjacency()

    # ── First pass: standard policy forward to get card/mode/country logits ──
    influence_list, cards_list, scalars_list = [], [], []
    for req in requests:
        inf, crd, scl = _extract_features(req.pub, req.hand, req.holds_china, req.side)
        inf = _normalize_influence_features(inf, expected_influence_dim)
        influence_list.append(inf)
        cards_list.append(crd)
        scalars_list.append(scl)

    influence_batch = torch.cat(influence_list)
    cards_batch = torch.cat(cards_list)
    scalars_batch = torch.cat(scalars_list)

    with torch.no_grad():
        first_pass = model(influence_batch, cards_batch, scalars_batch)

    card_logits_batch = first_pass["card_logits"]
    mode_logits_batch = first_pass.get("mode_logits")
    country_logits_batch = first_pass.get("country_logits")
    strategy_logits_batch = first_pass.get("strategy_logits")
    cs_logits_batch = first_pass.get("country_strategy_logits")

    # ── Build candidate (card, mode, action) for each request ────────────────
    # candidate_rows[request_idx] = list of (card_id, mode, action, next_pub | None)
    candidate_rows: list[list[tuple]] = [[] for _ in requests]

    lookahead_rng = make_rng(int(rng.integers(0, 2**31)))  # throwaway rng for stochastic lookahead

    for i, req in enumerate(requests):
        pub = req.pub
        side = req.side
        hand_set = frozenset(req.hand)
        playable = legal_cards(hand_set, pub, side, holds_china=req.holds_china)
        if not playable:
            continue

        card_logits = card_logits_batch[i]
        legal_ids = sorted(playable)
        masked = torch.full_like(card_logits, float("-inf"))
        legal_indices = torch.tensor([c - 1 for c in legal_ids], dtype=torch.long)
        masked[legal_indices] = card_logits[legal_indices]

        # Top-k cards by policy
        k = min(top_k, len(legal_ids))
        top_indices = masked.topk(k).indices.tolist()
        top_card_ids = [idx + 1 for idx in top_indices if idx + 1 in set(legal_ids)]
        if not top_card_ids:
            top_card_ids = legal_ids[:k]

        for card_id in top_card_ids:
            modes = list(legal_modes(card_id, pub, side, adj=adj))
            if not modes:
                continue

            # Best mode by mode logit; skip EVENT/SPACE for lookahead (no meaningful pub change)
            if mode_logits_batch is not None:
                ml = mode_logits_batch[i]
                mode_mask = torch.full_like(ml, float("-inf"))
                for m in modes:
                    mode_mask[int(m)] = 0.0
                mode = ActionMode(int((ml + mode_mask).argmax().item()))
            else:
                mode = modes[0]

            # DEFCON safety guards (same as standard infer)
            if mode == ActionMode.COUP and pub.defcon <= 2:
                safe = [m for m in modes if m != ActionMode.COUP]
                if not safe:
                    continue
                mode = safe[0]
            if mode == ActionMode.EVENT and pub.defcon <= 2:
                from tsrl.policies.minimal_hybrid import _DEFCON_LOWERING_CARDS
                if card_id in _DEFCON_LOWERING_CARDS:
                    safe = [m for m in modes if m != ActionMode.EVENT]
                    if safe:
                        mode = safe[0]

            # Build action
            if mode in (ActionMode.SPACE, ActionMode.EVENT):
                action = ActionEncoding(card_id=card_id, mode=mode, targets=())
                next_pub = None  # skip lookahead for these modes
            else:
                cl = country_logits_batch[i] if country_logits_batch is not None else None
                sl = strategy_logits_batch[i] if strategy_logits_batch is not None else None
                csl = cs_logits_batch[i] if cs_logits_batch is not None else None
                if has_strategy_heads and cl is not None:
                    action = _build_action_from_country_logits(
                        card_id, mode, cl, pub, side, adj, rng, sl, csl)
                else:
                    action = _build_random_targets(card_id, mode, pub, side, adj, rng)
                if action is None:
                    continue
                # Apply to get next pub state (non-mutating)
                try:
                    next_pub, _over, _winner = apply_action(pub, action, side, rng=lookahead_rng)
                except Exception:
                    next_pub = None

            candidate_rows[i].append((card_id, mode, action, next_pub))

    # ── Batch-evaluate next states with value head ────────────────────────────
    # Collect all (request_idx, candidate_idx, features) with a valid next_pub
    eval_meta: list[tuple[int, int]] = []
    eval_inf, eval_cards, eval_scalars = [], [], []
    for i, req in enumerate(requests):
        for j, (card_id, mode, action, next_pub) in enumerate(candidate_rows[i]):
            if next_pub is None:
                continue
            next_hand = frozenset(req.hand) - {card_id}
            inf, crd, scl = _extract_features(next_pub, next_hand, req.holds_china, req.side)
            inf = _normalize_influence_features(inf, expected_influence_dim)
            eval_inf.append(inf)
            eval_cards.append(crd)
            eval_scalars.append(scl)
            eval_meta.append((i, j))

    # Values indexed by (request_idx, candidate_idx)
    value_map: dict[tuple[int, int], float] = {}
    if eval_inf:
        with torch.no_grad():
            out = model(torch.cat(eval_inf), torch.cat(eval_cards), torch.cat(eval_scalars))
            vals = out["value"].squeeze(-1).tolist()
        for (ri, ci), v in zip(eval_meta, vals):
            value_map[(ri, ci)] = float(v)

    # ── Pick best candidate per request ──────────────────────────────────────
    actions = []
    for i, req in enumerate(requests):
        candidates = candidate_rows[i]
        if not candidates:
            # Full fallback
            from tsrl.engine.legal_actions import sample_action
            actions.append(sample_action(
                frozenset(req.hand), req.pub, req.side,
                holds_china=req.holds_china, rng=rng))
            continue

        # Score: value if lookahead available, else 0 (use first candidate as tiebreak)
        best_idx = max(
            range(len(candidates)),
            key=lambda j: value_map.get((i, j), 0.0),
        )
        actions.append(candidates[best_idx][2])

    return actions


def _infer_batch(
    requests,
    model,
    has_strategy_heads: bool,
    expected_influence_dim: int,
    rng: RNG,
):
    """Run batched model inference on a list of DecisionRequests → list of ActionEncodings."""
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency
    from tsrl.schemas import ActionEncoding, ActionMode

    adj = load_adjacency()
    n = len(requests)

    # Extract features for each request
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
    mode_logits_batch = outputs.get("mode_logits")
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
            # Fallback: sample randomly
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

        # Use mode_logits if available; otherwise fall back to random choice.
        if mode_logits_batch is not None:
            ml = mode_logits_batch[i]
            mode_mask = torch.full_like(ml, float("-inf"))
            for m in modes:
                mode_mask[int(m)] = 0.0
            mode = ActionMode(int((ml + mode_mask).argmax().item()))
        else:
            mode = rng.choice(modes)

        # DEFCON safety: never coup at DEFCON 2 (drops to 1 = phasing player loses).
        if mode == ActionMode.COUP and pub.defcon <= 2:
            safe = [m for m in modes if m != ActionMode.COUP]
            if not safe:
                from tsrl.engine.legal_actions import sample_action
                action = sample_action(hand_set, pub, side, holds_china=req.holds_china, rng=rng)
                actions.append(action)
                continue
            if mode_logits_batch is not None:
                ml = mode_logits_batch[i]
                safe_mask = torch.full_like(ml, float("-inf"))
                for m in safe:
                    safe_mask[int(m)] = 0.0
                mode = ActionMode(int((ml + safe_mask).argmax().item()))
            else:
                mode = rng.choice(safe)

        # DEFCON safety: never play EVENT for DEFCON-lowering cards at DEFCON ≤ 2.
        if mode == ActionMode.EVENT and pub.defcon <= 2:
            from tsrl.policies.minimal_hybrid import _DEFCON_LOWERING_CARDS
            if sampled_card_id in _DEFCON_LOWERING_CARDS:
                safe = [m for m in modes if m != ActionMode.EVENT]
                if safe:
                    if mode_logits_batch is not None:
                        ml = mode_logits_batch[i]
                        safe_mask = torch.full_like(ml, float("-inf"))
                        for m in safe:
                            safe_mask[int(m)] = 0.0
                        mode = ActionMode(int((ml + safe_mask).argmax().item()))
                    else:
                        mode = rng.choice(safe)

        if mode in (ActionMode.SPACE, ActionMode.EVENT):
            actions.append(ActionEncoding(card_id=sampled_card_id, mode=mode, targets=()))
            continue

        country_logits = country_logits_batch[i] if country_logits_batch is not None else None
        strategy_logits = strategy_logits_batch[i] if strategy_logits_batch is not None else None
        cs_logits = country_strategy_logits_batch[i] if country_strategy_logits_batch is not None else None

        if has_strategy_heads and country_logits is not None:
            action = _build_action_from_country_logits(
                sampled_card_id, mode, country_logits, pub, side, adj, rng,
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


# ---------------------------------------------------------------------------
# Worker process
# ---------------------------------------------------------------------------

def _worker_fn(args: dict[str, Any]) -> dict[str, Any]:
    """Run a slice of games in a single process. Returns summary dict."""
    try:
        os.nice(10)
    except OSError:
        pass

    worker_id: int = args["worker_id"]
    seed_base: int = args["seed_base"]
    game_indices: list[int] = args["game_indices"]  # global game indices for this worker
    checkpoint: str = args["checkpoint"]
    out_path_str: str = args["out_path"]

    # Set up worker logging
    logging.basicConfig(
        level=logging.INFO,
        format=f"%(asctime)s %(levelname)s worker{worker_id}: %(message)s",
    )
    wlog = logging.getLogger(f"worker{worker_id}")

    from tsrl.engine.game_state import reset
    from tsrl.engine.vec_runner import run_games_vectorized
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid
    from tsrl.schemas import Side
    from tsrl.selfplay.collector import _GAME_RESULT_STR, _step_to_row

    model, has_strategy_heads, expected_influence_dim = _load_model(checkpoint)
    model.eval()

    rng = make_rng(seed_base ^ (worker_id * 1_000_003 + 7))

    n_local = len(game_indices)
    game_counter = [0]

    def make_game_fn():
        global_idx = game_indices[game_counter[0]]
        gs = reset(seed=seed_base + global_idx)
        game_counter[0] += 1
        return gs

    def learned_side_fn(local_game_idx: int) -> Side:
        global_idx = game_indices[local_game_idx]
        return Side.USSR if global_idx % 2 == 0 else Side.US

    value_guided: bool = args.get("value_guided", False)
    value_guided_k: int = args.get("value_guided_k", 4)

    def learned_infer_fn(requests, game_states):  # game_states passed by vec_runner (unused here)
        if value_guided:
            return _infer_batch_value_guided(
                requests, model, has_strategy_heads, expected_influence_dim, rng,
                top_k=value_guided_k)
        return _infer_batch(requests, model, has_strategy_heads, expected_influence_dim, rng)

    def heuristic_fn(req):
        action = choose_minimal_hybrid(req.pub, req.hand, req.holds_china)
        if action is None:
            from tsrl.engine.legal_actions import sample_action
            action = sample_action(
                frozenset(req.hand), req.pub, req.side,
                holds_china=req.holds_china, rng=rng,
            )
        return action

    all_rows: list[dict] = []
    completed = [0]

    def on_game_done(local_game_idx, steps, result):
        global_idx = game_indices[local_game_idx]
        game_id = f"learned_vs_heuristic_{seed_base + global_idx}"
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
            game_id, len(rows),
            _GAME_RESULT_STR[result.winner],
            result.final_vp, result.end_turn,
            completed[0], n_local,
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

    # Write partial parquet
    out_path = Path(out_path_str)
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collect learned-vs-heuristic games with multiprocessing.",
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
        default=8,
        help="Number of worker processes (default: 8)",
    )
    # Keep --pool-size as alias for backwards compat with pipeline scripts,
    # but it now maps to --workers (pool-size → workers, rounded to reasonable value).
    parser.add_argument(
        "--pool-size",
        type=int,
        default=None,
        dest="pool_size",
        help="[deprecated] Use --workers instead. If provided, workers=min(pool_size, 16).",
    )
    parser.add_argument(
        "--value-guided",
        action="store_true",
        help="Use 1-ply value-guided action selection (evaluate top-k cards with value head).",
    )
    parser.add_argument(
        "--value-guided-k",
        type=int,
        default=4,
        help="Number of candidate cards to evaluate per decision (default: 4).",
    )
    args = parser.parse_args(argv)

    if args.n_games <= 0:
        raise ValueError("--n-games must be > 0")

    n_workers = args.workers
    if args.pool_size is not None:
        # Legacy: pool_size was thread count (256), map to a sane process count
        n_workers = min(args.pool_size, 16)
        log.info("--pool-size %d → --workers %d", args.pool_size, n_workers)

    n_workers = min(n_workers, args.n_games)

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
        "Collecting %d learned-vs-heuristic games  |  workers=%d  |  checkpoint=%s"
        "  |  seed=%d  ->  %s",
        args.n_games, n_workers, args.checkpoint, args.seed, out_path,
    )

    # Partition game indices across workers
    all_indices = list(range(args.n_games))
    chunks = [[] for _ in range(n_workers)]
    for i, idx in enumerate(all_indices):
        chunks[i % n_workers].append(idx)

    worker_args = []
    part_paths = []
    for wid, chunk in enumerate(chunks):
        if not chunk:
            continue
        part_path = str(out_path) + f".part_{wid:04d}.parquet"
        part_paths.append(part_path)
        worker_args.append({
            "worker_id": wid,
            "seed_base": args.seed,
            "game_indices": chunk,
            "checkpoint": args.checkpoint,
            "out_path": part_path,
            "value_guided": getattr(args, "value_guided", False),
            "value_guided_k": getattr(args, "value_guided_k", 4),
        })

    ctx = multiprocessing.get_context("spawn")
    total_rows = 0
    produced_parts = []

    with ctx.Pool(processes=n_workers) as pool:
        for result in pool.imap_unordered(_worker_fn, worker_args):
            wid = result["worker_id"]
            log.info(
                "Worker %d done: %d games, %d rows",
                wid, result["games"], result["rows"],
            )
            total_rows += result["rows"]
            if result["out_path"]:
                produced_parts.append(result["out_path"])

    if not produced_parts:
        log.error("No rows collected; check worker errors above.")
        return 1

    # Merge all parts into final output
    import polars as pl
    pl.concat(
        [pl.scan_parquet(p) for p in produced_parts], how="vertical"
    ).sink_parquet(str(out_path))

    if out_path.exists() and out_path.stat().st_size > 0:
        for p in produced_parts:
            try:
                Path(p).unlink()
            except OSError:
                pass
        log.info(
            "Done. %d rows total from %d games. -> %s",
            total_rows, args.n_games, out_path,
        )
        return 0

    log.error(
        "Merge output missing or empty; part files kept: %s",
        produced_parts,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
