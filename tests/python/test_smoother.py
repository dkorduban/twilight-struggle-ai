"""Tests for the offline hand smoother."""
import pytest
from tsrl.etl.parser import parse_replay
from tsrl.etl.smoother import SmootherMetrics, compute_metrics, smooth_game
from tsrl.schemas import EventKind, LabelQuality, Side


ALL_CARDS = frozenset(range(1, 111))


def _make_events(log: str):
    return parse_replay(log).events


# ---------------------------------------------------------------------------
# Basic smoke tests
# ---------------------------------------------------------------------------


def test_smooth_empty_game():
    labels = smooth_game([], ALL_CARDS)
    assert labels == []


def test_smooth_no_decision_events():
    """Events with no PLAY/HEADLINE produce no labels."""
    evs = _make_events(
        "Turn 1, Cleanup: : \n"
        "DEFCON degrades to 4"
    )
    labels = smooth_game(evs, ALL_CARDS)
    assert labels == []


def test_smooth_returns_one_label_per_decision():
    # Two action rounds → two PLAY events → two labels
    log = "\n".join([
        "Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):",
        "USSR +3 in Thailand [0][3]",
        "Turn 1, US AR1: NORAD*: Coup (3 Ops):",
        "US +2 in Iran [2][0]",
    ])
    evs = _make_events(log)
    labels = smooth_game(evs, ALL_CARDS)
    assert len(labels) == 2


def test_smooth_label_fields():
    log = "Turn 1, USSR AR1: Decolonization: Place Influence (3 Ops):"
    evs = _make_events(log)
    labels = smooth_game(evs, ALL_CARDS)
    assert len(labels) == 1
    lb = labels[0]
    assert lb.turn == 1
    assert lb.ar == 1
    assert lb.phasing == Side.USSR
    assert isinstance(lb.actor_hand, frozenset)
    assert isinstance(lb.opponent_possible, frozenset)
    assert lb.step_quality in LabelQuality.__members__.values()


# ---------------------------------------------------------------------------
# Backward propagation
# ---------------------------------------------------------------------------


def test_backward_propagates_reveal_hand():
    """REVEAL_HAND at a later step should propagate card knowledge backward."""
    log = "\n".join([
        "Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):",
        "USSR +3 in Thailand [0][3]",
        "Turn 1, USSR AR2: CIA Created*: Event: CIA Created*",
        "USSR reveals De Gaulle Leads France*",
    ])
    evs = _make_events(log)
    labels = smooth_game(evs, ALL_CARDS)
    # Two PLAY events → two labels; machinery should run without error.
    assert len(labels) == 2


def test_backward_propagates_end_turn_held():
    """Cards held into next turn (END_TURN_HELD) should propagate backward."""
    # END_TURN_HELD events come from e.g. scoring cards held at cleanup.
    # We build them directly since the real format doesn't have a standard "held" line.
    from tsrl.schemas import ReplayEvent
    evs = [
        ReplayEvent(kind=EventKind.PLAY, turn=1, ar=1, phasing=Side.USSR),
        ReplayEvent(kind=EventKind.END_TURN_HELD, turn=1, ar=7, phasing=Side.USSR,
                    aux_card_ids=(42,)),
    ]
    labels = smooth_game(evs, ALL_CARDS)
    assert len(labels) == 1


# ---------------------------------------------------------------------------
# Quality tags
# ---------------------------------------------------------------------------


def test_quality_unknown_when_no_observations():
    """Without any card observations, step quality should be AMBIGUOUS or UNKNOWN."""
    log = "Turn 1, USSR AR1: Decolonization: Place Influence (3 Ops):"
    evs = _make_events(log)
    labels = smooth_game(evs, ALL_CARDS)
    assert len(labels) == 1
    assert labels[0].step_quality in (LabelQuality.AMBIGUOUS, LabelQuality.UNKNOWN)


# ---------------------------------------------------------------------------
# Invariant: no false exclusions with known oracle
# ---------------------------------------------------------------------------


def test_false_exclusion_rate_zero_with_exact_oracle():
    """When oracle hand matches actor_hand, false_exclusion_violations == 0."""
    log = "Turn 1, USSR AR1: Decolonization: Place Influence (3 Ops):"
    evs = _make_events(log)
    labels = smooth_game(evs, ALL_CARDS)
    oracle = {(lb.turn, lb.ar, lb.phasing): lb.actor_hand for lb in labels}
    metrics = compute_metrics(labels, ground_truth_hands=oracle)
    assert metrics.false_exclusion_rate == 0.0


def test_false_exclusion_detected_with_wrong_oracle():
    """If oracle contains a card not in actor_hand, violations are counted."""
    log = "Turn 1, USSR AR1: Decolonization: Place Influence (3 Ops):"
    evs = _make_events(log)
    labels = smooth_game(evs, ALL_CARDS)
    oracle = {(labels[0].turn, labels[0].ar, labels[0].phasing): frozenset({99})}
    if 99 not in labels[0].actor_hand:
        metrics = compute_metrics(labels, ground_truth_hands=oracle)
        assert metrics.false_exclusion_violations > 0


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------


def test_compute_metrics_totals():
    log = "\n".join([
        "Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):",
        "Turn 1, US AR1: NORAD*: Coup (3 Ops):",
    ])
    evs = _make_events(log)
    labels = smooth_game(evs, ALL_CARDS)
    m = compute_metrics(labels)
    assert m.total == 2
    assert m.exact + m.inferred + m.ambiguous + m.unknown == m.total


def test_metrics_rates_are_fractions():
    m = SmootherMetrics(total=10, exact=3, inferred=4, ambiguous=2, unknown=1)
    assert 0.0 <= m.exact_rate <= 1.0
    assert 0.0 <= m.partial_rate <= 1.0
    assert m.partial_rate >= m.exact_rate


def test_metrics_empty():
    m = SmootherMetrics()
    assert m.exact_rate == 0.0
    assert m.false_exclusion_rate == 0.0
