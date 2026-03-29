"""
Core data schemas for Twilight Struggle replay processing.

Three strict layers – never leak between them:
  1. PublicState       – online-safe board state
  2. HandKnowledge     – online-safe per-player hidden-info state
  3. OfflineLabels     – offline smoother output for supervised training only
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import FrozenSet, Optional


# ---------------------------------------------------------------------------
# Primitive enumerations
# ---------------------------------------------------------------------------


class Side(IntEnum):
    USSR = 0
    US = 1
    NEUTRAL = 2


class ActionMode(IntEnum):
    """How a card is being used at a decision point."""
    INFLUENCE = 0   # play card for ops → place influence
    COUP      = 1   # play card for ops → attempt coup
    REALIGN   = 2   # play card for ops → attempt realignment(s)
    SPACE     = 3   # play card for space race attempt
    EVENT     = 4   # play card for its event effect


class Era(IntEnum):
    EARLY = 0
    MID = 1
    LATE = 2


class Region(IntEnum):
    EUROPE = 0
    ASIA = 1
    MIDDLE_EAST = 2
    CENTRAL_AMERICA = 3
    SOUTH_AMERICA = 4
    AFRICA = 5
    SOUTHEAST_ASIA = 6  # sub-region of Asia for scoring


# ---------------------------------------------------------------------------
# Action encoding
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ActionEncoding:
    """Factorized action for one decision point.

    card_id:  Card being played (1..111).
    mode:     How the card is used.
    targets:  Country IDs the ops are applied to, in order.

      - INFLUENCE: each entry receives 1 influence point;
        len(targets) == card.ops (full-ops use) or ≤ card.ops.
      - COUP:      len(targets) == 1; all ops applied to that country.
      - REALIGN:   len(targets) == card.ops; one attempt per country.
      - SPACE:     len(targets) == 0.
      - EVENT:     len(targets) == 0 (event effects handled separately).
    """
    card_id: int
    mode: ActionMode
    targets: tuple[int, ...] = ()


# ---------------------------------------------------------------------------
# Replay event types
# ---------------------------------------------------------------------------


class EventKind(IntEnum):
    """Normalized replay event kind.  Values are stable – do not reorder."""

    # Meta / structural
    GAME_START = 0
    TURN_START = 1
    HEADLINE_PHASE_START = 2
    ACTION_ROUND_START = 3
    TURN_END = 4
    GAME_END = 5

    # Card lifecycle
    HEADLINE = 10       # player places card face-down in headline
    PLAY = 11           # player plays card (ops or event)
    FORCED_DISCARD = 12 # e.g. Five Year Plan
    REVEAL_HAND = 13    # hand revealed (e.g. by CIA Created)
    TRANSFER = 14       # card moves from one player to another
    DRAW = 15           # player draws card(s)
    DISCARD = 16        # card goes to discard pile
    REMOVE = 17         # card removed from game (starred event resolved)
    RESHUFFLE = 18      # discard reshuffled into deck
    END_TURN_HELD = 19  # card held into next turn (revealed at AR end)

    # Board actions
    COUP = 20
    REALIGN = 21
    PLACE_INFLUENCE = 22
    REMOVE_INFLUENCE = 23
    SPACE_RACE = 24

    # Scoring
    SCORING = 30

    # State changes
    DEFCON_CHANGE = 40
    VP_CHANGE = 41
    MILOPS_CHANGE = 42
    CHINA_CARD_PASS = 43

    # Ongoing effect tracking
    CARD_IN_PLAY = 44   # e.g. "NATO* is now in play."
    CARD_EXPIRED = 45   # e.g. "Containment* is no longer in play."

    # Setup / handicap
    HANDICAP = 46       # competitive bidding handicap grant ("Handicap influence: US +2")

    # Unknown / unparsed
    UNKNOWN = 255


@dataclass(frozen=True)
class ReplayEvent:
    """A single normalized event extracted from a replay log.

    Immutable.  Preserve ``raw_line`` alongside normalized fields for
    debugging and audit.
    """

    kind: EventKind
    turn: int                        # 1-10; 0 = setup
    ar: int                          # action round; 0 = setup/headline
    phasing: Side                    # who is acting (USSR/US/NEUTRAL for scoring)
    card_id: int | None = None       # primary card involved (None until resolver pass)
    country_id: int | None = None    # primary country target (None until resolver pass)
    amount: int | None = None        # e.g. influence delta, VP delta, DEFCON value
    aux_card_ids: tuple[int, ...] = field(default_factory=tuple)  # secondary cards
    aux_country_ids: tuple[int, ...] = field(default_factory=tuple)
    raw_line: str = ""               # original log line for debugging
    line_number: int = 0
    # Raw string names, populated by parser; converted to IDs by resolver pass.
    card_name: str | None = None
    country_name: str | None = None
    # Absolute bracket values logged after an influence change (PLACE/REMOVE_INFLUENCE).
    # Populated by parser; used for reducer-vs-log cross-validation.
    us_bracket: int | None = None
    ussr_bracket: int | None = None


# ---------------------------------------------------------------------------
# Public state (online-safe, board-visible information only)
# ---------------------------------------------------------------------------


class InfluenceArray:
    """Flat-array influence store with dict-compatible tuple-key API.

    Supports country IDs 1..85 per side (85 = Taiwan).  The per-side stride is
    85 so that country_id maps to index (cid - 1) within each side block.
    Total array length = 170 (= 85 * 2 sides).

    Model features use only the first 84 countries per side (168 total) since
    the model vocabulary excludes Taiwan; _influence_array() slices [base:base+84].
    """

    _STRIDE = 85
    _TOTAL = 170  # _STRIDE * 2

    __slots__ = ("_data",)

    def __init__(self, source=None):
        if source is None:
            self._data = [0] * self._TOTAL
        elif isinstance(source, InfluenceArray):
            self._data = list(source._data)
        elif hasattr(source, "items"):
            self._data = [0] * self._TOTAL
            for (side, cid), val in source.items():
                self._data[int(side) * self._STRIDE + (cid - 1)] = val
        else:
            self._data = list(source)

    def __getitem__(self, key):
        side, cid = key
        return self._data[int(side) * self._STRIDE + (cid - 1)]

    def __setitem__(self, key, value):
        side, cid = key
        self._data[int(side) * self._STRIDE + (cid - 1)] = value

    def get(self, key, default=0):
        side, cid = key
        idx = int(side) * self._STRIDE + (cid - 1)
        if idx < 0 or idx >= self._TOTAL:
            return default
        return self._data[idx]

    _MISSING = object()

    def pop(self, key, default=_MISSING):
        side, cid = key
        idx = int(side) * self._STRIDE + (cid - 1)
        if idx < 0 or idx >= self._TOTAL:
            if default is InfluenceArray._MISSING:
                raise KeyError(key)
            return default
        old = self._data[idx]
        if old == 0:
            if default is InfluenceArray._MISSING:
                raise KeyError(key)
            return default
        self._data[idx] = 0
        return old

    def items(self):
        for side_idx in range(2):
            side = Side(side_idx)
            base = side_idx * self._STRIDE
            for cid in range(1, self._STRIDE + 1):
                val = self._data[base + cid - 1]
                if val != 0:
                    yield (side, cid), val

    def keys(self):
        return dict(self.items()).keys()

    def copy(self):
        new = InfluenceArray.__new__(InfluenceArray)
        new._data = list(self._data)
        return new

    def __iter__(self):
        return (k for k, _ in self.items())

    def __contains__(self, key):
        return self.get(key, 0) != 0

    def __repr__(self):
        return f"InfluenceArray({dict(self.items())})"

    def __eq__(self, other):
        if isinstance(other, InfluenceArray):
            return self._data == other._data
        return NotImplemented


@dataclass
class PublicState:
    """Complete public board state at a point in the game.

    Derived solely from events observable to both players.
    Never store per-player hand information here.
    """

    # Game progress
    turn: int = 0          # 1-10
    ar: int = 0            # action round within turn (0 = setup / headline)
    phasing: Side = Side.USSR

    # Scoring and global tracks
    vp: int = 0            # positive = USSR lead, negative = US lead
    defcon: int = 5        # 1=nuclear war, 5=peace
    milops: list[int] = field(default_factory=lambda: [0, 0])   # [USSR, US]
    space: list[int] = field(default_factory=lambda: [0, 0])    # [USSR, US] space race level

    # China Card
    china_held_by: Side = Side.USSR
    china_playable: bool = True  # face-up (playable) or face-down

    # Influence: indexed [Side][country_id]
    influence: "InfluenceArray" = field(default_factory=InfluenceArray)

    # Card location knowledge (public)
    discard: frozenset[int] = field(default_factory=frozenset)   # card ids in discard
    removed: frozenset[int] = field(default_factory=frozenset)   # removed from game
    # deck_remaining is implied: all cards not in discard/removed/known-in-hand

    # Per-turn space action counter; used by Yuri and Samantha (card 106).
    # Resets to [0, 0] at end of each turn.
    space_attempts: list[int] = field(default_factory=lambda: [0, 0])  # [USSR, US]
    space_level4_first: Optional[Side] = None  # first side to reach space level 4
    space_level6_first: Optional[Side] = None  # first side to reach space level 6

    # --- Persistent effect flags (game-scoped unless noted) ---
    warsaw_pact_played: bool = False
    marshall_plan_played: bool = False
    truman_doctrine_played: bool = False
    john_paul_ii_played: bool = False
    nato_active: bool = False          # NATO (21): blocks USSR coups/realigns in US-controlled WE
    de_gaulle_active: bool = False     # De Gaulle (17): France excluded from NATO protection
    willy_brandt_active: bool = False  # Willy Brandt (58): W.Germany excluded from NATO
    us_japan_pact_active: bool = False # US/Japan Pact (27): Japan blocked from USSR coups/realigns
    nuclear_subs_active: bool = False  # Nuclear Subs (44): US coups don't degrade DEFCON
    norad_active: bool = False         # NORAD (38): US free inf if DEFCON=2 after USSR AR
    shuttle_diplomacy_active: bool = False  # Shuttle Diplomacy (74): next scoring ignores top BG
    flower_power_active: bool = False  # Flower Power (62): USSR gains 2VP per US war card event
    flower_power_cancelled: bool = False  # An Evil Empire (100) cancels Flower Power
    salt_active: bool = False          # SALT Negotiations (46): DEFCON+2, discard visibility
    opec_cancelled: bool = False       # Iron Lady (86) / North Sea Oil (89) cancel OPEC
    awacs_active: bool = False         # AWACS Sale (107): Saudi Arabia excluded from OPEC (GAME-SCOPED)
    north_sea_oil_extra_ar: bool = False  # North Sea Oil (89): US gets one extra AR this turn (TURN-SCOPED)
    glasnost_extra_ar: bool = False    # Glasnost (93): USSR gets one extra AR when SALT active (TURN-SCOPED)
    formosan_active: bool = False      # Formosan Resolution (35): Taiwan counts as BG for scoring
    cuban_missile_crisis_active: bool = False  # CMC (43): DEFCON locked, BG coups = game over
    vietnam_revolts_active: bool = False  # Vietnam Revolts (9): USSR +1 ops bonus (TURN-SCOPED)

    # Trap / hostage state
    bear_trap_active: bool = False   # Bear Trap (47): USSR trapped, must use ops each AR
    quagmire_active: bool = False    # Quagmire (45): US trapped, must use ops each AR
    iran_hostage_crisis_active: bool = False  # Iranian Hostage Crisis (85): Terrorism discards 2 cards

    # Competitive handicap (bid amount) — 0 in standard games.
    handicap_ussr: int = 0   # extra influence granted to USSR at setup
    handicap_us: int = 0     # extra influence granted to US at setup

    # Turn-scoped ops modifiers (reset at end of each turn).
    # Index 0 = USSR, 1 = US. Positive = bonus, negative = penalty. Min effective ops = 1.
    ops_modifier: list[int] = field(default_factory=lambda: [0, 0])

    # Chernobyl (97): US designates one region per turn; USSR cannot place ops-influence there.
    # Reset to None at end of turn.
    chernobyl_blocked_region: "Region | None" = None

    # Latin American Death Squads (70): this side gets +1 on C/S America coup rolls; opponent gets -1.
    # Reset to None at end of turn.
    latam_coup_bonus: "Side | None" = None

    # Zobrist hash of this state (updated by reducer)
    state_hash: int = 0


# ---------------------------------------------------------------------------
# Hand knowledge (online-safe, per-player hidden info)
# ---------------------------------------------------------------------------


@dataclass
class HandKnowledge:
    """Causal per-player hand knowledge.

    Derived only from events in the replay prefix up to the current point.
    Safe to use during online inference and self-play.

    Invariant: ``known_in_hand`` ∩ ``known_not_in_hand`` == ∅
    Invariant: ``possible_hidden`` ⊆ (all_cards - known_not_in_hand)
    Invariant: false_exclusion_rate == 0
      (no card the actor actually holds may appear in known_not_in_hand)
    """

    observer: Side = Side.USSR   # whose perspective this tracks

    # Cards we have positively observed the actor draw/hold
    known_in_hand: FrozenSet[int] = field(default_factory=frozenset)

    # Cards we know cannot be in hand (played, discarded, removed, or observed elsewhere)
    known_not_in_hand: FrozenSet[int] = field(default_factory=frozenset)

    # Support mask: cards that *could* be in the unobserved portion of hand.
    # Must satisfy: no actual held card is excluded.
    possible_hidden: FrozenSet[int] = field(default_factory=frozenset)

    # Hand size (excluding China Card)
    hand_size: int = 0

    # Whether this player holds the China Card
    holds_china: bool = False


# ---------------------------------------------------------------------------
# Offline smoother labels (OFFLINE ONLY – never use during online inference)
# ---------------------------------------------------------------------------


class LabelQuality(IntEnum):
    """Confidence of an offline-smoothed label."""

    EXACT = 0        # card was directly observed in hand at this step
    INFERRED = 1     # card provably held based on future observations
    AMBIGUOUS = 2    # multiple cards possible; best-guess assignment
    UNKNOWN = 3      # could not reconstruct


@dataclass
class OfflineLabels:
    """Offline smoother output for supervised training.

    Built using the *full* replay (past + future).
    MUST NOT be used in online inference, self-play, or evaluation environments.
    """

    turn: int
    ar: int
    phasing: Side

    # Actor hand at this decision point (best reconstruction)
    actor_hand: FrozenSet[int] = field(default_factory=frozenset)

    # Quality tag per card in actor_hand
    card_quality: dict[int, LabelQuality] = field(default_factory=dict)

    # Overall quality for this step
    step_quality: LabelQuality = LabelQuality.UNKNOWN

    # Opponent hand support mask (exact, no false exclusions)
    opponent_possible: FrozenSet[int] = field(default_factory=frozenset)
