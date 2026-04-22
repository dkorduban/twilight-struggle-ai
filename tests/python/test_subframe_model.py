from __future__ import annotations

import torch

from tsrl.policies.model import TSCountryAttnSubframeModel


def test_subframe_model_outputs_country_pick_logits():
    model = TSCountryAttnSubframeModel().eval()
    influence = torch.zeros(2, 172)
    cards = torch.zeros(2, 448)
    scalars = torch.zeros(2, 40)
    scalars[:, 10] = torch.tensor([0.0, 1.0])
    eligible_cards = torch.ones(2, 112, dtype=torch.uint8)
    eligible_countries = torch.ones(2, 86, dtype=torch.uint8)

    with torch.no_grad():
        out = model(
            influence,
            cards,
            scalars,
            eligible_cards_mask=eligible_cards,
            eligible_countries_mask=eligible_countries,
        )

    assert out["card_logits"].shape == (2, 111)
    assert out["mode_logits"].shape == (2, 6)
    assert out["small_choice_logits"].shape == (2, 8)
    assert out["country_pick_logits"].shape == (2, 86)
