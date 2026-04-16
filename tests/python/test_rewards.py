import pytest

from tsrl.rewards import compute_shaped_reward


def test_compute_shaped_reward_ussr_win_uses_vp_and_turn_bonus() -> None:
    reward = compute_shaped_reward(
        winner=0,
        side=0,
        final_vp=10,
        end_turn=8,
        end_reason="vp_track",
        alpha=0.5,
    )
    assert reward == pytest.approx(1.029)


def test_compute_shaped_reward_flips_vp_sign_for_us() -> None:
    reward = compute_shaped_reward(
        winner=1,
        side=1,
        final_vp=10,
        end_turn=10,
        end_reason="turn_limit",
        alpha=0.5,
    )
    assert reward == pytest.approx(0.98)


def test_compute_shaped_reward_draw_uses_shaping_only() -> None:
    reward = compute_shaped_reward(
        winner=None,
        side=0,
        final_vp=-30,
        end_turn=10,
        end_reason="draw",
        alpha=0.5,
    )
    assert reward == pytest.approx(-0.045)
