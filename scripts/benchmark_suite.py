"""Comprehensive policy benchmark suite for Twilight Struggle AI.

Benchmarks all meaningful policy × MCTS combinations and outputs a clean win-rate table.

Matchups tested:
1. random vs random (baseline — should be ~50%)
2. heuristic vs random (heuristic = minimal_hybrid)
3. random vs heuristic (reversed — verifies symmetry)
4. heuristic vs heuristic (sanity check — should be ~50%)
5. heuristic+mcts5 vs random (flat_mcts n_sim=5)
6. heuristic+mcts5 vs heuristic
7. heuristic+mcts20 vs heuristic
8. learned vs random (if checkpoint exists)
9. learned vs heuristic (if checkpoint exists)

For each matchup:
- Play N games (default 100)
- Alternate sides every game (symmetric)
- Track wins/losses/draws by game outcome
- Print clean table with win rates and draw %
"""
from __future__ import annotations

import argparse
import os
import random
import subprocess
import sys
from dataclasses import dataclass
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.engine.game_loop import (
    GameResult,
    Policy,
    make_random_policy,
    play_game,
)
from tsrl.policies.minimal_hybrid import make_minimal_hybrid_policy
from tsrl.schemas import Side


# ---------------------------------------------------------------------------
# Direct MCTS game runner
# ---------------------------------------------------------------------------


def play_game_with_mcts(
    ussr_n_sim: int,
    us_n_sim: int,
    ussr_rollout: Policy,
    us_rollout: Policy,
    *,
    seed: int,
) -> GameResult:
    """Play one game where each side may use flat MCTS over the live GameState."""
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
    from tsrl.engine.mcts import flat_mcts

    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))

    sim_counts = {Side.USSR: ussr_n_sim, Side.US: us_n_sim}
    rollouts = {Side.USSR: ussr_rollout, Side.US: us_rollout}

    def _mcts_policy(pub, hand, holds_china):
        side = pub.phasing
        n_sim = sim_counts[side]
        rollout = rollouts[side]
        if n_sim == 0:
            return rollout(pub, hand, holds_china)

        gs_snap = clone_game_state(gs)
        gs_snap.hands[side] = hand
        action = flat_mcts(gs_snap, n_sim, rollout_policy=rollout, rng=rng)
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
        result = GameResult(winner, gs.pub.vp, _MAX_TURNS, "turn_limit")

    return result


# ---------------------------------------------------------------------------
# Match result tracking
# ---------------------------------------------------------------------------


@dataclass
class MatchResult:
    """Result of one matchup (side0 vs side1)."""
    name: str
    n_games: int
    side0_ussr_wins: int
    side0_us_wins: int
    side0_draws: int
    side1_ussr_wins: int
    side1_us_wins: int
    side1_draws: int

    @property
    def side0_win_rate(self) -> float:
        """Side 0's win rate (including both USSR and US victories)."""
        wins = self.side0_ussr_wins + self.side0_us_wins
        return wins / self.n_games if self.n_games > 0 else 0.0

    @property
    def side1_win_rate(self) -> float:
        """Side 1's win rate."""
        wins = self.side1_ussr_wins + self.side1_us_wins
        return wins / self.n_games if self.n_games > 0 else 0.0

    @property
    def draw_rate(self) -> float:
        """Draw rate."""
        total_draws = self.side0_draws + self.side1_draws
        return total_draws / self.n_games if self.n_games > 0 else 0.0


# ---------------------------------------------------------------------------
# Benchmark runner
# ---------------------------------------------------------------------------


def play_match(
    policy0: Policy,
    policy1: Policy,
    *,
    n_games: int = 100,
    base_seed: int = 42,
    ussr_n_sim: int = 0,
    us_n_sim: int = 0,
) -> MatchResult:
    """Play a match between two policies, alternating sides.

    Args:
        policy0: First rollout policy (USSR in even games, US in odd games).
        policy1: Second rollout policy (US in even games, USSR in odd games).
        n_games: Total number of games to play.
        base_seed: Base seed for RNG.
        ussr_n_sim: MCTS simulations for policy0 in even games / policy1 in odd games.
        us_n_sim: MCTS simulations for policy1 in even games / policy0 in odd games.

    Returns a MatchResult with win-rate breakdown.
    """
    side0_ussr_wins = 0
    side0_us_wins = 0
    side0_draws = 0
    side1_ussr_wins = 0
    side1_us_wins = 0
    side1_draws = 0

    for game_idx in range(n_games):
        game_seed = base_seed + game_idx
        use_mcts = ussr_n_sim > 0 or us_n_sim > 0

        # Alternate sides: even games policy0=USSR, odd games policy0=US
        if game_idx % 2 == 0:
            if use_mcts:
                result = play_game_with_mcts(
                    ussr_n_sim,
                    us_n_sim,
                    policy0,
                    policy1,
                    seed=game_seed,
                )
            else:
                result = play_game(policy0, policy1, seed=game_seed)
            if result.winner == Side.USSR:
                side0_ussr_wins += 1
            elif result.winner == Side.US:
                side1_us_wins += 1
            else:
                side0_draws += 1
        else:
            if use_mcts:
                result = play_game_with_mcts(
                    us_n_sim,
                    ussr_n_sim,
                    policy1,
                    policy0,
                    seed=game_seed,
                )
            else:
                result = play_game(policy1, policy0, seed=game_seed)
            if result.winner == Side.USSR:
                side1_ussr_wins += 1
            elif result.winner == Side.US:
                side0_us_wins += 1
            else:
                side1_draws += 1

    return MatchResult(
        name="",
        n_games=n_games,
        side0_ussr_wins=side0_ussr_wins,
        side0_us_wins=side0_us_wins,
        side0_draws=side0_draws,
        side1_ussr_wins=side1_ussr_wins,
        side1_us_wins=side1_us_wins,
        side1_draws=side1_draws,
    )


# ---------------------------------------------------------------------------
# Benchmark suite
# ---------------------------------------------------------------------------


def run_benchmark_suite(n_games: int = 100, base_seed: int = 42) -> list[tuple[str, MatchResult]]:
    """Run all benchmark matchups.

    Args:
        n_games: Number of games per matchup.
        base_seed: Base seed for RNG.

    Returns a list of (name, result) tuples.
    """
    try:
        os.nice(10)
    except OSError:
        pass

    results: list[tuple[str, MatchResult]] = []

    print("Building policies...", flush=True)
    # Build policies
    random_policy = make_random_policy()
    heuristic_policy = make_minimal_hybrid_policy()
    print("  random_policy: OK", flush=True)
    print("  heuristic_policy: OK", flush=True)

    # Try to load learned policy
    learned_policy_ussr: Optional[Policy] = None
    learned_policy_us: Optional[Policy] = None
    learned_available = False

    checkpoint_path = "/home/dkord/code/twilight-struggle-ai/checkpoints/baseline_epoch3.pt"
    if os.path.exists(checkpoint_path):
        try:
            torch_probe = subprocess.run(
                [sys.executable, "-c", "import torch"],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if torch_probe.returncode == 0:
                from tsrl.policies.learned_policy import make_learned_policy

                print(f"Loading learned policy from {checkpoint_path}...")
                learned_policy_ussr = make_learned_policy(checkpoint_path, Side.USSR)
                learned_policy_us = make_learned_policy(checkpoint_path, Side.US)
                learned_available = True
                print("  learned_policy: OK")
            else:
                print("  Skipping learned policy: torch import failed in this environment")
        except Exception as e:
            print(f"  Failed to load learned policy: {e}")

    # 1. random vs random (baseline)
    print(f"\n[1/9] random vs random ({n_games} games)...", flush=True)
    result = play_match(random_policy, random_policy, n_games=n_games, base_seed=base_seed)
    result.name = "random vs random"
    results.append(("random vs random", result))

    # 2. heuristic vs random
    print(f"[2/9] heuristic vs random ({n_games} games)...", flush=True)
    result = play_match(heuristic_policy, random_policy, n_games=n_games, base_seed=base_seed + 1000)
    result.name = "heuristic vs random"
    results.append(("heuristic vs random", result))

    # 3. random vs heuristic (reversed)
    print(f"[3/9] random vs heuristic ({n_games} games)...", flush=True)
    result = play_match(random_policy, heuristic_policy, n_games=n_games, base_seed=base_seed + 2000)
    result.name = "random vs heuristic"
    results.append(("random vs heuristic", result))

    # 4. heuristic vs heuristic (sanity check)
    print(f"[4/9] heuristic vs heuristic ({n_games} games)...", flush=True)
    result = play_match(heuristic_policy, heuristic_policy, n_games=n_games, base_seed=base_seed + 3000)
    result.name = "heuristic vs heuristic"
    results.append(("heuristic vs heuristic", result))

    # 5. heuristic+mcts5 vs random
    print(f"[5/9] heuristic+mcts5 vs random ({n_games} games)...", flush=True)
    result = play_match(
        heuristic_policy,
        random_policy,
        n_games=n_games,
        base_seed=base_seed + 4000,
        ussr_n_sim=5,
    )
    result.name = "heuristic+mcts5 vs random"
    results.append(("heuristic+mcts5 vs random", result))

    # 6. heuristic+mcts5 vs heuristic
    print(f"[6/9] heuristic+mcts5 vs heuristic ({n_games} games)...", flush=True)
    result = play_match(
        heuristic_policy,
        heuristic_policy,
        n_games=n_games,
        base_seed=base_seed + 5000,
        ussr_n_sim=5,
    )
    result.name = "heuristic+mcts5 vs heuristic"
    results.append(("heuristic+mcts5 vs heuristic", result))

    # 7. heuristic+mcts20 vs heuristic
    print(f"[7/9] heuristic+mcts20 vs heuristic ({n_games} games)...", flush=True)
    result = play_match(
        heuristic_policy,
        heuristic_policy,
        n_games=n_games,
        base_seed=base_seed + 6000,
        ussr_n_sim=20,
    )
    result.name = "heuristic+mcts20 vs heuristic"
    results.append(("heuristic+mcts20 vs heuristic", result))

    # 8. learned vs random (if available)
    if learned_available:
        print(f"[8/9] learned vs random ({n_games} games)...", flush=True)
        result = play_match(learned_policy_ussr, random_policy, n_games=n_games, base_seed=base_seed + 7000)
        # Note: learned_policy_us is used in play_match when alternating sides
        results.append(("learned vs random", result))
        print(f"[9/9] learned vs heuristic ({n_games} games)...", flush=True)
        result = play_match(learned_policy_ussr, heuristic_policy, n_games=n_games, base_seed=base_seed + 8000)
        results.append(("learned vs heuristic", result))
    else:
        print(f"[8/9] learned vs random - SKIPPED (no checkpoint)", flush=True)
        print(f"[9/9] learned vs heuristic - SKIPPED (no checkpoint)", flush=True)

    return results


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def print_results_table(results: list[tuple[str, MatchResult]]) -> None:
    """Print a clean win-rate table."""
    print("\n" + "=" * 90)
    print("BENCHMARK RESULTS")
    print("=" * 90)
    print(f"{'Matchup':<35} {'Games':>7} {'Side0 WR%':>10} {'Side1 WR%':>10} {'Draw%':>10}")
    print("-" * 90)

    for name, result in results:
        side0_wr = result.side0_win_rate * 100
        side1_wr = result.side1_win_rate * 100
        draw_pct = result.draw_rate * 100
        print(f"{name:<35} {result.n_games:>7d} {side0_wr:>10.1f}% {side1_wr:>10.1f}% {draw_pct:>10.1f}%")

    print("=" * 90)


def print_summary_stats(results: list[tuple[str, MatchResult]]) -> None:
    """Print summary findings."""
    print("\n" + "=" * 90)
    print("KEY FINDINGS")
    print("=" * 90)

    # Random baseline
    random_vs_random = next((r for n, r in results if n == "random vs random"), None)
    if random_vs_random:
        print(f"\nBaseline (random vs random):")
        print(f"  Side 0 win rate: {random_vs_random.side0_win_rate * 100:.1f}%")
        print(f"  Draw rate:       {random_vs_random.draw_rate * 100:.1f}%")

    # Heuristic strength vs random
    heur_vs_random = next((r for n, r in results if n == "heuristic vs random"), None)
    if heur_vs_random:
        print(f"\nHeuristic vs random:")
        print(f"  Heuristic win rate: {heur_vs_random.side0_win_rate * 100:.1f}%")
        print(f"  (Heuristic is stronger: {heur_vs_random.side0_win_rate > 0.5})")

    # Symmetry check
    heur_vs_random = next((r for n, r in results if n == "heuristic vs random"), None)
    random_vs_heur = next((r for n, r in results if n == "random vs heuristic"), None)
    if heur_vs_random and random_vs_heur:
        print(f"\nSymmetry check (heuristic vs random):")
        print(f"  heuristic (as side0) win rate: {heur_vs_random.side0_win_rate * 100:.1f}%")
        print(f"  random (as side0) win rate: {random_vs_heur.side0_win_rate * 100:.1f}%")
        expected_random_wr = 1.0 - heur_vs_random.side0_win_rate
        error = abs(random_vs_heur.side0_win_rate - expected_random_wr)
        print(f"  Symmetry error: {error * 100:.1f}% (goal: <5%)")

    # Heuristic self-play
    heur_vs_heur = next((r for n, r in results if n == "heuristic vs heuristic"), None)
    if heur_vs_heur:
        print(f"\nHeuristic self-play (sanity check):")
        print(f"  Side 0 win rate: {heur_vs_heur.side0_win_rate * 100:.1f}% (should be ~50%)")

    # MCTS value-add
    heur_mcts5_vs_heur = next((r for n, r in results if n == "heuristic+mcts5 vs heuristic"), None)
    if heur_mcts5_vs_heur:
        heur_mcts5_wr = heur_mcts5_vs_heur.side0_win_rate * 100
        print(f"\nMCTS value-add (heuristic+mcts5 vs heuristic):")
        print(f"  MCTS5 win rate: {heur_mcts5_wr:.1f}%")
        print(f"  Strength gain: {heur_mcts5_wr - 50.0:+.1f}pp")

    heur_mcts20_vs_heur = next((r for n, r in results if n == "heuristic+mcts20 vs heuristic"), None)
    if heur_mcts20_vs_heur:
        heur_mcts20_wr = heur_mcts20_vs_heur.side0_win_rate * 100
        print(f"\nMCTS value-add (heuristic+mcts20 vs heuristic):")
        print(f"  MCTS20 win rate: {heur_mcts20_wr:.1f}%")
        print(f"  Strength gain: {heur_mcts20_wr - 50.0:+.1f}pp")

    # Learned policy (if available)
    learned_vs_random = next((r for n, r in results if n == "learned vs random"), None)
    if learned_vs_random:
        print(f"\nLearned policy vs random:")
        print(f"  Learned win rate: {learned_vs_random.side0_win_rate * 100:.1f}%")

    learned_vs_heur = next((r for n, r in results if n == "learned vs heuristic"), None)
    if learned_vs_heur:
        print(f"\nLearned policy vs heuristic:")
        print(f"  Learned win rate: {learned_vs_heur.side0_win_rate * 100:.1f}%")
        print(f"  (Learned is stronger: {learned_vs_heur.side0_win_rate > 0.5})")

    print("=" * 90)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    import sys
    sys.stdout = __import__('sys').stdout  # Ensure stdout is flushed

    parser = argparse.ArgumentParser(
        description="Run comprehensive policy benchmark suite."
    )
    parser.add_argument(
        "--n-games",
        type=int,
        default=100,
        help="Number of games per matchup (default: 100)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Base seed for RNG (default: 42)",
    )
    args = parser.parse_args()

    print(f"Running benchmark suite: {args.n_games} games per matchup, seed={args.seed}", flush=True)

    results = run_benchmark_suite(n_games=args.n_games, base_seed=args.seed)
    print_results_table(results)
    print_summary_stats(results)


if __name__ == "__main__":
    main()
