"""Golden-log regression tests for the replay parser.

Each test ingests a full game log from data/raw_logs/ and asserts:
- zero unknown lines (100% coverage)
- at least one GAME_START event
- event count is stable (guards against silent regressions)
"""
import pathlib
import pytest
from tsrl.etl.parser import parse_replay
from tsrl.schemas import EventKind


GOLDEN_DIR = pathlib.Path(__file__).parents[2] / "data" / "raw_logs"


def _parse_golden(filename: str):
    path = GOLDEN_DIR / filename
    return parse_replay(path.read_text(encoding="utf-8"))


class TestTsreplayerGame75:
    """Regression suite for tsreplayer game 75 (przemas139 vs mak_ek)."""

    def setup_method(self):
        self.result = _parse_golden("tsreplayer_75.txt")

    def test_zero_unknown_lines(self):
        assert self.result.unknown_line_count == 0

    def test_has_game_start(self):
        starts = [e for e in self.result.events if e.kind == EventKind.GAME_START]
        assert len(starts) >= 1

    def test_event_count_stable(self):
        # 571 events on first parse; guard against silent regressions
        assert len(self.result.events) >= 571


class TestSyntheticBiddingSetup:
    """Regression suite for bidding-format setup (_PAT_SETUP_HEADER + _PAT_SETUP_USSR_STANDALONE).

    The 51 downloaded tsreplayer games all use the standard non-bidding setup format.
    This synthetic log is the only golden fixture that exercises the bidding path.
    """

    def setup_method(self):
        self.result = _parse_golden("synthetic_bidding_setup.txt")

    def test_zero_unknown_lines(self):
        assert self.result.unknown_line_count == 0

    def test_game_start_emitted_from_bid_line(self):
        # GAME_START must be emitted from the "bids Influence" line, not a standard SETUP line
        starts = [e for e in self.result.events if e.kind == EventKind.GAME_START]
        assert len(starts) == 1
        assert "bids" in starts[0].raw_line

    def test_event_count_stable(self):
        assert len(self.result.events) == 33  # +1 for HANDICAP event
