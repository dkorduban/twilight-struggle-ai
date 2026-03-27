"""Measure full-game end-reason frequencies for minimal_hybrid policies."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from tsrl.engine.game_loop import play_game
from tsrl.policies.minimal_hybrid import DEFAULT_MINIMAL_HYBRID_PARAMS, make_minimal_hybrid_policy
from tsrl.policies.validate_minimal_hybrid_snapshot import _load_params


def _task(payload: tuple[str, int, str | None]) -> str:
    mode, seed, snapshot = payload
    baseline = make_minimal_hybrid_policy(DEFAULT_MINIMAL_HYBRID_PARAMS)
    candidate = baseline
    if snapshot is not None:
        candidate = make_minimal_hybrid_policy(_load_params(Path(snapshot)))

    if mode == "baseline_selfplay":
        result = play_game(baseline, baseline, seed=seed)
    elif mode == "candidate_vs_baseline":
        result = play_game(candidate, baseline, seed=seed)
    elif mode == "baseline_vs_candidate":
        result = play_game(baseline, candidate, seed=seed)
    else:
        raise ValueError(f"Unknown mode: {mode}")
    return result.end_reason


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("baseline_selfplay", "candidate_vs_baseline", "baseline_vs_candidate"),
        default="baseline_selfplay",
    )
    parser.add_argument("--snapshot", help="Candidate snapshot for non-baseline modes")
    parser.add_argument("--games", type=int, default=20)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--seed-start", type=int, default=10_000)
    args = parser.parse_args()

    if args.mode != "baseline_selfplay" and args.snapshot is None:
        raise SystemExit("--snapshot is required for candidate modes")

    tasks = [
        (args.mode, seed, args.snapshot)
        for seed in range(args.seed_start, args.seed_start + args.games)
    ]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        reasons = list(pool.map(_task, tasks))

    counts = Counter(reasons)
    total = sum(counts.values())
    payload = {
        "mode": args.mode,
        "snapshot": args.snapshot,
        "games": total,
        "workers": args.workers,
        "seed_start": args.seed_start,
        "defcon1_rate": counts.get("defcon1", 0) / total if total else 0.0,
        "counts": dict(sorted(counts.items())),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
