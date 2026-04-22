#!/usr/bin/env python3
"""Temperature sweep: panel models (v20, v44, v54, v55, v56) vs heuristic.

NN side temperature ∈ {0.0, 0.5, 1.0, 1.5, 2.0}.
Heuristic side uses Nash-mix temperatures (panel default).
50 games/side → 100 games/config.

Reports: per-model × per-T combined WR, and per-side split.
Designed to be resource-light (pool=16, intra=4) so it runs alongside ISMCTS.
"""
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

CKPT_DIR = "data/checkpoints/scripted_for_elo"
MODELS = ["v20", "v44", "v54", "v55", "v56"]
TEMPS  = [0.0, 0.5, 1.0, 1.5, 2.0]

GAMES_SIDE = 50
POOL       = 16
DEVICE     = "cpu"
INTRA      = 4
SEED_USSR  = 70000
SEED_US    = 70500


def run_one(model_path, side, n_games, temperature, seed):
    results = tscore.benchmark_batched(
        model_path,
        side,
        n_games,
        pool_size=POOL,
        seed=seed,
        device=DEVICE,
        greedy_opponent=False,
        temperature=temperature,
        nash_temperatures=True,
    )
    wins = sum(1 for r in results if r.winner == side)
    return wins / n_games


def main():
    torch.set_num_threads(INTRA)

    print("Panel × Temperature sweep vs heuristic (nash temps on heur side)", flush=True)
    print(f"  games/side={GAMES_SIDE}  pool={POOL}  intra={INTRA}", flush=True)
    print(flush=True)

    hdr = f"{'model':>5} {'T':>4} {'ussr':>6} {'us':>6} {'comb':>6} {'t(s)':>6}"
    print(hdr, flush=True)
    print("-" * len(hdr), flush=True)

    # Run model-by-model, T-by-T. Interleave so partial output is useful.
    for model in MODELS:
        path = f"{CKPT_DIR}/{model}_scripted.pt"
        for T in TEMPS:
            t0 = time.perf_counter()
            ussr_wr = run_one(path, tscore.Side.USSR, GAMES_SIDE, T, SEED_USSR)
            us_wr   = run_one(path, tscore.Side.US,   GAMES_SIDE, T, SEED_US)
            elapsed = time.perf_counter() - t0
            comb = (ussr_wr + us_wr) / 2
            print(
                f"{model:>5} {T:>4.1f} {ussr_wr:>6.3f} {us_wr:>6.3f} {comb:>6.3f} {elapsed:>6.1f}",
                flush=True,
            )


if __name__ == "__main__":
    main()
