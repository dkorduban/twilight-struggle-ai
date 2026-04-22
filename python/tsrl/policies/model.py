"""TSBaselineModel and architecture variants for Twilight Struggle.

Input contract
--------------
All inputs are batched tensors with shape (B, *).

  influence : (B, 172)  — concat [ussr_influence, us_influence], raw counts (86 countries × 2)
  cards     : (B, 448)  — concat [actor_known_in, actor_known_in,
                                   discard_mask, removed_mask], binary
  scalars   : (B, 40)   — pre-normalised game + frame-context scalars (see dataset.py)

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
import torch.nn.functional as F

from tsrl.constants import (
    BASE_SCALAR_DIM,
    CARD_DIM,
    FRAME_CONTEXT_DIM,
    INFLUENCE_DIM,
    NUM_CARDS,
    NUM_COUNTRIES,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    NUM_STRATEGIES,
    SCALAR_DIM,
    SMALL_CHOICE_MAX,  # re-exported for backward compat
)
from tsrl.policies.dp_decoder import bounded_knapsack_dp

INFLUENCE_HIDDEN = 128
CARD_HIDDEN = 128
SCALAR_HIDDEN = 64
TRUNK_IN = INFLUENCE_HIDDEN + CARD_HIDDEN + SCALAR_HIDDEN  # 320
TRUNK_HIDDEN = 256

# Static feature dimensions for embedding encoders
_CARD_FEAT_DIM = 8    # ops/4, side_ussr, side_us, era_early, era_mid, era_late, is_scoring, is_starred
_COUNTRY_FEAT_DIM = 11  # stability/4, is_bg, 7x region_onehot, us_start/3, ussr_start/3

VALUE_BRANCH_HIDDEN = 128
SIDE_EMBED_DIM = 32  # learned side embedding for side-conditional models
DEFAULT_PLATT_A = 1.0
DEFAULT_PLATT_B = 0.0

# Region ordering for onehot encoding (must be stable)
_REGIONS = ["Europe", "Asia", "MiddleEast", "Africa", "CentralAmerica", "SouthAmerica", "SoutheastAsia"]

# Per-region BG and non-BG country counts (same order as _REGIONS).
# Used to convert mean-pooled control fractions back to counts for scoring tier computation.
_REGION_BG_COUNTS:    tuple[float, ...] = (7.0, 5.0, 6.0, 7.0, 3.0, 4.0, 4.0)
_REGION_NONBG_COUNTS: tuple[float, ...] = (16.0, 2.0, 4.0, 11.0, 7.0, 6.0, 3.0)

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

# Pre-compute static tensors for control/scoring features
_STABILITY: torch.Tensor = (_COUNTRY_FEATS[:, 0] * 4.0).to(torch.float32)  # (86,) raw stability
_IS_BG: torch.Tensor = _COUNTRY_FEATS[:, 1] > 0.5  # (86,) bool

# Per-region: BG mask, total countries, total BGs (for scoring tier computation)
_REGION_BG_MASKS: list[torch.Tensor] = [
    _REGION_MASKS[i] & _IS_BG for i in range(len(_REGION_MASKS))
]
_REGION_COUNTRY_COUNTS: list[int] = [int(m.sum().item()) for m in _REGION_MASKS]
_REGION_BG_COUNTS: tuple[float, ...] = tuple(float(m.sum().item()) for m in _REGION_BG_MASKS)
_REGION_NON_BG_COUNTS: tuple[int, ...] = tuple(
    _REGION_COUNTRY_COUNTS[i] - int(_REGION_BG_COUNTS[i]) for i in range(len(_REGION_MASKS))
)


def _build_country_adjacency(spec_path: str | None = None) -> torch.Tensor:
    """Return row-normalized adjacency matrix (86, 86) from adjacency.csv.

    adj[i, j] = 1/degree_i if country j is adjacent to country i, else 0.
    Includes superpower anchor nodes (ids 81=USA, 82=USSR) in the graph.
    """
    import csv as _csv

    path = pathlib.Path(spec_path) if spec_path is not None else _SPEC_DIR / "adjacency.csv"
    adj = torch.zeros(86, 86, dtype=torch.float32)
    with open(path, newline="") as f:
        reader = _csv.reader(f)
        for raw in reader:
            row = [cell.split("#")[0].strip() for cell in raw]
            if not row or row[0] == "" or row[0].startswith("#") or row[0] == "country_a":
                continue
            a, b = int(row[0]), int(row[1])
            if 0 <= a < 86 and 0 <= b < 86:
                adj[a, b] = 1.0
                adj[b, a] = 1.0
    # Row-normalize: divide each row by its degree (number of neighbors).
    degree = adj.sum(dim=1, keepdim=True).clamp(min=1.0)
    adj = adj / degree
    return adj


_COUNTRY_ADJACENCY: torch.Tensor = _build_country_adjacency()


class FrameContextScalarEncoder(nn.Linear):
    """Linear scalar encoder that accepts old 32-wide scalar tensors.

    When old inputs or checkpoints omit the 8 frame-context columns, insert
    zero frame features after the base scalar block and set is_top_level=1.
    """
    __constants__ = ['in_features', 'out_features', '_frame_ctx_dim', '_base_scalar_dim']
    _frame_ctx_dim: int = FRAME_CONTEXT_DIM
    _base_scalar_dim: int = BASE_SCALAR_DIM

    def _pad_frame_context(self, scalars: torch.Tensor) -> torch.Tensor:
        if scalars.size(-1) == self.in_features:
            return scalars
        if scalars.size(-1) != self.in_features - self._frame_ctx_dim:
            return scalars

        frame_ctx = scalars.new_zeros((scalars.size(0), self._frame_ctx_dim))
        frame_ctx[:, self._frame_ctx_dim - 1] = 1.0
        return torch.cat(
            (
                scalars[:, :self._base_scalar_dim],
                frame_ctx,
                scalars[:, self._base_scalar_dim:],
            ),
            dim=-1,
        )

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return F.linear(self._pad_frame_context(input), self.weight, self.bias)

    def _load_from_state_dict(
        self,
        state_dict,
        prefix,
        local_metadata,
        strict,
        missing_keys,
        unexpected_keys,
        error_msgs,
    ) -> None:
        weight_key = prefix + "weight"
        if weight_key in state_dict:
            old_weight = state_dict[weight_key]
            expected_old_cols = self.weight.shape[1] - self._frame_ctx_dim
            if (
                old_weight.dim() == 2
                and old_weight.shape[0] == self.weight.shape[0]
                and old_weight.shape[1] == expected_old_cols
            ):
                new_weight = torch.zeros_like(self.weight)
                new_weight[:, :self._base_scalar_dim] = old_weight[:, :self._base_scalar_dim]
                if old_weight.shape[1] > self._base_scalar_dim:
                    suffix_cols = old_weight.shape[1] - self._base_scalar_dim
                    new_weight[
                        :,
                        self._base_scalar_dim + self._frame_ctx_dim:
                        self._base_scalar_dim + self._frame_ctx_dim + suffix_cols,
                    ] = old_weight[:, self._base_scalar_dim:]
                state_dict[weight_key] = new_weight
        super()._load_from_state_dict(
            state_dict,
            prefix,
            local_metadata,
            strict,
            missing_keys,
            unexpected_keys,
            error_msgs,
        )


@torch.jit.script
def _masked_mean_pool(x: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    """TorchScript-friendly masked mean over the country dimension."""
    mask_weight = mask.to(dtype=x.dtype).unsqueeze(0).unsqueeze(-1)
    mask_count = mask_weight.sum().clamp(min=1.0)
    return (x * mask_weight).sum(dim=1) / mask_count


@torch.jit.script
def _masked_mean_1d(x: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    """TorchScript-friendly masked mean for per-country scalar features."""
    mask_weight = mask.to(dtype=x.dtype).unsqueeze(0)
    mask_count = mask_weight.sum().clamp(min=1.0)
    return (x * mask_weight).sum(dim=1) / mask_count


@torch.jit.script
def _compute_scoring_tier(
    side_bg_frac: torch.Tensor,
    opp_bg_frac: torch.Tensor,
    side_nonbg_frac: torch.Tensor,
    opp_nonbg_frac: torch.Tensor,
    n_bg: float,
    n_nonbg: float,
) -> torch.Tensor:
    """Compute normalized scoring tier (0=none, 1/3=presence, 2/3=domination, 1=control).

    Converts mean-pooled control fractions back to counts, then applies TS scoring rules:
      Presence:   ≥1 country with influence (≥1 BG or non-BG controlled)
      Domination: more BGs + more total + ≥1 BG controlled
      Control:    all BGs + majority total

    Returns (B,) tensor with values in {0, 1/3, 2/3, 1}.
    """
    side_bg = side_bg_frac * n_bg
    opp_bg = opp_bg_frac * n_bg
    side_nonbg = side_nonbg_frac * n_nonbg
    opp_nonbg = opp_nonbg_frac * n_nonbg
    side_total = side_bg + side_nonbg
    opp_total = opp_bg + opp_nonbg

    has_presence   = (side_total >= 0.5).to(dtype=side_bg_frac.dtype)
    has_domination = (
        (side_bg > opp_bg + 0.5)           # more BGs than opponent
        & (side_total > opp_total + 0.5)   # more total than opponent
        & (side_bg >= 0.5)                 # at least 1 BG controlled
        & (side_nonbg >= 0.5)              # at least 1 non-BG controlled
    ).to(dtype=side_bg_frac.dtype)
    has_control = (
        (side_bg >= n_bg - 0.5) & (side_total > opp_total + 0.5)
    ).to(dtype=side_bg_frac.dtype)
    # dom_or_ctrl ensures control (which may not imply domination in edge cases
    # like all-BG-no-nonBG) still reaches 2/3 before adding has_control
    dom_or_ctrl = torch.maximum(has_domination, has_control)

    return (has_presence + dom_or_ctrl + has_control) / 3.0


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


def _mask_logits(logits: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    mask = mask.to(device=logits.device, dtype=torch.bool)
    if mask.shape[-1] > logits.shape[-1]:
        mask = mask[..., : logits.shape[-1]]
    if mask.shape[-1] != logits.shape[-1]:
        raise ValueError(
            f"mask width {mask.shape[-1]} does not match logits width {logits.shape[-1]}"
        )
    return logits.masked_fill(~mask, torch.finfo(logits.dtype).min)


class CountryAllocHead(nn.Module):
    """Per-country per-ops-count score head plus DP decoder.

    Scores ``score[c, k]`` represent the value of allocating ``k`` ops to
    country ``c``. The existing DP decoder consumes marginal gains, so this
    head differences adjacent allocation values before decoding.
    """

    def __init__(self, hidden_dim: int, max_ops: int = 4) -> None:
        super().__init__()
        if max_ops < 1:
            raise ValueError("max_ops must be >= 1")
        self.max_ops = int(max_ops)
        self.score_head = nn.Linear(hidden_dim, self.max_ops + 1)

    def _budget_tensor(
        self,
        budget: int | torch.Tensor,
        batch_size: int,
        device: torch.device,
    ) -> torch.Tensor:
        if isinstance(budget, torch.Tensor):
            budget_t = budget.to(device=device, dtype=torch.long)
            if budget_t.ndim == 0:
                budget_t = budget_t.expand(batch_size)
            elif budget_t.shape != (batch_size,):
                raise ValueError(
                    f"budget tensor must have shape ({batch_size},), "
                    f"got {tuple(budget_t.shape)}"
                )
            return budget_t.clamp_min(0)
        return torch.full(
            (batch_size,),
            int(budget),
            device=device,
            dtype=torch.long,
        ).clamp_min(0)

    def forward(self, country_features: torch.Tensor, budget: int | torch.Tensor) -> torch.Tensor:
        """Decode the optimal allocation counts for a fixed ops budget.

        Parameters
        ----------
        country_features:
            Float tensor of shape ``(B, n_countries, hidden_dim)``.
        budget:
            Integer ops budget, or a length-B tensor of per-sample budgets.

        Returns
        -------
        Tensor of shape ``(B, n_countries)`` with decoded allocation counts.
        """
        allocation_scores = self.score_head(country_features)  # (B, C, max_ops + 1)
        marginal_scores = allocation_scores[:, :, 1:] - allocation_scores[:, :, :-1]
        batch_size, country_count, _ = marginal_scores.shape
        budget_t = self._budget_tensor(budget, batch_size, country_features.device)
        legal_mask = torch.ones(
            batch_size,
            country_count,
            device=country_features.device,
            dtype=torch.bool,
        )
        cap = torch.full(
            (batch_size, country_count),
            self.max_ops,
            device=country_features.device,
            dtype=torch.long,
        )
        return bounded_knapsack_dp(marginal_scores, budget_t, legal_mask, cap=cap)


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
      cards[:, 112:224]   = actor_known_in (duplicate)
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
            region_pools.append(_masked_mean_pool(per_country, mask))

        concat = torch.cat([global_pool] + region_pools, dim=-1)  # (B, 8*D)
        return torch.relu(self.out_proj(concat))  # (B, INFLUENCE_HIDDEN)


class CountryAttnEncoder(nn.Module):
    """Self-attention over per-country token embeddings.

    Same input/output contract as CountryEmbedEncoder but applies
    scaled dot-product attention over the 86 country tokens before pooling.

    Uses embed_dim=64 (must be divisible by num_heads=4).
    Output: (B, INFLUENCE_HIDDEN=128)
    """

    __constants__ = ['_EMBED_DIM', '_NUM_HEADS', '_NUM_REGIONS', '_NUM_COUNTRIES']
    _EMBED_DIM = 64
    _NUM_HEADS = 4
    _NUM_REGIONS = 7
    _NUM_COUNTRIES = NUM_COUNTRIES

    def __init__(self) -> None:
        super().__init__()
        self.register_buffer("country_static", _COUNTRY_FEATS.clone())  # (86, 11)
        # Stack all region masks into one buffer (7, 86) — avoids dynamic getattr in TorchScript
        self.register_buffer("region_masks", torch.stack([m.clone() for m in _REGION_MASKS]))

        # per-country input: ussr_inf/10, us_inf/10, 11 static features = 13
        self.country_proj = nn.Linear(_COUNTRY_FEAT_DIM + 2, self._EMBED_DIM)
        # Manual QKV + F.scaled_dot_product_attention (21× faster than nn.MHA)
        self.qkv_proj = nn.Linear(self._EMBED_DIM, 3 * self._EMBED_DIM)
        self.attn_out_proj = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.out_proj = nn.Linear(
            (1 + self._NUM_REGIONS) * self._EMBED_DIM, INFLUENCE_HIDDEN
        )

    def forward(self, influence: torch.Tensor) -> torch.Tensor:
        B = influence.shape[0]
        ussr_inf = influence[:, :self._NUM_COUNTRIES] / 10.0
        us_inf = influence[:, self._NUM_COUNTRIES:] / 10.0
        static = self.country_static.unsqueeze(0).expand(B, -1, -1)
        dyn = torch.stack([ussr_inf, us_inf], dim=-1)
        per_country_feats = torch.cat([dyn, static], dim=-1)  # (B, 86, 13)
        tokens = torch.relu(self.country_proj(per_country_feats))  # (B, 86, D)

        # Self-attention via F.scaled_dot_product_attention (uses FlashAttention/efficient kernels)
        S = tokens.shape[1]  # 86
        D = self._EMBED_DIM
        H = self._NUM_HEADS
        head_dim = D // H

        qkv = self.qkv_proj(tokens)  # (B, S, 3*D)
        q, k, v = qkv.chunk(3, dim=-1)  # each (B, S, D)
        q = q.view(B, S, H, head_dim).transpose(1, 2)  # (B, H, S, head_dim)
        k = k.view(B, S, H, head_dim).transpose(1, 2)
        v = v.view(B, S, H, head_dim).transpose(1, 2)

        attn_out = F.scaled_dot_product_attention(q, k, v)  # (B, H, S, head_dim)
        attn_out = attn_out.transpose(1, 2).contiguous().view(B, S, D)  # (B, S, D)
        attn_out = self.attn_out_proj(attn_out)  # (B, S, D)

        global_pool = attn_out.mean(dim=1)  # (B, D)
        region_pools = []
        for i in range(self._NUM_REGIONS):
            mask = self.region_masks[i]  # (86,) bool
            region_pools.append(_masked_mean_pool(attn_out, mask))

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
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

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

        # SmallChoice head for event-level binary/option decisions.
        # Outputs (B, SMALL_CHOICE_MAX) logits; masked to legal options at inference.
        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

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
            Float tensor of shape (B, 40), already normalised.

        Returns
        -------
        dict with keys ``card_logits``, ``mode_logits``, ``country_logits``,
        ``country_strategy_logits``, ``strategy_logits``, ``value``,
        and ``small_choice_logits``.
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
            hidden.shape[0], 4, 86  # NUM_STRATEGIES, NUM_COUNTRIES
        )
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        value = torch.tanh(self.value_head(torch.relu(self.value_branch(hidden))))
        small_choice_logits = self.small_choice_head(hidden)

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
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
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

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
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

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
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

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


class TSDirectCountryModel(nn.Module):
    """TSBaselineModel with a single Linear country head replacing K=4 mixture-of-softmaxes.

    The K=4 mixture-of-softmaxes (strategy_heads + strategy_mixer) is replaced
    with a single ``Linear(hidden_dim, 86)`` country projection.  All other
    components (encoders, trunk, card head, mode head, value branch) are
    identical to TSBaselineModel.

    Backward-compat output contract:
      - ``country_logits``          : (B, 86) — direct head output
      - ``country_strategy_logits`` : (B, 1, 86) — unsqueezed for callers
                                       that iterate over strategies
      - ``strategy_logits``         : (B, 1) — zeros (uniform single strategy)

    Input/output contract: otherwise identical to TSBaselineModel.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        # Single direct country projection — replaces strategy_heads + strategy_mixer
        self.country_head = nn.Linear(hidden_dim, NUM_COUNTRIES)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder(influence))
        h_card = torch.relu(self.card_encoder(cards))
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_logits = self.country_head(hidden)  # (B, 86)
        # Backward-compat shims so the training loop can use the same loss code
        # country_strategy_logits: (B, 1, 86), strategy_logits: (B, 1) zeros
        country_strategy_logits = country_logits.unsqueeze(1)  # (B, 1, 86)
        strategy_logits = torch.zeros(
            hidden.shape[0], 1, device=hidden.device, dtype=hidden.dtype
        )
        value = torch.tanh(self.value_head(torch.relu(self.value_branch(hidden))))

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
        }


class TSCountryAllocHeadModel(nn.Module):
    """TSBaseline-style model with a joint country allocation head.

    The country branch predicts per-country allocation values, decodes a fixed
    max-ops allocation with ``bounded_knapsack_dp``, and exposes normalized
    decoded counts as ``country_logits`` for compatibility with existing
    country-probability consumers.
    """

    def __init__(
        self,
        dropout: float = 0.1,
        hidden_dim: int = TRUNK_HIDDEN,
        max_ops: int = 4,
    ) -> None:
        super().__init__()

        self.influence_encoder = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.country_feature_proj = nn.Linear(hidden_dim, NUM_COUNTRIES * hidden_dim)
        self.country_head = CountryAllocHead(hidden_dim, max_ops=max_ops)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
        country_budget: int | torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder(influence))
        h_card = torch.relu(self.card_encoder(cards))
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        batch_size = hidden.shape[0]
        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_features = self.country_feature_proj(hidden).view(
            batch_size, NUM_COUNTRIES, -1
        )
        budget = self.country_head.max_ops if country_budget is None else country_budget
        country_allocations = self.country_head(country_features, budget=budget)
        denom = country_allocations.sum(dim=1, keepdim=True).clamp_min(1.0)
        country_logits = country_allocations / denom
        country_strategy_logits = country_logits.unsqueeze(1)
        strategy_logits = torch.zeros(
            batch_size, 1, device=hidden.device, dtype=hidden.dtype
        )
        value = torch.tanh(self.value_head(torch.relu(self.value_branch(hidden))))
        small_choice_logits = self.small_choice_head(hidden)

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "country_allocations": country_allocations,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


# T_MAX for marginal value head: max ops value on a single country per action
_MARGINAL_T_MAX = 4


class TSMarginalValueModel(nn.Module):
    """TSBaselineModel with a marginal-value country head.

    Predicts ``delta[c, t]`` — the logit for placing the t-th influence point
    in country c.  The head is ``Linear(hidden_dim, 86 * T_MAX)`` reshaped to
    ``(B, 86, T_MAX)``.

    The country loss is replaced with a per-threshold binary cross-entropy
    over the cumulative allocation target (see train_baseline.py).  A custom
    key ``"marginal_logits"`` is added to the output dict for this loss.

    Backward-compat output contract:
      - ``country_logits``          : (B, 86) — first-threshold slice (t=0)
      - ``country_strategy_logits`` : (B, T_MAX, 86) — all thresholds,
                                       permuted for callers that iterate over K
      - ``strategy_logits``         : (B, T_MAX) — zeros
      - ``marginal_logits``         : (B, 86, T_MAX) — raw output for custom loss

    Input/output contract: otherwise identical to TSBaselineModel.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        # Marginal-value head: (B, 86 * T_MAX) -> reshape to (B, 86, T_MAX)
        self.marginal_head = nn.Linear(hidden_dim, NUM_COUNTRIES * _MARGINAL_T_MAX)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder(influence))
        h_card = torch.relu(self.card_encoder(cards))
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        marginal_logits = self.marginal_head(hidden).view(
            hidden.shape[0], NUM_COUNTRIES, _MARGINAL_T_MAX
        )  # (B, 86, T_MAX)

        # country_logits: sum sigmoid(marginal) across thresholds to get
        # expected allocation per country. This converts BCE logits to a proper
        # country preference score compatible with softmax at inference time.
        country_logits = torch.sigmoid(marginal_logits).sum(dim=-1)  # (B, 86)
        # country_strategy_logits: (B, T_MAX, 86) for compat with strategy loop
        country_strategy_logits = marginal_logits.permute(0, 2, 1)  # (B, T_MAX, 86)
        strategy_logits = torch.zeros(
            hidden.shape[0], _MARGINAL_T_MAX, device=hidden.device, dtype=hidden.dtype
        )
        value = torch.tanh(self.value_head(torch.relu(self.value_branch(hidden))))
        small_choice_logits = self.small_choice_head(hidden)

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "marginal_logits": marginal_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


class ControlFeatCountryEncoder(nn.Module):
    """CountryEmbedEncoder extended with per-country control status features.

    Adds 2 dynamic features per country:
      ussr_controls: 1.0 if ussr_inf[c] >= us_inf[c] + stability[c]
      us_controls:   1.0 if us_inf[c] >= ussr_inf[c] + stability[c]

    Also computes 14 region-scoring scalars (appended to scalar path):
      For each of 6 scoring regions: ussr_bg_controlled, us_bg_controlled,
      ussr_non_bg_controlled, us_non_bg_controlled (skipped for SoutheastAsia).
      SoutheastAsia (region 6) uses a separate rule in Shuttle Diplomacy but
      for features we treat it same as others (2 BG + 2 non-BG counts).

    Total per-country input: 2 (dynamic inf) + 11 (static) + 2 (control) = 15.
    Total extra region scalars: 7 regions × 6 = 42 (4 control counts + 2 scoring tiers).
    """

    __constants__ = ['_NUM_REGIONS', '_EMBED_DIM', '_EXTRA_COUNTRY_DIM', '_REGION_SCALAR_DIM']
    _EMBED_DIM = 32
    _NUM_REGIONS = 7
    _EXTRA_COUNTRY_DIM = 2  # ussr_controls, us_controls
    _REGION_SCALAR_DIM = 42  # 7 regions × 6 (4 counts + 2 scoring tiers)

    def __init__(self) -> None:
        super().__init__()
        self.register_buffer("country_static", _COUNTRY_FEATS.clone())  # (86, 11)
        self.register_buffer("stability", _STABILITY.clone())           # (86,)
        # Register individual region masks (backward-compat state dict layout).
        for i, mask in enumerate(_REGION_MASKS):
            self.register_buffer(f"region_mask_{i}", mask.clone())
        for i, mask in enumerate(_REGION_BG_MASKS):
            self.register_buffer(f"region_bg_mask_{i}", mask.clone())

        # per-country input: 2 inf + 11 static + 2 control = 15
        self.country_proj = nn.Linear(
            _COUNTRY_FEAT_DIM + 2 + self._EXTRA_COUNTRY_DIM, self._EMBED_DIM
        )
        self.out_proj = nn.Linear(
            (1 + self._NUM_REGIONS) * self._EMBED_DIM, INFLUENCE_HIDDEN
        )

    def _get_region_mask(self, i: int) -> torch.Tensor:
        """TorchScript-compatible region mask lookup (explicit attr access, no dynamic getattr)."""
        if i == 0:
            return self.region_mask_0  # type: ignore[attr-defined]
        elif i == 1:
            return self.region_mask_1  # type: ignore[attr-defined]
        elif i == 2:
            return self.region_mask_2  # type: ignore[attr-defined]
        elif i == 3:
            return self.region_mask_3  # type: ignore[attr-defined]
        elif i == 4:
            return self.region_mask_4  # type: ignore[attr-defined]
        elif i == 5:
            return self.region_mask_5  # type: ignore[attr-defined]
        else:
            return self.region_mask_6  # type: ignore[attr-defined]

    def _get_region_bg_mask(self, i: int) -> torch.Tensor:
        """TorchScript-compatible region BG mask lookup."""
        if i == 0:
            return self.region_bg_mask_0  # type: ignore[attr-defined]
        elif i == 1:
            return self.region_bg_mask_1  # type: ignore[attr-defined]
        elif i == 2:
            return self.region_bg_mask_2  # type: ignore[attr-defined]
        elif i == 3:
            return self.region_bg_mask_3  # type: ignore[attr-defined]
        elif i == 4:
            return self.region_bg_mask_4  # type: ignore[attr-defined]
        elif i == 5:
            return self.region_bg_mask_5  # type: ignore[attr-defined]
        else:
            return self.region_bg_mask_6  # type: ignore[attr-defined]

    def forward(self, influence: torch.Tensor) -> "tuple[torch.Tensor, torch.Tensor]":
        """Returns (influence_hidden, region_scalars).

        influence_hidden: (B, INFLUENCE_HIDDEN)
        region_scalars: (B, 42) — per-region control counts + scoring tiers for scalar path
        """
        B = influence.shape[0]
        ussr_inf = influence[:, :86]         # (B, 86) raw
        us_inf = influence[:, 86:]            # (B, 86) raw
        stab = self.stability.unsqueeze(0)               # (1, 86)

        # Control status: binary
        ussr_controls = (ussr_inf >= us_inf + stab).float()  # (B, 86)
        us_controls = (us_inf >= ussr_inf + stab).float()    # (B, 86)

        # Build per-country features: (B, 86, 15)
        static = self.country_static.unsqueeze(0).expand(B, -1, -1)  # (B, 86, 11)
        dyn = torch.stack([ussr_inf / 10.0, us_inf / 10.0], dim=-1)  # (B, 86, 2)
        ctrl = torch.stack([ussr_controls, us_controls], dim=-1)      # (B, 86, 2)
        per_country_feats = torch.cat([dyn, static, ctrl], dim=-1)    # (B, 86, 15)

        per_country = torch.relu(self.country_proj(per_country_feats))  # (B, 86, D)

        # Pooling
        global_pool = per_country.mean(dim=1)  # (B, D)
        region_pools = []
        region_scalars = []

        for i in range(self._NUM_REGIONS):
            mask = self._get_region_mask(i)       # (86,) bool
            bg_mask = self._get_region_bg_mask(i)  # (86,) bool
            non_bg_mask = mask & ~bg_mask

            region_pools.append(_masked_mean_pool(per_country, mask))

            # Region scoring scalars: controlled BG and non-BG counts per side
            ussr_bg = _masked_mean_1d(ussr_controls, bg_mask)
            us_bg = _masked_mean_1d(us_controls, bg_mask)
            ussr_non_bg = _masked_mean_1d(ussr_controls, non_bg_mask)
            us_non_bg = _masked_mean_1d(us_controls, non_bg_mask)
            region_scalars.append(ussr_bg)
            region_scalars.append(us_bg)
            region_scalars.append(ussr_non_bg)
            region_scalars.append(us_non_bg)
            # Explicit scoring tiers (0=none, 1/3=presence, 2/3=domination, 1=control)
            n_bg_f: float = float(bg_mask.float().sum())
            n_nonbg_f: float = float(non_bg_mask.float().sum())
            region_scalars.append(_compute_scoring_tier(ussr_bg, us_bg, ussr_non_bg, us_non_bg, n_bg_f, n_nonbg_f))
            region_scalars.append(_compute_scoring_tier(us_bg, ussr_bg, us_non_bg, ussr_non_bg, n_bg_f, n_nonbg_f))

        concat = torch.cat([global_pool] + region_pools, dim=-1)  # (B, 8*D)
        h_inf = torch.relu(self.out_proj(concat))  # (B, INFLUENCE_HIDDEN)
        region_scalar_tensor = torch.stack(region_scalars, dim=-1)  # (B, 42)

        return h_inf, region_scalar_tensor


class TSControlFeatModel(nn.Module):
    """Model with per-country control features and region scoring scalars.

    Uses ControlFeatCountryEncoder which adds:
    - ussr_controls / us_controls binary per-country features
    - 28 region scoring scalars (BG/non-BG controlled fractions per region per side)

    The region scalars are concatenated with the 40 base/frame scalars before
    encoding.

    Input/output contract: same as TSBaselineModel.
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_NUM_STRATEGIES', '_NUM_COUNTRIES']
    _REGION_SCALAR_DIM = 42
    _NUM_STRATEGIES = NUM_STRATEGIES
    _NUM_COUNTRIES = NUM_COUNTRIES

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = ControlFeatCountryEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)

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
        h_inf_embed, region_scalars = self.influence_encoder_embed(influence)
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + h_inf_embed

        h_card = torch.relu(self.card_encoder(cards))
        # Append region scoring scalars to base scalars
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)  # (B, 39)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(
            hidden.shape[0], self._NUM_STRATEGIES, self._NUM_COUNTRIES
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


class ControlFeatGNNEncoder(nn.Module):
    """ControlFeatCountryEncoder with 2-round graph message passing over adjacency.

    Extends ControlFeatCountryEncoder by adding two rounds of graph convolution
    after the initial per-country projection. Uses the pre-computed row-normalized
    country adjacency matrix (86×86) as a fixed buffer.

    GNN round: h_new = relu(gconv(cat([h, adj @ h], dim=-1)))
    The adjacency aggregate (adj @ h) gives each country the mean of its
    neighbors' features. Two rounds allows 2-hop information propagation.

    Output interface: same as ControlFeatCountryEncoder — returns
    (influence_hidden: (B, INFLUENCE_HIDDEN), region_scalars: (B, 42)).
    """

    __constants__ = ['_NUM_REGIONS', '_EMBED_DIM', '_EXTRA_COUNTRY_DIM', '_REGION_SCALAR_DIM']
    _EMBED_DIM = 32
    _NUM_REGIONS = 7
    _EXTRA_COUNTRY_DIM = 2
    _REGION_SCALAR_DIM = 42

    def __init__(self) -> None:
        super().__init__()
        self.register_buffer("country_static", _COUNTRY_FEATS.clone())
        self.register_buffer("stability", _STABILITY.clone())
        self.register_buffer("adjacency", _COUNTRY_ADJACENCY.clone())
        for i, mask in enumerate(_REGION_MASKS):
            self.register_buffer(f"region_mask_{i}", mask.clone())
        for i, mask in enumerate(_REGION_BG_MASKS):
            self.register_buffer(f"region_bg_mask_{i}", mask.clone())

        country_in_dim = _COUNTRY_FEAT_DIM + 2 + self._EXTRA_COUNTRY_DIM  # 15
        self.country_proj = nn.Linear(country_in_dim, self._EMBED_DIM)
        # GNN layers: input is cat([h, adj@h], dim=-1) = 2*D → D
        self.gconv1 = nn.Linear(2 * self._EMBED_DIM, self._EMBED_DIM)
        self.gconv2 = nn.Linear(2 * self._EMBED_DIM, self._EMBED_DIM)
        self.out_proj = nn.Linear(
            (1 + self._NUM_REGIONS) * self._EMBED_DIM, INFLUENCE_HIDDEN
        )

    def _get_region_mask(self, i: int) -> torch.Tensor:
        if i == 0:
            return self.region_mask_0  # type: ignore[attr-defined]
        elif i == 1:
            return self.region_mask_1  # type: ignore[attr-defined]
        elif i == 2:
            return self.region_mask_2  # type: ignore[attr-defined]
        elif i == 3:
            return self.region_mask_3  # type: ignore[attr-defined]
        elif i == 4:
            return self.region_mask_4  # type: ignore[attr-defined]
        elif i == 5:
            return self.region_mask_5  # type: ignore[attr-defined]
        else:
            return self.region_mask_6  # type: ignore[attr-defined]

    def _get_region_bg_mask(self, i: int) -> torch.Tensor:
        if i == 0:
            return self.region_bg_mask_0  # type: ignore[attr-defined]
        elif i == 1:
            return self.region_bg_mask_1  # type: ignore[attr-defined]
        elif i == 2:
            return self.region_bg_mask_2  # type: ignore[attr-defined]
        elif i == 3:
            return self.region_bg_mask_3  # type: ignore[attr-defined]
        elif i == 4:
            return self.region_bg_mask_4  # type: ignore[attr-defined]
        elif i == 5:
            return self.region_bg_mask_5  # type: ignore[attr-defined]
        else:
            return self.region_bg_mask_6  # type: ignore[attr-defined]

    def forward(self, influence: torch.Tensor) -> "tuple[torch.Tensor, torch.Tensor]":
        B = influence.shape[0]
        ussr_inf = influence[:, :86]
        us_inf = influence[:, 86:]
        stab = self.stability.unsqueeze(0)

        ussr_controls = (ussr_inf >= us_inf + stab).float()
        us_controls = (us_inf >= ussr_inf + stab).float()

        static = self.country_static.unsqueeze(0).expand(B, -1, -1)
        dyn = torch.stack([ussr_inf / 10.0, us_inf / 10.0], dim=-1)
        ctrl = torch.stack([ussr_controls, us_controls], dim=-1)
        per_country_feats = torch.cat([dyn, static, ctrl], dim=-1)

        h = torch.relu(self.country_proj(per_country_feats))  # (B, 86, D)

        # GNN round 1: aggregate neighbor features via adjacency
        h_agg1 = torch.matmul(self.adjacency, h)  # (B, 86, D)
        h = torch.relu(self.gconv1(torch.cat([h, h_agg1], dim=-1)))  # (B, 86, D)

        # GNN round 2
        h_agg2 = torch.matmul(self.adjacency, h)  # (B, 86, D)
        h = torch.relu(self.gconv2(torch.cat([h, h_agg2], dim=-1)))  # (B, 86, D)

        # Pooling (same as ControlFeatCountryEncoder)
        global_pool = h.mean(dim=1)
        region_pools = []
        region_scalars = []

        for i in range(self._NUM_REGIONS):
            mask = self._get_region_mask(i)
            bg_mask = self._get_region_bg_mask(i)
            non_bg_mask = mask & ~bg_mask

            region_pools.append(_masked_mean_pool(h, mask))

            ussr_bg = _masked_mean_1d(ussr_controls, bg_mask)
            us_bg = _masked_mean_1d(us_controls, bg_mask)
            ussr_non_bg = _masked_mean_1d(ussr_controls, non_bg_mask)
            us_non_bg = _masked_mean_1d(us_controls, non_bg_mask)
            region_scalars.append(ussr_bg)
            region_scalars.append(us_bg)
            region_scalars.append(ussr_non_bg)
            region_scalars.append(us_non_bg)
            # Explicit scoring tiers (0=none, 1/3=presence, 2/3=domination, 1=control)
            n_bg_f: float = float(bg_mask.float().sum())
            n_nonbg_f: float = float(non_bg_mask.float().sum())
            region_scalars.append(_compute_scoring_tier(ussr_bg, us_bg, ussr_non_bg, us_non_bg, n_bg_f, n_nonbg_f))
            region_scalars.append(_compute_scoring_tier(us_bg, ussr_bg, us_non_bg, ussr_non_bg, n_bg_f, n_nonbg_f))

        concat = torch.cat([global_pool] + region_pools, dim=-1)
        h_inf = torch.relu(self.out_proj(concat))
        region_scalar_tensor = torch.stack(region_scalars, dim=-1)  # (B, 42)

        return h_inf, region_scalar_tensor


class GNNMessagePasser(nn.Module):
    """Mean-aggregator message passing over the fixed country graph."""

    def __init__(self, dim: int) -> None:
        super().__init__()
        self.message_proj = nn.Linear(2 * dim, dim)

    def forward(self, tokens: torch.Tensor, adjacency: torch.Tensor) -> torch.Tensor:
        adj = adjacency.to(device=tokens.device, dtype=tokens.dtype)
        neighbor_mean = torch.matmul(adj, tokens)
        update = self.message_proj(torch.cat([tokens, neighbor_mean], dim=-1))
        return torch.relu(tokens + update)


class SelfAttnBlock(nn.Module):
    """Residual multi-head self-attention block for token encoders."""

    def __init__(self, dim: int, num_heads: int) -> None:
        super().__init__()
        if dim % num_heads != 0:
            raise ValueError("dim must be divisible by num_heads")
        self.dim = dim
        self.num_heads = num_heads
        self.qkv_proj = nn.Linear(dim, 3 * dim)
        self.attn_out = nn.Linear(dim, dim)
        self.attn_ln = nn.LayerNorm(dim)
        self.ffn_in = nn.Linear(dim, 2 * dim)
        self.ffn_out = nn.Linear(2 * dim, dim)
        self.ffn_ln = nn.LayerNorm(dim)

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        B, S, D = x.shape
        head_dim = D // self.num_heads
        return x.view(B, S, self.num_heads, head_dim).transpose(1, 2)

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        B, S, D = tokens.shape
        q, k, v = self.qkv_proj(tokens).chunk(3, dim=-1)
        attn = F.scaled_dot_product_attention(
            self._split_heads(q),
            self._split_heads(k),
            self._split_heads(v),
        )
        attn = attn.transpose(1, 2).contiguous().view(B, S, D)
        tokens = self.attn_ln(tokens + self.attn_out(attn))
        ffn = self.ffn_out(torch.relu(self.ffn_in(tokens)))
        return self.ffn_ln(tokens + ffn)


class CountryGNNAttnCLSEncoder(nn.Module):
    """Country GNN + self-attention encoder with learned CLS pooling."""

    __constants__ = ['_EMBED_DIM', '_NUM_HEADS', '_NUM_REGIONS', '_NUM_COUNTRIES']
    _EMBED_DIM = 128
    _NUM_HEADS = 4
    _NUM_REGIONS = 7
    _NUM_COUNTRIES = NUM_COUNTRIES

    def __init__(
        self,
        n_mp: int = 2,
        attn_mask_mode: str = "full",
        use_cls: bool = True,
    ) -> None:
        super().__init__()
        if n_mp not in (0, 1, 2, 3):
            raise ValueError("n_mp must be one of {0, 1, 2, 3}")
        if attn_mask_mode not in ("full", "regional_local"):
            raise ValueError("attn_mask_mode must be 'full' or 'regional_local'")

        self.n_mp = n_mp
        self.attn_mask_mode = attn_mask_mode
        self.use_cls = use_cls

        self.register_buffer("country_static", _COUNTRY_FEATS.clone())
        self.register_buffer("region_masks", torch.stack([m.clone() for m in _REGION_MASKS]))
        self.register_buffer("adjacency", _COUNTRY_ADJACENCY.clone())
        self.register_buffer("attn_mask", self._build_attn_mask())

        self.country_proj = nn.Linear(_COUNTRY_FEAT_DIM + 2, self._EMBED_DIM)
        self.mp_layers = nn.ModuleList(
            [GNNMessagePasser(self._EMBED_DIM) for _ in range(n_mp)]
        )

        self.qkv_proj = nn.Linear(self._EMBED_DIM, 3 * self._EMBED_DIM)
        self.attn_out = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.attn_ln = nn.LayerNorm(self._EMBED_DIM)

        if use_cls:
            self.cls_token = nn.Parameter(torch.zeros(1, 1, self._EMBED_DIM))
            nn.init.normal_(self.cls_token, std=0.02)
            self.cls_q_proj = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
            self.cls_kv_proj = nn.Linear(self._EMBED_DIM, 2 * self._EMBED_DIM)
            self.cls_out = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
            self.cls_ln = nn.LayerNorm(self._EMBED_DIM)

        n_pool_components = (1 if use_cls else 0) + 1 + self._NUM_REGIONS
        self.out_proj = nn.Linear(
            n_pool_components * self._EMBED_DIM,
            INFLUENCE_HIDDEN,
        )

    def _build_attn_mask(self) -> torch.Tensor:
        if self.attn_mask_mode == "full":
            return torch.ones(self._NUM_COUNTRIES, self._NUM_COUNTRIES, dtype=torch.bool)

        region_onehot = _COUNTRY_FEATS[:, 2 : 2 + self._NUM_REGIONS] > 0.5
        same_region = torch.matmul(
            region_onehot.to(torch.float32),
            region_onehot.to(torch.float32).t(),
        ) > 0
        neighbors = _COUNTRY_ADJACENCY > 0
        self_edges = torch.eye(self._NUM_COUNTRIES, dtype=torch.bool)
        return same_region | neighbors | self_edges

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        B, S, D = x.shape
        head_dim = D // self._NUM_HEADS
        return x.view(B, S, self._NUM_HEADS, head_dim).transpose(1, 2)

    def _build_tokens(self, influence: torch.Tensor) -> torch.Tensor:
        B = influence.shape[0]
        ussr_inf = influence[:, :self._NUM_COUNTRIES] / 10.0
        us_inf = influence[:, self._NUM_COUNTRIES:] / 10.0
        static = self.country_static.to(dtype=influence.dtype).unsqueeze(0).expand(B, -1, -1)
        dyn = torch.stack([ussr_inf, us_inf], dim=-1)
        per_country = torch.cat([dyn, static], dim=-1)
        return torch.relu(self.country_proj(per_country))

    def _attn(self, tokens: torch.Tensor) -> torch.Tensor:
        B, S, D = tokens.shape
        q, k, v = self.qkv_proj(tokens).chunk(3, dim=-1)
        attn_mask = self.attn_mask if self.attn_mask_mode == "regional_local" else None
        attn = F.scaled_dot_product_attention(
            self._split_heads(q),
            self._split_heads(k),
            self._split_heads(v),
            attn_mask=attn_mask,
        )
        attn = attn.transpose(1, 2).contiguous().view(B, S, D)
        return self.attn_out(attn)

    def _cls_cross_attn(self, cls: torch.Tensor, tokens: torch.Tensor) -> torch.Tensor:
        B, S, D = tokens.shape
        q = self.cls_q_proj(cls)
        k, v = self.cls_kv_proj(tokens).chunk(2, dim=-1)
        head_dim = D // self._NUM_HEADS
        q = q.view(B, 1, self._NUM_HEADS, head_dim).transpose(1, 2)
        k = k.view(B, S, self._NUM_HEADS, head_dim).transpose(1, 2)
        v = v.view(B, S, self._NUM_HEADS, head_dim).transpose(1, 2)
        attn = F.scaled_dot_product_attention(q, k, v)
        attn = attn.transpose(1, 2).contiguous().view(B, 1, D)
        return self.cls_ln(cls + self.cls_out(attn)).squeeze(1)

    def forward(self, influence: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        B = influence.shape[0]
        tokens = self._build_tokens(influence)
        for layer in self.mp_layers:
            tokens = layer(tokens, self.adjacency)

        tokens = self.attn_ln(tokens + self._attn(tokens))

        sum_pool = tokens.mean(dim=1)
        region_pools = [
            _masked_mean_pool(tokens, self.region_masks[i])
            for i in range(self._NUM_REGIONS)
        ]

        parts = []
        if self.use_cls:
            cls = self.cls_token.expand(B, -1, -1)
            parts.append(self._cls_cross_attn(cls, tokens))
        parts.append(sum_pool)
        parts.extend(region_pools)
        concat = torch.cat(parts, dim=-1)
        return torch.relu(self.out_proj(concat)), tokens


class CardCrossAttnEncoder(nn.Module):
    """Card tokens cross-attend to countries, self-attend, then CLS-pool."""

    __constants__ = ['_EMBED_DIM', '_NUM_HEADS', '_NUM_CARDS']
    _EMBED_DIM = 128
    _NUM_HEADS = 4
    _NUM_CARDS = NUM_CARDS

    def __init__(self, n_self_attn: int = 2) -> None:
        super().__init__()
        if n_self_attn not in (1, 2):
            raise ValueError("n_self_attn must be 1 or 2")
        self.register_buffer("card_static", _CARD_FEATS.clone())
        self.card_proj = nn.Linear(4 + _CARD_FEAT_DIM, self._EMBED_DIM)

        self.cross_q = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.cross_kv = nn.Linear(self._EMBED_DIM, 2 * self._EMBED_DIM)
        self.cross_out = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.cross_ln = nn.LayerNorm(self._EMBED_DIM)

        self.self_attn = nn.ModuleList(
            [SelfAttnBlock(self._EMBED_DIM, self._NUM_HEADS) for _ in range(n_self_attn)]
        )

        self.card_pool_token = nn.Parameter(torch.zeros(1, 1, self._EMBED_DIM))
        nn.init.normal_(self.card_pool_token, std=0.02)
        self.pool_q = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.pool_kv = nn.Linear(self._EMBED_DIM, 2 * self._EMBED_DIM)
        self.pool_out = nn.Linear(self._EMBED_DIM, CARD_HIDDEN)

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        B, S, D = x.shape
        head_dim = D // self._NUM_HEADS
        return x.view(B, S, self._NUM_HEADS, head_dim).transpose(1, 2)

    def _cross_attn(self, tokens: torch.Tensor, country_tokens: torch.Tensor) -> torch.Tensor:
        B, S, D = tokens.shape
        q = self.cross_q(tokens)
        k, v = self.cross_kv(country_tokens).chunk(2, dim=-1)
        attn = F.scaled_dot_product_attention(
            self._split_heads(q),
            self._split_heads(k),
            self._split_heads(v),
        )
        attn = attn.transpose(1, 2).contiguous().view(B, S, D)
        return self.cross_out(attn)

    def _pool(self, tokens: torch.Tensor) -> torch.Tensor:
        B, S, D = tokens.shape
        q = self.pool_q(self.card_pool_token.expand(B, -1, -1))
        k, v = self.pool_kv(tokens).chunk(2, dim=-1)
        attn = F.scaled_dot_product_attention(
            self._split_heads(q),
            self._split_heads(k),
            self._split_heads(v),
        )
        attn = attn.transpose(1, 2).contiguous().view(B, 1, D).squeeze(1)
        return torch.relu(self.pool_out(attn))

    def forward(
        self,
        cards: torch.Tensor,
        country_tokens: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        B = cards.shape[0]
        status = cards.to(dtype=country_tokens.dtype).reshape(B, 4, self._NUM_CARDS)
        status = status.permute(0, 2, 1)
        static = self.card_static.to(dtype=country_tokens.dtype).unsqueeze(0).expand(B, -1, -1)
        per_card = torch.cat([status, static], dim=-1)
        tokens = torch.relu(self.card_proj(per_card))

        tokens = self.cross_ln(tokens + self._cross_attn(tokens, country_tokens))
        for block in self.self_attn:
            tokens = block(tokens)

        return self._pool(tokens), tokens


class TransitionDiffHead(nn.Module):
    """Auxiliary transition-delta head conditioned on a ground-truth action."""

    _ACTION_ONE_HOT_DIM = NUM_PLAYABLE_CARDS + NUM_MODES + NUM_COUNTRIES + SMALL_CHOICE_MAX

    def __init__(self, D: int = 128, D_a: int = 64, hidden: int = 128) -> None:
        super().__init__()
        self.action_enc = nn.Linear(self._ACTION_ONE_HOT_DIM, D_a)
        self.per_country_mlp = nn.Sequential(
            nn.Linear(D + D_a, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 2),
        )
        self.global_mlp = nn.Sequential(
            nn.Linear(D + D_a, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 4),
        )

    def _coerce_action(self, a_one_hot: torch.Tensor) -> torch.Tensor:
        expected = self.action_enc.in_features
        if a_one_hot.shape[-1] == expected:
            return a_one_hot
        if a_one_hot.shape[-1] > expected:
            return a_one_hot[..., :expected]
        pad = a_one_hot.new_zeros(*a_one_hot.shape[:-1], expected - a_one_hot.shape[-1])
        return torch.cat([a_one_hot, pad], dim=-1)

    def forward(
        self,
        country_tokens: torch.Tensor,
        trunk_hidden: torch.Tensor,
        a_one_hot: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        del trunk_hidden
        B = country_tokens.shape[0]
        a = torch.relu(self.action_enc(self._coerce_action(a_one_hot)))
        a_c = a.unsqueeze(1).expand(-1, NUM_COUNTRIES, -1)
        per_c = torch.cat([country_tokens, a_c], dim=-1)
        d_influence = self.per_country_mlp(per_c)

        pooled = country_tokens.mean(dim=1)
        global_in = torch.cat([pooled, a], dim=-1)
        d_global = self.global_mlp(global_in)
        return {"d_influence": d_influence, "d_global": d_global}


class OpponentBeliefHead(nn.Module):
    """Auxiliary per-card opponent-hand belief head."""

    def __init__(self, D: int = 128, hidden: int = 64) -> None:
        super().__init__()
        self.per_card_mlp = nn.Sequential(
            nn.Linear(D, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 1),
        )

    def forward(self, card_tokens: torch.Tensor) -> torch.Tensor:
        return self.per_card_mlp(card_tokens).squeeze(-1)


class TSControlFeatGNNModel(nn.Module):
    """TSControlFeatModel with 2-round GNN over country adjacency.

    Identical to TSControlFeatModel except the influence encoder uses
    ControlFeatGNNEncoder (adds 2-round graph convolution) instead of
    ControlFeatCountryEncoder.

    Input/output contract: same as TSBaselineModel.
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_NUM_COUNTRIES', 'num_strategies']
    _REGION_SCALAR_DIM = 42
    _NUM_COUNTRIES = NUM_COUNTRIES

    def __init__(
        self,
        dropout: float = 0.1,
        hidden_dim: int = TRUNK_HIDDEN,
        num_strategies: int = NUM_STRATEGIES,
    ) -> None:
        super().__init__()

        self.num_strategies = num_strategies

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = ControlFeatGNNEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, self.num_strategies * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, self.num_strategies)

        self.value_branch = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf_embed, region_scalars = self.influence_encoder_embed(influence)
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + h_inf_embed

        h_card = torch.relu(self.card_encoder(cards))
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(
            hidden.shape[0], self.num_strategies, self._NUM_COUNTRIES
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


class TSControlFeatGNNSideModel(nn.Module):
    """TSControlFeatGNNModel with side embedding + separate value heads.

    Changes vs TSControlFeatGNNModel:
    1. A learned 32-dim side embedding (USSR=0, US=1) concatenated to trunk input.
       Side is extracted from scalars[:, 10] (already 0/1 in the dataset).
    2. Separate value heads for USSR and US — selected at forward time by side.
       This lets the model learn different value functions per side without
       the shared head trying to compromise between asymmetric objectives.

    Policy heads remain shared (both sides need to pick from the same card/mode space).
    Input/output contract: same as TSBaselineModel.
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_SIDE_SCALAR_IDX']
    _REGION_SCALAR_DIM = 42
    _SIDE_SCALAR_IDX = 10  # index into scalars tensor where side is encoded

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = ControlFeatGNNEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)

        self.side_embed = nn.Embedding(2, SIDE_EMBED_DIM)

        self.trunk_proj = nn.Linear(TRUNK_IN + SIDE_EMBED_DIM, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch_ussr = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_ussr = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
        self.value_branch_us = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_us = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

        # SmallChoice head for event-level binary/option decisions.
        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf_embed, region_scalars = self.influence_encoder_embed(influence)
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + h_inf_embed

        h_card = torch.relu(self.card_encoder(cards))
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        # Side embedding from scalar index 10 (0=USSR, 1=US)
        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side = self.side_embed(side_idx)  # (B, SIDE_EMBED_DIM)

        trunk_input = torch.cat([h_inf, h_card, h_scalar, h_side], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(
            hidden.shape[0], 4, 86
        )
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        small_choice_logits = self.small_choice_head(hidden)

        # Side-conditional value: select USSR or US head per sample
        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us = torch.tanh(self.value_head_us(torch.relu(self.value_branch_us(hidden))))
        is_us = side_idx.unsqueeze(1).float()  # (B, 1), 0 for USSR, 1 for US
        value = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


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
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM, SCALAR_HIDDEN)

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


class TSCountryAttnSideModel(nn.Module):
    """Fair attention comparison with TSControlFeatGNNSideModel.

    Matches the GNN-side model's feature set exactly:
    - Region scalars (28 dims) from ControlFeatGNNEncoder — same as GNN
    - Learned side embedding (32 dims) — same as GNN
    - Separate USSR/US value heads — same as GNN

    The ONLY difference from TSControlFeatGNNSideModel:
    - Country encoder: 4-head self-attention (CountryAttnEncoder)
      instead of 2-hop GNN message passing (ControlFeatGNNEncoder)
    - Card encoder: CardEmbedEncoder added (attention model specialty)

    This isolates the adjacency message-passing vs self-attention question.
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_SIDE_SCALAR_IDX']
    _REGION_SCALAR_DIM = 42
    _SIDE_SCALAR_IDX = 10

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        # Attention-based country encoder (produces INFLUENCE_HIDDEN output)
        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = CountryAttnEncoder()

        # Card encoder: same simple linear as GNN-side (fair comparison isolates country encoder only)
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)

        # Region scalars from GNN encoder (used for features only, not graph pass)
        # We reuse ControlFeatGNNEncoder but only take its region scalar output.
        self.region_encoder = ControlFeatGNNEncoder()

        # Scalar encoder: same input size as GNN-side (SCALAR_DIM + 42)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)

        # Side embedding: same as GNN-side
        self.side_embed = nn.Embedding(2, SIDE_EMBED_DIM)

        self.trunk_proj = nn.Linear(TRUNK_IN + SIDE_EMBED_DIM, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        # Separate value heads per side (same as GNN-side)
        self.value_branch_ussr = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_ussr = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
        self.value_branch_us = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_us = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

        # SmallChoice head for event-level binary/option decisions.
        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)
        self._last_hidden = torch.empty(0)

    def _encode_hidden(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        # Country attention encoder
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + self.influence_encoder_embed(influence)

        # Card encoder (simple linear, same as GNN-side for fair comparison)
        h_card = torch.relu(self.card_encoder(cards))

        # Region scalars from GNN encoder (graph pass output discarded, only region features kept)
        _, region_scalars = self.region_encoder(influence)

        # Scalar encoder with region scalars appended (same as GNN-side)
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        # Side embedding from scalar index 10
        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side = self.side_embed(side_idx)

        trunk_input = torch.cat([h_inf, h_card, h_scalar, h_side], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))
        return hidden, side_idx

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        hidden, side_idx = self._encode_hidden(influence, cards, scalars)
        self._last_hidden = hidden

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(hidden.shape[0], 4, 86)
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        small_choice_logits = self.small_choice_head(hidden)

        # Side-conditional value
        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us = torch.tanh(self.value_head_us(torch.relu(self.value_branch_us(hidden))))
        is_us = side_idx.unsqueeze(1).float()
        value = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


class TSCountryAttnSubframeModel(TSCountryAttnSideModel):
    """v32 side model plus a dedicated CE head for sub-frame country picks."""

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__(dropout=dropout, hidden_dim=hidden_dim)
        self.country_pick_head = nn.Linear(hidden_dim, NUM_COUNTRIES)
        nn.init.xavier_uniform_(self.country_pick_head.weight)
        nn.init.zeros_(self.country_pick_head.bias)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
        eligible_cards_mask: torch.Tensor | None = None,
        eligible_countries_mask: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        out = super().forward(influence, cards, scalars)
        out["country_pick_logits"] = self.country_pick_head(self._last_hidden)
        if eligible_cards_mask is not None:
            out["card_logits"] = _mask_logits(out["card_logits"], eligible_cards_mask)
        if eligible_countries_mask is not None:
            out["country_pick_logits"] = _mask_logits(
                out["country_pick_logits"],
                eligible_countries_mask,
            )
        return out


class TSControlFeatGNNFiLMModel(nn.Module):
    """TSControlFeatGNNSideModel with FiLM conditioning instead of side-embed concatenation.

    FiLM (Feature-wise Linear Modulation) replaces the concat side embedding with
    multiplicative + additive modulation of the trunk activations:
        gamma, beta = f(side_embedding)
        trunk = gamma * trunk + beta

    This is strictly more expressive than concatenation: FiLM can learn to conditionally
    negate/swap any trunk neuron based on side, approximating virtual feature flipping.
    With SIDE_EMBED_DIM=32 and hidden_dim=256, this adds ~16K params (vs 8K for concat).

    Input/output contract: identical to TSControlFeatGNNSideModel.
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_SIDE_SCALAR_IDX']
    _REGION_SCALAR_DIM = 42
    _SIDE_SCALAR_IDX = 10

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = ControlFeatGNNEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)

        # FiLM: side embedding projects to gamma and beta for trunk modulation
        self.side_embed = nn.Embedding(2, SIDE_EMBED_DIM)
        self.film_gamma = nn.Linear(SIDE_EMBED_DIM, hidden_dim)
        self.film_beta = nn.Linear(SIDE_EMBED_DIM, hidden_dim)

        # Trunk uses TRUNK_IN (no extra SIDE_EMBED_DIM since FiLM is post-proj)
        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch_ussr = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_ussr = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
        self.value_branch_us = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_us = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

        # Initialize FiLM to identity: gamma=1, beta=0
        nn.init.zeros_(self.film_gamma.weight)
        nn.init.ones_(self.film_gamma.bias)
        nn.init.zeros_(self.film_beta.weight)
        nn.init.zeros_(self.film_beta.bias)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf_embed, region_scalars = self.influence_encoder_embed(influence)
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + h_inf_embed

        h_card = torch.relu(self.card_encoder(cards))
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side = self.side_embed(side_idx)  # (B, SIDE_EMBED_DIM)

        # FiLM conditioning: modulate trunk activations feature-wise by side
        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        gamma = self.film_gamma(h_side)  # (B, hidden_dim)
        beta = self.film_beta(h_side)    # (B, hidden_dim)
        trunk_base = gamma * trunk_base + beta
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(
            hidden.shape[0], 4, 86
        )
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        small_choice_logits = self.small_choice_head(hidden)

        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us = torch.tanh(self.value_head_us(torch.relu(self.value_branch_us(hidden))))
        is_us = side_idx.unsqueeze(1).float()
        value = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


class TSCountryAttnFiLMModel(nn.Module):
    """TSCountryAttnSideModel with FiLM conditioning instead of side-embed concatenation.

    Same as TSControlFeatGNNFiLMModel but uses CountryAttnEncoder (self-attention)
    instead of ControlFeatGNNEncoder (graph message passing).

    Input/output contract: identical to TSCountryAttnSideModel.
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_SIDE_SCALAR_IDX']
    _REGION_SCALAR_DIM = 42
    _SIDE_SCALAR_IDX = 10

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = CountryAttnEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.region_encoder = ControlFeatGNNEncoder()
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)

        self.side_embed = nn.Embedding(2, SIDE_EMBED_DIM)
        self.film_gamma = nn.Linear(SIDE_EMBED_DIM, hidden_dim)
        self.film_beta = nn.Linear(SIDE_EMBED_DIM, hidden_dim)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch_ussr = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_ussr = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
        self.value_branch_us = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_us = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

        # Initialize FiLM to identity: gamma=1, beta=0
        nn.init.zeros_(self.film_gamma.weight)
        nn.init.ones_(self.film_gamma.bias)
        nn.init.zeros_(self.film_beta.weight)
        nn.init.zeros_(self.film_beta.bias)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + self.influence_encoder_embed(influence)
        h_card = torch.relu(self.card_encoder(cards))
        _, region_scalars = self.region_encoder(influence)
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side = self.side_embed(side_idx)

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        gamma = self.film_gamma(h_side)
        beta = self.film_beta(h_side)
        trunk_base = gamma * trunk_base + beta
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(hidden.shape[0], 4, 86)
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        small_choice_logits = self.small_choice_head(hidden)

        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us = torch.tanh(self.value_head_us(torch.relu(self.value_branch_us(hidden))))
        is_us = side_idx.unsqueeze(1).float()
        value = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


class TSCountryAttnFiLMNormalInitModel(TSCountryAttnFiLMModel):
    """TSCountryAttnFiLMModel with N(0,1e-2) FiLM weight init instead of zeros.

    Preserves the near-identity prior but eliminates the step-0 zero-gradient
    singularity on side_embed that zero-init causes.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__(dropout=dropout, hidden_dim=hidden_dim)
        nn.init.normal_(self.film_gamma.weight, 0, 1e-2)
        nn.init.ones_(self.film_gamma.bias)
        nn.init.normal_(self.film_beta.weight, 0, 1e-2)
        nn.init.zeros_(self.film_beta.bias)


class TSCountryAttnFiLMZeroBetaBiasModel(TSCountryAttnFiLMModel):
    """TSCountryAttnFiLMModel with film_beta bias removed (bias=False).

    The beta bias is a side-invariant additive offset — downstream trunk layers
    can absorb it anyway. Removing it reduces parameters by hidden_dim with no
    expressiveness loss for side conditioning.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__(dropout=dropout, hidden_dim=hidden_dim)
        self.film_beta = nn.Linear(SIDE_EMBED_DIM, hidden_dim, bias=False)
        nn.init.zeros_(self.film_beta.weight)


class TSCountryAttnFiLMGatedModel(TSCountryAttnFiLMModel):
    """TSCountryAttnFiLMModel with a learnable per-neuron gate (gated-residual FiLM).

    Forward: trunk' = trunk + gate * (gamma * trunk + beta - trunk)
    Gate initialized to sigmoid(-4) ≈ 0.018 so model starts near identity,
    but side_embed receives gradient immediately (no cold-start).
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__(dropout=dropout, hidden_dim=hidden_dim)
        self.film_gate = nn.Parameter(torch.full((hidden_dim,), -4.0))

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + self.influence_encoder_embed(influence)
        h_card = torch.relu(self.card_encoder(cards))
        _, region_scalars = self.region_encoder(influence)
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side = self.side_embed(side_idx)

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        gamma = self.film_gamma(h_side)
        beta = self.film_beta(h_side)
        gate = torch.sigmoid(self.film_gate)
        trunk_base = trunk_base + gate * (gamma * trunk_base + beta - trunk_base)
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(hidden.shape[0], 4, 86)
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        small_choice_logits = self.small_choice_head(hidden)

        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us = torch.tanh(self.value_head_us(torch.relu(self.value_branch_us(hidden))))
        is_us = side_idx.unsqueeze(1).float()
        value = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


class TSCountryAttnFiLMNormalInitZeroBetaModel(TSCountryAttnFiLMModel):
    """Combines N(0,1e-2) FiLM init with bias-free film_beta (variants A + B combined)."""

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__(dropout=dropout, hidden_dim=hidden_dim)
        self.film_beta = nn.Linear(SIDE_EMBED_DIM, hidden_dim, bias=False)
        nn.init.normal_(self.film_gamma.weight, 0, 1e-2)
        nn.init.ones_(self.film_gamma.bias)
        nn.init.normal_(self.film_beta.weight, 0, 1e-2)


class TSControlFeatGNNCardAttnModel(nn.Module):
    """GNN board encoder + card-to-country cross-attention + FiLM side conditioning.

    Extends TSControlFeatGNNFiLMModel by adding cross-attention between hand
    card embeddings and per-country board features. This lets the model learn
    card-country affinity (e.g., De Gaulle → France, Truman Doctrine → Europe).

    Cross-attention mechanism:
      Q: static card embeddings (112, D_attn) for all cards
      K, V: per-country features (B, 86, D_attn)
      Attend for cards in hand; pool result over hand → (B, CARD_HIDDEN) added to h_card

    No input/output shape change vs TSControlFeatGNNFiLMModel. ~10K extra params.
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_XATTN_DIM', '_NUM_XATTN_HEADS', '_SIDE_SCALAR_IDX', '_NUM_COUNTRIES', '_NUM_STRATEGIES', '_NUM_CARDS']
    _REGION_SCALAR_DIM = 42
    _SIDE_SCALAR_IDX = 10
    _XATTN_DIM = 32
    _NUM_XATTN_HEADS = 4
    _NUM_COUNTRIES = NUM_COUNTRIES
    _NUM_STRATEGIES = NUM_STRATEGIES
    _NUM_CARDS = NUM_CARDS

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        # Standard GNN + flat encoders
        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = ControlFeatGNNEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)

        # Cross-attention: hand cards attend to per-country board features
        self.register_buffer("card_static", _CARD_FEATS.clone())          # (112, 8)
        self.register_buffer("country_static", _COUNTRY_FEATS.clone())    # (86, 11)
        self.card_proj = nn.Linear(_CARD_FEAT_DIM, self._XATTN_DIM)       # (8 → D)
        self.country_proj = nn.Linear(_COUNTRY_FEAT_DIM + 2, self._XATTN_DIM)  # (13 → D)
        self.cross_attn = nn.MultiheadAttention(
            self._XATTN_DIM, self._NUM_XATTN_HEADS,
            batch_first=True, dropout=dropout,
        )
        # Project cross-attn output (D) to CARD_HIDDEN and add to h_card
        self.cross_attn_proj = nn.Linear(self._XATTN_DIM, CARD_HIDDEN)

        # FiLM side conditioning
        self.side_embed = nn.Embedding(2, SIDE_EMBED_DIM)
        self.film_gamma = nn.Linear(SIDE_EMBED_DIM, hidden_dim)
        self.film_beta = nn.Linear(SIDE_EMBED_DIM, hidden_dim)

        self.trunk_proj = nn.Linear(TRUNK_IN, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)

        self.value_branch_ussr = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_ussr = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
        self.value_branch_us = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_us = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

        # Init FiLM to identity: gamma=1, beta=0
        nn.init.zeros_(self.film_gamma.weight)
        nn.init.ones_(self.film_gamma.bias)
        nn.init.zeros_(self.film_beta.weight)
        nn.init.zeros_(self.film_beta.bias)

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        B = influence.shape[0]

        # Standard GNN encoders
        h_inf_embed, region_scalars = self.influence_encoder_embed(influence)
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + h_inf_embed
        h_card = torch.relu(self.card_encoder(cards))
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        # Cross-attention: per-country features (B, 86, D_attn)
        ussr_inf = influence[:, :self._NUM_COUNTRIES] / 10.0   # (B, 86)
        us_inf   = influence[:, self._NUM_COUNTRIES:] / 10.0   # (B, 86)
        static_c = self.country_static.unsqueeze(0).expand(B, -1, -1)  # (B, 86, 11)
        dyn_c    = torch.stack([ussr_inf, us_inf], dim=-1)              # (B, 86, 2)
        countries = torch.relu(
            self.country_proj(torch.cat([dyn_c, static_c], dim=-1))
        )  # (B, 86, D_attn)

        # Per-card static embeddings: (B, 112, D_attn)
        card_emb = torch.relu(self.card_proj(self.card_static))          # (112, D_attn)
        card_emb = card_emb.unsqueeze(0).expand(B, -1, -1)               # (B, 112, D_attn)

        # Cross-attention: all card embeddings attend to all countries
        attn_out, _ = self.cross_attn(card_emb, countries, countries)    # (B, 112, D_attn)

        # Pool over cards in hand (actor_known_in = first 112 cols)
        hand_mask_f = cards[:, :self._NUM_CARDS].unsqueeze(-1)                  # (B, 112, 1)
        hand_n = hand_mask_f.sum(dim=1).clamp(min=1.0)                    # (B, 1)
        attn_pool = (attn_out * hand_mask_f).sum(dim=1) / hand_n          # (B, D_attn)
        h_cross = torch.relu(self.cross_attn_proj(attn_pool))             # (B, CARD_HIDDEN)

        # Residual: add cross-attention context to card features
        h_card = h_card + h_cross

        # FiLM conditioning
        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side   = self.side_embed(side_idx)
        gamma = self.film_gamma(h_side)
        beta  = self.film_beta(h_side)

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base  = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        trunk_base  = gamma * trunk_base + beta
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits  = self.card_head(hidden)
        mode_logits  = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(B, self._NUM_STRATEGIES, self._NUM_COUNTRIES)
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        small_choice_logits = self.small_choice_head(hidden)

        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us   = torch.tanh(self.value_head_us  (torch.relu(self.value_branch_us  (hidden))))
        is_us  = side_idx.unsqueeze(1).float()
        value  = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


class TSControlFeatGNNCardAttnGatedModel(TSControlFeatGNNCardAttnModel):
    """GNN + card cross-attention + gated FiLM (combines gnn_card_attn and film_gated).

    Adds a learnable per-neuron sigmoid gate over the FiLM modulation:
        trunk' = trunk + gate * (gamma * trunk + beta - trunk)
    Gate initialized to sigmoid(-4) ≈ 0.018 so model starts near identity
    but side_embed receives gradients from iteration 1 (no cold-start).

    gnn_card_attn excels vs specialists (38.4% avg panel WR).
    film_gated excels vs heuristic (43.5%), thanks to the gate.
    This arch targets both strengths simultaneously.
    """

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__(dropout=dropout, hidden_dim=hidden_dim)
        self.film_gate = nn.Parameter(torch.full((hidden_dim,), -4.0))

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        B = influence.shape[0]

        h_inf_embed, region_scalars = self.influence_encoder_embed(influence)
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + h_inf_embed
        h_card = torch.relu(self.card_encoder(cards))
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))

        # Card-to-country cross-attention (same as parent)
        ussr_inf = influence[:, :self._NUM_COUNTRIES] / 10.0
        us_inf   = influence[:, self._NUM_COUNTRIES:] / 10.0
        static_c = self.country_static.unsqueeze(0).expand(B, -1, -1)
        dyn_c    = torch.stack([ussr_inf, us_inf], dim=-1)
        countries = torch.relu(
            self.country_proj(torch.cat([dyn_c, static_c], dim=-1))
        )
        card_emb = torch.relu(self.card_proj(self.card_static)).unsqueeze(0).expand(B, -1, -1)
        attn_out, _ = self.cross_attn(card_emb, countries, countries)
        hand_mask_f = cards[:, :self._NUM_CARDS].unsqueeze(-1)
        hand_n = hand_mask_f.sum(dim=1).clamp(min=1.0)
        attn_pool = (attn_out * hand_mask_f).sum(dim=1) / hand_n
        h_card = h_card + torch.relu(self.cross_attn_proj(attn_pool))

        # Gated FiLM conditioning
        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side   = self.side_embed(side_idx)
        gamma = self.film_gamma(h_side)
        beta  = self.film_beta(h_side)
        gate  = torch.sigmoid(self.film_gate)  # (hidden_dim,), near 0 at init

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        trunk_base  = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        trunk_base  = trunk_base + gate * (gamma * trunk_base + beta - trunk_base)
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        card_logits  = self.card_head(hidden)
        mode_logits  = self.mode_head(hidden)
        country_strategy_logits = self.strategy_heads(hidden).view(B, self._NUM_STRATEGIES, self._NUM_COUNTRIES)
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        small_choice_logits = self.small_choice_head(hidden)

        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us   = torch.tanh(self.value_head_us  (torch.relu(self.value_branch_us  (hidden))))
        is_us  = side_idx.unsqueeze(1).float()
        value  = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }


class TSCountryAttnSidePolicyModel(nn.Module):
    """Country-attention model with per-side policy heads.

    Same trunk/encoder as TSCountryAttnSideModel, but duplicates all policy
    heads (card, mode, strategy, small_choice) per side. This eliminates
    gradient interference between USSR and US policy learning while keeping
    a shared representation trunk.

    Value heads are already per-side (inherited from TSCountryAttnSideModel).
    """

    __constants__ = ['_REGION_SCALAR_DIM', '_SIDE_SCALAR_IDX']
    _REGION_SCALAR_DIM = 42
    _SIDE_SCALAR_IDX = 10

    def __init__(self, dropout: float = 0.1, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()

        # Shared encoders (identical to TSCountryAttnSideModel)
        self.influence_encoder_flat = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.influence_encoder_embed = CountryAttnEncoder()
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.region_encoder = ControlFeatGNNEncoder()
        self.scalar_encoder = FrameContextScalarEncoder(SCALAR_DIM + self._REGION_SCALAR_DIM, SCALAR_HIDDEN)
        self.side_embed = nn.Embedding(2, SIDE_EMBED_DIM)

        # Shared trunk
        self.trunk_proj = nn.Linear(TRUNK_IN + SIDE_EMBED_DIM, hidden_dim)
        self.trunk_dropout = nn.Dropout(p=dropout)
        self.trunk_block1 = _ResidualBlock(hidden_dim)
        self.trunk_block2 = _ResidualBlock(hidden_dim)

        # Shared policy heads (kept for checkpoint warm-start compatibility)
        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)
        self.small_choice_head = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

        # Per-side policy heads (USSR)
        self.card_head_ussr = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head_ussr = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads_ussr = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer_ussr = nn.Linear(hidden_dim, NUM_STRATEGIES)
        self.small_choice_head_ussr = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

        # Per-side policy heads (US)
        self.card_head_us = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head_us = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads_us = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer_us = nn.Linear(hidden_dim, NUM_STRATEGIES)
        self.small_choice_head_us = nn.Linear(hidden_dim, SMALL_CHOICE_MAX)

        # Per-side value heads
        self.value_branch_ussr = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_ussr = nn.Linear(VALUE_BRANCH_HIDDEN, 1)
        self.value_branch_us = nn.Linear(hidden_dim, VALUE_BRANCH_HIDDEN)
        self.value_head_us = nn.Linear(VALUE_BRANCH_HIDDEN, 1)

    def _init_from_shared(self) -> None:
        """Copy shared head weights to per-side heads for warm-start."""
        for suffix in ("ussr", "us"):
            for name in ("card_head", "mode_head", "strategy_heads", "strategy_mixer", "small_choice_head"):
                src = getattr(self, name)
                dst = getattr(self, f"{name}_{suffix}")
                dst.weight.data.copy_(src.weight.data)
                dst.bias.data.copy_(src.bias.data)

    def _compute_country_logits(
        self, hidden: torch.Tensor, strategy_heads: nn.Linear, strategy_mixer: nn.Linear
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        country_strategy_logits = strategy_heads(hidden).view(hidden.shape[0], 4, 86)
        strategy_logits = strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        strategy_probs = torch.softmax(country_strategy_logits, dim=2)
        country_logits = (mixing * strategy_probs).sum(dim=1)
        return country_logits, country_strategy_logits, strategy_logits

    def forward(
        self,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        # Shared trunk (identical to TSCountryAttnSideModel)
        h_inf = torch.relu(self.influence_encoder_flat(influence)) + self.influence_encoder_embed(influence)
        h_card = torch.relu(self.card_encoder(cards))
        _, region_scalars = self.region_encoder(influence)
        scalars_extended = torch.cat([scalars, region_scalars], dim=-1)
        h_scalar = torch.relu(self.scalar_encoder(scalars_extended))
        side_idx = scalars[:, self._SIDE_SCALAR_IDX].long()
        h_side = self.side_embed(side_idx)
        trunk_input = torch.cat([h_inf, h_card, h_scalar, h_side], dim=-1)
        trunk_base = self.trunk_dropout(torch.relu(self.trunk_proj(trunk_input)))
        hidden = self.trunk_block2(self.trunk_block1(trunk_base))

        # Per-side policy heads
        is_us = side_idx.unsqueeze(1).float()

        card_logits = (1.0 - is_us) * self.card_head_ussr(hidden) + is_us * self.card_head_us(hidden)
        mode_logits = (1.0 - is_us) * self.mode_head_ussr(hidden) + is_us * self.mode_head_us(hidden)
        small_choice_logits = (
            (1.0 - is_us) * self.small_choice_head_ussr(hidden)
            + is_us * self.small_choice_head_us(hidden)
        )

        cl_ussr, csl_ussr, sl_ussr = self._compute_country_logits(
            hidden, self.strategy_heads_ussr, self.strategy_mixer_ussr
        )
        cl_us, csl_us, sl_us = self._compute_country_logits(
            hidden, self.strategy_heads_us, self.strategy_mixer_us
        )
        country_logits = (1.0 - is_us) * cl_ussr + is_us * cl_us
        country_strategy_logits = (1.0 - is_us.unsqueeze(2)) * csl_ussr + is_us.unsqueeze(2) * csl_us
        strategy_logits = (1.0 - is_us) * sl_ussr + is_us * sl_us

        # Per-side value heads
        v_ussr = torch.tanh(self.value_head_ussr(torch.relu(self.value_branch_ussr(hidden))))
        v_us = torch.tanh(self.value_head_us(torch.relu(self.value_branch_us(hidden))))
        value = (1.0 - is_us) * v_ussr + is_us * v_us

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": value,
            "small_choice_logits": small_choice_logits,
        }
