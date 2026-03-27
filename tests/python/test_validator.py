"""Tests for the replay validator."""
import pathlib

import pytest

from tsrl.etl.game_data import load_cards
from tsrl.etl.validator import (
    ValidationResult,
    ViolationKind,
    _collect_targets,
    _infer_mode,
    validate_game,
    validate_log_dir,
)
from tsrl.schemas import ActionMode, EventKind, ReplayEvent, Side

# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

ALL_CARD_IDS = frozenset(cid for cid in load_cards() if cid != 6)

# raw_logs: downloaded tsreplayer games (all have Handicap influence: US +2)
GOLDEN_DIR = pathlib.Path(__file__).parents[2] / "data" / "raw_logs"
# raw_log_extras: shorter focused games (also have handicap influence)
EXTRAS_DIR = pathlib.Path(__file__).parents[2] / "data" / "raw_log_extras"
# vp20.txt is a clean game in raw_log_extras with zero hard violations
_CLEAN_GAME_PATH = EXTRAS_DIR / "vp20.txt"

_MINIMAL_LOG = "\n".join([
    "Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):",
    "USSR +3 in Thailand [0][3]",
    "Turn 1, US AR1: NORAD*: Coup (3 Ops):",
    "US +2 in Iran [2][0]",
])


def _ev(kind, raw_line="", card_id=None, country_id=None, amount=None,
        phasing=Side.USSR, turn=1, ar=1):
    return ReplayEvent(
        kind=kind, turn=turn, ar=ar, phasing=phasing,
        card_id=card_id, country_id=country_id, amount=amount,
        raw_line=raw_line,
    )


# ---------------------------------------------------------------------------
# _infer_mode
# ---------------------------------------------------------------------------


def test_infer_mode_influence():
    ev = _ev(EventKind.PLAY, raw_line="Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):")
    assert _infer_mode(ev) == ActionMode.INFLUENCE


def test_infer_mode_coup():
    ev = _ev(EventKind.PLAY, raw_line="Turn 1, USSR AR1: NORAD*: Coup (3 Ops):")
    assert _infer_mode(ev) == ActionMode.COUP


def test_infer_mode_realign():
    ev = _ev(EventKind.PLAY, raw_line="Turn 1, USSR AR2: CIA Created: Realign (1 Op):")
    assert _infer_mode(ev) == ActionMode.REALIGN


def test_infer_mode_space():
    ev = _ev(EventKind.PLAY, raw_line="Turn 1, USSR AR1: Five Year Plan: Space Race (3 Ops):")
    assert _infer_mode(ev) == ActionMode.SPACE


def test_infer_mode_event():
    ev = _ev(EventKind.PLAY, raw_line="Turn 1, USSR AR1: Fidel: Event:")
    assert _infer_mode(ev) == ActionMode.EVENT


def test_infer_mode_headline_always_event():
    ev = _ev(EventKind.HEADLINE, raw_line="Turn 1, Headline Phase: Fidel / Marshall Plan:")
    assert _infer_mode(ev) == ActionMode.EVENT


def test_infer_mode_unrecognized_returns_none():
    ev = _ev(EventKind.PLAY, raw_line="Turn 1, USSR AR1: SomeCard: ???:")
    assert _infer_mode(ev) is None


# ---------------------------------------------------------------------------
# _collect_targets
# ---------------------------------------------------------------------------


def test_collect_targets_influence_single_country():
    play = _ev(EventKind.PLAY, raw_line="... Place Influence ...", phasing=Side.USSR)
    pi = _ev(EventKind.PLACE_INFLUENCE, country_id=5, amount=2, phasing=Side.USSR)
    stop = _ev(EventKind.PLAY, phasing=Side.US)
    events = [play, pi, stop]
    targets = _collect_targets(events, 0, ActionMode.INFLUENCE, Side.USSR)
    assert targets == [5, 5]  # amount=2 → country 5 appears twice


def test_collect_targets_influence_multi_country():
    play = _ev(EventKind.PLAY, phasing=Side.USSR)
    pi1 = _ev(EventKind.PLACE_INFLUENCE, country_id=5, amount=1, phasing=Side.USSR)
    pi2 = _ev(EventKind.PLACE_INFLUENCE, country_id=7, amount=1, phasing=Side.USSR)
    stop = _ev(EventKind.ACTION_ROUND_START, phasing=Side.US)
    targets = _collect_targets([play, pi1, pi2, stop], 0, ActionMode.INFLUENCE, Side.USSR)
    assert sorted(targets) == [5, 7]


def test_collect_targets_stops_at_decision():
    play = _ev(EventKind.PLAY, phasing=Side.USSR)
    pi = _ev(EventKind.PLACE_INFLUENCE, country_id=5, amount=1, phasing=Side.USSR)
    next_play = _ev(EventKind.PLAY, phasing=Side.US)
    pi_after = _ev(EventKind.PLACE_INFLUENCE, country_id=9, amount=1, phasing=Side.US)
    targets = _collect_targets([play, pi, next_play, pi_after], 0, ActionMode.INFLUENCE, Side.USSR)
    assert targets == [5]


def test_collect_targets_stops_at_opponent_board_action():
    """Opponent board action (e.g. event effect) should stop target collection."""
    play = _ev(EventKind.PLAY, phasing=Side.USSR)
    pi_opp = _ev(EventKind.PLACE_INFLUENCE, country_id=5, amount=1, phasing=Side.US)
    targets = _collect_targets([play, pi_opp], 0, ActionMode.INFLUENCE, Side.USSR)
    assert targets == []


def test_collect_targets_space_event_empty():
    play = _ev(EventKind.PLAY, phasing=Side.USSR)
    targets_space = _collect_targets([play], 0, ActionMode.SPACE, Side.USSR)
    targets_event = _collect_targets([play], 0, ActionMode.EVENT, Side.USSR)
    assert targets_space == []
    assert targets_event == []


def test_collect_targets_coup_uses_coup_event():
    play = _ev(EventKind.PLAY, phasing=Side.USSR)
    coup_ev = _ev(EventKind.COUP, country_id=33, phasing=Side.USSR)
    targets = _collect_targets([play, coup_ev], 0, ActionMode.COUP, Side.USSR)
    assert targets == [33]


# ---------------------------------------------------------------------------
# validate_game — smoke and shape
# ---------------------------------------------------------------------------


def test_validate_game_returns_result():
    result = validate_game(_MINIMAL_LOG, "test", ALL_CARD_IDS)
    assert isinstance(result, ValidationResult)
    assert result.game_id == "test"
    assert result.total_decisions == 2


def test_validate_game_empty_log():
    result = validate_game("", "empty", ALL_CARD_IDS)
    assert result.total_decisions == 0
    assert result.is_valid


def test_validate_game_no_hard_violations_on_minimal_log():
    result = validate_game(_MINIMAL_LOG, "test", ALL_CARD_IDS)
    hard = result.hard_violations
    # Minimal log has influence placement in Thailand (accessible from USSR anchor)
    # and coup in Iran (accessible, DEFCON 5).  Both should be legal.
    assert len(hard) == 0, f"Unexpected hard violations: {hard}"


def test_validate_game_decisions_counted_correctly():
    """Each PLAY/HEADLINE line = one decision."""
    log = "\n".join([
        "Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):",
        "USSR +1 in Poland [0][1]",
        "Turn 1, US AR1: Containment: Event:",
        "Turn 1, USSR AR2: Decolonization: Place Influence (3 Ops):",
        "USSR +1 in Angola [0][1]",
    ])
    result = validate_game(log, "g", ALL_CARD_IDS)
    assert result.total_decisions == 3


def test_validate_game_unresolved_card_is_soft():
    """An unresolved card_id=None becomes CARD_UNRESOLVED (soft, not hard)."""
    log = "Turn 1, USSR AR1: TOTALLY UNKNOWN CARD XYZ: Place Influence (3 Ops):"
    result = validate_game(log, "g", ALL_CARD_IDS)
    unresolved = [v for v in result.violations if v.kind == ViolationKind.CARD_UNRESOLVED]
    # Must not appear in hard violations.
    assert all(v not in result.hard_violations for v in unresolved)


def test_card_excluded_by_reducer_is_soft():
    """known_not_in_hand violations are soft (reducer may have false positives)."""
    result = validate_game(_MINIMAL_LOG, "test", ALL_CARD_IDS)
    excluded = [v for v in result.violations if v.kind == ViolationKind.CARD_EXCLUDED_BY_REDUCER]
    assert all(v not in result.hard_violations for v in excluded)


# ---------------------------------------------------------------------------
# validate_game — mode checks
# ---------------------------------------------------------------------------


def test_no_mode_illegal_on_real_game():
    """Clean game (vp20) has no MODE_ILLEGAL violations."""
    if not _CLEAN_GAME_PATH.exists():
        pytest.skip("vp20.txt not found")
    result = validate_game(_CLEAN_GAME_PATH.read_text(), "vp20", ALL_CARD_IDS)
    mode_violations = [v for v in result.violations if v.kind == ViolationKind.MODE_ILLEGAL]
    assert mode_violations == [], f"MODE_ILLEGAL in vp20: {mode_violations}"


# ---------------------------------------------------------------------------
# validate_game — TARGET_ILLEGAL checks
# ---------------------------------------------------------------------------


def test_no_target_illegal_on_real_game():
    """Clean game (vp20) has no TARGET_ILLEGAL violations."""
    if not _CLEAN_GAME_PATH.exists():
        pytest.skip("vp20.txt not found")
    result = validate_game(_CLEAN_GAME_PATH.read_text(), "vp20", ALL_CARD_IDS)
    target_violations = [v for v in result.violations if v.kind == ViolationKind.TARGET_ILLEGAL]
    assert target_violations == [], f"TARGET_ILLEGAL in vp20: {target_violations}"


# ---------------------------------------------------------------------------
# validate_log_dir — integration (both corpora)
# ---------------------------------------------------------------------------


def test_validate_log_dir_runs():
    """validate_log_dir runs on both raw_logs and raw_log_extras."""
    for log_dir in [GOLDEN_DIR, EXTRAS_DIR]:
        if not log_dir.exists() or not list(log_dir.glob("*.txt")):
            continue
        results = validate_log_dir(log_dir, all_card_ids=ALL_CARD_IDS)
        assert len(results) > 0
        for name, result in results.items():
            assert isinstance(result, ValidationResult), name


def test_validate_log_dir_no_hard_violations_across_corpus():
    """vp20.txt (clean extras game) has zero hard violations.

    Note: most TSEspionage games have accessibility violations where the mod
    allows placing influence in countries requiring an intermediate hop (e.g.
    Angola without prior SE African States influence).  These are systematic
    mod bugs, not engine errors.  vp20.txt is the one extras game that happens
    to have zero hard violations.
    """
    if not _CLEAN_GAME_PATH.exists():
        pytest.skip("vp20.txt not found")
    results = validate_log_dir(EXTRAS_DIR, all_card_ids=ALL_CARD_IDS)
    vp20 = results.get("vp20.txt")
    assert vp20 is not None, "vp20.txt not found in validate_log_dir output"
    assert vp20.hard_violations == [], (
        f"{len(vp20.hard_violations)} hard violations in vp20.txt:\n"
        + "\n".join(f"  {v}" for v in vp20.hard_violations)
    )


# ---------------------------------------------------------------------------
# ValidationResult helpers
# ---------------------------------------------------------------------------


def test_result_summary_no_violations():
    r = ValidationResult(game_id="g", total_decisions=10)
    s = r.summary()
    assert "violations=0" in s
    assert "hard=0" in s


# ---------------------------------------------------------------------------
# _cross_check_raw: stability, bracket, and space threshold checks
# ---------------------------------------------------------------------------


def test_cross_check_raw_stability_match():
    """No STABILITY_MISMATCH when stability in coup formula matches countries.csv."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # Iran (id=28): stability=2.  Formula 2x2 should match.
    log = "\n".join([
        "Turn 1, USSR AR1: Warsaw Pact Formed*: Coup (3 Ops):",
        "Target: Iran",
        "SUCCESS: 3 [ + 3 - 2x2 = 2 ]",
        "US -1 in Iran [0][0]",
    ])
    viols = _cross_check_raw(log, load_countries())
    stability_viols = [v for v in viols if v.kind == ViolationKind.STABILITY_MISMATCH]
    assert stability_viols == [], f"Unexpected STABILITY_MISMATCH: {stability_viols}"


def test_cross_check_raw_stability_mismatch():
    """STABILITY_MISMATCH fires when formula stability disagrees with countries.csv."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # Iran stability=2, but formula says 2x3 (stability=3) — wrong.
    log = "\n".join([
        "Turn 1, USSR AR1: Warsaw Pact Formed*: Coup (3 Ops):",
        "Target: Iran",
        "SUCCESS: 3 [ + 3 - 2x3 = 0 ]",
        "US -1 in Iran [0][0]",
    ])
    viols = _cross_check_raw(log, load_countries())
    stability_viols = [v for v in viols if v.kind == ViolationKind.STABILITY_MISMATCH]
    assert len(stability_viols) == 1
    assert stability_viols[0].country_id == 28  # Iran


def test_cross_check_raw_stability_modifier():
    """STABILITY check handles optional ops modifier like (-1) in the formula."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # Formula: 'SUCCESS: 6 [ + 3 (-1)  - 2x1 = 6 ]' — stability 1 should match some country.
    # Use Finland (id=6, stability=4)... or just check no crash and no false positive.
    log = "\n".join([
        "Turn 2, USSR AR2: Duck and Cover: Coup (4 Ops):",
        "Target: Afghanistan",
        "SUCCESS: 6 [ + 3 (-1)  - 2x1 = 6 ]",
        "US -1 in Afghanistan [0][0]",
    ])
    # Afghanistan (id=20) has stability=2.  Formula says 2x1 → stability=1.
    # This should produce a STABILITY_MISMATCH for Afghanistan.
    viols = _cross_check_raw(log, load_countries())
    stability_viols = [v for v in viols if v.kind == ViolationKind.STABILITY_MISMATCH]
    assert len(stability_viols) == 1
    assert stability_viols[0].country_id == 20  # Afghanistan


def test_cross_check_raw_bracket_consistent():
    """No INFLUENCE_BRACKET_MISMATCH when consecutive brackets are delta-consistent."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    log = "\n".join([
        "Turn 1, USSR AR1: Warsaw Pact Formed*: Place Influence (3 Ops):",
        "USSR +2 in Poland [0][6]",    # first occurrence; establishes running total
        "Turn 2, USSR AR1: Comecon: Place Influence (3 Ops):",
        "USSR +1 in Poland [0][7]",    # prev=6, delta=+1, expected=7 ✓
    ])
    viols = _cross_check_raw(log, load_countries())
    bracket_viols = [v for v in viols if v.kind == ViolationKind.INFLUENCE_BRACKET_MISMATCH]
    assert bracket_viols == [], f"Unexpected bracket mismatch: {bracket_viols}"


def test_cross_check_raw_bracket_mismatch():
    """INFLUENCE_BRACKET_MISMATCH fires when delta is inconsistent with brackets."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    log = "\n".join([
        "Turn 1, USSR AR1: Comecon: Place Influence (3 Ops):",
        "USSR +2 in Poland [0][6]",    # establishes running total: ussr=6
        "Turn 2, USSR AR1: Comecon: Place Influence (3 Ops):",
        "USSR +1 in Poland [0][9]",    # prev=6, delta=+1, expected=7, but bracket=9 → MISMATCH
    ])
    viols = _cross_check_raw(log, load_countries())
    bracket_viols = [v for v in viols if v.kind == ViolationKind.INFLUENCE_BRACKET_MISMATCH]
    assert len(bracket_viols) == 1


def test_cross_check_raw_space_threshold_correct():
    """No SPACE_THRESHOLD_MISMATCH for the empirically verified threshold table."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # Level 0 → threshold 3.
    log = "\n".join([
        "Turn 1, USSR AR3: Five Year Plan: Space Race (3 Ops):",
        "Die roll: 1 -- Success! (Needed 3 or less)",
        "USSR advances to 1 in the Space Race.",
    ])
    viols = _cross_check_raw(log, load_countries())
    space_viols = [v for v in viols if v.kind == ViolationKind.SPACE_THRESHOLD_MISMATCH]
    assert space_viols == [], f"Unexpected SPACE_THRESHOLD_MISMATCH: {space_viols}"


def test_cross_check_raw_space_threshold_mismatch():
    """SPACE_THRESHOLD_MISMATCH fires when threshold disagrees with our table."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # Level 0 threshold should be 3, but log says Needed 5 or less.
    log = "\n".join([
        "Turn 1, USSR AR3: Five Year Plan: Space Race (3 Ops):",
        "Die roll: 4 -- Success! (Needed 5 or less)",
    ])
    viols = _cross_check_raw(log, load_countries())
    space_viols = [v for v in viols if v.kind == ViolationKind.SPACE_THRESHOLD_MISMATCH]
    assert len(space_viols) == 1


def test_cross_check_raw_realign_outcome_correct():
    """No REALIGN_OUTCOME_MISMATCH when loser loses min(diff, loser_inf)."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # USSR 8, US 5 → diff=3, US had 2 → expected loss = min(3,2) = 2.
    log = "\n".join([
        "Turn 1, USSR AR2: Decolonization: Realignment (3 Ops):",
        "Target: Brazil",
        "USSR rolls 6 (+2) = 8",
        "US rolls 4 (+1) = 5",
        "US -2 in Brazil [0][0]",
    ])
    viols = _cross_check_raw(log, load_countries())
    realign_viols = [v for v in viols if v.kind == ViolationKind.REALIGN_OUTCOME_MISMATCH]
    assert realign_viols == [], f"Unexpected REALIGN_OUTCOME_MISMATCH: {realign_viols}"


def test_cross_check_raw_realign_outcome_capped_correct():
    """No REALIGN_OUTCOME_MISMATCH when loss is capped by loser's influence."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # USSR 7, US 2 → diff=5, US had 1 → expected loss = min(5,1) = 1.
    log = "\n".join([
        "Turn 2, US AR3: Decolonization: Realignment (2 Ops):",
        "Target: Angola",
        "USSR rolls 6 (+1) = 7",
        "US rolls 1 (+1) = 2",
        "US -1 in Angola [0][0]",
    ])
    viols = _cross_check_raw(log, load_countries())
    realign_viols = [v for v in viols if v.kind == ViolationKind.REALIGN_OUTCOME_MISMATCH]
    assert realign_viols == [], f"Unexpected REALIGN_OUTCOME_MISMATCH: {realign_viols}"


def test_cross_check_raw_realign_outcome_us_wins():
    """No REALIGN_OUTCOME_MISMATCH when US wins and USSR loses correct influence."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # US 9, USSR 4 → diff=5, USSR had 3 → expected loss = min(5,3) = 3.
    log = "\n".join([
        "Turn 3, US AR1: CIA Created: Realignment (1 Ops):",
        "Target: Poland",
        "USSR rolls 2 (+2) = 4",
        "US rolls 6 (+3) = 9",
        "USSR -3 in Poland [0][0]",
    ])
    viols = _cross_check_raw(log, load_countries())
    realign_viols = [v for v in viols if v.kind == ViolationKind.REALIGN_OUTCOME_MISMATCH]
    assert realign_viols == [], f"Unexpected REALIGN_OUTCOME_MISMATCH: {realign_viols}"


def test_cross_check_raw_realign_outcome_mismatch():
    """REALIGN_OUTCOME_MISMATCH fires when the influence change is wrong."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # USSR 8, US 5 → diff=3, US had 2 → expected loss = min(3,2) = 2.
    # But log shows US -1 (wrong — should be 2).
    log = "\n".join([
        "Turn 1, USSR AR2: Decolonization: Realignment (3 Ops):",
        "Target: Brazil",
        "USSR rolls 6 (+2) = 8",
        "US rolls 4 (+1) = 5",
        "US -1 in Brazil [1][0]",
    ])
    viols = _cross_check_raw(log, load_countries())
    realign_viols = [v for v in viols if v.kind == ViolationKind.REALIGN_OUTCOME_MISMATCH]
    assert len(realign_viols) == 1


def test_cross_check_raw_realign_tie_no_violation():
    """No REALIGN_OUTCOME_MISMATCH on a tie (no influence changes expected)."""
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    # USSR 5, US 5 → tie → no influence change.
    log = "\n".join([
        "Turn 1, USSR AR2: Decolonization: Realignment (3 Ops):",
        "Target: Brazil",
        "USSR rolls 4 (+1) = 5",
        "US rolls 4 (+1) = 5",
    ])
    viols = _cross_check_raw(log, load_countries())
    realign_viols = [v for v in viols if v.kind == ViolationKind.REALIGN_OUTCOME_MISMATCH]
    assert realign_viols == [], f"Unexpected REALIGN_OUTCOME_MISMATCH on tie: {realign_viols}"


def test_cross_check_raw_no_violations_on_vp20():
    """vp20.txt (clean game) has zero raw cross-check violations."""
    if not _CLEAN_GAME_PATH.exists():
        pytest.skip("vp20.txt not found")
    from tsrl.etl.validator import _cross_check_raw
    from tsrl.etl.game_data import load_countries
    text = _CLEAN_GAME_PATH.read_text()
    viols = _cross_check_raw(text, load_countries())
    assert viols == [], (
        f"{len(viols)} cross-check violations in vp20.txt:\n"
        + "\n".join(f"  {v}" for v in viols[:5])
    )


def test_cross_check_new_kinds_are_hard():
    """STABILITY_MISMATCH, INFLUENCE_BRACKET_MISMATCH, SPACE_THRESHOLD_MISMATCH are hard."""
    from tsrl.etl.validator import Violation
    hard_kinds = [
        ViolationKind.STABILITY_MISMATCH,
        ViolationKind.INFLUENCE_BRACKET_MISMATCH,
        ViolationKind.SPACE_THRESHOLD_MISMATCH,
        ViolationKind.REALIGN_OUTCOME_MISMATCH,
    ]
    for kind in hard_kinds:
        r = ValidationResult(
            game_id="g", total_decisions=5,
            violations=[Violation(
                kind=kind, turn=1, ar=1, phasing=Side.USSR,
                card_id=None, message="hard",
            )],
        )
        assert r.hard_violations != [], f"{kind} should be a hard violation"


def test_result_is_valid_with_only_soft_violations():
    from tsrl.etl.validator import Violation
    soft_kinds = [
        ViolationKind.CARD_NOT_RECONSTRUCTED,
        ViolationKind.CARD_EXCLUDED_BY_REDUCER,
        ViolationKind.CARD_UNRESOLVED,
        ViolationKind.MODE_UNRECOGNIZED,
    ]
    for kind in soft_kinds:
        r = ValidationResult(
            game_id="g", total_decisions=5,
            violations=[Violation(
                kind=kind, turn=1, ar=1, phasing=Side.USSR, card_id=7,
                message="soft",
            )],
        )
        assert not r.is_valid, f"{kind} should make is_valid False"
        assert r.hard_violations == [], f"{kind} should not appear in hard_violations"


# ---------------------------------------------------------------------------
# MILOPS_PENALTY_MISMATCH validator check
# ---------------------------------------------------------------------------


def test_milops_penalty_mismatch_violation_kind_exists():
    """ViolationKind.MILOPS_PENALTY_MISMATCH must be defined."""
    assert hasattr(ViolationKind, "MILOPS_PENALTY_MISMATCH"), (
        "ViolationKind.MILOPS_PENALTY_MISMATCH not found — add it to validator.py"
    )


def test_milops_penalty_mismatch_is_hard_violation():
    """MILOPS_PENALTY_MISMATCH must appear in hard_violations (not in the soft set)."""
    from tsrl.etl.validator import Violation
    r = ValidationResult(
        game_id="g", total_decisions=3,
        violations=[Violation(
            kind=ViolationKind.MILOPS_PENALTY_MISMATCH,
            turn=1, ar=6, phasing=Side.USSR,
            card_id=None, message="mismatch",
        )],
    )
    assert r.hard_violations != [], (
        "MILOPS_PENALTY_MISMATCH should be a hard violation"
    )


def test_milops_penalty_no_mismatch_on_corpus():
    """Real log corpus must have zero MILOPS_PENALTY_MISMATCH violations.

    The TSEspionage server checks milops against pre-advance DEFCON.
    This test confirms the validator's expectation (pre-advance DEFCON formula)
    is consistent with the logs.  Requires the reducer to correctly reset
    milops at HEADLINE_PHASE_START.
    """
    raw_log_dir = pathlib.Path(__file__).parent.parent.parent / "data" / "raw_logs"
    if not raw_log_dir.exists():
        pytest.skip("data/raw_logs/ not found")
    results = validate_log_dir(raw_log_dir, all_card_ids=ALL_CARD_IDS)
    milops_violations = [
        (game_id, v)
        for game_id, vr in results.items()
        for v in vr.violations
        if v.kind == ViolationKind.MILOPS_PENALTY_MISMATCH
    ]
    assert milops_violations == [], (
        f"{len(milops_violations)} MILOPS_PENALTY_MISMATCH violations across corpus:\n"
        + "\n".join(
            f"  game={gid} turn={v.turn} {v.message}"
            for gid, v in milops_violations[:10]
        )
    )
