#!/usr/bin/env python3
"""Select a diverse, Elo-stratified fixture set for PPO league training.

Algorithm: Pareto-front seeding + greedy max-min JSD diversification.

1. Load JSD matrix (from compute_jsd_matrix.py) + Elo ladder.
2. Find Pareto front in (elo_ussr, elo_us) space — mandatory anchors.
3. Greedily add models that maximize min-JSD distance to current set.
4. Stop at --target-n.

Prints: --league-fixtures argument list (space-separated paths).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def pareto_front(models: dict[str, dict]) -> list[str]:
    """Return names on the 2D Pareto front in (elo_ussr, elo_us) space (maximization)."""
    names = list(models.keys())
    front = []
    for a in names:
        dominated = False
        for b in names:
            if a == b:
                continue
            if (models[b]["elo_ussr"] >= models[a]["elo_ussr"] and
                    models[b]["elo_us"] >= models[a]["elo_us"] and
                    (models[b]["elo_ussr"] > models[a]["elo_ussr"] or
                     models[b]["elo_us"] > models[a]["elo_us"])):
                dominated = True
                break
        if not dominated:
            front.append(a)
    return front


def min_dist_to_set(
    candidate: str,
    current_set: list[str],
    matrix: dict[str, dict[str, dict]],
    metric: str = "combined",
) -> float:
    if not current_set:
        return float("inf")
    return min(
        matrix[candidate][s][metric]
        for s in current_set
        if s in matrix.get(candidate, {})
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Select diverse fixture set via Pareto + greedy max-min JSD"
    )
    p.add_argument("--jsd-matrix", default="results/jsd_matrix.json")
    p.add_argument("--elo-ladder", default="results/elo_full_ladder.json")
    p.add_argument("--model-dir", default="data/checkpoints/scripted_for_elo",
                   help="Directory containing *_scripted.pt files")
    p.add_argument("--target-n", type=int, default=16,
                   help="Target fixture count (excluding heuristic)")
    p.add_argument("--metric", default="combined",
                   choices=["combined", "card_jsd", "mode_jsd", "country_jsd"],
                   help="Distance metric for greedy selection")
    p.add_argument("--min-elo", type=float, default=None,
                   help="Exclude models below this combined Elo")
    p.add_argument("--add-heuristic", action="store_true", default=True,
                   help="Append __heuristic__ to output")
    p.add_argument("--no-heuristic", dest="add_heuristic", action="store_false")
    p.add_argument("--show-analysis", action="store_true",
                   help="Print per-model JSD stats")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # Load JSD matrix
    with open(args.jsd_matrix) as f:
        jsd_data = json.load(f)
    matrix: dict[str, dict[str, dict]] = jsd_data["matrix"]
    jsd_models = set(jsd_data["models"])

    # Load Elo ladder
    with open(args.elo_ladder) as f:
        elo_data = json.load(f)
    elo_ratings: dict[str, dict] = elo_data["ratings"]

    # Intersect: only models present in both JSD matrix AND Elo ladder AND scripted dir
    model_dir = Path(args.model_dir)
    scripted_models = {p.stem.replace("_scripted", ""): p for p in model_dir.glob("*_scripted.pt")}

    candidates = {}
    for name in jsd_models:
        if name not in elo_ratings:
            continue
        if name not in scripted_models:
            continue
        if name == "heuristic":
            continue
        if args.min_elo is not None and elo_ratings[name]["elo"] < args.min_elo:
            continue
        candidates[name] = elo_ratings[name]

    print(f"Candidate pool: {len(candidates)} models (in JSD matrix + Elo + scripted dir)")

    # Pareto front
    front = pareto_front(candidates)
    front_set = set(front)
    print(f"Pareto front ({len(front)} models): {sorted(front)}")

    # Greedy max-min JSD selection
    selected: list[str] = list(front)  # seed with Pareto-front models

    # If Pareto front already exceeds target, prune it by greedy removal of most redundant
    if len(selected) > args.target_n:
        print(f"Pareto front ({len(selected)}) > target ({args.target_n}), pruning...")
        while len(selected) > args.target_n:
            # Remove the model whose removal changes min-spread the least
            best_remove = None
            best_min_spread_after = -1.0
            for candidate in selected:
                remaining = [s for s in selected if s != candidate]
                # min-spread = average of (min dist to set) for each remaining model
                spread = sum(
                    min_dist_to_set(r, [s for s in remaining if s != r], matrix, args.metric)
                    for r in remaining
                ) / max(1, len(remaining))
                if spread > best_min_spread_after:
                    best_min_spread_after = spread
                    best_remove = candidate
            if best_remove:
                print(f"  Removing {best_remove} (spread after removal: {best_min_spread_after:.4f})")
                selected.remove(best_remove)

    # Greedy add: pick model maximizing min-distance to current set
    remaining_candidates = [n for n in candidates if n not in set(selected)]
    while len(selected) < args.target_n and remaining_candidates:
        best = max(
            remaining_candidates,
            key=lambda c: min_dist_to_set(c, selected, matrix, args.metric),
        )
        best_dist = min_dist_to_set(best, selected, matrix, args.metric)
        selected.append(best)
        remaining_candidates.remove(best)
        print(f"  Added {best}: min-dist={best_dist:.4f}")

    print(f"\nSelected {len(selected)} fixtures:")

    # Sort by Elo descending for display
    selected_sorted = sorted(selected, key=lambda n: elo_ratings[n]["elo"], reverse=True)
    for name in selected_sorted:
        r = elo_ratings[name]
        asym = r["elo_ussr"] - r["elo_us"]
        in_front = "* " if name in front_set else "  "
        print(f"  {in_front}{name}: elo={r['elo']:.0f} ussr={r['elo_ussr']:.0f} us={r['elo_us']:.0f} asym={asym:+.0f}")

    if args.show_analysis:
        print("\nPer-model JSD stats (vs rest of selected set):")
        for name in selected_sorted:
            dists = [
                matrix[name][other]["card_jsd"]
                for other in selected
                if other != name and other in matrix.get(name, {})
            ]
            if dists:
                print(f"  {name}: card_jsd min={min(dists):.4f} mean={sum(dists)/len(dists):.4f} max={max(dists):.4f}")

    # Output: --league-fixtures argument list
    print("\n--- Copy-paste for --league-fixtures ---")
    fixture_paths = [str(scripted_models[n]) for n in selected_sorted]
    if args.add_heuristic:
        fixture_paths.append("__heuristic__")
    print(" \\\n    ".join(fixture_paths))

    # Also output JSON for programmatic use
    out = {
        "selected": selected_sorted,
        "pareto_front": sorted(front),
        "metric": args.metric,
        "target_n": args.target_n,
        "fixture_paths": fixture_paths,
    }
    out_path = Path("results/selected_fixtures.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved selection to {out_path}")


if __name__ == "__main__":
    main()
