"""TS_SelfPlayDataset: PyTorch Dataset wrapping self-play Parquet files.

Each row in the Parquet files is one decision step. The dataset returns a
dict of tensors ready for the TSBaselineModel.

Returned dict keys and shapes (all float32 except the int64 *_target keys)
---------------------------------------------------------------------
  influence       : (168,)  — concat [ussr_influence, us_influence]
  cards           : (448,)  — concat [actor_known_in, actor_possible,
                                       discard_mask, removed_mask]
  scalars         : (11,)   — normalised game scalars
  card_target     : ()      — int64, 0-indexed card (action_card_id - 1)
  mode_target     : ()      — int64, action mode 0..4
  country_ops_target : (84,) — float32, per-country ops counts for country ids 1..84
                              COUP/REALIGN rows contain a single 1.0 in the target country.
                              INFLUENCE rows contain repeated counts for each allocated op.
                              SPACE/EVENT rows are all-zero and masked out in country loss.
  value_target    : (1,)    — float32, default=winner_side in {-1, 0, +1}
                              When value_target_mode='final_vp': uses final_vp/20 (clamped
                              to [-1,1]) as a denser value target. This provides more signal
                              than the sparse terminal ±1 and should improve value function
                              convergence. See TS_SelfPlayDataset(value_target_mode=...).
                              NOTE: final_vp column must exist in all Parquet files.

Scalar normalisation
--------------------
  [0]  vp / 20
  [1]  (defcon - 1) / 4
  [2]  milops_ussr / 6
  [3]  milops_us / 6
  [4]  space_ussr / 9
  [5]  space_us / 9
  [6]  china_held_by          (0 or 1, already in [0,1])
  [7]  actor_holds_china      (0 or 1)
  [8]  turn / 10
  [9]  ar / 8
  [10] phasing                (0=USSR, 1=US)
"""

from __future__ import annotations

import glob
import os
from typing import Any

import polars as pl
import torch
from torch.utils.data import Dataset


class TS_SelfPlayDataset(Dataset):
    """Load all Parquet files from a directory into a flat list of steps.

    Parameters
    ----------
    data_dir:
        Directory that contains ``*.parquet`` files produced by the
        self-play collector.
    """

    def __init__(self, data_dir: str, value_target_mode: str = "winner_side") -> None:
        """
        Parameters
        ----------
        data_dir:
            Directory containing *.parquet files.
        value_target_mode:
            'winner_side' (default) — use {-1, 0, +1} terminal outcome.
            'final_vp' — use final_vp/20 clamped to [-1, 1] as a denser
                         value target. Requires final_vp column in all files.
        """
        if value_target_mode not in ("winner_side", "final_vp"):
            raise ValueError(
                f"value_target_mode must be 'winner_side' or 'final_vp', got {value_target_mode!r}"
            )
        self._value_target_mode = value_target_mode

        paths = sorted(glob.glob(os.path.join(data_dir, "*.parquet")))
        if not paths:
            raise FileNotFoundError(
                f"No *.parquet files found in {data_dir!r}"
            )

        # Read and concatenate all Parquet files with polars (no pyarrow).
        frames = [pl.read_parquet(p) for p in paths]
        combined = pl.concat(frames, how="diagonal_relaxed")
        d = combined.to_dict(as_series=False)

        self._length = len(d["turn"])

        # ---- list-type columns: store as nested Python lists ----
        self._ussr_influence: list[list[int]] = d["ussr_influence"]
        self._us_influence: list[list[int]] = d["us_influence"]
        self._actor_known_in: list[list[int]] = d["actor_known_in"]
        self._actor_possible: list[list[int]] = d["actor_possible"]
        self._discard_mask: list[list[int]] = d["discard_mask"]
        self._removed_mask: list[list[int]] = d["removed_mask"]

        # ---- scalar columns ----
        self._vp: list[int] = d["vp"]
        self._defcon: list[int] = d["defcon"]
        self._milops_ussr: list[int] = d["milops_ussr"]
        self._milops_us: list[int] = d["milops_us"]
        self._space_ussr: list[int] = d["space_ussr"]
        self._space_us: list[int] = d["space_us"]
        self._china_held_by: list[int] = d["china_held_by"]
        self._actor_holds_china: list[bool] = d["actor_holds_china"]
        self._turn: list[int] = d["turn"]
        self._ar: list[int] = d["ar"]
        self._phasing: list[int] = d["phasing"]

        # ---- label columns ----
        self._action_card_id: list[int] = d["action_card_id"]
        self._action_mode: list[int] = d["action_mode"]
        self._action_targets: list[str] = d["action_targets"]
        self._winner_side: list[int] = d["winner_side"]
        # final_vp: the terminal VP margin (positive = USSR win).
        # Loaded only when value_target_mode='final_vp'.
        # Human-log rows may have final_vp=null (train.parquet); fall back to winner_side for those.
        if value_target_mode == "final_vp":
            # diagonal_relaxed concat fills missing final_vp with null.
            raw_final_vp = d.get("final_vp", [None] * self._length)
            # Convert None (null from polars) to None; keep integers as-is.
            self._final_vp: list[int | None] = [
                (int(v) if v is not None else None) for v in raw_final_vp
            ]

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, idx: int) -> dict[str, Any]:
        # --- influence features (168,) ---
        ussr = torch.tensor(self._ussr_influence[idx], dtype=torch.float32)
        us = torch.tensor(self._us_influence[idx], dtype=torch.float32)
        influence = torch.cat([ussr, us])  # (168,)

        # --- card features (448,) ---
        known_in = torch.tensor(self._actor_known_in[idx], dtype=torch.float32)
        possible = torch.tensor(self._actor_possible[idx], dtype=torch.float32)
        discard = torch.tensor(self._discard_mask[idx], dtype=torch.float32)
        removed = torch.tensor(self._removed_mask[idx], dtype=torch.float32)
        cards = torch.cat([known_in, possible, discard, removed])  # (448,)

        # --- scalar features (11,), normalised ---
        scalars = torch.tensor(
            [
                self._vp[idx] / 20.0,
                (self._defcon[idx] - 1) / 4.0,
                self._milops_ussr[idx] / 6.0,
                self._milops_us[idx] / 6.0,
                self._space_ussr[idx] / 9.0,
                self._space_us[idx] / 9.0,
                float(self._china_held_by[idx]),
                float(self._actor_holds_china[idx]),
                self._turn[idx] / 10.0,
                self._ar[idx] / 8.0,
                float(self._phasing[idx]),
            ],
            dtype=torch.float32,
        )  # (11,)

        # --- labels ---
        # card_id in data is 1..111; subtract 1 for 0-indexed CE loss
        card_target = torch.tensor(
            self._action_card_id[idx] - 1, dtype=torch.long
        )
        mode_target = torch.tensor(self._action_mode[idx], dtype=torch.long)

        # country_ops_target: per-country ops counts for country ids 1..84.
        raw_targets = self._action_targets[idx]
        country_ops_target = torch.zeros(84, dtype=torch.float32)
        if raw_targets:
            ids = [int(x) for x in raw_targets.split(",") if x.strip()]
            valid_ids = [i for i in ids if 1 <= i <= 84]
            for country_id in valid_ids:
                country_ops_target[country_id - 1] += 1.0

        if self._value_target_mode == "final_vp":
            # Normalize final VP to [-1, 1]: divide by 20 and clamp.
            # VP range is roughly [-20, +20] in typical games; clamping handles outliers.
            # Fall back to winner_side for rows where final_vp is null (e.g. human-log rows).
            raw_vp = self._final_vp[idx]
            if raw_vp is not None:
                value_target = torch.tensor(
                    [max(-1.0, min(1.0, float(raw_vp) / 20.0))], dtype=torch.float32
                )
            else:
                value_target = torch.tensor(
                    [float(self._winner_side[idx])], dtype=torch.float32
                )
        else:
            value_target = torch.tensor(
                [float(self._winner_side[idx])], dtype=torch.float32
            )  # (1,)

        return {
            "influence": influence,
            "cards": cards,
            "scalars": scalars,
            "card_target": card_target,
            "mode_target": mode_target,
            "country_ops_target": country_ops_target,
            "value_target": value_target,
        }
