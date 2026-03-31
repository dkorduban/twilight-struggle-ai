"""Smoke tests for TSBaselineModel and TS_SelfPlayDataset.

These tests verify shapes, dtypes, and basic invariants without requiring
a GPU or a trained checkpoint.
"""

from __future__ import annotations

from pathlib import Path

import torch

from tsrl.policies.model import (
    CARD_DIM,
    INFLUENCE_DIM,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    SCALAR_DIM,
    TSBaselineModel,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

BATCH_SIZE = 4


def _make_batch(batch: int = BATCH_SIZE) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Return random-valued dummy tensors matching the model input contract."""
    influence = torch.randn(batch, INFLUENCE_DIM)
    cards = torch.randint(0, 2, (batch, CARD_DIM)).float()
    scalars = torch.rand(batch, SCALAR_DIM)
    return influence, cards, scalars


# ---------------------------------------------------------------------------
# Model tests
# ---------------------------------------------------------------------------


def test_model_forward_pass() -> None:
    """Output tensors have the correct shapes and value ranges."""
    model = TSBaselineModel()
    model.eval()

    influence, cards, scalars = _make_batch()
    with torch.no_grad():
        out = model(influence, cards, scalars)

    assert "card_logits" in out
    assert "mode_logits" in out
    assert "value" in out

    assert out["card_logits"].shape == (BATCH_SIZE, NUM_PLAYABLE_CARDS), (
        f"Expected card_logits shape ({BATCH_SIZE}, {NUM_PLAYABLE_CARDS}), "
        f"got {out['card_logits'].shape}"
    )
    assert out["mode_logits"].shape == (BATCH_SIZE, NUM_MODES), (
        f"Expected mode_logits shape ({BATCH_SIZE}, {NUM_MODES}), "
        f"got {out['mode_logits'].shape}"
    )
    assert out["value"].shape == (BATCH_SIZE, 1), (
        f"Expected value shape ({BATCH_SIZE}, 1), got {out['value'].shape}"
    )

    # tanh guarantees values in (-1, 1); use strict bounds with tiny margin
    assert out["value"].min().item() >= -1.0 - 1e-6
    assert out["value"].max().item() <= 1.0 + 1e-6


def test_model_card_head_111_outputs() -> None:
    """Card head must produce exactly 111 logits (cards 1..111 mapped 0-indexed)."""
    model = TSBaselineModel()
    influence, cards, scalars = _make_batch(batch=1)
    with torch.no_grad():
        out = model(influence, cards, scalars)
    assert out["card_logits"].shape[-1] == 111


def test_model_mode_head_5_outputs() -> None:
    """Mode head must produce exactly 5 logits."""
    model = TSBaselineModel()
    influence, cards, scalars = _make_batch(batch=1)
    with torch.no_grad():
        out = model(influence, cards, scalars)
    assert out["mode_logits"].shape[-1] == 5


def test_model_value_is_scalar_per_sample() -> None:
    """Value head produces one scalar per sample."""
    model = TSBaselineModel()
    influence, cards, scalars = _make_batch(batch=8)
    with torch.no_grad():
        out = model(influence, cards, scalars)
    assert out["value"].shape == (8, 1)


def test_model_gradient_flows() -> None:
    """Backward pass should not raise and gradients must be non-None."""
    model = TSBaselineModel()
    model.train()
    influence, cards, scalars = _make_batch()

    out = model(influence, cards, scalars)
    # Fake targets
    card_target = torch.zeros(BATCH_SIZE, dtype=torch.long)
    mode_target = torch.zeros(BATCH_SIZE, dtype=torch.long)
    value_target = torch.zeros(BATCH_SIZE, 1)

    country_ops_target = torch.zeros(BATCH_SIZE, 86, dtype=torch.float32)
    country_ops_target[:, 0] = 1.0
    ops_prob = country_ops_target / country_ops_target.sum(dim=1, keepdim=True)
    log_probs = torch.log_softmax(out["country_logits"], dim=1)
    country_loss_test = -(ops_prob * log_probs).sum(dim=1).mean()
    loss = (
        torch.nn.functional.cross_entropy(out["card_logits"], card_target)
        + torch.nn.functional.cross_entropy(out["mode_logits"], mode_target)
        + country_loss_test
        + torch.nn.functional.mse_loss(out["value"], value_target)
    )
    loss.backward()

    for name, param in model.named_parameters():
        assert param.grad is not None, f"No gradient for parameter {name!r}"


def test_model_output_dtype_float32() -> None:
    """All output tensors are float32."""
    model = TSBaselineModel()
    influence, cards, scalars = _make_batch()
    with torch.no_grad():
        out = model(influence, cards, scalars)
    for key, tensor in out.items():
        assert tensor.dtype == torch.float32, (
            f"Expected float32 for {key!r}, got {tensor.dtype}"
        )


# ---------------------------------------------------------------------------
# Dataset test
# ---------------------------------------------------------------------------


def test_dataset_loads(tiny_selfplay_dir) -> None:
    """Dataset loads parquet files and returns correctly-shaped samples."""
    from tsrl.policies.dataset import TS_SelfPlayDataset

    ds = TS_SelfPlayDataset(str(tiny_selfplay_dir))
    assert len(ds) > 0, "Dataset should have at least one step"

    sample = ds[0]
    required_keys = {"influence", "cards", "scalars", "card_target", "mode_target", "country_ops_target", "value_target"}
    assert required_keys == set(sample.keys()), (
        f"Missing or extra keys: got {set(sample.keys())}"
    )

    assert sample["influence"].shape == (172,), sample["influence"].shape
    assert sample["cards"].shape == (448,), sample["cards"].shape
    assert sample["scalars"].shape == (11,), sample["scalars"].shape
    assert sample["card_target"].dtype == torch.long
    assert sample["mode_target"].dtype == torch.long
    assert sample["country_ops_target"].shape == (86,)
    assert sample["country_ops_target"].dtype == torch.float32
    assert sample["value_target"].shape == (1,)
    assert sample["value_target"].dtype == torch.float32

    # card_target must be 0-indexed (0..110)
    assert 0 <= sample["card_target"].item() <= 110, (
        f"card_target out of range: {sample['card_target'].item()}"
    )
    # mode_target must be 0..4
    assert 0 <= sample["mode_target"].item() <= 4, (
        f"mode_target out of range: {sample['mode_target'].item()}"
    )
    # value_target is winner_side: -1, 0, or +1
    assert sample["value_target"].item() in {-1.0, 0.0, 1.0}, (
        f"value_target unexpected: {sample['value_target'].item()}"
    )


def test_dataset_final_vp_mode(tiny_selfplay_dir) -> None:
    """Dataset with value_target_mode='final_vp' returns values in [-1, 1]."""
    from tsrl.policies.dataset import TS_SelfPlayDataset

    ds = TS_SelfPlayDataset(str(tiny_selfplay_dir), value_target_mode="final_vp")
    assert len(ds) > 0

    for idx in range(min(100, len(ds))):
        sample = ds[idx]
        v = sample["value_target"].item()
        assert -1.0 <= v <= 1.0, f"value_target out of range: {v}"


def test_dataset_final_vp_sign_matches_winner_for_special_endgames(tmp_path) -> None:
    """For defcon1 / europe_control end reasons, value_target sign must match winner_side.

    These end conditions determine the winner by who triggered the condition,
    not by board VP — so using final_vp/20 directly would produce wrong-signed
    targets for ~60% of such games.  The dataset must use winner_side instead.
    """
    import polars as pl
    from tsrl.policies.dataset import TS_SelfPlayDataset

    _C = 86
    _K = 112

    def cvec(v: int) -> list[int]:
        return [v] * _C

    def mvec() -> list[int]:
        return [0] * _K

    # Build rows where winner_side and final_vp have *opposite* signs for
    # defcon1 / europe_control.  The dataset must return winner_side-signed targets.
    rows = []
    for end_reason in ("defcon1", "europe_control"):
        rows.append({
            "ussr_influence": cvec(1), "us_influence": cvec(0),
            "actor_known_in": mvec(), "actor_possible": mvec(),
            "discard_mask": mvec(), "removed_mask": mvec(),
            "vp": 5, "defcon": 3, "milops_ussr": 2, "milops_us": 2,
            "space_ussr": 0, "space_us": 0, "china_held_by": 0,
            "actor_holds_china": False, "turn": 5, "ar": 3, "phasing": 0,
            "action_card_id": 1, "action_mode": 0, "action_targets": "",
            # USSR wins (winner_side=+1) but final_vp is negative (wrong sign):
            "winner_side": 1, "final_vp": -5, "end_reason": end_reason,
        })
        rows.append({
            "ussr_influence": cvec(0), "us_influence": cvec(1),
            "actor_known_in": mvec(), "actor_possible": mvec(),
            "discard_mask": mvec(), "removed_mask": mvec(),
            "vp": -3, "defcon": 2, "milops_ussr": 1, "milops_us": 3,
            "space_ussr": 0, "space_us": 0, "china_held_by": 1,
            "actor_holds_china": False, "turn": 7, "ar": 2, "phasing": 1,
            "action_card_id": 10, "action_mode": 1, "action_targets": "",
            # US wins (winner_side=-1) but final_vp is positive (wrong sign):
            "winner_side": -1, "final_vp": 8, "end_reason": end_reason,
        })

    pq = tmp_path / "test_sign.parquet"
    pl.DataFrame(rows).write_parquet(str(pq))
    ds = TS_SelfPlayDataset(str(tmp_path), value_target_mode="final_vp")

    df = pl.read_parquet(str(pq))
    for idx in range(len(ds)):
        row = df.row(idx, named=True)
        winner = row["winner_side"]
        v = ds[idx]["value_target"].item()
        assert v * winner > 0, (
            f"row {idx}: value_target={v:.3f} disagrees with winner_side={winner} "
            f"(end_reason={row['end_reason']}, final_vp={row['final_vp']})"
        )


def test_dataset_all_card_targets_in_range(tiny_selfplay_dir) -> None:
    """All card_target values in the full dataset must be 0..110."""
    from tsrl.policies.dataset import TS_SelfPlayDataset
    from torch.utils.data import DataLoader

    ds = TS_SelfPlayDataset(str(tiny_selfplay_dir))
    loader = DataLoader(ds, batch_size=256, shuffle=False,
                        collate_fn=TS_SelfPlayDataset.passthrough_collate)

    for batch in loader:
        card_targets = batch["card_target"]
        assert card_targets.min().item() >= 0
        assert card_targets.max().item() <= 110
        mode_targets = batch["mode_target"]
        assert mode_targets.min().item() >= 0
        assert mode_targets.max().item() <= 4
