#!/usr/bin/env python3
"""Disambiguate the 0.650 record: nash vs fixed temperature opponent (#114).

Runs v32_continue (the '0.650 ceiling' checkpoint) on post-Plan-B engine both
ways: nash_temperatures=True (formal bench default, hard heuristic) and
nash_temperatures=False (panel eval setting, easy heuristic). If FIXED recovers
~0.65, the ceiling is vs easy heuristic. If both ~0.48, something else is up.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, "build-ninja/bindings")
import torch  # noqa: E402
torch.set_num_threads(1)
import tscore  # noqa: E402

CKPT = "data/checkpoints/scripted_for_elo/v32_continue_scripted.pt"
N = 500

out = {"checkpoint": CKPT, "n_per_side": N, "modes": {}}
for mode_name, nash in [("nash_True", True), ("nash_False", False)]:
    t0 = time.time()
    r_ussr = tscore.benchmark_batched(CKPT, tscore.Side.USSR, N, pool_size=32, seed=50000, nash_temperatures=nash)
    r_us = tscore.benchmark_batched(CKPT, tscore.Side.US, N, pool_size=32, seed=50500, nash_temperatures=nash)
    ussr = sum(1 for x in r_ussr if x.winner == tscore.Side.USSR) / N
    us = sum(1 for x in r_us if x.winner == tscore.Side.US) / N
    out["modes"][mode_name] = {"ussr_wr": ussr, "us_wr": us, "combined_wr": (ussr + us) / 2, "elapsed_s": time.time() - t0}
    print(f"{mode_name}: USSR={ussr:.3f}  US={us:.3f}  combined={(ussr+us)/2:.3f}  t={time.time()-t0:.1f}s")

Path("results/bench_v32_nash_vs_fixed.json").write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
