#!/usr/bin/env python3
"""Simple policy benchmark - fast version for testing."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.engine.game_loop import make_random_policy, play_game
from tsrl.policies.minimal_hybrid import make_minimal_hybrid_policy
from tsrl.schemas import Side

def play_match_simple(policy0, policy1, n_games=40, base_seed=42):
    """Play n games alternating sides, return (p0_wins, p1_wins, draws)."""
    p0_wins = p1_wins = draws = 0
    for i in range(n_games):
        seed = base_seed + i
        if i % 2 == 0:
            result = play_game(policy0, policy1, seed=seed)
            if result.winner == Side.USSR:
                p0_wins += 1
            elif result.winner == Side.US:
                p1_wins += 1
            else:
                draws += 1
        else:
            result = play_game(policy1, policy0, seed=seed)
            if result.winner == Side.USSR:
                p1_wins += 1
            elif result.winner == Side.US:
                p0_wins += 1
            else:
                draws += 1
        print(f"Game {i+1}/{n_games}: W={result.winner} VP={result.final_vp} Turn={result.end_turn}", flush=True)
    return p0_wins, p1_wins, draws

if __name__ == "__main__":
    n_games = 40
    print(f"Building policies...", flush=True)
    random_policy = make_random_policy()
    heuristic_policy = make_minimal_hybrid_policy()

    print(f"\nRunning {n_games} games: random vs heuristic", flush=True)
    p0_w, p1_w, draws = play_match_simple(random_policy, heuristic_policy, n_games=n_games, base_seed=42)

    print(f"\n{'=' * 60}", flush=True)
    print(f"RESULTS: random vs heuristic ({n_games} games)", flush=True)
    print(f"  random win rate: {p0_w / n_games * 100:.1f}%", flush=True)
    print(f"  heuristic win rate: {p1_w / n_games * 100:.1f}%", flush=True)
    print(f"  draw rate: {draws / n_games * 100:.1f}%", flush=True)
    print(f"{'=' * 60}", flush=True)
