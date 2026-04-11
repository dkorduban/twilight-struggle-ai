#!/usr/bin/env python3
"""Estimate anchored BayesElo ratings from benchmark history."""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path


LOGISTIC_SCALE = math.log(10.0) / 400.0


@dataclass(frozen=True)
class MatchResult:
    player_a: str
    player_b: str
    wins_a: int
    wins_b: int

    @property
    def games(self) -> int:
        return self.wins_a + self.wins_b


def generation_sort_key(name: str) -> tuple[int, str]:
    match = re.fullmatch(r"v(\d+)", name)
    if match:
        return (int(match.group(1)), name)
    return (10**9, name)


def load_history(path: Path) -> dict[str, float]:
    raw = json.loads(path.read_text())
    if not isinstance(raw, dict):
        raise ValueError("benchmark history must be a JSON object")

    history: dict[str, float] = {}
    for generation, payload in raw.items():
        if not isinstance(payload, dict) or "learned_vs_heuristic" not in payload:
            raise ValueError(f"missing learned_vs_heuristic for {generation}")
        win_pct = float(payload["learned_vs_heuristic"])
        if win_pct < 0.0 or win_pct > 100.0:
            raise ValueError(f"win% for {generation} must be in [0, 100]")
        history[str(generation)] = win_pct
    return history


def build_matches(history: dict[str, float], games_per_match: int, anchor_name: str) -> list[MatchResult]:
    matches: list[MatchResult] = []
    for generation in sorted(history, key=generation_sort_key):
        wins = int(round(history[generation] * games_per_match / 100.0))
        wins = max(0, min(games_per_match, wins))
        matches.append(
            MatchResult(
                player_a=generation,
                player_b=anchor_name,
                wins_a=wins,
                wins_b=games_per_match - wins,
            )
        )
    return matches


def load_h2h_matches(path: Path) -> list[MatchResult]:
    """Load head-to-head results from checkpoint_elo.json history.

    Deduplicates by (model_a, model_b, seed) to avoid double-counting runs
    with the same seed. Uses the filename stem as the player identifier so
    results can be joined with vs-heuristic history.
    """
    raw = json.loads(path.read_text())
    history_entries = raw.get("history", [])

    seen: set[tuple[str, str, int]] = set()
    matches: list[MatchResult] = []
    for entry in history_entries:
        a_name = Path(entry["model_a"]).stem
        b_name = Path(entry["model_b"]).stem
        # Skip self-matches: no information content, and skewed results
        # from asymmetric game structure corrupt BayesElo fits.
        if a_name == b_name:
            continue
        seed = entry.get("seed", 0)
        key = (a_name, b_name, seed)
        if key in seen:
            continue
        seen.add(key)
        wins_a = entry["model_a_wins"]
        wins_b = entry["model_b_wins"]
        # Draws count as 0.5 wins each — split between both players
        draws = entry.get("draws", 0)
        wins_a_eff = wins_a * 2 + draws  # multiply by 2 to preserve integer arithmetic
        wins_b_eff = wins_b * 2 + draws
        if wins_a_eff + wins_b_eff == 0:
            continue
        # Use half-draws: each draw contributes 0.5 to both. MatchResult stores
        # integer wins, so represent as wins_a=actual+draws/2 using 2x scaling.
        # Simpler: just use actual wins (ignoring draws) since draws are rare.
        if wins_a + wins_b == 0:
            continue
        matches.append(MatchResult(player_a=a_name, player_b=b_name, wins_a=wins_a, wins_b=wins_b))
    return matches


def invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    if n == 0:
        return []

    augmented = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(augmented[row][col]))
        if abs(augmented[pivot][col]) < 1e-12:
            raise ValueError("information matrix is singular")
        if pivot != col:
            augmented[col], augmented[pivot] = augmented[pivot], augmented[col]

        pivot_value = augmented[col][col]
        for j in range(2 * n):
            augmented[col][j] /= pivot_value

        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor == 0.0:
                continue
            for j in range(2 * n):
                augmented[row][j] -= factor * augmented[col][j]

    return [row[n:] for row in augmented]


def fit_bayes_elo_mm(
    players: list[str],
    matches: list[MatchResult],
    anchor_name: str,
    anchor_rating: float,
    max_iter: int,
    tol: float,
) -> dict[str, float]:
    anchor_ability = 10.0 ** (anchor_rating / 400.0)
    abilities = {player: anchor_ability for player in players}
    abilities[anchor_name] = anchor_ability

    free_players = [player for player in players if player != anchor_name]
    if not free_players:
        return {anchor_name: anchor_rating}

    for _ in range(max_iter):
        updated = abilities.copy()
        max_delta = 0.0
        for player in free_players:
            total_wins = 0.0
            denom = 0.0
            ability_i = abilities[player]
            for match in matches:
                if match.player_a == player:
                    opponent = match.player_b
                    total_wins += match.wins_a
                    denom += match.games / (ability_i + abilities[opponent])
                elif match.player_b == player:
                    opponent = match.player_a
                    total_wins += match.wins_b
                    denom += match.games / (ability_i + abilities[opponent])
            if denom <= 0.0:
                continue
            new_ability = total_wins / denom
            updated[player] = new_ability
            max_delta = max(max_delta, abs(new_ability - ability_i) / max(ability_i, 1e-12))
        abilities = updated
        abilities[anchor_name] = anchor_ability
        if max_delta < tol:
            break
    else:
        raise RuntimeError("BayesElo solver did not converge")

    ratings = {
        player: 400.0 * math.log10(max(ability, 1e-300))
        for player, ability in abilities.items()
    }
    offset = anchor_rating - ratings[anchor_name]
    return {player: rating + offset for player, rating in ratings.items()}


def estimate_confidence_intervals(
    players: list[str],
    matches: list[MatchResult],
    ratings: dict[str, float],
    anchor_name: str,
) -> dict[str, tuple[float, float]]:
    free_players = [player for player in players if player != anchor_name]
    if not free_players:
        return {anchor_name: (ratings[anchor_name], ratings[anchor_name])}

    index = {player: i for i, player in enumerate(free_players)}
    info = [[0.0 for _ in free_players] for _ in free_players]
    for match in matches:
        ra = ratings[match.player_a]
        rb = ratings[match.player_b]
        p = 1.0 / (1.0 + 10.0 ** ((rb - ra) / 400.0))
        weight = match.games * LOGISTIC_SCALE * LOGISTIC_SCALE * p * (1.0 - p)
        a_free = match.player_a in index
        b_free = match.player_b in index
        if a_free:
            ia = index[match.player_a]
            info[ia][ia] += weight
        if b_free:
            ib = index[match.player_b]
            info[ib][ib] += weight
        if a_free and b_free:
            ia = index[match.player_a]
            ib = index[match.player_b]
            info[ia][ib] -= weight
            info[ib][ia] -= weight

    covariance = invert_matrix(info)
    ci: dict[str, tuple[float, float]] = {
        anchor_name: (ratings[anchor_name], ratings[anchor_name]),
    }
    for player, row_idx in index.items():
        variance = max(covariance[row_idx][row_idx], 0.0)
        delta = 1.96 * math.sqrt(variance)
        ci[player] = (ratings[player] - delta, ratings[player] + delta)
    return ci


def build_output(
    history: dict[str, float],
    matches: list[MatchResult],
    ratings: dict[str, float],
    ci: dict[str, tuple[float, float]],
    anchor_name: str,
    anchor_rating: float,
    games_per_match: int,
) -> dict[str, object]:
    per_player: dict[str, object] = {}
    for player, elo in ratings.items():
        if player == anchor_name:
            continue
        lo, hi = ci[player]
        entry: dict = {
            "elo": round(elo, 3),
            "ci95": [round(lo, 3), round(hi, 3)],
        }
        if player in history:
            entry["win_pct"] = history[player]
        per_player[player] = entry

    return {
        "anchor_player": anchor_name,
        "anchor_rating": anchor_rating,
        "games_per_match": games_per_match,
        "ratings": {
            anchor_name: {
                "elo": round(ratings[anchor_name], 3),
                "ci95": [round(ci[anchor_name][0], 3), round(ci[anchor_name][1], 3)],
            },
            **per_player,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--benchmark-history",
        type=Path,
        default=Path("results/benchmark_history.json"),
    )
    parser.add_argument(
        "--h2h-results",
        type=Path,
        default=None,
        help="Path to checkpoint_elo.json with head-to-head match history (optional)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("results/elo/elo_ratings.json"),
    )
    parser.add_argument(
        "--anchor-rating",
        type=float,
        default=1500.0,
    )
    parser.add_argument(
        "--games-per-match",
        type=int,
        default=200,
    )
    parser.add_argument(
        "--anchor-name",
        default="heuristic",
    )
    parser.add_argument(
        "--max-iter",
        type=int,
        default=10_000,
    )
    parser.add_argument(
        "--tol",
        type=float,
        default=1e-12,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.games_per_match <= 0:
        raise ValueError("--games-per-match must be positive")
    if args.max_iter <= 0:
        raise ValueError("--max-iter must be positive")
    if args.tol <= 0.0:
        raise ValueError("--tol must be positive")

    history = load_history(args.benchmark_history)
    matches = build_matches(history, args.games_per_match, args.anchor_name)

    # Optionally incorporate head-to-head model-vs-model results
    if args.h2h_results is not None and args.h2h_results.exists():
        h2h = load_h2h_matches(args.h2h_results)
        matches.extend(h2h)
        print(f"Added {len(h2h)} H2H match results from {args.h2h_results}")

    players = sorted({args.anchor_name, *(m.player_a for m in matches), *(m.player_b for m in matches)}, key=generation_sort_key)
    ratings = fit_bayes_elo_mm(
        players=players,
        matches=matches,
        anchor_name=args.anchor_name,
        anchor_rating=args.anchor_rating,
        max_iter=args.max_iter,
        tol=args.tol,
    )
    ci = estimate_confidence_intervals(players, matches, ratings, args.anchor_name)
    output = build_output(
        history=history,
        matches=matches,
        ratings=ratings,
        ci=ci,
        anchor_name=args.anchor_name,
        anchor_rating=args.anchor_rating,
        games_per_match=args.games_per_match,
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
