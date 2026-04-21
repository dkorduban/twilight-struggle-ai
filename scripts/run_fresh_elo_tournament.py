#!/usr/bin/env python3
"""Fresh per-side Elo tournament with CPU-saturating parallelism.

Re-anchors the Elo table using the heuristic-as-USSR = 1200 convention under bid+2.
Runs missing matchups across a curated 14-candidate panel in parallel worker
processes (each worker pinned to 1 torch thread for optimal throughput).

Usage:
    uv run python scripts/run_fresh_elo_tournament.py --games 200 --workers 18
    uv run python scripts/run_fresh_elo_tournament.py --dry-run  # just list plan
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "python"))

from tsrl.checkpoint_db import load_match_cache, save_match_cache  # noqa: E402


SCRIPTED_DIR = REPO_ROOT / "data/checkpoints/scripted_for_elo"
HEURISTIC_SENTINEL = "heuristic"


# Candidate panel (name, scripted path, tier, description)
CANDIDATES: list[tuple[str, str, str, str]] = [
    ("heuristic",          HEURISTIC_SENTINEL,                               "anchor",   "built-in heuristic, USSR side anchored at 1200"),
    ("bc_wide384",         str(SCRIPTED_DIR / "bc_wide384_scripted.pt"),     "bc",       "BC baseline (hidden_dim=384)"),
    ("v44",                str(SCRIPTED_DIR / "v44_scripted.pt"),            "league",   "old league v44 (pre-chain)"),
    ("v55",                str(SCRIPTED_DIR / "v55_scripted.pt"),            "league",   "old league v55 (pre-chain)"),
    ("v56",                str(SCRIPTED_DIR / "v56_scripted.pt"),            "league",   "old league v56 (chain warm-start root)"),
    ("v22_bugfix_full",    str(SCRIPTED_DIR / "v22_bugfix_full_scripted.pt"),"chain",    "chain iter40, 0.466 combined"),
    ("v25_continue",       str(SCRIPTED_DIR / "v25_continue_scripted.pt"),   "chain",    "chain iter26, 0.584 combined"),
    ("v27_continue",       str(SCRIPTED_DIR / "v27_continue_scripted.pt"),   "chain",    "chain iter30, 0.608 combined"),
    ("v29_continue",       str(SCRIPTED_DIR / "v29_continue_scripted.pt"),   "chain",    "chain iter30, 0.624 combined"),
    ("v31_continue",       str(SCRIPTED_DIR / "v31_continue_scripted.pt"),   "chain",    "chain iter20, 0.645 combined"),
    ("v32_continue",       str(SCRIPTED_DIR / "v32_continue_scripted.pt"),   "chain",    "chain iter20, 0.650 combined (RECORD)"),
    ("v33_continue",       str(SCRIPTED_DIR / "v33_continue_scripted.pt"),   "chain",    "chain iter10/20, 0.631-0.635 (post-peak)"),
    ("ussr_only_v5",       str(SCRIPTED_DIR / "ussr_only_v5_scripted.pt"),   "capacity", "USSR-only side specialist"),
    ("us_only_v5",         str(SCRIPTED_DIR / "us_only_v5_scripted.pt"),     "capacity", "US-only side specialist"),
]


# Real heuristic-vs-heuristic result from the 2000-game run (bid+2, greedy).
# Cache entry injected explicitly so the stub 50/50 does not contaminate the fit.
# From /tmp/heur_vs_heur.jsonl: 1439 USSR wins, 561 US wins across 2000 games.
# Split symmetrically: first 1000 games a=USSR, second 1000 games a=US.
HEUR_HEUR_INJECT = {
    "model_a": "heuristic", "model_b": "heuristic",
    "wins_a": 1000, "wins_b": 1000,   # symmetric (both are the same player)
    "wins_a_ussr": 720, "wins_b_us": 280,    # first half: a=USSR, heuristic wins 72%
    "wins_a_us": 280, "wins_b_ussr": 720,    # second half: a=US
    "n_games": 2000, "seed": 50000, "draws": 0,
}


@dataclass
class MatchTask:
    name_a: str
    path_a: str
    name_b: str
    path_b: str
    n_games: int
    seed: int
    tier: str  # priority tag


def _worker_setup_thread_caps() -> None:
    """Pin the worker process to 1 CPU thread before importing torch."""
    os.environ["OMP_NUM_THREADS"] = "1"
    os.environ["MKL_NUM_THREADS"] = "1"
    os.environ["OPENBLAS_NUM_THREADS"] = "1"
    os.environ["OMP_WAIT_POLICY"] = "passive"
    os.environ["KMP_BLOCKTIME"] = "0"


def _worker_run_match(task: MatchTask) -> dict:
    """Run one match in an isolated subprocess, return a dict ready for save_match_cache."""
    _worker_setup_thread_caps()
    import sys as _sys
    _sys.path.insert(0, "build-ninja/bindings")
    import torch  # noqa: E402
    torch.set_num_threads(1)
    import tscore  # noqa: E402

    t0 = time.time()
    half = task.n_games // 2

    # Heuristic-vs-heuristic handled outside; we should not receive such a task.
    if task.path_a == HEURISTIC_SENTINEL and task.path_b == HEURISTIC_SENTINEL:
        raise RuntimeError("heur-vs-heur should be injected from real data, not scheduled")

    if task.path_a == HEURISTIC_SENTINEL:
        # a=heuristic, b=model
        r_ussr = tscore.benchmark_batched(task.path_b, tscore.Side.USSR, half,
                                          pool_size=min(32, half), seed=task.seed)
        r_us = tscore.benchmark_batched(task.path_b, tscore.Side.US, half,
                                        pool_size=min(32, half), seed=task.seed + half)
        # First half: a=US (heuristic), b=USSR (model)
        # Interpretation of r_ussr: model plays USSR, heuristic plays US.
        wins_b_ussr = sum(1 for r in r_ussr if r.winner == tscore.Side.USSR)
        wins_a_us = sum(1 for r in r_ussr if r.winner == tscore.Side.US)
        # r_us: model plays US, heuristic plays USSR.
        wins_b_us = sum(1 for r in r_us if r.winner == tscore.Side.US)
        wins_a_ussr = sum(1 for r in r_us if r.winner == tscore.Side.USSR)

    elif task.path_b == HEURISTIC_SENTINEL:
        # b=heuristic, a=model
        r_ussr = tscore.benchmark_batched(task.path_a, tscore.Side.USSR, half,
                                          pool_size=min(32, half), seed=task.seed)
        r_us = tscore.benchmark_batched(task.path_a, tscore.Side.US, half,
                                        pool_size=min(32, half), seed=task.seed + half)
        wins_a_ussr = sum(1 for r in r_ussr if r.winner == tscore.Side.USSR)
        wins_b_us = sum(1 for r in r_ussr if r.winner == tscore.Side.US)
        wins_a_us = sum(1 for r in r_us if r.winner == tscore.Side.US)
        wins_b_ussr = sum(1 for r in r_us if r.winner == tscore.Side.USSR)

    else:
        # model vs model
        results = tscore.benchmark_model_vs_model_batched(
            model_a_path=task.path_a,
            model_b_path=task.path_b,
            n_games=task.n_games,
            pool_size=min(32, task.n_games),
            seed=task.seed,
            device="cpu",
            temperature=0.0,
        )
        wins_a_ussr = 0
        wins_b_us = 0
        wins_a_us = 0
        wins_b_ussr = 0
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

    elapsed = time.time() - t0
    return {
        "model_a": task.name_a,
        "model_b": task.name_b,
        "wins_a": wins_a, "wins_b": wins_b, "draws": 0,
        "wins_a_ussr": wins_a_ussr, "wins_b_ussr": wins_b_ussr,
        "wins_a_us": wins_a_us, "wins_b_us": wins_b_us,
        "n_games": task.n_games,
        "seed": task.seed,
        "_elapsed_s": round(elapsed, 1),
    }


def tier_priority(tier_a: str, tier_b: str) -> int:
    """Lower = higher priority. Chain peer-vs-peer is most informative."""
    order = {
        ("chain", "chain"): 0,
        ("chain", "anchor"): 1, ("anchor", "chain"): 1,
        ("chain", "capacity"): 2, ("capacity", "chain"): 2,
        ("chain", "bc"): 3, ("bc", "chain"): 3,
        ("chain", "league"): 4, ("league", "chain"): 4,
        ("capacity", "anchor"): 5, ("anchor", "capacity"): 5,
        ("capacity", "bc"): 6, ("bc", "capacity"): 6,
        ("capacity", "capacity"): 7,
        ("bc", "anchor"): 8, ("anchor", "bc"): 8,
        ("bc", "bc"): 9,
        ("anchor", "anchor"): 10,
    }
    return order.get((tier_a, tier_b), 20)


def build_task_list(n_games: int, chain_peer_games: int) -> list[MatchTask]:
    """Enumerate all (i,j) pairs including diagonals, skip pairs already in cache."""
    cache = load_match_cache()
    tasks: list[MatchTask] = []
    seed_base = 70000  # fresh seed namespace for this tournament

    name_to_path = {n: p for n, p, _, _ in CANDIDATES}
    name_to_tier = {n: t for n, _, t, _ in CANDIDATES}

    names = [n for n, _, _, _ in CANDIDATES]
    pairs = []
    for i in range(len(names)):
        for j in range(i, len(names)):
            pairs.append((names[i], names[j]))

    for idx, (a, b) in enumerate(pairs):
        key = frozenset([a, b])
        if key in cache and cache[key]["n_games"] >= n_games:
            continue  # already have enough data
        if a == HEURISTIC_SENTINEL and b == HEURISTIC_SENTINEL:
            continue  # inject real data separately
        tier_a, tier_b = name_to_tier[a], name_to_tier[b]
        games = chain_peer_games if (tier_a == "chain" and tier_b == "chain") else n_games
        tasks.append(MatchTask(
            name_a=a, path_a=name_to_path[a],
            name_b=b, path_b=name_to_path[b],
            n_games=games,
            seed=seed_base + idx * 1000,
            tier=f"{tier_a}x{tier_b}",
        ))

    # Sort by priority: chain peer-vs-peer first, then chain-anchor, etc.
    tasks.sort(key=lambda t: tier_priority(*t.tier.split("x")))
    return tasks


def verify_scripted_files() -> tuple[list[str], list[str]]:
    """Return (ok, missing) scripted checkpoint paths."""
    ok, missing = [], []
    for name, path, _, _ in CANDIDATES:
        if path == HEURISTIC_SENTINEL:
            ok.append(name)
            continue
        if Path(path).exists():
            ok.append(name)
        else:
            missing.append(f"{name}: {path}")
    return ok, missing


def fit_per_side_elo(cache: dict, anchor_side_rating: float = 1200.0) -> dict:
    """Fit per-side Elo with anchor heuristic-USSR=1200.

    Each (model, side) pair gets an independent rating. We treat side-assignment
    as encoded in wins_a_ussr/wins_a_us/wins_b_ussr/wins_b_us.

    Returns dict: {model_name: {"USSR": rating, "US": rating, "combined": avg}}
    """
    import numpy as np
    from scipy.optimize import minimize

    # Index: (model, side) -> idx
    all_players: set[tuple[str, str]] = set()
    observations: list[tuple[int, int, int, int]] = []  # (idx_winner_side, idx_loser_side, n_wins)

    # Build (p_ussr_idx, p_us_idx, wins_ussr, wins_us) triplets from every entry
    for key, entry in cache.items():
        a = entry["model_a"]
        b = entry["model_b"]
        # First half: a=USSR, b=US
        all_players.add((a, "USSR"))
        all_players.add((b, "US"))
        # Second half: a=US, b=USSR
        all_players.add((a, "US"))
        all_players.add((b, "USSR"))

    players = sorted(all_players)
    idx = {p: i for i, p in enumerate(players)}
    n = len(players)

    # For fitting: accumulate (i, j, w_i, w_j) pairs where i and j played
    # and i won w_i, j won w_j in that sub-series.
    pair_counts: dict[tuple[int, int], list[int]] = {}  # (i,j) -> [wi, wj]

    def add(i: int, j: int, wi: int, wj: int) -> None:
        key = (min(i, j), max(i, j))
        flip = (i > j)
        if flip:
            wi, wj = wj, wi
        pair_counts.setdefault(key, [0, 0])
        pair_counts[key][0] += wi
        pair_counts[key][1] += wj

    for entry in cache.values():
        a = entry["model_a"]
        b = entry["model_b"]
        wa_ussr = entry.get("wins_a_ussr") or 0
        wb_ussr = entry.get("wins_b_ussr") or 0
        wa_us = entry.get("wins_a_us") or 0
        wb_us = entry.get("wins_b_us") or 0

        # First half: a=USSR, b=US. a-ussr vs b-us, wa_ussr wins for a-USSR, wb_us wins for b-US.
        i1 = idx[(a, "USSR")]
        j1 = idx[(b, "US")]
        add(i1, j1, wa_ussr, wb_us)

        # Second half: a=US, b=USSR. a-us vs b-ussr.
        i2 = idx[(a, "US")]
        j2 = idx[(b, "USSR")]
        add(i2, j2, wa_us, wb_ussr)

    pair_list = [(i, j, wins[0], wins[1]) for (i, j), wins in pair_counts.items()]

    LOG10 = math.log(10.0)
    SCALE = LOG10 / 400.0

    anchor_idx = idx.get(("heuristic", "USSR"))
    if anchor_idx is None:
        raise RuntimeError("heuristic USSR player not found in cache — cannot anchor")

    def nll(x: "np.ndarray") -> float:
        # x has n-1 free params; x[anchor_idx] is implicit 0.
        r = np.zeros(n)
        free_mask = np.ones(n, dtype=bool)
        free_mask[anchor_idx] = False
        r[free_mask] = x

        total = 0.0
        for i, j, wi, wj in pair_list:
            d = r[i] - r[j]
            d = max(-700.0, min(700.0, d))
            p_i = 1.0 / (1.0 + math.exp(-d))
            p_j = 1.0 - p_i
            if wi > 0:
                total -= wi * math.log(max(p_i, 1e-300))
            if wj > 0:
                total -= wj * math.log(max(p_j, 1e-300))
        # L2 prior to prevent unbounded drift for undetermined params
        total += 0.001 * float(np.sum(r ** 2))
        return total

    x0 = np.zeros(n - 1)
    res = minimize(nll, x0, method="L-BFGS-B", options={"maxiter": 2000, "ftol": 1e-9})

    r = np.zeros(n)
    free_mask = np.ones(n, dtype=bool)
    free_mask[anchor_idx] = False
    r[free_mask] = res.x

    # Convert log-odds to Elo: Elo = anchor + (r - r_anchor) / SCALE
    elo_per_player: dict[tuple[str, str], float] = {}
    for p, i in idx.items():
        elo_per_player[p] = anchor_side_rating + (r[i] - r[anchor_idx]) / SCALE

    # Aggregate
    agg: dict[str, dict[str, float]] = {}
    models = sorted({m for m, _ in players})
    for m in models:
        ussr = elo_per_player.get((m, "USSR"))
        us = elo_per_player.get((m, "US"))
        combined = None
        if ussr is not None and us is not None:
            combined = (ussr + us) / 2.0
        agg[m] = {"USSR": ussr, "US": us, "combined": combined}
    return agg


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=200, help="standard games per match")
    ap.add_argument("--chain-peer-games", type=int, default=400,
                    help="games for chain-vs-chain pairs (more power needed)")
    ap.add_argument("--workers", type=int, default=18,
                    help="parallel worker processes (CPU count is 20)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-heur-inject", action="store_true",
                    help="do not overwrite heur-heur cache entry with real 2000g data")
    ap.add_argument("--out", type=str, default="results/elo/elo_fresh_panel.json")
    args = ap.parse_args()

    print("=== Fresh Elo Tournament ===", flush=True)
    print(f"Candidates: {len(CANDIDATES)}", flush=True)
    for name, path, tier, desc in CANDIDATES:
        exists = "✓" if path == HEURISTIC_SENTINEL or Path(path).exists() else "✗"
        print(f"  {exists} [{tier:8s}] {name:22s} — {desc}", flush=True)
    ok, missing = verify_scripted_files()
    if missing:
        print("\nMISSING scripted files:", flush=True)
        for m in missing:
            print(f"  {m}", flush=True)
        print("Cannot proceed — export them first.", flush=True)
        sys.exit(1)

    # Inject real heur-vs-heur data
    if not args.skip_heur_inject:
        print("\nInjecting real heur-vs-heur (2000 games): 1439 USSR wins / 561 US wins", flush=True)
        if not args.dry_run:
            save_match_cache(HEUR_HEUR_INJECT)

    # Build task list
    tasks = build_task_list(args.games, args.chain_peer_games)
    print(f"\nTasks to run: {len(tasks)}", flush=True)
    total_games = sum(t.n_games for t in tasks)
    print(f"Total games: {total_games}", flush=True)
    est_throughput_gps = max(1, args.workers) * 20  # ~20 g/s per worker
    eta_min = total_games / est_throughput_gps / 60.0
    print(f"Estimated time: ~{eta_min:.1f} min at ~{est_throughput_gps} g/s ({args.workers} workers × 20 g/s)", flush=True)
    print("\nTop 10 tasks by priority:", flush=True)
    for t in tasks[:10]:
        print(f"  [{t.tier:20s}] {t.name_a:22s} vs {t.name_b:22s}  ({t.n_games} games)", flush=True)
    if len(tasks) > 10:
        print(f"  ... and {len(tasks) - 10} more", flush=True)

    if args.dry_run:
        print("\n--dry-run: not executing", flush=True)
        return

    # Kick off workers
    print(f"\n=== Running {len(tasks)} matches across {args.workers} workers ===", flush=True)
    import multiprocessing as mp
    ctx = mp.get_context("spawn")
    t_start = time.time()
    completed = 0
    failures: list[tuple[str, str, str]] = []
    with ProcessPoolExecutor(max_workers=args.workers, mp_context=ctx) as pool:
        fut_to_task = {pool.submit(_worker_run_match, t): t for t in tasks}
        for fut in as_completed(fut_to_task):
            t = fut_to_task[fut]
            try:
                entry = fut.result()
                save_match_cache(entry)
                completed += 1
                elapsed = entry.pop("_elapsed_s", "?")
                frac_a = entry["wins_a"] / max(1, entry["n_games"])
                print(f"[{completed:3d}/{len(tasks)}] {t.name_a:22s} vs {t.name_b:22s}  "
                      f"{entry['wins_a']:>3d}-{entry['wins_b']:<3d}  "
                      f"(a_WR={frac_a:.3f}, {elapsed}s)", flush=True)
            except Exception as e:
                failures.append((t.name_a, t.name_b, repr(e)))
                print(f"[FAIL] {t.name_a} vs {t.name_b}: {e}", flush=True)

    total_elapsed = time.time() - t_start
    print(f"\nAll matches done in {total_elapsed/60:.1f} min", flush=True)
    if failures:
        print(f"\n{len(failures)} failures:", flush=True)
        for a, b, err in failures:
            print(f"  {a} vs {b}: {err}", flush=True)

    # Fit per-side Elo
    print("\n=== Fitting per-side Elo (anchor: heuristic-USSR = 1200) ===", flush=True)
    cache = load_match_cache()
    candidate_names = {n for n, _, _, _ in CANDIDATES}
    filtered = {k: v for k, v in cache.items() if {v["model_a"], v["model_b"]}.issubset(candidate_names)}
    print(f"Using {len(filtered)} cached matchups within candidate panel", flush=True)
    try:
        elos = fit_per_side_elo(filtered)
    except Exception as e:
        print(f"Elo fit failed: {e}", flush=True)
        elos = {}

    # Print table sorted by combined Elo
    print("\n=== Per-side Elo table ===", flush=True)
    print(f"{'model':25s}  {'USSR':>7s}  {'US':>7s}  {'combined':>9s}  {'delta':>7s}", flush=True)
    print("-" * 65, flush=True)
    rows = sorted(
        ((m, d) for m, d in elos.items() if d["combined"] is not None),
        key=lambda x: -x[1]["combined"]
    )
    for m, d in rows:
        delta = (d["USSR"] or 0) - (d["US"] or 0)
        print(f"{m:25s}  {d['USSR']:>7.1f}  {d['US']:>7.1f}  {d['combined']:>9.1f}  {delta:>+7.1f}", flush=True)

    # Persist
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "anchor": "heuristic-USSR=1200",
        "bid": "+2 (human openings)",
        "n_candidates": len(CANDIDATES),
        "n_matches_used": len(filtered),
        "ratings": {m: d for m, d in elos.items()},
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"\nWrote {out_path}", flush=True)


if __name__ == "__main__":
    main()
