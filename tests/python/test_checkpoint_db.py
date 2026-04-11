import json
from pathlib import Path
import pytest
from tsrl.checkpoint_db import log_checkpoint, log_benchmark, log_elo_rating, _get_db


def test_log_checkpoint_creates_db(tmp_path):
    db = tmp_path / "meta.sqlite3"
    log_checkpoint("ckpt_v1", tmp_path / "model.pt", {"lr": 1e-4}, db_path=db)
    assert db.exists()


def test_log_checkpoint_records_fields(tmp_path):
    db = tmp_path / "meta.sqlite3"
    model_file = tmp_path / "model.pt"
    model_file.write_bytes(b"fake")
    log_checkpoint("ckpt_v1", model_file, {"lr": 1e-4, "batch_size": 32}, wandb_run_id="abc123", parent_name="ckpt_v0", db_path=db)
    conn = _get_db(db)
    row = conn.execute("SELECT name, wandb_run_id, parent_name, hyperparams, file_hash FROM checkpoints WHERE name='ckpt_v1'").fetchone()
    conn.close()
    assert row is not None
    name, wandb_id, parent, hparams, fhash = row
    assert name == "ckpt_v1"
    assert wandb_id == "abc123"
    assert parent == "ckpt_v0"
    assert json.loads(hparams)["lr"] == 1e-4
    assert fhash is not None  # file exists so hash should be set


def test_log_benchmark(tmp_path):
    db = tmp_path / "meta.sqlite3"
    log_benchmark("ckpt_v1", "heuristic", "USSR", 100, 60, draws=5, db_path=db)
    conn = _get_db(db)
    row = conn.execute("SELECT checkpoint_name, wins, draws FROM benchmarks").fetchone()
    conn.close()
    assert row == ("ckpt_v1", 60, 5)


def test_log_elo_rating(tmp_path):
    db = tmp_path / "meta.sqlite3"
    log_elo_rating("ckpt_v1", 2100.5, ci_lo=2050.0, ci_hi=2150.0, db_path=db)
    conn = _get_db(db)
    row = conn.execute("SELECT checkpoint_name, elo, ci_lo, ci_hi FROM elo_ratings").fetchone()
    conn.close()
    assert row == ("ckpt_v1", 2100.5, 2050.0, 2150.0)


def test_multiple_checkpoints_same_name(tmp_path):
    db = tmp_path / "meta.sqlite3"
    log_checkpoint("ckpt_v1", tmp_path / "model.pt", {"lr": 1e-4}, db_path=db)
    log_checkpoint("ckpt_v1", tmp_path / "model.pt", {"lr": 2e-4}, db_path=db)
    conn = _get_db(db)
    rows = conn.execute("SELECT id FROM checkpoints WHERE name='ckpt_v1'").fetchall()
    conn.close()
    assert len(rows) == 2  # both stored, not overwritten
