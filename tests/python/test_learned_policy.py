import os
import random

import pytest

from tsrl.schemas import ActionEncoding, Side


def test_model_candidate_fn_returns_list():
    """make_model_candidate_fn returns a list of ActionEncodings."""
    ckpt = "data/checkpoints/baseline_epoch20.pt"
    if not os.path.exists(ckpt):
        pytest.skip("checkpoint not found")

    from tsrl.engine.game_state import deal_cards, reset
    from tsrl.policies.learned_policy import make_model_candidate_fn

    fn = make_model_candidate_fn(ckpt, n_candidates=5)
    rng = random.Random(42)
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
    ckpt = "data/checkpoints/baseline_epoch20.pt"
    if not os.path.exists(ckpt):
        pytest.skip("checkpoint not found")

    from tsrl.engine.game_state import deal_cards, reset
    from tsrl.engine.mcts import uct_mcts
    from tsrl.policies.learned_policy import make_model_candidate_fn

    fn = make_model_candidate_fn(ckpt, n_candidates=10)
    rng = random.Random(42)
    gs = reset(seed=42)
    deal_cards(gs, Side.USSR, rng=rng)
    deal_cards(gs, Side.US, rng=rng)

    action = uct_mcts(gs, n_sim=5, candidate_fn=fn, rng=rng)
    assert action is not None
