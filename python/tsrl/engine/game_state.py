"""
GameState: complete state for a live Twilight Struggle game.

Holds PublicState (board) + hidden information (actual hands, deck).
Used by the game loop; NOT the same as the replay-derived state.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from tsrl.engine.rng import RNG, make_rng
from enum import IntEnum, auto
from typing import Optional

from tsrl.etl.game_data import load_cards, load_countries
from tsrl.schemas import PublicState, Side

# ---------------------------------------------------------------------------
# Phase enum
# ---------------------------------------------------------------------------


class GamePhase(IntEnum):
    SETUP         = 0
    HEADLINE      = 1   # both players choose headline cards simultaneously
    ACTION_ROUND  = 2   # alternating action rounds
    CLEANUP       = 3   # end-of-turn housekeeping
    GAME_OVER     = 4


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_CHINA_CARD_ID: int = 6

# Action rounds per turn: turns 1-3 = 6; turns 4-10 = 7.
def _ars_for_turn(turn: int) -> int:
    return 6 if turn <= 3 else 7

# Hand size per turn.
def _hand_size_for_turn(turn: int) -> int:
    return 8 if turn <= 3 else 9

# Mid-war cards reshuffled in before Turn 4; Late-war before Turn 8.
# Era filtering is done via CardSpec.era (Era.EARLY=0, MID=1, LATE=2).


# ---------------------------------------------------------------------------
# GameState
# ---------------------------------------------------------------------------


@dataclass
class GameState:
    """Complete state for one live game.

    All fields are mutable; call reset() to get a fresh game.
    """
    pub: PublicState = field(default_factory=PublicState)

    # Actual hands (card IDs, excluding China Card tracked separately).
    hands: dict[Side, frozenset[int]] = field(
        default_factory=lambda: {Side.USSR: frozenset(), Side.US: frozenset()}
    )

    # Draw deck (list, order = draw order; pop from end).
    deck: list[int] = field(default_factory=list)

    # China Card ownership.
    ussr_holds_china: bool = True
    us_holds_china: bool = False

    # Game progress tracking.
    phase: GamePhase = GamePhase.SETUP
    current_side: Side = Side.USSR   # whose turn it is in this AR
    ar_index: int = 1                # current action round (1-based)
    ars_taken: dict[Side, int] = field(
        default_factory=lambda: {Side.USSR: 0, Side.US: 0}
    )

    # Headline choices (filled during HEADLINE phase).
    headline_card: dict[Side, Optional[int]] = field(
        default_factory=lambda: {Side.USSR: None, Side.US: None}
    )

    # Terminal state.
    game_over: bool = False
    winner: Optional[Side] = None

    # Cards dealt into current era (Early/Mid/Late) — used for refill.
    # We track the discard separately in pub.discard; deck is rebuilt at reshuffle.


# ---------------------------------------------------------------------------
# Factory: reset / new game
# ---------------------------------------------------------------------------


def reset(seed: Optional[int] = None) -> GameState:
    """Create and return a freshly initialized game state.

    Sets up starting influence per countries.csv, deals initial hands,
    and positions the game at the start of Turn 1 Headline Phase.
    """
    rng = make_rng(seed)
    gs = GameState()
    gs.pub = PublicState()
    gs.pub.turn = 1
    gs.pub.ar = 0
    gs.pub.defcon = 5
    gs.pub.vp = 0
    gs.pub.milops = [0, 0]
    gs.pub.space = [0, 0]
    gs.pub.china_held_by = Side.USSR
    gs.pub.china_playable = True

    # --- Place starting influence ---
    countries = load_countries()
    for cid, spec in countries.items():
        if spec.us_start > 0:
            gs.pub.influence[(Side.US, cid)] = spec.us_start
        if spec.ussr_start > 0:
            gs.pub.influence[(Side.USSR, cid)] = spec.ussr_start

    # --- Build and shuffle Early War deck ---
    gs.deck = _build_era_deck(era_max=0)  # 0 = Early War only
    rng.shuffle(gs.deck)

    # --- Deal initial hands (turn 1 = hand_size 8) ---
    hand_size = _hand_size_for_turn(1)
    for side in (Side.USSR, Side.US):
        drawn, gs.deck = gs.deck[:hand_size], gs.deck[hand_size:]
        gs.hands[side] = frozenset(drawn)

    gs.phase = GamePhase.HEADLINE
    gs.current_side = Side.USSR
    gs.ar_index = 1
    gs.ars_taken = {Side.USSR: 0, Side.US: 0}

    return gs


def advance_to_mid_war(gs: GameState, rng: RNG) -> None:
    """Reshuffle Early War discard + add Mid War cards before Turn 4."""
    mid_cards = _build_era_deck(era_max=1, exclude=set(gs.pub.removed))
    discard = list(gs.pub.discard)
    new_deck = mid_cards + discard
    rng.shuffle(new_deck)
    gs.deck = new_deck
    gs.pub.discard = frozenset()


def advance_to_late_war(gs: GameState, rng: RNG) -> None:
    """Reshuffle Mid War discard + add Late War cards before Turn 8."""
    late_cards = _build_era_deck(era_max=2, exclude=set(gs.pub.removed))
    discard = list(gs.pub.discard)
    new_deck = late_cards + discard
    rng.shuffle(new_deck)
    gs.deck = new_deck
    gs.pub.discard = frozenset()


def clone_game_state(gs: GameState) -> GameState:
    """Return a deep copy of GameState for MCTS simulation."""
    import copy
    new_gs = GameState()
    # Deep-copy PublicState mutable containers.
    new_gs.pub = copy.copy(gs.pub)
    new_gs.pub.milops = list(gs.pub.milops)
    new_gs.pub.space = list(gs.pub.space)
    new_gs.pub.space_attempts = list(gs.pub.space_attempts)
    new_gs.pub.ops_modifier = list(gs.pub.ops_modifier)
    new_gs.pub.influence = gs.pub.influence.copy()
    # frozensets are immutable — safe to share.
    new_gs.hands = {s: h for s, h in gs.hands.items()}
    new_gs.deck = list(gs.deck)
    new_gs.ussr_holds_china = gs.ussr_holds_china
    new_gs.us_holds_china = gs.us_holds_china
    new_gs.phase = gs.phase
    new_gs.current_side = gs.current_side
    new_gs.ar_index = gs.ar_index
    new_gs.ars_taken = dict(gs.ars_taken)
    new_gs.headline_card = dict(gs.headline_card)
    new_gs.game_over = gs.game_over
    new_gs.winner = gs.winner
    return new_gs


def deal_cards(gs: GameState, side: Side, rng: RNG) -> None:
    """Deal cards to bring side's hand up to the current turn's hand size.

    Reshuffles discard into deck if deck runs out mid-deal.
    """
    target = _hand_size_for_turn(gs.pub.turn)
    current = len(gs.hands[side])
    needed = target - current
    if needed <= 0:
        return

    hand_list = list(gs.hands[side])
    for _ in range(needed):
        if not gs.deck:
            _reshuffle(gs, rng)
        if gs.deck:
            hand_list.append(gs.deck.pop())
    gs.hands[side] = frozenset(hand_list)


def _reshuffle(gs: GameState, rng: RNG) -> None:
    """Move discard pile into deck and shuffle."""
    gs.deck = list(gs.pub.discard)
    gs.pub.discard = frozenset()
    rng.shuffle(gs.deck)


def _build_era_deck(era_max: int, exclude: set[int] | None = None) -> list[int]:
    """Return all non-scoring draw-deck cards with era <= era_max.

    era_max: 0=Early only, 1=Early+Mid, 2=Early+Mid+Late.
    Excludes China Card (id=6) and scoring cards (is_scoring=True).
    """
    exclude = exclude or set()
    cards = load_cards()
    return [
        cid for cid, spec in cards.items()
        if cid != _CHINA_CARD_ID
        and not spec.is_scoring
        and int(spec.era) <= era_max
        and cid not in exclude
    ]
