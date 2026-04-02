"""TSBaselineModel and architecture variants for Twilight Struggle.

Input contract
--------------
All inputs are batched tensors with shape (B, *).

  influence : (B, 172)  — concat [ussr_influence, us_influence], raw counts (86 countries × 2)
  cards     : (B, 448)  — concat [actor_known_in, actor_possible,
                                   discard_mask, removed_mask], binary
  scalars   : (B, 11)   — pre-normalised game scalars (see dataset.py)

Output contract
---------------
Returns a dict with six keys:

  card_logits    : (B, 111)  — unnormalised logits for card choice (0-indexed)
  mode_logits    : (B, 5)    — unnormalised logits for action mode
  country_logits : (B, 84)   — mixed country distribution from the strategy
                               mixture, kept for backward compatibility with
                               code that expects a single country output
  country_strategy_logits : (B, 4, 84) — per-strategy unnormalised country logits
  strategy_logits : (B, 4)   — unnormalised logits over strategy mixture weights
  value          : (B, 1)    — game value from USSR perspective, in [-1, 1]

Card index 0 corresponds to card_id 1 in the raw data (subtract 1 at
call-site before indexing).  Country index 0 corresponds to country_id 1.
"""

from __future__ import annotations

import pathlib

import torch
import torch.nn as nn


NUM_COUNTRIES = 86  # countries 0..85 (Austria=0, Taiwan=85)
NUM_STRATEGIES = 4
NUM_CARDS = 112  # card IDs 0..111, but index 0 unused; masks are len 112
NUM_PLAYABLE_CARDS = 111  # card IDs 1..111
NUM_MODES = 5
INFLUENCE_DIM = NUM_COUNTRIES * 2        # 172
CARD_DIM = NUM_CARDS * 4                 # 448
SCALAR_DIM = 11
INFLUENCE_HIDDEN = 128
CARD_HIDDEN = 128
SCALAR_HIDDEN = 64
TRUNK_IN = INFLUENCE_HIDDEN + CARD_HIDDEN + SCALAR_HIDDEN  # 320
TRUNK_HIDDEN = 256

# Static feature dimensions for embedding encoders
_CARD_FEAT_DIM = 8    # ops/4, side_ussr, side_us, era_early, era_mid, era_late, is_scoring, is_starred
_COUNTRY_FEAT_DIM = 11  # stability/4, is_bg, 7x region_onehot, us_start/3, ussr_start/3

VALUE_BRANCH_HIDDEN = 128
DEFAULT_PLATT_A = 1.0
DEFAULT_PLATT_B = 0.0

# Region ordering for onehot encoding (must be stable)
_REGIONS = ["Europe", "Asia", "MiddleEast", "Africa", "CentralAmerica", "SouthAmerica", "SoutheastAsia"]

# ---------------------------------------------------------------------------
# Static feature loaders
# ---------------------------------------------------------------------------

_SPEC_DIR = pathlib.Path(__file__).parent.parent.parent.parent / "data" / "spec"


def _build_card_features(spec_path: str | None = None) -> torch.Tensor:
    """Return (112, 8) float32 tensor of static card features.

    Rows are 0-indexed so that row i corresponds to card_id i+1.
    Row 0 (card_id 1 = Asia Scoring) through row 110 (card_id 111).
    Row index matches the bit position in the 112-wide card masks.

    Features per card:
      [0] ops / 4
      [1] side_ussr  (1 if side == 'USSR' else 0)
      [2] side_us    (1 if side == 'US' else 0)
      [3] era_early
      [4] era_mid
      [5] era_late
      [6] is_scoring
      [7] is_starred
    """
    import pandas as pd

    path = pathlib.Path(spec_path) if spec_path is not None else _SPEC_DIR / "cards.csv"
    df = pd.read_csv(path, comment="#")
    # card_id is 1-indexed; build a 112-row tensor indexed by card_id - 1
    feats = torch.zeros(112, 8, dtype=torch.float32)
    for _, row in df.iterrows():
        cid = int(row["card_id"])
        if cid < 1 or cid > 112:
            continue
        idx = cid - 1
        feats[idx, 0] = float(row["ops"]) / 4.0
        feats[idx, 1] = 1.0 if str(row["side"]).strip() == "USSR" else 0.0
        feats[idx, 2] = 1.0 if str(row["side"]).strip() == "US" else 0.0
        era = str(row["era"]).strip()
        feats[idx, 3] = 1.0 if era == "Early" else 0.0
        feats[idx, 4] = 1.0 if era == "Mid" else 0.0
        feats[idx, 5] = 1.0 if era == "Late" else 0.0
        is_scoring = str(row["is_scoring"]).strip().lower()
        feats[idx, 6] = 1.0 if is_scoring == "true" else 0.0
        is_starred = str(row["starred"]).strip().lower()
        feats[idx, 7] = 1.0 if is_starred == "true" else 0.0
    return feats


def _build_country_features(spec_path: str | None = None) -> torch.Tensor:
    """Return (86, 11) float32 tensor of static country features.

    Row i corresponds to country_id i (0-indexed, matching influence vector).

    Features per country:
      [0]    stability / 4
      [1]    is_battleground
      [2..8] region onehot: Europe, Asia, MiddleEast, Africa, CentralAmerica,
                            SouthAmerica, SoutheastAsia  (7 dims)
      [9]    us_start_influence / 3.0 (clamped to [0, 1])
      [10]   ussr_start_influence / 3.0 (clamped to [0, 1])
    """
    import pandas as pd

    path = pathlib.Path(spec_path) if spec_path is not None else _SPEC_DIR / "countries.csv"
    df = pd.read_csv(path, comment="#")
    feats = torch.zeros(86, 11, dtype=torch.float32)
    region_to_idx = {r: i for i, r in enumerate(_REGIONS)}
    for _, row in df.iterrows():
        cid = int(row["country_id"])
        if cid < 0 or cid >= 86:
            continue
        feats[cid, 0] = float(row["stability"]) / 4.0
        is_bg = str(row["is_battleground"]).strip().lower()
        feats[cid, 1] = 1.0 if is_bg == "true" else 0.0
        region = str(row["region"]).strip()
        if region in region_to_idx:
            feats[cid, 2 + region_to_idx[region]] = 1.0
        feats[cid, 9] = min(float(row["us_start_influence"]) / 3.0, 1.0)
        feats[cid, 10] = min(float(row["ussr_start_influence"]) / 3.0, 1.0)
    return feats


# Load once at module import time; encoding modules register these as buffers.
_CARD_FEATS: torch.Tensor = _build_card_features()
_COUNTRY_FEATS: torch.Tensor = _build_country_features()


# ---------------------------------------------------------------------------
# Helper: build per-region boolean index tensors (86,) for CountryEmbedEncoder
# ---------------------------------------------------------------------------

def _build_region_masks() -> list[torch.Tensor]:
    """Return 7 boolean masks of shape (86,), one per region in _REGIONS order."""
    masks = []
    for ridx, region in enumerate(_REGIONS):
        mask = _COUNTRY_FEATS[:, 2 + ridx] > 0.5  # onehot column for this region
        masks.append(mask)
    return masks


_REGION_MASKS: list[torch.Tensor] = _build_region_masks()

# ---------------------------------------------------------------------------
# Shared trunk building blocks
# ---------------------------------------------------------------------------


class PlattScaler(nn.Module):
    """Post-hoc sigmoid calibrator for value-head outputs in [-1, 1]."""

    def __init__(
        self,
        a: float = DEFAULT_PLATT_A,
        b: float = DEFAULT_PLATT_B,
    ) -> None:
        super().__init__()
        self.register_buffer("a", torch.tensor(float(a), dtype=torch.float32))
        self.register_buffer("b", torch.tensor(float(b), dtype=torch.float32))

    @property
    def is_identity(self) -> bool:
        return bool(
            torch.isclose(
                self.a,
                torch.tensor(DEFAULT_PLATT_A, dtype=self.a.dtype, device=self.a.device),
            ).item()
            and torch.isclose(
                self.b,
                torch.tensor(DEFAULT_PLATT_B, dtype=self.b.dtype, device=self.b.device),
            ).item()
        )

    def forward(self, value: torch.Tensor) -> torch.Tensor:
        if self.is_identity:
            return value
        logits = value * self.a.to(device=value.device, dtype=value.dtype)
        logits = logits + self.b.to(device=value.device, dtype=value.dtype)
        return 2.0 * torch.sigmoid(logits) - 1.0


class _ResidualBlock(nn.Module):
    """Pre-norm residual block: x = x + relu(linear(ln(x))).

    No dropout here — regularisation is handled by weight_decay + label_smoothing
    at training time.  Removing per-block dropout cuts training time ~30% with no
    measurable quality loss at this model size.
    """

    def __init__(self, dim: int) -> None:
        super().__init__()
        self.ln = nn.LayerNorm(dim)
        self.linear = nn.Linear(dim, dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + torch.relu(self.linear(self.ln(x)))


def _make_trunk_and_heads(
    hidden_dim: int, dropout: float
) -> tuple[nn.Module, nn.Module, nn.Module, nn.Module, nn.Module, nn.Module, nn.Module]:
    """Build the shared trunk + policy/value heads.

    Returns (trunk_proj, trunk_dropout, trunk_block1, trunk_block2,
             card_head, mode_head, strategy_heads, strategy_mixer,
             value_branch, value_head).
    """
    trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
    trunk_dropout = nn.Dropout(p=dropout)
    trunk_block1 = _ResidualBlock(hidden_dim)
    trunk_block2 = _ResidualBlock(hidden_dim)
    card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
    mode_head = nn.Linear(hidden_dim, NUM_MODES)
    strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
    strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)
    value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
    value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
    return (
        trunk_proj, trunk_dropout, trunk_block1, trunk_block2,
        card_head, mode_head, strategy_heads, strategy_mixer,
        value_branch, value_head,
    )


def _forward_trunk_and_heads(
    trunk_in: torch.Tensor,
    trunk_proj: nn.Linear,
    trunk_dropout: nn.Dropout,
    trunk_block1: _ResidualBlock,
    trunk_block2: _ResidualBlock,
    card_head: nn.Linear,
    mode_head: nn.Linear,
    strategy_heads: nn.Linear,
    strategy_mixer: nn.Linear,
    value_branch: nn.Linear,
    value_head: nn.Linear,
) -> dict[str, torch.Tensor]:
    """Run the shared trunk + heads and return the output dict."""
    trunk_base = trunk_dropout(torch.relu(trunk_proj(trunk_in)))
    hidden = trunk_block2(trunk_block1(trunk_base))

    card_logits = card_head(hidden)
    mode_logits = mode_head(hidden)
    country_strategy_logits = strategy_heads(hidden).view(
        hidden.shape[0], NUM_STRATEGIES, NUM_COUNTRIES
    )
    strategy_logits = strategy_mixer(hidden)
    mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
    strategy_probs = torch.softmax(country_strategy_logits, dim=2)
    country_logits = (mixing * strategy_probs).sum(dim=1)
    value = torch.tanh(value_head(torch.relu(value_branch(hidden))))

    return {
        "card_logits": card_logits,
        "mode_logits": mode_logits,
        "country_logits": country_logits,
        "country_strategy_logits": country_strategy_logits,
        "strategy_logits": strategy_logits,
        "value": value,
    }


# ---------------------------------------------------------------------------
# Encoder modules
# ---------------------------------------------------------------------------


class CardEmbedEncoder(nn.Module):
    """DeepSet encoder: embeds each card's static features, then does masked
    sum per mask type.

    Input  : cards (B, 448) — 4 × 112 binary masks concatenated
    Output : (B, CARD_HIDDEN=128)

    The 4 masks are:
      cards[:, 0:112]     = actor_known_in
      cards[:, 112:224]   = actor_possible
      cards[:, 224:336]   = discard_mask
      cards[:, 336:448]   = removed_mask

    Architecture:
      card_static : (112, 8) buffer — static card features
      card_proj   : Linear(8, embed_dim=32) — shared projection for all masks
      For each mask i in [0, 1, 2, 3]:
          embedded = relu(card_proj(card_static))  # (112, embed_dim)  [shared]
          pool_i = (mask_i.unsqueeze(-1) * embedded).sum(dim=1)  # (B, embed_dim)
      output = relu(Linear(4*embed_dim, CARD_HIDDEN)(cat([pool_0, pool_1, pool_2, pool_3])))
    """

    _EMBED_DIM = 32

    def __init__(self) -> None:
        super().__init__()
        self.register_buffer("card_static", _CARD_FEATS.clone())  # (112, 8)
        self.card_proj = nn.Linear(_CARD_FEAT_DIM, self._EMBED_DIM)
        self.out_proj = nn.Linear(4 * self._EMBED_DIM, CARD_HIDDEN)

    def forward(self, cards: torch.Tensor) -> torch.Tensor:
        # cards: (B, 448)
        # Compute shared card embeddings: (112, embed_dim)
        embedded = torch.relu(self.card_proj(self.card_static))  # (112, D)

        pools = []
        for i in range(4):
            mask_i = cards[:, i * NUM_CARDS : (i + 1) * NUM_CARDS]  # (B, 112)
            # Weighted sum: (B, 112) @ (112, D) via einsum broadcast
            pool_i = torch.matmul(mask_i, embedded)  # (B, D)
            pools.append(pool_i)

        concat = torch.cat(pools, dim=-1)  # (B, 4*D)
        return torch.relu(self.out_proj(concat))  # (B, CARD_HIDDEN)


class CountryEmbedEncoder(nn.Module):
    """Per-country MLP encoder with global + regional pooling.

    Input  : influence (B, 172) — [ussr_inf (B,86), us_inf (B,86)]
    Output : (B, INFLUENCE_HIDDEN=128)

    Architecture:
      country_static : (86, 11) buffer — static country features
      country_proj   : Linear(13, embed_dim=32)
      For each country c:
          feat_c = cat([ussr_inf[:,c]/10, us_inf[:,c]/10, country_static[c]])  (B, 13)
      per_country_out = relu(country_proj(all_feats))  # (B, 86, embed_dim)
      global_pool = per_country_out.mean(dim=1)       # (B, embed_dim)
      region_pools: mean over countries in each region, 7 pools  # (B, embed_dim) each
      output = relu(Linear((1+7)*embed_dim, INFLUENCE_HIDDEN)(cat([global_pool, *region_pools])))

    Region masks are registered as 7 boolean buffers (one per region in _REGIONS order).
    """

    _EMBED_DIM = 32
    _NUM_REGIONS = 7

    def __init__(self) -> None:
        super().__init__()
        self.register_buffer("country_static", _COUNTRY_FEATS.clone())  # (86, 11)
        # Register per-region boolean masks (86,)
        for i, mask in enumerate(_REGION_MASKS):
            self.register_buffer(f"region_mask_{i}", mask.clone())

        # per-country input: ussr_inf/10, us_inf/10, 11 static features = 13
        self.country_proj = nn.Linear(_COUNTRY_FEAT_DIM + 2, self._EMBED_DIM)
        self.out_proj = nn.Linear((1 + self._NUM_REGIONS) * self._EMBED_DIM, INFLUENCE_HIDDEN)

    def _region_mask(self, i: int) -> torch.Tensor:
        return getattr(self, f"region_mask_{i}")

    def _encode_per_country(self, influence: torch.Tensor) -> torch.Tensor:
        """Return per-country embeddings of shape (B, 86, embed_dim)."""
        B = influence.shape[0]
        ussr_inf = influence[:, :NUM_COUNTRIES] / 10.0  # (B, 86)
        us_inf = influence[:, NUM_COUNTRIES:] / 10.0    # (B, 86)
        # Expand static features: (86, 11) -> (B, 86, 11)
        static = self.country_static.unsqueeze(0).expand(B, -1, -1)
        # Stack dynamic features: (B, 86, 2)
        dyn = torch.stack([ussr_inf, us_inf], dim=-1)
        # Concatenate: (B, 86, 13)
        per_country_feats = torch.cat([dyn, static], dim=-1)
        return torch.relu(self.country_proj(per_country_feats))  # (B, 86, D)

    def forward(self, influence: torch.Tensor) -> torch.Tensor:
        per_country = self._encode_per_country(influence)  # (B, 86, D)
        global_pool = per_country.mean(dim=1)              # (B, D)

        region_pools = []
        for i in range(self._NUM_REGIONS):
            mask = self._region_mask(i)  # (86,) bool
            if mask.any():
                region_pool = per_country[:, mask, :].mean(dim=1)  # (B, D)
            else:
                # Fallback: zero pool if no countries in this region (should not happen)
                region_pool = torch.zeros(
                    per_country.shape[0], self._EMBED_DIM,
                    device=per_country.device, dtype=per_country.dtype
                )
            region_pools.append(region_pool)

        concat = torch.cat([global_pool] + region_pools, dim=-1)  # (B, 8*D)
        return torch.relu(self.out_proj(concat))  # (B, INFLUENCE_HIDDEN)


class CountryAttnEncoder(nn.Module):
    """Self-attention over per-country token embeddings.

    Same input/output contract as CountryEmbedEncoder but applies
    nn.MultiheadAttention over the 86 country tokens before pooling.

    Uses embed_dim=64 (must be divisible by num_heads=4).
    Output: (B, INFLUENCE_HIDDEN=128)
    """

    _EMBED_DIM = 64
    _NUM_HEADS = 4
    _NUM_REGIONS = 7

    def __init__(self) -> None:
        super().__init__()
        self.register_buffer("country_static", _COUNTRY_FEATS.clone())  # (86, 11)
        for i, mask in enumerate(_REGION_MASKS):
            self.register_buffer(f"region_mask_{i}", mask.clone())

        # per-country input: ussr_inf/10, us_inf/10, 11 static features = 13
        self.country_proj = nn.Linear(_COUNTRY_FEAT_DIM + 2, self._EMBED_DIM)
        self.attn = nn.MultiheadAttention(
            self._EMBED_DIM, self._NUM_HEADS, batch_first=True
        )
        self.out_proj = nn.Linear(
            (1 + self._NUM_REGIONS) * self._EMBED_DIM, INFLUENCE_HIDDEN
        )

    def _region_mask(self, i: int) -> torch.Tensor:
        return getattr(self, f"region_mask_{i}")

    def forward(self, influence: torch.Tensor) -> torch.Tensor:
        B = influence.shape[0]
        ussr_inf = influence[:, :NUM_COUNTRIES] / 10.0
        us_inf = influence[:, NUM_COUNTRIES:] / 10.0
        static = self.country_static.unsqueeze(0).expand(B, -1, -1)
        dyn = torch.stack([ussr_inf, us_inf], dim=-1)
        per_country_feats = torch.cat([dyn, static], dim=-1)  # (B, 86, 13)
        tokens = torch.relu(self.country_proj(per_country_feats))  # (B, 86, D)

        # Self-attention: (B, 86, D) -> (B, 86, D)
        attn_out, _ = self.attn(tokens, tokens, tokens)  # (B, 86, D)

        global_pool = attn_out.mean(dim=1)  # (B, D)
        region_pools = []
        for i in range(self._NUM_REGIONS):
            mask = self._region_mask(i)  # (86,) bool
            if mask.any():
                region_pool = attn_out[:, mask, :].mean(dim=1)
            else:
                region_pool = torch.zeros(
                    B, self._EMBED_DIM,
                    device=attn_out.device, dtype=attn_out.dtype
                )
            region_pools.append(region_pool)

        concat = torch.cat([global_pool] + region_pools, dim=-1)  # (B, 8*D)
        return torch.relu(self.out_proj(concat))  # (B, INFLUENCE_HIDDEN)


# ---------------------------------------------------------------------------
# Model classes
# ---------------------------------------------------------------------------


class TSBaselineModel(nn.Module):
    """Small factorised policy + value head for offline imitation learning.

    See module docstring for input/output contract.

    Architecture notes
    ------------------
    Trunk: a projection from TRUNK_IN -> hidden_dim followed by 2 pre-norm
    residual blocks (LayerNorm -> Linear -> ReLU -> Dropout, with a skip
    connection).  This gives the trunk better gradient flow than a plain MLP
    with comparable parameter count.

    Value branch: after the trunk, the value head gets a dedicated
    Linear(hidden_dim -> VALUE_BRANCH_HIDDEN) + ReLU layer before the final
    Linear(VALUE_BRANCH_HIDDEN -> 1).  This lets value specialise without
    competing for trunk capacity with the policy heads.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = nn.Linear(SCALAR_DIM, SCALAR_HIDDEN)

        # Project from TRUNK_IN -> hidden_dim, then two residual blocks.
        # Dropout is applied at the trunk input level (not per-block) to avoid
        # the ~30% training-throughput hit from per-block mask generation.
        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        # Separate value branch: trunk -> value_branch -> scalar output.
        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        """Run a forward pass.

        Parameters
        ----------
        influence:
            Float tensor of shape (B, 172).
        cards:
            Float tensor of shape (B, 448).
        scalars:
            Float tensor of shape (B, 11), already normalised.

        Returns
        -------
        dict with keys ``card_logits``, ``mode_logits``, ``country_logits``,
        ``country_strategy_logits``, ``strategy_logits``, and ``value``.
        """
        h_inf = torch.relu(self.influence_encoder(influence))
        h_card = torch.relu(self.card_encoder(cards))
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(
            hidden.shape[0], NUM_STRATEGIES, NUM_COUNTRIES
        )
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        value = torch.tanh(self.value_head(torch.relu(self.value_branch(hidden))))

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
        }


class TSCardEmbedModel(nn.Module):
    """TSBaselineModel with additive CardEmbedEncoder on top of the flat card encoder.

    Adds a DeepSet encoder alongside ``nn.Linear(CARD_DIM, CARD_HIDDEN)``
    using additive fusion: ``h_card = relu(flat(cards)) + embed(cards)``.
    This preserves the direct card-identity signal from the binary mask while
    adding structural inductive bias via per-card feature pooling.

    All other components (influence_encoder, scalar_encoder, trunk, heads)
    are identical to TSBaselineModel.

    Input/output contract: same as TSBaselineModel.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.card_encoder_flat = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.card_encoder_embed = CardEmbedEncoder()
        self.scalar_encoder = nn.Linear(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder(influence))
        # Additive fusion: flat encoder preserves card identity, embed adds structure
        h_card = torch.relu(self.card_encoder_flat(cards)) + self.card_encoder_embed(cards)
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        return _forward_trunk_and_heads(
            trunk_input,
            self.trunk_proj, self.trunk_dropout,
            self.trunk_block1, self.trunk_block2,
            self.card_head, self.mode_head,
            self.strategy_heads, self.strategy_mixer,
            self.value_branch, self.value_head,
        )


class TSCountryEmbedModel(nn.Module):
    """TSBaselineModel with additive CountryEmbedEncoder on top of the flat influence encoder.

    Adds a per-country MLP encoder alongside ``nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)``
    using additive fusion: ``h_inf = relu(flat(influence)) + embed(influence)``.
    This preserves the direct influence-count signal while adding structural
    inductive bias via per-country feature pooling with regional aggregation.

    All other components (card_encoder, scalar_encoder, trunk, heads) are
    identical to TSBaselineModel.

    Input/output contract: same as TSBaselineModel.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = CountryEmbedEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = nn.Linear(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        # Additive fusion: flat encoder preserves influence counts, embed adds structure
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + self.influence_encoder_embed(influence)
        h_card = torch.relu(self.card_encoder(cards))
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        return _forward_trunk_and_heads(
            trunk_input,
            self.trunk_proj, self.trunk_dropout,
            self.trunk_block1, self.trunk_block2,
            self.card_head, self.mode_head,
            self.strategy_heads, self.strategy_mixer,
            self.value_branch, self.value_head,
        )


class TSFullEmbedModel(nn.Module):
    """TSBaselineModel with additive CardEmbedEncoder and CountryEmbedEncoder.

    Both flat encoders are kept and augmented with structured embedding encoders
    using additive fusion (same pattern as TSCardEmbedModel + TSCountryEmbedModel).

    Input/output contract: same as TSBaselineModel.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = CountryEmbedEncoder()
        self.card_encoder_flat = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.card_encoder_embed = CardEmbedEncoder()
        self.scalar_encoder = nn.Linear(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + self.influence_encoder_embed(influence)
        h_card = torch.relu(self.card_encoder_flat(cards)) + self.card_encoder_embed(cards)
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        return _forward_trunk_and_heads(
            trunk_input,
            self.trunk_proj, self.trunk_dropout,
            self.trunk_block1, self.trunk_block2,
            self.card_head, self.mode_head,
            self.strategy_heads, self.strategy_mixer,
            self.value_branch, self.value_head,
        )


class TSCountryAttnModel(nn.Module):
    """TSBaselineModel with additive CardEmbedEncoder and CountryAttnEncoder.

    Both flat encoders are kept and augmented using additive fusion:
    - CardEmbedEncoder on top of flat card Linear
    - CountryAttnEncoder (self-attention) on top of flat influence Linear

    Input/output contract: same as TSBaselineModel.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = CountryAttnEncoder()
        self.card_encoder_flat = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.card_encoder_embed = CardEmbedEncoder()
        self.scalar_encoder = nn.Linear(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + self.influence_encoder_embed(influence)
        h_card = torch.relu(self.card_encoder_flat(cards)) + self.card_encoder_embed(cards)
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        return _forward_trunk_and_heads(
            trunk_input,
            self.trunk_proj, self.trunk_dropout,
            self.trunk_block1, self.trunk_block2,
            self.card_head, self.mode_head,
            self.strategy_heads, self.strategy_mixer,
            self.value_branch, self.value_head,
        )
