"""TSBaselineModel: small factorized policy/value network for Twilight Struggle.

Input contract
--------------
All inputs are batched tensors with shape (B, *).

  influence : (B, 168)  — concat [ussr_influence, us_influence], raw counts
  cards     : (B, 448)  — concat [actor_known_in, actor_possible,
                                   discard_mask, removed_mask], binary
  scalars   : (B, 11)   — pre-normalised game scalars (see dataset.py)

Output contract
---------------
Returns a dict with four keys:

  card_logits    : (B, 111)  — unnormalised logits for card choice (0-indexed)
  mode_logits    : (B, 5)    — unnormalised logits for action mode
  country_logits : (B, 84)   — unnormalised logits for primary country target
                               (used for COUP/REALIGN target and INFLUENCE
                               per-op country scoring; ignored for SPACE/EVENT)
  value          : (B, 1)    — game value from USSR perspective, in [-1, 1]

Card index 0 corresponds to card_id 1 in the raw data (subtract 1 at
call-site before indexing).  Country index 0 corresponds to country_id 1.
"""

import torch
import torch.nn as nn


NUM_COUNTRIES = 84
NUM_CARDS = 112  # card IDs 0..111, but index 0 unused; masks are len 112
NUM_PLAYABLE_CARDS = 111  # card IDs 1..111
NUM_MODES = 5
INFLUENCE_DIM = NUM_COUNTRIES * 2        # 168
CARD_DIM = NUM_CARDS * 4                 # 448
SCALAR_DIM = 11
INFLUENCE_HIDDEN = 128
CARD_HIDDEN = 128
SCALAR_HIDDEN = 64
TRUNK_IN = INFLUENCE_HIDDEN + CARD_HIDDEN + SCALAR_HIDDEN  # 320
TRUNK_HIDDEN = 256


class TSBaselineModel(nn.Module):
    """Small factorised policy + value head for offline imitation learning.

    See module docstring for input/output contract.
    """

    def __init__(self, dropout: float = 0.1) -> None:
        super().__init__()

        self.influence_encoder = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = nn.Linear(SCALAR_DIM, SCALAR_HIDDEN)

        self.trunk = nn.Sequential(
            nn.Linear(TRUNK_IN, TRUNK_HIDDEN),
            nn.ReLU(),
            nn.Linear(TRUNK_HIDDEN, TRUNK_HIDDEN),
            nn.ReLU(),
            nn.Dropout(p=dropout),
        )

        self.card_head = nn.Linear(TRUNK_HIDDEN, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(TRUNK_HIDDEN, NUM_MODES)
        self.country_head = nn.Linear(TRUNK_HIDDEN, NUM_COUNTRIES)
        self.value_head = nn.Linear(TRUNK_HIDDEN, 1)

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
            Float tensor of shape (B, 168).
        cards:
            Float tensor of shape (B, 448).
        scalars:
            Float tensor of shape (B, 11), already normalised.

        Returns
        -------
        dict with keys ``card_logits``, ``mode_logits``, ``country_logits``, ``value``.
        """
        h_inf = torch.relu(self.influence_encoder(influence))
        h_card = torch.relu(self.card_encoder(cards))
        h_scalar = torch.relu(self.scalar_encoder(scalars))

        trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
        hidden = self.trunk(trunk_input)

        card_logits = self.card_head(hidden)
        mode_logits = self.mode_head(hidden)
        country_logits = self.country_head(hidden)
        value = torch.tanh(self.value_head(hidden))

        return {
            "card_logits": card_logits,
            "mode_logits": mode_logits,
            "country_logits": country_logits,
            "value": value,
        }
