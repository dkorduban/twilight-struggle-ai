from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import torch
import torch.nn as nn
import torch.nn.functional as F

from experimental.ppo.live import load_train_ppo_module


@dataclass
class PackedSteps:
    """Device-friendly dense representation of a rollout batch.

    The live trainer stores one Python ``Step`` object per decision point.
    That is convenient for collection, but expensive during PPO epochs because
    the same batch has to be re-stacked many times. ``PackedSteps`` pays the
    assembly cost once.
    """
    influence: torch.Tensor
    cards: torch.Tensor
    scalars: torch.Tensor
    card_masks: torch.Tensor
    mode_masks: torch.Tensor
    country_masks: torch.Tensor
    card_indices: torch.Tensor
    mode_indices: torch.Tensor
    country_targets: torch.Tensor
    country_valid: torch.Tensor
    old_log_probs: torch.Tensor
    advantages: torch.Tensor
    returns: torch.Tensor

    def to(self, device: torch.device | str) -> PackedSteps:
        """Move the whole packed batch to a device in one shot."""
        return PackedSteps(
            influence=self.influence.to(device),
            cards=self.cards.to(device),
            scalars=self.scalars.to(device),
            card_masks=self.card_masks.to(device),
            mode_masks=self.mode_masks.to(device),
            country_masks=self.country_masks.to(device),
            card_indices=self.card_indices.to(device),
            mode_indices=self.mode_indices.to(device),
            country_targets=self.country_targets.to(device),
            country_valid=self.country_valid.to(device),
            old_log_probs=self.old_log_probs.to(device),
            advantages=self.advantages.to(device),
            returns=self.returns.to(device),
        )


def pack_steps(steps: list[Any]) -> PackedSteps:
    """Pack rollout steps once so PPO epochs avoid per-minibatch Python stacking.

    This mirrors the data preparation embedded in the live ``ppo_update``:
    - per-side advantage normalization
    - dense mask tensors
    - padded variable-length country target lists
    """
    train_ppo = load_train_ppo_module()
    if not steps:
        raise ValueError("steps must be non-empty")

    advantages = torch.tensor([step.advantage for step in steps], dtype=torch.float32)
    returns = torch.tensor([step.returns for step in steps], dtype=torch.float32)
    advantages = advantages.nan_to_num(nan=0.0, posinf=10.0, neginf=-10.0)
    returns = returns.nan_to_num(nan=0.0, posinf=10.0, neginf=-10.0)

    side_ints = torch.tensor([step.side_int for step in steps], dtype=torch.long)
    for side_val in (0, 1):
        mask = side_ints == side_val
        if int(mask.sum().item()) > 1:
            mu = advantages[mask].mean()
            sigma = advantages[mask].std()
            advantages[mask] = (advantages[mask] - mu) / (sigma + 1e-8)

    max_targets = max((len(step.country_targets) for step in steps), default=0)
    target_pad = torch.zeros((len(steps), max_targets), dtype=torch.long)
    target_valid = torch.zeros((len(steps), max_targets), dtype=torch.bool)
    for row, step in enumerate(steps):
        if not step.country_targets:
            continue
        targets = torch.tensor(step.country_targets, dtype=torch.long)
        target_pad[row, : len(targets)] = targets
        target_valid[row, : len(targets)] = True

    return PackedSteps(
        influence=torch.cat([step.influence for step in steps], dim=0),
        cards=torch.cat([step.cards for step in steps], dim=0),
        scalars=torch.cat([step.scalars for step in steps], dim=0),
        card_masks=torch.stack([step.card_mask for step in steps]),
        mode_masks=torch.stack([step.mode_mask for step in steps]),
        country_masks=torch.stack([
            step.country_mask if step.country_mask is not None
            else torch.zeros(train_ppo.COUNTRY_SLOTS, dtype=torch.bool)
            for step in steps
        ]),
        card_indices=torch.tensor([step.card_idx for step in steps], dtype=torch.long),
        mode_indices=torch.tensor([step.mode_idx for step in steps], dtype=torch.long),
        country_targets=target_pad,
        country_valid=target_valid,
        old_log_probs=torch.tensor([step.old_log_prob for step in steps], dtype=torch.float32),
        advantages=advantages,
        returns=returns,
    )


def ppo_update_packed(
    packed_steps: PackedSteps,
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: str,
    ppo_epochs: int = 4,
    clip_eps: float = 0.2,
    vf_coef: float = 0.5,
    ent_coef: float = 0.01,
    minibatch_size: int = 2048,
    perm_device: str | None = None,
) -> dict[str, float]:
    """Packed PPO update with device-resident tensors and vectorized minibatches.

    The intended comparison is with the live trainer's ``ppo_update``. The PPO
    objective is kept structurally the same; the main change is data movement:
    tensors are packed once, moved to device once, and minibatches are sliced by
    index instead of reconstructed from Python objects every time.
    """
    num_steps = packed_steps.influence.shape[0]
    if num_steps == 0:
        return {}

    packed = packed_steps.to(device)
    model.eval()
    perm_device = perm_device or device

    metrics = {
        "policy_loss": 0.0,
        "value_loss": 0.0,
        "entropy": 0.0,
        "clip_fraction": 0.0,
        "approx_kl": 0.0,
    }
    n_updates = 0

    for _ in range(ppo_epochs):
        # The live trainer samples minibatch permutations on CPU. Keeping this
        # configurable lets the equivalence check feed both implementations the
        # same minibatch ordering even when model execution happens on CUDA.
        perm = torch.randperm(num_steps, device=perm_device)
        for start in range(0, num_steps, minibatch_size):
            idx = perm[start:start + minibatch_size]
            idx_dev = idx.to(device) if idx.device.type != packed.influence.device.type else idx

            # ``index_select`` avoids rebuilding tensors from Python lists on
            # every minibatch and every PPO epoch.
            outputs = model(
                packed.influence.index_select(0, idx_dev),
                packed.cards.index_select(0, idx_dev),
                packed.scalars.index_select(0, idx_dev),
            )
            card_logits = outputs["card_logits"].nan_to_num(nan=0.0)
            mode_logits = outputs["mode_logits"].nan_to_num(nan=0.0)
            values = outputs["value"].squeeze(-1).nan_to_num(nan=0.0)
            country_logits = outputs.get("country_logits")
            if country_logits is not None:
                country_logits = country_logits.nan_to_num(nan=0.0)

            card_masks = packed.card_masks.index_select(0, idx_dev)
            mode_masks = packed.mode_masks.index_select(0, idx_dev)
            country_masks = packed.country_masks.index_select(0, idx_dev)
            card_indices = packed.card_indices.index_select(0, idx_dev)
            mode_indices = packed.mode_indices.index_select(0, idx_dev)
            old_log_probs = packed.old_log_probs.index_select(0, idx_dev)
            advantages = packed.advantages.index_select(0, idx_dev)
            returns = packed.returns.index_select(0, idx_dev)
            country_targets = packed.country_targets.index_select(0, idx_dev)
            country_valid = packed.country_valid.index_select(0, idx_dev)

            masked_card = card_logits.masked_fill(~card_masks, float("-inf"))
            masked_mode = mode_logits.masked_fill(~mode_masks, float("-inf"))

            log_prob_card = F.log_softmax(masked_card, dim=1).gather(
                1, card_indices.unsqueeze(1)
            ).squeeze(1)
            log_prob_mode = F.log_softmax(masked_mode, dim=1).gather(
                1, mode_indices.unsqueeze(1)
            ).squeeze(1)

            log_prob_country = torch.zeros_like(log_prob_card)
            ent_country = torch.zeros_like(log_prob_card)
            if country_logits is not None:
                # Country targets have variable length in the source Step
                # objects, so the packed representation stores a padded index
                # matrix plus a validity mask.
                country_probs = country_logits.masked_fill(~country_masks, 0.0)
                country_probs = country_probs / (
                    country_probs.sum(dim=1, keepdim=True) + 1e-10
                )
                log_country = torch.log(country_probs + 1e-10)
                ent_country = -(country_probs * log_country).sum(dim=1)
                if country_targets.shape[1] > 0:
                    gathered = log_country.gather(1, country_targets.clamp_min(0))
                    log_prob_country = (gathered * country_valid.float()).sum(dim=1)

            new_log_probs = log_prob_card + log_prob_mode + log_prob_country

            log_p_card = F.log_softmax(masked_card, dim=1).clamp(min=-20)
            log_p_mode = F.log_softmax(masked_mode, dim=1).clamp(min=-20)
            entropies = (
                -(log_p_card.exp() * log_p_card).sum(dim=1)
                -(log_p_mode.exp() * log_p_mode).sum(dim=1)
                + ent_country
            )

            ratio = torch.exp(new_log_probs - old_log_probs)
            clipped_ratio = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)
            policy_loss = -torch.min(ratio * advantages, clipped_ratio * advantages).mean()
            value_loss = F.mse_loss(values, returns)
            entropy_loss = -entropies.mean()
            loss = policy_loss + vf_coef * value_loss + ent_coef * entropy_loss

            if torch.isnan(loss):
                continue

            # ``set_to_none=True`` avoids unnecessary gradient tensor fills.
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=0.5)
            optimizer.step()

            with torch.no_grad():
                clip_frac = ((ratio - 1.0).abs() > clip_eps).float().mean().item()
                approx_kl = ((ratio - 1.0) - (new_log_probs - old_log_probs)).mean().item()

            metrics["policy_loss"] += float(policy_loss.item())
            metrics["value_loss"] += float(value_loss.item())
            metrics["entropy"] += float(entropies.mean().item())
            metrics["clip_fraction"] += clip_frac
            metrics["approx_kl"] += approx_kl
            n_updates += 1

    if n_updates == 0:
        return metrics
    for key in metrics:
        metrics[key] /= n_updates
    return metrics
