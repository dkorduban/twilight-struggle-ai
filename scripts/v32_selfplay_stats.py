#!/usr/bin/env python3
"""Run v32 vs v32 self-play, collect game-length and win-reason distributions."""

from __future__ import annotations

import os
import sys
import time
from collections import Counter
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

sys.path.insert(0, "build-ninja/bindings")
import torch  # noqa: E402
torch.set_num_threads(1)
import tscore  # noqa: E402

MODEL = "data/checkpoints/scripted_for_elo/v32_continue_scripted.pt"
N = 500

assert Path(MODEL).exists(), MODEL

t0 = time.time()
results = tscore.benchmark_model_vs_model_batched(
    MODEL, MODEL, n_games=N, pool_size=32, seed=20260421, temperature=0.0
)
t1 = time.time()

# First N/2: model_a=USSR, model_b=US. Next N/2: swapped.
half = N // 2
group_a_ussr = results[:half]
group_a_us = results[half:]

def summarize(rs, tag, ussr_is_a: bool):
    ussr_wins = sum(1 for x in rs if x.winner == tscore.Side.USSR)
    us_wins = sum(1 for x in rs if x.winner == tscore.Side.US)
    turns = Counter(x.end_turn for x in rs)
    reasons = Counter(str(x.end_reason) for x in rs)
    print(f"\n-- {tag} ({len(rs)}g; USSR=model_a={ussr_is_a}) --")
    print(f"  USSR wins: {ussr_wins} ({ussr_wins/len(rs):.1%})   US wins: {us_wins} ({us_wins/len(rs):.1%})")
    print(f"  End turn distribution:")
    for t in sorted(turns):
        bar = "#" * int(40 * turns[t] / len(rs))
        print(f"    T{t:>2}: {turns[t]:>4}  {bar}")
    print(f"  End reason distribution:")
    for r, c in reasons.most_common():
        print(f"    {r:<30} {c:>4} ({c/len(rs):.1%})")

summarize(group_a_ussr, "Half 1: v32 plays USSR", ussr_is_a=True)
summarize(group_a_us, "Half 2: v32 plays US", ussr_is_a=False)

# Combined: side-agnostic
all_r = list(results)
ussr_wins = sum(1 for x in all_r if x.winner == tscore.Side.USSR)
us_wins = sum(1 for x in all_r if x.winner == tscore.Side.US)
turns = Counter(x.end_turn for x in all_r)
reasons = Counter(str(x.end_reason) for x in all_r)

print(f"\n=== ALL {N} games (v32 self-play, greedy both sides) ===")
print(f"USSR wins: {ussr_wins}/{N} ({ussr_wins/N:.1%})   US wins: {us_wins}/{N} ({us_wins/N:.1%})")
mean_turn = sum(t*c for t, c in turns.items()) / N
median_sorted = sorted(x.end_turn for x in all_r)
median_turn = median_sorted[N // 2]
print(f"Mean end turn: {mean_turn:.2f}   Median: {median_turn}")
print(f"End turn distribution:")
for t in sorted(turns):
    bar = "#" * int(50 * turns[t] / N)
    print(f"  T{t:>2}: {turns[t]:>4} ({turns[t]/N:.1%})  {bar}")
print(f"End reason distribution:")
for r, c in reasons.most_common():
    print(f"  {r:<30} {c:>4} ({c/N:.1%})")

print(f"\nElapsed: {t1-t0:.1f}s")
