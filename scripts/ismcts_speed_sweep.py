#!/usr/bin/env python3
"""ISMCTS throughput sweep.

Sweeps pool_size x max_pending_per_det x device, with intra_threads on CPU.

Semantics (from cpp/tscore/ismcts.cpp):
  pool_size           = number of concurrent games (single-threaded cooperative loop,
                        NOT a thread pool — just contributes to NN batch size)
  max_pending_per_det = virtual-loss depth per determinization (tree-traversal
                        batching; up to this many leaves selected per det before NN fires)
  max_batch           = pool_size * n_det * max_pending_per_det  (NN batch ceiling)
  intra_threads       = torch.set_num_threads  (CPU BLAS intra-op parallelism;
                        same underlying knob as C++ at::set_num_threads)

Reports:
  games/s  — wall-clock games per second (always available)
  sims/s   — NN evaluations per second, parsed from C++ profile lines
             (via fd1+fd2 redirect with libc fflush). "N/A" if capture fails.
  WR       — combined win rate (ISMCTS as USSR + ISMCTS as US) / 2
"""
import ctypes
import itertools
import os
import re
import sys
import tempfile
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

_libc = ctypes.CDLL(None)

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"
N_GAMES = 20
N_DET = 4
N_SIM = 50
SEED = 99000

POOL_SIZES    = [8, 16, 32]
MAX_PENDINGS  = [4, 8, 16]
INTRA_THREADS = [1, 4, 8]  # CPU only; CUDA ignores this


def capture_fds(func, *args, **kwargs):
    """Run func() while fd1 and fd2 are redirected to a temp file.

    Returns (result, captured_text). Uses libc fflush(NULL) before restoring
    so C stdio buffers (std::cout, fmt::print) land in the capture file.
    """
    tmp = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".log")
    tmp.close()

    sys.stdout.flush()
    sys.stderr.flush()
    saved_1 = os.dup(1)
    saved_2 = os.dup(2)
    fd = os.open(tmp.name, os.O_WRONLY | os.O_TRUNC)
    os.dup2(fd, 1)
    os.dup2(fd, 2)
    os.close(fd)
    try:
        result = func(*args, **kwargs)
    finally:
        _libc.fflush(None)   # flush all C stdio streams (cout, fmt, stderr)
        os.dup2(saved_1, 1)
        os.dup2(saved_2, 2)
        os.close(saved_1)
        os.close(saved_2)

    with open(tmp.name) as f:
        captured = f.read()
    os.unlink(tmp.name)
    return result, captured


def run_config(pool_size, max_pending, device, intra_threads):
    torch.set_num_threads(intra_threads)

    t0 = time.perf_counter()
    results, captured = capture_fds(
        tscore.benchmark_ismcts_vs_model_both_sides,
        MODEL, MODEL,
        n_games=N_GAMES,
        n_determinizations=N_DET,
        n_simulations=N_SIM,
        seed=SEED,
        pool_size=pool_size,
        max_pending_per_det=max_pending,
        device=device,
    )
    elapsed = time.perf_counter() - t0

    # Parse C++ profile: lines like
    #   [ISMCTS vs model profile] advance=X select=Y nn=Z expand=A apply=B total=T
    #   [ISMCTS vs model profile] batches=N items=M avg_batch=K
    totals, items = [], []
    for line in captured.splitlines():
        m = re.search(r"total=([0-9.]+)s", line)
        if m:
            totals.append(float(m.group(1)))
        m = re.search(r"items=([0-9]+)", line)
        if m:
            items.append(int(m.group(1)))

    total_items       = sum(items) if items else None
    total_search_time = sum(totals) if totals else None
    sims_per_s        = (total_items / total_search_time) if (total_items and total_search_time) else None
    games_per_s       = N_GAMES / elapsed

    n_each   = N_GAMES // 2
    ussr_wr  = sum(1 for r in results[:n_each] if r.winner == tscore.Side.USSR) / n_each
    us_wr    = sum(1 for r in results[n_each:] if r.winner == tscore.Side.US)   / n_each
    combined = (ussr_wr + us_wr) / 2

    return {
        "elapsed":     elapsed,
        "games_per_s": games_per_s,
        "items":       total_items,
        "search_time": total_search_time,
        "sims_per_s":  sims_per_s,
        "combined":    combined,
        "capture_bytes": len(captured),
    }


def build_configs():
    # Interleave: for each (pool, pend), yield all CPU intra variants, then CUDA.
    # Keeps per-(pool,pend) comparisons adjacent in the output table.
    for pool, pend in itertools.product(POOL_SIZES, MAX_PENDINGS):
        for intra in INTRA_THREADS:
            yield (pool, pend, "cpu", intra)
        yield (pool, pend, "cuda", 1)


def main():
    configs = list(build_configs())
    print(f"ISMCTS speed sweep ({len(configs)} configs)", flush=True)
    print(f"  model     = {MODEL}", flush=True)
    print(f"  n_games   = {N_GAMES}  (half as USSR, half as US)", flush=True)
    print(f"  n_det     = {N_DET}", flush=True)
    print(f"  n_sim     = {N_SIM}", flush=True)
    print(flush=True)

    COLS = [
        ("pool",    4),
        ("pend",    4),
        ("dev",     4),
        ("intra",   5),
        ("mbatch",  6),
        ("time(s)", 7),
        ("games/s", 7),
        ("sims/s",  8),
        ("items",   8),
        ("WR",      6),
    ]
    hdr = " ".join(f"{name:>{w}}" for name, w in COLS)
    print(hdr, flush=True)
    print("-" * len(hdr), flush=True)

    rows = []
    for pool, pend, dev, intra in configs:
        mbatch = pool * N_DET * pend
        try:
            r = run_config(pool, pend, dev, intra)
            sps   = f"{r['sims_per_s']:.1f}" if r['sims_per_s'] is not None else "N/A"
            items = f"{r['items']}"           if r['items']      is not None else "N/A"
            line = (
                f"{pool:>4} {pend:>4} {dev:>4} {intra:>5} {mbatch:>6} "
                f"{r['elapsed']:>7.1f} {r['games_per_s']:>7.3f} {sps:>8} {items:>8} "
                f"{r['combined']:>6.3f}"
            )
            print(line, flush=True)
            rows.append((pool, pend, dev, intra, mbatch, r))
        except Exception as e:
            print(f"{pool:>4} {pend:>4} {dev:>4} {intra:>5} {mbatch:>6}  ERROR: {e}", flush=True)

    print(flush=True)
    # Summary: best by sims/s if captured, else best by games/s. Per device.
    for dev in ("cpu", "cuda"):
        sub = [row for row in rows if row[2] == dev]
        if not sub:
            continue
        with_sps = [row for row in sub if row[5]['sims_per_s'] is not None]
        if with_sps:
            best = max(with_sps, key=lambda row: row[5]['sims_per_s'])
            pool, pend, _, intra, mb, r = best
            print(
                f"Best {dev}: pool={pool} pend={pend} intra={intra} mbatch={mb}  "
                f"-> {r['sims_per_s']:.1f} sims/s, {r['games_per_s']:.3f} games/s",
                flush=True,
            )
        else:
            best = max(sub, key=lambda row: row[5]['games_per_s'])
            pool, pend, _, intra, mb, r = best
            print(
                f"Best {dev}: pool={pool} pend={pend} intra={intra} mbatch={mb}  "
                f"-> {r['games_per_s']:.3f} games/s  (sims/s unavailable — fd capture returned empty)",
                flush=True,
            )


if __name__ == "__main__":
    main()
