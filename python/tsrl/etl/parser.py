"""
Twilight Struggle replay log parser.

Parses raw replay logs in TSEspionage/ACTS format into normalized ReplayEvents.

Design rules:
  - Unknown lines are NEVER silently dropped; they become EventKind.UNKNOWN with
    raw_line preserved and appear in ParseResult.unknown_lines.
  - Informational sub-lines (e.g. "Target: Iran", "Die roll: 3 -- Success!") are
    RECOGNIZED (not unknown) but produce no events.
  - All matched patterns are deterministic; same input → same output.
  - Events are emitted in file order; no reordering.
  - Card/country name→ID resolution is intentionally deferred to a separate
    resolver pass.  The parser sets card_id=None; a resolver fills IDs from
    cards.csv / countries.csv.

Real log format (TSEspionage/ACTS):
  SETUP block
    SETUP: : PLAYER will play as USSR.
    PLAYER will play as USA.
    [optional: Handicap/bidding/scenario lines]
    SIDE +N in COUNTRY [us_inf][ussr_inf]   ← initial influence

  Turn blocks
    Turn N, Headline Phase: CARD1 & CARD2: [inline-text]
      USSR Headlines CARD1
      US Headlines CARD2
      Event: CARD1
      [sub-effects: influence, DEFCON, VP, …]

    Turn N, SIDE ARN: CARD: ACTION-TEXT
      [sub-effects]

    Turn N, Cleanup: : [inline-text]
      [sub-effects: cleanup discards, card expirations, VP for milops]

  Game end
    : : SIDE gains N VP. Score is SIDE M.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
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
# Parsing context (mutable per-game, updated as headers are parsed)
# ---------------------------------------------------------------------------


@dataclass
class _ParseContext:
    game_id: str = ""
    turn: int = 0
    ar: int = 0
    phasing: Side = Side.USSR
    ussr_player: str = ""
    us_player: str = ""
    in_setup: bool = True
    in_cleanup: bool = False


# ---------------------------------------------------------------------------
# Compiled regex patterns
# ---------------------------------------------------------------------------

# ── Setup block ──────────────────────────────────────────────────────────────

# "SETUP: : brown_town will play as USSR."  (USSR player on same line as SETUP marker)
_PAT_SETUP_USSR = re.compile(r"^SETUP: : (.+) will play as USSR\.")

# Fallback: any line starting with "SETUP: : " (e.g. bidding format:
# "SETUP: : brown_town bids 0 Influence for USSR")
_PAT_SETUP_HEADER = re.compile(r"^SETUP: :")

# Bidding game: player names appear on standalone lines after the bid lines.
# "brown_town will play as USSR."  (no SETUP: prefix)
_PAT_SETUP_USSR_STANDALONE = re.compile(r"^(.+) will play as USSR\.$")

# "Logarius will play as USA."
_PAT_SETUP_US = re.compile(r"^(.+) will play as USA\.$")

# "Handicap influence: US +2"  or  "Additional Influence from bidding: USSR +2"
_PAT_HANDICAP = re.compile(
    r"^(?:Handicap influence|Additional Influence from bidding): (USSR|US) ([+-]\d+)$"
)

# Informational setup lines (matched → skip, not unknown)
_PAT_SETUP_INFO = re.compile(
    r"^(?:"
    r"Scenario:|"
    r"Time per Player:|"
    r"Optional Cards Added$|"
    r".+ bids \d+ Influence for (?:USSR|US)$"
    r")"
)

# ── Turn / phase headers ──────────────────────────────────────────────────────

# "Turn 1, Headline Phase: Vietnam Revolts* & Marshall Plan*: DEFCON improves to 3"
# Group 1=turn, 2=card1, 3=card2, 4=optional inline text (may be empty string)
# Note: space after the final colon is optional because strip() removes trailing whitespace.
_PAT_HEADLINE_PHASE = re.compile(
    r"^Turn (\d+), Headline Phase: (.+?) & (.+?): ?(.*)$"
)

# Fallback for a single-card headline (one player passed or card not shown).
# "Turn 8, Headline Phase: Grain Sales To Soviets: DEFCON improves to 3"
# Group 1=turn, 2=card-name, 3=optional inline text (may be empty).
_PAT_HEADLINE_PHASE_SINGLE = re.compile(
    r"^Turn (\d+), Headline Phase: (.+?): ?(.*)$"
)

# "Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):"
# Group 1=turn, 2=USSR|US, 3=ar, 4=card-name (may be empty for pass lines), 5=action-text
# Use [^:]* (not .+?) for card-name so that empty-card lines like "Turn 2, US AR6: : "
# still match (the card field is empty between the two colons).
_PAT_ACTION_ROUND = re.compile(
    r"^Turn (\d+), (USSR|US) AR(\d+): ([^:]*): ?(.*)$"
)

# "Turn 5, Cleanup: : Vietnam Revolts* is no longer in play."  (canonical double-colon form)
# "Turn 5, Cleanup: USSR gains 2 VP. Score is even."           (single-colon form seen in some logs)
# "Turn 9, Cleanup"                                            (bare form, no colon)
# Group 1=turn, 2=inline text (may be empty / missing).
_PAT_CLEANUP = re.compile(r"^Turn (\d+), Cleanup(?:: ?:? ?(.*))?$")

# Game-end score line: ": : US gains 26 VP. Score is US 38."
# Space after the second colon is optional (strip() removes trailing whitespace from
# empty game-end lines like ": : " which becomes ": :" after stripping).
_PAT_GAME_END = re.compile(r"^: : ?(.*)$")

# ── Influence changes ─────────────────────────────────────────────────────────

# "USSR +4 in Poland [0][4]"  or  "US -2 in Iran [0][0]"
# Group 1=USSR|US, 2=signed-delta, 3=country-name, 4=us-inf, 5=ussr-inf
_PAT_INFLUENCE = re.compile(
    r"^(USSR|US) ([+-]\d+) in (.+?) \[(\d+)\]\[(\d+)\]$"
)

# ── State changes ─────────────────────────────────────────────────────────────

# "DEFCON degrades to 4"  /  "DEFCON improves to 3"
_PAT_DEFCON = re.compile(r"^DEFCON (degrades|improves) to (\d)$")

# "USSR gains 6 VP. Score is USSR 8."   /  "US gains 1 VP. Score is USSR 1."
# We extract the delta from the gaining side, not the absolute score.
_PAT_VP_GAIN = re.compile(r"^(USSR|US) gains (\d+) VP\. Score is ")

# "USSR Military Ops to 3"
_PAT_MILOPS = re.compile(r"^(USSR|US) Military Ops to (\d+)$")

# "USSR advances to 2 in the Space Race."
_PAT_SPACE_ADVANCE = re.compile(r"^(USSR|US) advances to (\d+) in the Space Race\.$")

# ── Headline sub-lines ────────────────────────────────────────────────────────

_PAT_USSR_HEADLINES = re.compile(r"^USSR Headlines (.+)$")
_PAT_US_HEADLINES = re.compile(r"^US Headlines (.+)$")

# ── Card state changes ────────────────────────────────────────────────────────

# "Marshall Plan* is now in play."
_PAT_IN_PLAY = re.compile(r"^(.+) is now in play\.$")

# "Vietnam Revolts* is no longer in play."
_PAT_EXPIRED = re.compile(r"^(.+) is no longer in play\.$")

# ── Card movement events ─────────────────────────────────────────────────────

# "USSR discards Containment*"  /  "US discards Decolonization"
_PAT_DISCARD_LINE = re.compile(r"^(USSR|US) discards (.+)$")

# "USSR reveals De Gaulle Leads France* from hand"  (CIA Created variant)
_PAT_REVEAL_FROM_HAND = re.compile(r"^(USSR|US) reveals (.+?) from hand$")

# "USSR reveals De Gaulle Leads France*"
_PAT_REVEAL = re.compile(r"^(USSR|US) reveals (.+)$")

# "US returns Central America Scoring to USSR"  (Grain Sales)
_PAT_TRANSFER = re.compile(r"^(USSR|US) returns (.+?) to (USSR|US)$")

# "USSR plays Bear Trap*"  (UN Intervention uses opponent card; phasing player picks it)
# The card belongs to the OPPONENT of the named side → FORCED_DISCARD from opponent's hand
_PAT_PLAYS_OPPONENT_CARD = re.compile(r"^(USSR|US) plays (.+)$")

# ── Reshuffle ─────────────────────────────────────────────────────────────────

_PAT_RESHUFFLE = re.compile(r"^\*RESHUFFLE\*$")

# ── Nixon Plays The China Card event ─────────────────────────────────────────
# When Nixon (card_id=72) fires as an EVENT, the China Card passes to the US
# face-up. There is no separate CHINA_CARD_PASS line in the log; it must be
# inferred from the event announcement.
_PAT_NIXON_EVENT = re.compile(r"^Event: Nixon Plays [Tt]he China Card\*?$")

# ── Informational sub-lines (recognized but produce no event) ─────────────────

# One compiled pattern to match all informational lines in a single pass.
_PAT_INFO = re.compile(
    r"^(?:"
    r"Target: .+|"                               # coup / realignment target
    r"(?:SUCCESS|FAILURE): \d+ \[|"             # coup result
    r"Die roll: \d+ --|"                         # space race roll
    r"War in .+|"                                # war announcement
    r"(?:VICTORY|DEFEAT): \d+|"                 # war result
    r"Trap Roll: \d+ [<>]=? \d+ --|"             # Bear/Quagmire trap roll (both <= and >)
    r"(?:Place Influence|Coup|Realignment|Space Race) \(\d+ Ops\):|"  # action announce
    r"Event: .+|"                                # event fires (just an announce)
    r"(?:USSR|US) has no cards to reveal$|"
    r"(?:USSR|US) has no cards to discard$|"
    r"(?:USSR|US) chooses to (?:participate|boycott)|"
    r"(?:USSR|US) chooses .+|"                          # Chernobyl / card region choice
    r"(?:USSR|US) rolls \d+|"                   # realignment dice
    r"No VP awarded\.|"                          # 0-VP line
    r"Score is (?:USSR|US) \d+\.$|"             # standalone score line
    r"Score is even\.$|"
    r"(?:USSR|US) wins|"
    r"Game over"
    r")"
)


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
    all_events: list[ReplayEvent] = []
    unknown_lines: list[tuple[int, str]] = []
    ctx = _ParseContext(game_id=game_id)
    lines = text.splitlines()

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if not stripped:
            continue

        result = _parse_line(stripped, lineno, ctx)

        if result is None:
            # Unrecognized line → UNKNOWN event, tracked in unknown_lines
            unknown_lines.append((lineno, raw))
            all_events.append(
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
            # result is a list of 0 or more events
            all_events.extend(result)

    return ParseResult(
        game_id=ctx.game_id or game_id,
        events=all_events,
        unknown_lines=unknown_lines,
        total_lines=sum(1 for ln in lines if ln.strip()),
    )


def iter_events(text: str, game_id: str = "") -> Iterator[ReplayEvent]:
    """Streaming event iterator (wraps parse_replay for convenience)."""
    yield from parse_replay(text, game_id).events


# ---------------------------------------------------------------------------
# Core line dispatcher
# ---------------------------------------------------------------------------


def _parse_line(
    line: str, lineno: int, ctx: _ParseContext
) -> list[ReplayEvent] | None:
    """Attempt to parse a single non-empty stripped line.

    Returns:
        None              → line is unrecognized (caller adds UNKNOWN event).
        []                → line is recognized but produces no events (skip).
        [event, ...]      → one or more events from this line.

    Updates ctx in-place for structural lines (turn, AR, phasing, flags).
    """
    # ── SETUP block ───────────────────────────────────────────────────────────

    if m := _PAT_SETUP_USSR.match(line):
        ctx.ussr_player = m.group(1)
        ctx.in_setup = True
        return [_ev(EventKind.GAME_START, ctx, lineno, raw_line=line)]

    # Bidding format: "SETUP: : brown_town bids 0 Influence for USSR"
    if _PAT_SETUP_HEADER.match(line):
        ctx.in_setup = True
        return [_ev(EventKind.GAME_START, ctx, lineno, raw_line=line)]

    if ctx.in_setup:
        if m := _PAT_SETUP_US.match(line):
            ctx.us_player = m.group(1)
            return []  # already emitted GAME_START; this is supplemental

        # Bidding games: player names appear on their own lines after bid lines
        if m := _PAT_SETUP_USSR_STANDALONE.match(line):
            ctx.ussr_player = m.group(1)
            return []

        if m := _PAT_HANDICAP.match(line):
            side = Side.USSR if m.group(1) == "USSR" else Side.US
            amount = int(m.group(2))
            return [_ev(EventKind.HANDICAP, ctx, lineno, raw_line=line,
                        phasing_override=side, amount=amount)]

        if _PAT_SETUP_INFO.match(line):
            return []

    # ── Turn / phase headers (always checked; end setup mode) ─────────────────

    if m := _PAT_HEADLINE_PHASE.match(line):
        ctx.turn = int(m.group(1))
        ctx.ar = 0
        ctx.in_setup = False
        ctx.in_cleanup = False
        events: list[ReplayEvent] = [
            _ev(EventKind.HEADLINE_PHASE_START, ctx, lineno, raw_line=line)
        ]
        # Parse optional inline text after the second colon (may be empty string)
        inline = (m.group(4) or "").strip()
        if inline:
            events.extend(_parse_subline(inline, lineno, ctx, line) or [])
        return events

    if m := _PAT_HEADLINE_PHASE_SINGLE.match(line):
        ctx.turn = int(m.group(1))
        ctx.ar = 0
        ctx.in_setup = False
        ctx.in_cleanup = False
        events = [_ev(EventKind.HEADLINE_PHASE_START, ctx, lineno, raw_line=line)]
        inline = (m.group(3) or "").strip()
        if inline:
            events.extend(_parse_subline(inline, lineno, ctx, line) or [])
        return events

    if m := _PAT_ACTION_ROUND.match(line):
        ctx.turn = int(m.group(1))
        ctx.phasing = Side.USSR if m.group(2) == "USSR" else Side.US
        ctx.ar = int(m.group(3))
        card_name = m.group(4).strip()
        ctx.in_setup = False
        ctx.in_cleanup = False
        events = [_ev(EventKind.ACTION_ROUND_START, ctx, lineno, raw_line=line,
                      card_name=card_name or None)]
        # Emit PLAY when a card is identified (card_id=None until resolver pass).
        # This marks the action as a decision point for the smoother.
        if card_name:
            events.append(_ev(EventKind.PLAY, ctx, lineno, raw_line=line,
                              card_name=card_name))
        # Parse inline action text (e.g. "USSR discards CARD", "CARD is no longer in play.")
        action_text = m.group(5).strip()
        if action_text:
            events.extend(_parse_subline(action_text, lineno, ctx, line) or [])
        return events

    if m := _PAT_CLEANUP.match(line):
        ctx.turn = int(m.group(1))
        ctx.in_cleanup = True
        ctx.in_setup = False
        events = [_ev(EventKind.TURN_END, ctx, lineno, raw_line=line)]
        inline = (m.group(2) or "").strip()
        if inline:
            events.extend(_parse_subline(inline, lineno, ctx, line) or [])
        return events

    if m := _PAT_GAME_END.match(line):
        inline = m.group(1).strip()
        events = [_ev(EventKind.GAME_END, ctx, lineno, raw_line=line)]
        if inline:
            events.extend(_parse_subline(inline, lineno, ctx, line) or [])
        return events

    # ── Sub-lines and standalone lines ────────────────────────────────────────

    return _parse_subline(line, lineno, ctx, line)


def _parse_subline(
    text: str,
    lineno: int,
    ctx: _ParseContext,
    raw_line: str,
) -> list[ReplayEvent] | None:
    """Parse a sub-line or inline text fragment into events.

    Returns None if text is unrecognized (caller decides how to handle).
    Returns [] if recognized but informational (no events).
    """
    # ── Nixon event: China Card passes to US face-up ─────────────────────────
    # Must be checked before _PAT_INFO, which would swallow "Event: .+" lines.

    if _PAT_NIXON_EVENT.match(text):
        return [_ev(EventKind.CHINA_CARD_PASS, ctx, lineno, raw_line=raw_line,
                    phasing_override=Side.US)]

    # ── Informational: no event needed ────────────────────────────────────────

    if _PAT_INFO.match(text):
        return []

    # ── Reshuffle ─────────────────────────────────────────────────────────────

    if _PAT_RESHUFFLE.match(text):
        return [_ev(EventKind.RESHUFFLE, ctx, lineno, raw_line=raw_line)]

    # ── Headline sub-lines ────────────────────────────────────────────────────

    if m := _PAT_USSR_HEADLINES.match(text):
        return [_ev(
            EventKind.HEADLINE, ctx, lineno, raw_line=raw_line,
            phasing_override=Side.USSR,
            ar_override=0,
            card_name=m.group(1).strip(),
        )]

    if m := _PAT_US_HEADLINES.match(text):
        return [_ev(
            EventKind.HEADLINE, ctx, lineno, raw_line=raw_line,
            phasing_override=Side.US,
            ar_override=0,
            card_name=m.group(1).strip(),
        )]

    # ── Influence changes ─────────────────────────────────────────────────────

    if m := _PAT_INFLUENCE.match(text):
        side = Side.USSR if m.group(1) == "USSR" else Side.US
        delta = int(m.group(2))
        kind = EventKind.PLACE_INFLUENCE if delta > 0 else EventKind.REMOVE_INFLUENCE
        us_b = int(m.group(4))
        ussr_b = int(m.group(5))
        return [_ev(
            kind, ctx, lineno, raw_line=raw_line,
            phasing_override=side,
            amount=abs(delta),
            country_name=m.group(3).strip(),
            us_bracket=us_b,
            ussr_bracket=ussr_b,
        )]

    # ── DEFCON ────────────────────────────────────────────────────────────────

    if m := _PAT_DEFCON.match(text):
        return [_ev(
            EventKind.DEFCON_CHANGE, ctx, lineno, raw_line=raw_line,
            amount=int(m.group(2)),
        )]

    # ── VP ────────────────────────────────────────────────────────────────────

    if m := _PAT_VP_GAIN.match(text):
        gaining_side = m.group(1)
        amount = int(m.group(2))
        # Convention: positive VP = USSR advantage; negative = US advantage
        delta = amount if gaining_side == "USSR" else -amount
        return [_ev(EventKind.VP_CHANGE, ctx, lineno, raw_line=raw_line, amount=delta)]

    # ── MilOps ───────────────────────────────────────────────────────────────

    if m := _PAT_MILOPS.match(text):
        side = Side.USSR if m.group(1) == "USSR" else Side.US
        return [_ev(
            EventKind.MILOPS_CHANGE, ctx, lineno, raw_line=raw_line,
            phasing_override=side,
            amount=int(m.group(2)),
        )]

    # ── Space advance ─────────────────────────────────────────────────────────

    if m := _PAT_SPACE_ADVANCE.match(text):
        side = Side.USSR if m.group(1) == "USSR" else Side.US
        return [_ev(
            EventKind.SPACE_RACE, ctx, lineno, raw_line=raw_line,
            phasing_override=side,
            amount=int(m.group(2)),
        )]

    # ── Card in play / expired ────────────────────────────────────────────────

    if m := _PAT_IN_PLAY.match(text):
        return [_ev(EventKind.CARD_IN_PLAY, ctx, lineno, raw_line=raw_line,
                    card_name=m.group(1).strip())]

    if m := _PAT_EXPIRED.match(text):
        return [_ev(EventKind.CARD_EXPIRED, ctx, lineno, raw_line=raw_line,
                    card_name=m.group(1).strip())]

    # ── Discard ───────────────────────────────────────────────────────────────

    if m := _PAT_DISCARD_LINE.match(text):
        side = Side.USSR if m.group(1) == "USSR" else Side.US
        return [_ev(
            EventKind.FORCED_DISCARD, ctx, lineno, raw_line=raw_line,
            phasing_override=side,
            card_name=m.group(2).strip(),
        )]

    # ── Reveal (check from-hand variant first) ────────────────────────────────

    if m := _PAT_REVEAL_FROM_HAND.match(text):
        side = Side.USSR if m.group(1) == "USSR" else Side.US
        return [_ev(
            EventKind.REVEAL_HAND, ctx, lineno, raw_line=raw_line,
            phasing_override=side,
            card_name=m.group(2).strip(),
        )]

    if m := _PAT_REVEAL.match(text):
        side = Side.USSR if m.group(1) == "USSR" else Side.US
        return [_ev(
            EventKind.REVEAL_HAND, ctx, lineno, raw_line=raw_line,
            phasing_override=side,
            card_name=m.group(2).strip(),
        )]

    # ── Transfer (Grain Sales: "US returns CARD to USSR") ─────────────────────

    if m := _PAT_TRANSFER.match(text):
        sender = Side.USSR if m.group(1) == "USSR" else Side.US
        return [_ev(
            EventKind.TRANSFER, ctx, lineno, raw_line=raw_line,
            phasing_override=sender,
            card_name=m.group(2).strip(),
        )]

    # ── UN Intervention: "USSR plays Bear Trap*" ──────────────────────────────
    # The named side is the ACTING player; the card was in the OPPONENT's hand.

    if m := _PAT_PLAYS_OPPONENT_CARD.match(text):
        acting = Side.USSR if m.group(1) == "USSR" else Side.US
        opponent = Side.US if acting == Side.USSR else Side.USSR
        return [_ev(
            EventKind.FORCED_DISCARD, ctx, lineno, raw_line=raw_line,
            phasing_override=opponent,
            card_name=m.group(2).strip(),
        )]

    # ── Setup influence ───────────────────────────────────────────────────────
    # This is already covered by _PAT_INFLUENCE above (same format), so this
    # branch is not needed separately.

    return None  # unrecognized


# ---------------------------------------------------------------------------
# Event builder helper
# ---------------------------------------------------------------------------


def _ev(
    kind: EventKind,
    ctx: _ParseContext,
    lineno: int,
    *,
    raw_line: str = "",
    phasing_override: Side | None = None,
    ar_override: int | None = None,
    amount: int | None = None,
    card_id: int | None = None,
    country_id: int | None = None,
    aux_card_ids: tuple[int, ...] = (),
    aux_country_ids: tuple[int, ...] = (),
    card_name: str | None = None,
    country_name: str | None = None,
    us_bracket: int | None = None,
    ussr_bracket: int | None = None,
) -> ReplayEvent:
    """Build a ReplayEvent from current context plus optional overrides."""
    return ReplayEvent(
        kind=kind,
        turn=ctx.turn,
        ar=ar_override if ar_override is not None else ctx.ar,
        phasing=phasing_override if phasing_override is not None else ctx.phasing,
        card_id=card_id,
        country_id=country_id,
        amount=amount,
        aux_card_ids=aux_card_ids,
        aux_country_ids=aux_country_ids,
        raw_line=raw_line,
        line_number=lineno,
        card_name=card_name,
        country_name=country_name,
        us_bracket=us_bracket,
        ussr_bracket=ussr_bracket,
    )
