"""Parity checks for the Python-friendly native legality helper bindings."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from tsrl.engine.adjacency import load_adjacency as py_load_adjacency
from tsrl.engine.game_state import _ars_for_turn, _hand_size_for_turn
from tsrl.engine.legal_actions import (
    accessible_countries as py_accessible_countries,
    effective_ops as py_effective_ops,
)
from tsrl.engine.legal_actions import (
    enumerate_actions as py_enumerate_actions,
)
from tsrl.engine.legal_actions import (
    has_legal_action as py_has_legal_action,
)
from tsrl.engine.legal_actions import legal_cards as py_legal_cards
from tsrl.engine.legal_actions import legal_countries as py_legal_countries
from tsrl.engine.legal_actions import legal_modes as py_legal_modes
from tsrl.schemas import ActionMode, PublicState, Side

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _relative in ("build/bindings", "build-ninja/bindings"):
    _candidate = _REPO_ROOT / _relative
    if _candidate.exists():
        sys.path.insert(0, str(_candidate))

tscore = pytest.importorskip("tscore", reason="tscore bindings are not built")


def _normalize_actions(actions: object) -> list[tuple[int, int, tuple[int, ...]]]:
    return sorted(
        (int(action.card_id), int(action.mode), tuple(int(t) for t in action.targets))
        for action in actions
    )


def test_tscore_turn_helpers_match_python_engine() -> None:
    for turn in range(1, 11):
        assert tscore.ars_for_turn(turn) == _ars_for_turn(turn)
        assert tscore.hand_size_for_turn(turn) == _hand_size_for_turn(turn)


def test_tscore_adjacency_and_accessible_countries_match_python_engine() -> None:
    pub = PublicState()
    pub.influence[Side.USSR, 12] = 2

    assert tscore.load_adjacency()[18] == py_load_adjacency()[18]
    assert set(tscore.accessible_countries(Side.USSR, pub, ActionMode.INFLUENCE)) == set(
        py_accessible_countries(Side.USSR, pub, mode=ActionMode.INFLUENCE)
    )


def test_tscore_legal_helpers_match_python_engine() -> None:
    pub = PublicState()
    pub.defcon = 3
    pub.space[int(Side.USSR)] = 0
    pub.ops_modifier[int(Side.USSR)] = 1
    pub.influence[Side.USSR, 60] = 1
    hand = frozenset({7, 23})

    assert tscore.effective_ops(7, pub, Side.USSR) == py_effective_ops(7, pub, Side.USSR)
    assert set(tscore.legal_cards(hand, pub, Side.USSR, False)) == py_legal_cards(
        hand, pub, Side.USSR, holds_china=False
    )
    assert {int(mode) for mode in tscore.legal_modes(7, pub, Side.USSR)} == {
        int(mode) for mode in py_legal_modes(7, pub, Side.USSR)
    }
    assert set(tscore.legal_countries(7, ActionMode.COUP, pub, Side.USSR)) == set(
        py_legal_countries(7, ActionMode.COUP, pub, Side.USSR)
    )
    assert tscore.has_legal_action(hand, pub, Side.USSR, False) == py_has_legal_action(
        hand, pub, Side.USSR, holds_china=False
    )


def test_tscore_enumerate_actions_matches_python_engine() -> None:
    pub = PublicState()
    pub.defcon = 3
    pub.space[int(Side.USSR)] = 0
    pub.influence[Side.USSR, 60] = 1
    hand = frozenset({7})

    assert _normalize_actions(
        tscore.enumerate_actions(hand, pub, Side.USSR, False, 84)
    ) == _normalize_actions(
        py_enumerate_actions(hand, pub, Side.USSR, holds_china=False)
    )
