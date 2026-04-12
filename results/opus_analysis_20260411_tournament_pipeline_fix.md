# Opus Analysis: Candidate Tournament Pipeline Fix
Date: 2026-04-11
Question: Why is the candidate tournament broken and how to fix + automate it?

## Executive Summary

The confirmation/candidate tournament broke because `ppo_loop_step.sh` assumes version names are pure numeric (e.g. `v65`) but the SmallChoice branch introduced suffixed versions (`v65_sc`, `v66_sc`). The watcher chain at line 344 does `sed 's/v//'` followed by arithmetic `$((NEXT_NUM + 1))`, which fails for `65_sc` (not a valid integer). Additionally, both the league fixture loop and Elo model list loop silently skip non-numeric versions, so `_sc` models were excluded from the tournament entirely. Fixed the version parsing to handle arbitrary suffixes and added a `--post-train-hook` to `train_ppo.py` for standalone launches that bypass `ppo_loop_step.sh`.

## Findings

### 1. The automated pipeline chain was broken for `_sc` versions

`ppo_loop_step.sh` has three locations that assume version names are purely numeric:

- **Line 39** (league fixtures loop): `if ! [[ "$fix_ver" =~ ^[0-9]+$ ]]; then continue; fi` -- silently skips `v55_sc`, `v64_sc`, etc.
- **Line 127** (Elo model list loop): Same pattern, same skip.
- **Line 344** (watcher chain): `NEXT_NUM=$(echo '$NEXT' | sed 's/v//')` then `AFTER_NUM=$((NEXT_NUM + 1))` -- arithmetic error for `v65_sc` -> `65_sc`.

### 2. The `v66_sc` training was launched manually

The `autonomous_decisions.log` shows v66_sc was launched with a direct `uv run python scripts/train_ppo.py` command, bypassing `ppo_loop_step.sh` entirely. This means:
- No watcher chain was set up
- No confirmation tournament was scheduled
- No Elo ladder update was scheduled

### 3. `train_ppo.py` had no post-training hook

When training is launched manually (outside `ppo_loop_step.sh`), there was no mechanism to automatically run the confirmation tournament or Elo update afterward.

### 4. The tournament itself works fine

The manually invoked `run_elo_tournament.py` (currently running with 21 chain matches) works correctly. `ppo_confirm_best.py` also works correctly when called with valid arguments. The issue is purely in the automation/wiring layer.

### 5. `ppo_confirm_best.py` correctly handles any version naming

It derives `run_prefix` from the directory name, so `ppo_v66_sc_league` produces model names like `ppo_v66_sc_league_iter0040`. No version parsing assumptions.

## Root Cause

**The SmallChoice architecture change introduced version names with non-numeric suffixes (`_sc`), breaking three hard-coded numeric-only version parsing patterns in `ppo_loop_step.sh`.**

The breakage manifests in three ways:
1. Silent exclusion of `_sc` models from league fixtures and Elo ladder (skipped by regex filter)
2. Arithmetic error in the watcher chain's auto-increment logic (bash `$((...))` fails on non-integer)
3. No fallback mechanism for manual training launches (no `--post-train-hook`)

## Fix

### 1. Fixed version parsing in `ppo_loop_step.sh` (3 locations)

**League fixtures loop** (line 34-46): Changed from `if ! [[ "$fix_ver" =~ ^[0-9]+$ ]]; then continue` to extracting just the numeric prefix: `fix_num="${fix_ver%%[^0-9]*}"`. Non-numeric versions like `v55_sc` now pass through (numeric prefix `55` is used for min-version and corruption-era filtering).

**Elo model list loop** (line 119-139): Same fix, extracting `ver_num="${ver%%[^0-9]*}"` for filtering while keeping the full name for the model path.

**Watcher chain** (line 338-361): Replaced `sed 's/v//'` + arithmetic with proper suffix-aware parsing:
```bash
VBODY="${VSTR#v}"        # 65_sc
VNUM="${VBODY%%[^0-9]*}" # 65
VSUFFIX="${VBODY#$VNUM}" # _sc
AFTER_NUM=$((VNUM + 1))  # 66
AFTER="v${AFTER_NUM}${VSUFFIX}"  # v66_sc
```

### 2. Added `--post-train-hook` to `train_ppo.py`

New argument: `--post-train-hook "bash scripts/post_train_confirm.sh {out_dir}"`

Runs after training completes (blocking, 1-hour timeout). The `{out_dir}` placeholder is replaced with the actual `--out-dir` value. Example usage:

```bash
uv run python scripts/train_ppo.py \
  --checkpoint ... --out-dir data/checkpoints/ppo_v67_sc_league \
  --post-train-hook "bash scripts/post_train_confirm.sh {out_dir}" \
  ...
```

### 3. Created `scripts/post_train_confirm.sh`

Standalone script that:
1. Runs `ppo_confirm_best.py` to select best checkpoint
2. Copies scripted checkpoint to `scripted_for_elo/`
3. Updates the full Elo ladder via `run_elo_tournament.py`

Handles arbitrary version names by deriving version from directory name (`ppo_v66_sc_league` -> `v66_sc`).

## Pipeline Integration

### For automated pipeline (ppo_loop_step.sh):
No additional wiring needed -- `ppo_loop_step.sh` already has inline confirmation tournament + Elo update + watcher chain. The fix ensures these work with suffixed version names.

### For manual launches:
Add `--post-train-hook` to the command:
```bash
uv run python scripts/train_ppo.py \
  --checkpoint ... --out-dir data/checkpoints/ppo_v67_sc_league \
  --post-train-hook "bash scripts/post_train_confirm.sh {out_dir}" \
  ...other args...
```

### For standalone confirmation (after training already finished):
```bash
bash scripts/post_train_confirm.sh data/checkpoints/ppo_v66_sc_league
```

## Conclusions

1. The confirmation tournament was not "broken" in the sense of crashing -- it was never invoked because `ppo_loop_step.sh` watcher chain arithmetic failed silently on `_sc` version suffixes.
2. Three separate version-parsing code paths in `ppo_loop_step.sh` assumed pure numeric versions, all now fixed.
3. Manual training launches (like v66_sc) had no automated post-training tournament hook; `--post-train-hook` fills this gap.
4. The tournament scripts themselves (`run_elo_tournament.py`, `ppo_confirm_best.py`) work correctly and need no changes.
5. A new standalone `scripts/post_train_confirm.sh` provides a clean entry point for confirmation + Elo update from any context.

## Recommendations

1. Use `--post-train-hook "bash scripts/post_train_confirm.sh {out_dir}"` in all future manual training launches.
2. When launching the next `_sc` run, use `ppo_loop_step.sh v66_sc v67_sc` to restore the automated watcher chain.
3. Consider making `--post-train-hook` the default in `ppo_loop_step.sh` too (belt-and-suspenders) to handle the case where the watcher misses the training completion.
4. The currently-running manual candidate tournament (21 chain matches) should complete successfully -- no intervention needed.
5. Add a simple integration test that verifies `ppo_loop_step.sh` version parsing for both `v65` and `v65_sc` inputs.

## Open Questions

1. Should `_sc` era models be excluded from the corrupted-era filter? Currently the filter only checks the numeric prefix, so `v27_sc` would be excluded along with `v27`. This is correct behavior if corruption affected the base model, but would need revisiting if a clean `_sc` branch starts from a non-corrupted base at version 27+.
2. The `ppo_loop_step.sh` watcher chain polls every 15 seconds -- should this be replaced by inotifywait or a Python-native callback for lower overhead?
3. The Snakefile.ppo `confirm` rule (line 230) is still a stub. Should it be wired to call `post_train_confirm.sh`?
