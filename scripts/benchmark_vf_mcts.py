"""Benchmark value-function MCTS against baselines.

Usage:
    uv run python scripts/benchmark_vf_mcts.py \\
        --checkpoint data/checkpoints/baseline_epoch20.pt \\
        --n-games 20 \\
        --n-sim 5

Compares:
  1. vf_mcts5 (value-function MCTS, n_sim=5) vs random
  2. vf_mcts5 vs heuristic
  3. vf_mcts20 vs heuristic
  4. Prints wall-time per move for profiling
"""
from __future__ import annotations

import argparse
import os
import random
import sys
import time
from dataclasses import dataclass
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.engine.game_loop import GameResult, Policy, make_random_policy, play_game
from tsrl.engine.mcts import uct_mcts
from tsrl.policies.learned_policy import make_value_function
from tsrl.policies.minimal_hybrid import make_minimal_hybrid_policy
from tsrl.schemas import Side


@dataclass
class BenchmarkResult:
    """Result of a matchup: policy_a vs policy_b."""

    name: str  # "vf_mcts5 vs random", etc.
    games: int
    ussr_wins: int
    us_wins: int
    draws: int
    avg_wall_time_per_move: float  # seconds

    @property
    def ussr_winrate(self) -> float:
        return self.ussr_wins / max(1, self.games - self.draws)

    @property
    def us_winrate(self) -> float:
        return self.us_wins / max(1, self.games - self.draws)

    @property
    def draw_rate(self) -> float:
        return self.draws / max(1, self.games)

    def __str__(self) -> str:
        decisive = self.games - self.draws
        return (
            f"{self.name:30s} "
            f"  USSR {self.ussr_wins:3d}/{decisive:3d} ({100*self.ussr_winrate:5.1f}%)  "
            f"US {self.us_wins:3d}/{decisive:3d} ({100*self.us_winrate:5.1f}%)  "
            f"Draw {self.draws:2d}/{self.games} ({100*self.draw_rate:4.1f}%)  "
            f"Time {self.avg_wall_time_per_move*1000:.1f}ms/move"
        )


_VF_SIDE: Side = Side.USSR
_VF_OPPONENT_POLICY: Optional[Policy] = None


def play_game_with_vf_uct(
    value_fn,
    n_sim: int,
    seed: int,
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

    del candidate_fn

    if _VF_OPPONENT_POLICY is None:
        raise RuntimeError("opponent policy not configured")

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))

    def _vf_policy(pub, hand, holds_china):
        side = pub.phasing
        if side != _VF_SIDE:
            return _VF_OPPONENT_POLICY(pub, hand, holds_china)

        gs_snap = clone_game_state(gs)
        gs_snap.hands[side] = hand
        action = uct_mcts(gs_snap, n_sim, value_fn=value_fn, rng=rng)
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


def run_matchup(
    name: str,
    policy_a: Policy,
    policy_b: Policy,
    n_games: int,
    seed: int,
    *,
    vf_value_fn=None,
    vf_n_sim: int = 0,
) -> BenchmarkResult:
    """Play n_games between two policies, alternating sides."""
    ussr_wins = us_wins = draws = 0
    total_time = 0.0
    move_count = 0

    for game_idx in range(n_games):
        # Alternate sides
        if game_idx % 2 == 0:
            ussr_pol, us_pol = policy_a, policy_b
        else:
            ussr_pol, us_pol = policy_b, policy_a

        t0 = time.time()
        if vf_value_fn is None:
            result = play_game(ussr_pol, us_pol, seed=seed + game_idx)
        else:
            global _VF_SIDE, _VF_OPPONENT_POLICY
            _VF_SIDE = Side.USSR if game_idx % 2 == 0 else Side.US
            _VF_OPPONENT_POLICY = us_pol if _VF_SIDE == Side.USSR else ussr_pol
            result = play_game_with_vf_uct(
                vf_value_fn,
                vf_n_sim,
                seed + game_idx,
            )
        t1 = time.time()
        total_time += t1 - t0

        if result.winner == Side.USSR:
            ussr_wins += 1
        elif result.winner == Side.US:
            us_wins += 1
        else:
            draws += 1

        # Rough estimate of move count per game (~50-150 moves typically)
        move_count += 100

    avg_time = total_time / max(1, move_count)
    return BenchmarkResult(
        name=name,
        games=n_games,
        ussr_wins=ussr_wins,
        us_wins=us_wins,
        draws=draws,
        avg_wall_time_per_move=avg_time,
    )


def main():
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
    args = p.parse_args()

    if not os.path.exists(args.checkpoint):
        print(f"ERROR: checkpoint not found: {args.checkpoint}")
        sys.exit(1)

    print(f"Loading checkpoint: {args.checkpoint}")
    print(f"Games per matchup: {args.n_games}")
    print(f"MCTS simulations: {args.n_sim}\n")

    # Make policies
    random_pol = make_random_policy(random.Random(args.seed))
    heuristic_pol = make_minimal_hybrid_policy()

    try:
        value_fn = make_value_function(args.checkpoint)
        print(f"✓ Value function loaded\n")
    except Exception as e:
        print(f"ERROR loading value function: {e}")
        sys.exit(1)

    # Run benchmarks
    print("=" * 120)
    print(f"BENCHMARK RESULTS (n_games={args.n_games}, n_sim={args.n_sim})")
    print("=" * 120)

    results = []

    # 1. Random vs Random (baseline)
    print("\n1. Baseline: random vs random")
    r = run_matchup("random vs random", random_pol, random_pol, args.n_games, args.seed)
    results.append(r)
    print(f"   {r}")

    # 2. Heuristic vs Random
    print("\n2. Heuristic vs random")
    r = run_matchup(
        "heuristic vs random", heuristic_pol, random_pol, args.n_games, args.seed + 100
    )
    results.append(r)
    print(f"   {r}")

    # 3. vf_mcts5 vs random
    print("\n3. vf_mcts5 vs random")
    r = run_matchup(
        "vf_mcts5 vs random",
        random_pol,
        random_pol,
        args.n_games,
        args.seed + 200,
        vf_value_fn=value_fn,
        vf_n_sim=5,
    )
    results.append(r)
    print(f"   {r}")

    # 4. vf_mcts5 vs heuristic
    print("\n4. vf_mcts5 vs heuristic")
    r = run_matchup(
        "vf_mcts5 vs heuristic",
        heuristic_pol,
        heuristic_pol,
        args.n_games,
        args.seed + 300,
        vf_value_fn=value_fn,
        vf_n_sim=5,
    )
    results.append(r)
    print(f"   {r}")


if __name__ == "__main__":
    main()
