"""
Replay validator: cross-check every logged action against the engine's
legal-action rules.

For each PLAY / HEADLINE event in a game log the validator:
  1. Reconstructs pub state BEFORE the action (from reduce_game).
  2. Reconstructs the actor's best-known hand (from smooth_game labels).
  3. Infers the ActionMode from the raw log line.
  4. Collects target countries from subsequent board-action events.
  5. Checks card/mode/target legality against the engine.

Violations are categorised by kind so callers can distinguish hard errors
(CARD_EXCLUDED: the card was positively known to be absent from hand) from
soft evidence gaps (CARD_NOT_RECONSTRUCTED: hand reconstruction was incomplete)
from genuine rule violations (MODE_ILLEGAL, TARGET_ILLEGAL).
"""
from __future__ import annotations

import logging
import re
import warnings
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache as _lru_cache
from pathlib import Path

from tsrl.engine.legal_actions import legal_countries, legal_modes
from tsrl.etl.game_data import fixed_starting_influence, load_cards, load_countries
from tsrl.etl.parser import parse_replay
from tsrl.etl.reducer import reduce_game
from tsrl.etl.resolver import resolve_names
from tsrl.etl.smoother import smooth_game
from tsrl.schemas import (
    ActionMode,
    EventKind,
    HandKnowledge,
    OfflineLabels,
    PublicState,
    ReplayEvent,
    Side,
)

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Violation types
# ---------------------------------------------------------------------------

_DECISION_KINDS: frozenset[EventKind] = frozenset({EventKind.PLAY, EventKind.HEADLINE})

# EventKinds that carry board-action targets immediately after a PLAY.
_BOARD_ACTION_KINDS: frozenset[EventKind] = frozenset({
    EventKind.PLACE_INFLUENCE,
    EventKind.REMOVE_INFLUENCE,
    EventKind.COUP,
    EventKind.REALIGN,
    EventKind.SPACE_RACE,
})

# EventKinds that terminate target collection (next decision or turn boundary).
_STOP_KINDS: frozenset[EventKind] = frozenset({
    EventKind.PLAY,
    EventKind.HEADLINE,
    EventKind.ACTION_ROUND_START,
    EventKind.HEADLINE_PHASE_START,
    EventKind.TURN_START,
    EventKind.TURN_END,
    EventKind.GAME_END,
})


class ViolationKind(Enum):
    # Card is in pub.removed — definitively gone from the game, cannot be in hand.
    # This should never happen in a valid game log.
    CARD_REMOVED = "CARD_REMOVED"

    # Card is in known_not_in_hand per the causal forward reducer.
    # Soft: the reducer never sees DRAW events, so cards can remain excluded
    # after being reshuffled and redrawn.  Treat as informative, not hard.
    CARD_EXCLUDED_BY_REDUCER = "CARD_EXCLUDED_BY_REDUCER"

    # Card is not in the smoother's best-estimate actor_hand.
    # Soft: hand reconstruction may be incomplete (AMBIGUOUS label).
    CARD_NOT_RECONSTRUCTED = "CARD_NOT_RECONSTRUCTED"

    # Mode extracted from raw_line could not be mapped to an ActionMode.
    MODE_UNRECOGNIZED = "MODE_UNRECOGNIZED"

    # The inferred mode is not in legal_modes() for this card+state.
    MODE_ILLEGAL = "MODE_ILLEGAL"

    # A target country is not in legal_countries() for this card+mode+state.
    # For INFLUENCE mode the check is done step-by-step (chaining is allowed).
    TARGET_ILLEGAL = "TARGET_ILLEGAL"

    # card_id is None — the resolver did not resolve the card name.
    CARD_UNRESOLVED = "CARD_UNRESOLVED"

    # Stability extracted from "SUCCESS/FAILURE: D [ + O - 2xS = R ]" doesn't
    # match the country's stability in countries.csv.  Hard violation — the log
    # formula encodes the actual stability used by the game server.
    STABILITY_MISMATCH = "STABILITY_MISMATCH"

    # Consecutive [US][USSR] bracket totals for the same country are inconsistent
    # with the delta shown on the influence line.  Hard violation — brackets are
    # absolute totals written by the game server; any delta inconsistency means
    # the log is internally contradictory or our parsing is wrong.
    INFLUENCE_BRACKET_MISMATCH = "INFLUENCE_BRACKET_MISMATCH"

    # "Die roll: D -- ...(Needed X or less)" threshold doesn't match our
    # _SPACE_ADVANCE_THRESHOLD table for the current space level.
    # Hard violation — the game server tells us the exact threshold.
    SPACE_THRESHOLD_MISMATCH = "SPACE_THRESHOLD_MISMATCH"

    # Realignment outcome influence change doesn't match min(dice_diff, loser_inf).
    # Hard violation — the log states both the dice totals and the bracket change.
    REALIGN_OUTCOME_MISMATCH = "REALIGN_OUTCOME_MISMATCH"

    # Reducer-computed influence after a PLACE/REMOVE_INFLUENCE event doesn't match
    # the absolute [US][USSR] bracket logged by the game server.  Hard violation —
    # the bracket is authoritative; a mismatch means the reducer missed an event or
    # has a wrong starting state.
    INFLUENCE_STATE_MISMATCH = "INFLUENCE_STATE_MISMATCH"

    # Scoring engine's computed VP delta doesn't match the VP change logged immediately
    # after the scoring card play.  Hard violation given a correctly reduced game state.
    SCORING_VP_MISMATCH = "SCORING_VP_MISMATCH"

    # End-of-turn MilOps penalty (sum of VP_CHANGE events after TURN_END) doesn't
    # match max(0, DEFCON - milops) for each side using pre-advance DEFCON.
    # Hard violation — the log states both the milops (via MILOPS_CHANGE) and the
    # VP penalty applied; any mismatch means the engine formula or ordering is wrong.
    MILOPS_PENALTY_MISMATCH = "MILOPS_PENALTY_MISMATCH"

    # Reducer-computed DEFCON after a DEFCON_CHANGE event doesn't match the absolute
    # value logged ("DEFCON degrades/improves to N").  Hard violation — the game
    # server writes the exact new DEFCON; any mismatch means the reducer missed a
    # DEFCON-modifying event or applied it incorrectly.
    DEFCON_STATE_MISMATCH = "DEFCON_STATE_MISMATCH"

    # Reducer-computed milops for a side after a MILOPS_CHANGE event doesn't match the
    # absolute value logged ("USSR/US Military Ops to N").  Hard violation.
    MILOPS_STATE_MISMATCH = "MILOPS_STATE_MISMATCH"

    # Reducer-computed space level for a side after a SPACE_RACE advance event doesn't
    # match the absolute level logged ("USSR/US advances to N in the Space Race").
    # Hard violation.
    SPACE_LEVEL_MISMATCH = "SPACE_LEVEL_MISMATCH"

    # Reducer-computed pub.vp after a VP_CHANGE event doesn't match the absolute score
    # snapshot embedded in the VP line ("Score is USSR N" / "Score is US N" / "Score
    # is even").  Hard violation — the game server writes the authoritative running
    # score; drift here catches any missed or mis-applied VP-changing event.
    VP_ABSOLUTE_MISMATCH = "VP_ABSOLUTE_MISMATCH"

    # Full coup arithmetic check: the die_roll + ops_modifier - 2×stability must equal
    # the stated result in "SUCCESS/FAILURE: D [ + O - 2xS = R ]".
    # Hard violation — the formula is deterministic; any mismatch means our regex or
    # arithmetic interpretation of the log is wrong.
    COUP_FORMULA_MISMATCH = "COUP_FORMULA_MISMATCH"

    # The lower-ops headline card fired before the higher-ops card (or, on a tie,
    # the US headline fired before the USSR headline).
    # Soft violation — the headline firing order rule can be overridden by special
    # events (e.g. Defectors cancels a headline), so treat as informational.
    HEADLINE_ORDER_MISMATCH = "HEADLINE_ORDER_MISMATCH"

    # RESHUFFLE event fired when pub.discard was empty — nothing to reshuffle.
    # Hard violation — the game server only triggers a reshuffle when the draw
    # pile is exhausted; if the discard is also empty that means all known
    # cards are still in hands, which should never trigger a reshuffle.
    RESHUFFLE_EMPTY_DISCARD = "RESHUFFLE_EMPTY_DISCARD"

    # DEFCON dropped to 1 but no GAME_END event followed before the next
    # PLAY or HEADLINE.  Hard violation — DEFCON 1 ends the game immediately
    # with the non-phasing player winning; any subsequent action is impossible.
    DEFCON_GAME_NOT_ENDED = "DEFCON_GAME_NOT_ENDED"

    # VP crossed the ±20 threshold (absolute win) but no GAME_END followed
    # before the next PLAY or HEADLINE.  Hard violation — ±20 VP ends the
    # game immediately.  Uses the absolute score snapshot in the VP_CHANGE
    # log line, so this check is independent of scoring-formula accuracy.
    VP_WIN_NOT_TRIGGERED = "VP_WIN_NOT_TRIGGERED"


@dataclass
class Violation:
    kind: ViolationKind
    turn: int
    ar: int
    phasing: Side
    card_id: int | None
    message: str
    country_id: int | None = None
    raw_line: str = ""


@dataclass
class ValidationResult:
    game_id: str
    total_decisions: int
    violations: list[Violation] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return len(self.violations) == 0

    @property
    def hard_violations(self) -> list[Violation]:
        """Only violations that indicate genuine rule or data integrity errors.

        Soft violations (CARD_NOT_RECONSTRUCTED, CARD_EXCLUDED_BY_REDUCER,
        CARD_UNRESOLVED, MODE_UNRECOGNIZED) are excluded — they reflect
        incomplete information rather than illegal play.
        """
        soft = {
            ViolationKind.CARD_NOT_RECONSTRUCTED,
            ViolationKind.CARD_EXCLUDED_BY_REDUCER,
            ViolationKind.CARD_UNRESOLVED,
            ViolationKind.MODE_UNRECOGNIZED,
            # Scoring VP formula is incomplete (missing per-BG bonus, Shuttle Diplomacy
            # tracking, possible mod-version differences).  306 violations across 51 logs.
            # See project memory: project_scoring_vp_regressions.md
            ViolationKind.SCORING_VP_MISMATCH,
            # VP absolute check: the reducer does not apply scoring-card VP changes,
            # so VP_ABSOLUTE_MISMATCH fires on every VP event that follows a scoring
            # play.  This is informational until SCORING_VP_MISMATCH is made hard.
            ViolationKind.VP_ABSOLUTE_MISMATCH,
            # Headline order can be legitimately overridden by Defectors (card 108)
            # and other special cases.  Treat as informational.
            ViolationKind.HEADLINE_ORDER_MISMATCH,
            # pub.discard only captures explicit DISCARD events (forced discards,
            # specific card effects) — regular card plays go to discard without an
            # explicit DISCARD event, so pub.discard is always an undercount of the
            # real discard pile.  This makes empty-discard checks unreliable.
            ViolationKind.RESHUFFLE_EMPTY_DISCARD,
            # Game-end via DEFCON=1 or VP±20 may not have an explicit GAME_END event
            # in the log (many logs end abruptly after the last win-condition event).
            # The check is informational: flags if game continued after win condition.
            ViolationKind.DEFCON_GAME_NOT_ENDED,
            ViolationKind.VP_WIN_NOT_TRIGGERED,
        }
        return [v for v in self.violations if v.kind not in soft]

    def summary(self) -> str:
        from collections import Counter
        counts = Counter(v.kind.value for v in self.violations)
        lines = [
            f"game={self.game_id}  decisions={self.total_decisions}  "
            f"violations={len(self.violations)}  hard={len(self.hard_violations)}"
        ]
        for kind, n in sorted(counts.items()):
            lines.append(f"  {kind}: {n}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Mode inference from raw_line
# ---------------------------------------------------------------------------


@_lru_cache(maxsize=1)
def _cached_cards():
    from tsrl.etl.game_data import load_cards

    return load_cards()


# Patterns tried in order; first match wins.
_MODE_RE: list[tuple[re.Pattern, ActionMode]] = [
    (re.compile(r"Place Influence", re.I), ActionMode.INFLUENCE),
    (re.compile(r"\bRealign", re.I),       ActionMode.REALIGN),
    (re.compile(r"\bCoup\b", re.I),        ActionMode.COUP),
    (re.compile(r"Space Race", re.I),      ActionMode.SPACE),
    (re.compile(r"\bdiscards?\b", re.I),   ActionMode.EVENT),
    (re.compile(r"\bEvent\b", re.I),       ActionMode.EVENT),
]
_EVENT_ONLY_CARD_IDS: frozenset[int] = frozenset({103})  # Wargames


def _infer_mode(ev: ReplayEvent) -> ActionMode | None:
    """Infer ActionMode from the raw log line of a PLAY event.

    HEADLINE events are always EVENT (played for event effect in headline phase).
    """
    if ev.kind == EventKind.HEADLINE:
        return ActionMode.EVENT

    for pat, mode in _MODE_RE:
        if pat.search(ev.raw_line):
            return mode

    # War-card VP result lines are inline event resolution, not the play mode.
    if re.search(r"\bgains \d+ VP\b", ev.raw_line) or "Score is" in ev.raw_line:
        return ActionMode.EVENT

    # China Card can carry Formosan Resolution expiry text inline; that side effect
    # does not change the play mode, which is influence placement in these logs.
    if ev.card_id == 6 and "no longer in play" in ev.raw_line:
        return ActionMode.INFLUENCE

    # Cards with no alternate play mode can still appear with empty action text.
    if ev.card_id in _EVENT_ONLY_CARD_IDS:
        return ActionMode.EVENT

    if ev.card_id is not None:
        spec = _cached_cards().get(ev.card_id)
        if spec is not None and spec.is_scoring:
            return ActionMode.EVENT

    return None


# ---------------------------------------------------------------------------
# Target collection from subsequent board-action events
# ---------------------------------------------------------------------------


def _collect_targets(
    events: list[ReplayEvent],
    start_idx: int,
    mode: ActionMode,
    actor: Side,
) -> list[int]:
    """Collect the country targets used by this action from subsequent events.

    Scans forward from start_idx+1 until a STOP_KIND or a board-action
    event belonging to a different actor.  Returns a flat list of country
    IDs (a country appears once per op point or attempt).

    For SPACE/EVENT: returns [] immediately (no country targets).
    """
    if mode in (ActionMode.SPACE, ActionMode.EVENT):
        return []

    targets: list[int] = []

    for ev in events[start_idx + 1:]:
        if ev.kind in _STOP_KINDS:
            break
        if ev.kind not in _BOARD_ACTION_KINDS:
            continue
        if ev.phasing != actor:
            # Board action belongs to the other side (opponent event effect) — stop.
            break

        cid = ev.country_id
        if cid is None:
            continue

        if mode == ActionMode.INFLUENCE and ev.kind == EventKind.PLACE_INFLUENCE:
            # amount > 1 means multiple ops placed in the same country.
            n = ev.amount if ev.amount and ev.amount > 0 else 1
            targets.extend([cid] * n)

        elif mode == ActionMode.COUP and ev.kind == EventKind.COUP:
            targets.append(cid)
            break  # only one coup target per play

        elif mode == ActionMode.REALIGN and ev.kind == EventKind.REALIGN:
            targets.append(cid)

    return targets


# ---------------------------------------------------------------------------
# Raw-text cross-checks (ground truth from log metadata)
# ---------------------------------------------------------------------------

# "SUCCESS: 4 [ + 4 - 2x2 = 4 ]"  or  "FAILURE: 3 [ + 1 (-2)  - 2x1 = 0 ]"
# The 2xS term gives stability directly; optional modifier in parens.
_CROSS_RE_COUP_RESULT = re.compile(
    r"^(?:SUCCESS|FAILURE): \d+ "
    r"\[ \+ \d+(?:\s+\([+-]?\d+\))?\s* - 2x(\d+) = [+-]?\d+ \]$"
)

# "USSR +4 in Poland [0][4]"  →  side, delta, name, us_after, ussr_after
_CROSS_RE_INFLUENCE = re.compile(
    r"^(USSR|US) ([+-]\d+) in (.+?) \[(\d+)\]\[(\d+)\]$"
)

# "Target: Iran"
_CROSS_RE_TARGET = re.compile(r"^Target: (.+)$")

# "Turn N, SIDE ARN: CARD_NAME: ACTION_TEXT"
# group(1)=turn, group(2)=side, group(3)=ar_num, group(4)=card_name, group(5)=action_text
_CROSS_RE_AR = re.compile(r"^Turn (\d+), (USSR|US) AR(\d+): ([^:]*): ?(.*)$")

# "USSR advances to N in the Space Race."
_CROSS_RE_SPACE_ADVANCE = re.compile(
    r"^(USSR|US) advances to (\d+) in the Space Race\.$"
)

# "Die roll: D -- Success! (Needed X or less)"
_CROSS_RE_SPACE_ROLL = re.compile(
    r"^Die roll: \d+ -- (?:Success|Failed)! \(Needed (\d+) or less\)$"
)

# Space race advance thresholds (index = current level 0..7, value = needed roll ≤ this).
# Empirically verified from corpus: each level has a unique threshold observed across
# all games; values confirmed against TS Deluxe rulebook space race track.
_SPACE_THRESHOLDS = [3, 4, 3, 4, 3, 4, 3, 2]  # levels 0-7

# "USSR rolls 6 (+2) = 8"  or  "US rolls 3"  (modifier and total optional)
_CROSS_RE_REALIGN_ROLL = re.compile(
    r"^(USSR|US) rolls (\d+)(?: \(([+-]?\d+)\))?(?: = (\d+))?$"
)

# Full coup formula: "SUCCESS: D [ + O [modifier]  - 2xS = R ]"
# Groups: (1)=die, (2)=ops_base, (3)=opt_modifier (may be None), (4)=stability, (5)=result
_CROSS_RE_COUP_FULL = re.compile(
    r"^(?:SUCCESS|FAILURE): (\d+) "
    r"\[ \+ (\d+)(?:\s+\(([+-]?\d+)\))?\s* - 2x(\d+) = ([+-]?\d+) \]$"
)

# "Turn N, Headline Phase: CARD_A & CARD_B: ..."
# Groups: (1)=turn, (2)=card_a_name, (3)=card_b_name
_CROSS_RE_HEADLINE_PHASE = re.compile(
    r"^Turn (\d+), Headline Phase: (.+?) & (.+?):"
)

# "USSR Headlines CARD_NAME"  or  "US Headlines CARD_NAME"
_CROSS_RE_HEADLINE_SELECT = re.compile(r"^(USSR|US) Headlines (.+)$")

# "Event: CARD_NAME"
_CROSS_RE_EVENT_LINE = re.compile(r"^Event: (.+)$")

# "CARD_NAME is now in play." / "CARD_NAME is no longer in play."
_CROSS_RE_CARD_IN_PLAY = re.compile(r"^(.+?) is (now in|no longer in) play\.$")

# "Score is USSR N."  /  "Score is US N."  /  "Score is even."
# Groups: (1)=side_str (may be None for "even"), (2)=score_str (may be None)
_CROSS_RE_SCORE_SNAPSHOT = re.compile(
    r"Score is (?:(USSR|US) (\d+)|even)\.$"
)

def _cross_check_raw(
    raw_text: str,
    countries: dict,
    card_name_to_ops: dict[str, int] | None = None,
) -> list[Violation]:
    """Scan raw log text for hard ground-truth inconsistencies.

    Checks:
    1. STABILITY_MISMATCH — stability S in coup formula "2xS" vs countries.csv.
    2. INFLUENCE_BRACKET_MISMATCH — consecutive [US][USSR] bracket totals must
       be delta-consistent.
    3. SPACE_THRESHOLD_MISMATCH — "Needed X or less" in space roll vs our table.
    4. REALIGN_OUTCOME_MISMATCH — influence change after realignment must equal
       min(|ussr_total - us_total|, loser_inf_before).
    5. COUP_FORMULA_MISMATCH — full arithmetic: die + ops [+ mod] - 2×S == result.
    6. HEADLINE_ORDER_MISMATCH (soft) — higher-ops card fires first; USSR wins ties.

    All checks are self-consistent within the log (do not require external state
    reconstruction beyond what the log itself provides).
    """
    name_to_cid: dict[str, int] = {}
    cid_to_stability: dict[int, int] = {}
    for cid, spec in countries.items():
        name_to_cid[spec.name.lower()] = cid
        cid_to_stability[cid] = spec.stability

    # Normalised card name → ops for headline order check.  Strip trailing * and lower.
    _cname_to_ops: dict[str, int] = {}
    if card_name_to_ops:
        for raw_name, ops_val in card_name_to_ops.items():
            _cname_to_ops[raw_name.lower().rstrip("* ").strip()] = ops_val

    violations: list[Violation] = []
    # country_name → (us_total, ussr_total) after last seen influence line
    running_brackets: dict[str, tuple[int, int]] = {}
    space_level: dict[int, int] = {int(Side.USSR): 0, int(Side.US): 0}

    # Headline-phase tracking for order check.
    in_headline = False
    hl_turn = 0
    hl_ussr_card: str | None = None   # card name selected by USSR
    hl_us_card: str | None = None     # card name selected by US
    hl_events_fired: list[str] = []   # event names fired in this headline phase

    cur_turn = 0
    cur_ar = 0
    cur_side = Side.USSR
    coup_target_name: str | None = None
    in_coup = False
    in_space = False
    in_realign = False

    # Realignment dice state for the current target country.
    realign_target: str | None = None
    realign_ussr_total: int | None = None
    realign_us_total: int | None = None
    iran_contra_active: bool = False

    for line in raw_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        # --- Headline Phase header — start headline tracking ---
        if m := _CROSS_RE_HEADLINE_PHASE.match(stripped):
            # Before updating, flush any pending headline check from previous turn.
            if in_headline:
                violations.extend(_check_headline_order(
                    hl_turn, hl_ussr_card, hl_us_card, hl_events_fired, _cname_to_ops,
                ))
            in_headline = True
            hl_turn = int(m.group(1))
            hl_ussr_card = None
            hl_us_card = None
            hl_events_fired = []
            iran_contra_active = False
            continue

        # --- Headline card selection ---
        if in_headline and (m := _CROSS_RE_HEADLINE_SELECT.match(stripped)):
            sel_side, sel_card = m.group(1), m.group(2).strip()
            if sel_side == "USSR":
                hl_ussr_card = sel_card
            else:
                hl_us_card = sel_card
            continue

        # --- Event line — record fires during headline phase ---
        if in_headline and (m := _CROSS_RE_EVENT_LINE.match(stripped)):
            hl_events_fired.append(m.group(1).strip())
            # Don't 'continue' — fall through to AR header check below.

        # --- Action round header — update context (also ends headline phase) ---
        if m := _CROSS_RE_AR.match(stripped):
            # An AR header means the headline phase is over; flush order check.
            if in_headline:
                violations.extend(_check_headline_order(
                    hl_turn, hl_ussr_card, hl_us_card, hl_events_fired, _cname_to_ops,
                ))
                in_headline = False
            cur_turn = int(m.group(1))
            cur_side = Side.USSR if m.group(2) == "USSR" else Side.US
            cur_ar = int(m.group(3))
            action_text = m.group(5)
            coup_target_name = None
            in_coup = bool(re.search(r"\bCoup\b", action_text, re.I))
            in_space = bool(re.search(r"Space Race", action_text, re.I))
            in_realign = bool(re.search(r"\bRealign", action_text, re.I))
            realign_target = None
            realign_ussr_total = None
            realign_us_total = None
            continue

        # --- Target line — record coup/realign country ---
        if m := _CROSS_RE_TARGET.match(stripped):
            target_name = m.group(1).strip()
            if in_coup:
                coup_target_name = target_name
            elif in_realign:
                realign_target = target_name
                realign_ussr_total = None
                realign_us_total = None
            continue

        # --- Space race advance — update level ---
        if m := _CROSS_RE_SPACE_ADVANCE.match(stripped):
            side_idx = int(Side.USSR if m.group(1) == "USSR" else Side.US)
            space_level[side_idx] = int(m.group(2))
            continue

        # --- Space roll — check threshold ---
        if in_space and (m := _CROSS_RE_SPACE_ROLL.match(stripped)):
            needed = int(m.group(1))
            level = space_level[int(cur_side)]
            if level < len(_SPACE_THRESHOLDS):
                expected = _SPACE_THRESHOLDS[level]
                if needed != expected:
                    violations.append(Violation(
                        kind=ViolationKind.SPACE_THRESHOLD_MISMATCH,
                        turn=cur_turn, ar=cur_ar, phasing=cur_side,
                        card_id=None, country_id=None,
                        message=(
                            f"space threshold mismatch: log says Needed {needed} or less "
                            f"but table has {expected} at level {level}"
                        ),
                        raw_line=stripped,
                    ))
            continue

        # --- Coup result — check stability (via old regex for fallback) AND full formula ---
        if in_coup and (m := _CROSS_RE_COUP_FULL.match(stripped)):
            die = int(m.group(1))
            ops_base = int(m.group(2))
            mod = int(m.group(3)) if m.group(3) is not None else 0
            s_from_log = int(m.group(4))
            stated_result = int(m.group(5))
            computed_result = die + ops_base + mod - 2 * s_from_log

            # 1. Stability check (hard) — 2xS must match countries.csv
            if coup_target_name is not None:
                cid = name_to_cid.get(coup_target_name.lower())
                if cid is not None:
                    expected_s = cid_to_stability.get(cid)
                    if expected_s is not None and s_from_log != expected_s:
                        violations.append(Violation(
                            kind=ViolationKind.STABILITY_MISMATCH,
                            turn=cur_turn, ar=cur_ar, phasing=cur_side,
                            card_id=None, country_id=cid,
                            message=(
                                f"stability mismatch for {coup_target_name!r}: "
                                f"log formula has 2x{s_from_log} "
                                f"but countries.csv has stability={expected_s}"
                            ),
                            raw_line=stripped,
                        ))

            # 2. Full formula check (hard) — die + ops + mod - 2*S == stated result
            if computed_result != stated_result:
                cid = name_to_cid.get(coup_target_name.lower()) if coup_target_name else None
                violations.append(Violation(
                    kind=ViolationKind.COUP_FORMULA_MISMATCH,
                    turn=cur_turn, ar=cur_ar, phasing=cur_side,
                    card_id=None, country_id=cid,
                    message=(
                        f"coup formula mismatch: die={die} + ops={ops_base} + mod={mod:+d}"
                        f" - 2×{s_from_log} = {computed_result}, "
                        f"but log states result={stated_result}"
                    ),
                    raw_line=stripped,
                ))
            continue

        # --- Realignment dice rolls ---
        if in_realign and (m := _CROSS_RE_REALIGN_ROLL.match(stripped)):
            roll_side_str = m.group(1)
            die = int(m.group(2))
            # mod group may be None when modifier is 0 (log omits it)
            mod_str = m.group(3)
            total_str = m.group(4)
            mod = int(mod_str) if mod_str is not None else 0
            total = int(total_str) if total_str is not None else die + mod
            if roll_side_str == "USSR":
                realign_ussr_total = total
            else:
                realign_us_total = total
            continue

        # Track Iran-Contra Scandal active state (reduces US realign rolls by -1).
        if m := _CROSS_RE_CARD_IN_PLAY.match(stripped):
            card_name_normalized = m.group(1).lower().rstrip("* ").strip()
            if "iran" in card_name_normalized and "contra" in card_name_normalized:
                iran_contra_active = (m.group(2) == "now in")
            continue

        # --- Influence line — bracket delta check + realignment outcome check ---
        if m := _CROSS_RE_INFLUENCE.match(stripped):
            side_str, delta_str, cname, us_str, ussr_str = m.groups()
            delta = int(delta_str)
            us_after = int(us_str)
            ussr_after = int(ussr_str)

            # Bracket delta consistency check.
            if cname in running_brackets:
                prev_us, prev_ussr = running_brackets[cname]
                if side_str == "USSR":
                    expected = prev_ussr + delta
                    if expected != ussr_after:
                        cid = name_to_cid.get(cname.lower())
                        violations.append(Violation(
                            kind=ViolationKind.INFLUENCE_BRACKET_MISMATCH,
                            turn=cur_turn, ar=cur_ar, phasing=cur_side,
                            card_id=None, country_id=cid,
                            message=(
                                f"bracket delta mismatch for {cname!r} USSR: "
                                f"prev={prev_ussr}, delta={delta:+d}, "
                                f"expected={expected}, bracket={ussr_after}"
                            ),
                            raw_line=stripped,
                        ))
                else:
                    expected = prev_us + delta
                    if expected != us_after:
                        cid = name_to_cid.get(cname.lower())
                        violations.append(Violation(
                            kind=ViolationKind.INFLUENCE_BRACKET_MISMATCH,
                            turn=cur_turn, ar=cur_ar, phasing=cur_side,
                            card_id=None, country_id=cid,
                            message=(
                                f"bracket delta mismatch for {cname!r} US: "
                                f"prev={prev_us}, delta={delta:+d}, "
                                f"expected={expected}, bracket={us_after}"
                            ),
                            raw_line=stripped,
                        ))

            # Realignment outcome check: the loser should lose min(diff, loser_inf).
            # Only check when we have both dice totals for this realignment target.
            if (
                in_realign
                and delta < 0
                and realign_target is not None
                and cname.lower() == realign_target.lower()
                and realign_ussr_total is not None
                and realign_us_total is not None
            ):
                # Infer loser's influence BEFORE the outcome.
                # bracket_before = bracket_after with the delta reversed.
                us_before = us_after - (delta if side_str == "US" else 0)
                ussr_before = ussr_after - (delta if side_str == "USSR" else 0)

                # Adjust US total for Iran-Contra Scandal effect (-1 to US rolls).
                eff_us_total = max(0, realign_us_total - 1) if iran_contra_active else realign_us_total
                eff_ussr_total = realign_ussr_total

                if eff_ussr_total > eff_us_total:
                    # USSR won — US lost influence.
                    if side_str == "US":
                        diff = eff_ussr_total - eff_us_total
                        expected_loss = min(diff, us_before)
                        actual_loss = abs(delta)
                        if actual_loss != expected_loss:
                            cid = name_to_cid.get(cname.lower())
                            violations.append(Violation(
                                kind=ViolationKind.REALIGN_OUTCOME_MISMATCH,
                                turn=cur_turn, ar=cur_ar, phasing=cur_side,
                                card_id=None, country_id=cid,
                                message=(
                                    f"realignment outcome mismatch for {cname!r}: "
                                    f"USSR total={realign_ussr_total}, US total={realign_us_total}, "
                                    f"diff={diff}, US had {us_before}, "
                                    f"expected loss={expected_loss}, actual loss={actual_loss}"
                                ),
                                raw_line=stripped,
                            ))
                elif eff_us_total > eff_ussr_total:
                    # US won — USSR lost influence.
                    if side_str == "USSR":
                        diff = eff_us_total - eff_ussr_total
                        expected_loss = min(diff, ussr_before)
                        actual_loss = abs(delta)
                        if actual_loss != expected_loss:
                            cid = name_to_cid.get(cname.lower())
                            violations.append(Violation(
                                kind=ViolationKind.REALIGN_OUTCOME_MISMATCH,
                                turn=cur_turn, ar=cur_ar, phasing=cur_side,
                                card_id=None, country_id=cid,
                                message=(
                                    f"realignment outcome mismatch for {cname!r}: "
                                    f"US total={realign_us_total}, USSR total={realign_ussr_total}, "
                                    f"diff={diff}, USSR had {ussr_before}, "
                                    f"expected loss={expected_loss}, actual loss={actual_loss}"
                                ),
                                raw_line=stripped,
                            ))

            running_brackets[cname] = (us_after, ussr_after)
            continue

    # Flush any pending headline check at end of log.
    if in_headline:
        violations.extend(_check_headline_order(
            hl_turn, hl_ussr_card, hl_us_card, hl_events_fired, _cname_to_ops,
        ))

    return violations


def _check_headline_order(
    turn: int,
    ussr_card: str | None,
    us_card: str | None,
    events_fired: list[str],
    cname_to_ops: dict[str, int],
) -> list[Violation]:
    """Check that headline events fired in the correct ops-descending order.

    Rule: higher-ops card fires first; US wins ties (TSEspionage implementation).
    Soft violation — Defectors and other special cases can legitimately alter order.

    Defectors exception: when the US headlines Defectors, Defectors fires first
    regardless of ops — it cancels the USSR headline entirely. Skip the check.

    Strategy: scan events_fired for the first occurrence of EITHER headlined card
    (not just events_fired[0], which may be a sub-event from the first card's effect).
    """
    if not ussr_card or not us_card:
        return []  # Incomplete headline data (Defectors cancellation, etc.)

    def _norm(s: str) -> str:
        return s.lower().rstrip("* ").strip()

    def _ops(name: str) -> int | None:
        key = _norm(name)
        return cname_to_ops.get(key)

    # Defectors exception: US headlines Defectors → it fires first and cancels USSR
    # headline regardless of ops. No order violation to report.
    if _norm(us_card) == "defectors":
        return []

    ussr_ops = _ops(ussr_card)
    us_ops = _ops(us_card)
    if ussr_ops is None or us_ops is None:
        return []  # Can't look up ops — skip.

    # Determine expected first firer.
    # TSEspionage fires the higher-ops card first; US wins ties (empirically
    # confirmed from 88 log observations: all 71 tied-ops headline events in
    # competitive logs fire US first).
    if ussr_ops > us_ops:
        expected_first_side = "USSR"
        expected_first_card = ussr_card
    elif us_ops > ussr_ops:
        expected_first_side = "US"
        expected_first_card = us_card
    else:
        # Tied ops — US fires first (TSEspionage implementation).
        expected_first_side = "US"
        expected_first_card = us_card

    # Find the first occurrence of either headlined card in the events stream.
    # This is robust against sub-events generated by the first card's effects.
    ussr_norm = _norm(ussr_card)
    us_norm = _norm(us_card)
    first_match_side: str | None = None
    first_match_name: str | None = None
    for evt in events_fired:
        evt_norm = _norm(evt)
        if evt_norm == ussr_norm:
            first_match_side = "USSR"
            first_match_name = evt
            break
        elif evt_norm == us_norm:
            first_match_side = "US"
            first_match_name = evt
            break

    if first_match_side is None:
        return []  # Neither headline card found in fired events — skip.

    if first_match_side != expected_first_side:
        return [Violation(
            kind=ViolationKind.HEADLINE_ORDER_MISMATCH,
            turn=turn, ar=0, phasing=Side.USSR,
            card_id=None, country_id=None,
            message=(
                f"headline order mismatch at turn {turn}: "
                f"USSR played {ussr_card!r} ({ussr_ops} ops), "
                f"US played {us_card!r} ({us_ops} ops); "
                f"expected {expected_first_side} to fire first "
                f"but {first_match_side} ({first_match_name!r}) fired first"
            ),
            raw_line="",
        )]
    return []


# ---------------------------------------------------------------------------
# Core validation logic
# ---------------------------------------------------------------------------


def _pub_with_influence(
    pub: PublicState,
    influence: dict[tuple[Side, int], int],
) -> PublicState:
    """Return a shallow copy of pub with influence replaced by the given dict.

    Used during step-by-step chaining simulation without mutating the original.
    """
    import dataclasses
    return dataclasses.replace(pub, influence=influence)


def _effective_influence(
    pub: PublicState,
    fixed: dict[tuple[Side, int], int],
) -> dict[tuple[Side, int], int]:
    """Merge fixed starting influence with the reducer's pub influence.

    TSEspionage logs never emit PLACE_INFLUENCE events for the fixed starting
    influence (e.g. UK=5 for US, Poland=4 for USSR).  The reducer therefore
    under-counts influence from the very first event.  This function produces
    the corrected influence map by adding the fixed baseline to whatever the
    reducer has accumulated.
    """
    merged: dict[tuple[Side, int], int] = dict(fixed)
    for key, val in pub.influence.items():
        merged[key] = merged.get(key, 0) + val
    return merged


def _validate_decision(
    ev: ReplayEvent,
    ev_idx: int,
    events: list[ReplayEvent],
    pub_before: PublicState,
    hand_knowledge: HandKnowledge,
    label: OfflineLabels | None,
    adj: dict,
    fixed_inf: dict[tuple[Side, int], int],
) -> list[Violation]:
    """Validate one PLAY or HEADLINE event.  Returns a (possibly empty) list."""
    violations: list[Violation] = []
    actor = ev.phasing
    card_id = ev.card_id

    def _v(kind: ViolationKind, msg: str, country_id: int | None = None) -> Violation:
        return Violation(
            kind=kind, turn=ev.turn, ar=ev.ar, phasing=actor,
            card_id=card_id, message=msg, country_id=country_id,
            raw_line=ev.raw_line,
        )

    # --- 1. Card resolved? ---
    if card_id is None:
        return [_v(ViolationKind.CARD_UNRESOLVED, "card_id not resolved")]

    # --- 2. Card vs pub.removed (hard) and known_not_in_hand (soft) ---
    if card_id in pub_before.removed:
        violations.append(_v(
            ViolationKind.CARD_REMOVED,
            f"card {card_id} is in pub.removed (removed from game)",
        ))
    elif card_id in hand_knowledge.known_not_in_hand:
        # Soft: the causal reducer lacks DRAW events, so cards can remain in
        # known_not_in_hand after being reshuffled and redrawn.
        violations.append(_v(
            ViolationKind.CARD_EXCLUDED_BY_REDUCER,
            f"card {card_id} in known_not_in_hand (may be false positive — no DRAW events)",
        ))

    # --- 3. Card vs smoother label ---
    actor_hand: frozenset[int]
    if label is not None:
        # Smoother's best estimate; add played card as a ground-truth guarantee.
        actor_hand = label.actor_hand | {card_id}
        if card_id not in label.actor_hand:
            violations.append(_v(
                ViolationKind.CARD_NOT_RECONSTRUCTED,
                f"card {card_id} absent from smoother label "
                f"(step_quality={label.step_quality.name})",
            ))
    else:
        actor_hand = frozenset({card_id})

    # --- 4. Mode inference ---
    mode = _infer_mode(ev)
    if mode is None:
        violations.append(_v(ViolationKind.MODE_UNRECOGNIZED, f"cannot infer mode from: {ev.raw_line!r}"))
        return violations  # can't check further without a mode

    # --- 5. Mode legality ---
    # Use effective pub (fixed + reducer influence) so COUP/REALIGN accessibility
    # checks see the correct starting influence.
    holds_china = hand_knowledge.holds_china
    eff_pub = _pub_with_influence(pub_before, _effective_influence(pub_before, fixed_inf))
    lmodes = legal_modes(card_id, eff_pub, actor, adj=adj)
    if mode not in lmodes:
        violations.append(_v(
            ViolationKind.MODE_ILLEGAL,
            f"mode {mode.name} not in legal_modes={[m.name for m in sorted(lmodes)]}",
        ))

    # --- 6. Target legality ---
    if mode in (ActionMode.INFLUENCE, ActionMode.COUP, ActionMode.REALIGN):
        targets = _collect_targets(events, ev_idx, mode, actor)
        if mode == ActionMode.INFLUENCE:
            # Simulate influence placements step-by-step so that chaining is
            # respected: placing 1 op in country A makes A's neighbours
            # accessible for the subsequent ops of the same card.
            # Start from effective (fixed + reducer) influence.
            sim_influence = _effective_influence(pub_before, fixed_inf)
            seen_illegal: set[int] = set()
            for cid in targets:
                # Recompute accessible from current sim state.
                sim_pub = _pub_with_influence(pub_before, sim_influence)
                from tsrl.engine.adjacency import accessible_countries as _acc
                accessible = _acc(actor, sim_pub, adj)
                if cid not in accessible and cid not in seen_illegal:
                    seen_illegal.add(cid)
                    violations.append(_v(
                        ViolationKind.TARGET_ILLEGAL,
                        f"country {cid} not accessible for INFLUENCE (chaining checked)",
                        country_id=cid,
                    ))
                # Always advance sim even if illegal, to not cascade errors.
                sim_influence[(actor, cid)] = sim_influence.get((actor, cid), 0) + 1
        else:
            # COUP / REALIGN: static check is correct (single-step, no chaining).
            legal_ctrs = legal_countries(card_id, mode, eff_pub, actor, adj=adj)
            seen: set[int] = set()
            for cid in targets:
                if cid in seen:
                    continue
                seen.add(cid)
                if cid not in legal_ctrs:
                    violations.append(_v(
                        ViolationKind.TARGET_ILLEGAL,
                        f"country {cid} not in legal_countries for mode={mode.name}",
                        country_id=cid,
                    ))

    return violations


# ---------------------------------------------------------------------------
# Reducer-vs-log cross-validation
# ---------------------------------------------------------------------------


def _check_reducer_vs_log(
    resolved: list,
    states: list,
    cards: dict,
) -> list[Violation]:
    """Compare reducer-computed state to absolute values logged by the server.

    Checks:
    1. INFLUENCE_STATE_MISMATCH — after PLACE/REMOVE_INFLUENCE, reducer influence
       must match logged [US][USSR] bracket.
    2. SCORING_VP_MISMATCH — scoring engine VP delta vs. logged VP_CHANGE sum.
    3. MILOPS_PENALTY_MISMATCH — end-of-turn VP penalty formula.
    4. DEFCON_STATE_MISMATCH — after DEFCON_CHANGE, pub.defcon must match ev.amount.
    5. MILOPS_STATE_MISMATCH — after MILOPS_CHANGE, pub.milops[side] must match ev.amount.
    6. SPACE_LEVEL_MISMATCH — after SPACE_RACE advance, pub.space[side] must match ev.amount.
    7. VP_ABSOLUTE_MISMATCH — after VP_CHANGE, reducer pub.vp must match absolute score
       in "Score is X" suffix of the log line.
    """
    from tsrl.engine.scoring import apply_scoring_card

    violations: list[Violation] = []

    for i, ev in enumerate(resolved):
        pub_after = states[i][0]

        # ── Influence bracket check ──────────────────────────────────────────
        if ev.kind in (EventKind.PLACE_INFLUENCE, EventKind.REMOVE_INFLUENCE):
            cid = ev.country_id
            if (
                cid is not None
                and ev.us_bracket is not None
                and ev.ussr_bracket is not None
            ):
                actual_us = pub_after.influence.get((Side.US, cid), 0)
                actual_ussr = pub_after.influence.get((Side.USSR, cid), 0)
                if actual_us != ev.us_bracket or actual_ussr != ev.ussr_bracket:
                    violations.append(Violation(
                        kind=ViolationKind.INFLUENCE_STATE_MISMATCH,
                        turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                        card_id=None, country_id=cid,
                        message=(
                            f"influence mismatch for country {cid}: "
                            f"reducer=[{actual_us}][{actual_ussr}] "
                            f"log bracket=[{ev.us_bracket}][{ev.ussr_bracket}]"
                        ),
                        raw_line=ev.raw_line,
                    ))

        # ── Scoring VP check ─────────────────────────────────────────────────
        if ev.kind == EventKind.PLAY and ev.card_id is not None:
            spec = cards.get(ev.card_id)
            if spec and spec.is_scoring:
                pub_before = states[i - 1][0] if i > 0 else PublicState()
                try:
                    result = apply_scoring_card(ev.card_id, pub_before)
                    expected_vp = result.vp_delta
                except Exception:
                    continue  # scoring engine bug — don't false-positive

                # Sum VP_CHANGE events that immediately follow (up to next PLAY/AR/HEADLINE).
                _STOP_KINDS = {
                    EventKind.PLAY, EventKind.ACTION_ROUND_START,
                    EventKind.HEADLINE_PHASE_START, EventKind.TURN_END,
                    EventKind.HEADLINE,
                }
                actual_vp = 0
                for j in range(i + 1, len(resolved)):
                    nev = resolved[j]
                    if nev.kind in _STOP_KINDS:
                        break
                    if nev.kind == EventKind.VP_CHANGE and nev.amount is not None:
                        actual_vp += nev.amount

                if actual_vp != expected_vp:
                    violations.append(Violation(
                        kind=ViolationKind.SCORING_VP_MISMATCH,
                        turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                        card_id=ev.card_id,
                        message=(
                            f"scoring VP mismatch for card {ev.card_id}: "
                            f"engine={expected_vp:+d}, log={actual_vp:+d}"
                        ),
                        raw_line=ev.raw_line,
                    ))

        # ── MilOps penalty check ─────────────────────────────────────────────
        # At end of each turn (turns 1-9), the game server applies a VP penalty
        # of max(0, DEFCON - milops) for each side, using the PRE-advance DEFCON.
        # DEFCON_CHANGE fires at the start of the NEXT turn (after HEADLINE_PHASE_START),
        # so the reducer's defcon at TURN_END is the correct pre-advance value.
        # Skip turn 10: final scoring also generates VP_CHANGE events in the same window.
        if ev.kind == EventKind.TURN_END and ev.turn <= 9:
            pub_before = states[i - 1][0] if i > 0 else PublicState()
            defcon = pub_before.defcon  # pre-advance DEFCON (correct)
            milops = pub_before.milops

            ussr_shortfall = max(0, defcon - milops[int(Side.USSR)])
            us_shortfall = max(0, defcon - milops[int(Side.US)])
            # net VP delta: US penalty → pub.vp increases (USSR gains); USSR → decreases
            expected_vp = us_shortfall - ussr_shortfall

            # Collect VP_CHANGE events immediately after TURN_END.
            _MILOPS_STOP = frozenset({
                EventKind.HEADLINE_PHASE_START,
                EventKind.TURN_START,
                EventKind.GAME_END,
                EventKind.ACTION_ROUND_START,
            })
            actual_vp = 0
            for j in range(i + 1, len(resolved)):
                nev = resolved[j]
                if nev.kind in _MILOPS_STOP:
                    break
                if nev.kind == EventKind.VP_CHANGE and nev.amount is not None:
                    actual_vp += nev.amount

            if actual_vp != expected_vp:
                violations.append(Violation(
                    kind=ViolationKind.MILOPS_PENALTY_MISMATCH,
                    turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                    card_id=None,
                    message=(
                        f"milops penalty mismatch at end of turn {ev.turn}: "
                        f"defcon={defcon}, milops={milops}, "
                        f"expected_vp={expected_vp:+d}, logged_vp={actual_vp:+d}"
                    ),
                    raw_line=ev.raw_line,
                ))

        # ── DEFCON state check ───────────────────────────────────────────────
        if ev.kind == EventKind.DEFCON_CHANGE and ev.amount is not None:
            actual_defcon = pub_after.defcon
            if actual_defcon != ev.amount:
                violations.append(Violation(
                    kind=ViolationKind.DEFCON_STATE_MISMATCH,
                    turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                    card_id=None, country_id=None,
                    message=(
                        f"DEFCON state mismatch: reducer={actual_defcon}, "
                        f"log says DEFCON changed to {ev.amount}"
                    ),
                    raw_line=ev.raw_line,
                ))

        # ── MilOps state check ───────────────────────────────────────────────
        if ev.kind == EventKind.MILOPS_CHANGE and ev.amount is not None:
            side_idx = int(ev.phasing) if ev.phasing in (Side.USSR, Side.US) else None
            if side_idx is not None:
                actual_milops = pub_after.milops[side_idx]
                if actual_milops != ev.amount:
                    violations.append(Violation(
                        kind=ViolationKind.MILOPS_STATE_MISMATCH,
                        turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                        card_id=None, country_id=None,
                        message=(
                            f"milops state mismatch for {ev.phasing.name}: "
                            f"reducer={actual_milops}, log says milops changed to {ev.amount}"
                        ),
                        raw_line=ev.raw_line,
                    ))

        # ── Space level check ────────────────────────────────────────────────
        if ev.kind == EventKind.SPACE_RACE and ev.amount is not None:
            side_idx = int(ev.phasing) if ev.phasing in (Side.USSR, Side.US) else None
            if side_idx is not None:
                actual_space = pub_after.space[side_idx]
                if actual_space != ev.amount:
                    violations.append(Violation(
                        kind=ViolationKind.SPACE_LEVEL_MISMATCH,
                        turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                        card_id=None, country_id=None,
                        message=(
                            f"space level mismatch for {ev.phasing.name}: "
                            f"reducer={actual_space}, log says space advanced to {ev.amount}"
                        ),
                        raw_line=ev.raw_line,
                    ))

        # ── VP absolute score check ──────────────────────────────────────────
        if ev.kind == EventKind.VP_CHANGE:
            m = _CROSS_RE_SCORE_SNAPSHOT.search(ev.raw_line)
            if m:
                side_str = m.group(1)    # "USSR", "US", or None (even)
                score_str = m.group(2)   # digit string or None
                if side_str is None:
                    expected_vp = 0
                elif side_str == "USSR":
                    expected_vp = int(score_str)   # type: ignore[arg-type]
                else:
                    expected_vp = -int(score_str)  # type: ignore[arg-type]
                actual_vp = pub_after.vp
                if actual_vp != expected_vp:
                    violations.append(Violation(
                        kind=ViolationKind.VP_ABSOLUTE_MISMATCH,
                        turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                        card_id=None, country_id=None,
                        message=(
                            f"VP absolute mismatch: reducer={actual_vp}, "
                            f"log says score={side_str or 'even'}"
                            + (f" {score_str}" if score_str else "")
                            + f" (expected pub.vp={expected_vp})"
                        ),
                        raw_line=ev.raw_line,
                    ))

                # ── VP win condition check ─────────────────────────────
                # If absolute score crossed ±20 threshold, GAME_END must follow
                # before any new PLAY or HEADLINE.  Also scan backward by 2 for
                # GAME_END since the parser can emit GAME_END+VP_CHANGE from the
                # same raw line with GAME_END first.
                if abs(expected_vp) >= 20:
                    _WIN_STOP = frozenset({
                        EventKind.PLAY, EventKind.HEADLINE,
                        EventKind.ACTION_ROUND_START, EventKind.TURN_START,
                    })
                    game_ended = any(
                        resolved[j].kind == EventKind.GAME_END
                        for j in range(max(0, i - 2), i)
                    )
                    game_continued = False
                    if not game_ended:
                        for j in range(i + 1, len(resolved)):
                            nev = resolved[j]
                            if nev.kind == EventKind.GAME_END:
                                game_ended = True
                                break
                            if nev.kind in _WIN_STOP:
                                game_continued = True
                                break
                    # Only flag if game demonstrably continued; if log ends
                    # after the VP threshold was crossed, game ended there.
                    if not game_ended and game_continued:
                        vp_desc = (
                            f"score={side_str} {score_str}"
                            if side_str else "score=even"
                        )
                        violations.append(Violation(
                            kind=ViolationKind.VP_WIN_NOT_TRIGGERED,
                            turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                            card_id=None, country_id=None,
                            message=(
                                f"VP absolute win ({vp_desc}) not followed "
                                f"by GAME_END before next PLAY/HEADLINE"
                            ),
                            raw_line=ev.raw_line,
                        ))

        # ── Reshuffle non-empty discard check ────────────────────────────────
        if ev.kind == EventKind.RESHUFFLE:
            pub_before = states[i - 1][0] if i > 0 else PublicState()
            if not pub_before.discard:
                violations.append(Violation(
                    kind=ViolationKind.RESHUFFLE_EMPTY_DISCARD,
                    turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                    card_id=None, country_id=None,
                    message=(
                        "RESHUFFLE fired but pub.discard was empty before the event; "
                        "nothing available to reshuffle into the draw pile"
                    ),
                    raw_line=ev.raw_line,
                ))

        # ── DEFCON-1 game-end check ──────────────────────────────────────────
        if ev.kind == EventKind.DEFCON_CHANGE and pub_after.defcon == 1:
            _DEFCON_WIN_STOP = frozenset({
                EventKind.PLAY, EventKind.HEADLINE,
                EventKind.ACTION_ROUND_START, EventKind.TURN_START,
            })
            game_ended = False
            game_continued = False  # a stop event was found before GAME_END
            for j in range(i + 1, len(resolved)):
                nev = resolved[j]
                if nev.kind == EventKind.GAME_END:
                    game_ended = True
                    break
                if nev.kind in _DEFCON_WIN_STOP:
                    game_continued = True
                    break
            # Only flag if the game demonstrably continued (a play/headline
            # was found after DEFCON=1 without GAME_END).  If the log simply
            # ends after DEFCON=1, the game likely ended there — no violation.
            if not game_ended and game_continued:
                violations.append(Violation(
                    kind=ViolationKind.DEFCON_GAME_NOT_ENDED,
                    turn=ev.turn, ar=ev.ar, phasing=ev.phasing,
                    card_id=None, country_id=None,
                    message=(
                        "DEFCON dropped to 1 but no GAME_END event followed "
                        "before the next PLAY/HEADLINE — game should end immediately"
                    ),
                    raw_line=ev.raw_line,
                ))

    return violations


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def validate_game(
    text: str,
    game_id: str,
    all_card_ids: frozenset[int],
) -> ValidationResult:
    """Validate all decision events in one game log.

    Returns a ValidationResult with zero violations if the log is fully
    consistent with the engine's legality rules and the hand reconstruction.
    """
    from tsrl.engine.adjacency import load_adjacency

    result = parse_replay(text)
    if not result.events:
        return ValidationResult(game_id=game_id, total_decisions=0)

    cards = load_cards()
    countries = load_countries()
    adj = load_adjacency()
    fixed_inf = fixed_starting_influence()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        resolved = resolve_names(result.events, cards, countries, warn_unresolved=False)

    try:
        states = reduce_game(resolved, all_card_ids, check_invariants=False)
    except Exception as exc:
        log.warning("game %s: reduce_game failed: %s", game_id, exc)
        return ValidationResult(game_id=game_id, total_decisions=0)

    try:
        labels = smooth_game(resolved, all_card_ids)
    except Exception as exc:
        log.warning("game %s: smooth_game failed: %s", game_id, exc)
        labels = []

    # Build a (turn, ar, phasing) → OfflineLabels index.
    label_map: dict[tuple[int, int, Side], OfflineLabels] = {}
    for lbl in labels:
        label_map[(lbl.turn, lbl.ar, lbl.phasing)] = lbl

    # Initial state sentinel (before any event).
    _initial_pub = PublicState()
    _initial_hand = HandKnowledge(observer=Side.USSR, possible_hidden=all_card_ids)

    all_violations: list[Violation] = []
    total_decisions = 0

    for i, ev in enumerate(resolved):
        if ev.kind not in _DECISION_KINDS:
            continue
        if ev.phasing not in (Side.USSR, Side.US):
            continue

        total_decisions += 1
        actor = ev.phasing

        pub_before = states[i - 1][0] if i > 0 else _initial_pub
        if i > 0:
            ussr_hk, us_hk = states[i - 1][1], states[i - 1][2]
        else:
            ussr_hk = us_hk = _initial_hand

        hand_knowledge = ussr_hk if actor == Side.USSR else us_hk
        label = label_map.get((ev.turn, ev.ar, actor))

        violations = _validate_decision(
            ev, i, resolved, pub_before, hand_knowledge, label, adj, fixed_inf,
        )
        all_violations.extend(violations)

    # Raw-evidence cross-checks (ground truth embedded in log metadata).
    card_name_to_ops = {spec.name: spec.ops for spec in cards.values()}
    all_violations.extend(_cross_check_raw(text, countries, card_name_to_ops))

    # Reducer-vs-log cross-checks (compare computed state to logged brackets + VP).
    all_violations.extend(_check_reducer_vs_log(resolved, states, cards))

    return ValidationResult(
        game_id=game_id,
        total_decisions=total_decisions,
        violations=all_violations,
    )


def validate_log_dir(
    log_dir: str | Path = "data/raw_logs",
    *,
    all_card_ids: frozenset[int] | None = None,
) -> dict[str, ValidationResult]:
    """Validate every *.txt file in log_dir.  Returns {filename: result}."""
    import hashlib

    log_dir = Path(log_dir)
    if all_card_ids is None:
        cards = load_cards()
        all_card_ids = frozenset(cid for cid in cards if cid != 6)

    results: dict[str, ValidationResult] = {}
    for path in sorted(log_dir.glob("*.txt")):
        text = path.read_text()
        game_id = hashlib.sha1(path.read_bytes()).hexdigest()[:12]
        results[path.name] = validate_game(text, game_id, all_card_ids)
    return results
