"""Checkpoint identity and metadata database.

Every checkpoint saved during training is logged here with full lineage.
DB lives at results/metadata.sqlite3 and is committed to git after Elo updates.
"""
import hashlib
import json
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

DB_PATH = Path("results/metadata.sqlite3")

SCHEMA = """
CREATE TABLE IF NOT EXISTS checkpoints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    git_sha TEXT,
    wandb_run_id TEXT,
    parent_name TEXT,
    file_hash TEXT,
    file_path TEXT,
    hyperparams TEXT,  -- JSON blob
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS benchmarks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    checkpoint_name TEXT NOT NULL,
    opponent TEXT NOT NULL,
    side TEXT NOT NULL,
    games INTEGER NOT NULL,
    wins INTEGER NOT NULL,
    draws INTEGER DEFAULT 0,
    elo_estimate REAL,
    run_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS elo_ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    checkpoint_name TEXT NOT NULL,
    elo REAL NOT NULL,
    ci_lo REAL,
    ci_hi REAL,
    computed_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_checkpoints_name ON checkpoints(name);
CREATE INDEX IF NOT EXISTS idx_benchmarks_name ON benchmarks(checkpoint_name);
"""


def _get_db(db_path: Path = DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


def get_git_sha() -> Optional[str]:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True, timeout=5
        ).strip()
    except Exception:
        return None


def hash_file(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def log_checkpoint(
    name: str,
    file_path: Path,
    hyperparams: dict,
    wandb_run_id: Optional[str] = None,
    parent_name: Optional[str] = None,
    db_path: Path = DB_PATH,
) -> None:
    """Log a checkpoint to the metadata DB. Call after torch.save()."""
    conn = _get_db(db_path)
    conn.execute(
        """INSERT INTO checkpoints (name, git_sha, wandb_run_id, parent_name, file_hash, file_path, hyperparams, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            name,
            get_git_sha(),
            wandb_run_id,
            parent_name,
            hash_file(file_path),
            str(file_path),
            json.dumps(hyperparams),
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    conn.commit()
    conn.close()


def log_benchmark(
    checkpoint_name: str,
    opponent: str,
    side: str,
    games: int,
    wins: int,
    draws: int = 0,
    elo_estimate: Optional[float] = None,
    db_path: Path = DB_PATH,
) -> None:
    """Log benchmark results. Call after benchmark completes."""
    conn = _get_db(db_path)
    conn.execute(
        """INSERT INTO benchmarks (checkpoint_name, opponent, side, games, wins, draws, elo_estimate, run_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            checkpoint_name,
            opponent,
            side,
            games,
            wins,
            draws,
            elo_estimate,
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    conn.commit()
    conn.close()


def log_elo_rating(
    checkpoint_name: str,
    elo: float,
    ci_lo: Optional[float] = None,
    ci_hi: Optional[float] = None,
    db_path: Path = DB_PATH,
) -> None:
    """Log a BayesElo rating after it's computed."""
    conn = _get_db(db_path)
    conn.execute(
        """INSERT INTO elo_ratings (checkpoint_name, elo, ci_lo, ci_hi, computed_at)
           VALUES (?, ?, ?, ?, ?)""",
        (
            checkpoint_name,
            elo,
            ci_lo,
            ci_hi,
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    conn.commit()
    conn.close()
