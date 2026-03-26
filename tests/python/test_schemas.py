"""Sanity tests for core schema definitions."""
import pytest
from tsrl.schemas import (
    EventKind,
    HandKnowledge,
    LabelQuality,
    OfflineLabels,
    PublicState,
    ReplayEvent,
    Side,
)


def test_side_values():
    assert Side.USSR == 0
    assert Side.US == 1
    assert Side.NEUTRAL == 2


def test_replay_event_immutable():
    ev = ReplayEvent(kind=EventKind.PLAY, turn=1, ar=1, phasing=Side.USSR, card_id=42)
    with pytest.raises(Exception):
        ev.turn = 2  # type: ignore[misc]


def test_replay_event_defaults():
    ev = ReplayEvent(kind=EventKind.TURN_START, turn=1, ar=0, phasing=Side.USSR)
    assert ev.card_id is None
    assert ev.aux_card_ids == ()
    assert ev.raw_line == ""


def test_public_state_defaults():
    ps = PublicState()
    assert ps.defcon == 5
    assert ps.vp == 0
    assert ps.turn == 0
    assert ps.china_held_by == Side.USSR
    assert len(ps.discard) == 0
    assert len(ps.removed) == 0


def test_hand_knowledge_invariant():
    """known_in_hand and known_not_in_hand must be disjoint."""
    hk = HandKnowledge(
        observer=Side.USSR,
        known_in_hand=frozenset({1, 2, 3}),
        known_not_in_hand=frozenset({4, 5}),
    )
    assert hk.known_in_hand.isdisjoint(hk.known_not_in_hand)


def test_hand_knowledge_invariant_violation_detected():
    """Overlapping sets should be flagged by application logic (not schema itself)."""
    # The schema is a plain dataclass; invariant checking is the reducer's job.
    # This test documents that the schema does NOT auto-enforce the invariant,
    # so the reducer MUST validate it.
    hk = HandKnowledge(
        observer=Side.US,
        known_in_hand=frozenset({10}),
        known_not_in_hand=frozenset({10}),  # violation
    )
    # Intersection is non-empty – must be caught by reducer
    assert not hk.known_in_hand.isdisjoint(hk.known_not_in_hand)


def test_offline_labels_not_imported_from_public_state():
    """OfflineLabels must not appear in PublicState or HandKnowledge."""
    import inspect
    import tsrl.schemas as m

    ps_src = inspect.getsource(PublicState)
    hk_src = inspect.getsource(HandKnowledge)
    assert "OfflineLabels" not in ps_src
    assert "OfflineLabels" not in hk_src


def test_label_quality_ordering():
    assert LabelQuality.EXACT < LabelQuality.INFERRED < LabelQuality.AMBIGUOUS < LabelQuality.UNKNOWN
