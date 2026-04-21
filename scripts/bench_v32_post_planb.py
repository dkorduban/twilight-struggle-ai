#!/usr/bin/env python3
"""Formal bench of v32_continue on the POST-Plan-B fixed engine."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

sys.path.insert(0, "build-ninja/bindings")
import torch  # noqa: E402
torch.set_num_threads(1)
import tscore  # noqa: E402

CKPT = "data/checkpoints/scripted_for_elo/v32_continue_scripted.pt"
if not Path(CKPT).exists():
    print(f"ERROR: {CKPT} not found", file=sys.stderr)
    sys.exit(1)

N = 500

t0 = time.time()
r_ussr = tscore.benchmark_batched(CKPT, tscore.Side.USSR, N, pool_size=32, seed=50000)
t1 = time.time()
r_us = tscore.benchmark_batched(CKPT, tscore.Side.US, N, pool_size=32, seed=50500)
t2 = time.time()

ussr = sum(1 for x in r_ussr if x.winner == tscore.Side.USSR) / N
us = sum(1 for x in r_us if x.winner == tscore.Side.US) / N
combined = (ussr + us) / 2

out = {
    "checkpoint": CKPT,
    "engine_head": "abe69f3 (post Plan B: SALT+2, Yuri timing, SA Unrest, LatAm Debt)",
    "n_per_side": N,
    "seeds": [50000, 50500],
    "ussr_wr": ussr,
    "us_wr": us,
    "combined_wr": combined,
    "t_ussr_s": t1 - t0,
    "t_us_s": t2 - t1,
    "t_total_s": t2 - t0,
}

out_path = Path("results/bench_v32_post_planb.json")
out_path.write_text(json.dumps(out, indent=2))

print(json.dumps(out, indent=2))
print(f"\nWrote {out_path}")
