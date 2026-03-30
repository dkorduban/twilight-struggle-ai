"""TS_SelfPlayDataset: PyTorch Dataset wrapping self-play Parquet files.

Each row in the Parquet files is one decision step. The dataset returns a
dict of tensors ready for the TSBaselineModel.

Returned dict keys and shapes (all float32 except the int64 *_target keys)
---------------------------------------------------------------------
  influence       : (172,)  — concat [ussr_influence, us_influence]
  cards           : (448,)  — concat [actor_known_in, actor_possible,
                                       discard_mask, removed_mask]
  scalars         : (11,)   — normalised game scalars
  card_target     : ()      — int64, 0-indexed card (action_card_id - 1)
  mode_target     : ()      — int64, action mode 0..4
  country_ops_target : (86,) — float32, per-country ops counts for country ids 0..85
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
import time

import numpy as np
import polars as pl
import torch
from torch.utils.data import Dataset


class TS_SelfPlayDataset(Dataset):
    """Load Parquet files from a directory, preloading all data into tensors.

    All rows are converted to tensors once at construction time (column-wise,
    using numpy). __getitem__ is then pure tensor indexing — ~50-100x faster
    than per-row Polars access, making the DataLoader GPU-bound rather than
    CPU-bound.

    Memory: ~3 GB for 850k rows (float32 arrays). Fits easily in Modal RAM;
    on WSL2 use num_workers=0 to avoid duplicating memory across workers.

    Parameters
    ----------
    data_dir:
        Directory that contains ``*.parquet`` files produced by the
        self-play collector.
    value_target_mode:
        'winner_side' (default) — use {-1, 0, +1} terminal outcome.
        'final_vp' — use final_vp/20 clamped to [-1, 1] as a denser
                     value target. Requires final_vp column in all files.
    """

    def __init__(self, data_dir: str, value_target_mode: str = "winner_side") -> None:
        if value_target_mode not in ("winner_side", "final_vp"):
            raise ValueError(
                f"value_target_mode must be 'winner_side' or 'final_vp', got {value_target_mode!r}"
            )

        paths = sorted(glob.glob(os.path.join(data_dir, "*.parquet")))
        if not paths:
            raise FileNotFoundError(f"No *.parquet files found in {data_dir!r}")

        t0 = time.time()
        df = pl.concat([pl.read_parquet(p) for p in paths])
        N = len(df)

        # --- influence (172,) ---
        ussr_inf = np.array(df["ussr_influence"].to_list(), dtype=np.float32)   # (N, 86)
        us_inf   = np.array(df["us_influence"].to_list(),   dtype=np.float32)   # (N, 86)
        self._influence = torch.from_numpy(np.concatenate([ussr_inf, us_inf], axis=1))  # (N, 172)

        # --- card features (448,) stored as uint8, cast to float32 at index time ---
        known_in = np.array(df["actor_known_in"].to_list(), dtype=np.uint8)   # (N, 112)
        possible = np.array(df["actor_possible"].to_list(), dtype=np.uint8)   # (N, 112)
        discard  = np.array(df["discard_mask"].to_list(),   dtype=np.uint8)   # (N, 112)
        removed  = np.array(df["removed_mask"].to_list(),   dtype=np.uint8)   # (N, 112)
        # Store as uint8 tensor (4x less RAM than float32), cast to float32 in __getitem__
        self._cards = torch.from_numpy(
            np.concatenate([known_in, possible, discard, removed], axis=1)
        )  # (N, 448) uint8

        # --- scalars (11,) — np.stack with axis=1 on 1-D arrays gives (N, 11) ---
        scalars = np.stack([
            df["vp"].cast(pl.Float32).to_numpy() / 20.0,
            (df["defcon"].cast(pl.Float32).to_numpy() - 1.0) / 4.0,
            df["milops_ussr"].cast(pl.Float32).to_numpy() / 6.0,
            df["milops_us"].cast(pl.Float32).to_numpy() / 6.0,
            df["space_ussr"].cast(pl.Float32).to_numpy() / 9.0,
            df["space_us"].cast(pl.Float32).to_numpy() / 9.0,
            df["china_held_by"].cast(pl.Float32).to_numpy(),
            df["actor_holds_china"].cast(pl.Float32).to_numpy(),
            df["turn"].cast(pl.Float32).to_numpy() / 10.0,
            df["ar"].cast(pl.Float32).to_numpy() / 8.0,
            df["phasing"].cast(pl.Float32).to_numpy(),
        ], axis=1).astype(np.float32)  # (N, 11)
        self._scalars = torch.from_numpy(scalars)

        # --- integer targets ---
        self._card_target = torch.from_numpy(
            (df["action_card_id"].to_numpy() - 1).astype(np.int64)
        )  # (N,)
        self._mode_target = torch.from_numpy(
            df["action_mode"].to_numpy().astype(np.int64)
        )  # (N,)

        # --- country ops target (86,) — parsed from comma-separated string ---
        raw_targets = df["action_targets"].to_list()
        country_ops = np.zeros((N, 86), dtype=np.float32)
        for i, raw in enumerate(raw_targets):
            if raw:
                for x in raw.split(","):
                    x = x.strip()
                    if x:
                        cid = int(x)
                        if 0 <= cid <= 85:
                            country_ops[i, cid] += 1.0
        self._country_ops = torch.from_numpy(country_ops)  # (N, 86)

        # --- value target (1,) ---
        winner_arr = df["winner_side"].cast(pl.Float32).to_numpy()  # (N,)
        if value_target_mode == "final_vp":
            final_vp_arr = np.clip(
                df["final_vp"].cast(pl.Float32).to_numpy() / 20.0, -1.0, 1.0
            )
            end_reasons = df["end_reason"].to_list()
            bad_end = np.array(
                [er in ("defcon1", "europe_control") for er in end_reasons], dtype=bool
            )
            value_arr = np.where(bad_end, winner_arr, final_vp_arr).astype(np.float32)
        else:
            value_arr = winner_arr.astype(np.float32)
        self._value = torch.from_numpy(value_arr[:, None])  # (N, 1)

        self._length = N
        elapsed = time.time() - t0
        print(f"[dataset] Loaded {N:,} rows from {len(paths)} file(s) in {elapsed:.1f}s", flush=True)

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, idx: int) -> dict:
        return {
            "influence":          self._influence[idx],
            "cards":              self._cards[idx].float(),
            "scalars":            self._scalars[idx],
            "card_target":        self._card_target[idx],
            "mode_target":        self._mode_target[idx],
            "country_ops_target": self._country_ops[idx],
            "value_target":       self._value[idx],
        }
