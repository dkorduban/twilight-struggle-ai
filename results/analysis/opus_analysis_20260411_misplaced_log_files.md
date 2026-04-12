# Opus Analysis: Misplaced Log/JSON Files in Source Dirs
Date: 2026-04-11
Question: What non-code files are in source directories and where should they go?

## Executive Summary

Two large collections of generated data files were found tracked by git inside the `python/tsrl/policies/` source tree:

1. **`python/tsrl/policies/rollout_logs/`** -- 315 files across 35 subdirectories, totaling **551 MB** of rollout game JSON logs from heuristic policy tuning iterations (March-May 2026).
2. **`python/tsrl/policies/runs/`** -- 795 files across 11 subdirectories plus an `index.jsonl`, totaling **3.5 MB** of autotune parameter search snapshots and history.

These were moved to `results/logs/rollout_logs/` and `results/logs/autotune_runs/` respectively, removed from git tracking (the `logs/` gitignore pattern now applies), and all hardcoded path references in 3 Python scripts and 3 documentation files were updated. No other misplaced artifacts were found in `cpp/`, `scripts/`, `tests/`, or `bindings/` source directories (excluding expected CMake build artifacts which are already gitignored).

## Findings

### Files found in wrong locations

| Source path | File count | Size | Type |
|---|---|---|---|
| `python/tsrl/policies/rollout_logs/` | 315 | 551 MB | Rollout game JSONs + summaries + trace MDs |
| `python/tsrl/policies/runs/` | 795 | 3.5 MB | Autotune run configs, snapshots, histories |

Both directories contained generated output from the heuristic policy tuning pipeline. They were fully tracked by git, bloating the repository.

### Hardcoded paths in scripts

Three Python files had hardcoded paths pointing into the source tree:

1. **`python/tsrl/policies/generate_minimal_hybrid_rollout_logs.py`** line 625: default `--out-dir` was `python/tsrl/policies/rollout_logs/<timestamp>` -- updated to `results/logs/rollout_logs/<timestamp>`
2. **`python/tsrl/policies/local_refine_minimal_hybrid.py`** line 32: `_RUNS_DIR = Path("python/tsrl/policies/runs")` -- updated to `results/logs/autotune_runs`
3. **`python/tsrl/policies/autotune_minimal_hybrid.py`** line 47: `_RUNS_DIR = Path("python/tsrl/policies/runs")` -- updated to `results/logs/autotune_runs`

Three documentation files had stale references:

4. **`python/tsrl/policies/HANDOFF_minimal_hybrid_rollout.md`** -- multiple path references updated
5. **`python/tsrl/policies/README.md`** -- one reference to `python/tsrl/policies/runs/` updated
6. **`python/tsrl/policies/HANDOFF_STATUS.md`** -- baseline_log_dir reference updated

### Test fixtures (should stay)

No test fixture files were found outside `tests/` that needed attention. The `tests/` directory itself contained no JSON/log/data files outside of expected locations.

### Other source directories -- clean

- **`scripts/`**: No data files found (only `__pycache__/` which is gitignored)
- **`cpp/`**: Only CMake build artifacts in `build/` and `build-asan/` dirs (already gitignored)
- **`bindings/`**: Only `CMakeLists.txt` (code, not data)
- **`tests/`**: Only `tests/cpp/CMakeLists.txt` (code)

## Actions Taken

1. Created destination directories: `results/logs/rollout_logs/`, `results/logs/autotune_runs/`
2. Moved 35 rollout_logs subdirectories via `git mv` from `python/tsrl/policies/rollout_logs/*/` to `results/logs/rollout_logs/`
3. Moved 11 autotune runs subdirectories + `index.jsonl` via `git mv` from `python/tsrl/policies/runs/` to `results/logs/autotune_runs/`
4. Removed moved files from git tracking via `git rm --cached` (they now fall under the existing `logs/` gitignore pattern, which is correct for large generated artifacts)
5. Removed empty source directories `python/tsrl/policies/rollout_logs/` and `python/tsrl/policies/runs/`
6. Updated hardcoded paths in 3 Python files (listed above)
7. Updated path references in 3 documentation files (listed above)
8. Verified `import tsrl` still works
9. Verified test failures are pre-existing (unrelated to moved files)
10. Verified no remaining references to old paths in `python/`, `scripts/`, `tests/`, `docs/`

## Conclusions

1. The `python/tsrl/policies/` directory had accumulated 554 MB of generated rollout data that was tracked by git -- this was the only significant case of misplaced artifacts in the source tree.
2. All generated data is now in `results/logs/` where it is gitignored, reducing tracked repo size by ~1110 files and ~23M lines of JSON.
3. The three scripts that generate this data now default to writing under `results/logs/` instead of into the source tree.
4. No other source directories (`cpp/`, `scripts/`, `tests/`, `bindings/`) had misplaced data files.
5. Two pre-existing test failures were observed (`test_model_gradient_flows` for `small_choice_head` gradients, and a flaky `test_all_results_have_winner`) -- neither is related to the file moves.

## Recommendations

1. **Commit these changes** to finalize the removal of 1110 tracked generated files from the repository. The staged deletions plus the unstaged script updates should be committed together.
2. **Consider `git filter-branch` or `git-filter-repo`** if the repo clone size is a concern -- the 551 MB of JSON blobs remain in git history even after this commit removes them from HEAD.
3. **Add a `.gitignore` inside `python/tsrl/policies/`** with `rollout_logs/` and `runs/` entries as a secondary guard against re-tracking, in case someone creates these dirs locally without the move.

## Open Questions

1. Should the rollout logs be preserved at all, or could they be deleted entirely? They're from March-May 2026 heuristic tuning iterations and may have only historical value.
2. Should the `results/logs/` gitignore be made more specific (e.g., only ignore `*.json` and `*.jsonl` under `results/logs/`) to allow tracking of small metadata files there?
