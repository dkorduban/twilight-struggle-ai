"""Local tuner for the first-pass minimal_hybrid parameter block.

This intentionally tunes a smaller 26-parameter surface first:
  - 21 region weights
  - 4 action-mode priors
  - 1 per-ops card-use penalty

Evaluation modes:
  - proxy: cheap fixed-state action-agreement proxy plus speed penalty
  - selfplay: paired self-play score plus speed penalty
  - combined: weighted proxy + self-play + speed penalty

This is a policy-local tuning harness. It does not change engine contracts,
game loop semantics, or action interfaces.
"""
from __future__ import annotations

import argparse
import gc
import random
import time
from dataclasses import dataclass

from tsrl.engine.game_loop import GameResult, play_game
from tsrl.policies.benchmark_hybrid_vs_random import BenchmarkCase, benchmark_cases
from tsrl.policies.minimal_hybrid import (
    DEFAULT_MINIMAL_HYBRID_PARAMS,
    MinimalHybridParams,
    make_minimal_hybrid_policy,
)
from tsrl.policies.proxy_corpus import build_proxy_corpus, score_proxy_action
from tsrl.schemas import Side

_REGION_LABELS = (
    "europe",
    "asia",
    "middle_east",
    "central_america",
    "south_america",
    "africa",
    "southeast_asia",
)

_EVAL_MODES = ("proxy", "selfplay", "combined")

_PARAMETER_NAMES = tuple(
    [f"early_{label}" for label in _REGION_LABELS]
    + [f"mid_{label}" for label in _REGION_LABELS]
    + [f"late_{label}" for label in _REGION_LABELS]
    + [
        "influence_mode_bonus",
        "coup_mode_bonus",
        "realign_mode_bonus",
        "space_mode_bonus",
        "ops_card_penalty",
        "control_break_bonus",
        "access_bonus",
        "coup_battleground_bonus",
        "coup_defcon2_penalty",
        "coup_defcon3_penalty",
        "realign_base_penalty",
        "realign_country_scale",
        "realign_defcon2_bonus",
        "space_when_behind_bonus",
        "space_early_bonus",
        "space_offside_bonus",
        "headline_ops_scale",
        "headline_friendly_bonus",
        "china_early_penalty",
        "china_asia_target_bonus",
        "country_region_scale",
        "country_battleground_bonus",
        "country_non_battleground_bonus",
        "country_stability_scale",
        "country_thailand_early_bonus",
        "country_europe_core_bonus",
        "country_mid_war_entry_bonus",
    ]
)

_LOWER_BOUNDS = (
    (0.25,) * 21
    + (
        0.0,
        0.0,
        -4.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        -16.0,
        -8.0,
        -8.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        -8.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    )
)
_UPPER_BOUNDS = (
    (2.0,) * 21
    + (
        10.0,
        8.0,
        2.0,
        4.0,
        0.75,
        12.0,
        4.0,
        8.0,
        0.0,
        0.0,
        0.0,
        2.0,
        6.0,
        6.0,
        4.0,
        6.0,
        2.0,
        6.0,
        0.0,
        6.0,
        12.0,
        12.0,
        4.0,
        2.0,
        10.0,
        6.0,
        6.0,
    )
)
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
class CandidateEvaluation:
    objective: float
    proxy_score: float
    paired_score: float
    speed_penalty: float
    candidate_us_per_decision: float
    baseline_us_per_decision: float
    paired_games: int


@dataclass(frozen=True)
class TuningResult:
    best_params: MinimalHybridParams
    best_eval: CandidateEvaluation
    best_step: int
    start_eval: CandidateEvaluation


@dataclass(frozen=True)
class EvaluationConfig:
    mode: str
    pair_seeds: tuple[int, ...]
    speed_iterations: int
    speed_warmup: int
    time_weight: float
    proxy_weight: float
    selfplay_weight: float


class Evaluator:
    """Cached evaluator for repeated candidate scoring."""

    def __init__(self, config: EvaluationConfig) -> None:
        self.config = config
        self.proxy_cases = build_proxy_corpus()
        self.latency_cases: tuple[BenchmarkCase, ...] = benchmark_cases()
        self.baseline_us = _policy_latency_us(
            DEFAULT_MINIMAL_HYBRID_PARAMS,
            cases=self.latency_cases,
            iterations=config.speed_iterations,
            warmup=config.speed_warmup,
        )

    def evaluate(self, params: MinimalHybridParams) -> CandidateEvaluation:
        proxy_score = 0.0
        paired_score = 0.0
        paired_games = 0

        if self.config.mode in ("proxy", "combined"):
            proxy_score = self._proxy_score(params)

        if self.config.mode in ("selfplay", "combined"):
            paired_score = paired_selfplay_score(params, pair_seeds=self.config.pair_seeds)
            paired_games = 2 * len(self.config.pair_seeds)

        candidate_us = _policy_latency_us(
            params,
            cases=self.latency_cases,
            iterations=self.config.speed_iterations,
            warmup=self.config.speed_warmup,
        )
        speed_penalty = max(0.0, (candidate_us / self.baseline_us) - 1.0)

        if self.config.mode == "proxy":
            objective = proxy_score - self.config.time_weight * speed_penalty
        elif self.config.mode == "selfplay":
            objective = paired_score - self.config.time_weight * speed_penalty
        else:
            objective = (
                self.config.proxy_weight * proxy_score
                + self.config.selfplay_weight * paired_score
                - self.config.time_weight * speed_penalty
            )

        return CandidateEvaluation(
            objective=objective,
            proxy_score=proxy_score,
            paired_score=paired_score,
            speed_penalty=speed_penalty,
            candidate_us_per_decision=candidate_us,
            baseline_us_per_decision=self.baseline_us,
            paired_games=paired_games,
        )

    def _proxy_score(self, params: MinimalHybridParams) -> float:
        policy = make_minimal_hybrid_policy(params)
        total_weight = 0.0
        total_score = 0.0
        for case in self.proxy_cases:
            action = policy(case.pub, case.hand, case.holds_china)
            total_score += case.weight * score_proxy_action(case, action)
            total_weight += case.weight
        return total_score / total_weight


def flatten_params(params: MinimalHybridParams) -> tuple[float, ...]:
    return (
        *params.early_region_weights,
        *params.mid_region_weights,
        *params.late_region_weights,
        params.influence_mode_bonus,
        params.coup_mode_bonus,
        params.realign_mode_bonus,
        params.space_mode_bonus,
        params.ops_card_penalty,
        params.control_break_bonus,
        params.access_bonus,
        params.coup_battleground_bonus,
        params.coup_defcon2_penalty,
        params.coup_defcon3_penalty,
        params.realign_base_penalty,
        params.realign_country_scale,
        params.realign_defcon2_bonus,
        params.space_when_behind_bonus,
        params.space_early_bonus,
        params.space_offside_bonus,
        params.headline_ops_scale,
        params.headline_friendly_bonus,
        params.china_early_penalty,
        params.china_asia_target_bonus,
        params.country_region_scale,
        params.country_battleground_bonus,
        params.country_non_battleground_bonus,
        params.country_stability_scale,
        params.country_thailand_early_bonus,
        params.country_europe_core_bonus,
        params.country_mid_war_entry_bonus,
    )


def unflatten_params(values: tuple[float, ...]) -> MinimalHybridParams:
    if len(values) != len(_PARAMETER_NAMES):
        raise ValueError(f"Expected {len(_PARAMETER_NAMES)} values, got {len(values)}")
    return MinimalHybridParams(
        early_region_weights=tuple(values[0:7]),
        mid_region_weights=tuple(values[7:14]),
        late_region_weights=tuple(values[14:21]),
        influence_mode_bonus=values[21],
        coup_mode_bonus=values[22],
        realign_mode_bonus=values[23],
        space_mode_bonus=values[24],
        ops_card_penalty=values[25],
        control_break_bonus=values[26],
        access_bonus=values[27],
        coup_battleground_bonus=values[28],
        coup_defcon2_penalty=values[29],
        coup_defcon3_penalty=values[30],
        realign_base_penalty=values[31],
        realign_country_scale=values[32],
        realign_defcon2_bonus=values[33],
        space_when_behind_bonus=values[34],
        space_early_bonus=values[35],
        space_offside_bonus=values[36],
        headline_ops_scale=values[37],
        headline_friendly_bonus=values[38],
        china_early_penalty=values[39],
        china_asia_target_bonus=values[40],
        country_region_scale=values[41],
        country_battleground_bonus=values[42],
        country_non_battleground_bonus=values[43],
        country_stability_scale=values[44],
        country_thailand_early_bonus=values[45],
        country_europe_core_bonus=values[46],
        country_mid_war_entry_bonus=values[47],
    )


def clip_vector(values: tuple[float, ...]) -> tuple[float, ...]:
    clipped = []
    for value, lower, upper in zip(values, _LOWER_BOUNDS, _UPPER_BOUNDS, strict=True):
        clipped.append(min(max(value, lower), upper))
    return tuple(clipped)


def _policy_latency_us(
    params: MinimalHybridParams,
    *,
    cases: tuple[BenchmarkCase, ...],
    iterations: int,
    warmup: int,
) -> float:
    policy = make_minimal_hybrid_policy(params)

    for _ in range(warmup):
        for case in cases:
            policy(case.pub, case.hand, case.holds_china)

    gc_was_enabled = gc.isenabled()
    if gc_was_enabled:
        gc.disable()

    try:
        start_ns = time.perf_counter_ns()
        decisions = 0
        for _ in range(iterations):
            for case in cases:
                action = policy(case.pub, case.hand, case.holds_china)
                if action is None:
                    raise RuntimeError(f"Policy returned None for benchmark case {case.name}")
                decisions += 1
        total_ns = time.perf_counter_ns() - start_ns
    finally:
        if gc_was_enabled:
            gc.enable()

    return (total_ns / decisions) / 1_000


def _game_score(result: GameResult, candidate_side: Side) -> float:
    winner_score = 0.0
    if result.winner == candidate_side:
        winner_score = 1.0
    elif result.winner is not None:
        winner_score = -1.0

    vp_score = max(-1.0, min(1.0, result.final_vp / 20.0))
    if candidate_side == Side.US:
        vp_score = -vp_score

    return 0.75 * winner_score + 0.25 * vp_score


def paired_selfplay_score(
    params: MinimalHybridParams,
    *,
    pair_seeds: tuple[int, ...],
) -> float:
    candidate_policy = make_minimal_hybrid_policy(params)
    baseline_policy = make_minimal_hybrid_policy()
    pair_scores: list[float] = []

    for seed in pair_seeds:
        result_a = play_game(candidate_policy, baseline_policy, seed=seed)
        result_b = play_game(baseline_policy, candidate_policy, seed=seed)
        pair_score = 0.5 * (
            _game_score(result_a, Side.USSR) + _game_score(result_b, Side.US)
        )
        pair_scores.append(pair_score)

    return sum(pair_scores) / len(pair_scores)


def evaluate_params(
    params: MinimalHybridParams,
    *,
    mode: str,
    pair_seeds: tuple[int, ...],
    speed_iterations: int,
    speed_warmup: int,
    time_weight: float,
    proxy_weight: float = 0.25,
    selfplay_weight: float = 0.75,
) -> CandidateEvaluation:
    evaluator = Evaluator(
        EvaluationConfig(
            mode=mode,
            pair_seeds=pair_seeds,
            speed_iterations=speed_iterations,
            speed_warmup=speed_warmup,
            time_weight=time_weight,
            proxy_weight=proxy_weight,
            selfplay_weight=selfplay_weight,
        )
    )
    return evaluator.evaluate(params)


def tune_with_spsa(
    *,
    evaluator: Evaluator,
    steps: int,
    seed: int,
    evaluate_updated_theta: bool,
    a: float = 0.15,
    c: float = 0.30,
    A: float = 5.0,
    alpha: float = 0.602,
    gamma: float = 0.101,
) -> TuningResult:
    rng = random.Random(seed)
    theta = flatten_params(DEFAULT_MINIMAL_HYBRID_PARAMS)
    start_eval = evaluator.evaluate(DEFAULT_MINIMAL_HYBRID_PARAMS)
    best_theta = theta
    best_eval = start_eval
    best_step = 0

    for step in range(1, steps + 1):
        ak = a / ((step + A) ** alpha)
        ck = c / (step ** gamma)
        delta = tuple(rng.choice((-1.0, 1.0)) for _ in theta)

        theta_plus = clip_vector(
            tuple(
                value + ck * scale * sign
                for value, scale, sign in zip(theta, _PERTURBATION_SCALE, delta, strict=True)
            )
        )
        theta_minus = clip_vector(
            tuple(
                value - ck * scale * sign
                for value, scale, sign in zip(theta, _PERTURBATION_SCALE, delta, strict=True)
            )
        )

        eval_plus = evaluator.evaluate(unflatten_params(theta_plus))
        eval_minus = evaluator.evaluate(unflatten_params(theta_minus))

        gradient = tuple(
            (eval_plus.objective - eval_minus.objective) / (2.0 * ck * scale * sign)
            for scale, sign in zip(_PERTURBATION_SCALE, delta, strict=True)
        )
        theta = clip_vector(
            tuple(
                value + ak * grad
                for value, grad in zip(theta, gradient, strict=True)
            )
        )

        current_eval: CandidateEvaluation | None = None
        if evaluate_updated_theta:
            current_eval = evaluator.evaluate(unflatten_params(theta))

        candidates = [
            (theta_plus, eval_plus),
            (theta_minus, eval_minus),
        ]
        if current_eval is not None:
            candidates.append((theta, current_eval))

        for candidate_theta, candidate_eval in candidates:
            if candidate_eval.objective > best_eval.objective:
                best_theta = candidate_theta
                best_eval = candidate_eval
                best_step = step

        displayed_eval = current_eval or max(candidates, key=lambda item: item[1].objective)[1]
        print(
            f"step={step} objective={displayed_eval.objective:.4f} "
            f"proxy={displayed_eval.proxy_score:.4f} "
            f"paired={displayed_eval.paired_score:.4f} "
            f"time_pen={displayed_eval.speed_penalty:.4f}"
        )

    return TuningResult(
        best_params=unflatten_params(best_theta),
        best_eval=best_eval,
        best_step=best_step,
        start_eval=start_eval,
    )


def format_params_delta(params: MinimalHybridParams) -> str:
    default = flatten_params(DEFAULT_MINIMAL_HYBRID_PARAMS)
    tuned = flatten_params(params)
    changed = []
    for name, before, after in zip(_PARAMETER_NAMES, default, tuned, strict=True):
        if abs(after - before) >= 1e-9:
            changed.append(f"  {name}: {before:.4f} -> {after:.4f}")
    if not changed:
        return "  no changes"
    return "\n".join(changed)


def _build_config(
    args: argparse.Namespace,
    pair_seeds: tuple[int, ...],
) -> tuple[EvaluationConfig, bool]:
    evaluate_updated_theta = not args.skip_current_eval
    if args.smoke:
        return (
            EvaluationConfig(
                mode="proxy",
                pair_seeds=(),
                speed_iterations=1,
                speed_warmup=0,
                time_weight=args.time_weight,
                proxy_weight=1.0,
                selfplay_weight=0.0,
            ),
            False,
        )

    return (
        EvaluationConfig(
            mode=args.eval_mode,
            pair_seeds=pair_seeds,
            speed_iterations=args.speed_iterations,
            speed_warmup=args.speed_warmup,
            time_weight=args.time_weight,
            proxy_weight=args.proxy_weight,
            selfplay_weight=args.selfplay_weight,
        ),
        evaluate_updated_theta,
    )


def _validate_args(args: argparse.Namespace) -> None:
    if args.eval_mode not in _EVAL_MODES:
        raise ValueError(f"Unknown eval mode: {args.eval_mode}")
    if args.eval_mode in ("selfplay", "combined") and args.pairs <= 0 and not args.smoke:
        raise ValueError("--pairs must be positive for selfplay or combined mode")
    if args.speed_iterations <= 0 and not args.smoke:
        raise ValueError("--speed-iterations must be positive")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=4, help="SPSA steps to run")
    parser.add_argument(
        "--pairs",
        type=int,
        default=4,
        help="Number of fixed paired self-play seeds per evaluation",
    )
    parser.add_argument(
        "--eval-mode",
        choices=_EVAL_MODES,
        default="combined",
        help="Evaluation mode: proxy, selfplay, or combined",
    )
    parser.add_argument(
        "--speed-iterations",
        type=int,
        default=20,
        help="Latency benchmark iterations per case",
    )
    parser.add_argument(
        "--speed-warmup",
        type=int,
        default=5,
        help="Latency benchmark warmup iterations per case",
    )
    parser.add_argument(
        "--time-weight",
        type=float,
        default=0.10,
        help="Penalty weight for relative latency regression",
    )
    parser.add_argument(
        "--proxy-weight",
        type=float,
        default=0.25,
        help="Proxy weight in combined mode",
    )
    parser.add_argument(
        "--selfplay-weight",
        type=float,
        default=0.75,
        help="Self-play weight in combined mode",
    )
    parser.add_argument(
        "--skip-current-eval",
        action="store_true",
        help="Skip evaluating the updated theta each SPSA step",
    )
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Run the fast proxy-only smoke path",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=20260327,
        help="Seed for SPSA perturbations and paired self-play seed generation",
    )
    args = parser.parse_args()
    _validate_args(args)

    rng = random.Random(args.seed)
    pair_seeds = tuple(rng.randint(0, 2**31 - 1) for _ in range(args.pairs))
    config, evaluate_updated_theta = _build_config(args, pair_seeds)
    evaluator = Evaluator(config)
    result = tune_with_spsa(
        evaluator=evaluator,
        steps=args.steps,
        seed=args.seed,
        evaluate_updated_theta=evaluate_updated_theta,
    )

    print("")
    print("Evaluation mode")
    print(f"  mode: {config.mode}")
    print(f"  proxy_weight: {config.proxy_weight:.2f}")
    print(f"  selfplay_weight: {config.selfplay_weight:.2f}")
    print(f"  evaluate_updated_theta: {evaluate_updated_theta}")
    print("")
    print("Initial evaluation")
    print(f"  objective: {result.start_eval.objective:.4f}")
    print(f"  proxy_score: {result.start_eval.proxy_score:.4f}")
    print(f"  paired_score: {result.start_eval.paired_score:.4f}")
    print(f"  speed_penalty: {result.start_eval.speed_penalty:.4f}")
    print("")
    print("Best evaluation")
    print(f"  step: {result.best_step}")
    print(f"  objective: {result.best_eval.objective:.4f}")
    print(f"  proxy_score: {result.best_eval.proxy_score:.4f}")
    print(f"  paired_score: {result.best_eval.paired_score:.4f}")
    print(f"  speed_penalty: {result.best_eval.speed_penalty:.4f}")
    print(
        "  candidate_us_per_decision: "
        f"{result.best_eval.candidate_us_per_decision:.3f}"
    )
    print(
        "  baseline_us_per_decision: "
        f"{result.best_eval.baseline_us_per_decision:.3f}"
    )
    print(f"  paired_games: {result.best_eval.paired_games}")
    print("")
    print("Changed parameters")
    print(format_params_delta(result.best_params))


if __name__ == "__main__":
    main()
