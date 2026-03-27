"""
Dice rolls for Twilight Struggle stochastic actions.

All randomness is isolated here so the game loop can inject an RNG for
deterministic seeds.  Pass a ``random.Random`` instance to each function;
callers that want the global RNG can pass ``None``.
"""
from __future__ import annotations

import random as _random_module
from typing import Optional

_RNG = _random_module.Random()   # module-level default


def set_seed(seed: int) -> None:
    """Seed the module-level RNG (used when callers pass rng=None)."""
    _RNG.seed(seed)


def roll_d6(rng: Optional[_random_module.Random] = None) -> int:
    """Roll one fair 6-sided die (1–6)."""
    r = rng if rng is not None else _RNG
    return r.randint(1, 6)


def roll_2d6(rng: Optional[_random_module.Random] = None) -> tuple[int, int]:
    """Roll two fair 6-sided dice independently."""
    r = rng if rng is not None else _RNG
    return r.randint(1, 6), r.randint(1, 6)


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
    rng: Optional[_random_module.Random] = None,
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
    rng: Optional[_random_module.Random] = None,
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
    ussr_roll = r.randint(1, 6)
    us_roll = r.randint(1, 6)

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
    rng: Optional[_random_module.Random] = None,
) -> bool:
    """Roll for space race advancement from current_level.

    Returns True if the roll succeeds (die ≤ threshold for current level).
    Returns False if current_level >= 8 (already at max).
    """
    if current_level >= 8:
        return False
    roll = roll_d6(rng)
    return roll <= SPACE_ADVANCE_THRESHOLD[current_level]
