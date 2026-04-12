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
    elo_ussr REAL,
    elo_us REAL,
    ci_lo REAL,
    ci_hi REAL,
    computed_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS rollout_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    checkpoint_name TEXT NOT NULL,
    iter_num INTEGER NOT NULL,
    ussr_wr REAL,
    us_wr REAL,
    combined_wr REAL,
    n_games INTEGER,
    logged_at TEXT NOT NULL
);

-- Each time run_elo_tournament.py runs, one row per tournament run.
CREATE TABLE IF NOT EXISTS tournaments (
    id TEXT PRIMARY KEY,              -- e.g. "incremental_20260411T183042Z_v67"
    run_at TEXT NOT NULL,
    mode TEXT,                        -- "incremental" | "full"
    new_model TEXT,                   -- model being placed (NULL for full round-robin)
    models_json TEXT,                 -- JSON list of all models in this run
    anchor TEXT,
    anchor_elo REAL,
    games_per_match INTEGER
);

-- One row per (model_a, model_b) pair per tournament.
-- model_a/model_b order matches the tournament script (not normalized here — use the view).
CREATE TABLE IF NOT EXISTS match_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tournament_id TEXT NOT NULL REFERENCES tournaments(id),
    model_a TEXT NOT NULL,
    model_b TEXT NOT NULL,
    wins_a INTEGER NOT NULL,
    wins_b INTEGER NOT NULL,
    draws INTEGER NOT NULL DEFAULT 0,
    wins_a_ussr INTEGER,
    wins_b_ussr INTEGER,
    wins_a_us INTEGER,
    wins_b_us INTEGER,
    n_games INTEGER NOT NULL,
    seed INTEGER,
    run_at TEXT NOT NULL
);

-- Per-tournament Elo snapshot for each model.
CREATE TABLE IF NOT EXISTS elo_ladder (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tournament_id TEXT NOT NULL REFERENCES tournaments(id),
    model TEXT NOT NULL,
    elo REAL NOT NULL,
    elo_ussr REAL,
    elo_us REAL,
    ci_lo REAL,
    ci_hi REAL,
    computed_at TEXT NOT NULL
);

-- Per-opponent, per-side rollout results for each training iteration.
-- Finer-grained than rollout_stats (aggregate). Never used for BayesElo —
-- hyperparams (temp, dir noise, PFSP sampling) differ from tournament games.
CREATE TABLE IF NOT EXISTS rollout_opponent_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,            -- e.g. "ppo_v67_league" (args.out_dir basename)
    checkpoint_name TEXT NOT NULL,   -- e.g. "v67_iter0120"
    iter_num INTEGER NOT NULL,
    opponent TEXT NOT NULL,          -- e.g. "v55_scripted", "heuristic", "self"
    side TEXT NOT NULL,              -- "ussr" | "us" | "both"
    wins INTEGER NOT NULL,
    losses INTEGER NOT NULL,
    draws INTEGER NOT NULL DEFAULT 0,
    n_games INTEGER NOT NULL,
    rollout_temp REAL,
    dir_alpha REAL,
    dir_epsilon REAL,
    git_sha TEXT,
    checkpoint_sha TEXT,             -- hash of the .pt file used for this rollout
    logged_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_ros_run ON rollout_opponent_stats(run_id);
CREATE INDEX IF NOT EXISTS idx_ros_checkpoint ON rollout_opponent_stats(checkpoint_name, iter_num);
CREATE INDEX IF NOT EXISTS idx_ros_opponent ON rollout_opponent_stats(opponent);

CREATE INDEX IF NOT EXISTS idx_rollout_checkpoint ON rollout_stats(checkpoint_name);
CREATE INDEX IF NOT EXISTS idx_checkpoints_name ON checkpoints(name);
CREATE INDEX IF NOT EXISTS idx_benchmarks_name ON benchmarks(checkpoint_name);
CREATE INDEX IF NOT EXISTS idx_match_results_tournament ON match_results(tournament_id);
CREATE INDEX IF NOT EXISTS idx_match_results_pair ON match_results(model_a, model_b);
CREATE INDEX IF NOT EXISTS idx_elo_ladder_model ON elo_ladder(model);
CREATE INDEX IF NOT EXISTS idx_elo_ladder_tournament ON elo_ladder(tournament_id);
"""

# Aggregate view DDL — created separately because executescript can't mix CREATE VIEW
# with IF NOT EXISTS in older sqlite3 versions reliably.
_MATCHUP_VIEW_DDL = """
CREATE VIEW IF NOT EXISTS matchup_aggregates AS
SELECT
    CASE WHEN model_a < model_b THEN model_a ELSE model_b END AS player_1,
    CASE WHEN model_a < model_b THEN model_b ELSE model_a END AS player_2,
    SUM(CASE WHEN model_a < model_b THEN wins_a ELSE wins_b END) AS p1_wins,
    SUM(CASE WHEN model_a < model_b THEN wins_b ELSE wins_a END) AS p2_wins,
    SUM(draws) AS draws,
    SUM(n_games) AS total_games,
    COUNT(*) AS n_tournaments
FROM match_results
GROUP BY player_1, player_2;
"""


def _ensure_column(
    conn: sqlite3.Connection,
    table_name: str,
    column_name: str,
    column_def: str,
) -> None:
    columns = {
        row[1] for row in conn.execute(f"PRAGMA table_info({table_name})").fetchall()
    }
    if column_name not in columns:
        conn.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_def}"
        )


def _get_db(db_path: Path = DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA)
    _ensure_column(conn, "elo_ratings", "elo_ussr", "REAL")
    _ensure_column(conn, "elo_ratings", "elo_us", "REAL")
    # Create aggregate view separately (CREATE VIEW IF NOT EXISTS is safe to re-run)
    conn.executescript(_MATCHUP_VIEW_DDL)
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


def log_rollout_wr(
    checkpoint_name: str,
    iter_num: int,
    ussr_wr: float,
    us_wr: float,
    combined_wr: float,
    n_games: int = 0,
    db_path: Path = DB_PATH,
) -> None:
    """Log per-iteration rollout win rates. Call after each training iteration."""
    conn = _get_db(db_path)
    conn.execute(
        """INSERT INTO rollout_stats (checkpoint_name, iter_num, ussr_wr, us_wr, combined_wr, n_games, logged_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            checkpoint_name,
            iter_num,
            ussr_wr,
            us_wr,
            combined_wr,
            n_games,
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    conn.commit()
    conn.close()


def log_rollout_opponent_stats(
    run_id: str,
    checkpoint_name: str,
    iter_num: int,
    opponent_results: list[dict],
    rollout_temp: float = 1.0,
    dir_alpha: float = 0.0,
    dir_epsilon: float = 0.0,
    checkpoint_sha: Optional[str] = None,
    db_path: Path = DB_PATH,
) -> None:
    """Log per-opponent, per-side rollout results for one training iteration.

    Args:
        run_id: Training run directory basename (e.g. "ppo_v67_league").
        checkpoint_name: Checkpoint name at this iteration (e.g. "v67_iter0120").
        iter_num: Training iteration number.
        opponent_results: List of dicts, one per opponent slot:
            {"opponent": str, "side": str, "wins": int, "losses": int,
             "draws": int, "n_games": int}
        rollout_temp: Temperature used for rollout sampling.
        dir_alpha: Dirichlet alpha for root noise (0 = disabled).
        dir_epsilon: Dirichlet epsilon for root noise (0 = disabled).
        checkpoint_sha: Hash of the .pt file (for reproducibility).
    """
    conn = _get_db(db_path)
    now = datetime.now(timezone.utc).isoformat()
    git = get_git_sha()
    for r in opponent_results:
        conn.execute(
            """INSERT INTO rollout_opponent_stats
               (run_id, checkpoint_name, iter_num, opponent, side,
                wins, losses, draws, n_games,
                rollout_temp, dir_alpha, dir_epsilon,
                git_sha, checkpoint_sha, logged_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                run_id,
                checkpoint_name,
                iter_num,
                r["opponent"],
                r["side"],
                r.get("wins", 0),
                r.get("losses", 0),
                r.get("draws", 0),
                r.get("n_games", 0),
                rollout_temp,
                dir_alpha,
                dir_epsilon,
                git,
                checkpoint_sha,
                now,
            ),
        )
    conn.commit()
    conn.close()


def log_elo_rating(
    checkpoint_name: str,
    elo: float,
    elo_ussr: Optional[float] = None,
    elo_us: Optional[float] = None,
    ci_lo: Optional[float] = None,
    ci_hi: Optional[float] = None,
    db_path: Path = DB_PATH,
) -> None:
    """Log a BayesElo rating after it's computed."""
    conn = _get_db(db_path)
    conn.execute(
        """INSERT INTO elo_ratings (checkpoint_name, elo, elo_ussr, elo_us, ci_lo, ci_hi, computed_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            checkpoint_name,
            elo,
            elo_ussr,
            elo_us,
            ci_lo,
            ci_hi,
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    conn.commit()
    conn.close()


def log_tournament(
    tournament_id: str,
    mode: str,
    models: list[str],
    anchor: str,
    anchor_elo: float,
    games_per_match: int,
    match_log: list[dict],
    ratings: dict[str, dict],
    new_model: Optional[str] = None,
    db_path: Path = DB_PATH,
) -> None:
    """Persist a complete tournament run to SQL with full provenance.

    Args:
        tournament_id: Unique string ID, e.g. "incremental_20260411T183042Z_v67".
        mode: "incremental" or "full".
        models: List of all model names in this tournament.
        anchor: Anchor model name (e.g. "v14").
        anchor_elo: Anchor Elo value.
        games_per_match: Games per pair.
        match_log: List of match dicts from run_elo_tournament.py
                   (keys: model_a, model_b, wins_a, wins_b, draws,
                    wins_a_ussr, wins_b_ussr, wins_a_us, wins_b_us, n_games, seed).
        ratings: Dict of {model: {"elo", "elo_ussr", "elo_us", "ci95": [lo, hi]}}.
        new_model: Which model was being placed (None for full round-robin).
    """
    conn = _get_db(db_path)
    now = datetime.now(timezone.utc).isoformat()

    # Upsert tournament record (replace on conflict so re-runs are idempotent)
    conn.execute(
        """INSERT OR REPLACE INTO tournaments
           (id, run_at, mode, new_model, models_json, anchor, anchor_elo, games_per_match)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            tournament_id,
            now,
            mode,
            new_model,
            json.dumps(models),
            anchor,
            anchor_elo,
            games_per_match,
        ),
    )

    # Delete old match rows for this tournament (idempotent re-run support)
    conn.execute("DELETE FROM match_results WHERE tournament_id = ?", (tournament_id,))
    conn.execute("DELETE FROM elo_ladder WHERE tournament_id = ?", (tournament_id,))

    # Insert match results — one row per pair, preserving order from tournament script
    for m in match_log:
        conn.execute(
            """INSERT INTO match_results
               (tournament_id, model_a, model_b, wins_a, wins_b, draws,
                wins_a_ussr, wins_b_ussr, wins_a_us, wins_b_us, n_games, seed, run_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                tournament_id,
                m["model_a"],
                m["model_b"],
                m["wins_a"],
                m["wins_b"],
                m.get("draws", 0),
                m.get("wins_a_ussr"),
                m.get("wins_b_ussr"),
                m.get("wins_a_us"),
                m.get("wins_b_us"),
                m.get("n_games", games_per_match),
                m.get("seed"),
                now,
            ),
        )

    # Insert per-tournament Elo snapshot
    for model, r in ratings.items():
        ci = r.get("ci95", [None, None])
        conn.execute(
            """INSERT INTO elo_ladder
               (tournament_id, model, elo, elo_ussr, elo_us, ci_lo, ci_hi, computed_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                tournament_id,
                model,
                r["elo"],
                r.get("elo_ussr"),
                r.get("elo_us"),
                ci[0] if ci else None,
                ci[1] if ci else None,
                now,
            ),
        )

    conn.commit()
    conn.close()
