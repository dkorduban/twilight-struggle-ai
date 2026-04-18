#!/usr/bin/env python3
"""Run one game per bucket with TS_ACTION_LOG=1 enabled. Capture stderr."""
import os
import sys

os.environ["TS_ACTION_LOG"] = "1"

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
torch.set_num_threads(2)

bucket = sys.argv[1] if len(sys.argv) > 1 else "B_heur_ussr"

if bucket == "B_heur_ussr":
    # ISMCTS as USSR vs heuristic US
    print("=== B_heur_ussr: ISMCTS USSR vs heuristic US ===", file=sys.stderr, flush=True)
    r = tscore.benchmark_ismcts(
        MODEL, tscore.Side.USSR, 1,
        n_determinizations=4, n_simulations=50,
        seed=12345, pool_size=1, max_pending_per_det=4, device="cpu",
    )
elif bucket == "B_heur_us":
    print("=== B_heur_us: ISMCTS US vs heuristic USSR ===", file=sys.stderr, flush=True)
    r = tscore.benchmark_ismcts(
        MODEL, tscore.Side.US, 1,
        n_determinizations=4, n_simulations=50,
        seed=12346, pool_size=1, max_pending_per_det=4, device="cpu",
    )
elif bucket == "A_self":
    print("=== A_self: ISMCTS vs greedy self (2 games) ===", file=sys.stderr, flush=True)
    r = tscore.benchmark_ismcts_vs_model_both_sides(
        MODEL, MODEL,
        n_games=2,
        n_determinizations=4, n_simulations=50,
        seed=12347, pool_size=1, max_pending_per_det=4, device="cpu",
    )
elif bucket == "C_ctrl_ussr":
    # Greedy NN USSR vs heuristic US (control)
    print("=== C_ctrl_ussr: greedy NN USSR vs heuristic US ===", file=sys.stderr, flush=True)
    r = tscore.benchmark_batched(
        MODEL, tscore.Side.USSR, 1,
        pool_size=1, seed=12348, device="cpu",
        greedy_opponent=False, temperature=0.0, nash_temperatures=False,
    )
else:
    print(f"Unknown bucket: {bucket}", file=sys.stderr)
    sys.exit(1)

print(f"\n=== result ===", file=sys.stderr, flush=True)
for g in r:
    w = "USSR" if g.winner == tscore.Side.USSR else ("US" if g.winner == tscore.Side.US else "DRAW")
    print(f"winner={w} end_turn={g.end_turn} end_reason={g.end_reason}", file=sys.stderr, flush=True)
