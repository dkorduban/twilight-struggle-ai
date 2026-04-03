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
from pathlib import Path

import numpy as np
import polars as pl
import torch
from torch.utils.data import Dataset

_TEACHER_CARD_TARGET_SIZE = 111
_TEACHER_MODE_TARGET_SIZE = 5


def _load_teacher_targets(teacher_targets_path: str) -> pl.DataFrame:
    path = Path(teacher_targets_path)
    if path.is_file():
        paths = [path]
    elif path.is_dir():
        paths = sorted(
            p
            for p in path.iterdir()
            if p.is_file() and p.suffix.lower() in {".parquet", ".jsonl", ".ndjson"}
        )
        if not paths:
            raise FileNotFoundError(
                "No teacher target files (*.parquet, *.jsonl, *.ndjson) found in "
                f"{teacher_targets_path!r}"
            )
    else:
        raise FileNotFoundError(teacher_targets_path)

    frames: list[pl.DataFrame] = []
    for teacher_path in paths:
        suffix = teacher_path.suffix.lower()
        if suffix == ".parquet":
            frame = pl.read_parquet(str(teacher_path))
        elif suffix in {".jsonl", ".ndjson"}:
            frame = pl.read_ndjson(str(teacher_path))
        else:
            raise ValueError(f"Unsupported teacher target format: {teacher_path}")
        frames.append(frame)

    teacher_df = pl.concat(frames, how="vertical_relaxed") if len(frames) > 1 else frames[0]
    if "step_idx" in teacher_df.columns:
        teacher_step_col = "step_idx"
    elif "step_index" in teacher_df.columns:
        teacher_step_col = "step_index"
    else:
        raise ValueError("Teacher targets must contain 'step_index' or 'step_idx'")

    required_cols = {
        "game_id",
        teacher_step_col,
        "teacher_card_target",
        "teacher_mode_target",
        "teacher_value_target",
    }
    missing = required_cols.difference(teacher_df.columns)
    if missing:
        raise ValueError(f"Teacher targets missing required columns: {sorted(missing)}")

    teacher_df = teacher_df.select(
        pl.col("game_id").cast(pl.String),
        pl.col(teacher_step_col).cast(pl.Int64).alias("step_idx"),
        pl.col("teacher_card_target").cast(pl.List(pl.Float32)),
        pl.col("teacher_mode_target").cast(pl.List(pl.Float32)),
        pl.col("teacher_value_target").cast(pl.Float32),
    )

    dupes = teacher_df.group_by(["game_id", "step_idx"]).len().filter(pl.col("len") > 1)
    if len(dupes) > 0:
        duped = dupes.row(0, named=True)
        raise ValueError(
            "Teacher targets contain duplicate keys for "
            f"game_id={duped['game_id']!r}, step_idx={duped['step_idx']}"
        )

    return teacher_df


class TS_SelfPlayDataset(Dataset):
    """Load Parquet files from a directory, preloading all data into tensors.

    All rows are converted to tensors once at construction time (column-wise,
    using numpy). __getitems__ (PyTorch 2.0+ batch indexing) is used for a
    single vectorised tensor slice per batch, replacing 8192 individual
    __getitem__ calls and cutting per-step CPU overhead ~4-8x.

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

    def __init__(
        self,
        data_dir: str,
        value_target_mode: str = "winner_side",
        teacher_targets_path: str | None = None,
    ) -> None:
        if value_target_mode not in ("winner_side", "final_vp"):
            raise ValueError(
                f"value_target_mode must be 'winner_side' or 'final_vp', got {value_target_mode!r}"
            )

        paths = sorted(glob.glob(os.path.join(data_dir, "*.parquet")))
        if not paths:
            raise FileNotFoundError(f"No *.parquet files found in {data_dir!r}")

        t0 = time.time()

        # Only read columns the model actually needs — cuts memory ~60-70%
        # when parquet files have 75 columns but model uses ~24.
        _NEEDED_COLS = {
            # influence
            "ussr_influence", "us_influence",
            # card features
            "actor_known_in", "actor_possible", "discard_mask", "removed_mask",
            # scalars
            "vp", "defcon", "milops_ussr", "milops_us",
            "space_ussr", "space_us", "china_held_by", "actor_holds_china",
            "turn", "ar", "phasing",
            # targets
            "action_card_id", "action_mode", "action_targets",
            # value targets
            "winner_side", "final_vp", "end_reason",
            # teacher join keys
            "game_id", "step_idx",
        }

        def _read_slim(p: str) -> pl.DataFrame:
            """Read only needed columns from a parquet file."""
            available = set(pl.read_parquet_schema(p).keys())
            cols = sorted(_NEEDED_COLS & available)
            return pl.read_parquet(p, columns=cols)

        frames = [_read_slim(p) for p in paths]
        # Normalise column order before concat — files may have different
        # column sets (e.g. older data lacks full-state columns). Use the
        # intersection so all frames share the same schema.
        col_sets = [set(f.columns) for f in frames]
        common = col_sets[0]
        for s in col_sets[1:]:
            common &= s
        canonical = [c for c in frames[0].columns if c in common]
        frames = [f.select(canonical) for f in frames]

        # Normalise list/array column schemas: C++ JSONL→Parquet emits
        # Array(Int32, N) while Python collectors emit List(Int64).
        # Cast everything to List(Int32) so pl.concat doesn't fail.
        _LIST_COLS = [
            "ussr_influence",
            "us_influence",
            "discard_mask",
            "removed_mask",
            "actor_known_in",
            "actor_known_not_in",
            "actor_possible",
            "opp_known_in",
            "opp_known_not_in",
            "opp_possible",
            "lbl_actor_hand",
            "lbl_card_quality",
            "lbl_opponent_possible",
        ]

        def _normalize_frame(f: pl.DataFrame) -> pl.DataFrame:
            casts = []
            for col in _LIST_COLS:
                if col in f.columns:
                    casts.append(pl.col(col).cast(pl.List(pl.Int32)).alias(col))
            return f.with_columns(casts) if casts else f

        frames = [_normalize_frame(f) for f in frames]

        df = pl.concat(frames, how="vertical_relaxed")
        del frames  # free individual frame memory

        # Filter out setup-influence rows (card_id=0) — these aren't card-play
        # decisions and would produce target=-1 after the card_id-1 transform.
        if "action_card_id" in df.columns:
            n_before = len(df)
            df = df.filter(pl.col("action_card_id") > 0)
            n_dropped = n_before - len(df)
            if n_dropped > 0:
                print(f"[dataset] Dropped {n_dropped:,} setup-influence rows (card_id=0)")
        if teacher_targets_path is not None:
            if "game_id" not in df.columns or "step_idx" not in df.columns:
                raise ValueError(
                    "Teacher targets require training rows to include 'game_id' and 'step_idx'"
                )
            teacher_df = _load_teacher_targets(teacher_targets_path)
            df = df.join(teacher_df, on=["game_id", "step_idx"], how="left")
        N = len(df)

        # --- influence (172,) ---
        ussr_inf = np.array(df["ussr_influence"].to_list(), dtype=np.float32)  # (N, 86)
        us_inf = np.array(df["us_influence"].to_list(), dtype=np.float32)  # (N, 86)
        self._influence = torch.from_numpy(np.concatenate([ussr_inf, us_inf], axis=1))  # (N, 172)
        del ussr_inf, us_inf

        # --- card features (448,) stored as uint8, cast to float32 at index time ---
        known_in = np.array(df["actor_known_in"].to_list(), dtype=np.uint8)  # (N, 112)
        possible = np.array(df["actor_possible"].to_list(), dtype=np.uint8)  # (N, 112)
        discard = np.array(df["discard_mask"].to_list(), dtype=np.uint8)  # (N, 112)
        removed = np.array(df["removed_mask"].to_list(), dtype=np.uint8)  # (N, 112)
        # Store as uint8 tensor (4x less RAM than float32), cast to float32 in __getitem__
        self._cards = torch.from_numpy(
            np.concatenate([known_in, possible, discard, removed], axis=1)
        )  # (N, 448) uint8
        del known_in, possible, discard, removed

        # --- scalars (11,) — np.stack with axis=1 on 1-D arrays gives (N, 11) ---
        scalars = np.stack(
            [
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
            ],
            axis=1,
        ).astype(np.float32)  # (N, 11)
        self._scalars = torch.from_numpy(scalars)

        # --- integer targets ---
        self._card_target = torch.from_numpy(
            (df["action_card_id"].to_numpy() - 1).astype(np.int64)
        )  # (N,)
        self._mode_target = torch.from_numpy(df["action_mode"].to_numpy().astype(np.int64))  # (N,)

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
            final_vp_arr = np.clip(df["final_vp"].cast(pl.Float32).to_numpy() / 20.0, -1.0, 1.0)
            end_reasons = df["end_reason"].to_list()
            bad_end = np.array(
                [er in ("defcon1", "europe_control") for er in end_reasons], dtype=bool
            )
            value_arr = np.where(bad_end, winner_arr, final_vp_arr).astype(np.float32)
        else:
            value_arr = winner_arr.astype(np.float32)
        self._value = torch.from_numpy(value_arr[:, None])  # (N, 1)

        self._has_teacher: torch.Tensor | None = None
        self._teacher_card: torch.Tensor | None = None
        self._teacher_mode: torch.Tensor | None = None
        self._teacher_value: torch.Tensor | None = None
        if teacher_targets_path is not None:
            teacher_card_rows = df["teacher_card_target"].to_list()
            teacher_mode_rows = df["teacher_mode_target"].to_list()
            teacher_value_rows = df["teacher_value_target"].to_list()
            has_teacher = np.array(
                [
                    card is not None and mode is not None and value is not None
                    for card, mode, value in zip(
                        teacher_card_rows,
                        teacher_mode_rows,
                        teacher_value_rows,
                        strict=True,
                    )
                ],
                dtype=bool,
            )

            teacher_card = np.zeros((N, _TEACHER_CARD_TARGET_SIZE), dtype=np.float32)
            teacher_mode = np.zeros((N, _TEACHER_MODE_TARGET_SIZE), dtype=np.float32)
            teacher_value = np.zeros((N, 1), dtype=np.float32)
            for row_idx, (card, mode, value, present) in enumerate(
                zip(
                    teacher_card_rows,
                    teacher_mode_rows,
                    teacher_value_rows,
                    has_teacher,
                    strict=True,
                )
            ):
                if not present:
                    continue
                if len(card) != _TEACHER_CARD_TARGET_SIZE:
                    raise ValueError(
                        f"teacher_card_target row {row_idx} has len={len(card)}; "
                        f"expected {_TEACHER_CARD_TARGET_SIZE}"
                    )
                if len(mode) != _TEACHER_MODE_TARGET_SIZE:
                    raise ValueError(
                        f"teacher_mode_target row {row_idx} has len={len(mode)}; "
                        f"expected {_TEACHER_MODE_TARGET_SIZE}"
                    )
                teacher_card[row_idx] = np.asarray(card, dtype=np.float32)
                teacher_mode[row_idx] = np.asarray(mode, dtype=np.float32)
                teacher_value[row_idx, 0] = np.float32(value)

            self._has_teacher = torch.from_numpy(has_teacher)
            self._teacher_card = torch.from_numpy(teacher_card)
            self._teacher_mode = torch.from_numpy(teacher_mode)
            self._teacher_value = torch.from_numpy(teacher_value)

        # Store game_id for deterministic train/val splitting by game.
        if "game_id" in canonical:
            self._game_ids = df["game_id"].to_numpy().copy()
        else:
            self._game_ids = None

        # Free DataFrame — all data is now in tensors
        del df

        self._length = N
        elapsed = time.time() - t0
        print(
            f"[dataset] Loaded {N:,} rows from {len(paths)} file(s) in {elapsed:.1f}s",
            flush=True,
        )

    def deterministic_split(self, val_fraction: float = 0.05) -> tuple[list[int], list[int]]:
        """Split into train/val by hashing game_id — deterministic regardless of seed.

        Returns (train_indices, val_indices).  Every row from a given game goes
        entirely into train or entirely into val, so there is no cross-game leakage.
        """
        if self._game_ids is None:
            raise RuntimeError("Cannot split by game_id: column not in data")
        import hashlib
        # Assign each unique game to val if hash(game_id) mod 1/fraction < 1
        denominator = max(1, round(1.0 / val_fraction))
        unique_ids = set(self._game_ids.tolist())
        val_games = set()
        for gid in unique_ids:
            h = int(hashlib.md5(str(gid).encode()).hexdigest(), 16)
            if h % denominator == 0:
                val_games.add(gid)
        train_idx = []
        val_idx = []
        for i, gid in enumerate(self._game_ids.tolist()):
            if gid in val_games:
                val_idx.append(i)
            else:
                train_idx.append(i)
        return train_idx, val_idx

    @staticmethod
    def passthrough_collate(batch: dict) -> dict:
        """collate_fn for DataLoader — pass the pre-batched dict straight through.

        Must be used whenever creating a DataLoader over TS_SelfPlayDataset so that
        the pre-batched dict returned by __getitems__ is not re-collated.

        Usage::

            loader = DataLoader(ds, batch_size=N, collate_fn=TS_SelfPlayDataset.passthrough_collate)
        """
        return batch

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, idx: int) -> dict:
        item = {
            "influence": self._influence[idx],
            # uint8; cast to float32 on GPU in training loop
            "cards": self._cards[idx],
            "scalars": self._scalars[idx],
            "card_target": self._card_target[idx],
            "mode_target": self._mode_target[idx],
            "country_ops_target": self._country_ops[idx],
            "value_target": self._value[idx],
        }

        if self._has_teacher is not None:
            item["has_teacher_target"] = self._has_teacher[idx]
            item["teacher_card_target"] = self._teacher_card[idx]
            item["teacher_mode_target"] = self._teacher_mode[idx]
            item["teacher_value_target"] = self._teacher_value[idx]
        return item

    def __getitems__(self, indices: list) -> dict:
        """Batch indexing: one vectorised tensor slice instead of len(indices) __getitem__ calls.

        PyTorch DataLoader calls this when available (PyTorch 2.0+), replacing the default
        loop of individual __getitem__ calls + collation.  For batch_size=8192 this turns
        8192 Python function calls into a single tensor index per field, cutting per-step
        CPU overhead by ~4-8x and pushing GPU utilisation from ~20% toward ~60-70%.
        """
        idx = torch.tensor(indices, dtype=torch.long)
        batch = {
            "influence": self._influence[idx],
            # uint8; cast to float32 on GPU in training loop
            "cards": self._cards[idx],
            "scalars": self._scalars[idx],
            "card_target": self._card_target[idx],
            "mode_target": self._mode_target[idx],
            "country_ops_target": self._country_ops[idx],
            "value_target": self._value[idx],
        }

        if self._has_teacher is not None:
            batch["has_teacher_target"] = self._has_teacher[idx]
            batch["teacher_card_target"] = self._teacher_card[idx]
            batch["teacher_mode_target"] = self._teacher_mode[idx]
            batch["teacher_value_target"] = self._teacher_value[idx]
        return batch
