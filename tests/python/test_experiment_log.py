import json
from pathlib import Path
from tsrl.experiment_log import log_experiment_start, log_experiment_end


def test_log_start_creates_file(tmp_path):
    log_path = tmp_path / "experiments.jsonl"
    log_experiment_start("run1", "Testing if X helps", "python train.py", log_path=log_path)
    assert log_path.exists()
    entry = json.loads(log_path.read_text().strip())
    assert entry["name"] == "run1"
    assert entry["status"] == "running"
    assert entry["finished_at"] is None


def test_log_end_updates_entry(tmp_path):
    log_path = tmp_path / "experiments.jsonl"
    log_experiment_start("run1", "Testing if X helps", "python train.py", log_path=log_path)
    log_experiment_end("run1", "Elo 2145, USSR 52%", log_path=log_path)
    entry = json.loads(log_path.read_text().strip())
    assert entry["status"] == "completed"
    assert entry["result_summary"] == "Elo 2145, USSR 52%"
    assert entry["finished_at"] is not None


def test_log_end_noop_if_no_match(tmp_path):
    log_path = tmp_path / "experiments.jsonl"
    # File doesn't exist — should be a no-op
    log_experiment_end("nonexistent", "result", log_path=log_path)
    assert not log_path.exists()


def test_log_start_hypothesis_required(tmp_path):
    """Hypothesis parameter must be passed (documented contract, not enforced)."""
    log_path = tmp_path / "experiments.jsonl"
    log_experiment_start("run1", hypothesis="My hypothesis", command="python train.py", log_path=log_path)
    entry = json.loads(log_path.read_text().strip())
    assert entry["hypothesis"] == "My hypothesis"
