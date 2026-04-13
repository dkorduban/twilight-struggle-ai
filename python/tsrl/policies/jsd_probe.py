"""Frozen-position JSD probe evaluation for PPO checkpoints."""

from __future__ import annotations

from dataclasses import dataclass
from math import log
from pathlib import Path

import polars as pl
import torch
import torch.nn as nn

CARD_SLOTS = 111
MODE_SLOTS = 5
COUNTRY_SLOTS = 86
_LOG2 = log(2.0)
_COUNTRY_ACTIVE_MODES = frozenset({0, 1, 2})


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


def _mean_or_zero(total: float, count: int) -> float:
    return total / count if count > 0 else 0.0


class ProbeEvaluator:
    """Evaluate JSD between two models at a frozen probe position set."""

    def __init__(
        self,
        probe_path: str | Path,
        device: str = "cpu",
        batch_size: int = 256,
    ):
        self.probe_path = Path(probe_path)
        self.device = torch.device(device)
        self.batch_size = batch_size

        frame = pl.read_parquet(self.probe_path)
        required = {
            "influence",
            "cards",
            "scalars",
            "card_mask",
            "mode_mask",
            "raw_turn",
            "side_int",
            "raw_defcon",
            "raw_vp",
        }
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

    def compare(
        self,
        model_a: nn.Module,
        model_b: nn.Module,
    ) -> ProbeMetrics:
        was_training_a = model_a.training
        was_training_b = model_b.training

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
                        country_active = (
                            (mode_ids == 0) | (mode_ids == 1) | (mode_ids == 2)
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
            n_positions=self.n_positions,
        )

    @staticmethod
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
