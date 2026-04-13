"""Harness tests for C++ engine event-gap regressions.

This file is intentionally conservative about what it treats as runnable.
The current ``tscore`` Python binding exposes whole-game traced play and
callback policies, but it does not expose a traced "play from injected state"
entrypoint or a direct legal-action query over an injected C++ ``GameState``.

Tests that can be exercised through the existing binding surface run as normal
assertions. Tests that require mid-game state injection or hidden deck access
are kept as explicit gap-linked skips so the harness compiles cleanly today and
can be filled in as the binding surface grows.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest

from tsrl.engine.legal_actions import legal_cards
from tsrl.etl.game_data import load_cards
from tsrl.schemas import ActionMode, PublicState, Side

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _relative in ("build/bindings", "build-ninja/bindings"):
    _candidate = _REPO_ROOT / _relative
    if _candidate.exists():
        sys.path.insert(0, str(_candidate))

tscore = pytest.importorskip("tscore", reason="tscore bindings are not built")

_CARDS = load_cards()
_CHINA_CARD_ID = 6
_SPACE_SUPPRESSION_CARD_ID = 4  # Duck and Cover (US, 3 ops)
_PROMO_CARD_IDS = (109, 110, 111)

_INT_FIELDS = ("turn", "ar", "vp", "defcon")
_BOOL_FIELDS = (
    "china_playable",
    "warsaw_pact_played",
    "marshall_plan_played",
    "truman_doctrine_played",
    "john_paul_ii_played",
    "nato_active",
    "de_gaulle_active",
    "willy_brandt_active",
    "us_japan_pact_active",
    "nuclear_subs_active",
    "norad_active",
    "shuttle_diplomacy_active",
    "flower_power_active",
    "flower_power_cancelled",
    "salt_active",
    "opec_cancelled",
    "awacs_active",
    "north_sea_oil_extra_ar",
    "glasnost_extra_ar",
    "formosan_active",
    "cuban_missile_crisis_active",
    "vietnam_revolts_active",
    "bear_trap_active",
    "quagmire_active",
    "iran_hostage_crisis_active",
)


def _mode_value(mode: object) -> int:
    return int(mode)


def _build_public_state(state_dict: dict[str, Any]) -> PublicState:
    pub = PublicState()
    for field in _INT_FIELDS:
        if field in state_dict:
            setattr(pub, field, int(state_dict[field]))

    pub.phasing = Side(int(state_dict["phasing"]))
    pub.china_held_by = Side(int(state_dict["china_held_by"]))
    pub.china_playable = bool(state_dict.get("china_playable", False))
    pub.milops = [int(x) for x in state_dict.get("milops", [0, 0])]
    pub.space = [int(x) for x in state_dict.get("space", [0, 0])]
    pub.ops_modifier = [int(x) for x in state_dict.get("ops_modifier", [0, 0])]
    pub.discard = frozenset(int(x) for x in state_dict.get("discard", []))
    pub.removed = frozenset(int(x) for x in state_dict.get("removed", []))

    for field in _BOOL_FIELDS:
        if field in state_dict:
            setattr(pub, field, bool(state_dict[field]))

    for cid, amount in enumerate(state_dict.get("ussr_influence", [])):
        if amount:
            pub.influence[Side.USSR, cid] = int(amount)
    for cid, amount in enumerate(state_dict.get("us_influence", [])):
        if amount:
            pub.influence[Side.US, cid] = int(amount)
    return pub


def _action_dict(card_id: int, mode: ActionMode, targets: tuple[int, ...] = ()) -> dict[str, object]:
    return {"card_id": card_id, "mode": int(mode), "targets": list(targets)}


def _headline_pick(
    state_dict: dict[str, Any],
    hand_list: list[int],
    holds_china: bool,
    side: Side,
) -> dict[str, object] | None:
    pub = _build_public_state(state_dict)
    hand = frozenset(int(cid) for cid in hand_list)
    playable = sorted(legal_cards(hand, pub, side, holds_china=holds_china) - {_CHINA_CARD_ID})
    if not playable:
        return None
    return _action_dict(playable[0], ActionMode.EVENT)


class _SpaceOpponentCardPolicy:
    """Choose a specific opponent card as a space shot when the chance appears."""

    def __call__(
        self,
        state_dict: dict[str, Any],
        hand_list: list[int],
        holds_china: bool,
        side_int: int,
    ) -> dict[str, object] | None:
        side = Side(side_int)
        if int(state_dict["ar"]) == 0:
            return _headline_pick(state_dict, hand_list, holds_china, side)

        if side != Side.USSR:
            return None

        pub = _build_public_state(state_dict)
        hand = frozenset(int(cid) for cid in hand_list)
        if _SPACE_SUPPRESSION_CARD_ID not in hand:
            return None

        card = _CARDS[_SPACE_SUPPRESSION_CARD_ID]
        if card.side != Side.US:
            return None

        level = pub.space[int(side)]
        if level >= 8:
            return None

        ops_minimum = (2, 2, 2, 2, 3, 3, 3, 4)[min(level, 7)]
        if card.ops < ops_minimum:
            return None

        return _action_dict(_SPACE_SUPPRESSION_CARD_ID, ActionMode.SPACE)


@pytest.mark.serial
def test_space_race_event_suppression_gap_003():
    """Spacing an opponent card must not fire that opponent event."""
    for seed in range(128):
        traced = tscore.play_traced_game_with_callback(_SpaceOpponentCardPolicy(), seed=seed)
        for step in traced.steps:
            if step.side != tscore.Side.USSR:
                continue
            if step.action.card_id != _SPACE_SUPPRESSION_CARD_ID:
                continue
            if _mode_value(step.action.mode) != _mode_value(tscore.ActionMode.Space):
                continue

            assert _SPACE_SUPPRESSION_CARD_ID in set(step.hand_snapshot)
            assert step.defcon_after == step.defcon_before, (
                "Duck and Cover's DEFCON change fired while the card was being spaced"
            )
            return

    pytest.skip(
        "GAP-003: current whole-game callback binding did not surface a seeded USSR "
        "space attempt with card 4 within 128 traced games"
    )


@pytest.mark.parametrize("seed", range(50))
def test_china_card_never_headlined_gap_001(seed: int):
    """China Card (id=6) must never be selected as a headline card."""
    traced = tscore.play_traced_game(
        tscore.PolicyKind.Random,
        tscore.PolicyKind.Random,
        seed=seed,
    )
    headline_cards = [step.action.card_id for step in traced.steps if step.ar == 0]
    assert _CHINA_CARD_ID not in headline_cards, (
        f"seed={seed} produced China Card as a headline: {headline_cards}"
    )


@pytest.mark.parametrize(
    ("space_level", "card_id"),
    [
        (4, 12),
        (4, 22),
        (7, 4),
    ],
)
@pytest.mark.skip(
    reason=(
        "GAP-004: current tscore bindings do not expose traced play or direct legality "
        "queries from an injected mid-game state"
    )
)
def test_space_race_ops_minimum_gap_004(space_level: int, card_id: int):
    """Low-ops cards cannot be spaced once the space track requires more ops."""


@pytest.mark.skip(
    reason=(
        "GAP-044/GAP-045/GAP-046: current Python bindings do not expose the hidden deck "
        "or full hidden-state snapshots needed for an exact deck/hands/discard count"
    )
)
def test_promo_cards_never_in_deck_gap_044_045_046():
    """Promo cards 109-111 should never appear in a new game's deck flow."""


@pytest.mark.skip(
    reason=(
        "GAP-039: current tscore bindings do not expose injected-state influence actions "
        "with controlled target selection for Vietnam Revolts ops accounting"
    )
)
def test_vietnam_revolts_sea_restriction_gap_039():
    """Vietnam Revolts should boost only USSR influence actions in Southeast Asia."""


@pytest.mark.skip(
    reason=(
        "GAP-041: current tscore bindings do not expose a deterministic injected-state "
        "cleanup path for Cuban Missile Crisis turn-end verification"
    )
)
def test_cuban_missile_crisis_turn_end_clear_gap_041():
    """Cuban Missile Crisis should clear during end-of-turn cleanup."""


@pytest.mark.skip(
    reason=(
        "GAP-008: current tscore bindings do not expose deterministic single-step "
        "event resolution from an injected DEFCON-3 Korean War scenario"
    )
)
def test_war_cards_do_not_lower_defcon_gap_008():
    """War card events should not lower DEFCON during resolution."""


@pytest.mark.skip(
    reason=(
        "Harness placeholder: exact promo-card counting over deck/hands/discard remains blocked "
        "until Python can observe hidden deck snapshots"
    )
)
@pytest.mark.parametrize("promo_card_id", _PROMO_CARD_IDS)
def test_promo_card_exact_count_placeholder(promo_card_id: int):
    """Per-card placeholder tied to the exact-count promo-card coverage request."""
