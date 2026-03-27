"""TS_SelfPlayDataset: PyTorch Dataset wrapping self-play Parquet files.

Each row in the Parquet files is one decision step. The dataset returns a
dict of tensors ready for the TSBaselineModel.

Returned dict keys and shapes (all float32 except the *_target keys)
---------------------------------------------------------------------
  influence    : (168,)  — concat [ussr_influence, us_influence]
  cards        : (448,)  — concat [actor_known_in, actor_possible,
                                    discard_mask, removed_mask]
  scalars      : (11,)   — normalised game scalars
  card_target  : ()      — int64, 0-indexed card (action_card_id - 1)
  mode_target  : ()      — int64, action mode 0..4
  value_target : (1,)    — float32, winner_side in {-1, 0, +1}

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

import pyarrow.parquet as pq
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

    def __init__(self, data_dir: str) -> None:
        paths = sorted(glob.glob(os.path.join(data_dir, "*.parquet")))
        if not paths:
            raise FileNotFoundError(
                f"No *.parquet files found in {data_dir!r}"
            )

        tables = [pq.read_table(p) for p in paths]

        # Concatenate all tables into column-oriented Python lists for fast
        # indexed access.  Parquet files are small (month-1 corpus), so
        # materialising everything in RAM is fine.
        import pyarrow as pa

        combined = pa.concat_tables(tables)
        d = combined.to_pydict()

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
        self._winner_side: list[int] = d["winner_side"]

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
        value_target = torch.tensor(
            [float(self._winner_side[idx])], dtype=torch.float32
        )  # (1,)

        return {
            "influence": influence,
            "cards": cards,
            "scalars": scalars,
            "card_target": card_target,
            "mode_target": mode_target,
            "value_target": value_target,
        }
