"""Play learned-policy benchmark games against the random policy."""
from __future__ import annotations

import argparse
import os
import random
import sys

import torch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.engine.game_loop import make_random_policy, play_game
from tsrl.policies.learned_policy import make_learned_policy
from tsrl.schemas import Side


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmark learned policy vs random.")
    parser.add_argument("--checkpoint", required=True, help="Path to a saved model checkpoint")
    parser.add_argument("--n-games", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def _rate(wins: int, games: int) -> float:
    return wins / games if games else 0.0


def main() -> None:
    try:
        os.nice(10)
    except OSError:
        pass

    args = parse_args()
    learned_ussr = make_learned_policy(args.checkpoint, Side.USSR)
    learned_us = make_learned_policy(args.checkpoint, Side.US)

    n_as_ussr = args.n_games // 2
    wins_as_ussr = 0
    wins_as_us = 0
    turns: list[int] = []

    for game_idx in range(args.n_games):
        game_seed = args.seed + game_idx
        random.seed(game_seed)
        torch.manual_seed(game_seed)
        random_policy = make_random_policy(random.Random(game_seed + 10_000))

        if game_idx < n_as_ussr:
            result = play_game(learned_ussr, random_policy, seed=game_seed)
            wins_as_ussr += int(result.winner == Side.USSR)
        else:
            result = play_game(random_policy, learned_us, seed=game_seed)
            wins_as_us += int(result.winner == Side.US)

        turns.append(result.end_turn)

    n_as_us = args.n_games - n_as_ussr
    overall_wins = wins_as_ussr + wins_as_us
    print(f"win_rate_as_ussr={_rate(wins_as_ussr, n_as_ussr):.3f}")
    print(f"win_rate_as_us={_rate(wins_as_us, n_as_us):.3f}")
    print(f"overall_win_rate={_rate(overall_wins, args.n_games):.3f}")
    print(f"avg_turns={sum(turns) / len(turns):.3f}")


if __name__ == "__main__":
    main()
