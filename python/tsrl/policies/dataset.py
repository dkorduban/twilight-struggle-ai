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

import bisect
import glob
import os
from typing import Any

import numpy as np
import polars as pl
import torch
from torch.utils.data import Dataset


class TS_SelfPlayDataset(Dataset):
    """Load Parquet files from a directory via per-file lazy caching.

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

        self._paths = paths
        self._file_lengths = [
            int(pl.scan_parquet(path).select(pl.len()).collect().item()) for path in paths
        ]
        self._cumulative = np.cumsum([0] + self._file_lengths)
        self._cache: dict[int, pl.DataFrame] = {}
        self._length = int(self._cumulative[-1])

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, idx: int) -> dict[str, Any]:
        if idx < 0:
            idx += self._length
        if idx < 0 or idx >= self._length:
            raise IndexError(idx)

        file_idx = bisect.bisect_right(self._cumulative, idx) - 1
        local_idx = idx - int(self._cumulative[file_idx])

        frame = self._cache.get(file_idx)
        if frame is None:
            frame = pl.read_parquet(self._paths[file_idx])
            self._cache[file_idx] = frame

        row = frame.row(local_idx, named=True)

        # --- influence features (168,) ---
        ussr = torch.tensor(row["ussr_influence"], dtype=torch.float32)
        us = torch.tensor(row["us_influence"], dtype=torch.float32)
        influence = torch.cat([ussr, us])  # (168,)

        # --- card features (448,) ---
        known_in = torch.tensor(row["actor_known_in"], dtype=torch.float32)
        possible = torch.tensor(row["actor_possible"], dtype=torch.float32)
        discard = torch.tensor(row["discard_mask"], dtype=torch.float32)
        removed = torch.tensor(row["removed_mask"], dtype=torch.float32)
        cards = torch.cat([known_in, possible, discard, removed])  # (448,)

        # --- scalar features (11,), normalised ---
        scalars = torch.tensor(
            [
                row["vp"] / 20.0,
                (row["defcon"] - 1) / 4.0,
                row["milops_ussr"] / 6.0,
                row["milops_us"] / 6.0,
                row["space_ussr"] / 9.0,
                row["space_us"] / 9.0,
                float(row["china_held_by"]),
                float(row["actor_holds_china"]),
                row["turn"] / 10.0,
                row["ar"] / 8.0,
                float(row["phasing"]),
            ],
            dtype=torch.float32,
        )  # (11,)

        # --- labels ---
        # card_id in data is 1..111; subtract 1 for 0-indexed CE loss
        card_target = torch.tensor(row["action_card_id"] - 1, dtype=torch.long)
        mode_target = torch.tensor(row["action_mode"], dtype=torch.long)

        # country_ops_target: per-country ops counts for country ids 1..84.
        raw_targets = row["action_targets"]
        country_ops_target = torch.zeros(84, dtype=torch.float32)
        if raw_targets:
            ids = [int(x) for x in raw_targets.split(",") if x.strip()]
            valid_ids = [i for i in ids if 1 <= i <= 84]
            for country_id in valid_ids:
                country_ops_target[country_id - 1] += 1.0

        if self._value_target_mode == "final_vp":
            # Fall back to winner_side when a file omits final_vp or a row has null.
            raw_vp = row.get("final_vp")
            if raw_vp is not None:
                value_target = torch.tensor(
                    [max(-1.0, min(1.0, float(raw_vp) / 20.0))], dtype=torch.float32
                )
            else:
                value_target = torch.tensor(
                    [float(row["winner_side"])], dtype=torch.float32
                )
        else:
            value_target = torch.tensor(
                [float(row["winner_side"])], dtype=torch.float32
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
