<<<<<<< HEAD
from __future__ import annotations

import math
from dataclasses import dataclass
=======
"""Frozen-position JSD probe evaluation for PPO checkpoints."""

from __future__ import annotations

from dataclasses import dataclass
from math import log
>>>>>>> worktree-agent-a04f61a3
from pathlib import Path

import polars as pl
import torch
import torch.nn as nn

CARD_SLOTS = 111
MODE_SLOTS = 5
COUNTRY_SLOTS = 86
<<<<<<< HEAD
COUNTRY_HEAD_MODE_IDS = frozenset({0, 2, 3})
=======
_LOG2 = log(2.0)
_COUNTRY_ACTIVE_MODES = frozenset({0, 1, 2})
>>>>>>> worktree-agent-a04f61a3


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


<<<<<<< HEAD
=======
def _mean_or_zero(total: float, count: int) -> float:
    return total / count if count > 0 else 0.0


>>>>>>> worktree-agent-a04f61a3
class ProbeEvaluator:
    """Evaluate JSD between two models at a frozen probe position set."""

    def __init__(
        self,
        probe_path: str | Path,
        device: str = "cpu",
        batch_size: int = 256,
<<<<<<< HEAD
    ) -> None:
        self.probe_path = Path(probe_path)
        if not self.probe_path.exists():
            raise FileNotFoundError(self.probe_path)

        df = pl.read_parquet(self.probe_path)
        if len(df) == 0:
            raise ValueError(f"Probe parquet is empty: {self.probe_path}")

=======
    ):
        self.probe_path = Path(probe_path)
        self.device = torch.device(device)
        self.batch_size = batch_size

        frame = pl.read_parquet(self.probe_path)
>>>>>>> worktree-agent-a04f61a3
        required = {
            "influence",
            "cards",
            "scalars",
<<<<<<< HEAD
=======
            "card_mask",
            "mode_mask",
>>>>>>> worktree-agent-a04f61a3
            "raw_turn",
            "side_int",
            "raw_defcon",
            "raw_vp",
        }
<<<<<<< HEAD
        missing = sorted(required.difference(df.columns))
        if missing:
            raise ValueError(f"Probe parquet missing required columns: {missing}")

        self.device = torch.device(device)
        self.batch_size = batch_size
        self.n_positions = len(df)

        self.influence = self._load_float_tensor(df, "influence")
        self.cards = self._load_float_tensor(df, "cards")
        self.scalars = self._load_float_tensor(df, "scalars")
        self.raw_turn = self._load_long_tensor(df, "raw_turn")
        self.side_int = self._load_long_tensor(df, "side_int")
        self.raw_defcon = self._load_long_tensor(df, "raw_defcon")
        self.raw_vp = self._load_long_tensor(df, "raw_vp")
        self.mode_id = (
            self._load_long_tensor(df, "mode_id")
            if "mode_id" in df.columns
            else torch.full((self.n_positions,), -1, dtype=torch.int64)
        )

        if "card_mask" in df.columns:
            self.card_mask = self._load_bool_tensor(df, "card_mask")
        elif "hand_card_ids" in df.columns:
            self.card_mask = self._card_masks_from_hands(df["hand_card_ids"].to_list())
        else:
            self.card_mask = torch.ones((self.n_positions, CARD_SLOTS), dtype=torch.bool)

        if "mode_mask" in df.columns:
            self.mode_mask = self._load_bool_tensor(df, "mode_mask")
        else:
            self.mode_mask = torch.ones((self.n_positions, MODE_SLOTS), dtype=torch.bool)

        self.country_mask = torch.ones((self.n_positions, COUNTRY_SLOTS), dtype=torch.bool)
        self._validate_shapes()
=======
        missing = sorted(required.difference(frame.columns))
        if missing:
            raise ValueError(f"Probe parquet missing required columns: {missing}")

        self.influence = self._tensor_from_list_column(frame, "influence", torch.float32)
        self.cards = self._tensor_from_list_column(frame, "cards", torch.float32)
        self.scalars = self._tensor_from_list_column(frame, "scalars", torch.float32)
        self.card_mask = self._tensor_from_list_column(frame, "card_mask", torch.bool)
        self.mode_mask = self._tensor_from_list_column(frame, "mode_mask", torch.bool)

        self.raw_turn = torch.tensor(frame["raw_turn"].to_list(), dtype=torch.int64)
        self.side_int = torch.tensor(frame["side_int"].to_list(), dtype=torch.int64)
        self.raw_defcon = torch.tensor(frame["raw_defcon"].to_list(), dtype=torch.int64)
        self.raw_vp = torch.tensor(frame["raw_vp"].to_list(), dtype=torch.int64)
        if "mode_id" in frame.columns:
            self.mode_id = torch.tensor(frame["mode_id"].to_list(), dtype=torch.int64)
        else:
            self.mode_id = torch.full((len(frame),), -1, dtype=torch.int64)

        self.n_positions = len(frame)
>>>>>>> worktree-agent-a04f61a3

    def compare(
        self,
        model_a: nn.Module,
        model_b: nn.Module,
    ) -> ProbeMetrics:
<<<<<<< HEAD
        """Run both models on all probe positions; return divergence metrics."""
        was_training_a = model_a.training
        was_training_b = model_b.training
        model_a.eval()
        model_b.eval()
=======
        was_training_a = model_a.training
        was_training_b = model_b.training
>>>>>>> worktree-agent-a04f61a3

        card_jsd_sum = 0.0
        card_jsd_count = 0
        mode_jsd_sum = 0.0
        mode_jsd_count = 0
        country_jsd_sum = 0.0
        country_jsd_count = 0
        value_mae_sum = 0.0
        value_mae_count = 0
        top1_card_sum = 0.0
        top1_card_count = 0
        top1_mode_sum = 0.0
        top1_mode_count = 0
<<<<<<< HEAD
        phase_card_jsd_sum = {"early": 0.0, "mid": 0.0, "late": 0.0}
        phase_card_jsd_count = {"early": 0, "mid": 0, "late": 0}

        try:
            with torch.no_grad():
                for start in range(0, self.n_positions, self.batch_size):
                    end = min(start + self.batch_size, self.n_positions)

                    influence = self.influence[start:end].to(self.device)
                    cards = self.cards[start:end].to(self.device)
                    scalars = self.scalars[start:end].to(self.device)
                    card_mask = self.card_mask[start:end].to(self.device)
                    mode_mask = self.mode_mask[start:end].to(self.device)
                    country_mask = self.country_mask[start:end].to(self.device)
                    turns = self.raw_turn[start:end]
                    mode_ids = self.mode_id[start:end].to(self.device)

                    out_a = self._forward_model(model_a, influence, cards, scalars)
                    out_b = self._forward_model(model_b, influence, cards, scalars)

                    card_jsd = self._jsd(out_a["card_logits"], out_b["card_logits"], card_mask)
                    card_valid = card_mask.any(dim=1)
                    if torch.any(card_valid):
                        card_jsd_sum += float(card_jsd[card_valid].sum().item())
                        card_jsd_count += int(card_valid.sum().item())

                        top1_card_a = self._masked_argmax(out_a["card_logits"], card_mask)
                        top1_card_b = self._masked_argmax(out_b["card_logits"], card_mask)
                        top1_card_sum += float(
                            (top1_card_a[card_valid] == top1_card_b[card_valid]).float().sum().item()
                        )
                        top1_card_count += int(card_valid.sum().item())

                        card_jsd_cpu = card_jsd.cpu()
                        phase_masks = {
                            "early": (turns >= 1) & (turns <= 3) & card_valid.cpu(),
                            "mid": (turns >= 4) & (turns <= 7) & card_valid.cpu(),
                            "late": (turns >= 8) & (turns <= 10) & card_valid.cpu(),
                        }
                        for phase_name, phase_mask in phase_masks.items():
                            if torch.any(phase_mask):
                                phase_card_jsd_sum[phase_name] += float(card_jsd_cpu[phase_mask].sum().item())
                                phase_card_jsd_count[phase_name] += int(phase_mask.sum().item())

                    mode_jsd = self._jsd(out_a["mode_logits"], out_b["mode_logits"], mode_mask)
                    mode_valid = mode_mask.any(dim=1)
                    if torch.any(mode_valid):
                        mode_jsd_sum += float(mode_jsd[mode_valid].sum().item())
                        mode_jsd_count += int(mode_valid.sum().item())

                        top1_mode_a = self._masked_argmax(out_a["mode_logits"], mode_mask)
                        top1_mode_b = self._masked_argmax(out_b["mode_logits"], mode_mask)
                        top1_mode_sum += float(
                            (top1_mode_a[mode_valid] == top1_mode_b[mode_valid]).float().sum().item()
                        )
                        top1_mode_count += int(mode_valid.sum().item())

                    country_active = torch.isin(
                        mode_ids,
                        torch.tensor(sorted(COUNTRY_HEAD_MODE_IDS), device=self.device, dtype=torch.int64),
                    )
                    if torch.any(country_active):
                        country_probs_a = self._country_distribution(out_a, country_mask)
                        country_probs_b = self._country_distribution(out_b, country_mask)
                        country_jsd = self._jsd(
                            torch.log(country_probs_a[country_active].clamp(min=1e-12)),
                            torch.log(country_probs_b[country_active].clamp(min=1e-12)),
                            country_mask[country_active],
                        )
                        country_jsd_sum += float(country_jsd.sum().item())
                        country_jsd_count += int(country_active.sum().item())

                    value_a = out_a["value"].squeeze(-1)
                    value_b = out_b["value"].squeeze(-1)
                    value_mae_sum += float(torch.abs(value_a - value_b).sum().item())
                    value_mae_count += end - start
        finally:
            model_a.train(was_training_a)
            model_b.train(was_training_b)

        return ProbeMetrics(
            card_jsd=self._mean_or_nan(card_jsd_sum, card_jsd_count),
            mode_jsd=self._mean_or_nan(mode_jsd_sum, mode_jsd_count),
            country_jsd=self._mean_or_nan(country_jsd_sum, country_jsd_count),
            value_mae=self._mean_or_nan(value_mae_sum, value_mae_count),
            top1_card_agree=self._mean_or_nan(top1_card_sum, top1_card_count),
            top1_mode_agree=self._mean_or_nan(top1_mode_sum, top1_mode_count),
            card_jsd_early=self._mean_or_nan(phase_card_jsd_sum["early"], phase_card_jsd_count["early"]),
            card_jsd_mid=self._mean_or_nan(phase_card_jsd_sum["mid"], phase_card_jsd_count["mid"]),
            card_jsd_late=self._mean_or_nan(phase_card_jsd_sum["late"], phase_card_jsd_count["late"]),
=======
        phase_card_sum = {"early": 0.0, "mid": 0.0, "late": 0.0}
        phase_card_count = {"early": 0, "mid": 0, "late": 0}

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

                    card_valid = torch.isfinite(card_jsd)
                    if card_valid.any():
                        card_jsd_sum += float(card_jsd[card_valid].sum().item())
                        card_jsd_count += int(card_valid.sum().item())

                    mode_valid = torch.isfinite(mode_jsd)
                    if mode_valid.any():
                        mode_jsd_sum += float(mode_jsd[mode_valid].sum().item())
                        mode_jsd_count += int(mode_valid.sum().item())

                    value_delta = (out_a["value"] - out_b["value"]).abs().squeeze(-1)
                    value_mae_sum += float(value_delta.sum().item())
                    value_mae_count += int(value_delta.numel())

                    top1_card_agree, top1_card_valid = self._top1_agreement(
                        out_a["card_logits"], out_b["card_logits"], card_mask
                    )
                    if top1_card_valid.any():
                        top1_card_sum += float(top1_card_agree[top1_card_valid].sum().item())
                        top1_card_count += int(top1_card_valid.sum().item())

                    top1_mode_agree, top1_mode_valid = self._top1_agreement(
                        out_a["mode_logits"], out_b["mode_logits"], mode_mask
                    )
                    if top1_mode_valid.any():
                        top1_mode_sum += float(top1_mode_agree[top1_mode_valid].sum().item())
                        top1_mode_count += int(top1_mode_valid.sum().item())

                    country_head_a = out_a.get("country_logits")
                    country_head_b = out_b.get("country_logits")
                    if country_head_a is not None and country_head_b is not None:
                        country_active = torch.tensor(
                            [int(mode_id) in _COUNTRY_ACTIVE_MODES for mode_id in mode_ids.tolist()],
                            dtype=torch.bool,
                        )
                        if country_active.any():
                            country_mask = torch.ones(
                                (int(country_active.sum().item()), COUNTRY_SLOTS),
                                dtype=torch.bool,
                                device=self.device,
                            )
                            country_jsd = self._jsd(
                                country_head_a[country_active.to(self.device)],
                                country_head_b[country_active.to(self.device)],
                                country_mask,
                            )
                            country_valid = torch.isfinite(country_jsd)
                            if country_valid.any():
                                country_jsd_sum += float(country_jsd[country_valid].sum().item())
                                country_jsd_count += int(country_valid.sum().item())

                    phase_masks = {
                        "early": turns <= 3,
                        "mid": (turns >= 4) & (turns <= 7),
                        "late": turns >= 8,
                    }
                    for phase_name, phase_mask in phase_masks.items():
                        phase_valid = card_valid.cpu() & phase_mask
                        if phase_valid.any():
                            phase_card_sum[phase_name] += float(card_jsd.cpu()[phase_valid].sum().item())
                            phase_card_count[phase_name] += int(phase_valid.sum().item())
        finally:
            model_a.train(was_training_a)
            if model_b is not model_a:
                model_b.train(was_training_b)

        return ProbeMetrics(
            card_jsd=_mean_or_zero(card_jsd_sum, card_jsd_count),
            mode_jsd=_mean_or_zero(mode_jsd_sum, mode_jsd_count),
            country_jsd=_mean_or_zero(country_jsd_sum, country_jsd_count),
            value_mae=_mean_or_zero(value_mae_sum, value_mae_count),
            top1_card_agree=_mean_or_zero(top1_card_sum, top1_card_count),
            top1_mode_agree=_mean_or_zero(top1_mode_sum, top1_mode_count),
            card_jsd_early=_mean_or_zero(phase_card_sum["early"], phase_card_count["early"]),
            card_jsd_mid=_mean_or_zero(phase_card_sum["mid"], phase_card_count["mid"]),
            card_jsd_late=_mean_or_zero(phase_card_sum["late"], phase_card_count["late"]),
>>>>>>> worktree-agent-a04f61a3
            n_positions=self.n_positions,
        )

    @staticmethod
<<<<<<< HEAD
    def _jsd(p: torch.Tensor, q: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        """Compute JSD(P||Q) ∈ [0, log2] per row, with illegal actions zeroed.

        Args:
            p, q: (B, N) raw logits (pre-softmax)
            mask: (B, N) bool — True = legal action
        Returns:
            (B,) JSD values in [0, 1] (normalized by log 2)
        """
        if p.shape != q.shape or p.shape != mask.shape:
            raise ValueError(
                f"Shape mismatch for JSD: p={tuple(p.shape)} q={tuple(q.shape)} mask={tuple(mask.shape)}"
            )

        valid = mask.any(dim=1)
        jsd = torch.zeros(p.shape[0], dtype=p.dtype, device=p.device)
        if not torch.any(valid):
            return jsd

        p_valid = p[valid]
        q_valid = q[valid]
        mask_valid = mask[valid]

        neg_inf = torch.tensor(float("-inf"), dtype=p.dtype, device=p.device)
        p_masked = torch.where(mask_valid, p_valid, neg_inf)
        q_masked = torch.where(mask_valid, q_valid, neg_inf)

        log_p = torch.log_softmax(p_masked, dim=1)
        log_q = torch.log_softmax(q_masked, dim=1)
        prob_p = torch.where(mask_valid, log_p.exp(), torch.zeros_like(log_p))
        prob_q = torch.where(mask_valid, log_q.exp(), torch.zeros_like(log_q))
        log_m = torch.logaddexp(log_p, log_q) - math.log(2.0)

        kl_pm = torch.where(mask_valid, prob_p * (log_p - log_m), torch.zeros_like(prob_p)).sum(dim=1)
        kl_qm = torch.where(mask_valid, prob_q * (log_q - log_m), torch.zeros_like(prob_q)).sum(dim=1)
        jsd_valid = 0.5 * (kl_pm + kl_qm) / math.log(2.0)
        jsd[valid] = torch.clamp(jsd_valid, min=0.0, max=1.0)
        return jsd

    @staticmethod
    def _load_float_tensor(df: pl.DataFrame, column: str) -> torch.Tensor:
        return torch.tensor(df[column].to_list(), dtype=torch.float32)

    @staticmethod
    def _load_long_tensor(df: pl.DataFrame, column: str) -> torch.Tensor:
        return torch.tensor(df[column].to_list(), dtype=torch.int64)

    @staticmethod
    def _load_bool_tensor(df: pl.DataFrame, column: str) -> torch.Tensor:
        return torch.tensor(df[column].to_list(), dtype=torch.bool)

    @staticmethod
    def _card_masks_from_hands(hand_card_ids: list[list[int] | None]) -> torch.Tensor:
        mask = torch.zeros((len(hand_card_ids), CARD_SLOTS), dtype=torch.bool)
        for row_idx, hand in enumerate(hand_card_ids):
            if hand is None:
                mask[row_idx] = True
                continue
            for raw_card_id in hand:
                card_id = int(raw_card_id)
                if 1 <= card_id <= CARD_SLOTS:
                    mask[row_idx, card_id - 1] = True
        return mask

    @staticmethod
    def _masked_argmax(logits: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        masked_logits = logits.masked_fill(~mask, float("-inf"))
        return masked_logits.argmax(dim=1)

    @staticmethod
    def _mean_or_nan(total: float, count: int) -> float:
        if count == 0:
            return float("nan")
        return total / count

    def _validate_shapes(self) -> None:
        expected = {
            "influence": (self.n_positions, 172),
            "cards": (self.n_positions, 448),
            "scalars": (self.n_positions, 32),
            "card_mask": (self.n_positions, CARD_SLOTS),
            "mode_mask": (self.n_positions, MODE_SLOTS),
            "country_mask": (self.n_positions, COUNTRY_SLOTS),
        }
        actual = {
            "influence": tuple(self.influence.shape),
            "cards": tuple(self.cards.shape),
            "scalars": tuple(self.scalars.shape),
            "card_mask": tuple(self.card_mask.shape),
            "mode_mask": tuple(self.mode_mask.shape),
            "country_mask": tuple(self.country_mask.shape),
        }
        mismatched = {
            key: (actual[key], expected[key])
            for key in expected
            if actual[key] != expected[key]
        }
        if mismatched:
            raise ValueError(f"Probe parquet tensors have unexpected shapes: {mismatched}")

    @staticmethod
    def _forward_model(
        model: nn.Module,
        influence: torch.Tensor,
        cards: torch.Tensor,
        scalars: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        expected_scalars = scalars.shape[1]
        scalar_encoder = getattr(model, "scalar_encoder", None)
        if scalar_encoder is not None and hasattr(scalar_encoder, "in_features"):
            # scalar_encoder.in_features = SCALAR_DIM + _REGION_SCALAR_DIM for models
            # that append region scalars internally (e.g. TSCountryAttnModel).
            # We must pass only the raw SCALAR_DIM portion; the model appends region
            # scalars itself. Subtract _REGION_SCALAR_DIM if present.
            region_dim = int(getattr(model, "_REGION_SCALAR_DIM", 0))
            expected_scalars = int(scalar_encoder.in_features) - region_dim

        if scalars.shape[1] < expected_scalars:
            pad = torch.zeros(
                (scalars.shape[0], expected_scalars - scalars.shape[1]),
                dtype=scalars.dtype,
                device=scalars.device,
            )
            scalars = torch.cat([scalars, pad], dim=1)
        elif scalars.shape[1] > expected_scalars:
            scalars = scalars[:, :expected_scalars]

        return model(influence, cards, scalars)

    @staticmethod
    def _country_distribution(outputs: dict[str, torch.Tensor], mask: torch.Tensor) -> torch.Tensor:
        if "marginal_logits" not in outputs:
            strategy_logits = outputs.get("strategy_logits")
            country_strategy_logits = outputs.get("country_strategy_logits")
            if (
                strategy_logits is not None
                and country_strategy_logits is not None
                and strategy_logits.ndim == 2
                and country_strategy_logits.ndim == 3
                and strategy_logits.shape[0] == country_strategy_logits.shape[0]
                and strategy_logits.shape[1] == country_strategy_logits.shape[1]
            ):
                mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
                strategy_probs = torch.softmax(country_strategy_logits, dim=2)
                probs = (mixing * strategy_probs).sum(dim=1)
                probs = probs * mask.to(dtype=probs.dtype)
                return probs / probs.sum(dim=1, keepdim=True).clamp(min=1e-12)

        country_logits = outputs["country_logits"]
        if ProbeEvaluator._looks_like_probability_distribution(country_logits, mask):
            probs = country_logits * mask.to(dtype=country_logits.dtype)
            return probs / probs.sum(dim=1, keepdim=True).clamp(min=1e-12)

        masked_logits = country_logits.masked_fill(~mask, float("-inf"))
        probs = torch.softmax(masked_logits, dim=1)
        probs = probs * mask.to(dtype=probs.dtype)
        return probs / probs.sum(dim=1, keepdim=True).clamp(min=1e-12)

    @staticmethod
    def _looks_like_probability_distribution(values: torch.Tensor, mask: torch.Tensor) -> bool:
        if values.numel() == 0:
            return False
        masked = values * mask.to(dtype=values.dtype)
        row_sums = masked.sum(dim=1)
        valid = mask.any(dim=1)
        if not torch.any(valid):
            return False
        return bool(
            torch.all(masked[valid] >= -1e-6).item()
            and torch.all(masked[valid] <= 1.0 + 1e-6).item()
            and torch.allclose(
                row_sums[valid],
                torch.ones_like(row_sums[valid]),
                atol=1e-4,
                rtol=1e-4,
            )
        )
=======
    def _tensor_from_list_column(
        frame: pl.DataFrame,
        column: str,
        dtype: torch.dtype,
    ) -> torch.Tensor:
        return torch.tensor(frame[column].to_list(), dtype=dtype)

    @staticmethod
    def _masked_distribution(
        logits: torch.Tensor,
        mask: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
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
    def _jsd(p: torch.Tensor, q: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        """Compute row-wise JSD(P||Q) in [0, 1] with masked illegal actions."""
        p_prob, p_valid = ProbeEvaluator._masked_distribution(p, mask)
        q_prob, q_valid = ProbeEvaluator._masked_distribution(q, mask)
        valid = p_valid & q_valid
        jsd = torch.full((p.shape[0],), float("nan"), dtype=torch.float32, device=p.device)
        if not valid.any():
            return jsd

        p_valid_prob = p_prob[valid]
        q_valid_prob = q_prob[valid]
        m = 0.5 * (p_valid_prob + q_valid_prob)
        log_p = torch.log(p_valid_prob.clamp_min(1e-12))
        log_q = torch.log(q_valid_prob.clamp_min(1e-12))
        log_m = torch.log(m.clamp_min(1e-12))
        kl_pm = torch.where(
            p_valid_prob > 0,
            p_valid_prob * (log_p - log_m),
            torch.zeros_like(p_valid_prob),
        ).sum(dim=1)
        kl_qm = torch.where(
            q_valid_prob > 0,
            q_valid_prob * (log_q - log_m),
            torch.zeros_like(q_valid_prob),
        ).sum(dim=1)
        jsd[valid] = (0.5 * kl_pm + 0.5 * kl_qm) / _LOG2
        return jsd

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
            agree[valid] = (
                p_prob[valid].argmax(dim=1) == q_prob[valid].argmax(dim=1)
            ).to(torch.float32)
        return agree, valid
>>>>>>> worktree-agent-a04f61a3
