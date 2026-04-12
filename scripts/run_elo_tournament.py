#!/usr/bin/env python3
"""Model-vs-model BayesElo tournament for PPO checkpoints.

Exports checkpoints to TorchScript, runs head-to-head matches to form a
connected graph, then fits BayesElo ratings anchored to a reference model.
Three separate ratings are computed: combined, USSR-side, and US-side.

Usage (full tournament):
    uv run python scripts/run_elo_tournament.py \
        --models v12:data/checkpoints/ppo_v12_league/ppo_best.pt \
                 v13:data/checkpoints/ppo_v13_league/ppo_final.pt \
        --games 400 --anchor v12 --anchor-elo 2001 \
        --schedule round_robin --out results/elo/elo_ppo_ladder.json

Usage (add new candidate, reuse existing results):
    uv run python scripts/run_elo_tournament.py \
        --models v12:... v13:... v14:data/checkpoints/ppo_v14_league/ppo_final.pt \
        --games 400 --anchor v12 --anchor-elo 2001 \
        --schedule round_robin \
        --resume-from results/elo/elo_ppo_ladder.json \
        --out results/elo/elo_ppo_ladder.json
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
    wins_a: int           # combined wins (both sides)
    wins_b: int           # combined wins (both sides)
    wins_a_ussr: int = 0  # wins when model_a played USSR
    wins_b_ussr: int = 0  # wins when model_b played USSR
    wins_a_us: int = 0    # wins when model_a played US
    wins_b_us: int = 0    # wins when model_b played US

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
                    r_diff = max(-700, min(700, r_diff))  # clamp to avoid exp overflow
                    p_win = 1.0 / (1.0 + math.exp(-r_diff))
                    denom += g * p_win * (1 - p_win)
            if denom > 1e-12:
                # Newton step in log-odds space
                grad = num - sum(
                    m.games / (1.0 + math.exp(max(-700, min(700, ratings[idx[m.player_b if m.player_a == p else m.player_a]] - ratings[i]))))
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


def bayeselo_fit_mm(
    matches: list[MatchResult],
    anchor: str,
    anchor_elo: float = 1500.0,
    max_iter: int = 5000,
    tol: float = 1e-10,
) -> dict[str, float]:
    """MM (minorization-maximization) BayesElo solver in gamma-space.

    Unlike the Newton-step solver in bayeselo_fit(), this is provably convergent
    for any connected comparison graph (Hunter 2004), including bipartite graphs
    where the Newton diagonal Hessian approximation diverges.
    """
    players = sorted({m.player_a for m in matches} | {m.player_b for m in matches})
    idx = {p: i for i, p in enumerate(players)}
    n = len(players)
    gamma = [1.0] * n  # strength parameters (positive reals)
    anchor_idx = idx[anchor]

    # Pre-compute per-player match lists for efficiency
    player_matches: list[list[tuple[int, int, int]]] = [[] for _ in range(n)]
    player_wins: list[float] = [0.0] * n
    for m in matches:
        ia, ib = idx[m.player_a], idx[m.player_b]
        g = m.games
        player_matches[ia].append((ib, g, 0))
        player_matches[ib].append((ia, g, 0))
        player_wins[ia] += m.wins_a
        player_wins[ib] += m.wins_b

    for iteration in range(max_iter):
        new_gamma = gamma[:]
        for i in range(n):
            if i == anchor_idx:
                continue
            w_i = player_wins[i]
            if w_i < 1e-15:
                new_gamma[i] = 1e-10
                continue
            denom = 0.0
            for opp_idx, g, _ in player_matches[i]:
                denom += g / (gamma[i] + gamma[opp_idx])
            if denom > 1e-15:
                new_gamma[i] = w_i / denom

        # Rescale so anchor gamma = 1.0
        scale = 1.0 / max(new_gamma[anchor_idx], 1e-300)
        new_gamma = [g * scale for g in new_gamma]

        # Check convergence in log-space
        delta = max(
            abs(math.log(max(new_gamma[i], 1e-300)) - math.log(max(gamma[i], 1e-300)))
            for i in range(n)
        )
        gamma = new_gamma
        if delta < tol:
            break

    # Convert gamma → Elo
    elo_scale = 400.0 / math.log(10.0)
    return {
        p: anchor_elo + math.log(max(gamma[idx[p]], 1e-300)) * elo_scale
        for p in players
    }


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
        r_diff = max(-700, min(700, r_diff))
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

HEURISTIC_SENTINEL = "heuristic"


def _run_heuristic_match(model_script: str, n_games: int, seed: int) -> tuple[int, int, int, int, int, int]:
    """Benchmark model vs built-in heuristic.

    Returns (model_wins_as_ussr, heuristic_wins_as_us,
             model_wins_as_us, heuristic_wins_as_ussr,
             model_wins_total, heuristic_wins_total).
    """
    half = n_games // 2
    ussr_results = tscore.benchmark_batched(
        model_script, tscore.Side.USSR, half, pool_size=min(32, half), seed=seed,
    )
    us_results = tscore.benchmark_batched(
        model_script, tscore.Side.US, half, pool_size=min(32, half), seed=seed + half,
    )
    model_wins_as_ussr = sum(1 for r in ussr_results if r.winner == tscore.Side.USSR)
    heuristic_wins_as_us = sum(1 for r in ussr_results if r.winner == tscore.Side.US)
    model_wins_as_us = sum(1 for r in us_results if r.winner == tscore.Side.US)
    heuristic_wins_as_ussr = sum(1 for r in us_results if r.winner == tscore.Side.USSR)
    model_wins = model_wins_as_ussr + model_wins_as_us
    heuristic_wins = heuristic_wins_as_us + heuristic_wins_as_ussr
    return (model_wins_as_ussr, heuristic_wins_as_us,
            model_wins_as_us, heuristic_wins_as_ussr,
            model_wins, heuristic_wins)


def run_match(script_a: str, script_b: str, n_games: int, seed: int) -> MatchResult:
    """Run n_games head-to-head (half each side) and return wins with per-side breakdown.

    Either script may be HEURISTIC_SENTINEL to use the built-in heuristic player.
    """
    half = n_games // 2

    if script_a == HEURISTIC_SENTINEL and script_b == HEURISTIC_SENTINEL:
        return MatchResult(
            player_a="", player_b="",
            wins_a=half, wins_b=half,
            wins_a_ussr=half // 2, wins_b_ussr=half // 2,
            wins_a_us=half - half // 2, wins_b_us=half - half // 2,
        )

    if script_a == HEURISTIC_SENTINEL:
        (b_ussr, h_us, b_us, h_ussr, b_total, h_total) = _run_heuristic_match(script_b, n_games, seed)
        return MatchResult(
            player_a="", player_b="",
            wins_a=h_total, wins_b=b_total,
            wins_a_ussr=h_ussr, wins_b_ussr=b_ussr,
            wins_a_us=h_us, wins_b_us=b_us,
        )

    if script_b == HEURISTIC_SENTINEL:
        (a_ussr, h_us, a_us, h_ussr, a_total, h_total) = _run_heuristic_match(script_a, n_games, seed)
        return MatchResult(
            player_a="", player_b="",
            wins_a=a_total, wins_b=h_total,
            wins_a_ussr=a_ussr, wins_b_ussr=h_ussr,
            wins_a_us=a_us, wins_b_us=h_us,
        )

    # Model vs model
    results = tscore.benchmark_model_vs_model_batched(
        model_a_path=script_a,
        model_b_path=script_b,
        n_games=n_games,
        pool_size=min(64, n_games),
        seed=seed,
        device="cpu",
        temperature=0.0,
    )
    # First half: model_a=USSR, model_b=US
    # Second half: model_a=US, model_b=USSR
    wins_a_ussr = 0
    wins_b_us = 0    # model_b wins as US (when a=USSR)
    wins_a_us = 0
    wins_b_ussr = 0  # model_b wins as USSR (when a=US)

    for i, r in enumerate(results):
        if i < half:
            if r.winner == tscore.Side.USSR:
                wins_a_ussr += 1
            elif r.winner == tscore.Side.US:
                wins_b_us += 1
        else:
            if r.winner == tscore.Side.US:
                wins_a_us += 1
            elif r.winner == tscore.Side.USSR:
                wins_b_ussr += 1

    wins_a = wins_a_ussr + wins_a_us
    wins_b = wins_b_us + wins_b_ussr
    return MatchResult(
        player_a="", player_b="",
        wins_a=wins_a, wins_b=wins_b,
        wins_a_ussr=wins_a_ussr, wins_b_ussr=wins_b_ussr,
        wins_a_us=wins_a_us, wins_b_us=wins_b_us,
    )


def export_if_needed(checkpoint: Path, script_dir: Path, name: str) -> str:
    """Export checkpoint to TorchScript if it's not already scripted.

    Returns HEURISTIC_SENTINEL unchanged if checkpoint is 'heuristic'.
    """
    if str(checkpoint) == HEURISTIC_SENTINEL:
        print(f"  {name}: built-in heuristic (no export needed)", flush=True)
        return HEURISTIC_SENTINEL
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
# Bipartite per-side BayesElo
# ---------------------------------------------------------------------------

def _bipartite_matches(matches: list[MatchResult]) -> list[MatchResult]:
    """Build 2N-node bipartite match list for per-side BayesElo.

    Each checkpoint becomes two nodes: "{name}_USSR" and "{name}_US".
    Each match between model_a and model_b generates two sub-matches:
      - {model_a}_USSR vs {model_b}_US  (first half: a=USSR, b=US)
      - {model_b}_USSR vs {model_a}_US  (second half: a=US, b=USSR)

    A single anchor (e.g. "v12_USSR") is sufficient for the full 2N-node fit
    because USSR nodes and US nodes are connected through the bipartite graph.
    Anchoring both sides independently (as two separate pools did) is incorrect:
    it forces a different absolute scale onto each side.
    """
    out = []
    for m in matches:
        # First half: player_a played USSR, player_b played US
        if m.wins_a_ussr + m.wins_b_us > 0:
            out.append(MatchResult(
                player_a=f"{m.player_a}_USSR",
                player_b=f"{m.player_b}_US",
                wins_a=m.wins_a_ussr,
                wins_b=m.wins_b_us,
            ))
        # Second half: player_b played USSR, player_a played US
        if m.wins_b_ussr + m.wins_a_us > 0:
            out.append(MatchResult(
                player_a=f"{m.player_b}_USSR",
                player_b=f"{m.player_a}_US",
                wins_a=m.wins_b_ussr,
                wins_b=m.wins_a_us,
            ))
    return out


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
    p.add_argument("--games", type=int, default=400, help="Games per match (must be even; half each side)")
    p.add_argument("--anchor", required=True, help="Model name to anchor at --anchor-elo")
    p.add_argument("--anchor-elo", type=float, default=1500.0)
    p.add_argument("--schedule", choices=["chain", "round_robin"], default="chain")
    p.add_argument("--seed", type=int, default=88000)
    p.add_argument("--script-dir", type=Path, default=Path("data/checkpoints/scripted_for_elo"))
    p.add_argument("--out", type=Path, default=Path("results/elo/elo_ppo_ladder.json"))
    p.add_argument(
        "--resume-from", type=Path, default=None,
        help="JSON from a previous tournament run; reuse existing match results and only "
             "play missing pairs. Typically --resume-from and --out point to the same file.",
    )
    p.add_argument(
        "--match-cache-dir", type=Path, default=Path("results/matches"),
        help="Directory for per-pair match result files (one JSON per pair). "
             "Written after each match; never overwritten by unrelated tournament runs. "
             "Loaded before --resume-from so match history survives ladder resets. "
             "Default: results/matches/",
    )
    p.add_argument(
        "--mode", default=None,
        help="Tournament mode tag for SQL provenance (e.g. 'incremental', 'full', 'sanity'). "
             "Defaults to --schedule value if not set.",
    )
    p.add_argument(
        "--new-model", default=None,
        help="Name of the newly trained model being placed (for SQL provenance).",
    )
    args = p.parse_args()
    if args.mode is None:
        args.mode = args.schedule

    if args.games % 2 != 0:
        p.error("--games must be even (half played each side)")

    # Parse model name:path pairs.
    # Special: bare "heuristic" or "name:heuristic" uses the built-in heuristic player.
    models: dict[str, Path] = {}
    ordered_names: list[str] = []
    for spec in args.models:
        name, _, path = spec.partition(":")
        if not path:
            if name == HEURISTIC_SENTINEL:
                path = HEURISTIC_SENTINEL
            else:
                p.error(f"Invalid model spec {spec!r}, expected name:path")
        models[name] = Path(path)
        ordered_names.append(name)

    if args.anchor not in models:
        # Fall back: pick first fixture/model as anchor instead of failing
        print(f"WARNING: anchor {args.anchor!r} not in model list, using {ordered_names[0]!r} as anchor", flush=True)
        args.anchor = ordered_names[0]

    args.script_dir.mkdir(parents=True, exist_ok=True)

    # Export all checkpoints to TorchScript
    print("Exporting checkpoints to TorchScript ...", flush=True)
    scripts: dict[str, str] = {}
    for name, ckpt in models.items():
        scripts[name] = export_if_needed(ckpt, args.script_dir, name)

    # Load prior match results when resuming
    prior_matches: dict[frozenset, dict] = {}
    # Load per-pair match cache first (survives ladder resets).
    cache_dir: Path = args.match_cache_dir
    cache_loaded = 0
    if cache_dir.exists():
        for cache_file in sorted(cache_dir.glob("*.json")):
            try:
                entry = json.loads(cache_file.read_text())
                key = frozenset([entry["model_a"], entry["model_b"]])
                if key not in prior_matches:
                    prior_matches[key] = entry
                    cache_loaded += 1
            except Exception:
                pass
        if cache_loaded:
            print(f"Loaded {cache_loaded} match results from cache {cache_dir}/", flush=True)

    if args.resume_from is not None and args.resume_from.exists():
        prev = json.loads(args.resume_from.read_text())
        ladder_loaded = 0
        for entry in prev.get("matches", []):
            key = frozenset([entry["model_a"], entry["model_b"]])
            if key not in prior_matches:  # cache takes priority
                prior_matches[key] = entry
                ladder_loaded += 1
        if ladder_loaded:
            print(f"Loaded {ladder_loaded} additional match results from {args.resume_from}", flush=True)

    # Build match schedule
    if args.schedule == "round_robin":
        schedule = round_robin_schedule(ordered_names)
    else:
        schedule = chain_schedule(ordered_names)

    new_count = sum(1 for a, b in schedule if frozenset([a, b]) not in prior_matches)
    print(f"\nMatch schedule ({len(schedule)} total, {new_count} new, "
          f"{len(schedule) - new_count} reused from prior run):", flush=True)
    for a, b in schedule:
        tag = "" if frozenset([a, b]) not in prior_matches else "  [reuse]"
        print(f"  {a} vs {b}{tag}", flush=True)

    # Run matches (skip pairs already in prior_matches)
    matches: list[MatchResult] = []
    match_log = []
    new_idx = 0
    half = args.games // 2
    for name_a, name_b in schedule:
        pair_key = frozenset([name_a, name_b])
        if pair_key in prior_matches:
            entry = prior_matches[pair_key]
            if entry["model_a"] == name_a:
                wins_a, wins_b = entry["wins_a"], entry["wins_b"]
                wins_a_ussr = entry.get("wins_a_ussr", wins_a // 2)
                wins_b_ussr = entry.get("wins_b_ussr", wins_b // 2)
                wins_a_us = entry.get("wins_a_us", wins_a - wins_a_ussr)
                wins_b_us = entry.get("wins_b_us", wins_b - wins_b_ussr)
            else:
                wins_a, wins_b = entry["wins_b"], entry["wins_a"]
                wins_a_ussr = entry.get("wins_b_ussr", wins_a // 2)
                wins_b_ussr = entry.get("wins_a_ussr", wins_b // 2)
                wins_a_us = entry.get("wins_b_us", wins_a - wins_a_ussr)
                wins_b_us = entry.get("wins_a_us", wins_b - wins_b_ussr)

            m = MatchResult(
                player_a=name_a, player_b=name_b,
                wins_a=wins_a, wins_b=wins_b,
                wins_a_ussr=wins_a_ussr, wins_b_ussr=wins_b_ussr,
                wins_a_us=wins_a_us, wins_b_us=wins_b_us,
            )
            draws = entry.get("draws", args.games - wins_a - wins_b)
            n_games = entry.get("n_games", args.games)
            wr_a = (wins_a + 0.5 * draws) / n_games if n_games > 0 else 0.0
            print(f"  [reuse] {name_a} {wins_a}({wins_a_ussr}u/{wins_a_us}s) "
                  f"- {wins_b}({wins_b_ussr}u/{wins_b_us}s) {name_b}  draws={draws}  "
                  f"WR={wr_a:.3f}", flush=True)
            matches.append(m)
            match_log.append({
                "model_a": name_a, "model_b": name_b,
                "n_games": n_games,
                "seed": entry.get("seed", -1),
                "wins_a": wins_a, "wins_b": wins_b, "draws": draws,
                "wins_a_ussr": wins_a_ussr, "wins_b_ussr": wins_b_ussr,
                "wins_a_us": wins_a_us, "wins_b_us": wins_b_us,
                "wr_a": round(wr_a, 4),
                "reused": True,
            })
        else:
            seed = args.seed + new_idx * args.games
            new_idx += 1
            t0 = time.time()
            print(f"\n[new {new_idx}/{new_count}] {name_a} vs {name_b} "
                  f"({args.games} games = {half}/side, seed={seed}) ...", flush=True)
            m = run_match(scripts[name_a], scripts[name_b], args.games, seed)
            m = MatchResult(
                player_a=name_a, player_b=name_b,
                wins_a=m.wins_a, wins_b=m.wins_b,
                wins_a_ussr=m.wins_a_ussr, wins_b_ussr=m.wins_b_ussr,
                wins_a_us=m.wins_a_us, wins_b_us=m.wins_b_us,
            )
            draws = args.games - m.wins_a - m.wins_b
            elapsed = time.time() - t0
            wr_a = (m.wins_a + 0.5 * draws) / args.games if args.games > 0 else 0.0
            print(
                f"  {name_a}: {m.wins_a}({m.wins_a_ussr}u/{m.wins_a_us}s)  "
                f"{name_b}: {m.wins_b}({m.wins_b_ussr}u/{m.wins_b_us}s)  "
                f"draws: {draws}  WR({name_a})={wr_a:.3f}  t={elapsed:.1f}s",
                flush=True,
            )
            matches.append(m)
            entry = {
                "model_a": name_a, "model_b": name_b,
                "n_games": args.games, "seed": seed,
                "wins_a": m.wins_a, "wins_b": m.wins_b, "draws": draws,
                "wins_a_ussr": m.wins_a_ussr, "wins_b_ussr": m.wins_b_ussr,
                "wins_a_us": m.wins_a_us, "wins_b_us": m.wins_b_us,
                "wr_a": round(wr_a, 4),
            }
            match_log.append(entry)
            # Write to per-pair cache immediately so crash-recovery works.
            pair_name = "__vs__".join(sorted([name_a, name_b]))
            cache_dir.mkdir(parents=True, exist_ok=True)
            cache_file = cache_dir / f"{pair_name}.json"
            cache_file.write_text(json.dumps(entry, indent=2))

    # ---------------------------------------------------------------------------
    # Compute BayesElo: combined + bipartite per-side
    # ---------------------------------------------------------------------------
    print("\nFitting BayesElo (combined) ...", flush=True)
    elos = bayeselo_fit(matches, anchor=args.anchor, anchor_elo=args.anchor_elo)
    cis = bayeselo_ci95(matches, elos, anchor=args.anchor)

    # Bipartite per-side fit: 2N nodes ({name}_USSR, {name}_US), single anchor.
    # This is the mathematically correct formulation: USSR nodes only play US nodes,
    # so the graph is bipartite and requires exactly one anchor (not one per side).
    bipartite_mlist = _bipartite_matches(matches)
    bipartite_anchor = f"{args.anchor}_USSR"
    elos_bipartite: dict[str, float] = {}

    if len(bipartite_mlist) >= 2:
        print(f"Fitting BayesElo (bipartite per-side, anchor={bipartite_anchor}={args.anchor_elo}) ...", flush=True)
        elos_bipartite = bayeselo_fit_mm(bipartite_mlist, anchor=bipartite_anchor, anchor_elo=args.anchor_elo)
    else:
        print("  (skipping bipartite BayesElo: insufficient matches)", flush=True)

    def _belo(name: str, side: str) -> float | None:
        return elos_bipartite.get(f"{name}_{side}")

    # Sort by combined Elo descending
    ranked = sorted(elos.items(), key=lambda x: -x[1])

    # Print table
    print(f"\n{'Model':<20} {'Elo':>6}  {'USSR*':>7}  {'US*':>7}  {'Gap':>5}  {'95% CI':>20}  {'vs anchor':>10}")
    print(f"  (* bipartite per-side, single anchor: {bipartite_anchor}={args.anchor_elo:.0f})")
    print("-" * 88)
    for name, elo in ranked:
        lo, hi = cis[name]
        diff = elo - args.anchor_elo
        ussr_e = _belo(name, "USSR")
        us_e = _belo(name, "US")
        ussr_str = f"{ussr_e:>5.0f}" if ussr_e is not None else "  n/a"
        us_str = f"{us_e:>5.0f}" if us_e is not None else "  n/a"
        gap_str = f"{ussr_e - us_e:>+.0f}" if (ussr_e is not None and us_e is not None) else "  n/a"
        print(f"{name:<20} {elo:>6.0f}  {ussr_str}  {us_str}  {gap_str}  [{lo:>6.0f}, {hi:>6.0f}]  {diff:>+.0f}")

    # ---------------------------------------------------------------------------
    # WR residual table: observed vs bipartite-predicted vs combined-predicted
    # ---------------------------------------------------------------------------
    def _sigma(delta_elo: float) -> float:
        x = -delta_elo / 400.0
        x = max(-300, min(300, x))
        return 1.0 / (1.0 + 10.0 ** x)

    def _bipartite_wr(name_a: str, name_b: str) -> float | None:
        ua, va = _belo(name_a, "USSR"), _belo(name_a, "US")
        ub, vb = _belo(name_b, "USSR"), _belo(name_b, "US")
        if any(x is None for x in [ua, va, ub, vb]):
            return None
        return 0.5 * _sigma(ua - vb) + 0.5 * _sigma(va - ub)

    print(f"\n{'Pair':<32} {'Obs WR':>7}  {'Bip WR':>7}  {'Comb WR':>8}  {'Bip err':>8}  {'Comb err':>9}")
    print("-" * 84)
    bip_sq_err, comb_sq_err, n_pairs = 0.0, 0.0, 0
    for entry in match_log:
        na, nb = entry["model_a"], entry["model_b"]
        obs = entry["wr_a"]
        bip = _bipartite_wr(na, nb)
        comb = _sigma(elos.get(na, 0.0) - elos.get(nb, 0.0)) if na in elos and nb in elos else None
        bip_str = f"{bip:>7.3f}" if bip is not None else "    n/a"
        comb_str = f"{comb:>8.3f}" if comb is not None else "     n/a"
        bip_err = obs - bip if bip is not None else None
        comb_err = obs - comb if comb is not None else None
        bip_err_str = f"{bip_err:>+8.3f}" if bip_err is not None else "     n/a"
        comb_err_str = f"{comb_err:>+9.3f}" if comb_err is not None else "      n/a"
        print(f"{na:<14} vs {nb:<14} {obs:>7.3f}  {bip_str}  {comb_str}  {bip_err_str}  {comb_err_str}")
        if bip is not None and comb is not None:
            bip_sq_err += bip_err ** 2
            comb_sq_err += comb_err ** 2
            n_pairs += 1
    if n_pairs > 0:
        print("-" * 84)
        print(f"{'RMSE':>50}  {(bip_sq_err/n_pairs)**0.5:>8.4f}  {(comb_sq_err/n_pairs)**0.5:>9.4f}")
        print(f"  (bipartite RMSE {'<' if bip_sq_err < comb_sq_err else '>='} combined RMSE "
              f"→ bipartite model {'better' if bip_sq_err < comb_sq_err else 'not better'} fit)")

    # Save results
    ratings_out = {
        name: {
            "elo": round(elo, 1),
            "elo_ussr": round(_belo(name, "USSR"), 1) if _belo(name, "USSR") is not None else None,
            "elo_us": round(_belo(name, "US"), 1) if _belo(name, "US") is not None else None,
            "ci95": [round(cis[name][0], 1), round(cis[name][1], 1)],
            "delta_vs_anchor": round(elo - args.anchor_elo, 1),
        }
        for name, elo in ranked
    }
    out_data = {
        "anchor": args.anchor,
        "anchor_elo": args.anchor_elo,
        "bipartite_anchor": bipartite_anchor,
        "games_per_match": args.games,
        "games_per_side": half,
        "schedule": args.schedule,
        "ratings": ratings_out,
        "matches": match_log,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out_data, indent=2))
    print(f"\nSaved to {args.out}", flush=True)

    # Persist to SQL for provenance and cross-tournament aggregation.
    try:
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent / "python"))
        from tsrl.checkpoint_db import log_tournament, DB_PATH
        from datetime import datetime, timezone
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        # Infer which model is new: the one not in resume-from (or last alphabetically)
        new_model = getattr(args, "new_model", None)
        mode = getattr(args, "mode", args.schedule)
        tid = f"{mode}_{ts}_{'_'.join(sorted(scripts.keys())[:2])}"
        log_tournament(
            tournament_id=tid,
            mode=mode,
            models=list(scripts.keys()),
            anchor=args.anchor,
            anchor_elo=args.anchor_elo,
            games_per_match=args.games,
            match_log=match_log,
            ratings=ratings_out,
            new_model=new_model,
        )
        print(f"[sql] Tournament logged: {tid} → {DB_PATH}", flush=True)
    except Exception as _sql_err:
        print(f"[sql] WARNING: failed to log tournament to SQL: {_sql_err}", flush=True)


if __name__ == "__main__":
    main()
