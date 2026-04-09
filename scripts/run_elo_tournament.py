#!/usr/bin/env python3
"""Model-vs-model BayesElo tournament for PPO checkpoints.

Exports checkpoints to TorchScript, runs head-to-head matches to form a
connected graph, then fits BayesElo ratings anchored to a reference model.

Usage:
    uv run python scripts/run_elo_tournament.py \
        --models v3:data/checkpoints/league_v4/iter_0200.pt \
                 v4:data/checkpoints/ppo_v4_league/ppo_best.pt \
                 v5:data/checkpoints/ppo_v5_league/ppo_best.pt \
                 v6:data/checkpoints/ppo_v6_league/ppo_best.pt \
                 v7:data/checkpoints/ppo_v7_league/ppo_best.pt \
        --games 500 --anchor v3 --anchor-elo 1500 \
        --out results/elo_ppo_ladder.json
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).parent.parent / "python"))
sys.path.insert(0, "build-ninja/bindings")
sys.path.insert(0, "build/bindings")

import tscore  # noqa: E402

sys.path.insert(0, str(Path(__file__).parent.parent))
from cpp.tools.export_baseline_to_torchscript import export_checkpoint  # noqa: E402

# ---------------------------------------------------------------------------
# BayesElo solver (anchored, iterative)
# ---------------------------------------------------------------------------

LOGISTIC_SCALE = math.log(10.0) / 400.0


@dataclass
class MatchResult:
    player_a: str
    player_b: str
    wins_a: int
    wins_b: int

    @property
    def games(self) -> int:
        return self.wins_a + self.wins_b


def bayeselo_fit(
    matches: list[MatchResult],
    anchor: str,
    anchor_elo: float = 1500.0,
    max_iter: int = 2000,
    tol: float = 1e-8,
) -> dict[str, float]:
    """Iterative MM (minorization-maximization) BayesElo solver."""
    players = sorted({m.player_a for m in matches} | {m.player_b for m in matches})
    idx = {p: i for i, p in enumerate(players)}
    n = len(players)
    ratings = [0.0] * n  # log-odds

    for _ in range(max_iter):
        new_ratings = ratings[:]
        for i, p in enumerate(players):
            if p == anchor:
                continue
            num = sum(
                m.wins_a for m in matches if m.player_a == p
            ) + sum(
                m.wins_b for m in matches if m.player_b == p
            )
            if num == 0:
                continue
            denom = 0.0
            for m in matches:
                if m.player_a == p or m.player_b == p:
                    opp = m.player_b if m.player_a == p else m.player_a
                    g = m.games
                    r_diff = ratings[i] - ratings[idx[opp]]
                    p_win = 1.0 / (1.0 + math.exp(-r_diff))
                    denom += g * p_win * (1 - p_win)
            if denom > 1e-12:
                # Newton step in log-odds space
                grad = num - sum(
                    m.games / (1.0 + math.exp(ratings[idx[m.player_b if m.player_a == p else m.player_a]] - ratings[i]))
                    for m in matches if m.player_a == p or m.player_b == p
                )
                new_ratings[i] = ratings[i] + grad / denom

        # Re-anchor: shift so anchor stays at 0 log-odds
        anchor_val = new_ratings[idx[anchor]]
        new_ratings = [r - anchor_val for r in new_ratings]
        delta = max(abs(new_ratings[i] - ratings[i]) for i in range(n))
        ratings = new_ratings
        if delta < tol:
            break

    # Convert log-odds → Elo
    elo_scale = 400.0 / math.log(10.0)
    return {p: anchor_elo + ratings[idx[p]] * elo_scale for p in players}


def bayeselo_ci95(
    matches: list[MatchResult],
    elos: dict[str, float],
    anchor: str,
) -> dict[str, tuple[float, float]]:
    """Approx 95% CI via Fisher information diagonal (Hessian inverse)."""
    players = sorted(elos.keys())
    idx = {p: i for i, p in enumerate(players)}
    n = len(players)
    elo_scale = 400.0 / math.log(10.0)

    # Build diagonal of Fisher info matrix (in log-odds space)
    fisher_diag = [0.0] * n
    for m in matches:
        i, j = idx[m.player_a], idx[m.player_b]
        r_diff = (elos[m.player_a] - elos[m.player_b]) / elo_scale
        p_win = 1.0 / (1.0 + math.exp(-r_diff))
        fisher_diag[i] += m.games * p_win * (1 - p_win)
        fisher_diag[j] += m.games * p_win * (1 - p_win)

    ci = {}
    z = 1.96  # 95%
    for p in players:
        if p == anchor or fisher_diag[idx[p]] < 1e-12:
            ci[p] = (elos[p], elos[p])
        else:
            se = elo_scale / math.sqrt(fisher_diag[idx[p]])
            ci[p] = (elos[p] - z * se, elos[p] + z * se)
    return ci


# ---------------------------------------------------------------------------
# Match running
# ---------------------------------------------------------------------------

def run_match(script_a: str, script_b: str, n_games: int, seed: int) -> MatchResult:
    """Run n_games head-to-head (half each side) and return wins."""
    results = tscore.benchmark_model_vs_model_batched(
        model_a_path=script_a,
        model_b_path=script_b,
        n_games=n_games,
        pool_size=min(64, n_games),
        seed=seed,
        device="cpu",
        temperature=0.0,
    )
    wins_a = sum(1 for r in results if r.winner == tscore.Side.USSR and results.index(r) < n_games // 2
                 or r.winner == tscore.Side.US and results.index(r) >= n_games // 2)
    # Simpler: use the GameResult winner field directly
    # First half: model_a=USSR wins if winner==USSR; second half: model_a=US wins if winner==US
    half = n_games // 2
    wins_a = 0
    wins_b = 0
    for i, r in enumerate(results):
        if i < half:
            # model_a = USSR
            if r.winner == tscore.Side.USSR:
                wins_a += 1
            elif r.winner == tscore.Side.US:
                wins_b += 1
        else:
            # model_a = US
            if r.winner == tscore.Side.US:
                wins_a += 1
            elif r.winner == tscore.Side.USSR:
                wins_b += 1
    return MatchResult(player_a="", player_b="", wins_a=wins_a, wins_b=wins_b)


def export_if_needed(checkpoint: Path, script_dir: Path, name: str) -> str:
    """Export checkpoint to TorchScript if it's not already scripted."""
    out = script_dir / f"{name}_scripted.pt"
    if out.exists():
        return str(out)
    # Check if checkpoint is already TorchScript
    try:
        torch.jit.load(str(checkpoint))
        print(f"  {name}: already TorchScript, using directly", flush=True)
        return str(checkpoint)
    except Exception:
        pass
    print(f"  Exporting {name} → {out} ...", flush=True)
    export_checkpoint(checkpoint, out)
    return str(out)


# ---------------------------------------------------------------------------
# Minimum spanning tree for match schedule
# ---------------------------------------------------------------------------

def chain_schedule(names: list[str]) -> list[tuple[str, str]]:
    """Simple chain: each model plays the next one. Guaranteed connected."""
    return [(names[i], names[i + 1]) for i in range(len(names) - 1)]


def round_robin_schedule(names: list[str]) -> list[tuple[str, str]]:
    """All pairs."""
    pairs = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pairs.append((names[i], names[j]))
    return pairs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--models", nargs="+", required=True,
        metavar="NAME:PATH",
        help="Models as name:path pairs, in ascending strength order (best last)"
    )
    p.add_argument("--games", type=int, default=500, help="Games per match (must be even)")
    p.add_argument("--anchor", required=True, help="Model name to anchor at --anchor-elo")
    p.add_argument("--anchor-elo", type=float, default=1500.0)
    p.add_argument("--schedule", choices=["chain", "round_robin"], default="chain")
    p.add_argument("--seed", type=int, default=88000)
    p.add_argument("--script-dir", type=Path, default=Path("data/checkpoints/scripted_for_elo"))
    p.add_argument("--out", type=Path, default=Path("results/elo_ppo_ladder.json"))
    args = p.parse_args()

    if args.games % 2 != 0:
        p.error("--games must be even (half played each side)")

    # Parse model name:path pairs
    models: dict[str, Path] = {}
    ordered_names: list[str] = []
    for spec in args.models:
        name, _, path = spec.partition(":")
        if not path:
            p.error(f"Invalid model spec {spec!r}, expected name:path")
        models[name] = Path(path)
        ordered_names.append(name)

    if args.anchor not in models:
        p.error(f"Anchor {args.anchor!r} not in model list")

    args.script_dir.mkdir(parents=True, exist_ok=True)

    # Export all checkpoints to TorchScript
    print("Exporting checkpoints to TorchScript ...", flush=True)
    scripts: dict[str, str] = {}
    for name, ckpt in models.items():
        scripts[name] = export_if_needed(ckpt, args.script_dir, name)

    # Build match schedule
    if args.schedule == "round_robin":
        schedule = round_robin_schedule(ordered_names)
    else:
        schedule = chain_schedule(ordered_names)

    print(f"\nMatch schedule ({len(schedule)} matches × {args.games} games each):", flush=True)
    for a, b in schedule:
        print(f"  {a} vs {b}", flush=True)

    # Run matches
    matches: list[MatchResult] = []
    match_log = []
    for i, (name_a, name_b) in enumerate(schedule):
        seed = args.seed + i * args.games
        t0 = time.time()
        print(f"\n[{i+1}/{len(schedule)}] {name_a} vs {name_b} ({args.games} games, seed={seed}) ...", flush=True)
        m = run_match(scripts[name_a], scripts[name_b], args.games, seed)
        m = MatchResult(player_a=name_a, player_b=name_b, wins_a=m.wins_a, wins_b=m.wins_b)
        draws = args.games - m.wins_a - m.wins_b
        elapsed = time.time() - t0
        wr_a = m.wins_a / args.games
        print(f"  {name_a} wins: {m.wins_a}  {name_b} wins: {m.wins_b}  draws: {draws}  "
              f"WR({name_a})={wr_a:.3f}  t={elapsed:.1f}s", flush=True)
        matches.append(m)
        match_log.append({
            "model_a": name_a, "model_b": name_b,
            "n_games": args.games, "seed": seed,
            "wins_a": m.wins_a, "wins_b": m.wins_b, "draws": draws,
            "wr_a": round(wr_a, 4),
        })

    # Compute BayesElo
    print("\nFitting BayesElo ...", flush=True)
    elos = bayeselo_fit(matches, anchor=args.anchor, anchor_elo=args.anchor_elo)
    cis = bayeselo_ci95(matches, elos, anchor=args.anchor)

    # Sort by Elo descending
    ranked = sorted(elos.items(), key=lambda x: -x[1])

    print(f"\n{'Model':<20} {'Elo':>6}  {'95% CI':>20}  {'vs anchor':>10}")
    print("-" * 65)
    for name, elo in ranked:
        lo, hi = cis[name]
        diff = elo - args.anchor_elo
        print(f"{name:<20} {elo:>6.0f}  [{lo:>6.0f}, {hi:>6.0f}]  {diff:>+.0f}")

    # Save results
    out_data = {
        "anchor": args.anchor,
        "anchor_elo": args.anchor_elo,
        "games_per_match": args.games,
        "schedule": args.schedule,
        "ratings": {
            name: {
                "elo": round(elo, 1),
                "ci95": [round(cis[name][0], 1), round(cis[name][1], 1)],
                "delta_vs_anchor": round(elo - args.anchor_elo, 1),
            }
            for name, elo in ranked
        },
        "matches": match_log,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out_data, indent=2))
    print(f"\nSaved to {args.out}", flush=True)


if __name__ == "__main__":
    main()
