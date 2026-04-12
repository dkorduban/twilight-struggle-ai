#!/usr/bin/env python3
"""Post-training candidate tournament for ppo_best.pt selection.

Reads panel_eval_history.json from a finished PPO run, picks the top-N
checkpoints by Elo-weighted panel combined WR, runs a round-robin tournament
among them using run_elo_tournament.py, and copies the Elo winner to
ppo_best.pt / ppo_best_scripted.pt.

Usage:
    uv run python scripts/ppo_confirm_best.py \\
        --run-dir data/checkpoints/ppo_v27_league \\
        --fixtures v8:data/checkpoints/scripted_for_elo/v8_scripted.pt \\
                   v14:data/checkpoints/scripted_for_elo/v14_scripted.pt \\
                   v22:data/checkpoints/scripted_for_elo/v22_scripted.pt \\
                   heuristic \\
        [--n-top 3] [--n-games 400] [--anchor v12] [--anchor-elo 2001]
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--run-dir", required=True,
                   help="PPO run directory (contains panel_eval_history.json)")
    p.add_argument("--fixtures", nargs="*", default=[],
                   help="Fixture models as 'name:path' pairs or 'heuristic'. "
                        "Included in tournament for absolute anchoring.")
    p.add_argument("--n-top", type=int, default=3,
                   help="Number of top panel-eval candidates to include (default: 3)")
    p.add_argument("--n-games", type=int, default=400,
                   help="Games per matchup in candidate tournament (default: 400)")
    p.add_argument("--anchor", type=str, default="v12",
                   help="Elo anchor model name (default: v12)")
    p.add_argument("--anchor-elo", type=float, default=2001.0,
                   help="Elo anchor value (default: 2001)")
    p.add_argument("--script-dir", type=str, default="data/checkpoints/scripted_for_elo",
                   help="Directory where scripted fixture models live")
    p.add_argument("--out-json", type=str, default=None,
                   help="Write tournament results to this path (default: <run-dir>/candidate_tournament.json)")
    p.add_argument("--dry-run", action="store_true",
                   help="Print what would be done without running the tournament")
    return p.parse_args()


def load_history(run_dir: str) -> dict:
    path = os.path.join(run_dir, "panel_eval_history.json")
    if not os.path.exists(path):
        print(f"ERROR: {path} not found. Was --eval-panel used during training?", file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def score_candidates(history: dict, run_dir: str, n_top: int) -> list[tuple[float, int, str]]:
    """Return top-N (weighted_avg_wr, iteration, scripted_path) sorted by score descending.

    Elo-weighted: frontier opponents contribute more to the score.
    Weights calibrated to Elo range: v22~2096 > v14~2015 > v8~1915 > heuristic~1751.
    Normalized over whichever opponents actually ran (some may error or be absent).
    """
    # Weights must match --eval-panel opponents in ppo_loop_step.sh.
    # 5-opponent pool (Opus rec 2026-04-12): v55+v54+v44+v45+v14, no heuristic.
    PANEL_WEIGHTS: dict[str, float] = {"v55": 0.35, "v54": 0.25, "v44": 0.20, "v45": 0.15, "v14": 0.05}

    scored = []
    for iter_str, res in history.items():
        it = int(iter_str)
        valid = {k: v for k, v in res.items() if "error" not in v}
        if not valid:
            continue
        wsum = sum(PANEL_WEIGHTS.get(k, 0.25) for k in valid)
        avg_wr = sum(v["combined_wr"] * PANEL_WEIGHTS.get(k, 0.25) for k, v in valid.items()) / wsum
        scripted = os.path.join(run_dir, f"ppo_iter{it:04d}_scripted.pt")
        if not os.path.exists(scripted):
            print(f"  [candidate] iter {it:04d}: scripted checkpoint missing, skipping", file=sys.stderr)
            continue
        scored.append((avg_wr, it, scripted))

    if not scored:
        print("ERROR: no valid panel eval results with existing scripted checkpoints.", file=sys.stderr)
        sys.exit(1)

    scored.sort(key=lambda x: -x[0])
    return scored[:n_top]


def main() -> None:
    args = parse_args()
    run_dir = args.run_dir
    out_json = args.out_json or os.path.join(run_dir, "candidate_tournament.json")

    history = load_history(run_dir)
    top = score_candidates(history, run_dir, args.n_top)

    print(f"\n[candidate] Top-{args.n_top} panel-eval candidates:")
    for wr, it, path in top:
        print(f"  iter {it:04d}: avg_panel_wr={wr:.3f}  {path}")

    # Build --models list for run_elo_tournament.py
    # Candidates: <run>_iterNNNN:path — run prefix prevents match-cache collisions
    # across different runs that all save iter0010, iter0020, etc.
    run_prefix = os.path.basename(run_dir.rstrip("/"))  # e.g. "ppo_v47_league"
    models = [f"{run_prefix}_iter{it:04d}:{path}" for _, it, path in top]

    # Fixtures: either "heuristic" or "name:path"
    fixture_names = []
    for fix in args.fixtures:
        if fix == "heuristic" or fix == "__heuristic__":
            models.append("heuristic")
            fixture_names.append("heuristic")
        elif ":" in fix:
            name, path = fix.split(":", 1)
            if os.path.exists(path):
                models.append(f"{name}:{path}")
                fixture_names.append(name)
            else:
                print(f"  [candidate] fixture {name} not found at {path}, skipping", file=sys.stderr)
        else:
            print(f"  [candidate] unrecognized fixture spec '{fix}', skipping", file=sys.stderr)

    # Pick anchor from fixtures actually in the tournament (prefer args.anchor, fall back)
    anchor = args.anchor
    if anchor not in fixture_names and fixture_names:
        anchor = fixture_names[0]
        print(f"[candidate] anchor {args.anchor!r} not in fixtures, using {anchor!r}")

    print(f"[candidate] Models in tournament: {models}")
    print(f"[candidate] Games per matchup: {args.n_games}, anchor: {anchor}={args.anchor_elo}")

    if args.dry_run:
        print("[candidate] --dry-run: exiting without running tournament.")
        return

    # Run tournament
    cmd = [
        sys.executable, "scripts/run_elo_tournament.py",
        "--models", *models,
        "--games", str(args.n_games),
        "--anchor", anchor,
        "--anchor-elo", str(args.anchor_elo),
        "--schedule", "round_robin",
        "--out", out_json,
        "--script-dir", args.script_dir,
    ]
    print(f"[candidate] Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        print(f"ERROR: tournament exited with code {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)

    # Read results and find winner among candidates (exclude fixtures)
    with open(out_json) as f:
        tournament = json.load(f)
    ratings = tournament.get("ratings", {})

    candidate_names = [f"{run_prefix}_iter{it:04d}" for _, it, _ in top]
    candidate_ratings = {k: v["elo"] for k, v in ratings.items() if k in candidate_names}
    if not candidate_ratings:
        print("ERROR: no candidate ratings found in tournament output.", file=sys.stderr)
        sys.exit(1)

    winner_name = max(candidate_ratings, key=lambda k: candidate_ratings[k])
    winner_iter = int(winner_name.split("_iter")[1])
    winner_scripted = os.path.join(run_dir, f"ppo_iter{winner_iter:04d}_scripted.pt")
    winner_ckpt = os.path.join(run_dir, f"ppo_iter{winner_iter:04d}.pt")

    print(f"\n[candidate] Tournament results (candidates only):")
    for name in sorted(candidate_ratings, key=lambda k: -candidate_ratings[k]):
        marker = " ← WINNER" if name == winner_name else ""
        print(f"  {name}: Elo={candidate_ratings[name]:.1f}{marker}")

    # Copy winner to ppo_best.pt / ppo_best_scripted.pt
    best_path = os.path.join(run_dir, "ppo_best.pt")
    best_scripted = os.path.join(run_dir, "ppo_best_scripted.pt")
    if os.path.exists(winner_ckpt):
        shutil.copy2(winner_ckpt, best_path)
        print(f"[candidate] ppo_best.pt ← {winner_ckpt}")
    if os.path.exists(winner_scripted):
        shutil.copy2(winner_scripted, best_scripted)
        print(f"[candidate] ppo_best_scripted.pt ← {winner_scripted}")

    print(f"\n[candidate] Done. Winner: {winner_name} (Elo={candidate_ratings[winner_name]:.1f})")
    print(f"[candidate] Full tournament results: {out_json}")


if __name__ == "__main__":
    main()
