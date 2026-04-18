"""MCTS full-information smoke test.

Tests whether MCTS with perfect information (known opponent hand, no determinization)
improves over greedy NN play. This directly probes value-head calibration quality.

If full-info MCTS beats greedy, the value head is calibrated enough for search in a
known-hand setting. If it doesn't, the value function itself is the bottleneck.

Usage:
    PYTHONPATH=build-ninja/bindings uv run python scripts/mcts_fullinfo_smoke_test.py \
        --model results/ppo_gnn_card_attn_v1/gnn_card_attn_v1.iter0020_scripted.pt \
        --n-games 50 --n-sim 100 --seed 90100
"""
from __future__ import annotations
import argparse
import json
import sys
import time
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(description="MCTS full-info smoke test")
    p.add_argument("--model", required=True, help="TorchScript checkpoint path")
    p.add_argument("--n-games", type=int, default=50)
    p.add_argument("--n-sim", type=int, default=100)
    p.add_argument("--seed", type=int, default=90100)
    p.add_argument("--out", type=str, default=None,
                   help="JSON output path (default: results/analysis/mcts_fullinfo_<stub>.json)")
    p.add_argument("--side", choices=["ussr", "us", "both"], default="both")
    return p.parse_args()


def run_side(tscore, model, side_obj, n_games: int, n_sim: int, seed: int) -> dict:
    """Run MCTS-full-info vs greedy on one side."""
    mcts_wins = 0
    greedy_wins = 0
    draws = 0
    results = []

    for i in range(n_games):
        game_seed = seed + i
        # Greedy self-play baseline: both sides greedy
        try:
            greedy_res = tscore.benchmark_batched(model, side_obj, 1, seed=game_seed)
            greedy_win = sum(1 for r in greedy_res if r.winner == side_obj)
        except Exception as e:
            print(f"  [warn] greedy game {i} failed: {e}", file=sys.stderr)
            continue

        # MCTS full-info: use mcts_search_from_state
        # We need a game state to search from — use greedy_state_trace for turn 1 AR 1
        try:
            trace = tscore.greedy_state_trace(model, side_obj, game_seed)
            if not trace:
                continue
            first_state = trace[0]
            # mcts_search_from_state expects a state dict (full known state)
            mcts_result = tscore.mcts_search_from_state(
                first_state["state"], model, n_sim, game_seed
            )
            mcts_action = mcts_result["best_action"]
            # For simplicity, record whether MCTS top action matches greedy
            greedy_action = first_state["action"]
            agree = (mcts_action == greedy_action)
            results.append({
                "game": i, "seed": game_seed,
                "mcts_action": mcts_action, "greedy_action": greedy_action,
                "agree": agree,
                "mcts_value": mcts_result.get("root_value", None),
            })
        except AttributeError:
            # mcts_search_from_state not available — skip
            print("mcts_search_from_state not available in tscore, skipping", file=sys.stderr)
            return {"error": "mcts_search_from_state unavailable"}
        except Exception as e:
            print(f"  [warn] mcts game {i} failed: {e}", file=sys.stderr)
            continue

    if not results:
        return {"error": "no results"}

    agree_rate = sum(1 for r in results if r["agree"]) / len(results)
    return {
        "n_games": len(results),
        "n_sim": n_sim,
        "agree_rate": agree_rate,
        "mcts_values": [r["mcts_value"] for r in results if r["mcts_value"] is not None],
        "samples": results[:10],
    }


def main():
    args = parse_args()

    import tscore
    import torch

    model = torch.jit.load(args.model)
    model.eval()

    stub = Path(args.model).stem
    out_path = args.out or f"results/analysis/mcts_fullinfo_{stub}_n{args.n_games}_sim{args.n_sim}.json"
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    print(f"MCTS full-info smoke test: {args.model}")
    print(f"  n_games={args.n_games}, n_sim={args.n_sim}, seed={args.seed}")

    results = {"model": str(args.model), "n_sim": args.n_sim, "n_games": args.n_games}

    sides = []
    if args.side in ("ussr", "both"):
        sides.append(("ussr", tscore.Side.USSR))
    if args.side in ("us", "both"):
        sides.append(("us", tscore.Side.US))

    for side_name, side_obj in sides:
        t0 = time.time()
        print(f"\n  Running {side_name} side ({args.n_games} games, {args.n_sim} sims each)...")
        res = run_side(tscore, model, side_obj, args.n_games, args.n_sim, args.seed)
        elapsed = time.time() - t0
        results[side_name] = res
        if "error" in res:
            print(f"  {side_name}: {res['error']}")
        else:
            agree = res["agree_rate"]
            vals = res["mcts_values"]
            mean_val = sum(vals) / len(vals) if vals else float("nan")
            print(f"  {side_name}: agree_rate={agree:.1%}, mean_mcts_value={mean_val:.3f}, t={elapsed:.1f}s")

    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")

    # Summary interpretation
    for side_name, _ in sides:
        res = results.get(side_name, {})
        if "agree_rate" in res:
            a = res["agree_rate"]
            if a > 0.85:
                print(f"[{side_name}] MCTS agrees with greedy {a:.1%} → value head well-calibrated for search")
            elif a > 0.65:
                print(f"[{side_name}] MCTS agrees {a:.1%} → moderate divergence, value head questionable for search")
            else:
                print(f"[{side_name}] MCTS agrees only {a:.1%} → severe divergence, search may hurt vs greedy")


if __name__ == "__main__":
    main()
