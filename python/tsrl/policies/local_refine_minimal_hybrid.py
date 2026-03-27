"""Local direct-search refinement around saved minimal_hybrid snapshots."""
from __future__ import annotations

import argparse
import json
import random
import time
from dataclasses import asdict
from pathlib import Path

from tsrl.policies.autotune_minimal_hybrid import (
    SnapshotRecord,
    _append_jsonl,
    _candidate_id,
    _make_random_candidate,
    _now_stamp,
    _params_to_dict,
    _print_validation,
    _validate_candidate,
    _validation_sort_key,
    _write_json,
)
from tsrl.policies.minimal_hybrid import DEFAULT_MINIMAL_HYBRID_PARAMS, MinimalHybridParams
from tsrl.policies.tune_minimal_hybrid import (
    CandidateEvaluation,
    EvaluationConfig,
    Evaluator,
    format_params_delta,
)
from tsrl.policies.validate_minimal_hybrid_snapshot import _load_params

_RUNS_DIR = Path("python/tsrl/policies/runs")


def _log_snapshot(
    *,
    run_dir: Path,
    history_path: Path,
    snapshot_id: str,
    label: str,
    params: MinimalHybridParams,
    source: str,
    evaluation: CandidateEvaluation,
    wall_start: float,
    process_start: float,
) -> SnapshotRecord:
    record = SnapshotRecord(
        snapshot_id=snapshot_id,
        label=label,
        params=_params_to_dict(params),
        objective=evaluation.objective,
        proxy_score=evaluation.proxy_score,
        paired_score=evaluation.paired_score,
        speed_penalty=evaluation.speed_penalty,
        created_wall_s=time.perf_counter() - wall_start,
        created_process_s=time.process_time() - process_start,
        source=source,
    )
    _write_json(run_dir / "snapshots" / f"{snapshot_id}.json", asdict(record))
    _append_jsonl(
        history_path,
        {
            "event": "candidate_evaluated",
            "snapshot_id": snapshot_id,
            "label": label,
            "source": source,
            "objective": evaluation.objective,
            "proxy_score": evaluation.proxy_score,
            "paired_score": evaluation.paired_score,
            "speed_penalty": evaluation.speed_penalty,
            "wall_s": record.created_wall_s,
            "process_s": record.created_process_s,
        },
    )
    return record


def run_local_refine(
    *,
    base_snapshots: tuple[str, ...],
    neighbors_per_base: int,
    sigma: float,
    screen_pairs: int,
    mini_pairs: int,
    full_pairs: int,
    screen_turn_cutoff: int | None,
    mini_turn_cutoff: int | None,
    full_turn_cutoff: int | None,
    workers: int,
    seed: int,
) -> dict[str, object]:
    wall_start = time.perf_counter()
    process_start = time.process_time()
    rng = random.Random(seed)
    run_stamp = _now_stamp()
    run_dir = _RUNS_DIR / run_stamp
    history_path = run_dir / "history.jsonl"

    _write_json(
        run_dir / "config.json",
        {
            "run_stamp": run_stamp,
            "seed": seed,
            "base_snapshots": list(base_snapshots),
            "neighbors_per_base": neighbors_per_base,
            "sigma": sigma,
            "screen_pairs": screen_pairs,
            "mini_pairs": mini_pairs,
            "full_pairs": full_pairs,
            "screen_turn_cutoff": screen_turn_cutoff,
            "mini_turn_cutoff": mini_turn_cutoff,
            "full_turn_cutoff": full_turn_cutoff,
            "workers": workers,
        },
    )

    evaluator = Evaluator(
        EvaluationConfig(
            mode="proxy",
            pair_seeds=(),
            speed_iterations=3,
            speed_warmup=1,
            time_weight=0.10,
            proxy_weight=1.0,
            selfplay_weight=0.0,
        )
    )

    baseline_eval = evaluator.evaluate(DEFAULT_MINIMAL_HYBRID_PARAMS)
    baseline_record = _log_snapshot(
        run_dir=run_dir,
        history_path=history_path,
        snapshot_id="baseline",
        label="baseline_default",
        params=DEFAULT_MINIMAL_HYBRID_PARAMS,
        source="baseline",
        evaluation=baseline_eval,
        wall_start=wall_start,
        process_start=process_start,
    )

    records: list[tuple[SnapshotRecord, MinimalHybridParams]] = [
        (baseline_record, DEFAULT_MINIMAL_HYBRID_PARAMS)
    ]
    for base_index, snapshot_path in enumerate(base_snapshots, start=1):
        base_params = _load_params(Path(snapshot_path))
        base_eval = evaluator.evaluate(base_params)
        base_record = _log_snapshot(
            run_dir=run_dir,
            history_path=history_path,
            snapshot_id=f"base_{base_index:02d}",
            label=f"base_{base_index:02d}",
            params=base_params,
            source=snapshot_path,
            evaluation=base_eval,
            wall_start=wall_start,
            process_start=process_start,
        )
        records.append((base_record, base_params))

        for neighbor_index in range(1, neighbors_per_base + 1):
            candidate = _make_random_candidate(base_params, rng=rng, sigma=sigma)
            candidate_eval = evaluator.evaluate(candidate)
            snapshot_id = _candidate_id(len(records))
            record = _log_snapshot(
                run_dir=run_dir,
                history_path=history_path,
                snapshot_id=snapshot_id,
                label=f"base{base_index}_neighbor_{neighbor_index}",
                params=candidate,
                source=f"neighbor_of_base_{base_index}",
                evaluation=candidate_eval,
                wall_start=wall_start,
                process_start=process_start,
            )
            records.append((record, candidate))

    screen_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(screen_pairs))
    screened: list[tuple[object, SnapshotRecord, MinimalHybridParams]] = []
    for idx, (record, params) in enumerate(records[1:], start=1):
        print(f"screen-start {idx}/{len(records) - 1} label={record.label}", flush=True)
        summary = _validate_candidate(
            params,
            label=record.label,
            pair_seeds=screen_seeds,
            turn_cutoff=screen_turn_cutoff,
            seed=seed + idx,
            workers=workers,
        )
        _append_jsonl(
            history_path,
            {"event": "screen_validation", "snapshot_id": record.snapshot_id, **asdict(summary)},
        )
        _print_validation("screen-validation", summary)
        screened.append((summary, record, params))

    screened.sort(key=lambda item: _validation_sort_key(item[0]), reverse=True)
    shortlisted = screened[:4]

    mini_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(mini_pairs))
    best_mini = None
    best_params = DEFAULT_MINIMAL_HYBRID_PARAMS
    for idx, (screen_summary, record, params) in enumerate(shortlisted, start=1):
        print(f"mini-start {idx}/{len(shortlisted)} label={record.label}", flush=True)
        summary = _validate_candidate(
            params,
            label=record.label,
            pair_seeds=mini_seeds,
            turn_cutoff=mini_turn_cutoff,
            seed=seed + 1000 + idx,
            workers=workers,
        )
        _append_jsonl(
            history_path,
            {"event": "mini_validation", "snapshot_id": record.snapshot_id, **asdict(summary)},
        )
        _print_validation("mini-validation", summary)
        if best_mini is None or _validation_sort_key(summary) > _validation_sort_key(best_mini):
            best_mini = summary
            best_params = params

    full_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(full_pairs))
    full_summary = _validate_candidate(
        best_params,
        label="best_local_refine",
        pair_seeds=full_seeds,
        turn_cutoff=full_turn_cutoff,
        seed=seed + 2000,
        workers=workers,
    )
    _append_jsonl(history_path, {"event": "full_validation", **asdict(full_summary)})
    _print_validation("full-validation", full_summary)

    summary_payload = {
        "run_stamp": run_stamp,
        "screen_validation": asdict(screened[0][0]) if screened else None,
        "mini_validation": asdict(best_mini) if best_mini is not None else None,
        "full_validation": asdict(full_summary),
        "best_local_params_delta": format_params_delta(best_params),
        "wall_s_total": time.perf_counter() - wall_start,
        "process_s_total": time.process_time() - process_start,
    }
    _write_json(run_dir / "summary.json", summary_payload)
    return summary_payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-snapshot", action="append", required=True)
    parser.add_argument("--neighbors-per-base", type=int, default=8)
    parser.add_argument("--sigma", type=float, default=0.15)
    parser.add_argument("--screen-pairs", type=int, default=2)
    parser.add_argument("--mini-pairs", type=int, default=12)
    parser.add_argument("--full-pairs", type=int, default=6)
    parser.add_argument("--screen-turn-cutoff", type=int, default=4)
    parser.add_argument("--mini-turn-cutoff", type=int, default=4)
    parser.add_argument("--full-turn-cutoff", type=int, default=6)
    parser.add_argument("--workers", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260327)
    args = parser.parse_args()

    summary = run_local_refine(
        base_snapshots=tuple(args.base_snapshot),
        neighbors_per_base=args.neighbors_per_base,
        sigma=args.sigma,
        screen_pairs=args.screen_pairs,
        mini_pairs=args.mini_pairs,
        full_pairs=args.full_pairs,
        screen_turn_cutoff=(None if args.screen_turn_cutoff == 0 else args.screen_turn_cutoff),
        mini_turn_cutoff=(None if args.mini_turn_cutoff == 0 else args.mini_turn_cutoff),
        full_turn_cutoff=(None if args.full_turn_cutoff == 0 else args.full_turn_cutoff),
        workers=args.workers,
        seed=args.seed,
    )
    print("")
    print("local-refine-summary")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
