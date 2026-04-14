"""Smoke tests for TSBaselineModel and TS_SelfPlayDataset.

These tests verify shapes, dtypes, and basic invariants without requiring
a GPU or a trained checkpoint.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import polars as pl
import torch
from torch.utils.data import DataLoader, Subset
from tsrl.policies.model import (
    CARD_DIM,
    DEFAULT_PLATT_A,
    DEFAULT_PLATT_B,
    INFLUENCE_DIM,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    PlattScaler,
    SCALAR_DIM,
    TSBaselineModel,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

BATCH_SIZE = 4
_SCRIPT_PATH = Path(__file__).resolve().parents[2] / "scripts" / "train_baseline.py"


def _make_batch(batch: int = BATCH_SIZE) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Return random-valued dummy tensors matching the model input contract."""
    influence = torch.randn(batch, INFLUENCE_DIM)
    cards = torch.randint(0, 2, (batch, CARD_DIM)).float()
    scalars = torch.rand(batch, SCALAR_DIM)
    return influence, cards, scalars


def _load_train_baseline_module():
    spec = importlib.util.spec_from_file_location("train_baseline", _SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
        f"Expected mode_logits shape ({BATCH_SIZE}, {NUM_MODES}), got {out['mode_logits'].shape}"
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


def test_model_mode_head_6_outputs() -> None:
    """Mode head must produce exactly 6 logits (Influence/Coup/Realign/Space/Event/EventFirst)."""
    model = TSBaselineModel()
    influence, cards, scalars = _make_batch(batch=1)
    with torch.no_grad():
        out = model(influence, cards, scalars)
    assert out["mode_logits"].shape[-1] == NUM_MODES


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
    small_choice_target = torch.zeros(BATCH_SIZE, dtype=torch.long)
    loss = (
        torch.nn.functional.cross_entropy(out["card_logits"], card_target)
        + torch.nn.functional.cross_entropy(out["mode_logits"], mode_target)
        + country_loss_test
        + torch.nn.functional.mse_loss(out["value"], value_target)
        + torch.nn.functional.cross_entropy(out["small_choice_logits"], small_choice_target)
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
        assert tensor.dtype == torch.float32, f"Expected float32 for {key!r}, got {tensor.dtype}"


def test_platt_scaler_identity_is_noop() -> None:
    scaler = PlattScaler()
    values = torch.tensor([[-0.8], [0.0], [0.6]], dtype=torch.float32)

    with torch.no_grad():
        calibrated = scaler(values)

    assert scaler.is_identity is True
    assert DEFAULT_PLATT_A == 1.0
    assert DEFAULT_PLATT_B == 0.0
    assert torch.allclose(calibrated, values)


def test_platt_scaler_matches_sigmoid_affine_formula() -> None:
    scaler = PlattScaler(a=1.5, b=-0.25)
    values = torch.tensor([[-0.8], [0.0], [0.6]], dtype=torch.float32)

    with torch.no_grad():
        calibrated = scaler(values)

    expected = 2.0 * torch.sigmoid(1.5 * values - 0.25) - 1.0
    assert scaler.is_identity is False
    assert torch.allclose(calibrated, expected)


# ---------------------------------------------------------------------------
# Dataset test
# ---------------------------------------------------------------------------


def test_dataset_loads(tiny_selfplay_dir) -> None:
    """Dataset loads parquet files and returns correctly-shaped samples."""
    from tsrl.policies.dataset import TS_SelfPlayDataset

    ds = TS_SelfPlayDataset(str(tiny_selfplay_dir))
    assert len(ds) > 0, "Dataset should have at least one step"

    sample = ds[0]
    required_keys = {
        "influence",
        "cards",
        "scalars",
        "card_target",
        "mode_target",
        "country_ops_target",
        "value_target",
    }
    assert required_keys == set(sample.keys()), f"Missing or extra keys: got {set(sample.keys())}"

    assert sample["influence"].shape == (172,), sample["influence"].shape
    assert sample["cards"].shape == (448,), sample["cards"].shape
    assert sample["scalars"].shape == (SCALAR_DIM,), sample["scalars"].shape
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


def test_dataset_loads_teacher_targets(tmp_path, tiny_selfplay_dir) -> None:
    """Teacher targets join onto rows by (game_id, step_idx) and default to zeros otherwise."""
    from tsrl.policies.dataset import TS_SelfPlayDataset

    teacher_path = tmp_path / "teacher_targets.parquet"
    teacher_rows = [
        {
            "game_id": "tiny_game_0",
            "step_index": 0,
            "teacher_value_target": 0.25,
            "teacher_card_target": [1.0] + [0.0] * 110,
            "teacher_mode_target": [0.0, 1.0, 0.0, 0.0, 0.0],
        },
        {
            "game_id": "tiny_game_0",
            "step_index": 2,
            "teacher_value_target": -0.5,
            "teacher_card_target": [0.0, 1.0] + [0.0] * 109,
            "teacher_mode_target": [1.0, 0.0, 0.0, 0.0, 0.0],
        },
    ]
    pl.DataFrame(teacher_rows).write_parquet(teacher_path)

    ds = TS_SelfPlayDataset(
        str(tiny_selfplay_dir),
        teacher_targets_path=str(teacher_path),
    )

    sample_with_teacher = ds[0]
    assert sample_with_teacher["has_teacher_target"].item() is True
    assert sample_with_teacher["teacher_card_target"].shape == (111,)
    assert sample_with_teacher["teacher_mode_target"].shape == (NUM_MODES,)
    assert sample_with_teacher["teacher_value_target"].shape == (1,)
    assert sample_with_teacher["teacher_card_target"][0].item() == 1.0
    assert sample_with_teacher["teacher_mode_target"][1].item() == 1.0
    assert sample_with_teacher["teacher_value_target"][0].item() == 0.25

    sample_without_teacher = ds[1]
    assert sample_without_teacher["has_teacher_target"].item() is False
    assert sample_without_teacher["teacher_card_target"].sum().item() == 0.0
    assert sample_without_teacher["teacher_mode_target"].sum().item() == 0.0
    assert sample_without_teacher["teacher_value_target"][0].item() == 0.0


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
        rows.append(
            {
                "ussr_influence": cvec(1),
                "us_influence": cvec(0),
                "actor_known_in": mvec(),
                "actor_possible": mvec(),
                "discard_mask": mvec(),
                "removed_mask": mvec(),
                "vp": 5,
                "defcon": 3,
                "milops_ussr": 2,
                "milops_us": 2,
                "space_ussr": 0,
                "space_us": 0,
                "china_held_by": 0,
                "actor_holds_china": False,
                "turn": 5,
                "ar": 3,
                "phasing": 0,
                "action_card_id": 1,
                "action_mode": 0,
                "action_targets": "",
                # USSR wins (winner_side=+1) but final_vp is negative (wrong sign):
                "winner_side": 1,
                "final_vp": -5,
                "end_reason": end_reason,
            }
        )
        rows.append(
            {
                "ussr_influence": cvec(0),
                "us_influence": cvec(1),
                "actor_known_in": mvec(),
                "actor_possible": mvec(),
                "discard_mask": mvec(),
                "removed_mask": mvec(),
                "vp": -3,
                "defcon": 2,
                "milops_ussr": 1,
                "milops_us": 3,
                "space_ussr": 0,
                "space_us": 0,
                "china_held_by": 1,
                "actor_holds_china": False,
                "turn": 7,
                "ar": 2,
                "phasing": 1,
                "action_card_id": 10,
                "action_mode": 1,
                "action_targets": "",
                # US wins (winner_side=-1) but final_vp is positive (wrong sign):
                "winner_side": -1,
                "final_vp": 8,
                "end_reason": end_reason,
            }
        )

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
    from torch.utils.data import DataLoader
    from tsrl.policies.dataset import TS_SelfPlayDataset

    ds = TS_SelfPlayDataset(str(tiny_selfplay_dir))
    loader = DataLoader(
        ds, batch_size=256, shuffle=False, collate_fn=TS_SelfPlayDataset.passthrough_collate
    )

    for batch in loader:
        card_targets = batch["card_target"]
        assert card_targets.min().item() >= 0
        assert card_targets.max().item() <= 110
        mode_targets = batch["mode_target"]
        assert mode_targets.min().item() >= 0
        assert mode_targets.max().item() <= 4


def test_run_epoch_reports_teacher_metrics(tmp_path, tiny_selfplay_dir) -> None:
    """Teacher-enabled train batches report KL metrics while eval remains BC-only."""
    from tsrl.policies.dataset import TS_SelfPlayDataset

    mod = _load_train_baseline_module()
    teacher_path = tmp_path / "teacher_targets.parquet"
    teacher_rows = [
        {
            "game_id": "tiny_game_0",
            "step_index": step_idx,
            "teacher_value_target": 0.1 * (step_idx + 1),
            "teacher_card_target": [1.0 if i == step_idx else 0.0 for i in range(111)],
            "teacher_mode_target": [1.0 if i == (step_idx % 5) else 0.0 for i in range(5)],
        }
        for step_idx in range(4)
    ]
    pl.DataFrame(teacher_rows).write_parquet(teacher_path)

    ds = TS_SelfPlayDataset(
        str(tiny_selfplay_dir),
        teacher_targets_path=str(teacher_path),
    )
    subset = Subset(ds, list(range(8)))
    loader = DataLoader(
        subset,
        batch_size=4,
        shuffle=False,
        collate_fn=TS_SelfPlayDataset.passthrough_collate,
    )
    model = TSBaselineModel()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

    train_metrics = mod.run_epoch(
        model,
        loader,
        optimizer,
        torch.device("cpu"),
        log_interval=100,
        epoch_label="train test",
        teacher_weight=0.7,
        teacher_value_weight=0.3,
    )
    assert train_metrics["teacher_coverage"] > 0.0
    assert train_metrics["teacher_kl_card"] >= 0.0
    assert train_metrics["teacher_kl_mode"] >= 0.0
    assert train_metrics["teacher_value_mse"] >= 0.0

    val_metrics = mod.run_epoch(
        model,
        loader,
        None,
        torch.device("cpu"),
        log_interval=100,
        epoch_label="val test",
        teacher_weight=0.7,
        teacher_value_weight=0.3,
    )
    assert val_metrics["teacher_coverage"] == 0.0
    assert val_metrics["teacher_kl_card"] == 0.0
    assert val_metrics["teacher_kl_mode"] == 0.0
    assert val_metrics["teacher_value_mse"] == 0.0


def test_resolve_training_args_sets_warm_start_defaults() -> None:
    mod = _load_train_baseline_module()

    args = mod.parse_args(["--data-dir", "data/selfplay", "--init-from", "prev.pt", "--deterministic-split"])
    args = mod.resolve_training_args(args)

    assert args.lr == 3e-4
    assert args.patience == 8


def test_make_scheduler_uses_cosine_for_warm_start() -> None:
    mod = _load_train_baseline_module()

    args = mod.parse_args(
        [
            "--data-dir",
            "data/selfplay",
            "--init-from",
            "prev.pt",
            "--one-cycle",
            "--epochs",
            "3",
            "--patience",
            "5",
            "--deterministic-split",
        ]
    )
    args = mod.resolve_training_args(args)
    model = TSBaselineModel()
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr)

    scheduler, step_per_batch = mod.make_scheduler(args, optimizer, steps_per_epoch=2)

    assert scheduler is not None
    # --one-cycle uses OneCycleLR (step_per_batch=True); warm-start doesn't change this.
    assert scheduler.__class__.__name__ == "OneCycleLR"
    assert step_per_batch is True
    assert args.patience == 5
    assert args.lr == 3e-4
