"""Shared model and checkpoint constants for Twilight Struggle RL code."""

from __future__ import annotations

NUM_COUNTRIES = 86
NUM_STRATEGIES = 4
NUM_CARDS = 112
NUM_PLAYABLE_CARDS = 111
NUM_MODES = 6  # Influence, Coup, Realign, Space, Event, OpsFirst
SMALL_CHOICE_MAX = 8
INFLUENCE_DIM = NUM_COUNTRIES * 2
CARD_DIM = NUM_CARDS * 4
SCALAR_DIM = 32
ACTION_DIM = NUM_PLAYABLE_CARDS + NUM_MODES + NUM_COUNTRIES

PANEL_WEIGHTS: dict[str, float] = {
    "v55": 0.35,
    "v54": 0.25,
    "v44": 0.20,
    "v45": 0.15,
    "v14": 0.05,
}


class _LazyModelRegistry(dict[str, type]):
    """Load model classes on first use so model.py can import scalar constants."""

    def _ensure_loaded(self) -> None:
        if dict.__len__(self) > 0:
            return

        from tsrl.policies.model import (
            TSBaselineModel,
            TSCardEmbedModel,
            TSControlFeatGNNFiLMModel,
            TSControlFeatGNNModel,
            TSControlFeatGNNSideModel,
            TSControlFeatModel,
            TSCountryAttnFiLMModel,
            TSCountryAttnModel,
            TSCountryAttnSideModel,
            TSCountryAttnSidePolicyModel,
            TSCountryEmbedModel,
            TSDirectCountryModel,
            TSFullEmbedModel,
            TSMarginalValueModel,
        )

        dict.update(
            self,
            {
                "baseline": TSBaselineModel,
                "card_embed": TSCardEmbedModel,
                "country_embed": TSCountryEmbedModel,
                "full_embed": TSFullEmbedModel,
                "country_attn": TSCountryAttnModel,
                "country_attn_side": TSCountryAttnSideModel,
                "country_attn_side_policy": TSCountryAttnSidePolicyModel,
                "country_attn_film": TSCountryAttnFiLMModel,
                "direct_country": TSDirectCountryModel,
                "marginal_value": TSMarginalValueModel,
                "control_feat": TSControlFeatModel,
                "control_feat_gnn": TSControlFeatGNNModel,
                "control_feat_gnn_side": TSControlFeatGNNSideModel,
                "control_feat_gnn_film": TSControlFeatGNNFiLMModel,
            },
        )

    def __getitem__(self, key: str) -> type:
        self._ensure_loaded()
        return dict.__getitem__(self, key)

    def get(self, key: str, default=None):
        self._ensure_loaded()
        return dict.get(self, key, default)

    def __contains__(self, key: object) -> bool:
        self._ensure_loaded()
        return dict.__contains__(self, key)

    def __iter__(self):
        self._ensure_loaded()
        return dict.__iter__(self)

    def __len__(self) -> int:
        self._ensure_loaded()
        return dict.__len__(self)

    def items(self):
        self._ensure_loaded()
        return dict.items(self)

    def keys(self):
        self._ensure_loaded()
        return dict.keys(self)

    def values(self):
        self._ensure_loaded()
        return dict.values(self)


MODEL_REGISTRY: dict[str, type] = _LazyModelRegistry()
