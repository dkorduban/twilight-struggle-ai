"""Standalone micro benchmark for minimal_hybrid versus random policy.

This benchmark measures policy-call latency on a fixed corpus of legal
action-round decision states. It does not run full games or compare strength;
it compares how quickly each policy can choose a legal action under the
current live-play policy contract.
"""
from __future__ import annotations

import argparse
import gc
import random
import time
from dataclasses import asdict, dataclass

from tsrl.engine.game_loop import make_random_policy
from tsrl.engine.legal_actions import enumerate_actions
from tsrl.etl.game_data import load_countries
from tsrl.policies.minimal_hybrid import choose_minimal_hybrid
from tsrl.schemas import PublicState, Side


@dataclass(frozen=True)
class BenchmarkCase:
    name: str
    pub: PublicState
    hand: frozenset[int]
    holds_china: bool


@dataclass(frozen=True)
class CaseSummary:
    name: str
    turn: int
    ar: int
    side: str
    hand: tuple[int, ...]
    holds_china: bool
    legal_actions: int


@dataclass(frozen=True)
class PolicyResult:
    name: str
    decisions: int
    total_ns: int
    ns_per_decision: float
    decisions_per_second: float


@dataclass(frozen=True)
class BenchmarkReport:
    iterations: int
    warmup: int
    seed: int
    cases: tuple[CaseSummary, ...]
    results: tuple[PolicyResult, ...]


def _country_id(name: str) -> int:
    for country_id, spec in load_countries().items():
        if spec.name == name:
            return country_id
    raise KeyError(f"Unknown country name: {name}")


def _make_pub(
    *,
    turn: int,
    ar: int,
    phasing: Side,
    defcon: int = 5,
    milops: tuple[int, int] = (0, 0),
    space: tuple[int, int] = (0, 0),
    china_held_by: Side = Side.USSR,
    china_playable: bool = True,
    influence: tuple[tuple[Side, str, int], ...] = (),
) -> PublicState:
    pub = PublicState()
    pub.turn = turn
    pub.ar = ar
    pub.phasing = phasing
    pub.defcon = defcon
    pub.milops = list(milops)
    pub.space = list(space)
    pub.china_held_by = china_held_by
    pub.china_playable = china_playable
    for side, country_name, amount in influence:
        pub.influence[(side, _country_id(country_name))] = amount
    return pub


def benchmark_cases() -> tuple[BenchmarkCase, ...]:
    return (
        BenchmarkCase(
            name="early_ussr_opening",
            pub=_make_pub(turn=1, ar=1, phasing=Side.USSR),
            hand=frozenset({7, 15}),
            holds_china=False,
        ),
        BenchmarkCase(
            name="early_ussr_thailand",
            pub=_make_pub(
                turn=1,
                ar=3,
                phasing=Side.USSR,
                influence=((Side.USSR, "Vietnam", 1),),
            ),
            hand=frozenset({15}),
            holds_china=False,
        ),
        BenchmarkCase(
            name="mid_us_pressure",
            pub=_make_pub(
                turn=5,
                ar=2,
                phasing=Side.US,
                defcon=3,
                space=(0, 2),
            ),
            hand=frozenset({4, 5}),
            holds_china=False,
        ),
        BenchmarkCase(
            name="mid_ussr_africa_entry",
            pub=_make_pub(
                turn=5,
                ar=4,
                phasing=Side.USSR,
                defcon=3,
                influence=((Side.USSR, "Angola", 1),),
            ),
            hand=frozenset({7, 15}),
            holds_china=False,
        ),
        BenchmarkCase(
            name="late_ussr_europe",
            pub=_make_pub(
                turn=8,
                ar=5,
                phasing=Side.USSR,
                defcon=4,
                milops=(0, 2),
                influence=(
                    (Side.USSR, "Poland", 1),
                    (Side.USSR, "East Germany", 1),
                ),
            ),
            hand=frozenset({7, 15}),
            holds_china=False,
        ),
    )


def _case_summary(case: BenchmarkCase) -> CaseSummary:
    legal = enumerate_actions(
        case.hand,
        case.pub,
        case.pub.phasing,
        holds_china=case.holds_china,
    )
    if not legal:
        raise RuntimeError(f"Benchmark case {case.name} has no legal actions")
    return CaseSummary(
        name=case.name,
        turn=case.pub.turn,
        ar=case.pub.ar,
        side=case.pub.phasing.name,
        hand=tuple(sorted(case.hand)),
        holds_china=case.holds_china,
        legal_actions=len(legal),
    )


def _measure_policy(
    name: str,
    policy,
    cases: tuple[BenchmarkCase, ...],
    *,
    iterations: int,
    warmup: int,
) -> PolicyResult:
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
                    raise RuntimeError(f"{name} returned no action for {case.name}")
                decisions += 1
        total_ns = time.perf_counter_ns() - start_ns
    finally:
        if gc_was_enabled:
            gc.enable()

    return PolicyResult(
        name=name,
        decisions=decisions,
        total_ns=total_ns,
        ns_per_decision=total_ns / decisions,
        decisions_per_second=decisions / (total_ns / 1_000_000_000),
    )


def run_benchmark(
    *,
    iterations: int = 2_000,
    warmup: int = 200,
    seed: int = 20260327,
) -> BenchmarkReport:
    cases = benchmark_cases()
    case_summaries = tuple(_case_summary(case) for case in cases)

    hybrid = _measure_policy(
        "minimal_hybrid",
        choose_minimal_hybrid,
        cases,
        iterations=iterations,
        warmup=warmup,
    )
    random_policy = make_random_policy(random.Random(seed))
    random_result = _measure_policy(
        "random_policy",
        random_policy,
        cases,
        iterations=iterations,
        warmup=warmup,
    )

    return BenchmarkReport(
        iterations=iterations,
        warmup=warmup,
        seed=seed,
        cases=case_summaries,
        results=(hybrid, random_result),
    )


def format_report(report: BenchmarkReport) -> str:
    name_width = max(len(case.name) for case in report.cases)
    lines = [
        "Hybrid vs random policy micro benchmark",
        f"Iterations per case: {report.iterations}",
        f"Warmup per case: {report.warmup}",
        f"Random seed: {report.seed}",
        "",
        "Cases:",
    ]
    for case in report.cases:
        lines.append(
            f"  {case.name:<{name_width}}  "
            f"turn={case.turn} ar={case.ar} side={case.side:<4} "
            f"hand={list(case.hand)} legal={case.legal_actions}"
        )

    lines.extend(("", "Results:"))
    header = (
        f"  {'policy':<16} {'decisions':>10} {'total_ms':>12} "
        f"{'us/decision':>14} {'decisions/s':>14}"
    )
    lines.append(header)
    for result in report.results:
        lines.append(
            f"  {result.name:<16} "
            f"{result.decisions:>10} "
            f"{result.total_ns / 1_000_000:>12.3f} "
            f"{result.ns_per_decision / 1_000:>14.3f} "
            f"{result.decisions_per_second:>14.1f}"
        )

    hybrid, random_result = report.results
    slowdown = hybrid.ns_per_decision / random_result.ns_per_decision
    lines.extend(
        (
            "",
            f"Relative slowdown (hybrid/random): {slowdown:.2f}x",
        )
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--iterations",
        type=int,
        default=2_000,
        help="Timed iterations per benchmark case",
    )
    parser.add_argument(
        "--warmup",
        type=int,
        default=200,
        help="Warmup iterations per benchmark case",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=20260327,
        help="Seed used by the random policy",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of the formatted text report",
    )
    args = parser.parse_args()

    report = run_benchmark(
        iterations=args.iterations,
        warmup=args.warmup,
        seed=args.seed,
    )
    if args.json:
        import json

        print(json.dumps(asdict(report), indent=2, sort_keys=True))
        return

    print(format_report(report))


if __name__ == "__main__":
    main()
