# results/matches — Match Cache (DEPRECATED)

**This directory is archived.** Match results are now stored in `results/metadata.sqlite3`
(`match_cache` table for fast lookup, `match_results` table for provenance).

## Archive

All 1632 historical JSON files were compressed and migrated to SQL on 2026-04-12:

```
results/matches_archive_20260412.tar.bz2   (~36K compressed, ~6.5M raw)
```

To inspect: `tar -tjf results/matches_archive_20260412.tar.bz2 | head -20`

To extract a specific file: `tar -xjOf results/matches_archive_20260412.tar.bz2 results/matches/vX__vs__vY.json`

## Schema (match_cache table)

```sql
CREATE TABLE match_cache (
    model_a TEXT NOT NULL,   -- normalized: always < model_b alphabetically
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
    run_at TEXT NOT NULL,
    PRIMARY KEY (model_a, model_b)
);
```

## Why SQL instead of JSON files

- 1546 JSON files → single DB query (no glob + parse loop at startup)
- Atomic writes: no partial-file crash window
- Queryable: `SELECT * FROM match_cache WHERE model_a='v55'`
- Provenance: `match_results` table links to `tournaments` for full history

## Migration

The 1546 JSON files were migrated to `match_cache` by `scripts/migrate_match_cache.py`.
New matches are written to SQL only. The JSON directory is kept empty (except this README)
so old shell scripts that check `results/matches/` existence don't break.
