"""Reward shaping helpers for PPO training.

Only GameResult-derived shaping is implemented here for now. Final-board signals
such as region control, milops compliance, and space race progress need access to
 the terminal public state and are intentionally left as TODOs.
"""

from __future__ import annotations

from typing import Optional


def _clip_unit(value: float) -> float:
    return max(-1.0, min(1.0, value))


def _base_reward(winner: Optional[int], side: int) -> float:
    if winner is None:
        return 0.0
    return 1.0 if winner == side else -1.0


def _vp_trajectory_bonus(side: int, final_vp: int) -> float:
    """Scaled final VP from the acting side's perspective.

    `final_vp` is defined from the USSR perspective, so the sign flips for US.
    """
    vp_bonus = _clip_unit(final_vp / 20.0)
    return vp_bonus if side == 0 else -vp_bonus


def _region_control_bonus() -> float:
    """TODO: derive region control shaping from the final board state.

    This needs the terminal public state with per-country influence and the
    scoring helpers needed to classify each main scoring region as Presence,
    Domination, or Control for both sides.
    """
    return 0.0


def _milops_compliance_bonus() -> float:
    """TODO: penalize end-of-turn milops shortfalls.

    This needs per-turn terminal snapshots or a turn history carrying each
    side's milops and DEFCON at the end of every turn.
    """
    return 0.0


def _space_race_bonus() -> float:
    """TODO: reward terminal space-race progress.

    This needs the final public state with the player's terminal space-race
    level so the configured `0.02 * level` bonus can be applied.
    """
    return 0.0


def _turn_length_bonus(end_turn: int) -> float:
    return 0.01 * (end_turn / 10.0)


def compute_shaped_reward(
    winner: Optional[int],
    side: int,
    final_vp: int,
    end_turn: int,
    end_reason: str,
    *,
    alpha: float = 0.5,
) -> float:
    """Compute terminal reward with lightweight shaping.

    Implemented today:
    - base win/loss/draw reward
    - VP trajectory bonus
    - turn length bonus

    Reserved for future terminal-state extensions:
    - region control bonus
    - milops compliance bonus
    - space race bonus

    `end_reason` is accepted for API stability with the rollout result contract.
    It is not used by the currently implemented shaping terms.
    """
    del end_reason

    shaping_bonus = 0.0
    shaping_bonus += 0.1 * _vp_trajectory_bonus(side, final_vp)
    shaping_bonus += _turn_length_bonus(end_turn)
    shaping_bonus += _region_control_bonus()
    shaping_bonus += _milops_compliance_bonus()
    shaping_bonus += _space_race_bonus()

    return _base_reward(winner, side) + alpha * shaping_bonus
