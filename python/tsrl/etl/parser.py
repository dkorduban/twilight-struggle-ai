"""
Twilight Struggle replay log parser.

Parses raw replay log text into a sequence of normalized ReplayEvents.

Design rules:
  - Unknown lines are NEVER silently dropped; emit EventKind.UNKNOWN with raw_line preserved.
  - All matched patterns are deterministic; same input → same output.
  - Parser emits events in file order; no reordering.
  - Track parse coverage metrics per game.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Iterator

from tsrl.schemas import EventKind, ReplayEvent, Side


# ---------------------------------------------------------------------------
# Parse result
# ---------------------------------------------------------------------------


@dataclass
class ParseResult:
    """Output of parsing a single replay file."""

    game_id: str
    events: list[ReplayEvent]
    unknown_lines: list[tuple[int, str]]  # (line_number, raw_line)
    total_lines: int

    @property
    def line_parse_coverage(self) -> float:
        if self.total_lines == 0:
            return 1.0
        return 1.0 - len(self.unknown_lines) / self.total_lines

    @property
    def unknown_line_count(self) -> int:
        return len(self.unknown_lines)


# ---------------------------------------------------------------------------
# Parsing context (mutable per-game state used during parsing)
# ---------------------------------------------------------------------------


@dataclass
class _ParseContext:
    game_id: str = ""
    turn: int = 0
    ar: int = 0
    phasing: Side = Side.USSR
    ussr_player: str = ""
    us_player: str = ""


# ---------------------------------------------------------------------------
# Compiled patterns
# ---------------------------------------------------------------------------
# NOTE: These are initial stubs.  Patterns must be validated against actual
# replay logs before use.  Add new patterns alongside tests.

_PAT_GAME_ID = re.compile(r"^GAME[_\s]?ID\s*:\s*(\S+)", re.IGNORECASE)
_PAT_PLAYERS = re.compile(
    r"^PLAYERS\s*:\s*(\S+)\s+vs\.?\s+(\S+)", re.IGNORECASE
)
_PAT_TURN_START = re.compile(r"^[-=\s]*TURN\s+(\d+)\s*[-=]*$", re.IGNORECASE)
_PAT_TURN_END = re.compile(r"^END\s+OF\s+TURN\s+(\d+)", re.IGNORECASE)
_PAT_HEADLINE_PHASE = re.compile(r"^\s*HEADLINE\s*:", re.IGNORECASE)
_PAT_AR_START = re.compile(r"^\s*AR\s*(\d+)\s*:", re.IGNORECASE)
_PAT_RESHUFFLE = re.compile(r"discard\s+pile\s+reshuffled", re.IGNORECASE)
_PAT_FINAL_SCORE = re.compile(r"^FINAL\s+SCORE", re.IGNORECASE)

# Card play patterns (placeholders – calibrate against actual log format)
_PAT_HEADLINE = re.compile(
    r"(\w+)\s+headlines?\s+(.+?)(?:\s*\(.*\))?\s*$", re.IGNORECASE
)
_PAT_PLAY = re.compile(
    r"(\w+)\s+plays?\s+(.+?)\s+(?:for\s+(?:ops|space|event)|(?:\(event\)))",
    re.IGNORECASE,
)
_PAT_FORCED_DISCARD = re.compile(
    r"(\w+)\s+(?:is\s+)?forced\s+to\s+discard\s+(.+)", re.IGNORECASE
)
_PAT_REVEAL_HAND = re.compile(
    r"(\w+)'s?\s+hand\s+(?:is\s+)?revealed\s*:\s*(.+)", re.IGNORECASE
)
_PAT_END_TURN_HELD = re.compile(
    r"(\w+)\s+holds?\s+(?:into\s+next\s+turn\s*:\s*)?(.+)", re.IGNORECASE
)
_PAT_CHINA_PASS = re.compile(
    r"china\s+card\s+passed\s+to\s+(\w+)", re.IGNORECASE
)
_PAT_DEFCON = re.compile(r"defcon\s+(?:drops?|rises?|changes?)\s+to\s+(\d)", re.IGNORECASE)
_PAT_VP = re.compile(r"([+-]?\d+)\s+VP\s+to\s+(\w+)", re.IGNORECASE)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def parse_replay(text: str, game_id: str = "") -> ParseResult:
    """Parse a full replay log string into a ParseResult.

    Args:
        text: Raw replay log content.
        game_id: Optional game identifier (used for reporting).

    Returns:
        ParseResult with normalized events and parse-coverage metrics.
    """
    events: list[ReplayEvent] = []
    unknown_lines: list[tuple[int, str]] = []
    ctx = _ParseContext(game_id=game_id)
    lines = text.splitlines()

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if not stripped:
            continue

        ev = _try_parse_line(stripped, lineno, ctx)
        if ev is None:
            unknown_lines.append((lineno, raw))
            events.append(
                ReplayEvent(
                    kind=EventKind.UNKNOWN,
                    turn=ctx.turn,
                    ar=ctx.ar,
                    phasing=ctx.phasing,
                    raw_line=raw,
                    line_number=lineno,
                )
            )
        else:
            events.append(ev)

    return ParseResult(
        game_id=ctx.game_id or game_id,
        events=events,
        unknown_lines=unknown_lines,
        total_lines=sum(1 for l in lines if l.strip()),
    )


def iter_events(text: str, game_id: str = "") -> Iterator[ReplayEvent]:
    """Streaming event iterator (wraps parse_replay for convenience)."""
    result = parse_replay(text, game_id)
    yield from result.events


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _try_parse_line(
    line: str, lineno: int, ctx: _ParseContext
) -> ReplayEvent | None:
    """Attempt to parse a single non-empty line.

    Returns a ReplayEvent on success, None if no pattern matches.
    Updates ctx in place for structural events.
    """
    # --- Structural ---
    if m := _PAT_GAME_ID.match(line):
        ctx.game_id = m.group(1)
        return ReplayEvent(
            kind=EventKind.GAME_START,
            turn=0, ar=0, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if m := _PAT_PLAYERS.match(line):
        ctx.ussr_player = m.group(1)
        ctx.us_player = m.group(2)
        return ReplayEvent(
            kind=EventKind.GAME_START,
            turn=0, ar=0, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if m := _PAT_TURN_START.match(line):
        ctx.turn = int(m.group(1))
        ctx.ar = 0
        return ReplayEvent(
            kind=EventKind.TURN_START,
            turn=ctx.turn, ar=0, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_TURN_END.match(line):
        return ReplayEvent(
            kind=EventKind.TURN_END,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_HEADLINE_PHASE.match(line):
        ctx.ar = 0
        return ReplayEvent(
            kind=EventKind.HEADLINE_PHASE_START,
            turn=ctx.turn, ar=0, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if m := _PAT_AR_START.match(line):
        ctx.ar = int(m.group(1))
        return ReplayEvent(
            kind=EventKind.ACTION_ROUND_START,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_RESHUFFLE.search(line):
        return ReplayEvent(
            kind=EventKind.RESHUFFLE,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_FINAL_SCORE.match(line):
        return ReplayEvent(
            kind=EventKind.GAME_END,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    # --- Card events ---
    # NOTE: Card/country name resolution (str → id) is intentionally deferred.
    # The parser emits card_id=None for now; a separate resolution pass uses
    # data/spec/cards.csv to fill in ids.  This keeps the parser stateless
    # with respect to game data and easier to test in isolation.

    if _PAT_HEADLINE.match(line):
        return ReplayEvent(
            kind=EventKind.HEADLINE,
            turn=ctx.turn, ar=0, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_PLAY.match(line):
        return ReplayEvent(
            kind=EventKind.PLAY,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_FORCED_DISCARD.match(line):
        return ReplayEvent(
            kind=EventKind.FORCED_DISCARD,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_REVEAL_HAND.match(line):
        return ReplayEvent(
            kind=EventKind.REVEAL_HAND,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_END_TURN_HELD.match(line):
        return ReplayEvent(
            kind=EventKind.END_TURN_HELD,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_CHINA_PASS.match(line):
        return ReplayEvent(
            kind=EventKind.CHINA_CARD_PASS,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_DEFCON.search(line):
        return ReplayEvent(
            kind=EventKind.DEFCON_CHANGE,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    if _PAT_VP.search(line):
        return ReplayEvent(
            kind=EventKind.VP_CHANGE,
            turn=ctx.turn, ar=ctx.ar, phasing=ctx.phasing,
            raw_line=line, line_number=lineno,
        )

    return None  # unknown line
