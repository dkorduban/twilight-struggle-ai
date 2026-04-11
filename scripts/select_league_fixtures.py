#!/usr/bin/env python3
"""Select a diverse, Elo-stratified fixture set for PPO league training.

v2 Algorithm: Per-side pools with JSD deduplication.

USSR pool: ranked by elo_ussr, greedily add models with min-JSD > --min-jsd.
US pool:   ranked by elo_us,   greedily add models with min-JSD > --min-jsd.
Both pools deduplicate within themselves (models too similar are skipped).

The combined unique set is what --league-fixtures outputs.
With two separate pools, the PFSP trainer can pick harder USSR opponents for
USSR decisions and harder US opponents for US decisions.

Prints:
  --league-fixtures argument list (space-separated paths)
  --ussr-fixtures / --us-fixtures argument lists for two-pool PFSP
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def min_dist_to_set(
    candidate: str,
    current_set: list[str],
    matrix: dict[str, dict[str, dict]],
    metric: str = "combined",
) -> float:
    if not current_set:
        return float("inf")
    dists = [
        matrix[candidate][s][metric]
        for s in current_set
        if s in matrix.get(candidate, {})
    ]
    return min(dists) if dists else float("inf")


def build_pool(
    candidates_sorted: list[str],
    target_n: int,
    min_jsd: float,
    matrix: dict[str, dict[str, dict]],
    metric: str = "combined",
) -> list[str]:
    """Greedily build a pool by rank order, skipping near-duplicates.

    Models are pre-sorted by the relevant Elo dimension (caller's responsibility).
    We add the top model, then each subsequent model only if its min-JSD to the
    already-selected set exceeds min_jsd.
    """
    selected: list[str] = []
    for cand in candidates_sorted:
        if len(selected) >= target_n:
            break
        d = min_dist_to_set(cand, selected, matrix, metric)
        if d >= min_jsd:
            selected.append(cand)
    return selected


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Select per-side fixture pools via Elo ranking + JSD deduplication"
    )
    p.add_argument("--jsd-matrix", default="results/elo/jsd_matrix.json")
    p.add_argument("--elo-ladder", default="results/elo/elo_full_ladder.json")
    p.add_argument("--model-dir", default="data/checkpoints/scripted_for_elo",
                   help="Directory containing *_scripted.pt files")
    p.add_argument("--ussr-pool-n", type=int, default=8,
                   help="Target USSR pool size")
    p.add_argument("--us-pool-n", type=int, default=8,
                   help="Target US pool size")
    p.add_argument("--min-jsd", type=float, default=0.010,
                   help="Minimum JSD distance to include a model (deduplication threshold)")
    p.add_argument("--metric", default="combined",
                   choices=["combined", "card_jsd", "mode_jsd", "country_jsd"],
                   help="Distance metric for deduplication")
    p.add_argument("--min-elo", type=float, default=None,
                   help="Exclude models below this combined Elo")
    p.add_argument("--add-heuristic", action="store_true", default=True,
                   help="Append __heuristic__ to output")
    p.add_argument("--no-heuristic", dest="add_heuristic", action="store_false")
    p.add_argument("--show-analysis", action="store_true",
                   help="Print per-model JSD stats vs selected set")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    with open(args.jsd_matrix) as f:
        jsd_data = json.load(f)
    matrix: dict[str, dict[str, dict]] = jsd_data["matrix"]
    jsd_models = set(jsd_data["models"])

    with open(args.elo_ladder) as f:
        elo_data = json.load(f)
    elo_ratings: dict[str, dict] = elo_data["ratings"]

    model_dir = Path(args.model_dir)
    scripted_models = {p.stem.replace("_scripted", ""): p for p in model_dir.glob("*_scripted.pt")}

    candidates: dict[str, dict] = {}
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

    # --- USSR pool: rank by elo_ussr ---
    ussr_ranked = sorted(candidates, key=lambda n: candidates[n]["elo_ussr"], reverse=True)
    ussr_pool = build_pool(ussr_ranked, args.ussr_pool_n, args.min_jsd, matrix, args.metric)

    print(f"\nUSSR pool ({len(ussr_pool)} models, ranked by elo_ussr, min-JSD={args.min_jsd}):")
    for name in ussr_pool:
        r = candidates[name]
        d = min_dist_to_set(name, [x for x in ussr_pool if x != name], matrix, args.metric)
        print(f"  {name}: elo={r['elo']:.0f} ussr={r['elo_ussr']:.0f} us={r['elo_us']:.0f}  min-JSD={d:.4f}")

    # --- US pool: rank by elo_us ---
    us_ranked = sorted(candidates, key=lambda n: candidates[n]["elo_us"], reverse=True)
    us_pool = build_pool(us_ranked, args.us_pool_n, args.min_jsd, matrix, args.metric)

    print(f"\nUS pool ({len(us_pool)} models, ranked by elo_us, min-JSD={args.min_jsd}):")
    for name in us_pool:
        r = candidates[name]
        d = min_dist_to_set(name, [x for x in us_pool if x != name], matrix, args.metric)
        print(f"  {name}: elo={r['elo']:.0f} ussr={r['elo_ussr']:.0f} us={r['elo_us']:.0f}  min-JSD={d:.4f}")

    # --- Combined unique set ---
    combined_set: list[str] = list(dict.fromkeys(ussr_pool + us_pool))  # preserve order, dedup
    combined_sorted = sorted(combined_set, key=lambda n: candidates[n]["elo"], reverse=True)

    print(f"\nCombined unique fixtures: {len(combined_sorted)} models")
    for name in combined_sorted:
        r = candidates[name]
        in_ussr = "U" if name in ussr_pool else " "
        in_us = "S" if name in us_pool else " "
        print(f"  [{in_ussr}{in_us}] {name}: elo={r['elo']:.0f} ussr={r['elo_ussr']:.0f} us={r['elo_us']:.0f}")

    if args.show_analysis:
        print("\nPer-model JSD stats (vs rest of combined set):")
        for name in combined_sorted:
            dists = [
                matrix[name][other]["card_jsd"]
                for other in combined_set
                if other != name and other in matrix.get(name, {})
            ]
            if dists:
                print(f"  {name}: card_jsd min={min(dists):.4f} mean={sum(dists)/len(dists):.4f} max={max(dists):.4f}")

    # --- Output copy-paste blocks ---
    ussr_paths = [str(scripted_models[n]) for n in ussr_pool]
    us_paths = [str(scripted_models[n]) for n in us_pool]
    combined_paths = [str(scripted_models[n]) for n in combined_sorted]
    if args.add_heuristic:
        combined_paths.append("__heuristic__")
        ussr_paths.append("__heuristic__")
        us_paths.append("__heuristic__")

    print("\n--- --league-fixtures (combined, for single-pool PFSP) ---")
    print(" \\\n    ".join(combined_paths))

    print("\n--- --ussr-fixtures (for two-pool PFSP) ---")
    print(" \\\n    ".join(ussr_paths))

    print("\n--- --us-fixtures (for two-pool PFSP) ---")
    print(" \\\n    ".join(us_paths))

    out = {
        "ussr_pool": ussr_pool,
        "us_pool": us_pool,
        "combined": combined_sorted,
        "metric": args.metric,
        "min_jsd": args.min_jsd,
        "ussr_pool_n": args.ussr_pool_n,
        "us_pool_n": args.us_pool_n,
        "fixture_paths": combined_paths,
        "ussr_fixture_paths": ussr_paths,
        "us_fixture_paths": us_paths,
    }
    out_path = Path("results/elo/selected_fixtures.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved selection to {out_path}")


if __name__ == "__main__":
    main()
