#!/usr/bin/env python3
"""v55 ISMCTS benchmark grid: {(4,50), (2,50), (4,25)} x {self-play, heuristic}.

Fixed: pool=16, max_pending_per_det=8, device=cpu, torch intra_threads=4.
100 games per side (200 total per config).

Reports: USSR WR, US WR, combined, wall time, games/s, sims/s.
"""
import ctypes
import os
import re
import sys
import tempfile
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

_libc = ctypes.CDLL(None)

MODEL       = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
GAMES_SIDE  = 100
POOL        = 16
PEND        = 8
DEVICE      = "cpu"
INTRA       = 4
SEED_USSR   = 50000
SEED_US     = 50500
SEED_SELF   = 60000   # for self-play both_sides (split internally)

CONFIGS = [("4x50", 4, 50), ("2x50", 2, 50), ("4x25", 4, 25)]


def capture_fds(func, *args, **kwargs):
    tmp = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".log")
    tmp.close()
    sys.stdout.flush(); sys.stderr.flush()
    s1 = os.dup(1); s2 = os.dup(2)
    fd = os.open(tmp.name, os.O_WRONLY | os.O_TRUNC)
    os.dup2(fd, 1); os.dup2(fd, 2); os.close(fd)
    try:
        result = func(*args, **kwargs)
    finally:
        _libc.fflush(None)
        os.dup2(s1, 1); os.dup2(s2, 2); os.close(s1); os.close(s2)
    with open(tmp.name) as f:
        captured = f.read()
    os.unlink(tmp.name)
    return result, captured


def parse_profile(captured):
    totals, items = [], []
    for line in captured.splitlines():
        m = re.search(r"total=([0-9.]+)s", line)
        if m: totals.append(float(m.group(1)))
        m = re.search(r"items=([0-9]+)", line)
        if m: items.append(int(m.group(1)))
    t = sum(totals) if totals else None
    n = sum(items) if items else None
    return n, t


def run_selfplay(n_det, n_sim):
    t0 = time.perf_counter()
    results, captured = capture_fds(
        tscore.benchmark_ismcts_vs_model_both_sides,
        MODEL, MODEL,
        n_games=2 * GAMES_SIDE,
        n_determinizations=n_det, n_simulations=n_sim,
        seed=SEED_SELF, pool_size=POOL, max_pending_per_det=PEND, device=DEVICE,
    )
    elapsed = time.perf_counter() - t0
    # First half = ISMCTS as USSR, second half = ISMCTS as US
    ussr_res = results[:GAMES_SIDE]
    us_res   = results[GAMES_SIDE:]
    ussr_wr = sum(1 for r in ussr_res if r.winner == tscore.Side.USSR) / GAMES_SIDE
    us_wr   = sum(1 for r in us_res   if r.winner == tscore.Side.US)   / GAMES_SIDE
    items, search_t = parse_profile(captured)
    return ussr_wr, us_wr, elapsed, items, search_t


def run_heuristic(n_det, n_sim):
    t0 = time.perf_counter()
    # ISMCTS as USSR vs heuristic
    res_ussr, cap1 = capture_fds(
        tscore.benchmark_ismcts,
        MODEL, tscore.Side.USSR, GAMES_SIDE,
        n_determinizations=n_det, n_simulations=n_sim,
        seed=SEED_USSR, pool_size=POOL, max_pending_per_det=PEND, device=DEVICE,
    )
    # ISMCTS as US vs heuristic
    res_us, cap2 = capture_fds(
        tscore.benchmark_ismcts,
        MODEL, tscore.Side.US, GAMES_SIDE,
        n_determinizations=n_det, n_simulations=n_sim,
        seed=SEED_US, pool_size=POOL, max_pending_per_det=PEND, device=DEVICE,
    )
    elapsed = time.perf_counter() - t0
    ussr_wr = sum(1 for r in res_ussr if r.winner == tscore.Side.USSR) / GAMES_SIDE
    us_wr   = sum(1 for r in res_us   if r.winner == tscore.Side.US)   / GAMES_SIDE
    i1, t1 = parse_profile(cap1)
    i2, t2 = parse_profile(cap2)
    items    = (i1 or 0) + (i2 or 0) if (i1 or i2) else None
    search_t = (t1 or 0) + (t2 or 0) if (t1 or t2) else None
    return ussr_wr, us_wr, elapsed, items, search_t


def main():
    torch.set_num_threads(INTRA)

    print(f"v55 ISMCTS benchmark", flush=True)
    print(f"  model       = {MODEL}", flush=True)
    print(f"  pool_size   = {POOL}", flush=True)
    print(f"  pend/det    = {PEND}", flush=True)
    print(f"  device      = {DEVICE}", flush=True)
    print(f"  intra_threads = {INTRA}", flush=True)
    print(f"  games/side  = {GAMES_SIDE}  (total 2*{GAMES_SIDE} per config)", flush=True)
    print(flush=True)

    hdr = f"{'config':>8} {'opponent':>10} {'ussr_wr':>8} {'us_wr':>6} {'comb':>6} {'time(s)':>8} {'games/s':>8} {'sims/s':>8}"
    print(hdr, flush=True)
    print("-" * len(hdr), flush=True)

    for tag, n_det, n_sim in CONFIGS:
        # self-play
        ussr_wr, us_wr, elapsed, items, st = run_selfplay(n_det, n_sim)
        comb = (ussr_wr + us_wr) / 2
        gps  = (2 * GAMES_SIDE) / elapsed
        sps  = f"{items/st:.1f}" if (items and st) else "N/A"
        print(
            f"{tag:>8} {'self':>10} {ussr_wr:>8.3f} {us_wr:>6.3f} {comb:>6.3f} "
            f"{elapsed:>8.1f} {gps:>8.3f} {sps:>8}",
            flush=True,
        )

        # heuristic
        ussr_wr, us_wr, elapsed, items, st = run_heuristic(n_det, n_sim)
        comb = (ussr_wr + us_wr) / 2
        gps  = (2 * GAMES_SIDE) / elapsed
        sps  = f"{items/st:.1f}" if (items and st) else "N/A"
        print(
            f"{tag:>8} {'heuristic':>10} {ussr_wr:>8.3f} {us_wr:>6.3f} {comb:>6.3f} "
            f"{elapsed:>8.1f} {gps:>8.3f} {sps:>8}",
            flush=True,
        )


if __name__ == "__main__":
    main()
