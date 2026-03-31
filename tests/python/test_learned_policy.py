import os
from tsrl.engine.rng import make_rng

import pytest

from tsrl.schemas import ActionEncoding, ActionMode, Side


def test_model_candidate_fn_returns_list():
    """make_model_candidate_fn returns a list of ActionEncodings."""
    ckpt = "data/checkpoints/retrain_v17/baseline_best.pt"
    if not os.path.exists(ckpt):
        pytest.skip("checkpoint not found")

    from tsrl.engine.game_state import deal_cards, reset
    from tsrl.policies.learned_policy import make_model_candidate_fn

    fn = make_model_candidate_fn(ckpt, n_candidates=5)
    rng = make_rng(42)
    gs = reset(seed=42)
    deal_cards(gs, Side.USSR, rng=rng)
    deal_cards(gs, Side.US, rng=rng)

    side = gs.pub.phasing
    holds_china = gs.ussr_holds_china if side == Side.USSR else gs.us_holds_china
    candidates = fn(gs, side, holds_china, 5, rng=rng)

    assert isinstance(candidates, list)
    assert 0 < len(candidates) <= 5
    for a in candidates:
        assert isinstance(a, ActionEncoding)


def test_model_candidate_fn_with_uct_mcts():
    """uct_mcts with model candidate_fn should produce a valid action."""
    ckpt = "data/checkpoints/retrain_v17/baseline_best.pt"
    if not os.path.exists(ckpt):
        pytest.skip("checkpoint not found")

    from tsrl.engine.game_state import deal_cards, reset
    from tsrl.engine.mcts import uct_mcts
    from tsrl.policies.learned_policy import make_model_candidate_fn

    fn = make_model_candidate_fn(ckpt, n_candidates=10)
    rng = make_rng(42)
    gs = reset(seed=42)
    deal_cards(gs, Side.USSR, rng=rng)
    deal_cards(gs, Side.US, rng=rng)

    action = uct_mcts(gs, n_sim=5, candidate_fn=fn, rng=rng)
    assert action is not None


def test_learned_policy_no_defcon2_coup():
    """make_learned_policy must never return a COUP action at DEFCON 2."""
    ckpt = "data/checkpoints/retrain_v17/baseline_best.pt"
    if not os.path.exists(ckpt):
        pytest.skip("checkpoint not found")

    from tsrl.engine.game_state import deal_cards, reset
    from tsrl.policies.learned_policy import make_learned_policy

    policy = make_learned_policy(ckpt, Side.USSR)
    rng = make_rng(99)

    for seed in range(20):
        gs = reset(seed=seed)
        deal_cards(gs, Side.USSR, rng=rng)
        gs.pub.defcon = 2  # Force DEFCON 2

        action = policy(gs.pub, gs.hands[Side.USSR], gs.ussr_holds_china)
        if action is not None:
            assert action.mode != ActionMode.COUP, (
                f"Learned policy returned COUP at DEFCON 2 (seed={seed}): {action}"
            )
