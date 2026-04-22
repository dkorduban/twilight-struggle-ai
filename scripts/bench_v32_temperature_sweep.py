#!/usr/bin/env python3
"""R3 diagnostic: bench v32_iter20 at different sampling temperatures.

If any τ>0 dominates greedy by >2pp combined, it's a free Elo lift.
If all within 2pp, current greedy is correct — rule out and move to R1.
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

# Pin thread caps before importing torch
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OMP_WAIT_POLICY", "passive")
os.environ.setdefault("KMP_BLOCKTIME", "0")

sys.path.insert(0, "build-ninja/bindings")
import torch  # noqa: E402
torch.set_num_threads(1)
import tscore  # noqa: E402

V32 = "data/checkpoints/scripted_for_elo/v32_iter20_scripted.pt"
if not Path(V32).exists():
    # fallback to continue-scripted
    V32 = "data/checkpoints/scripted_for_elo/v32_continue_scripted.pt"
    print(f"fallback: using {V32}")

TEMPS = [0.0, 0.1, 0.3, 0.5, 0.7, 1.0]
N_PER_SIDE = 200

results: list[dict] = []
t_start_all = time.time()
for tau in TEMPS:
    t0 = time.time()
    r_ussr = tscore.benchmark_batched(V32, tscore.Side.USSR, N_PER_SIDE,
                                      pool_size=32, seed=50000,
                                      temperature=tau, nash_temperatures=True)
    r_us = tscore.benchmark_batched(V32, tscore.Side.US, N_PER_SIDE,
                                    pool_size=32, seed=50500,
                                    temperature=tau, nash_temperatures=True)
    ussr = sum(1 for x in r_ussr if x.winner == tscore.Side.USSR) / N_PER_SIDE
    us = sum(1 for x in r_us if x.winner == tscore.Side.US) / N_PER_SIDE
    combined = (ussr + us) / 2
    elapsed = time.time() - t0
    row = {"tau": tau, "ussr": ussr, "us": us, "combined": combined, "elapsed_s": round(elapsed, 1)}
    results.append(row)
    print(f"tau={tau:.1f}  USSR={ussr:.3f}  US={us:.3f}  combined={combined:.3f}  ({elapsed:.1f}s)", flush=True)

total = time.time() - t_start_all
print(f"\nTotal: {total:.1f}s")

# Find best
best = max(results, key=lambda r: r["combined"])
greedy = next(r for r in results if r["tau"] == 0.0)
uplift = best["combined"] - greedy["combined"]
print(f"\nBest tau={best['tau']} combined={best['combined']:.3f}, greedy={greedy['combined']:.3f}, uplift={uplift:+.3f}")

out = Path("results/analysis/v32_temperature_sweep.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({
    "checkpoint": V32,
    "n_per_side": N_PER_SIDE,
    "seeds": [50000, 50500],
    "nash_temperatures": True,
    "results": results,
    "best_tau": best["tau"],
    "uplift_over_greedy": round(uplift, 4),
}, indent=2))
print(f"wrote {out}")
