"""Benchmark value-function MCTS against baselines.

Usage:
    uv run python scripts/benchmark_vf_mcts.py \\
        --checkpoint data/checkpoints/baseline_epoch20.pt \\
        --n-games 20 \\
        --n-sim 5

Compares:
  1. learned policy (no MCTS) vs heuristic  ← only signal that matters
  2. vf_mcts vs random    (only when --n-sim > 0)
  3. vf_mcts vs heuristic (only when --n-sim > 0)
"""
from __future__ import annotations

import argparse
import math
import multiprocessing
import os
import sys
import time
from dataclasses import dataclass
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

import numpy as np
import torch

from tsrl.engine.rng import RNG, make_rng
from tsrl.engine.game_loop import GameResult, Policy, make_random_policy, play_game
from tsrl.engine.game_state import GameState, reset
from tsrl.engine.mcts import interleaved_uct_mcts
from tsrl.engine.vec_runner import run_games_vectorized
from tsrl.policies.learned_policy import (
    _build_action_from_country_logits,
    _build_random_targets,
    _extract_features,
    make_learned_policy,
)
from tsrl.policies.model import (
    TSBaselineModel,
    TSCardEmbedModel,
    TSControlFeatGNNModel,
    TSControlFeatGNNSideModel,
    TSControlFeatModel,
    TSCountryEmbedModel,
    TSFullEmbedModel,
    TSCountryAttnModel,
)

_BENCH_MODEL_REGISTRY = {
    "baseline": TSBaselineModel,
    "card_embed": TSCardEmbedModel,
    "country_embed": TSCountryEmbedModel,
    "full_embed": TSFullEmbedModel,
    "country_attn": TSCountryAttnModel,
    "control_feat": TSControlFeatModel,
    "control_feat_gnn": TSControlFeatGNNModel,
    "control_feat_gnn_side": TSControlFeatGNNSideModel,
}
from tsrl.policies.minimal_hybrid import _DEFCON_LOWERING_CARDS, make_minimal_hybrid_policy
from tsrl.schemas import ActionEncoding, ActionMode, Side


@dataclass
class BenchmarkResult:
    """Result of a matchup: policy_a vs policy_b.

    policy_a_wins / policy_b_wins track wins by the policy (not by side).
    Games alternate: even games policy_a plays USSR, odd games policy_a plays US.
    """

    name: str  # "vf_mcts5 vs random", etc.
    games: int
    policy_a_wins: int
    policy_b_wins: int
    draws: int
    avg_wall_time_per_move: float  # seconds

    @property
    def a_winrate(self) -> float:
        return self.policy_a_wins / max(1, self.games - self.draws)

    @property
    def b_winrate(self) -> float:
        return self.policy_b_wins / max(1, self.games - self.draws)

    @property
    def draw_rate(self) -> float:
        return self.draws / max(1, self.games)

    def __str__(self) -> str:
        decisive = self.games - self.draws
        a_name, b_name = self.name.split(" vs ", 1) if " vs " in self.name else ("A", "B")
        return (
            f"{self.name:35s} "
            f"  {a_name[:12]:12s} {self.policy_a_wins:3d}/{decisive:3d} ({100*self.a_winrate:5.1f}%)  "
            f"{b_name[:12]:12s} {self.policy_b_wins:3d}/{decisive:3d} ({100*self.b_winrate:5.1f}%)  "
            f"Draw {self.draws:2d}/{self.games}  "
            f"Time {self.avg_wall_time_per_move*1000:.1f}ms/move"
        )


def _load_model(checkpoint_path: str):
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(checkpoint_path)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model_type = ckpt_args.get("model_type", "baseline")
    model_cls = _BENCH_MODEL_REGISTRY.get(model_type, TSBaselineModel)
    model = model_cls(hidden_dim=hidden_dim)
    model.load_state_dict(state_dict, strict=False)
    # Resolve influence encoder input dim: flat encoders use .in_features;
    # embedding encoders expose it differently.
    inf_enc = getattr(model, "influence_encoder", None) or getattr(model, "influence_encoder_flat", None)
    expected_influence_dim = inf_enc.in_features if inf_enc is not None else 172
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
    try:
        model = torch.compile(model, dynamic=True)
    except Exception:
        pass
    return model, has_strategy_heads, expected_influence_dim


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


def _make_value_fns(
    model,
    expected_influence_dim: int,
):
    device = next(model.parameters()).device

    def _value_fn(gs) -> float:
        pub = gs.pub
        side = pub.phasing
        holds_china = (side == Side.USSR and gs.ussr_holds_china) or (
            side == Side.US and gs.us_holds_china
        )
        hand = gs.hands[side]
        influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
        influence = _normalize_influence_features(
            influence.to(device=device),
            expected_influence_dim,
        )
        cards = cards.to(device=device)
        scalars = scalars.to(device=device)
        with torch.no_grad():
            outputs = model(influence, cards, scalars)
        return outputs["value"][0, 0].item()

    def _batch_value_fn(states) -> list[float]:
        influence_list = []
        cards_list = []
        scalars_list = []
        for gs in states:
            pub = gs.pub
            side = pub.phasing
            holds_china = (side == Side.USSR and gs.ussr_holds_china) or (
                side == Side.US and gs.us_holds_china
            )
            hand = gs.hands[side]
            influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
            influence_list.append(
                _normalize_influence_features(influence.to(device=device), expected_influence_dim)
            )
            cards_list.append(cards.to(device=device))
            scalars_list.append(scalars.to(device=device))

        influence_batch = torch.cat(influence_list, dim=0)
        cards_batch = torch.cat(cards_list, dim=0)
        scalars_batch = torch.cat(scalars_list, dim=0)
        with torch.no_grad():
            outputs = model(influence_batch, cards_batch, scalars_batch)
        return outputs["value"][:, 0].tolist()

    return _value_fn, _batch_value_fn


def _make_candidate_fn(
    model,
    expected_influence_dim: int,
    *,
    n_candidates: int,
    has_strategy_heads: bool,
):
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency

    adj = load_adjacency()
    device = next(model.parameters()).device

    def _candidate_fn(
        gs,
        side: Side,
        holds_china: bool,
        n: int,
        *,
        rng: RNG | None = None,
    ) -> list[ActionEncoding]:
        hand = gs.hands[side]
        pub = gs.pub
        playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china))
        if not playable:
            return []

        influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
        influence = _normalize_influence_features(
            influence.to(device=device),
            expected_influence_dim,
        )
        cards = cards.to(device=device)
        scalars = scalars.to(device=device)
        with torch.no_grad():
            outputs = model(influence, cards, scalars)
        card_logits = outputs["card_logits"][0]
        mode_logits = outputs["mode_logits"][0]
        country_logits = outputs.get("country_logits")
        if country_logits is not None:
            country_logits = country_logits[0]
        strategy_logits = outputs.get("strategy_logits")
        if strategy_logits is not None:
            strategy_logits = strategy_logits[0]
        country_strategy_logits = outputs.get("country_strategy_logits")
        if country_strategy_logits is not None:
            country_strategy_logits = country_strategy_logits[0]

        card_probs = torch.softmax(card_logits, dim=0)
        mode_probs = torch.softmax(mode_logits, dim=0)

        scored_pairs: list[tuple[int, ActionMode, float]] = []
        for card_id in playable:
            card_score = float(card_probs[card_id - 1].item())
            modes = sorted(legal_modes(card_id, pub, side, adj=adj), key=int)
            for mode in modes:
                scored_pairs.append((card_id, mode, card_score * float(mode_probs[int(mode)].item())))

        if not scored_pairs:
            return []

        limit = min(n, n_candidates, len(scored_pairs))
        if limit <= 0:
            return []

        scored_pairs.sort(key=lambda item: (-item[2], item[0], int(item[1])))
        selected_pairs = [(card_id, mode) for card_id, mode, _ in scored_pairs[:limit]]

        _rng = rng or make_rng()
        actions: list[ActionEncoding] = []
        for card_id, mode in selected_pairs:
            if mode in (ActionMode.SPACE, ActionMode.EVENT):
                actions.append(ActionEncoding(card_id=card_id, mode=mode, targets=()))
                continue

            action = None
            if has_strategy_heads and country_logits is not None:
                action = _build_action_from_country_logits(
                    card_id,
                    mode,
                    country_logits,
                    pub,
                    side,
                    adj,
                    _rng,
                    strategy_logits=strategy_logits,
                    country_strategy_logits=country_strategy_logits,
                )
            if action is None:
                action = _build_random_targets(card_id, mode, pub, side, adj, _rng)
            if action is not None:
                actions.append(action)
        return actions

    return _candidate_fn


def _build_policy(kind: str, seed: int) -> Policy:
    if kind == "random":
        return make_random_policy(make_rng(seed))
    if kind == "heuristic":
        return make_minimal_hybrid_policy()
    raise ValueError(f"unsupported policy kind for multiprocessing benchmark: {kind}")


def _opponent_policy_kind(name: str) -> str:
    lower_name = name.lower()
    if lower_name.endswith("vs random"):
        return "random"
    if lower_name.endswith("vs heuristic"):
        return "heuristic"
    raise ValueError(f"unsupported vf benchmark matchup: {name}")


def play_game_with_vf_uct(
    value_fn,
    n_sim: int,
    seed: int,
    *,
    vf_side: Side,
    opponent_policy: Policy,
    batch_value_fn=None,
    candidate_fn=None,
) -> GameResult:
    """Play one game with value-function UCT on one side over the live GameState."""
    from tsrl.engine.game_loop import (
        _MID_WAR_TURN,
        _LATE_WAR_TURN,
        _MAX_TURNS,
        _end_of_turn,
        _run_action_rounds,
        _run_extra_ar,
        _run_headline_phase,
    )
    from tsrl.engine.game_state import (
        _ars_for_turn,
        advance_to_late_war,
        advance_to_mid_war,
        clone_game_state,
        deal_cards,
        reset,
    )
    from tsrl.engine.legal_actions import sample_action

    rng = make_rng(seed)
    gs = reset(seed=int(rng.integers(0, 2**32)))

    def _vf_policy(pub, hand, holds_china):
        side = pub.phasing
        if side != vf_side:
            return opponent_policy(pub, hand, holds_china)

        gs_snap = clone_game_state(gs)
        gs_snap.hands[side] = hand
        action = uct_mcts(
            gs_snap, n_sim,
            value_fn=value_fn,
            batch_value_fn=batch_value_fn,
            candidate_fn=candidate_fn,
            rng=rng,
        )
        if action is None:
            action = sample_action(hand, pub, side, holds_china=holds_china, rng=rng)
        return action

    result: Optional[GameResult] = None
    for turn in range(1, _MAX_TURNS + 1):
        gs.pub.turn = turn
        if turn == _MID_WAR_TURN:
            advance_to_mid_war(gs, rng)
        elif turn == _LATE_WAR_TURN:
            advance_to_late_war(gs, rng)

        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)

        result = _run_headline_phase(gs, _vf_policy, _vf_policy, rng)
        if result is not None:
            break

        result = _run_action_rounds(gs, _vf_policy, _vf_policy, rng, _ars_for_turn(turn))
        if result is not None:
            break

        if gs.pub.north_sea_oil_extra_ar:
            gs.pub.north_sea_oil_extra_ar = False
            result = _run_extra_ar(gs, Side.US, _vf_policy, rng)
            if result is not None:
                break

        if gs.pub.glasnost_extra_ar:
            gs.pub.glasnost_extra_ar = False
            result = _run_extra_ar(gs, Side.USSR, _vf_policy, rng)
            if result is not None:
                break

        result = _end_of_turn(gs, rng, turn)
        if result is not None:
            break

    if result is None:
        winner: Optional[Side] = None
        if gs.pub.vp > 0:
            winner = Side.USSR
        elif gs.pub.vp < 0:
            winner = Side.US
        result = GameResult(winner, gs.pub.vp, _MAX_TURNS, "turn_limit")

    return result


def _benchmark_worker(worker_args: tuple) -> list[tuple[int, GameResult, float]]:
    checkpoint_path, game_indices, seed_base, name, n_sim, n_candidates = worker_args
    model, has_strategy_heads, expected_influence_dim = _load_model(checkpoint_path)
    model.eval()
    value_fn, batch_value_fn = _make_value_fns(model, expected_influence_dim)
    candidate_fn = None
    if n_candidates > 0:
        candidate_fn = _make_candidate_fn(
            model,
            expected_influence_dim,
            n_candidates=n_candidates,
            has_strategy_heads=has_strategy_heads,
        )

    opponent_kind = _opponent_policy_kind(name)
    results: list[tuple[int, GameResult, float]] = []
    for game_idx in game_indices:
        a_is_ussr = (game_idx % 2 == 0)
        vf_side = Side.USSR if a_is_ussr else Side.US
        opponent_policy = _build_policy(opponent_kind, seed_base + game_idx)

        t0 = time.time()
        result = play_game_with_vf_uct(
            value_fn,
            n_sim,
            seed_base + game_idx,
            vf_side=vf_side,
            opponent_policy=opponent_policy,
            batch_value_fn=batch_value_fn,
            candidate_fn=candidate_fn,
        )
        results.append((game_idx, result, time.time() - t0))

    return results


def _run_learned_games_vectorized(
    name: str,
    model,
    expected_influence_dim: int,
    has_strategy_heads: bool,
    opponent_kind: str,
    n_games: int,
    seed: int,
    n_candidates: int,
    n_sim: int = 0,
) -> list[tuple[int, GameResult]]:
    """Run n_games with batched learned-policy inference using vec_runner.

    All games run concurrently in one process. At each tick, all games that
    need a learned-policy decision are batched into a single forward pass.
    The opponent (random/heuristic) is stepped cheaply in the same loop.
    """
    rng_main = make_rng(seed)
    game_seeds = [int(rng_main.integers(0, 2**32)) for _ in range(n_games)]
    live_game_states = []
    device = next(model.parameters()).device

    game_counter = [0]

    def make_game_fn_ordered():
        gs = reset(seed=game_seeds[game_counter[0]])
        game_counter[0] += 1
        live_game_states.append(gs)
        return gs

    def learned_side_fn(game_idx: int) -> Side:
        return Side.USSR if (game_idx % 2 == 0) else Side.US

    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency
    from tsrl.engine.mcts import _holds_china as _mcts_holds_china
    adj = load_adjacency()

    # ── Shared batch inference helper ─────────────────────────────────────────
    def _batch_forward(reqs_or_states):
        """Run one model forward pass over a list of requests or GameStates."""
        inf_list, crd_list, scl_list = [], [], []
        for item in reqs_or_states:
            if isinstance(item, GameState):
                side = item.pub.phasing
                holds_c = _mcts_holds_china(item, side)
                inf, crd, scl = _extract_features(item.pub, item.hands[side], holds_c, side)
            else:
                inf, crd, scl = _extract_features(item.pub, item.hand, item.holds_china, item.side)
            inf = _normalize_influence_features(inf.to(device), expected_influence_dim)
            inf_list.append(inf)
            crd_list.append(crd.to(device))
            scl_list.append(scl.to(device))
        with torch.no_grad():
            return model(
                torch.cat(inf_list),
                torch.cat(crd_list),
                torch.cat(scl_list),
            )

    # ── Value function for MCTS leaves ────────────────────────────────────────
    def batch_value_fn(game_states_leaf: list[GameState]) -> list[float]:
        if not game_states_leaf:
            return []
        out = _batch_forward(game_states_leaf)
        return out["value"].squeeze(-1).cpu().tolist()

    # ── Candidate function: model-guided top-k (card × mode) ─────────────────
    def model_candidate_fn(
        gs: GameState, side: Side, holds_china: bool, n: int, *, rng: RNG | None = None,
    ) -> list[ActionEncoding]:
        if n_candidates <= 0:
            from tsrl.engine.mcts import _sample_candidates
            return _sample_candidates(gs, side, holds_china, n, rng or make_rng())
        playable = sorted(legal_cards(gs.hands[side], gs.pub, side, holds_china=holds_china))
        if not playable:
            return []
        out = _batch_forward([gs])
        card_probs = torch.softmax(out["card_logits"][0], dim=0)
        mode_probs = torch.softmax(out["mode_logits"][0], dim=0)
        cl = out.get("country_logits")
        cl = cl[0] if cl is not None else None
        sl = out.get("strategy_logits")
        sl = sl[0] if sl is not None else None
        csl = out.get("country_strategy_logits")
        csl = csl[0] if csl is not None else None

        scored: list[tuple[int, ActionMode, float]] = []
        for card_id in playable:
            cs = float(card_probs[card_id - 1].item())
            for mode in sorted(legal_modes(card_id, gs.pub, side, adj=adj), key=int):
                # DEFCON safety: skip suicide actions from candidates
                if mode == ActionMode.COUP and gs.pub.defcon <= 2:
                    continue
                if mode == ActionMode.EVENT and gs.pub.defcon <= 2 and card_id in _DEFCON_LOWERING_CARDS:
                    continue
                scored.append((card_id, mode, cs * float(mode_probs[int(mode)].item())))

        if not scored:
            # All pairs were filtered — fall back to random sampling
            from tsrl.engine.mcts import _sample_candidates
            return _sample_candidates(gs, side, holds_china, n, rng or make_rng())

        scored.sort(key=lambda x: (-x[2], x[0], int(x[1])))
        _rng = rng or make_rng()
        actions: list[ActionEncoding] = []
        seen: set[ActionEncoding] = set()
        for card_id, mode, _ in scored[:max(1, n)]:
            if mode in (ActionMode.SPACE, ActionMode.EVENT):
                a = ActionEncoding(card_id=card_id, mode=mode, targets=())
            else:
                a = _build_action_from_country_logits(card_id, mode, cl, gs.pub, side, adj, _rng,
                                                       strategy_logits=sl,
                                                       country_strategy_logits=csl)
                if a is None:
                    a = _build_random_targets(card_id, mode, gs.pub, side, adj, _rng)
            if a is not None and a not in seen:
                seen.add(a)
                actions.append(a)
        return actions

    # ── Plain batched inference (no search) ───────────────────────────────────
    def plain_infer_fn(requests: list, game_states_arg: list[GameState]) -> list[ActionEncoding]:
        out = _batch_forward(requests)
        actions = []
        for i, req in enumerate(requests):
            card_logits = out["card_logits"][i].cpu()
            mode_logits = out["mode_logits"][i].cpu()
            cl = out.get("country_logits")
            cl_i = cl[i].cpu() if cl is not None else None
            _rng = make_rng(seed + i)

            legal_c = legal_cards(req.hand, req.pub, req.side, holds_china=req.holds_china)
            mask = torch.full((card_logits.shape[0],), float("-inf"))
            for cid in legal_c:
                if 1 <= cid <= card_logits.shape[0]:
                    mask[cid - 1] = 0.0
            card_id = int((card_logits + mask).argmax()) + 1

            legal_m = legal_modes(card_id, req.pub, req.side, adj=adj)
            mode_mask = torch.full((mode_logits.shape[0],), float("-inf"))
            for m in legal_m:
                mode_mask[int(m)] = 0.0
            mode = ActionMode((mode_logits + mode_mask).argmax().item())

            # DEFCON safety
            if mode == ActionMode.COUP and req.pub.defcon <= 2:
                safe = [m for m in legal_m if m != ActionMode.COUP]
                if safe:
                    sm = torch.full((mode_logits.shape[0],), float("-inf"))
                    for m in safe: sm[int(m)] = 0.0
                    mode = ActionMode((mode_logits + sm).argmax().item())
                else:
                    actions.append(ActionEncoding(card_id=card_id, mode=ActionMode.EVENT, targets=()))
                    continue
            if mode == ActionMode.EVENT and req.pub.defcon <= 2 and card_id in _DEFCON_LOWERING_CARDS:
                safe = [m for m in legal_m if m != ActionMode.EVENT]
                if safe:
                    sm = torch.full((mode_logits.shape[0],), float("-inf"))
                    for m in safe: sm[int(m)] = 0.0
                    mode = ActionMode((mode_logits + sm).argmax().item())

            if mode in (ActionMode.COUP, ActionMode.REALIGN, ActionMode.INFLUENCE):
                action = _build_action_from_country_logits(card_id, mode, cl_i, req.pub, req.side, adj, _rng)
            else:
                action = ActionEncoding(card_id=card_id, mode=mode, targets=())
            if action is None:
                action = _build_random_targets(card_id, mode, req.pub, req.side, adj, _rng)
            if action is None:
                action = ActionEncoding(card_id=card_id, mode=mode, targets=())
            actions.append(action)
        return actions

    # ── MCTS inference via interleaved_uct_mcts ───────────────────────────────
    def mcts_infer_fn(requests: list, game_states_arg: list[GameState]) -> list[ActionEncoding]:
        from tsrl.engine.legal_actions import sample_action
        mcts_rng = make_rng(seed)
        results = interleaved_uct_mcts(
            game_states_arg,
            n_sim,
            batch_value_fn,
            c=1.41,
            candidate_fn=model_candidate_fn,
            rng=mcts_rng,
        )
        # Fill in fallback for any None result (empty hand / no legal actions).
        actions = []
        for action, req in zip(results, requests):
            if action is None:
                action = sample_action(
                    req.hand, req.pub, req.side, holds_china=req.holds_china,
                    rng=make_rng(seed),
                )
            actions.append(action)
        return actions

    learned_infer_fn = mcts_infer_fn if n_sim > 0 else plain_infer_fn

    if opponent_kind == "random":
        rng_opp = make_rng(seed ^ 0xDEAD)
        def heuristic_fn(req):
            from tsrl.engine.legal_actions import sample_action
            return sample_action(req.hand, req.pub, req.side, holds_china=req.holds_china, rng=rng_opp)
    else:
        from tsrl.policies.minimal_hybrid import choose_minimal_hybrid
        from tsrl.engine.legal_actions import sample_action
        rng_fb = make_rng(seed ^ 0xBEEF)
        def heuristic_fn(req):
            action = choose_minimal_hybrid(req.pub, req.hand, req.holds_china)
            if action is None:
                action = sample_action(req.hand, req.pub, req.side, holds_china=req.holds_china, rng=rng_fb)
            return action

    game_results = run_games_vectorized(
        n_games=n_games,
        make_game_fn=make_game_fn_ordered,
        learned_side_fn=learned_side_fn,
        learned_infer_fn=learned_infer_fn,
        heuristic_fn=heuristic_fn,
        seed_base=seed,
    )
    return [(i, r) for i, r in enumerate(game_results)]


def run_matchup(
    name: str,
    policy_a: Policy,
    policy_b: Policy,
    n_games: int,
    seed: int,
    *,
    vf_value_fn=None,
    vf_n_sim: int = 0,
    vf_candidate_fn=None,
    pool_size: int = 32,
    learned_checkpoint: str | None = None,
) -> BenchmarkResult:
    """Play n_games between policy_a and policy_b, alternating sides.

    policy_a plays USSR on even games and US on odd games.
    Wins are tracked by policy (not side) so results are unbiased by TS's side asymmetry.
    """
    a_wins = b_wins = draws = 0
    total_time = 0.0
    move_count = 0

    if learned_checkpoint is not None:
        # Vectorized learned-policy games: all games run concurrently in one process,
        # learned-side requests are batched into a single GPU forward pass each tick.
        t0 = time.time()
        model, has_strategy_heads, expected_influence_dim = _load_model(learned_checkpoint)
        model.eval()
        opponent_kind = _opponent_policy_kind(name)
        n_cands = vf_candidate_fn if isinstance(vf_candidate_fn, int) else 0
        game_result_pairs = _run_learned_games_vectorized(
            name, model, expected_influence_dim, has_strategy_heads,
            opponent_kind, n_games, seed, n_cands, vf_n_sim,
        )
        for game_idx, result in game_result_pairs:
            a_side = Side.USSR if (game_idx % 2 == 0) else Side.US
            if result.winner is None:
                draws += 1
            elif result.winner == a_side:
                a_wins += 1
            else:
                b_wins += 1
            move_count += 100
            completed = game_idx + 1
            if completed % 5 == 0 or completed == 1:
                print(
                    f"  [{name}] game {completed}/{n_games}"
                    f"  a_wins={a_wins} b_wins={b_wins} draws={draws}"
                )
        total_time = time.time() - t0

    elif vf_value_fn is None:
        for game_idx in range(n_games):
            a_is_ussr = (game_idx % 2 == 0)
            if a_is_ussr:
                ussr_pol, us_pol = policy_a, policy_b
            else:
                ussr_pol, us_pol = policy_b, policy_a

            t0 = time.time()
            result = play_game(ussr_pol, us_pol, seed=seed + game_idx)
            t1 = time.time()
            total_time += t1 - t0

            a_side = Side.USSR if a_is_ussr else Side.US
            if result.winner is None:
                draws += 1
            elif result.winner == a_side:
                a_wins += 1
            else:
                b_wins += 1

            move_count += 100  # rough estimate

            if (game_idx + 1) % 5 == 0 or game_idx == 0:
                elapsed = t1 - t0
                print(
                    f"  [{name}] game {game_idx+1}/{n_games}"
                    f"  a_wins={a_wins} b_wins={b_wins} draws={draws}"
                    f"  game_time={elapsed:.1f}s"
                )
    else:
        worker_count = max(1, min(pool_size, n_games))
        chunks = [list(range(offset, n_games, worker_count)) for offset in range(worker_count)]
        worker_args = [
            (vf_value_fn, chunk, seed, name, vf_n_sim, vf_candidate_fn or 0)
            for chunk in chunks
            if chunk
        ]
        with multiprocessing.Pool(processes=worker_count) as pool:
            worker_results = pool.map(_benchmark_worker, worker_args)

        completed = 0
        for game_idx, result, elapsed in sorted(
            [item for batch in worker_results for item in batch],
            key=lambda item: item[0],
        ):
            completed += 1
            total_time += elapsed

            a_is_ussr = (game_idx % 2 == 0)
            a_side = Side.USSR if a_is_ussr else Side.US
            if result.winner is None:
                draws += 1
            elif result.winner == a_side:
                a_wins += 1
            else:
                b_wins += 1

            move_count += 100  # rough estimate

            if (completed % 5 == 0) or game_idx == 0:
                print(
                    f"  [{name}] game {completed}/{n_games}"
                    f"  a_wins={a_wins} b_wins={b_wins} draws={draws}"
                    f"  game_time={elapsed:.1f}s"
                )

    avg_time = total_time / max(1, move_count)
    return BenchmarkResult(
        name=name,
        games=n_games,
        policy_a_wins=a_wins,
        policy_b_wins=b_wins,
        draws=draws,
        avg_wall_time_per_move=avg_time,
    )


def main():
    import sys as _sys
    _sys.stdout.reconfigure(line_buffering=True)

    p = argparse.ArgumentParser(
        description="Benchmark value-function MCTS against baselines."
    )
    p.add_argument(
        "--checkpoint",
        required=True,
        help="Path to learned policy checkpoint (.pt)",
    )
    p.add_argument("--n-games", type=int, default=20, help="Games per matchup")
    p.add_argument("--n-sim", type=int, default=5, help="MCTS simulations per move")
    p.add_argument("--seed", type=int, default=42, help="RNG seed")
    p.add_argument(
        "--pool-size", type=int, default=32,
        help="Concurrent game threads / inference slots (default: 32)"
    )
    p.add_argument(
        "--n-candidates", type=int, default=0,
        help="If >0, use model candidate fn with this many candidates (model-guided MCTS)"
    )
    args = p.parse_args()

    if not os.path.exists(args.checkpoint):
        print(f"ERROR: checkpoint not found: {args.checkpoint}")
        sys.exit(1)

    print(f"Loading checkpoint: {args.checkpoint}")
    print(f"Games per matchup: {args.n_games}")
    print(f"MCTS simulations: {args.n_sim}\n")

    # Make policies
    random_pol = make_random_policy(make_rng(args.seed))
    heuristic_pol = make_minimal_hybrid_policy()

    try:
        _load_model(args.checkpoint)
        value_fn = args.checkpoint
        print(f"✓ Value function loaded")
    except Exception as e:
        print(f"ERROR loading value function: {e}")
        sys.exit(1)

    candidate_fn = None
    if args.n_candidates > 0:
        try:
            candidate_fn = args.n_candidates
            print(f"✓ Model candidate fn loaded (n_candidates={args.n_candidates})")
        except Exception as e:
            print(f"ERROR loading candidate fn: {e}")
            sys.exit(1)
    print()

    # Run benchmarks
    print("=" * 120)
    print(f"BENCHMARK RESULTS (n_games={args.n_games}, n_sim={args.n_sim})")
    print("=" * 120)

    results = []

    # 1. learned policy (no MCTS) vs heuristic — only signal that matters
    n_sim = args.n_sim
    tag = f"vf_mcts{n_sim}"
    if candidate_fn is not None:
        print(f"\n1. learned_policy vs heuristic")
        r = run_matchup(
            "learned vs heuristic",
            make_learned_policy(args.checkpoint, Side.USSR),
            heuristic_pol,
            args.n_games,
            args.seed + 400,
            learned_checkpoint=args.checkpoint,
            pool_size=args.pool_size,
        )
        results.append(r)
        print(f"   {r}")

    # 3. vf_mcts vs random  (skipped when n_sim=0)
    if n_sim > 0:
        print(f"\n3. {tag} vs random")
        r = run_matchup(
            f"{tag} vs random",
            random_pol,
            random_pol,
            args.n_games,
            args.seed + 200,
            vf_value_fn=value_fn,
            vf_n_sim=n_sim,
            vf_candidate_fn=candidate_fn,
            pool_size=args.pool_size,
            learned_checkpoint=args.checkpoint,
        )
        results.append(r)
        print(f"   {r}")

        # 4. vf_mcts vs heuristic
        print(f"\n4. {tag} vs heuristic")
        r = run_matchup(
            f"{tag} vs heuristic",
            heuristic_pol,
            heuristic_pol,
            args.n_games,
            args.seed + 300,
            vf_value_fn=value_fn,
            vf_n_sim=n_sim,
            vf_candidate_fn=candidate_fn,
            pool_size=args.pool_size,
            learned_checkpoint=args.checkpoint,
        )
        results.append(r)
        print(f"   {r}")


if __name__ == "__main__":
    main()
