"""Focused tests for autotune campaign bookkeeping."""

from __future__ import annotations

import json
from dataclasses import fields

from tsrl.policies.autotune_minimal_hybrid import (
    ValidationSummary,
    _params_to_dict,
    _validation_sort_key,
)
from tsrl.policies.minimal_hybrid import DEFAULT_MINIMAL_HYBRID_PARAMS, MinimalHybridParams
from tsrl.policies.validate_minimal_hybrid_snapshot import _load_params


def test_snapshot_params_round_trip_preserves_full_parameter_surface(tmp_path):
    snapshot_path = tmp_path / "candidate.json"
    snapshot_path.write_text(
        json.dumps({"params": _params_to_dict(DEFAULT_MINIMAL_HYBRID_PARAMS)}),
        encoding="utf-8",
    )

    loaded = _load_params(snapshot_path)

    assert loaded == DEFAULT_MINIMAL_HYBRID_PARAMS
    assert set(_params_to_dict(DEFAULT_MINIMAL_HYBRID_PARAMS)) == {
        field.name for field in fields(MinimalHybridParams)
    }


def test_validation_sort_key_prefers_significant_candidate():
    non_significant = _validation_sort_key(
        ValidationSummary(
            label="non_sig",
            mean_score=0.20,
            ci_low=-0.05,
            ci_high=0.40,
            n_pairs=10,
            significant_positive=False,
            turn_cutoff=4,
        )
    )
    significant = _validation_sort_key(
        ValidationSummary(
            label="sig",
            mean_score=0.10,
            ci_low=0.01,
            ci_high=0.20,
            n_pairs=10,
            significant_positive=True,
            turn_cutoff=4,
        )
    )

    assert significant > non_significant
