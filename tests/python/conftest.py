"""Pytest configuration for the tsrl test suite."""
from __future__ import annotations

import os
import random
from pathlib import Path

import polars as pl
import pytest


# ---------------------------------------------------------------------------
# Worker nice-ness (xdist workers only)
# ---------------------------------------------------------------------------

def pytest_configure(config):
    """Register the tsrl_nice_workers plugin if xdist is available."""
    config.pluginmanager.register(_NiceWorkersPlugin(), "tsrl_nice_workers")


class _NiceWorkersPlugin:
    """Lower the OS priority of xdist worker processes.

    Each worker detects that it *is* a worker via the ``workerinput`` attribute
    that xdist sets on the config object, then calls ``os.nice(10)`` once.
    This keeps parallel test runs from starving interactive processes.
    """

    def pytest_sessionstart(self, session):
        if getattr(session.config, "workerinput", None) is not None:
            # We are inside an xdist worker subprocess — lower priority.
            try:
                os.nice(10)
            except OSError:
                pass  # non-Unix or permission denied; ignore silently


# ---------------------------------------------------------------------------
# @pytest.mark.serial support
# ---------------------------------------------------------------------------

def pytest_collection_modifyitems(config, items):
    """Move @pytest.mark.serial tests to the 'serial' xdist group.

    xdist routes items with ``pytest.mark.xdist_group("serial")`` to a single
    worker, preserving ordering and preventing parallel interference.
    """
    for item in items:
        if item.get_closest_marker("serial"):
            item.add_marker(pytest.mark.xdist_group("serial"))


# ---------------------------------------------------------------------------
# Synthetic self-play dataset fixture
# ---------------------------------------------------------------------------

_COUNTRY_LEN = 84
_CARD_LEN = 112
_ROW_COUNT = 50


@pytest.fixture(scope="session")
def tiny_selfplay_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Create a minimal self-play parquet directory for dataset tests."""
    out_dir = tmp_path_factory.mktemp("tiny_selfplay")
    parquet_path = out_dir / "tiny_selfplay.parquet"
    rng = random.Random(0)

    def country_vec(offset: int) -> list[int]:
        return [int((idx + offset) % 4) for idx in range(_COUNTRY_LEN)]

    def mask_vec(period: int, offset: int) -> list[int]:
        return [1 if (idx + offset) % period == 0 else 0 for idx in range(_CARD_LEN)]

    rows: list[dict[str, object]] = []
    target_patterns = ("", "1", "2,3", "10,10,11", "84")
    for row_idx in range(_ROW_COUNT):
        rows.append(
            {
                "ussr_influence": country_vec(row_idx),
                "us_influence": country_vec(row_idx + 1),
                "actor_known_in": mask_vec(2, row_idx),
                "actor_possible": mask_vec(3, row_idx),
                "discard_mask": mask_vec(5, row_idx),
                "removed_mask": mask_vec(7, row_idx),
                "vp": (row_idx % 41) - 20,
                "defcon": (row_idx % 5) + 1,
                "milops_ussr": row_idx % 7,
                "milops_us": (row_idx + 3) % 7,
                "space_ussr": row_idx % 10,
                "space_us": (row_idx + 4) % 10,
                "china_held_by": row_idx % 2,
                "actor_holds_china": bool((row_idx + 1) % 2),
                "turn": (row_idx % 10) + 1,
                "ar": row_idx % 9,
                "phasing": row_idx % 2,
                "action_card_id": (row_idx % 111) + 1,
                "action_mode": row_idx % 5,
                "action_targets": rng.choice(target_patterns),
                "winner_side": (-1, 0, 1)[row_idx % 3],
                "final_vp": ((row_idx * 3) % 41) - 20,
            }
        )

    pl.DataFrame(rows).write_parquet(parquet_path)
    return out_dir
