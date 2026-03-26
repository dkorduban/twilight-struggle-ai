"""Tests for the replay log parser.

Patterns are validated here against synthetic lines.  Golden-log tests
live in tests/python/test_parser_golden.py (to be added once we have logs).
"""
import pytest
from tsrl.etl.parser import parse_replay
from tsrl.schemas import EventKind, Side


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def parse_single(line: str):
    result = parse_replay(line)
    events = [e for e in result.events if e.kind != EventKind.UNKNOWN]
    return events


# ---------------------------------------------------------------------------
# Structural events
# ---------------------------------------------------------------------------


def test_turn_start():
    result = parse_replay("--- TURN 3 ---")
    evs = [e for e in result.events if e.kind == EventKind.TURN_START]
    assert len(evs) == 1
    assert evs[0].turn == 3


def test_turn_end():
    result = parse_replay("END OF TURN 2")
    evs = [e for e in result.events if e.kind == EventKind.TURN_END]
    assert len(evs) == 1
    assert evs[0].turn == 0  # ctx not updated yet in this minimal test


def test_ar_start():
    result = parse_replay("--- TURN 1 ---\nAR3:")
    ar_evs = [e for e in result.events if e.kind == EventKind.ACTION_ROUND_START]
    assert len(ar_evs) == 1
    assert ar_evs[0].ar == 3


def test_headline_phase():
    result = parse_replay("HEADLINE:")
    evs = [e for e in result.events if e.kind == EventKind.HEADLINE_PHASE_START]
    assert len(evs) == 1


def test_reshuffle():
    result = parse_replay("Discard pile reshuffled into draw pile")
    evs = [e for e in result.events if e.kind == EventKind.RESHUFFLE]
    assert len(evs) == 1


def test_game_end():
    result = parse_replay("FINAL SCORE: USSR wins by 6 VP")
    evs = [e for e in result.events if e.kind == EventKind.GAME_END]
    assert len(evs) == 1


# ---------------------------------------------------------------------------
# Card events
# ---------------------------------------------------------------------------


def test_headline_event():
    result = parse_replay("PlayerA headlines Duck and Cover")
    evs = [e for e in result.events if e.kind == EventKind.HEADLINE]
    assert len(evs) == 1


def test_play_for_ops():
    result = parse_replay("PlayerA plays Decolonization for ops")
    evs = [e for e in result.events if e.kind == EventKind.PLAY]
    assert len(evs) == 1


def test_play_event():
    result = parse_replay("PlayerB plays Five Year Plan (event)")
    evs = [e for e in result.events if e.kind == EventKind.PLAY]
    assert len(evs) == 1


def test_forced_discard():
    result = parse_replay("PlayerB is forced to discard Defectors")
    evs = [e for e in result.events if e.kind == EventKind.FORCED_DISCARD]
    assert len(evs) == 1


def test_reveal_hand():
    result = parse_replay("PlayerA's hand is revealed: CIA Created, Decolonization, COMECON")
    evs = [e for e in result.events if e.kind == EventKind.REVEAL_HAND]
    assert len(evs) == 1


def test_china_pass():
    result = parse_replay("China Card passed to PlayerB")
    evs = [e for e in result.events if e.kind == EventKind.CHINA_CARD_PASS]
    assert len(evs) == 1


def test_defcon_change():
    result = parse_replay("DEFCON drops to 2")
    evs = [e for e in result.events if e.kind == EventKind.DEFCON_CHANGE]
    assert len(evs) == 1


def test_vp_change():
    result = parse_replay("+3 VP to USSR")
    evs = [e for e in result.events if e.kind == EventKind.VP_CHANGE]
    assert len(evs) == 1


# ---------------------------------------------------------------------------
# Unknown line handling
# ---------------------------------------------------------------------------


def test_unknown_lines_not_dropped():
    """Unknown lines must appear as UNKNOWN events, not be silently dropped."""
    text = "--- TURN 1 ---\nsome completely unknown line\nAR1:"
    result = parse_replay(text)
    unknown_evs = [e for e in result.events if e.kind == EventKind.UNKNOWN]
    assert len(unknown_evs) == 1
    assert "some completely unknown line" in unknown_evs[0].raw_line


def test_unknown_lines_tracked_in_result():
    text = "--- TURN 1 ---\nunknown line 1\nunknown line 2\nAR1:"
    result = parse_replay(text)
    assert result.unknown_line_count == 2
    assert len(result.unknown_lines) == 2


def test_coverage_all_known():
    text = "--- TURN 1 ---\nAR1:\nEND OF TURN 1"
    result = parse_replay(text)
    assert result.line_parse_coverage == 1.0


def test_coverage_some_unknown():
    text = "--- TURN 1 ---\nunknown\nAR1:"
    result = parse_replay(text)
    assert 0 < result.line_parse_coverage < 1.0


def test_empty_replay():
    result = parse_replay("")
    assert result.events == []
    assert result.unknown_line_count == 0
    assert result.line_parse_coverage == 1.0


# ---------------------------------------------------------------------------
# Turn context propagation
# ---------------------------------------------------------------------------


def test_turn_context_propagates():
    text = "--- TURN 4 ---\nAR2:\nPlayerX plays Decolonization for ops"
    result = parse_replay(text)
    play_evs = [e for e in result.events if e.kind == EventKind.PLAY]
    assert len(play_evs) == 1
    assert play_evs[0].turn == 4
    assert play_evs[0].ar == 2
