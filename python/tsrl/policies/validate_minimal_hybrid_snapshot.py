"""Validate a saved minimal_hybrid snapshot against the baseline policy."""
from __future__ import annotations

import argparse
import json
import random
import time
from dataclasses import fields
from pathlib import Path

from tsrl.policies.autotune_minimal_hybrid import (
    _append_jsonl,
    _bootstrap_ci,
    _paired_scores,
)
from tsrl.policies.minimal_hybrid import DEFAULT_MINIMAL_HYBRID_PARAMS, MinimalHybridParams


def _load_params(path: Path) -> MinimalHybridParams:
    payload = json.loads(path.read_text(encoding="utf-8"))
    params = payload["params"]
    default = DEFAULT_MINIMAL_HYBRID_PARAMS
    kwargs = {}
    for field in fields(MinimalHybridParams):
        value = params.get(field.name, getattr(default, field.name))
        if isinstance(getattr(default, field.name), tuple):
            value = tuple(value)
        kwargs[field.name] = value
    return MinimalHybridParams(**kwargs)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", help="Path to snapshot json")
    parser.add_argument("--pairs", type=int, default=12)
    parser.add_argument("--turn-cutoff", type=int, default=3)
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--seed", type=int, default=20260327)
    args = parser.parse_args()

    snapshot_path = Path(args.snapshot)
    payload = json.loads(snapshot_path.read_text(encoding="utf-8"))
    params = _load_params(snapshot_path)
    rng = random.Random(args.seed)
    pair_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(args.pairs))
    start_wall = time.perf_counter()
    start_cpu = time.process_time()
    scores = _paired_scores(
        params,
        pair_seeds=pair_seeds,
        turn_cutoff=(None if args.turn_cutoff == 0 else args.turn_cutoff),
        workers=args.workers,
    )
    mean_score = sum(scores) / len(scores)
    ci_low, ci_high = _bootstrap_ci(scores, seed=args.seed + 1)
    result = {
        "snapshot_id": payload["snapshot_id"],
        "label": payload["label"],
        "pairs": args.pairs,
        "turn_cutoff": None if args.turn_cutoff == 0 else args.turn_cutoff,
        "mean_score": mean_score,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "significant_positive": ci_low > 0.0,
        "wall_s": time.perf_counter() - start_wall,
        "process_s": time.process_time() - start_cpu,
    }
    _append_jsonl(
        snapshot_path.parent.parent / "history.jsonl",
        {"event": "snapshot_validation", **result},
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
