#!/usr/bin/env python3
"""Analyze AWR sweep results and print ranked architecture comparison.

Usage:
    python scripts/analyze_awr_results.py results/awr_sweep/panel_v5_full.json
    python scripts/analyze_awr_results.py results/awr_sweep/panel_v5_full.json --top 3
    python scripts/analyze_awr_results.py results/awr_sweep/panel_v5_full.json --top 3 --emit-phase2-cmd
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze AWR sweep results")
    parser.add_argument("results_json", help="Path to sweep results JSON")
    parser.add_argument("--top", type=int, default=3, help="Number of top archs to show")
    parser.add_argument("--metric", default="val_adv_card_acc",
                        help="Primary metric for ranking (default: val_adv_card_acc)")
    parser.add_argument("--emit-phase2-cmd", action="store_true",
                        help="Print Phase 2 launch command for top-N archs")
    args = parser.parse_args()

    path = Path(args.results_json)
    if not path.exists():
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text())
    runs = data.get("runs", data)  # support both flat list and {"runs": [...]}
    if "aggregated" in data:
        agg = data["aggregated"]
    else:
        # Compute aggregated from runs
        agg_dict: dict = defaultdict(list)
        for r in runs:
            key = (r["model_type"], r["hidden_dim"], r.get("tau", 1.0))
            agg_dict[key].append(r)
        agg = []
        for (arch, hdim, tau), rs in agg_dict.items():
            entry = {"model_type": arch, "hidden_dim": hdim, "tau": tau,
                     "params": rs[0]["params"], "n_seeds": len(rs)}
            for m in [args.metric, "val_card_acc", "val_policy_loss", "val_value_loss", "time_s"]:
                vals = [r.get(m, 0) for r in rs]
                entry[m] = float(np.mean(vals))
                entry[f"{m}_std"] = float(np.std(vals))
            agg.append(entry)

    # Rank by metric across all taus; take best tau per arch
    best_per_arch: dict = {}
    for entry in agg:
        key = (entry["model_type"], entry["hidden_dim"])
        if key not in best_per_arch or entry[args.metric] > best_per_arch[key][args.metric]:
            best_per_arch[key] = entry

    ranked = sorted(best_per_arch.values(), key=lambda r: r[args.metric], reverse=True)

    # Print table
    print(f"\n{'='*100}")
    print(f"AWR Sweep Results — ranked by {args.metric}")
    print(f"{'='*100}")
    print(f"{'Architecture':<40} {'tau':>6} {'Seeds':>5} {'Params':>8} {'CardAcc':>8} {'AdvCard%':>9} {'PolicyL':>8} {'T(s)':>6}")
    print(f"{'='*100}")
    for r in ranked:
        tag = f"{r['model_type']}_h{r['hidden_dim']}"
        std = r.get(f"{args.metric}_std", 0)
        std_str = f"±{std:.3f}" if std > 0 else "     "
        print(f"{tag:<40} {r['tau']:>6.3g} {r['n_seeds']:>5} {r['params']:>8,} "
              f"{r.get('val_card_acc',0):>8.1%} {r[args.metric]:>9.1%} "
              f"{std_str} {r.get('val_policy_loss',0):>8.3f} {r.get('time_s',0):>6.0f}")

    print(f"{'='*100}")

    # Top-N summary
    print(f"\nTop-{args.top} by {args.metric}:")
    top_archs = []
    for i, r in enumerate(ranked[:args.top]):
        tag = f"{r['model_type']}_h{r['hidden_dim']}_tau{r['tau']:.3g}"
        val = r[args.metric]
        params = r["params"]
        print(f"  {i+1}. {tag}: {val:.3%} ({params:,} params)")
        top_archs.append(r["model_type"])

    # Full per-tau breakdown for top archs
    if len(runs) > 0:
        print(f"\nPer-tau breakdown for top archs:")
        tau_agg: dict = defaultdict(list)
        for r in runs:
            key = (r["model_type"], r["hidden_dim"], r.get("tau", 1.0))
            tau_agg[key].append(r)

        print(f"  {'Architecture':<40} {'tau':>8} {'AdvCard%':>10} {'CardAcc':>9} {'PolicyL':>8}")
        for arch in top_archs:
            for entry in sorted(agg, key=lambda x: x.get("tau", 1.0)):
                if entry["model_type"] == arch and entry["hidden_dim"] == 256:
                    tag = f"{arch}_h{entry['hidden_dim']}"
                    print(f"  {tag:<40} {entry['tau']:>8.3g} "
                          f"{entry[args.metric]:>10.1%} "
                          f"{entry.get('val_card_acc',0):>9.1%} "
                          f"{entry.get('val_policy_loss',0):>8.3f}")

    if args.emit_phase2_cmd:
        top_arch_names = [r["model_type"] for r in ranked[:args.top]]
        print(f"\n# Phase 2 command (full tau × 3-seed validation for top-{args.top}):")
        archs_str = " ".join(top_arch_names)
        print(f"bash scripts/run_awr_sweep_phase2.sh {archs_str}")


if __name__ == "__main__":
    main()
