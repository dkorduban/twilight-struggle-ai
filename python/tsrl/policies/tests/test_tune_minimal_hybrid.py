"""Smoke tests for the minimal_hybrid tuning harness."""

from tsrl.policies.minimal_hybrid import DEFAULT_MINIMAL_HYBRID_PARAMS
from tsrl.policies.tune_minimal_hybrid import (
    EvaluationConfig,
    Evaluator,
    evaluate_params,
    flatten_params,
    unflatten_params,
)


def test_flatten_round_trip_preserves_default_params():
    assert (
        unflatten_params(flatten_params(DEFAULT_MINIMAL_HYBRID_PARAMS))
        == DEFAULT_MINIMAL_HYBRID_PARAMS
    )


def test_proxy_evaluator_returns_metrics():
    evaluator = Evaluator(
        EvaluationConfig(
            mode="proxy",
            pair_seeds=(),
            speed_iterations=1,
            speed_warmup=0,
            time_weight=0.10,
            proxy_weight=1.0,
            selfplay_weight=0.0,
        )
    )
    evaluation = evaluator.evaluate(DEFAULT_MINIMAL_HYBRID_PARAMS)

    assert 0.80 < evaluation.proxy_score < 1.0
    assert evaluation.paired_score == 0.0
    assert evaluation.paired_games == 0
    assert evaluation.baseline_us_per_decision > 0
    assert evaluation.candidate_us_per_decision > 0


def test_evaluate_params_proxy_mode_returns_metrics():
    evaluation = evaluate_params(
        DEFAULT_MINIMAL_HYBRID_PARAMS,
        mode="proxy",
        pair_seeds=(),
        speed_iterations=1,
        speed_warmup=0,
        time_weight=0.10,
    )

    assert 0.80 < evaluation.proxy_score < 1.0
    assert evaluation.paired_games == 0
    assert evaluation.baseline_us_per_decision > 0
    assert evaluation.candidate_us_per_decision > 0
