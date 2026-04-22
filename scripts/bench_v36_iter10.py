#!/usr/bin/env python3
"""Formal bench of v36_iter10 (HWM) vs heuristic, 500g/side, canonical + 60k cross-check seeds."""

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

CKPT = "results/ppo_v36_dense_reward/ppo_best_scripted.pt"
assert Path(CKPT).exists(), CKPT

N = 500
SEED_A = 50000
SEED_B = 60000

t0 = time.time()
r_ussr_a = tscore.benchmark_batched(CKPT, tscore.Side.USSR, N, pool_size=32, seed=SEED_A)
r_us_a = tscore.benchmark_batched(CKPT, tscore.Side.US, N, pool_size=32, seed=SEED_A + 500)
r_ussr_b = tscore.benchmark_batched(CKPT, tscore.Side.USSR, N, pool_size=32, seed=SEED_B)
r_us_b = tscore.benchmark_batched(CKPT, tscore.Side.US, N, pool_size=32, seed=SEED_B + 500)
t1 = time.time()

ussr_a = sum(1 for x in r_ussr_a if x.winner == tscore.Side.USSR) / N
us_a = sum(1 for x in r_us_a if x.winner == tscore.Side.US) / N
comb_a = (ussr_a + us_a) / 2

ussr_b = sum(1 for x in r_ussr_b if x.winner == tscore.Side.USSR) / N
us_b = sum(1 for x in r_us_b if x.winner == tscore.Side.US) / N
comb_b = (ussr_b + us_b) / 2

mean_comb = (comb_a + comb_b) / 2

out = {
    "checkpoint": CKPT,
    "n_per_side": N,
    "seed_A": {"seed": SEED_A, "ussr": round(ussr_a, 4), "us": round(us_a, 4), "combined": round(comb_a, 4)},
    "seed_B": {"seed": SEED_B, "ussr": round(ussr_b, 4), "us": round(us_b, 4), "combined": round(comb_b, 4)},
    "mean_combined": round(mean_comb, 4),
    "elapsed_s": round(t1 - t0, 1),
    "v32_record_combined": 0.650,
    "uplift_vs_v32": round(mean_comb - 0.650, 4),
    "kill_gate": 0.66,
    "passes_kill_gate": mean_comb >= 0.66,
}
print(f"v36_iter10 seed={SEED_A}: USSR={ussr_a:.3f} US={us_a:.3f} comb={comb_a:.3f}")
print(f"v36_iter10 seed={SEED_B}: USSR={ussr_b:.3f} US={us_b:.3f} comb={comb_b:.3f}")
print(f"MEAN combined = {mean_comb:.3f}  ({t1-t0:.1f}s)")
print(f"vs v32 (0.650): {mean_comb - 0.650:+.4f}")
print(f"kill gate 0.66: {'PASS' if mean_comb >= 0.66 else 'FAIL'}")

Path("results/analysis").mkdir(parents=True, exist_ok=True)
Path("results/analysis/v36_iter10_formal_bench.json").write_text(json.dumps(out, indent=2))
print("wrote results/analysis/v36_iter10_formal_bench.json")
