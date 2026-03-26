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
from typing import FrozenSet


# ---------------------------------------------------------------------------
# Primitive enumerations
# ---------------------------------------------------------------------------


class Side(IntEnum):
    USSR = 0
    US = 1
    NEUTRAL = 2


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
    card_id: int | None = None       # primary card involved (None if not applicable)
    country_id: int | None = None    # primary country target (None if not applicable)
    amount: int | None = None        # e.g. influence delta, VP delta, DEFCON delta
    aux_card_ids: tuple[int, ...] = field(default_factory=tuple)  # secondary cards
    aux_country_ids: tuple[int, ...] = field(default_factory=tuple)
    raw_line: str = ""               # original log line for debugging
    line_number: int = 0


# ---------------------------------------------------------------------------
# Public state (online-safe, board-visible information only)
# ---------------------------------------------------------------------------


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
    # Populated lazily; use defaultdict semantics in practice.
    influence: dict[tuple[Side, int], int] = field(default_factory=dict)

    # Card location knowledge (public)
    discard: frozenset[int] = field(default_factory=frozenset)   # card ids in discard
    removed: frozenset[int] = field(default_factory=frozenset)   # removed from game
    # deck_remaining is implied: all cards not in discard/removed/known-in-hand

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
