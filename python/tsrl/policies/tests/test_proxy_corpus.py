"""Tests for the richer minimal_hybrid proxy corpus."""

from tsrl.policies.minimal_hybrid import DEFAULT_MINIMAL_HYBRID_PARAMS, make_minimal_hybrid_policy
from tsrl.policies.proxy_corpus import build_proxy_corpus, score_proxy_action


def test_proxy_corpus_has_multiple_cases():
    corpus = build_proxy_corpus()

    assert len(corpus) >= 12
    assert any(case.weight > 1.0 for case in corpus)


def test_default_policy_scores_strongly_but_not_perfectly_on_proxy_corpus():
    corpus = build_proxy_corpus()
    policy = make_minimal_hybrid_policy(DEFAULT_MINIMAL_HYBRID_PARAMS)

    total_weight = 0.0
    total_score = 0.0
    for case in corpus:
        total_score += case.weight * score_proxy_action(
            case,
            policy(case.pub, case.hand, case.holds_china),
        )
        total_weight += case.weight

    score = total_score / total_weight
    assert 0.80 < score < 1.0
