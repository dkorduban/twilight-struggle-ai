"""
Dice rolls for Twilight Struggle stochastic actions.

All randomness is isolated here so the game loop can inject an RNG for
deterministic seeds.  Pass a ``np.random.Generator`` (PCG64) instance to each
function; callers that want the module-level default RNG can pass ``None``.
"""
from __future__ import annotations

from typing import Optional

import numpy as np

from tsrl.engine.rng import RNG, make_rng

_RNG: RNG = make_rng()   # module-level default (randomly seeded)


def set_seed(seed: int) -> None:
    """Re-seed the module-level RNG (used when callers pass rng=None)."""
    global _RNG
    _RNG = make_rng(seed)


def roll_d6(rng: Optional[RNG] = None) -> int:
    """Roll one fair 6-sided die (1–6)."""
    r = rng if rng is not None else _RNG
    return int(r.integers(1, 7))


def roll_2d6(rng: Optional[RNG] = None) -> tuple[int, int]:
    """Roll two fair 6-sided dice independently."""
    r = rng if rng is not None else _RNG
    return int(r.integers(1, 7)), int(r.integers(1, 7))


# ---------------------------------------------------------------------------
# Coup
# ---------------------------------------------------------------------------


def coup_net(
    attacker_roll: int,
    ops: int,
    defender_stability: int,
) -> int:
    """Net influence change after a coup attempt.

    Rule: net = (attacker_die + ops) - (2 × stability)
    If net > 0: attacker removes that many opponent influence.
    If net ≤ 0: no effect.

    Returns the net (may be ≤ 0).
    """
    return attacker_roll + ops - 2 * defender_stability


def coup_result(
    ops: int,
    defender_stability: int,
    *,
    rng: Optional[RNG] = None,
) -> int:
    """Roll for a coup and return the net influence swing.

    Positive return value: attacker removes that many opponent influence
    (and gains the excess as own influence if opponent hits 0).
    0 or negative: coup fails.
    """
    roll = roll_d6(rng)
    return coup_net(roll, ops, defender_stability)


# ---------------------------------------------------------------------------
# Realignment
# ---------------------------------------------------------------------------


def realign_result(
    ussr_influence: int,
    us_influence: int,
    ussr_adj_nations: int,
    us_adj_nations: int,
    *,
    rng: Optional[RNG] = None,
) -> tuple[int, int]:
    """Roll realignment dice and return (ussr_die_total, us_die_total).

    The side with the higher total removes (total_diff) influence from the
    other side in the target country.  Ties have no effect.

    Modifiers added per side (before rolling):
      +1 if side has more influence in the country than the opponent
      +1 per adjacent nation controlled by the side
      +1 if side holds the country's superpower (adjacency anchor)

    The caller computes the pre-roll modifiers and passes them as
    ussr_adj_nations / us_adj_nations (adjacent countries controlled by each side).

    Returns raw dice only; caller applies influence delta.
    """
    r = rng if rng is not None else _RNG
    ussr_roll = int(r.integers(1, 7))
    us_roll = int(r.integers(1, 7))

    ussr_mod = ussr_adj_nations + (1 if ussr_influence > us_influence else 0)
    us_mod = us_adj_nations + (1 if us_influence > ussr_influence else 0)

    return ussr_roll + ussr_mod, us_roll + us_mod


# ---------------------------------------------------------------------------
# Space Race
# ---------------------------------------------------------------------------

# Required die roll to advance from level N (0-indexed) to N+1.
# Source: TS rulebook space race track, ITS rules.
SPACE_ADVANCE_THRESHOLD = [3, 4, 3, 4, 3, 4, 3, 2]  # indices 0-7 (current level); roll ≤ this to advance


def space_result(
    current_level: int,
    *,
    rng: Optional[RNG] = None,
) -> bool:
    """Roll for space race advancement from current_level.

    Returns True if the roll succeeds (die ≤ threshold for current level).
    Returns False if current_level >= 8 (already at max).
    """
    if current_level >= 8:
        return False
    roll = roll_d6(rng)
    return roll <= SPACE_ADVANCE_THRESHOLD[current_level]
