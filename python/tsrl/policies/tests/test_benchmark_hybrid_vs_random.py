"""Tests for the hybrid-vs-random policy micro benchmark."""

from tsrl.engine.game_loop import make_random_policy
from tsrl.engine.legal_actions import enumerate_actions
from tsrl.policies.benchmark_hybrid_vs_random import benchmark_cases, run_benchmark
from tsrl.policies.minimal_hybrid import choose_minimal_hybrid
from tsrl.schemas import ActionEncoding, ActionMode


def _canonicalize(action: ActionEncoding | None) -> ActionEncoding | None:
    if action is None:
        return None
    if action.mode in (ActionMode.INFLUENCE, ActionMode.REALIGN):
        return ActionEncoding(
            card_id=action.card_id,
            mode=action.mode,
            targets=tuple(sorted(action.targets)),
        )
    return action


def test_benchmark_cases_are_legal_for_both_policies():
    random_policy = make_random_policy()

    for case in benchmark_cases():
        legal = enumerate_actions(
            case.hand,
            case.pub,
            case.pub.phasing,
            holds_china=case.holds_china,
        )

        hybrid_action = choose_minimal_hybrid(case.pub, case.hand, case.holds_china)
        random_action = random_policy(case.pub, case.hand, case.holds_china)

        assert legal
        assert hybrid_action in legal
        assert _canonicalize(random_action) in legal


def test_run_benchmark_returns_structured_results():
    report = run_benchmark(iterations=2, warmup=1, seed=7)

    assert len(report.cases) == len(benchmark_cases())
    assert len(report.results) == 2
    assert [result.name for result in report.results] == [
        "minimal_hybrid",
        "random_policy",
    ]
    assert all(result.decisions == len(report.cases) * 2 for result in report.results)
    assert all(result.total_ns > 0 for result in report.results)
