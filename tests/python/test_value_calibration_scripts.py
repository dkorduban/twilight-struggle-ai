from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np


def _load_script(name: str):
    script_path = Path(__file__).resolve().parents[2] / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fit_platt_reduces_ece_on_synthetic_bias():
    check_mod = _load_script("check_value_calibration")
    fit_mod = _load_script("fit_value_calibration")

    raw_preds = np.linspace(-0.8, 0.8, 401, dtype=np.float32)
    probs = 1.0 / (1.0 + np.exp(-(2.0 * raw_preds - 0.75)))
    actuals = (2.0 * probs - 1.0).astype(np.float32)

    before = check_mod.calibration_report(raw_preds, actuals, "synthetic before", n_bins=20)
    a, b = fit_mod.fit_platt(raw_preds, actuals)
    calibrated = check_mod.apply_platt_scaling(raw_preds, a, b)
    after = check_mod.calibration_report(calibrated, actuals, "synthetic after", n_bins=20)

    assert after["ece"] < before["ece"]
