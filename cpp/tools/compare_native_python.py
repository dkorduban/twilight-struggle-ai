#!/usr/bin/env python3
"""Compare native C++ and Python game-loop outcomes on fixed seeds/policies.

This is a parity triage tool rather than a formal proof harness. It answers the
practical question "how far does the native trace stay aligned before drifting?"
and writes the first mismatch in a compact machine-readable form so the next C++
fix can be driven by a concrete seed and action prefix.

Two execution modes matter:

- normal mode exercises the default native reset/play path
- ``--exact-setup`` forces native traced play to start from NumPy-compatible
  seed words so setup and opening headline drift can be separated from later
  runtime RNG or event-semantics drift
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

import tscore
from numpy.random import SeedSequence
from tsrl.engine.game_loop import _run_game_gen
from tsrl.engine.game_state import reset
from tsrl.engine.rng import make_rng
from tsrl.policies.minimal_hybrid import choose_minimal_hybrid


PythonPolicy = Callable[[object, frozenset[int], bool], object | None]


def make_python_policy(name: str, seed: int) -> PythonPolicy:
    if name in {"minimal", "minimal_hybrid"}:
        return choose_minimal_hybrid
    if name == "random":
        from tsrl.engine.game_loop import make_random_policy

        return make_random_policy(make_rng(seed))
    raise ValueError(f"unsupported python policy: {name}")


def native_policy_kind(name: str) -> tscore.PolicyKind:
    if name in {"minimal", "minimal_hybrid"}:
        return tscore.PolicyKind.MinimalHybrid
    if name == "random":
        return tscore.PolicyKind.Random
    raise ValueError(f"unsupported native policy: {name}")


@dataclass
class TraceStep:
    turn: int
    ar: int
    side: int
    card_id: int
    mode: int
    targets: tuple[int, ...]


@dataclass
class TraceResult:
    winner: int | None
    final_vp: int
    end_turn: int
    end_reason: str
    steps: list[TraceStep]


def collect_python_trace(ussr_policy_name: str, us_policy_name: str, seed: int) -> TraceResult:
    rng = make_rng(seed)
    gs = reset(seed=seed)
    gen = _run_game_gen(gs, rng, 10)
    ussr_policy = make_python_policy(ussr_policy_name, seed)
    us_policy = make_python_policy(us_policy_name, seed + 1)
    steps: list[TraceStep] = []

    try:
        req = next(gen)
        while True:
            policy = ussr_policy if int(req.side) == 0 else us_policy
            action = policy(req.pub, req.hand, req.holds_china)
            if action is not None:
                steps.append(
                    TraceStep(
                        turn=req.pub.turn,
                        ar=req.pub.ar,
                        side=int(req.side),
                        card_id=int(action.card_id),
                        mode=int(action.mode),
                        targets=tuple(int(t) for t in action.targets),
                    )
                )
            req = gen.send(action)
    except StopIteration as stop:
        result = stop.value

    return TraceResult(
        winner=None if result.winner is None else int(result.winner),
        final_vp=int(result.final_vp),
        end_turn=int(result.end_turn),
        end_reason=str(result.end_reason),
        steps=steps,
    )


def collect_native_trace(ussr_policy_name: str, us_policy_name: str, seed: int, *, exact_setup: bool) -> TraceResult:
    if exact_setup:
        words = [int(v) for v in SeedSequence(seed).generate_state(4, dtype="uint64").tolist()]
        traced = tscore.play_traced_game_from_seed_words(
            native_policy_kind(ussr_policy_name),
            native_policy_kind(us_policy_name),
            words,
            seed,
        )
    else:
        traced = tscore.play_traced_game(
            native_policy_kind(ussr_policy_name),
            native_policy_kind(us_policy_name),
            seed,
        )
    return TraceResult(
        winner=None if traced.result.winner is None else int(traced.result.winner),
        final_vp=int(traced.result.final_vp),
        end_turn=int(traced.result.end_turn),
        end_reason=str(traced.result.end_reason),
        steps=[
            TraceStep(
                turn=int(step.turn),
                ar=int(step.ar),
                side=int(step.side),
                card_id=int(step.action.card_id),
                mode=int(step.action.mode),
                targets=tuple(int(t) for t in step.action.targets),
            )
            for step in traced.steps
        ],
    )


def prefix_match_length(lhs: list[TraceStep], rhs: list[TraceStep]) -> int:
    matched = 0
    for left, right in zip(lhs, rhs):
        if left != right:
            break
        matched += 1
    return matched


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=5)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--ussr-policy", default="minimal_hybrid")
    parser.add_argument("--us-policy", default="random")
    parser.add_argument("--exact-setup", action="store_true")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    report: dict[str, object] = {
        "games": args.games,
        "base_seed": args.seed,
        "ussr_policy": args.ussr_policy,
        "us_policy": args.us_policy,
        "exact_setup": args.exact_setup,
        "result_matches": 0,
        "exact_trace_matches": 0,
        "comparisons": [],
    }

    for offset in range(args.games):
        seed = args.seed + offset
        native = collect_native_trace(args.ussr_policy, args.us_policy, seed, exact_setup=args.exact_setup)
        python = collect_python_trace(args.ussr_policy, args.us_policy, seed)
        prefix = prefix_match_length(native.steps, python.steps)

        result_match = (
            native.winner == python.winner
            and native.final_vp == python.final_vp
            and native.end_turn == python.end_turn
            and native.end_reason == python.end_reason
        )
        exact_trace_match = (
            len(native.steps) == len(python.steps)
            and prefix == len(native.steps) == len(python.steps)
            and result_match
        )
        report["result_matches"] += int(result_match)
        report["exact_trace_matches"] += int(exact_trace_match)
        report["comparisons"].append(
            {
                "seed": seed,
                "result_match": result_match,
                "exact_trace_match": exact_trace_match,
                "native_result": {
                    "winner": native.winner,
                    "final_vp": native.final_vp,
                    "end_turn": native.end_turn,
                    "end_reason": native.end_reason,
                    "steps": len(native.steps),
                },
                "python_result": {
                    "winner": python.winner,
                    "final_vp": python.final_vp,
                    "end_turn": python.end_turn,
                    "end_reason": python.end_reason,
                    "steps": len(python.steps),
                },
                "trace_prefix_match": prefix,
                "first_native_only": None if prefix >= len(native.steps) else asdict(native.steps[prefix]),
                "first_python_only": None if prefix >= len(python.steps) else asdict(python.steps[prefix]),
            }
        )

    if args.out is not None:
        args.out.write_text(json.dumps(report, indent=2) + "\n")

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
