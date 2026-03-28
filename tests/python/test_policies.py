from __future__ import annotations

import torch

from tsrl.engine.game_state import reset
from tsrl.policies.learned_policy import make_learned_policy
from tsrl.policies.model import TSBaselineModel
from tsrl.schemas import ActionEncoding, Side


def test_learned_policy_raises_on_missing_checkpoint(tmp_path) -> None:
    missing = tmp_path / "missing.pt"
    try:
        make_learned_policy(str(missing), Side.USSR)
    except FileNotFoundError:
        return
    raise AssertionError("Expected FileNotFoundError for a missing checkpoint")


def test_learned_policy_returns_action_or_none(tmp_path) -> None:
    checkpoint = tmp_path / "baseline.pt"
    model = TSBaselineModel()
    torch.save({"model_state_dict": model.state_dict()}, checkpoint)

    gs = reset(seed=0)
    policy = make_learned_policy(str(checkpoint), Side.USSR)
    action = policy(gs.pub, gs.hands[Side.USSR], gs.ussr_holds_china)

    assert action is None or isinstance(action, ActionEncoding)
