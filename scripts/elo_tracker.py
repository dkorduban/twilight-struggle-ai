#!/usr/bin/env python3
"""Elo rating tracker for model checkpoints.

Tracks relative strength between model checkpoints using head-to-head game results.
Uses standard Elo rating system with K=32 and initial rating 1500.

Usage:
    # Run a matchup and update ratings:
    uv run python scripts/elo_tracker.py matchup \\
        --model-a data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt \\
        --model-b data/checkpoints/ppo_v2_selfplay/ppo_best_scripted.pt \\
        --n-games 200 --seed 77000

    # Print current leaderboard:
    uv run python scripts/elo_tracker.py leaderboard

    # Show match history:
    uv run python scripts/elo_tracker.py history
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

RATINGS_FILE = Path("results/checkpoint_elo.json")
INITIAL_ELO = 1500.0
K = 32.0


def load_ratings() -> dict:
    if RATINGS_FILE.exists():
        return json.loads(RATINGS_FILE.read_text())
    return {"ratings": {}, "history": []}


def save_ratings(data: dict) -> None:
    RATINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    RATINGS_FILE.write_text(json.dumps(data, indent=2))


def expected_score(rating_a: float, rating_b: float) -> float:
    return 1.0 / (1.0 + 10 ** ((rating_b - rating_a) / 400.0))


def update_elo(rating_a: float, rating_b: float, score_a: float) -> tuple[float, float]:
    """Update Elo ratings. score_a: 1.0=model_a won, 0.0=model_a lost, 0.5=draw."""
    exp_a = expected_score(rating_a, rating_b)
    new_a = rating_a + K * (score_a - exp_a)
    new_b = rating_b + K * ((1.0 - score_a) - (1.0 - exp_a))
    return new_a, new_b


def get_rating(data: dict, model_path: str) -> float:
    return data["ratings"].get(model_path, INITIAL_ELO)


def cmd_matchup(args: argparse.Namespace) -> None:
    """Run a head-to-head matchup and update Elo ratings."""
    import sys
    sys.path.insert(0, "build-ninja/bindings")
    sys.path.insert(0, "build/bindings")
    try:
        import tscore
    except ImportError:
        print("ERROR: cannot import tscore. Build first: cmake --build build-ninja -j")
        sys.exit(1)

    if not hasattr(tscore, "benchmark_model_vs_model_batched"):
        print("ERROR: tscore.benchmark_model_vs_model_batched not available. Rebuild with new C++.")
        sys.exit(1)

    model_a = args.model_a
    model_b = args.model_b
    n_games = args.n_games
    seed = args.seed
    pool_size = min(n_games, 64)

    # Verify files exist
    if not Path(model_a).exists():
        print(f"ERROR: model_a not found: {model_a}")
        sys.exit(1)
    if not Path(model_b).exists():
        print(f"ERROR: model_b not found: {model_b}")
        sys.exit(1)

    print(f"Running {n_games} games:")
    print(f"  A: {model_a}")
    print(f"  B: {model_b}")

    results = tscore.benchmark_model_vs_model_batched(
        model_a_path=model_a,
        model_b_path=model_b,
        n_games=n_games,
        pool_size=pool_size,
        seed=seed,
        temperature=0.0,
        nash_temperatures=False,
    )

    # First half: model_a=USSR, model_b=US
    # Second half: model_a=US, model_b=USSR
    half = n_games // 2
    a_wins = 0
    b_wins = 0
    draws = 0
    for i, r in enumerate(results):
        if r.winner is None:
            draws += 1
            continue
        if i < half:
            # model_a is USSR
            a_wins += 1 if r.winner == tscore.Side.USSR else 0
            b_wins += 1 if r.winner == tscore.Side.US else 0
        else:
            # model_a is US
            a_wins += 1 if r.winner == tscore.Side.US else 0
            b_wins += 1 if r.winner == tscore.Side.USSR else 0

    total = len(results)
    a_wr = a_wins / total if total > 0 else 0.5

    print(f"\nResults: A wins {a_wins}/{total} ({a_wr:.1%}), B wins {b_wins}/{total}, draws {draws}")

    # Load and update Elo
    data = load_ratings()
    rating_a_before = get_rating(data, model_a)
    rating_b_before = get_rating(data, model_b)

    # Apply per-game Elo updates (more accurate than aggregate)
    rating_a = rating_a_before
    rating_b = rating_b_before
    for i, r in enumerate(results):
        if r.winner is None:
            score_a = 0.5
        elif i < half:
            score_a = 1.0 if r.winner == tscore.Side.USSR else 0.0
        else:
            score_a = 1.0 if r.winner == tscore.Side.US else 0.0
        rating_a, rating_b = update_elo(rating_a, rating_b, score_a)

    print(f"\nElo update:")
    print(f"  A: {rating_a_before:.1f} -> {rating_a:.1f} ({rating_a - rating_a_before:+.1f})")
    print(f"  B: {rating_b_before:.1f} -> {rating_b:.1f} ({rating_b - rating_b_before:+.1f})")

    # Save
    data["ratings"][model_a] = rating_a
    data["ratings"][model_b] = rating_b
    data["history"].append({
        "date": datetime.now(timezone.utc).isoformat(),
        "model_a": model_a,
        "model_b": model_b,
        "n_games": n_games,
        "seed": seed,
        "model_a_wins": a_wins,
        "model_b_wins": b_wins,
        "draws": draws,
        "model_a_wr": round(a_wr, 4),
        "model_a_elo_before": round(rating_a_before, 2),
        "model_a_elo_after": round(rating_a, 2),
        "model_b_elo_before": round(rating_b_before, 2),
        "model_b_elo_after": round(rating_b, 2),
    })
    save_ratings(data)
    print(f"\nSaved to {RATINGS_FILE}")


def cmd_leaderboard(args: argparse.Namespace) -> None:
    """Print current Elo leaderboard sorted by rating."""
    data = load_ratings()
    if not data["ratings"]:
        print("No ratings yet. Run a matchup first.")
        return

    print(f"\n{'Elo':>7}  {'Model':}")
    print("-" * 60)
    sorted_ratings = sorted(data["ratings"].items(), key=lambda x: -x[1])
    for model, rating in sorted_ratings:
        label = Path(model).name if len(model) > 50 else model
        print(f"{rating:7.1f}  {label}")


def cmd_history(args: argparse.Namespace) -> None:
    """Print match history."""
    data = load_ratings()
    if not data["history"]:
        print("No match history yet.")
        return

    print(f"\n{'Date':<22} {'A WR':>6}  {'ΔElo(A)':>8}  A vs B")
    print("-" * 80)
    for entry in data["history"]:
        date = entry["date"][:19].replace("T", " ")
        a_label = Path(entry["model_a"]).name
        b_label = Path(entry["model_b"]).name
        delta = entry["model_a_elo_after"] - entry["model_a_elo_before"]
        print(f"{date:<22} {entry['model_a_wr']:6.1%}  {delta:+8.1f}  {a_label} vs {b_label}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Elo rating tracker for model checkpoints")
    sub = parser.add_subparsers(dest="cmd")

    p_matchup = sub.add_parser("matchup", help="Run a head-to-head matchup")
    p_matchup.add_argument("--model-a", required=True, help="Path to model A scripted .pt")
    p_matchup.add_argument("--model-b", required=True, help="Path to model B scripted .pt")
    p_matchup.add_argument("--n-games", type=int, default=200, help="Total games (half each side)")
    p_matchup.add_argument("--seed", type=int, default=77000, help="Random seed")

    sub.add_parser("leaderboard", help="Print Elo leaderboard")
    sub.add_parser("history", help="Print match history")

    args = parser.parse_args()
    if args.cmd is None:
        parser.print_help()
        sys.exit(1)

    if args.cmd == "matchup":
        cmd_matchup(args)
    elif args.cmd == "leaderboard":
        cmd_leaderboard(args)
    elif args.cmd == "history":
        cmd_history(args)


if __name__ == "__main__":
    main()
