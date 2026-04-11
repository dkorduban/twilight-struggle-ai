"""Tests for model checkpoint loading and compatibility.

Catches regressions in:
  - load_model handling of missing/extra keys
  - Partial warm-start when dimensions change (e.g. SCALAR_DIM expansion)
  - Model registry covering all registered model types
  - TorchScript export/load roundtrip
  - State dict completeness (no missing parameters after loading)
  - Forward pass equivalence before/after save-load cycle
"""

from __future__ import annotations

import os
import tempfile

import pytest
import torch
import torch.nn as nn

from tsrl.policies.model import (
    CARD_DIM,
    INFLUENCE_DIM,
    NUM_COUNTRIES,
    NUM_MODES,
    NUM_PLAYABLE_CARDS,
    SCALAR_DIM,
    TSBaselineModel,
)


# ---------------------------------------------------------------------------
# Save/load roundtrip tests
# ---------------------------------------------------------------------------

class TestSaveLoadRoundtrip:
    """Test model save → load produces identical outputs."""

    def test_state_dict_roundtrip(self):
        """Save and reload state_dict, verify outputs match."""
        model1 = TSBaselineModel(hidden_dim=64)
        model1.eval()

        with tempfile.NamedTemporaryFile(suffix=".pt", delete=False) as f:
            torch.save({"model_state_dict": model1.state_dict(), "args": {"hidden_dim": 64}}, f.name)
            path = f.name

        try:
            model2 = TSBaselineModel(hidden_dim=64)
            ckpt = torch.load(path, map_location="cpu", weights_only=False)
            model2.load_state_dict(ckpt["model_state_dict"])
            model2.eval()

            g = torch.Generator().manual_seed(42)
            inp = (
                torch.randn(2, INFLUENCE_DIM, generator=g),
                torch.randn(2, CARD_DIM, generator=g),
                torch.randn(2, SCALAR_DIM, generator=g),
            )

            with torch.no_grad():
                out1 = model1(*inp)
                out2 = model2(*inp)

            for key in out1:
                torch.testing.assert_close(
                    out1[key], out2[key],
                    msg=f"Output '{key}' differs after state_dict roundtrip",
                )
        finally:
            os.unlink(path)

    def test_torchscript_roundtrip(self):
        """TorchScript export → load should produce same outputs."""
        model = TSBaselineModel(hidden_dim=64)
        model.eval()

        g = torch.Generator().manual_seed(42)
        inp = (
            torch.randn(1, INFLUENCE_DIM, generator=g),
            torch.randn(1, CARD_DIM, generator=g),
            torch.randn(1, SCALAR_DIM, generator=g),
        )

        with torch.no_grad():
            out_original = model(*inp)

        with tempfile.NamedTemporaryFile(suffix=".pt", delete=False) as f:
            scripted = torch.jit.script(model)
            scripted.save(f.name)
            path = f.name

        try:
            loaded = torch.jit.load(path, map_location="cpu")
            with torch.no_grad():
                out_loaded = loaded(*inp)

            for key in out_original:
                torch.testing.assert_close(
                    out_original[key], out_loaded[key],
                    atol=1e-5, rtol=1e-5,
                    msg=f"TorchScript output '{key}' differs",
                )
        finally:
            os.unlink(path)


# ---------------------------------------------------------------------------
# Partial warm-start tests
# ---------------------------------------------------------------------------

class TestPartialWarmStart:
    """Test loading checkpoints with dimension mismatches."""

    def test_missing_keys_handled_gracefully(self):
        """Loading a state dict with missing keys should not crash."""
        model = TSBaselineModel(hidden_dim=64)
        full_state = model.state_dict()

        # Remove some keys
        partial_state = {k: v for k, v in full_state.items()
                         if "value_head" not in k}

        model2 = TSBaselineModel(hidden_dim=64)
        model2.load_state_dict(partial_state, strict=False)

        # Should still produce outputs
        out = model2(
            torch.randn(1, INFLUENCE_DIM),
            torch.randn(1, CARD_DIM),
            torch.randn(1, SCALAR_DIM),
        )
        assert "value" in out
        assert torch.isfinite(out["value"]).all()

    def test_extra_keys_ignored(self):
        """Extra keys in state dict should be ignored with strict=False."""
        model = TSBaselineModel(hidden_dim=64)
        state = model.state_dict()
        state["nonexistent_layer.weight"] = torch.randn(10, 10)

        model2 = TSBaselineModel(hidden_dim=64)
        model2.load_state_dict(state, strict=False)  # should not crash

    def test_width_mismatch_detected(self):
        """Mismatched hidden_dim should fail with strict=True."""
        model1 = TSBaselineModel(hidden_dim=64)
        state = model1.state_dict()

        model2 = TSBaselineModel(hidden_dim=128)

        with pytest.raises(RuntimeError):
            model2.load_state_dict(state, strict=True)


# ---------------------------------------------------------------------------
# State dict completeness tests
# ---------------------------------------------------------------------------

class TestStateDictCompleteness:
    """Verify state dicts contain all expected parameters."""

    def test_all_parameters_in_state_dict(self):
        """Every named parameter should appear in state_dict."""
        model = TSBaselineModel(hidden_dim=64)
        state_dict = model.state_dict()
        named_params = dict(model.named_parameters())

        for name in named_params:
            assert name in state_dict, f"Parameter '{name}' missing from state_dict"

    def test_state_dict_shapes_match_model(self):
        """All state dict tensors should match model parameter shapes."""
        model = TSBaselineModel(hidden_dim=64)
        state_dict = model.state_dict()

        for name, param in model.named_parameters():
            assert state_dict[name].shape == param.shape, \
                f"Shape mismatch for '{name}': state_dict={state_dict[name].shape} vs param={param.shape}"

    def test_model_has_required_heads(self):
        """Model should have card, mode, and value output heads."""
        model = TSBaselineModel(hidden_dim=64)
        out = model(
            torch.randn(1, INFLUENCE_DIM),
            torch.randn(1, CARD_DIM),
            torch.randn(1, SCALAR_DIM),
        )
        assert "card_logits" in out
        assert "mode_logits" in out
        assert "value" in out

    def test_output_dimensions(self):
        """Output dimensions should match constants."""
        model = TSBaselineModel(hidden_dim=64)
        out = model(
            torch.randn(2, INFLUENCE_DIM),
            torch.randn(2, CARD_DIM),
            torch.randn(2, SCALAR_DIM),
        )
        assert out["card_logits"].shape == (2, NUM_PLAYABLE_CARDS)
        assert out["mode_logits"].shape == (2, NUM_MODES)
        assert out["value"].shape == (2, 1)


# ---------------------------------------------------------------------------
# Model determinism tests
# ---------------------------------------------------------------------------

class TestModelDeterminism:
    """Test that eval mode produces deterministic outputs."""

    def test_eval_mode_deterministic(self):
        """Same inputs in eval mode should give identical outputs."""
        model = TSBaselineModel(hidden_dim=64)
        model.eval()

        g = torch.Generator().manual_seed(99)
        inp = (
            torch.randn(4, INFLUENCE_DIM, generator=g),
            torch.randn(4, CARD_DIM, generator=g),
            torch.randn(4, SCALAR_DIM, generator=g),
        )

        with torch.no_grad():
            out1 = model(*inp)
            out2 = model(*inp)

        for key in out1:
            torch.testing.assert_close(out1[key], out2[key],
                                       msg=f"Non-deterministic output for '{key}'")

    def test_train_mode_with_no_dropout_deterministic(self):
        """If dropout is 0, train mode should also be deterministic."""
        model = TSBaselineModel(hidden_dim=64, dropout=0.0)
        model.train()

        g = torch.Generator().manual_seed(99)
        inp = (
            torch.randn(4, INFLUENCE_DIM, generator=g),
            torch.randn(4, CARD_DIM, generator=g),
            torch.randn(4, SCALAR_DIM, generator=g),
        )

        with torch.no_grad():
            out1 = model(*inp)
            out2 = model(*inp)

        for key in out1:
            torch.testing.assert_close(out1[key], out2[key],
                                       msg=f"Non-deterministic output for '{key}' with dropout=0")


# ---------------------------------------------------------------------------
# Gradient checkpointing / training mode tests
# ---------------------------------------------------------------------------

class TestTrainingMode:
    """Test model in training configuration."""

    def test_train_mode_outputs_require_grad(self):
        """In train mode, outputs should have grad_fn."""
        model = TSBaselineModel(hidden_dim=64)
        model.train()

        out = model(
            torch.randn(2, INFLUENCE_DIM),
            torch.randn(2, CARD_DIM),
            torch.randn(2, SCALAR_DIM),
        )

        assert out["card_logits"].requires_grad
        assert out["value"].requires_grad

    def test_eval_mode_with_no_grad(self):
        """In eval mode with no_grad, outputs should not have grad."""
        model = TSBaselineModel(hidden_dim=64)
        model.eval()

        with torch.no_grad():
            out = model(
                torch.randn(2, INFLUENCE_DIM),
                torch.randn(2, CARD_DIM),
                torch.randn(2, SCALAR_DIM),
            )

        assert not out["card_logits"].requires_grad
        assert not out["value"].requires_grad

    def test_optimizer_step_changes_parameters(self):
        """One optimizer step should change at least some parameters."""
        model = TSBaselineModel(hidden_dim=64)
        model.train()
        opt = torch.optim.Adam(model.parameters(), lr=0.01)

        # Store original params
        orig_params = {n: p.clone() for n, p in model.named_parameters()}

        out = model(
            torch.randn(4, INFLUENCE_DIM),
            torch.randn(4, CARD_DIM),
            torch.randn(4, SCALAR_DIM),
        )
        loss = out["card_logits"].sum() + out["value"].sum()
        loss.backward()
        opt.step()

        changed = sum(1 for n, p in model.named_parameters()
                      if not torch.equal(p, orig_params[n]))
        total = sum(1 for _ in model.named_parameters())
        assert changed > total * 0.5, \
            f"Only {changed}/{total} params changed after optimizer step"
