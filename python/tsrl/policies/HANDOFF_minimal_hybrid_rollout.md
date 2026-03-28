# minimal_hybrid rollout handoff

## Purpose

This note is a compact handoff for the ongoing `minimal_hybrid` policy work under `python/tsrl/policies/`.

The current workflow has shifted away from blind weight tuning and toward:

1. generating detailed self-play rollout logs,
2. manually comparing decisions against the richer `.md` policy docs,
3. identifying repeated failure modes,
4. implementing small policy-local heuristic fixes,
5. regenerating the same seeded logs to see whether the blind spots were actually addressed.

This file is intended to let a different coding agent resume work without rereading the full terminal history.

## User preferences and operating constraints

- Keep changes local to `python/tsrl/policies/` unless explicitly told otherwise.
- Do not remove legacy code; add new helpers, logs, snapshots, and artifacts instead.
- Keep previous results logged so progress over time is visible.
- Track compute / wall cost when doing heavier optimization campaigns.
- Do not do destructive git operations in this directory.
- For future detailed rollout log folders, use `DATE_TIME_<suffix>` naming so lexical order matches chronology.
- The user explicitly wants autonomous progress when possible.

## Environment notes

- Focused `pytest` runs should usually use `-n 0`.
  The repo config enables parallel pytest by default, which previously caused confusion.
- Useful already-approved command prefixes in this environment included:
  - `uv run python`
  - `uv run pytest`
  - `uv run ruff`
  - `nice -n 10 uv run python`

## Relevant code files

- `python/tsrl/policies/minimal_hybrid.py`
  - current heuristic rollout policy
  - now also exposes ranked decision analysis for tracing
- `python/tsrl/policies/generate_minimal_hybrid_rollout_logs.py`
  - generates detailed self-play logs
  - now supports multi-process parallelism via `ProcessPoolExecutor`
- `python/tsrl/policies/tests/test_minimal_hybrid.py`
  - focused regression tests for policy behavior
- `python/tsrl/policies/benchmark_hybrid_vs_random.py`
  - micro benchmark for policy-call latency
- `python/tsrl/policies/minimal_hybrid.md`
- `python/tsrl/policies/classic.md`
- `python/tsrl/policies/sankt.md`

## Important policy-local additions already made

### 1. Decision tracing support

`minimal_hybrid.py` now contains:

- `ActionScoreBreakdown`
- `DecisionAnalysis`
- `analyze_minimal_hybrid_decision(...)`

These expose:

- legal action count,
- chosen action,
- ranked alternatives,
- per-action score components,
- notes describing why the heuristic liked or disliked an action.

This tracing is what powers the detailed rollout logs.

### 2. Heuristic fixes already implemented

These were added after inspecting the first batch of detailed logs:

- offside ops penalty for `INFLUENCE` / `COUP` / `REALIGN` on hostile non-scoring cards
- non-coup MilOps urgency penalty
- stronger coup scoring from expected swing
- access-opening coup bonus
- USSR turn-1 Iran coup bonus
- penalty for empty coups
- DEFCON-2 battleground coup safety veto
  - except the currently exposed safe ops-coup case:
    - `US` battleground coup while `pub.nuclear_subs_active` is true

### 3. Parallel rollout-log generation

`generate_minimal_hybrid_rollout_logs.py` used to generate games sequentially.
It now parallelizes by game using `ProcessPoolExecutor` and a `--workers` argument.

Important behavior:

- the script writes output files only after worker results return,
- so an empty output directory during execution is normal,
- progress prints appear as `completed N/total`.

## Failure-analysis loop completed so far

### Baseline detailed logs

Initial 5-game detailed batch:

- directory:
  - `python/tsrl/policies/rollout_logs/20260327_110757`
- seeds:
  - `20260410` to `20260414`

Summary:

- all 5 games ended by `turn_limit`
- average step count around full-length games

Repeated failure modes found in those logs:

1. `offside_event_blindness`
   - hostile non-scoring cards were routinely burned for ops with little policy resistance
2. `milops_urgency_blindness`
   - many late non-coup plays happened while MilOps shortfall was still active
3. `opening_iran_coup_blindness`
   - USSR turn-1 AR1 never chose the strong Iran coup opening
4. `passive_rollout_drift`
   - games often drifted to `turn_limit`

Representative aggregate tallies from the baseline batch:

- chosen mode counts:
  - `INFLUENCE`: `626`
  - `EVENT`: `100`
  - `COUP`: `43`
- issue counts:
  - `milops_shortfall_non_coup`: `724`
  - `offside_ops_play`: `291`

### First heuristic-fix batch

After adding offside penalties, MilOps urgency, and the Iran-coup hook:

- directory:
  - `python/tsrl/policies/rollout_logs/20260327_postfix_mp`

Observed effect:

- the intended blind spots were partly fixed
  - offside ops plays dropped materially
  - MilOps-non-coup cases dropped materially
  - USSR now opened with Iran coups
- but the fix overshot badly into aggression
  - all 5 games ended by `defcon1`

Aggregate tallies from that batch:

- chosen mode counts:
  - `INFLUENCE`: `244`
  - `COUP`: `49`
  - `EVENT`: `48`
- issue counts:
  - `milops_shortfall_non_coup`: `275`
  - `offside_ops_play`: `118`

Interpretation:

- the original blind spots were real and were being addressed,
- but a new failure mode appeared:
  - `defcon_suicidal_coup_overcorrection`

### DEFCON-2 safety batch

After adding the DEFCON-2 battleground coup veto plus the Nuclear Subs exception:

- directory:
  - `python/tsrl/policies/rollout_logs/20260327_114100_defcon2_safety_mp`

Summary from `summary.json`:

- all 5 games ended by `turn_limit`
- steps:
  - `154`
  - `154`
  - `153`
  - `154`
  - `153`
- winners / final VP:
  - game 1: USSR, `+2`
  - game 2: US, `-7`
  - game 3: USSR, `+8`
  - game 4: USSR, `+4`
  - game 5: USSR, `+11`

Before/after comparison versus the all-`defcon1` batch:

- before:
  - end reasons: `{'defcon1': 5}`
  - average steps: `68.2`
- after:
  - end reasons: `{'turn_limit': 5}`
  - average steps: `153.6`

Additional validation:

- chosen `DEFCON 2` battleground coups in the new batch: `0`

Interpretation:

- the DEFCON-2 suicide mode is fixed for the tested seeds,
- but the policy is now back to long, mostly passive games.

### DEFCON-3 safety batch

After strengthening the DEFCON-3 battleground coup penalty from `-2.5` to `-6.0` and adding a suicide veto for low-MilOps cases:

- directory:
  - `python/tsrl/policies/rollout_logs/20260327_162106_defcon3_fix`
- seeds:
  - `20260410` to `20260414` (same seeds as baseline for direct comparison)

Summary from `summary.json`:

- end reasons: `{'turn_limit': 4, 'europe_control': 1}`
- steps: `[154, 60, 154, 154, 154]`
- average: `145.6` (down from `153.6`)
- final VP: `[+4, +1, +5, +10, +1]` (USSR favored, as in baseline)
- all 5 seeds completed successfully

Before/after comparison vs baseline DEFCON-2 safety batch:

- DEFCON-3 battleground coups:
  - before: `137` total (13, 33, 40, 21, 30 per game)
  - after: `57` total (12, 7, 4, 13, 21 per game)
  - **reduction: 58%** ✓
- game length: `153.6` avg → `145.6` avg
- games reaching turn 10: `5/5` → `4/5` (one europe_control win)

Validation:

- all 11 unit tests pass (including new `test_policy_avoids_defcon3_battleground_coup_without_milops_urgency`)
- remaining DEFCON-3 battleground coups have milops_urgency `0.75–7.00` (strategically justified)
- no illegal actions or safety violations

Interpretation:

- the suicide penalty successfully vetos risky DEFCON-3 BG coups when MilOps pressure is low (<0.5 urgency)
- remaining coups are strategically sound, driven by genuine MilOps catch-up needs
- the early europe_control win (game 2) suggests the policy can now pursue more aggressive endgame tactics
- DEFCON-3 safety is now sufficient; next focus should be midgame / endgame pressure

## Current assessment

The highest-ROI issues appear to be:

1. coup selectivity at `DEFCON 3` / `DEFCON 4`
   - the policy may still be too eager to coup in lower-safety windows
2. endgame / midgame pressure
   - after removing suicidal coups, the policy often drifts back to full-length games
3. richer pressure heuristics rather than more pure numeric tuning
   - previous broad tuning efforts found seed-fragile candidates but no durable statistically significant improvement

At this point, more blind tuning on the current surface is probably lower ROI than another manual log-analysis iteration.

## Useful scripts and artifacts from earlier tuning work

These already exist under `python/tsrl/policies/`:

- `autotune_minimal_hybrid.py`
- `local_refine_minimal_hybrid.py`
- `validate_minimal_hybrid_snapshot.py`
- `measure_end_reasons.py`
- `proxy_corpus.py`

Existing run-artifact directories worth preserving:

- `python/tsrl/policies/runs/20260327_024617`
- `python/tsrl/policies/runs/20260327_031638`
- `python/tsrl/policies/runs/20260327_035600`
- `python/tsrl/policies/runs/20260327_084930`
- `python/tsrl/policies/runs/20260327_090505`

Important conclusion from that tuning phase:

- no candidate has yet shown statistically significant durable improvement over the baseline policy,
- and DEFCON-1 does not appear common in the baseline policy itself,
- so the larger gains seem to come from heuristic-surface changes, not parameter nudging alone.

## Benchmark status

Latest micro benchmark after the DEFCON-2 safety patch:

- `minimal_hybrid`: `4208.152 us/decision`
- `random_policy`: `24.669 us/decision`
- relative slowdown: `170.59x`

This benchmark is only a policy-call latency benchmark on a fixed corpus.
It is not a playing-strength benchmark.

## Tests currently covering the policy

`python/tsrl/policies/tests/test_minimal_hybrid.py` currently covers:

- `None` when no legal action exists
- deterministic legal action selection
- scoring-card preference
- Early War Thailand preference
- China conservation
- friendly ops card preferred over offside hostile ops card
- urgent MilOps can trigger coup preference
- DEFCON-2 battleground coup avoidance
- Nuclear Subs DEFCON-2 battleground coup allowance
- DEFCON-3 battleground coup avoidance (unless MilOps urgent)
- tracing helper consistency with actual policy choice

## Recommended next step

If another agent resumes from here, the best next loop is:

1. inspect the newest detailed logs in:
   - `python/tsrl/policies/rollout_logs/20260327_114100_defcon2_safety_mp`
2. compare step-by-step against:
   - `minimal_hybrid.md`
   - `classic.md`
   - `sankt.md`
3. classify the next repeated blind spot,
   likely one of:
   - overly eager coups at `DEFCON 3`
   - weak endgame pressure
   - bad scoring timing
   - insufficient battleground / access prioritization after the opening
4. implement one small policy-local heuristic change
5. rerun:
   - focused tests
   - the 5 detailed seeded logs
   - optionally the micro benchmark
6. compare the new seeded batch against:
   - `20260327_postfix_mp`
   - `20260327_114100_defcon2_safety_mp`

## Useful commands

Focused checks:

```bash
uv run ruff check python/tsrl/policies/minimal_hybrid.py python/tsrl/policies/tests/test_minimal_hybrid.py
uv run pytest -n 0 python/tsrl/policies/tests/test_minimal_hybrid.py
```

Generate 5 detailed logs with parallel workers:

```bash
nice -n 10 uv run python python/tsrl/policies/generate_minimal_hybrid_rollout_logs.py \
  --games 5 \
  --seed-start 20260410 \
  --workers 20 \
  --out-dir python/tsrl/policies/rollout_logs/$(date +%Y%m%d_%H%M%S)_<suffix>
```

Run the micro benchmark:

```bash
uv run python python/tsrl/policies/benchmark_hybrid_vs_random.py
```

## Final state of the current handoff

- Detailed-log analysis is now the main driver.
- DEFCON-2 battleground suicide coups are fixed for the tested seeds.
- The next iteration should focus on stronger but still safe pressure, not another blind global tuning sweep.
