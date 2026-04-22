#!/usr/bin/env python3
"""Subprocess-isolated version of ismcts_sweep_vs_self.

If the crash is caused by memory accumulation across configs in one Python
process (the hypothesis after ASAN shows single-config runs are clean), then
running each config in a fresh subprocess sidesteps it.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
N_PER_SIDE = 20
POOL = 16
PEND = 8
DEV = "cpu"
SEED = 91000

CONFIGS = [
    (2, 25),
    (2, 50),
    (4, 50),
    (4, 100),
    (8, 100),
    (16, 100),
]


WORKER = r"""
import json, sys, time
sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

torch.set_num_threads(4)

args = json.loads(sys.stdin.read())
t0 = time.perf_counter()
results = tscore.benchmark_ismcts_vs_model_both_sides(
    args["model"], args["model"],
    n_games=2 * args["n_per_side"],
    n_determinizations=args["n_det"], n_simulations=args["n_sim"],
    seed=args["seed"], pool_size=args["pool"],
    max_pending_per_det=args["pend"], device=args["dev"],
)
elapsed = time.perf_counter() - t0
u = sum(1 for g in results[:args["n_per_side"]] if g.winner == tscore.Side.USSR)
s = sum(1 for g in results[args["n_per_side"]:] if g.winner == tscore.Side.US)
print(json.dumps({"u": u, "s": s, "elapsed": elapsed}))
"""


def run(n_det, n_sim):
    payload = json.dumps({
        "model": MODEL, "n_per_side": N_PER_SIDE,
        "n_det": n_det, "n_sim": n_sim,
        "seed": SEED, "pool": POOL, "pend": PEND, "dev": DEV,
    })
    proc = subprocess.run(
        ["uv", "run", "python", "-c", WORKER],
        input=payload,
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        print(f"FAIL(rc={proc.returncode}): {proc.stderr[-500:]}")
        return None
    out = proc.stdout.strip().split("\n")[-1]
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        print(f"UNPARSED: {proc.stdout[-300:]}")
        return None


def main():
    print(f"ISMCTS subprocess-isolated sweep: N={N_PER_SIDE}/side seed={SEED}")
    print(f"{'n_det':>6} {'n_sim':>6} {'USSR':>6} {'US':>6} {'secs':>6}")
    for n_det, n_sim in CONFIGS:
        result = run(n_det, n_sim)
        if result is None:
            print(f"{n_det:>6} {n_sim:>6}   FAIL")
            continue
        print(
            f"{n_det:>6} {n_sim:>6} "
            f"{result['u']:>6} {result['s']:>6} {result['elapsed']:>6.1f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
