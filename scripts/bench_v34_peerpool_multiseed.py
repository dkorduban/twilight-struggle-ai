#!/usr/bin/env python3
"""Formal multi-seed bench of v34_peerpool iter10 on post-Plan-B engine (#113).

Panel eval at iter10 reported combined=0.700 (v56=0.650, heuristic=0.717).
Kill criterion: <0.55 abort; 0.55-0.67 continue; >=0.67 NEW RECORD vs prior 0.650.
This bench uses benchmark_batched vs heuristic, canonical seed grid.
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

CKPTS = {
    "v34_peerpool_iter10": "results/ppo_v34_peerpool/ppo_iter0010_scripted.pt",
    "v34_peerpool_running_best": "results/ppo_v34_peerpool/ppo_running_best_scripted.pt",
}
SEEDS_US   = [50500, 60500, 70500, 80500, 90500]
SEEDS_USSR = [50000, 60000, 70000, 80000, 90000]
N = 500

out: dict = {
    "engine_head": "78b7aa5 (Plan B + Camp David + v110 scripts)",
    "n_per_side_per_seed": N,
    "results": {},
}

for label, ckpt in CKPTS.items():
    if not Path(ckpt).exists():
        print(f"SKIP {label}: {ckpt} not found", file=sys.stderr)
        continue
    us_wrs, ussr_wrs = [], []
    print(f"\n=== {label} ({ckpt}) ===", flush=True)
    t_label = time.time()
    for s in SEEDS_US:
        r = tscore.benchmark_batched(ckpt, tscore.Side.US, N, pool_size=32, seed=s)
        wr = sum(1 for x in r if x.winner == tscore.Side.US) / N
        us_wrs.append(wr)
        print(f"  US   seed={s}: {wr:.3f}", flush=True)
    for s in SEEDS_USSR:
        r = tscore.benchmark_batched(ckpt, tscore.Side.USSR, N, pool_size=32, seed=s)
        wr = sum(1 for x in r if x.winner == tscore.Side.USSR) / N
        ussr_wrs.append(wr)
        print(f"  USSR seed={s}: {wr:.3f}", flush=True)
    res = {
        "us_wrs":      us_wrs,
        "us_mean":     mean(us_wrs),
        "us_std":      stdev(us_wrs) if len(us_wrs) > 1 else 0.0,
        "ussr_wrs":    ussr_wrs,
        "ussr_mean":   mean(ussr_wrs),
        "ussr_std":    stdev(ussr_wrs) if len(ussr_wrs) > 1 else 0.0,
        "combined_mean": (mean(us_wrs) + mean(ussr_wrs)) / 2,
        "elapsed_s":   time.time() - t_label,
    }
    out["results"][label] = res
    print(f"  -> US mean={res['us_mean']:.3f} +/- {res['us_std']:.3f}", flush=True)
    print(f"  -> USSR mean={res['ussr_mean']:.3f} +/- {res['ussr_std']:.3f}", flush=True)
    print(f"  -> combined={res['combined_mean']:.3f}", flush=True)

out_path = Path("results/bench_v34_peerpool_multiseed.json")
out_path.write_text(json.dumps(out, indent=2))
print(f"\nWrote {out_path}")
