"""Benchmark heuristic-rollout MCTS vs plain learned policy (no search).

Hypothesis: using the heuristic policy as a rollout function in MCTS bypasses
the miscalibrated value head and gives unbiased position estimates, potentially
improving win rate vs heuristic above the plain-learned BC ceiling (~15%).

Usage:
    uv run python scripts/bench_rollout_heuristic.py \\
        --checkpoint data/checkpoints/retrain_v47/baseline_best.pt \\
        --n-games 100 --n-sim 5 --seed 42

Compares:
  1. rollout_mcts (heuristic rollout, n_sim sims) vs heuristic
  2. learned (no MCTS, n_sim=0) vs heuristic  -- baseline for comparison

No value_fn is passed to uct_mcts; leaf evaluation is done via heuristic rollout.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

import torch

from tsrl.engine.rng import RNG, make_rng
from tsrl.engine.game_loop import GameResult, Policy, play_game
from tsrl.engine.game_state import GameState, reset, clone_game_state
from tsrl.engine.mcts import uct_mcts
from tsrl.policies.learned_policy import (
    _build_action_from_country_logits,
    _build_random_targets,
    _extract_features,
    make_learned_policy,  # takes (checkpoint_path, side)
)
from tsrl.policies.model import (
    TSBaselineModel,
    TSCardEmbedModel,
    TSCountryEmbedModel,
    TSFullEmbedModel,
    TSCountryAttnModel,
)
from tsrl.policies.minimal_hybrid import make_minimal_hybrid_policy
from tsrl.schemas import ActionEncoding, ActionMode, Side

_MODEL_REGISTRY = {
    "baseline": TSBaselineModel,
    "card_embed": TSCardEmbedModel,
    "country_embed": TSCountryEmbedModel,
    "full_embed": TSFullEmbedModel,
    "country_attn": TSCountryAttnModel,
}


# ---------------------------------------------------------------------------
# Checkpoint search order
# ---------------------------------------------------------------------------

_FALLBACK_VERSIONS = [47, 46, 45, 44]


def _find_checkpoint(path: str) -> str:
    """Return path if it exists, else try retrain_vN fallbacks."""
    if os.path.exists(path):
        return path
    for v in _FALLBACK_VERSIONS:
        candidate = f"data/checkpoints/retrain_v{v}/baseline_best.pt"
        if os.path.exists(candidate):
            print(f"[warn] {path} not found; falling back to {candidate}")
            return candidate
    raise FileNotFoundError(
        f"Could not find checkpoint at {path} or any fallback v{_FALLBACK_VERSIONS}"
    )


# ---------------------------------------------------------------------------
# Model loading (mirrors benchmark_vf_mcts.py)
# ---------------------------------------------------------------------------

def _load_model(checkpoint_path: str):
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    ckpt_args = checkpoint.get("args", {})
    hidden_dim = ckpt_args.get("hidden_dim", 256)
    model_type = ckpt_args.get("model_type", "baseline")
    model_cls = _MODEL_REGISTRY.get(model_type, TSBaselineModel)
    model = model_cls(hidden_dim=hidden_dim)
    model.load_state_dict(state_dict, strict=False)
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


def _normalize_influence_features(influence: torch.Tensor, expected_dim: int) -> torch.Tensor:
    actual_dim = int(influence.shape[1])
    if actual_dim == expected_dim:
        return influence
    if actual_dim == expected_dim + 2 and expected_dim % 2 == 0:
        half = actual_dim // 2
        return torch.cat([influence[:, 1:half], influence[:, half + 1:]], dim=1)
    if actual_dim > expected_dim:
        return influence[:, :expected_dim]
    pad = torch.zeros(
        (influence.shape[0], expected_dim - actual_dim),
        dtype=influence.dtype,
        device=influence.device,
    )
    return torch.cat([influence, pad], dim=1)


# ---------------------------------------------------------------------------
# Candidate function (top-n by model, restricts branching factor)
# ---------------------------------------------------------------------------

def _make_candidate_fn(model, expected_influence_dim: int, *, n_candidates: int, has_strategy_heads: bool):
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency

    adj = load_adjacency()
    device = next(model.parameters()).device

    def _candidate_fn(gs, side: Side, holds_china: bool, n: int, *, rng: RNG | None = None):
        hand = gs.hands[side]
        pub = gs.pub
        playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china))
        if not playable:
            return []

        influence, cards, scalars = _extract_features(pub, hand, holds_china, side)
        influence = _normalize_influence_features(influence.to(device=device), expected_influence_dim)
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
                    card_id, mode, country_logits, pub, side, adj, _rng,
                    strategy_logits=strategy_logits,
                    country_strategy_logits=country_strategy_logits,
                )
            if action is None:
                action = _build_random_targets(card_id, mode, pub, side, adj, _rng)
            if action is not None:
                actions.append(action)
        return actions

    return _candidate_fn


# ---------------------------------------------------------------------------
# Game runner: rollout MCTS on one side, opponent on the other
# ---------------------------------------------------------------------------

def play_game_with_rollout_mcts(
    rollout_policy: Policy,
    n_sim: int,
    seed: int,
    *,
    mcts_side: Side,
    opponent_policy: Policy,
    candidate_fn=None,
    c: float = 1.41,
) -> GameResult:
    """Play one game with heuristic-rollout UCT on mcts_side."""
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
        deal_cards,
        reset,
    )
    from tsrl.engine.legal_actions import sample_action

    rng = make_rng(seed)
    gs = reset(seed=int(rng.integers(0, 2**32)))

    def _mcts_policy(pub, hand, holds_china):
        side = pub.phasing
        if side != mcts_side:
            return opponent_policy(pub, hand, holds_china)

        gs_snap = clone_game_state(gs)
        gs_snap.hands[side] = hand
        # Key: pass rollout_policy, omit value_fn and batch_value_fn
        action = uct_mcts(
            gs_snap, n_sim,
            c=c,
            rollout_policy=rollout_policy,
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

        result = _run_headline_phase(gs, _mcts_policy, _mcts_policy, rng)
        if result is not None:
            break

        result = _run_action_rounds(gs, _mcts_policy, _mcts_policy, rng, _ars_for_turn(turn))
        if result is not None:
            break

        if gs.pub.north_sea_oil_extra_ar:
            gs.pub.north_sea_oil_extra_ar = False
            result = _run_extra_ar(gs, Side.US, _mcts_policy, rng)
            if result is not None:
                break

        if gs.pub.glasnost_extra_ar:
            gs.pub.glasnost_extra_ar = False
            result = _run_extra_ar(gs, Side.USSR, _mcts_policy, rng)
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
        from tsrl.engine.game_loop import _MAX_TURNS as _MT
        result = GameResult(winner, gs.pub.vp, _MT, "turn_limit")

    return result


# ---------------------------------------------------------------------------
# Main benchmark loop
# ---------------------------------------------------------------------------

def run_matchup(
    name: str,
    n_games: int,
    game_fn,
    seed_base: int,
) -> dict:
    """Run n_games, alternating sides. Return win/loss/draw counts."""
    wins = 0
    losses = 0
    draws = 0
    move_times: list[float] = []

    for i in range(n_games):
        # Even games: learned plays USSR; odd games: learned plays US
        mcts_side = Side.USSR if i % 2 == 0 else Side.US
        seed = seed_base + i

        t0 = time.monotonic()
        result = game_fn(seed=seed, mcts_side=mcts_side)
        elapsed = time.monotonic() - t0
        move_times.append(elapsed)

        if result.winner is None:
            draws += 1
        elif result.winner == mcts_side:
            wins += 1
        else:
            losses += 1

        if (i + 1) % 10 == 0 or i == n_games - 1:
            decisive = wins + losses
            wr = wins / decisive if decisive > 0 else 0.0
            print(
                f"  [{name}] game {i+1:3d}/{n_games}  "
                f"W{wins} L{losses} D{draws}  "
                f"win%={100*wr:.1f}%  "
                f"game_time={elapsed:.1f}s"
            )

    decisive = wins + losses
    win_rate = wins / decisive if decisive > 0 else 0.0
    return {
        "name": name,
        "games": n_games,
        "wins": wins,
        "losses": losses,
        "draws": draws,
        "win_rate": win_rate,
        "avg_game_time": sum(move_times) / len(move_times) if move_times else 0.0,
    }


def main():
    parser = argparse.ArgumentParser(description="Benchmark heuristic-rollout MCTS")
    parser.add_argument(
        "--checkpoint",
        default="data/checkpoints/retrain_v47/baseline_best.pt",
        help="Path to model checkpoint",
    )
    parser.add_argument("--n-games", type=int, default=100, help="Games per matchup")
    parser.add_argument("--n-sim", type=int, default=5, help="MCTS simulations per move")
    parser.add_argument("--n-candidates", type=int, default=8, help="Max root children")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--c", type=float, default=1.41, help="UCB1 exploration constant")
    args = parser.parse_args()

    checkpoint_path = _find_checkpoint(args.checkpoint)
    print(f"Loading checkpoint: {checkpoint_path}")
    model, has_strategy_heads, expected_influence_dim = _load_model(checkpoint_path)
    print(f"  model loaded (expected_influence_dim={expected_influence_dim}, "
          f"has_strategy_heads={has_strategy_heads})")

    heuristic_pol = make_minimal_hybrid_policy()
    # make_learned_policy loads from path and is side-specific; create one per side.
    learned_pol_ussr = make_learned_policy(checkpoint_path, Side.USSR)
    learned_pol_us = make_learned_policy(checkpoint_path, Side.US)

    candidate_fn = _make_candidate_fn(
        model,
        expected_influence_dim,
        n_candidates=args.n_candidates,
        has_strategy_heads=has_strategy_heads,
    )

    print(f"\n=== Experiment: heuristic-rollout MCTS (n_sim={args.n_sim}) vs heuristic ===")
    print(f"  n_games={args.n_games}  n_candidates={args.n_candidates}  c={args.c}  seed={args.seed}")
    print()

    # --- Matchup 1: rollout MCTS vs heuristic ---
    print(f"[1/2] rollout_mcts(n_sim={args.n_sim}) vs heuristic:")

    def _rollout_game(seed, mcts_side):
        return play_game_with_rollout_mcts(
            rollout_policy=heuristic_pol,
            n_sim=args.n_sim,
            seed=seed,
            mcts_side=mcts_side,
            opponent_policy=heuristic_pol,
            candidate_fn=candidate_fn,
            c=args.c,
        )

    result_mcts = run_matchup(
        f"rollout_mcts(n={args.n_sim}) vs heuristic",
        args.n_games,
        _rollout_game,
        args.seed,
    )

    # --- Matchup 2: plain learned (n_sim=0) vs heuristic ---
    print(f"\n[2/2] learned(n_sim=0) vs heuristic  [baseline comparison]:")

    def _learned_game(seed, mcts_side):
        # Use play_game directly; learned plays mcts_side, heuristic plays the other
        rng = make_rng(seed)
        if mcts_side == Side.USSR:
            return play_game(learned_pol_ussr, heuristic_pol, rng=rng)
        else:
            return play_game(heuristic_pol, learned_pol_us, rng=rng)

    result_learned = run_matchup(
        "learned(n=0) vs heuristic",
        args.n_games,
        _learned_game,
        args.seed,
    )

    # --- Summary ---
    print()
    print("=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)

    def _fmt(r: dict) -> str:
        decisive = r["wins"] + r["losses"]
        return (
            f"  {r['name']:42s}  "
            f"W{r['wins']:3d} L{r['losses']:3d} D{r['draws']:2d} / {r['games']}  "
            f"win%={100*r['win_rate']:5.1f}%  "
            f"avg_game={r['avg_game_time']:.1f}s"
        )

    print(_fmt(result_mcts))
    print(_fmt(result_learned))
    print()

    delta = result_mcts["win_rate"] - result_learned["win_rate"]
    if delta > 0:
        print(f"  rollout MCTS is +{100*delta:.1f}pp vs plain learned "
              f"(hypothesis SUPPORTED)")
    elif delta < 0:
        print(f"  rollout MCTS is {100*delta:.1f}pp vs plain learned "
              f"(hypothesis NOT supported)")
    else:
        print("  No difference between rollout MCTS and plain learned.")

    print(f"\n  BC ceiling reference: ~15% win rate vs heuristic")
    print("=" * 70)


if __name__ == "__main__":
    main()
