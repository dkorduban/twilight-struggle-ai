"""Find the first greedy-NN / ISMCTS mismatch in a single game trajectory.

Playbook:
1. Play greedy-NN vs heuristic on learned_side from (seed).
2. At each learned-side decision, query ISMCTS on the same full state
   and compare the top action with the greedy pick.
3. On the first mismatch, dump the state + both actions + ISMCTS edges.

Symptom we're investigating: on v55 with n_det=4, n_sim=50 paired games
(N=50 USSR), greedy-NN wins 27/50 and ISMCTS wins 5/50 — 23 wins flipped to
losses. This script localises the first state where that divergence kicks in.
"""

import argparse
import json
import os
import sys

import tscore


def action_key(action):
    return (action["card_id"], action["mode"], tuple(action["targets"])) if action else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--model",
        default="data/checkpoints/scripted_for_elo/v55_scripted.pt",
    )
    ap.add_argument("--learned-side", choices=["ussr", "us"], default="ussr")
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--n-det", type=int, default=4)
    ap.add_argument("--n-sim", type=int, default=50)
    ap.add_argument("--ismcts-seed", type=int, default=42)
    ap.add_argument("--max-steps", type=int, default=0, help="0 = all")
    ap.add_argument(
        "--skip-headline",
        action="store_true",
        help="Skip ar=0 decisions to test whether the bug is AR-phase-specific",
    )
    ap.add_argument("--output", default="results/ismcts_fix/first_divergence_v55.json")
    args = ap.parse_args()

    side = tscore.Side.USSR if args.learned_side == "ussr" else tscore.Side.US
    print(f"Model: {args.model}")
    print(f"Learned side: {args.learned_side}")
    print(f"Greedy seed: {args.seed}  ISMCTS seed: {args.ismcts_seed}  "
          f"n_det={args.n_det}  n_sim={args.n_sim}")

    trace = tscore.greedy_state_trace(args.model, side, args.seed)
    limit = len(trace) if args.max_steps <= 0 else min(args.max_steps, len(trace))
    print(f"Trace: {len(trace)} learned-side decisions (scanning {limit})")

    for i in range(limit):
        step = trace[i]
        if args.skip_headline and step["ar"] == 0:
            continue
        state = step["state"]
        greedy_act = step["action"]
        result = tscore.ismcts_search_from_state(
            state,
            args.model,
            n_determinizations=args.n_det,
            n_simulations=args.n_sim,
            seed=args.ismcts_seed,
            acting_side=side,
        )
        g_key = action_key(greedy_act)
        i_key = action_key(result["best_action"])
        if g_key is None or i_key is None or g_key == i_key:
            continue

        edges_sorted = sorted(result["edges"], key=lambda edge: -edge["visits"])
        out = {
            "step_index": i,
            "turn": step["turn"],
            "ar": step["ar"],
            "phasing": step["phasing"],
            "learned_side": args.learned_side,
            "state": state,
            "greedy_action": greedy_act,
            "ismcts_best_action": result["best_action"],
            "ismcts_root_value": result["root_value"],
            "ismcts_total_determinizations": result["total_determinizations"],
            "ismcts_top_edges": edges_sorted[:10],
            "meta": {
                "model": args.model,
                "seed": args.seed,
                "ismcts_seed": args.ismcts_seed,
                "n_det": args.n_det,
                "n_sim": args.n_sim,
            },
        }
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as handle:
            json.dump(out, handle, indent=2)
        print(f"FIRST DIVERGENCE at step {i} "
              f"(turn={step['turn']} ar={step['ar']} phasing={step['phasing']})")
        print(f"  greedy: {greedy_act}")
        print(f"  ismcts: {result['best_action']}  root_value={result['root_value']:+.3f}")
        print(f"  wrote: {args.output}")
        return 0

    print(f"No divergence found across {limit} decisions — greedy and ISMCTS agreed on every one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
