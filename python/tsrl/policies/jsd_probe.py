"""JSD probe evaluation for frozen Twilight Struggle positions."""

from __future__ import annotations

from dataclasses import dataclass
from glob import glob
from math import log
from pathlib import Path

import polars as pl
import torch
import torch.nn as nn

from tsrl.constants import MODEL_REGISTRY
from tsrl.policies.model import TSBaselineModel, TSControlFeatGNNModel

CARD_SLOTS = 111
MODE_SLOTS = 5
COUNTRY_SLOTS = 86
_COUNTRY_ACTIVE_MODES = frozenset({0, 1, 2})
_LOG2 = log(2.0)
_DEFAULT_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def jsd(p: torch.Tensor, q: torch.Tensor, eps: float = 1e-8) -> float:
    """Compute Jensen-Shannon divergence between two unmasked logit vectors."""
    p_prob = torch.softmax(p.to(torch.float32), dim=-1).clamp_min(eps)
    q_prob = torch.softmax(q.to(torch.float32), dim=-1).clamp_min(eps)
    mean = 0.5 * (p_prob + q_prob)
    kl_pm = torch.sum(p_prob * torch.log(p_prob / mean))
    kl_qm = torch.sum(q_prob * torch.log(q_prob / mean))
    return float(((0.5 * kl_pm + 0.5 * kl_qm) / _LOG2).item())


def _mean_or_zero(total: float, count: int) -> float:
    return total / count if count > 0 else 0.0


def _turn_bucket(turn: int) -> str:
    if turn <= 3:
        return "early"
    if turn <= 7:
        return "mid"
    return "late"


def _defcon_bucket(defcon: int) -> str:
    if defcon <= 2:
        return "low"
    if defcon == 3:
        return "mid"
    return "high"


def _vp_bucket(vp: int) -> str:
    if vp <= -7:
        return "us_ahead"
    if vp >= 7:
        return "ussr_ahead"
    return "close"


def _hand_to_card_mask(hand_card_ids: list[int] | None) -> list[bool]:
    mask = [False] * CARD_SLOTS
    if hand_card_ids is None:
        values: list[int] = []
    elif hasattr(hand_card_ids, "to_list"):
        values = hand_card_ids.to_list()
    else:
        values = list(hand_card_ids)
    for card_id in values:
        idx = int(card_id) - 1
        if 0 <= idx < CARD_SLOTS:
            mask[idx] = True
    return mask if any(mask) else [True] * CARD_SLOTS


def _resolve_parquet_paths(parquet_glob: str | Path) -> list[Path]:
    candidate = Path(parquet_glob)
    if candidate.exists():
        if candidate.is_dir():
            paths = sorted(candidate.glob("*.parquet"))
        else:
            paths = [candidate]
    else:
        paths = [Path(path) for path in sorted(glob(str(parquet_glob), recursive=True))]
    if not paths:
        raise FileNotFoundError(f"No parquet files found for {parquet_glob!r}")
    return paths


def _load_strata_index(paths: list[Path]) -> pl.DataFrame:
    scalar_cols = {"raw_turn", "side_int", "raw_defcon", "raw_vp", "mode_id"}
    frames: list[pl.DataFrame] = []
    offset = 0
    for path in paths:
        available = set(pl.read_parquet_schema(path).keys())
        cols = sorted(scalar_cols & available)
        frame = pl.read_parquet(path, columns=cols).with_row_index(name="_local_idx")
        frame = frame.with_columns(
            (pl.col("_local_idx") + offset).alias("row_idx"),
            pl.lit(str(path)).alias("_src_path"),
        ).drop("_local_idx")
        frames.append(frame)
        offset += len(frame)
    frame = pl.concat(frames, how="vertical_relaxed")
    for column in ("raw_turn", "side_int", "raw_defcon", "raw_vp"):
        if column not in frame.columns:
            raise ValueError(f"Source parquet missing required column {column!r}")
    if "mode_id" not in frame.columns:
        frame = frame.with_columns(pl.lit(-1, dtype=pl.Int32).alias("mode_id"))
    return frame


def _load_selected_rows(paths: list[Path], selected_idx: set[int]) -> pl.DataFrame:
    needed_cols = {
        "influence",
        "cards",
        "scalars",
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
        "hand_card_ids",
        "card_mask",
        "mode_mask",
        "country_mask",
        "mode_id",
    }
    frames: list[pl.DataFrame] = []
    offset = 0
    for path in paths:
        available = set(pl.read_parquet_schema(path).keys())
        cols = sorted(needed_cols & available)
        frame = pl.read_parquet(path, columns=cols).with_row_index(name="_local_idx")
        n_rows = len(frame)
        local_needed = [idx - offset for idx in selected_idx if offset <= idx < offset + n_rows]
        if local_needed:
            frame = frame.filter(pl.col("_local_idx").is_in(local_needed))
            frame = frame.with_columns((pl.col("_local_idx") + offset).alias("row_idx")).drop("_local_idx")
            frames.append(frame)
        offset += n_rows
    return pl.concat(frames, how="vertical_relaxed") if frames else pl.DataFrame()


def _allocate_counts(group_sizes: dict[str, int], n: int) -> dict[str, int]:
    if not group_sizes:
        return {}
    total_rows = sum(group_sizes.values())
    if n >= total_rows:
        return dict(group_sizes)

    allocations = {key: 0 for key in group_sizes}
    ordered = sorted(group_sizes)
    remaining = n
    if n >= len(ordered):
        for key in ordered:
            allocations[key] = 1
            remaining -= 1

    spare_total = sum(max(0, group_sizes[key] - allocations[key]) for key in ordered)
    if remaining <= 0 or spare_total <= 0:
        return allocations

    fractional: list[tuple[float, str]] = []
    for key in ordered:
        spare = max(0, group_sizes[key] - allocations[key])
        if spare <= 0:
            continue
        raw_share = remaining * (spare / spare_total)
        add = min(spare, int(raw_share))
        allocations[key] += add
        fractional.append((raw_share - add, key))

    for _, key in sorted(fractional, key=lambda item: (-item[0], item[1])):
        if sum(allocations.values()) >= n:
            break
        if allocations[key] < group_sizes[key]:
            allocations[key] += 1
    return allocations


def build_probe_set(
    parquet_glob: str | Path,
    output_path: str | Path,
    n: int = 1000,
    seed: int = 42,
    force: bool = False,
) -> Path:
    """Build a frozen probe set from rollout parquet data."""
    output_path = Path(output_path)
    if output_path.exists() and not force:
        raise FileExistsError(f"{output_path} already exists; pass force=True to overwrite")

    paths = _resolve_parquet_paths(parquet_glob)
    strata = _load_strata_index(paths).with_columns(
        pl.col("raw_turn").map_elements(_turn_bucket, return_dtype=pl.String).alias("_tb"),
        pl.col("side_int").cast(pl.String).alias("_si"),
        pl.col("raw_defcon").map_elements(_defcon_bucket, return_dtype=pl.String).alias("_db"),
        pl.col("raw_vp").map_elements(_vp_bucket, return_dtype=pl.String).alias("_vb"),
    ).with_columns(
        (pl.col("_tb") + "|" + pl.col("_si") + "|" + pl.col("_db") + "|" + pl.col("_vb")).alias("_stratum")
    )

    group_sizes = {
        row["_stratum"]: row["count"]
        for row in strata.group_by("_stratum").agg(pl.len().alias("count")).to_dicts()
    }
    allocations = _allocate_counts(group_sizes, n)

    selected_idx: list[int] = []
    for offset, (stratum_key, want) in enumerate(sorted(allocations.items())):
        if want <= 0:
            continue
        group = strata.filter(pl.col("_stratum") == stratum_key)
        chosen = group if want >= len(group) else group.sample(n=want, seed=seed + offset, shuffle=True)
        selected_idx.extend(chosen["row_idx"].to_list())

    selected = _load_selected_rows(paths, set(selected_idx)).sort("row_idx")
    if "card_mask" not in selected.columns:
        if "hand_card_ids" in selected.columns:
            selected = selected.with_columns(
                pl.col("hand_card_ids")
                .map_elements(_hand_to_card_mask, return_dtype=pl.List(pl.Boolean))
                .alias("card_mask")
            )
        else:
            selected = selected.with_columns(pl.Series("card_mask", [[True] * CARD_SLOTS] * len(selected)))
    if "mode_mask" not in selected.columns:
        selected = selected.with_columns(pl.Series("mode_mask", [[True] * MODE_SLOTS] * len(selected)))
    if "mode_id" not in selected.columns:
        selected = selected.with_columns(pl.lit(-1, dtype=pl.Int32).alias("mode_id"))

    output = selected.select(
        "influence",
        "cards",
        "scalars",
        "card_mask",
        "mode_mask",
        *([ "country_mask" ] if "country_mask" in selected.columns else []),
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
        "mode_id",
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.write_parquet(output_path)
    return output_path


@dataclass
class ProbeMetrics:
    card_jsd: float
    mode_jsd: float
    country_jsd: float
    value_mae: float
    top1_card_agree: float
    top1_mode_agree: float
    card_jsd_early: float
    card_jsd_mid: float
    card_jsd_late: float
    n_positions: int

    @property
    def top1_card_agreement(self) -> float:
        return self.top1_card_agree

    @property
    def top1_mode_agreement(self) -> float:
        return self.top1_mode_agree

    def to_dict(self) -> dict[str, float]:
        return {
            "card_jsd": self.card_jsd,
            "mode_jsd": self.mode_jsd,
            "country_jsd": self.country_jsd,
            "value_mae": self.value_mae,
            "early_card_jsd": self.card_jsd_early,
            "mid_card_jsd": self.card_jsd_mid,
            "late_card_jsd": self.card_jsd_late,
            "top1_card_agreement": self.top1_card_agree,
            "top1_mode_agreement": self.top1_mode_agree,
            "n_positions": self.n_positions,
        }


class ProbeEvaluator:
    """Evaluate policy stability over a frozen position parquet."""

    def __init__(self, probe_path: str | Path, device: str = "cpu", batch_size: int = 256):
        frame = pl.read_parquet(Path(probe_path))
        missing = sorted({"influence", "cards", "scalars", "raw_turn"} - set(frame.columns))
        if missing:
            raise ValueError(f"Probe parquet missing required columns: {missing}")

        self.device = torch.device(device)
        self.batch_size = batch_size
        self.influence = torch.tensor(frame["influence"].to_list(), dtype=torch.float32)
        self.cards = torch.tensor(frame["cards"].to_list(), dtype=torch.float32)
        self.scalars = torch.tensor(frame["scalars"].to_list(), dtype=torch.float32)
        self.card_mask = self._mask_tensor(frame, "card_mask", CARD_SLOTS)
        self.mode_mask = self._mask_tensor(frame, "mode_mask", MODE_SLOTS)
        self.country_mask = self._mask_tensor(frame, "country_mask", COUNTRY_SLOTS, required=False)
        self.raw_turn = self._scalar_tensor(frame, "raw_turn")
        self.side_int = self._scalar_tensor(frame, "side_int")
        self.raw_defcon = self._scalar_tensor(frame, "raw_defcon")
        self.raw_vp = self._scalar_tensor(frame, "raw_vp")
        self.mode_id = self._scalar_tensor(frame, "mode_id", default=-1)
        self.n_positions = len(frame)

    def compare(self, model_a: nn.Module, model_b: nn.Module) -> ProbeMetrics:
        was_training_a = model_a.training
        was_training_b = model_b.training
        totals = {
            "card_sum": 0.0,
            "card_count": 0,
            "mode_sum": 0.0,
            "mode_count": 0,
            "country_sum": 0.0,
            "country_count": 0,
            "value_sum": 0.0,
            "value_count": 0,
            "top1_card_sum": 0.0,
            "top1_card_count": 0,
            "top1_mode_sum": 0.0,
            "top1_mode_count": 0,
        }
        phase_sum = {"early": 0.0, "mid": 0.0, "late": 0.0}
        phase_count = {"early": 0, "mid": 0, "late": 0}

        model_a.eval()
        model_b.eval()
        try:
            with torch.no_grad():
                for start in range(0, self.n_positions, self.batch_size):
                    stop = min(start + self.batch_size, self.n_positions)
                    influence = self.influence[start:stop].to(self.device)
                    cards = self.cards[start:stop].to(self.device)
                    scalars = self.scalars[start:stop].to(self.device)
                    card_mask = self.card_mask[start:stop].to(self.device)
                    mode_mask = self.mode_mask[start:stop].to(self.device)
                    turns = self.raw_turn[start:stop]
                    mode_ids = self.mode_id[start:stop]

                    out_a = model_a(influence, cards, scalars)
                    out_b = model_b(influence, cards, scalars)

                    card_jsd = self._jsd(out_a["card_logits"], out_b["card_logits"], card_mask)
                    mode_jsd = self._jsd(out_a["mode_logits"], out_b["mode_logits"], mode_mask)
                    self._accumulate(card_jsd, totals, "card")
                    self._accumulate(mode_jsd, totals, "mode")

                    value_delta = (out_a["value"] - out_b["value"]).abs().squeeze(-1)
                    totals["value_sum"] += float(value_delta.sum().item())
                    totals["value_count"] += int(value_delta.numel())

                    top1_card, top1_card_valid = self._top1_agreement(
                        out_a["card_logits"], out_b["card_logits"], card_mask
                    )
                    top1_mode, top1_mode_valid = self._top1_agreement(
                        out_a["mode_logits"], out_b["mode_logits"], mode_mask
                    )
                    totals["top1_card_sum"] += float(top1_card[top1_card_valid].sum().item())
                    totals["top1_card_count"] += int(top1_card_valid.sum().item())
                    totals["top1_mode_sum"] += float(top1_mode[top1_mode_valid].sum().item())
                    totals["top1_mode_count"] += int(top1_mode_valid.sum().item())

                    country_a = out_a.get("country_logits")
                    country_b = out_b.get("country_logits")
                    if country_a is not None and country_b is not None:
                        country_active = torch.tensor(
                            [int(mode_id) in _COUNTRY_ACTIVE_MODES for mode_id in mode_ids.tolist()],
                            dtype=torch.bool,
                            device=self.device,
                        )
                        if country_active.any():
                            country_mask = (
                                self.country_mask[start:stop].to(self.device)[country_active]
                                if self.country_mask is not None
                                else torch.ones(
                                    (int(country_active.sum().item()), COUNTRY_SLOTS),
                                    dtype=torch.bool,
                                    device=self.device,
                                )
                            )
                            country_jsd = self._jsd(
                                country_a[country_active],
                                country_b[country_active],
                                country_mask,
                            )
                            self._accumulate(country_jsd, totals, "country")

                    card_valid = torch.isfinite(card_jsd).cpu()
                    for phase_name, phase_mask in {
                        "early": turns <= 3,
                        "mid": (turns >= 4) & (turns <= 7),
                        "late": turns >= 8,
                    }.items():
                        phase_valid = card_valid & phase_mask
                        if phase_valid.any():
                            phase_sum[phase_name] += float(card_jsd.cpu()[phase_valid].sum().item())
                            phase_count[phase_name] += int(phase_valid.sum().item())
        finally:
            model_a.train(was_training_a)
            if model_b is not model_a:
                model_b.train(was_training_b)

        return ProbeMetrics(
            card_jsd=_mean_or_zero(totals["card_sum"], totals["card_count"]),
            mode_jsd=_mean_or_zero(totals["mode_sum"], totals["mode_count"]),
            country_jsd=_mean_or_zero(totals["country_sum"], totals["country_count"]),
            value_mae=_mean_or_zero(totals["value_sum"], totals["value_count"]),
            top1_card_agree=_mean_or_zero(totals["top1_card_sum"], totals["top1_card_count"]),
            top1_mode_agree=_mean_or_zero(totals["top1_mode_sum"], totals["top1_mode_count"]),
            card_jsd_early=_mean_or_zero(phase_sum["early"], phase_count["early"]),
            card_jsd_mid=_mean_or_zero(phase_sum["mid"], phase_count["mid"]),
            card_jsd_late=_mean_or_zero(phase_sum["late"], phase_count["late"]),
            n_positions=self.n_positions,
        )

    @staticmethod
    def _scalar_tensor(frame: pl.DataFrame, column: str, default: int = 0) -> torch.Tensor:
        if column not in frame.columns:
            return torch.full((len(frame),), default, dtype=torch.int64)
        return torch.tensor(frame[column].to_list(), dtype=torch.int64)

    @staticmethod
    def _mask_tensor(
        frame: pl.DataFrame,
        column: str,
        width: int,
        required: bool = True,
    ) -> torch.Tensor | None:
        if column not in frame.columns:
            if required:
                return torch.ones((len(frame), width), dtype=torch.bool)
            return None
        return torch.tensor(frame[column].to_list(), dtype=torch.bool)

    @staticmethod
    def _accumulate(values: torch.Tensor, totals: dict[str, float | int], prefix: str) -> None:
        valid = torch.isfinite(values)
        if valid.any():
            totals[f"{prefix}_sum"] += float(values[valid].sum().item())
            totals[f"{prefix}_count"] += int(valid.sum().item())

    @staticmethod
    def _masked_distribution(logits: torch.Tensor, mask: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        mask = ProbeEvaluator._align_mask(mask, logits.shape[1])
        valid = mask.any(dim=1)
        probs = torch.zeros_like(logits, dtype=torch.float32)
        if not valid.any():
            return probs, valid

        logits_valid = logits[valid].to(torch.float32)
        mask_valid = mask[valid]
        looks_like_probs = (
            bool(torch.isfinite(logits_valid).all().item())
            and bool((logits_valid >= -1e-6).all().item())
            and bool(((logits_valid.sum(dim=1) - 1.0).abs() <= 1e-4).all().item())
        )
        if looks_like_probs:
            masked = logits_valid.clamp_min(0.0) * mask_valid.to(torch.float32)
            denom = masked.sum(dim=1, keepdim=True)
            valid_valid = denom.squeeze(1) > 0
            probs_valid = torch.zeros_like(masked)
            if valid_valid.any():
                probs_valid[valid_valid] = masked[valid_valid] / denom[valid_valid]
        else:
            masked = logits_valid.masked_fill(~mask_valid, float("-inf"))
            probs_valid = torch.softmax(masked, dim=1)
            valid_valid = torch.ones(masked.shape[0], dtype=torch.bool, device=masked.device)

        valid_out = valid.clone()
        valid_out[valid] = valid_valid
        probs[valid] = probs_valid
        return probs, valid_out

    @staticmethod
    def _align_mask(mask: torch.Tensor, width: int) -> torch.Tensor:
        if mask.shape[1] == width:
            return mask
        if mask.shape[1] > width:
            return mask[:, :width]
        pad = torch.ones((mask.shape[0], width - mask.shape[1]), dtype=mask.dtype, device=mask.device)
        return torch.cat([mask, pad], dim=1)

    @staticmethod
    def _jsd(p: torch.Tensor, q: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        p_prob, p_valid = ProbeEvaluator._masked_distribution(p, mask)
        q_prob, q_valid = ProbeEvaluator._masked_distribution(q, mask)
        valid = p_valid & q_valid
        out = torch.full((p.shape[0],), float("nan"), dtype=torch.float32, device=p.device)
        if not valid.any():
            return out

        p_valid_prob = p_prob[valid]
        q_valid_prob = q_prob[valid]
        mean = 0.5 * (p_valid_prob + q_valid_prob)
        kl_pm = torch.where(
            p_valid_prob > 0,
            p_valid_prob * torch.log(p_valid_prob.clamp_min(1e-12) / mean.clamp_min(1e-12)),
            torch.zeros_like(p_valid_prob),
        ).sum(dim=1)
        kl_qm = torch.where(
            q_valid_prob > 0,
            q_valid_prob * torch.log(q_valid_prob.clamp_min(1e-12) / mean.clamp_min(1e-12)),
            torch.zeros_like(q_valid_prob),
        ).sum(dim=1)
        out[valid] = (0.5 * kl_pm + 0.5 * kl_qm) / _LOG2
        return out

    @staticmethod
    def _top1_agreement(
        p: torch.Tensor,
        q: torch.Tensor,
        mask: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        p_prob, p_valid = ProbeEvaluator._masked_distribution(p, mask)
        q_prob, q_valid = ProbeEvaluator._masked_distribution(q, mask)
        valid = p_valid & q_valid
        agree = torch.zeros((p.shape[0],), dtype=torch.float32, device=p.device)
        if valid.any():
            agree[valid] = (p_prob[valid].argmax(dim=1) == q_prob[valid].argmax(dim=1)).to(torch.float32)
        return agree, valid


def load_probe_model(checkpoint_path: str | Path, device: str = _DEFAULT_DEVICE) -> nn.Module:
    """Load a standard checkpoint or scripted module for probe evaluation."""
    checkpoint_path = Path(checkpoint_path)
    if checkpoint_path.name.endswith("_scripted.pt") or checkpoint_path.name == "scripted.pt":
        model = torch.jit.load(str(checkpoint_path), map_location=device)
        model.eval()
        return model

    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = ckpt.get("model_state_dict", ckpt)
    args = ckpt.get("args", {})
    hidden_dim = args.get("hidden_dim", 256)
    model_type = args.get("model_type", "baseline")
    dropout = args.get("dropout", 0.1)
    num_strategies = args.get("num_strategies", 4)

    cls = MODEL_REGISTRY.get(model_type, TSBaselineModel)
    if cls in (TSControlFeatGNNModel,) and num_strategies != 4:
        model = cls(hidden_dim=hidden_dim, dropout=dropout, num_strategies=num_strategies)
    else:
        model = cls(hidden_dim=hidden_dim, dropout=dropout)

    model_state = model.state_dict()
    filtered = {}
    for key, value in state_dict.items():
        if key not in model_state:
            continue
        if value.shape == model_state[key].shape:
            filtered[key] = value
        elif value.dim() == 2 and model_state[key].dim() == 2 and value.shape[0] == model_state[key].shape[0]:
            widened = model_state[key].clone()
            widened[:, : value.shape[1]] = value
            filtered[key] = widened
    model.load_state_dict(filtered, strict=False)
    model.to(device)
    model.eval()
    return model


def compute_jsd(
    model_a_path: str,
    model_b_path: str,
    probe_path: str,
    device: str = _DEFAULT_DEVICE,
) -> dict[str, float]:
    """Load two checkpoints, evaluate them on the frozen probe set, and return metrics."""
    evaluator = ProbeEvaluator(probe_path, device=device)
    model_a = load_probe_model(model_a_path, device=device)
    model_b = load_probe_model(model_b_path, device=device)
    return evaluator.compare(model_a, model_b).to_dict()
