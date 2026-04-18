"""Run ISMCTS at multiple (n_det, n_sim) budgets on a single captured state.

Takes the state dict from a first_divergence_*.json dump and asks: does
visit-argmax converge to value-argmax (and/or to the greedy choice) as
we crank up budget? This is the Opus §4 Open Q2 probe — if the mode
mismatch is a low-budget visit-argmax artifact, we should see it
disappear around n_sim=200-400 per determinization. If it persists at
n_sim=1000+, the value head is disagreeing with greedy on these states.
"""

import argparse
import json
import os
import sys
from typing import Any

import tscore


def action_key(action: dict[str, Any] | None) -> tuple[int, int, tuple[int, ...]] | None:
    return (action["card_id"], action["mode"], tuple(action["targets"])) if action else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="First-divergence JSON produced by ismcts_first_divergence.py")
    ap.add_argument("--model", default="data/checkpoints/scripted_for_elo/v55_scripted.pt")
    ap.add_argument("--ismcts-seed", type=int, default=42)
    ap.add_argument("--n-det", type=int, default=4)
    ap.add_argument(
        "--sims",
        type=str,
        default="50,100,200,400,800,1600",
        help="Comma-separated n_simulations values to try",
    )
    ap.add_argument("--output", default="results/ismcts_fix/budget_convergence.json")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    state = payload["state"]
    greedy_action = payload["greedy_action"]
    learned_side = payload["learned_side"]
    side = tscore.Side.USSR if learned_side == "ussr" else tscore.Side.US

    print(f"State: step_index={payload['step_index']} turn={payload['turn']} ar={payload['ar']} phasing={payload['phasing']}")
    print(f"Greedy action: {greedy_action}")
    print(f"n_det={args.n_det}  ismcts_seed={args.ismcts_seed}")
    print()

    sim_values = [int(s) for s in args.sims.split(",") if s.strip()]
    greedy_key = action_key(greedy_action)

    results = []
    header = (
        f"{'n_sim':>6}  {'best (card,mode,targets)':<30}"
        f"  {'best_visits':>11}  {'best_value':>10}  {'=greedy':>7}  "
        f"{'value_argmax (card,mode)':<25}"
    )
    print(header)
    print("-" * len(header))

    for n_sim in sim_values:
        result = tscore.ismcts_search_from_state(
            state,
            args.model,
            n_determinizations=args.n_det,
            n_simulations=n_sim,
            seed=args.ismcts_seed,
            acting_side=side,
        )
        best = result["best_action"]
        best_key = action_key(best)
        edges = sorted(result["edges"], key=lambda e: -e["visits"])
        top_edge = edges[0] if edges else {}
        value_sorted = sorted(result["edges"], key=lambda e: -e["mean_value"]) if result["edges"] else []
        value_top = value_sorted[0] if value_sorted else {}
        match = "YES" if best_key == greedy_key else "no"
        best_repr = f"({best['card_id']},{best['mode']},{best['targets']})" if best else "-"
        value_repr = (
            f"({value_top.get('card_id', '?')},{value_top.get('mode', '?')})"
            if value_top
            else "-"
        )
        print(
            f"{n_sim:>6}  {best_repr:<30}"
            f"  {top_edge.get('visits', 0):>11}  {top_edge.get('mean_value', 0.0):>10.4f}"
            f"  {match:>7}  {value_repr:<25}"
        )
        results.append(
            {
                "n_sim": n_sim,
                "best_action": best,
                "root_value": result["root_value"],
                "total_determinizations": result["total_determinizations"],
                "top5_by_visits": edges[:5],
                "top5_by_value": value_sorted[:5],
                "matches_greedy": best_key == greedy_key,
            }
        )

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(
            {
                "input": args.input,
                "greedy_action": greedy_action,
                "n_det": args.n_det,
                "ismcts_seed": args.ismcts_seed,
                "model": args.model,
                "sims": sim_values,
                "sweep": results,
            },
            handle,
            indent=2,
        )
    print()
    print(f"Wrote: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
