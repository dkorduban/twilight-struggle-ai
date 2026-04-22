#!/usr/bin/env python3
"""Formal bench of v34_iter10 vs heuristic, 500g/side, canonical seeds."""

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

CKPT = "results/ppo_v34_peerpool/ppo_running_best_scripted.pt"
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
    "n_per_side": N,
    "seeds": [50000, 50500],
    "ussr": round(ussr, 4),
    "us": round(us, 4),
    "combined": round(combined, 4),
    "elapsed_s": round(t2 - t0, 1),
    "v32_record_combined": 0.650,
    "uplift_vs_v32": round(combined - 0.650, 4),
}
print(f"v34_iter10 USSR={ussr:.3f}  US={us:.3f}  combined={combined:.3f}  ({t2-t0:.1f}s)")
print(f"vs v32 (0.650): {combined - 0.650:+.4f}")

Path("results/analysis").mkdir(parents=True, exist_ok=True)
Path("results/analysis/v34_iter10_formal_bench.json").write_text(json.dumps(out, indent=2))
print("wrote results/analysis/v34_iter10_formal_bench.json")
