#!/usr/bin/env python3
"""Formal multi-seed bench of BC-on-fixed-engine checkpoint (#109).

Gate criterion (from advisor plan):
  combined >= 0.55 -> unblock #96 (v37 distill stage 1)
  combined <  0.55 -> escalate to architecture changes (Phase 2a/2b)

Uses canonical seed grid (same as bench_v34_peerpool_multiseed.py) and
nash_temperatures=True (the benchmark_batched default, the real metric).
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from statistics import mean, stdev

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

sys.path.insert(0, "build-ninja/bindings")
import torch  # noqa: E402
torch.set_num_threads(1)
import tscore  # noqa: E402

CKPT = os.environ.get(
    "BC_CKPT",
    "results/bc_v32_fixed_engine/baseline_best_scripted.pt",
)
SEEDS_US   = [50500, 60500, 70500, 80500, 90500]
SEEDS_USSR = [50000, 60000, 70000, 80000, 90000]
N = 500

out: dict = {
    "engine_head": "abe69f3 + fb9e814 (Plan B + Camp David)",
    "checkpoint": CKPT,
    "n_per_side_per_seed": N,
    "nash_temperatures": True,
}

if not Path(CKPT).exists():
    print(f"ERROR: checkpoint not found: {CKPT}", file=sys.stderr)
    sys.exit(1)

us_wrs, ussr_wrs = [], []
print(f"=== {CKPT} ===", flush=True)
t0 = time.time()
for s in SEEDS_US:
    r = tscore.benchmark_batched(CKPT, tscore.Side.US, N, pool_size=32, seed=s)
    wr = sum(1 for x in r if x.winner == tscore.Side.US) / N
    us_wrs.append(wr)
    print(f"  US   seed={s}: {wr:.3f}", flush=True)
for s in SEEDS_USSR:
    r = tscore.benchmark_batched(CKPT, tscore.Side.USSR, N, pool_size=32, seed=s)
    wr = sum(1 for x in r if x.winner == tscore.Side.USSR) / N
    ussr_wrs.append(wr)
    print(f"  USSR seed={s}: {wr:.3f}", flush=True)

res = {
    "us_wrs":        us_wrs,
    "us_mean":       mean(us_wrs),
    "us_std":        stdev(us_wrs),
    "ussr_wrs":      ussr_wrs,
    "ussr_mean":     mean(ussr_wrs),
    "ussr_std":      stdev(ussr_wrs),
    "combined_mean": (mean(us_wrs) + mean(ussr_wrs)) / 2,
    "elapsed_s":     time.time() - t0,
}
out["results"] = res
print(f"-> US mean={res['us_mean']:.3f} +/- {res['us_std']:.3f}", flush=True)
print(f"-> USSR mean={res['ussr_mean']:.3f} +/- {res['ussr_std']:.3f}", flush=True)
print(f"-> combined={res['combined_mean']:.3f}", flush=True)

gate = 0.55
if res["combined_mean"] >= gate:
    verdict = f"PASS (>= {gate}) -> unblock #96 (v37 distill stage 1)"
else:
    verdict = f"FAIL (< {gate}) -> escalate to Phase 2a GNN / 2b regional features"
print(f"-> verdict: {verdict}", flush=True)
out["verdict"] = verdict

out_path = Path("results/bench_bc_v32_fixed_multiseed.json")
out_path.write_text(json.dumps(out, indent=2))
print(f"Wrote {out_path}")
