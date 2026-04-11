"""Experiment tracking: append-only JSONL log at results/experiments.jsonl.

Each line is one experiment with hypothesis, git SHA, command, W&B ID, and result.
"""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

LOG_PATH = Path("results/experiments.jsonl")


def get_git_sha() -> Optional[str]:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True, timeout=5
        ).strip()
    except Exception:
        return None


def log_experiment_start(
    name: str,
    hypothesis: str,
    command: str,
    wandb_id: Optional[str] = None,
    parent: Optional[str] = None,
    log_path: Path = LOG_PATH,
) -> None:
    """Call before launching training. hypothesis is REQUIRED — must explain why this will help."""
    entry = {
        "name": name,
        "hypothesis": hypothesis,
        "git_sha": get_git_sha(),
        "command": command,
        "wandb_id": wandb_id,
        "parent": parent,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "finished_at": None,
        "result_summary": None,
        "status": "running",
    }
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")


def log_experiment_end(
    name: str,
    result_summary: str,
    status: str = "completed",
    log_path: Path = LOG_PATH,
) -> None:
    """Call after training + benchmark complete. result_summary: e.g. 'Elo 2145, USSR 52%, US 3%'."""
    if not log_path.exists():
        return
    lines = log_path.read_text().strip().splitlines()
    updated = []
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            updated.append(line)
            continue
        if entry.get("name") == name and entry.get("finished_at") is None:
            entry["finished_at"] = datetime.now(timezone.utc).isoformat()
            entry["result_summary"] = result_summary
            entry["status"] = status
        updated.append(json.dumps(entry))
    log_path.write_text("\n".join(updated) + "\n")
