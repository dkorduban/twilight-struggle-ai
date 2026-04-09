from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import polars as pl
import torch
import torch.nn as nn

CARD_SLOTS = 111
MODE_SLOTS = 5
COUNTRY_SLOTS = 86
COUNTRY_HEAD_MODE_IDS = frozenset({0, 2, 3})

_VALID_COUNTRY_MASK = torch.ones(COUNTRY_SLOTS, dtype=torch.bool)
_VALID_COUNTRY_MASK[64] = False


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


class ProbeEvaluator:
    """Evaluate divergence between two models on a frozen probe set."""

    def __init__(
        self,
        probe_path: str | Path,
        device: str = "cpu",
        batch_size: int = 256,
    ) -> None:
        self.probe_path = Path(probe_path)
        if not self.probe_path.exists():
            raise FileNotFoundError(self.probe_path)

        df = pl.read_parquet(self.probe_path)
        if len(df) == 0:
            raise ValueError(f"Probe parquet is empty: {self.probe_path}")

        required = {
            "influence",
            "cards",
            "scalars",
            "raw_turn",
            "side_int",
            "raw_defcon",
            "raw_vp",
            "mode_id",
        }
        missing = sorted(required.difference(df.columns))
        if missing:
            raise ValueError(f"Probe parquet missing required columns: {missing}")

        self.device = torch.device(device)
        self.batch_size = batch_size
        self.n_positions = len(df)

        self.influence = torch.tensor(df["influence"].to_list(), dtype=torch.float32)
        self.cards = torch.tensor(df["cards"].to_list(), dtype=torch.float32)
        self.scalars = torch.tensor(df["scalars"].to_list(), dtype=torch.float32)
        self.raw_turn = torch.tensor(df["raw_turn"].to_list(), dtype=torch.int64)
        self.side_int = torch.tensor(df["side_int"].to_list(), dtype=torch.int64)
        self.raw_defcon = torch.tensor(df["raw_defcon"].to_list(), dtype=torch.int64)
        self.raw_vp = torch.tensor(df["raw_vp"].to_list(), dtype=torch.int64)
        self.mode_id = torch.tensor(df["mode_id"].to_list(), dtype=torch.int64)

        if "card_mask" in df.columns:
            self.card_mask = torch.tensor(df["card_mask"].to_list(), dtype=torch.bool)
        elif "hand_card_ids" in df.columns:
            self.card_mask = self._card_masks_from_hands(df["hand_card_ids"].to_list())
        else:
            self.card_mask = torch.ones((self.n_positions, CARD_SLOTS), dtype=torch.bool)

        if "mode_mask" in df.columns:
            self.mode_mask = torch.tensor(df["mode_mask"].to_list(), dtype=torch.bool)
        else:
            self.mode_mask = torch.ones((self.n_positions, MODE_SLOTS), dtype=torch.bool)

        self.country_mask = _VALID_COUNTRY_MASK.unsqueeze(0).expand(self.n_positions, -1).clone()

    def compare(
        self,
        model_a: nn.Module,
        model_b: nn.Module,
    ) -> ProbeMetrics:
        was_training_a = model_a.training
        was_training_b = model_b.training
        model_a.eval()
        model_b.eval()

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
        phase_card_jsd_sum = {"early": 0.0, "mid": 0.0, "late": 0.0}
        phase_card_jsd_count = {"early": 0, "mid": 0, "late": 0}

        with torch.no_grad():
            for start in range(0, self.n_positions, self.batch_size):
                end = min(start + self.batch_size, self.n_positions)
                batch_inf = self.influence[start:end].to(self.device)
                batch_cards = self.cards[start:end].to(self.device)
                batch_scalars = self.scalars[start:end].to(self.device)
                batch_card_mask = self.card_mask[start:end].to(self.device)
                batch_mode_mask = self.mode_mask[start:end].to(self.device)
                batch_country_mask = self.country_mask[start:end].to(self.device)
                batch_turn = self.raw_turn[start:end]
                batch_mode_ids = self.mode_id[start:end]

                out_a = self._forward_model(model_a, batch_inf, batch_cards, batch_scalars)
                out_b = self._forward_model(model_b, batch_inf, batch_cards, batch_scalars)

                card_valid = batch_card_mask.any(dim=1)
                if torch.any(card_valid):
                    card_jsd = self._jsd(out_a["card_logits"], out_b["card_logits"], batch_card_mask)
                    card_jsd_sum += float(card_jsd[card_valid].sum().item())
                    card_jsd_count += int(card_valid.sum().item())

                    top1_card_a = self._masked_argmax(out_a["card_logits"], batch_card_mask)
                    top1_card_b = self._masked_argmax(out_b["card_logits"], batch_card_mask)
                    top1_card_sum += float((top1_card_a[card_valid] == top1_card_b[card_valid]).float().sum().item())
                    top1_card_count += int(card_valid.sum().item())

                    phase_specs = {
                        "early": (batch_turn >= 1) & (batch_turn <= 3) & card_valid.cpu(),
                        "mid": (batch_turn >= 4) & (batch_turn <= 7) & card_valid.cpu(),
                        "late": (batch_turn >= 8) & (batch_turn <= 10) & card_valid.cpu(),
                    }
                    card_jsd_cpu = card_jsd.cpu()
                    for name, phase_mask in phase_specs.items():
                        if torch.any(phase_mask):
                            phase_card_jsd_sum[name] += float(card_jsd_cpu[phase_mask].sum().item())
                            phase_card_jsd_count[name] += int(phase_mask.sum().item())

                mode_valid = batch_mode_mask.any(dim=1)
                if torch.any(mode_valid):
                    mode_jsd = self._jsd(out_a["mode_logits"], out_b["mode_logits"], batch_mode_mask)
                    mode_jsd_sum += float(mode_jsd[mode_valid].sum().item())
                    mode_jsd_count += int(mode_valid.sum().item())

                    top1_mode_a = self._masked_argmax(out_a["mode_logits"], batch_mode_mask)
                    top1_mode_b = self._masked_argmax(out_b["mode_logits"], batch_mode_mask)
                    top1_mode_sum += float((top1_mode_a[mode_valid] == top1_mode_b[mode_valid]).float().sum().item())
                    top1_mode_count += int(mode_valid.sum().item())

                country_active = torch.isin(
                    batch_mode_ids,
                    torch.tensor(sorted(COUNTRY_HEAD_MODE_IDS), dtype=torch.int64),
                )
                if torch.any(country_active):
                    country_jsd = self._jsd(
                        out_a["country_logits"][country_active.to(self.device)],
                        out_b["country_logits"][country_active.to(self.device)],
                        batch_country_mask[country_active.to(self.device)],
                    )
                    country_jsd_sum += float(country_jsd.sum().item())
                    country_jsd_count += int(country_active.sum().item())

                value_a = out_a["value"].squeeze(-1)
                value_b = out_b["value"].squeeze(-1)
                value_mae_sum += float(torch.abs(value_a - value_b).sum().item())
                value_mae_count += end - start

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
            n_positions=self.n_positions,
        )

    @staticmethod
    def _jsd(p: torch.Tensor, q: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        """Compute masked JSD(P||Q) in [0, 1] for each row."""
        if p.shape != q.shape or p.shape != mask.shape:
            raise ValueError(
                f"Shape mismatch for JSD: p={tuple(p.shape)} q={tuple(q.shape)} mask={tuple(mask.shape)}"
            )

        p_probs = ProbeEvaluator._masked_probs(p, mask)
        q_probs = ProbeEvaluator._masked_probs(q, mask)
        mix = 0.5 * (p_probs + q_probs)

        safe_p = torch.clamp(p_probs, min=1e-10)
        safe_q = torch.clamp(q_probs, min=1e-10)
        safe_mix = torch.clamp(mix, min=1e-10)

        kl_pm = (p_probs * (safe_p.log() - safe_mix.log())).sum(dim=1)
        kl_qm = (q_probs * (safe_q.log() - safe_mix.log())).sum(dim=1)
        jsd = 0.5 * (kl_pm + kl_qm) / math.log(2.0)
        jsd = torch.clamp(jsd, min=0.0, max=1.0)

        valid = mask.any(dim=1)
        jsd[~valid] = 0.0
        return jsd

    @staticmethod
    def _card_masks_from_hands(hand_card_ids: list[list[int] | None]) -> torch.Tensor:
        card_masks = torch.zeros((len(hand_card_ids), CARD_SLOTS), dtype=torch.bool)
        for row_idx, hand in enumerate(hand_card_ids):
            if hand is None:
                card_masks[row_idx] = True
                continue
            for card_id in hand:
                if 1 <= int(card_id) <= CARD_SLOTS:
                    card_masks[row_idx, int(card_id) - 1] = True
        return card_masks

    @staticmethod
    def _masked_argmax(logits: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        masked_logits = logits.masked_fill(~mask, float("-inf"))
        return masked_logits.argmax(dim=1)

    @staticmethod
    def _masked_probs(logits: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        masked_logits = torch.where(mask, logits, torch.zeros_like(logits))
        probs = torch.softmax(masked_logits, dim=1)
        probs = probs * mask.to(dtype=probs.dtype)
        probs = probs / probs.sum(dim=1, keepdim=True).clamp(min=1e-10)
        return probs

    @staticmethod
    def _mean_or_nan(total: float, count: int) -> float:
        if count == 0:
            return float("nan")
        return total / count

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
            expected_scalars = int(scalar_encoder.in_features)

        if scalars.shape[1] < expected_scalars:
            pad = torch.zeros(
                (scalars.shape[0], expected_scalars - scalars.shape[1]),
                dtype=scalars.dtype,
                device=scalars.device,
            )
            model_scalars = torch.cat([scalars, pad], dim=1)
        else:
            model_scalars = scalars[:, :expected_scalars]

        return model(influence, cards, model_scalars)
