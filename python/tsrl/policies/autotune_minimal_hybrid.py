"""Autonomous tuning campaign for minimal_hybrid.

This runner preserves the current baseline policy, logs every candidate
snapshot and evaluation, tracks wall/process time, and validates the best
candidate with confidence intervals.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import random
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass
from pathlib import Path

from tsrl.engine.game_loop import (
    GameResult,
    _ars_for_turn,
    _end_of_turn,
    _run_action_rounds,
    _run_headline_phase,
)
from tsrl.engine.game_state import (
    advance_to_late_war,
    advance_to_mid_war,
    deal_cards,
    reset,
)
from tsrl.policies.minimal_hybrid import (
    DEFAULT_MINIMAL_HYBRID_PARAMS,
    MinimalHybridParams,
    make_minimal_hybrid_policy,
)
from tsrl.policies.tune_minimal_hybrid import (
    EvaluationConfig,
    Evaluator,
    clip_vector,
    flatten_params,
    format_params_delta,
    unflatten_params,
)
from tsrl.schemas import Side

_RUNS_DIR = Path("results/logs/autotune_runs")
_INDEX_FILE = _RUNS_DIR / "index.jsonl"
_PERTURBATION_SCALE = (
    (0.10,) * 21
    + (
        0.30,
        0.30,
        0.20,
        0.20,
        0.03,
        0.30,
        0.15,
        0.20,
        0.40,
        0.25,
        0.25,
        0.05,
        0.15,
        0.15,
        0.10,
        0.15,
        0.05,
        0.15,
        0.20,
        0.10,
        0.25,
        0.25,
        0.15,
        0.05,
        0.20,
        0.10,
        0.10,
    )
)


@dataclass(frozen=True)
class ValidationSummary:
    label: str
    mean_score: float
    ci_low: float
    ci_high: float
    n_pairs: int
    significant_positive: bool
    turn_cutoff: int | None


@dataclass(frozen=True)
class SnapshotRecord:
    snapshot_id: str
    label: str
    params: dict[str, object]
    objective: float
    proxy_score: float
    paired_score: float
    speed_penalty: float
    created_wall_s: float
    created_process_s: float
    source: str


def _now_stamp() -> str:
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


def _params_to_dict(params: MinimalHybridParams) -> dict[str, object]:
    return asdict(params)


def _score_from_result(result: GameResult, candidate_side: Side) -> float:
    winner_score = 0.0
    if result.winner == candidate_side:
        winner_score = 1.0
    elif result.winner is not None:
        winner_score = -1.0

    vp_score = max(-1.0, min(1.0, result.final_vp / 20.0))
    if candidate_side == Side.US:
        vp_score = -vp_score
    return 0.75 * winner_score + 0.25 * vp_score


def _play_game_to_turn(
    ussr_policy,
    us_policy,
    *,
    seed: int,
    max_turn: int,
) -> GameResult:
    rng = random.Random(seed)
    gs = reset(seed=rng.randint(0, 2**32))

    for turn in range(1, max_turn + 1):
        gs.pub.turn = turn
        if turn == 4:
            advance_to_mid_war(gs, rng)
        elif turn == 8:
            advance_to_late_war(gs, rng)

        deal_cards(gs, Side.USSR, rng)
        deal_cards(gs, Side.US, rng)

        result = _run_headline_phase(gs, ussr_policy, us_policy, rng)
        if result is not None:
            return result

        total_ars = _ars_for_turn(turn)
        result = _run_action_rounds(gs, ussr_policy, us_policy, rng, total_ars)
        if result is not None:
            return result

        result = _end_of_turn(gs, rng, turn)
        if result is not None:
            return result

    winner: Side | None
    if gs.pub.vp > 0:
        winner = Side.USSR
    elif gs.pub.vp < 0:
        winner = Side.US
    else:
        winner = None
    return GameResult(
        winner=winner,
        final_vp=gs.pub.vp,
        end_turn=max_turn,
        end_reason="turn_cutoff",
    )


def _paired_scores(
    params: MinimalHybridParams,
    *,
    pair_seeds: tuple[int, ...],
    turn_cutoff: int | None,
    workers: int,
) -> list[float]:
    tasks = [(params, seed, turn_cutoff) for seed in pair_seeds]
    if workers <= 1:
        return [_paired_score_task(task) for task in tasks]
    with ProcessPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(_paired_score_task, tasks))


def _play_full_game(ussr_policy, us_policy, seed: int) -> GameResult:
    from tsrl.engine.game_loop import play_game

    return play_game(ussr_policy, us_policy, seed=seed)


def _paired_score_task(task: tuple[MinimalHybridParams, int, int | None]) -> float:
    params, seed, turn_cutoff = task
    candidate_policy = make_minimal_hybrid_policy(params)
    baseline_policy = make_minimal_hybrid_policy(DEFAULT_MINIMAL_HYBRID_PARAMS)
    if turn_cutoff is None:
        result_a = _play_full_game(candidate_policy, baseline_policy, seed)
        result_b = _play_full_game(baseline_policy, candidate_policy, seed)
    else:
        result_a = _play_game_to_turn(
            candidate_policy,
            baseline_policy,
            seed=seed,
            max_turn=turn_cutoff,
        )
        result_b = _play_game_to_turn(
            baseline_policy,
            candidate_policy,
            seed=seed,
            max_turn=turn_cutoff,
        )
    return 0.5 * (
        _score_from_result(result_a, Side.USSR)
        + _score_from_result(result_b, Side.US)
    )


def _evaluate_candidate_task(
    task: tuple[EvaluationConfig, MinimalHybridParams],
) -> tuple[MinimalHybridParams, object]:
    config, params = task
    evaluator = Evaluator(config)
    return params, evaluator.evaluate(params)


def _bootstrap_ci(scores: list[float], *, seed: int, samples: int = 2000) -> tuple[float, float]:
    if not scores:
        return 0.0, 0.0
    if len(scores) == 1:
        return scores[0], scores[0]
    rng = random.Random(seed)
    means: list[float] = []
    for _ in range(samples):
        sample = [scores[rng.randrange(len(scores))] for _ in scores]
        means.append(sum(sample) / len(sample))
    means.sort()
    low_idx = int(0.025 * (samples - 1))
    high_idx = int(0.975 * (samples - 1))
    return means[low_idx], means[high_idx]


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _append_jsonl(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\n")


def _candidate_id(index: int) -> str:
    return f"candidate_{index:04d}"


def _make_random_candidate(
    base: MinimalHybridParams,
    *,
    rng: random.Random,
    sigma: float,
) -> MinimalHybridParams:
    base_vec = flatten_params(base)
    proposal = []
    for value, scale in zip(base_vec, _PERTURBATION_SCALE, strict=True):
        proposal.append(value + rng.gauss(0.0, sigma * scale))
    return unflatten_params(clip_vector(tuple(proposal)))


def _evaluate_and_log(
    *,
    run_dir: Path,
    history_path: Path,
    snapshot_id: str,
    label: str,
    params: MinimalHybridParams,
    evaluator: Evaluator,
    source: str,
    wall_start: float,
    process_start: float,
) -> tuple[SnapshotRecord, object]:
    evaluation = evaluator.evaluate(params)
    wall_elapsed = time.perf_counter() - wall_start
    process_elapsed = time.process_time() - process_start
    record = SnapshotRecord(
        snapshot_id=snapshot_id,
        label=label,
        params=_params_to_dict(params),
        objective=evaluation.objective,
        proxy_score=evaluation.proxy_score,
        paired_score=evaluation.paired_score,
        speed_penalty=evaluation.speed_penalty,
        created_wall_s=wall_elapsed,
        created_process_s=process_elapsed,
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
            "wall_s": wall_elapsed,
            "process_s": process_elapsed,
        },
    )
    return record, evaluation


def _validate_candidate(
    params: MinimalHybridParams,
    *,
    label: str,
    pair_seeds: tuple[int, ...],
    turn_cutoff: int | None,
    seed: int,
    workers: int,
) -> ValidationSummary:
    scores = _paired_scores(
        params,
        pair_seeds=pair_seeds,
        turn_cutoff=turn_cutoff,
        workers=workers,
    )
    mean_score = sum(scores) / len(scores)
    ci_low, ci_high = _bootstrap_ci(scores, seed=seed)
    return ValidationSummary(
        label=label,
        mean_score=mean_score,
        ci_low=ci_low,
        ci_high=ci_high,
        n_pairs=len(scores),
        significant_positive=ci_low > 0.0,
        turn_cutoff=turn_cutoff,
    )


def _print_validation(prefix: str, summary: ValidationSummary) -> None:
    cutoff = "full" if summary.turn_cutoff is None else f"turn{summary.turn_cutoff}"
    print(
        f"{prefix} label={summary.label} cutoff={cutoff} "
        f"mean={summary.mean_score:.4f} "
        f"ci95=[{summary.ci_low:.4f}, {summary.ci_high:.4f}] "
        f"pairs={summary.n_pairs} sig={summary.significant_positive}"
    , flush=True)


def _validation_sort_key(summary: ValidationSummary) -> tuple[int, float]:
    return (1 if summary.significant_positive else 0, summary.mean_score)


def run_campaign(
    *,
    proxy_candidates: int,
    proxy_sigma: float,
    proxy_steps: int,
    screen_candidates: int,
    screen_pairs: int,
    screen_turn_cutoff: int | None,
    refine_candidates: int,
    refine_sigma: float,
    shortlist_size: int,
    mini_pairs: int,
    full_pairs: int,
    mini_turn_cutoff: int,
    full_turn_cutoff: int | None,
    workers: int,
    seed: int,
) -> dict[str, object]:
    wall_start = time.perf_counter()
    process_start = time.process_time()
    run_stamp = _now_stamp()
    run_dir = _RUNS_DIR / run_stamp
    history_path = run_dir / "history.jsonl"
    rng = random.Random(seed)

    config = EvaluationConfig(
        mode="proxy",
        pair_seeds=(),
        speed_iterations=3,
        speed_warmup=1,
        time_weight=0.10,
        proxy_weight=1.0,
        selfplay_weight=0.0,
    )
    evaluator = Evaluator(config)

    _write_json(
        run_dir / "config.json",
        {
            "run_stamp": run_stamp,
            "seed": seed,
            "proxy_candidates": proxy_candidates,
            "proxy_sigma": proxy_sigma,
            "proxy_steps": proxy_steps,
            "screen_candidates": screen_candidates,
            "screen_pairs": screen_pairs,
            "screen_turn_cutoff": screen_turn_cutoff,
            "refine_candidates": refine_candidates,
            "refine_sigma": refine_sigma,
            "shortlist_size": shortlist_size,
            "mini_pairs": mini_pairs,
            "full_pairs": full_pairs,
            "mini_turn_cutoff": mini_turn_cutoff,
            "full_turn_cutoff": full_turn_cutoff,
            "workers": workers,
        },
    )

    baseline_record, baseline_eval = _evaluate_and_log(
        run_dir=run_dir,
        history_path=history_path,
        snapshot_id="baseline",
        label="baseline_default",
        params=DEFAULT_MINIMAL_HYBRID_PARAMS,
        evaluator=evaluator,
        source="baseline",
        wall_start=wall_start,
        process_start=process_start,
    )
    best_params = DEFAULT_MINIMAL_HYBRID_PARAMS
    best_eval = baseline_eval
    best_record = baseline_record
    incumbent_vec = flatten_params(DEFAULT_MINIMAL_HYBRID_PARAMS)
    candidate_records: list[tuple[SnapshotRecord, object, MinimalHybridParams]] = [
        (baseline_record, baseline_eval, DEFAULT_MINIMAL_HYBRID_PARAMS)
    ]

    print(
        f"campaign start run={run_stamp} baseline_proxy={baseline_eval.proxy_score:.4f} "
        f"baseline_us={baseline_eval.candidate_us_per_decision:.1f}"
    , flush=True)

    random_candidates = [
        _make_random_candidate(best_params, rng=rng, sigma=proxy_sigma)
        for _ in range(proxy_candidates)
    ]
    if workers <= 1:
        random_results = [
            (candidate, evaluator.evaluate(candidate))
            for candidate in random_candidates
        ]
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            random_results = list(
                pool.map(
                    _evaluate_candidate_task,
                    [(config, candidate) for candidate in random_candidates],
                )
            )

    for idx, (candidate, evaluation) in enumerate(random_results, start=1):
        snapshot_id = _candidate_id(idx)
        record = SnapshotRecord(
            snapshot_id=snapshot_id,
            label=f"random_{idx}",
            params=_params_to_dict(candidate),
            objective=evaluation.objective,
            proxy_score=evaluation.proxy_score,
            paired_score=evaluation.paired_score,
            speed_penalty=evaluation.speed_penalty,
            created_wall_s=time.perf_counter() - wall_start,
            created_process_s=time.process_time() - process_start,
            source="random_proxy_search",
        )
        _write_json(run_dir / "snapshots" / f"{snapshot_id}.json", asdict(record))
        _append_jsonl(
            history_path,
            {
                "event": "candidate_evaluated",
                "snapshot_id": snapshot_id,
                "label": record.label,
                "source": record.source,
                "objective": evaluation.objective,
                "proxy_score": evaluation.proxy_score,
                "paired_score": evaluation.paired_score,
                "speed_penalty": evaluation.speed_penalty,
                "wall_s": record.created_wall_s,
                "process_s": record.created_process_s,
            },
        )
        candidate_records.append((record, evaluation, candidate))
        if evaluation.objective > best_eval.objective:
            best_params = candidate
            best_eval = evaluation
            best_record = record
            incumbent_vec = flatten_params(candidate)
        if idx % 10 == 0 or idx == proxy_candidates:
            print(
                f"proxy-search {idx}/{proxy_candidates} best_proxy={best_eval.proxy_score:.4f} "
                f"best_obj={best_eval.objective:.4f}",
                flush=True,
            )

    theta = incumbent_vec
    for step in range(1, proxy_steps + 1):
        delta = tuple(rng.choice((-1.0, 1.0)) for _ in theta)
        step_scale = 0.20 / math.sqrt(step)
        theta_plus = clip_vector(
            tuple(
                v + step_scale * s * d
                for v, s, d in zip(theta, _PERTURBATION_SCALE, delta, strict=True)
            )
        )
        theta_minus = clip_vector(
            tuple(
                v - step_scale * s * d
                for v, s, d in zip(theta, _PERTURBATION_SCALE, delta, strict=True)
            )
        )
        for suffix, candidate_theta in (("plus", theta_plus), ("minus", theta_minus)):
            candidate = unflatten_params(candidate_theta)
            offset = 2 * step - 1 if suffix == "plus" else 2 * step
            snapshot_id = _candidate_id(proxy_candidates + offset)
            record, evaluation = _evaluate_and_log(
                run_dir=run_dir,
                history_path=history_path,
                snapshot_id=snapshot_id,
                label=f"spsa_{step}_{suffix}",
                params=candidate,
                evaluator=evaluator,
                source="proxy_spsa",
                wall_start=wall_start,
                process_start=process_start,
            )
            candidate_records.append((record, evaluation, candidate))
            if evaluation.objective > best_eval.objective:
                best_params = candidate
                best_eval = evaluation
                best_record = record
                theta = candidate_theta
        print(
            f"proxy-spsa step={step}/{proxy_steps} best_proxy={best_eval.proxy_score:.4f} "
            f"best_obj={best_eval.objective:.4f}"
        , flush=True)

    proxy_ranked = sorted(
        candidate_records,
        key=lambda item: item[1].objective,
        reverse=True,
    )
    screened_pool = proxy_ranked[: max(shortlist_size, screen_candidates)]

    shortlisted = screened_pool[:shortlist_size]
    best_screen_validation: ValidationSummary | None = None
    if screen_pairs > 0:
        screen_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(screen_pairs))
        screened_results: list[
            tuple[ValidationSummary, SnapshotRecord, object, MinimalHybridParams]
        ] = []
        for idx, (record, evaluation, params) in enumerate(screened_pool, start=1):
            print(
                f"screen-validation-start {idx}/{len(screened_pool)} label={record.label}",
                flush=True,
            )
            summary = _validate_candidate(
                params,
                label=record.label,
                pair_seeds=screen_seeds,
                turn_cutoff=screen_turn_cutoff,
                seed=seed + 10_000 + idx,
                workers=workers,
            )
            _append_jsonl(
                history_path,
                {
                    "event": "screen_validation",
                    "snapshot_id": record.snapshot_id,
                    **asdict(summary),
                },
            )
            _print_validation("screen-validation", summary)
            if (
                best_screen_validation is None
                or _validation_sort_key(summary)
                > _validation_sort_key(best_screen_validation)
            ):
                best_screen_validation = summary
            screened_results.append((summary, record, evaluation, params))

        if refine_candidates > 0 and best_screen_validation is not None:
            refine_base = max(
                screened_results,
                key=lambda item: _validation_sort_key(item[0]),
            )
            _, _, _, refine_params = refine_base
            for idx in range(1, refine_candidates + 1):
                refined = _make_random_candidate(
                    refine_params,
                    rng=rng,
                    sigma=refine_sigma,
                )
                snapshot_id = _candidate_id(len(candidate_records))
                record, evaluation = _evaluate_and_log(
                    run_dir=run_dir,
                    history_path=history_path,
                    snapshot_id=snapshot_id,
                    label=f"refine_{idx}",
                    params=refined,
                    evaluator=evaluator,
                    source="screen_refine",
                    wall_start=wall_start,
                    process_start=process_start,
                )
                summary = _validate_candidate(
                    refined,
                    label=record.label,
                    pair_seeds=screen_seeds,
                    turn_cutoff=screen_turn_cutoff,
                    seed=seed + 20_000 + idx,
                    workers=workers,
                )
                _append_jsonl(
                    history_path,
                    {
                        "event": "refine_screen_validation",
                        "snapshot_id": record.snapshot_id,
                        **asdict(summary),
                    },
                )
                _print_validation("refine-screen-validation", summary)
                candidate_records.append((record, evaluation, refined))
                if (
                    best_screen_validation is None
                    or _validation_sort_key(summary)
                    > _validation_sort_key(best_screen_validation)
                ):
                    best_screen_validation = summary
                screened_results.append((summary, record, evaluation, refined))

        shortlisted = [
            (record, evaluation, params)
            for summary, record, evaluation, params in sorted(
                screened_results,
                key=lambda item: _validation_sort_key(item[0]),
                reverse=True,
            )[:shortlist_size]
        ]

    train_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(mini_pairs))
    holdout_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(full_pairs))
    best_validation: ValidationSummary | None = None
    best_mean_validation: ValidationSummary | None = None
    best_validated_params = DEFAULT_MINIMAL_HYBRID_PARAMS
    improvement_milestone: dict[str, object] | None = None

    for idx, (record, _, params) in enumerate(shortlisted, start=1):
        print(
            f"mini-validation-start {idx}/{len(shortlisted)} label={record.label}",
            flush=True,
        )
        summary = _validate_candidate(
            params,
            label=record.label,
            pair_seeds=train_seeds,
            turn_cutoff=mini_turn_cutoff,
            seed=seed + idx,
            workers=workers,
        )
        _append_jsonl(history_path, {"event": "mini_validation", **asdict(summary)})
        _print_validation("mini-validation", summary)
        if best_mean_validation is None or summary.mean_score > best_mean_validation.mean_score:
            best_mean_validation = summary
        if (
            best_validation is None
            or _validation_sort_key(summary) > _validation_sort_key(best_validation)
        ):
            best_validation = summary
            best_validated_params = params
            if summary.significant_positive and improvement_milestone is None:
                improvement_milestone = {
                    "label": summary.label,
                    "wall_s": time.perf_counter() - wall_start,
                    "process_s": time.process_time() - process_start,
                    "stage": "mini_validation",
                }

    full_summary = _validate_candidate(
        best_validated_params,
        label="best_validated_candidate",
        pair_seeds=holdout_seeds,
        turn_cutoff=full_turn_cutoff,
        seed=seed + 999,
        workers=workers,
    )
    _append_jsonl(history_path, {"event": "full_validation", **asdict(full_summary)})
    _print_validation("full-validation", full_summary)
    if full_summary.significant_positive and improvement_milestone is None:
        improvement_milestone = {
            "label": full_summary.label,
            "wall_s": time.perf_counter() - wall_start,
            "process_s": time.process_time() - process_start,
            "stage": "full_validation",
        }

    summary_payload = {
        "run_stamp": run_stamp,
        "baseline_snapshot": baseline_record.snapshot_id,
        "best_proxy_snapshot": best_record.snapshot_id,
        "best_proxy_label": best_record.label,
        "best_proxy_objective": best_eval.objective,
        "best_proxy_score": best_eval.proxy_score,
        "screen_validation": (
            asdict(best_screen_validation) if best_screen_validation is not None else None
        ),
        "mini_validation": asdict(best_validation) if best_validation is not None else None,
        "best_mean_mini_validation": (
            asdict(best_mean_validation) if best_mean_validation is not None else None
        ),
        "full_validation": asdict(full_summary),
        "improvement_milestone": improvement_milestone,
        "wall_s_total": time.perf_counter() - wall_start,
        "process_s_total": time.process_time() - process_start,
        "best_proxy_params_delta": format_params_delta(best_params),
        "best_validated_params_delta": format_params_delta(best_validated_params),
    }
    _write_json(run_dir / "summary.json", summary_payload)
    _append_jsonl(_INDEX_FILE, summary_payload)
    return summary_payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proxy-candidates", type=int, default=24)
    parser.add_argument("--proxy-sigma", type=float, default=1.0)
    parser.add_argument("--proxy-steps", type=int, default=8)
    parser.add_argument("--screen-candidates", type=int, default=12)
    parser.add_argument("--screen-pairs", type=int, default=2)
    parser.add_argument(
        "--screen-turn-cutoff",
        type=int,
        default=4,
        help="Turn cutoff for cheap pre-screening; omit by passing 0 to disable cutoff",
    )
    parser.add_argument("--refine-candidates", type=int, default=0)
    parser.add_argument("--refine-sigma", type=float, default=0.35)
    parser.add_argument("--shortlist-size", type=int, default=4)
    parser.add_argument("--mini-pairs", type=int, default=8)
    parser.add_argument("--full-pairs", type=int, default=2)
    parser.add_argument("--mini-turn-cutoff", type=int, default=4)
    parser.add_argument(
        "--full-turn-cutoff",
        type=int,
        default=6,
        help="Late-turn holdout cutoff; omit by passing 0 to play full games",
    )
    parser.add_argument("--seed", type=int, default=20260327)
    parser.add_argument(
        "--workers",
        type=int,
        default=max(1, (os.cpu_count() or 1) // 2),
        help="Parallel worker processes for candidate and seed evaluation",
    )
    args = parser.parse_args()

    summary = run_campaign(
        proxy_candidates=args.proxy_candidates,
        proxy_sigma=args.proxy_sigma,
        proxy_steps=args.proxy_steps,
        screen_candidates=args.screen_candidates,
        screen_pairs=args.screen_pairs,
        screen_turn_cutoff=(None if args.screen_turn_cutoff == 0 else args.screen_turn_cutoff),
        refine_candidates=args.refine_candidates,
        refine_sigma=args.refine_sigma,
        shortlist_size=args.shortlist_size,
        mini_pairs=args.mini_pairs,
        full_pairs=args.full_pairs,
        mini_turn_cutoff=args.mini_turn_cutoff,
        full_turn_cutoff=(None if args.full_turn_cutoff == 0 else args.full_turn_cutoff),
        workers=args.workers,
        seed=args.seed,
    )
    print("")
    print("campaign-summary")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
