# HANDOFF: Fix DEFCON-3 Coup Penalty in minimal_hybrid.py

## Bug

In `python/tsrl/policies/minimal_hybrid.py`, `_score_coup` at line 708:

```python
if country.is_battleground:
    score += context.params.coup_battleground_bonus
    if pub.defcon == 2:
        ...
    elif pub.defcon == 3:
        score += context.params.coup_defcon3_penalty   # -6
        if _milops_urgency(pub, side) < 0.5:
            score -= _DEFCON3_BATTLEGROUND_SUICIDE_PENALTY  # 1M
```

**Non-battleground coups at DEFCON 3 have zero penalty**, even though ALL coups (BG and non-BG) lower DEFCON by 1. DEFCON 3 → 2 via non-BG coup is completely free in the current scoring.

This is the primary cause of the 62% DEFCON-1 end-game rate (competitive target is ~5%).

## Required Changes (all in `python/tsrl/policies/minimal_hybrid.py`)

### 1. Add constant (near line 51, with other DEFCON penalty constants)

```python
_DEFCON3_NONBG_COUP_SUICIDE_PENALTY = 800_000.0
```

### 2. Tighten BG urgency threshold: 0.5 → 0.8 (line 718)

Change:
```python
        if _milops_urgency(pub, side) < 0.5:
```
To:
```python
        if _milops_urgency(pub, side) < 0.8:
```

### 3. Add non-BG DEFCON-3 penalty block (right after line 719, still inside `_score_coup`)

After the entire `if country.is_battleground:` block, add:
```python
    # Non-battleground coups at DEFCON 3 also drop DEFCON to 2 — penalise unless
    # milops urgency is critical.  Keep a small urgency escape (0.9) since
    # non-BG coups are legal at DEFCON 2 and sometimes the only milops path.
    if pub.defcon == 3 and not country.is_battleground:
        if _milops_urgency(pub, side) < 0.9:
            score -= _DEFCON3_NONBG_COUP_SUICIDE_PENALTY
```

### 4. Add HybridParams field (near line 137, in HybridParams dataclass)

Add next to `coup_defcon3_penalty`:
```python
coup_defcon3_nonbg_threshold: float = 0.9
```

Then update step 3 to use it:
```python
    if pub.defcon == 3 and not country.is_battleground:
        if _milops_urgency(pub, side) < context.params.coup_defcon3_nonbg_threshold:
            score -= _DEFCON3_NONBG_COUP_SUICIDE_PENALTY
```

And update step 2 to use a param too (add `coup_defcon3_bg_threshold: float = 0.8` to HybridParams and use it instead of hardcoded 0.8).

## Validation

After making the changes, run:

```bash
cd /home/dkord/code/twilight-struggle-ai
uv run python -c "
import random
random.seed(42)
from tsrl.policies.minimal_hybrid import choose_minimal_hybrid, HybridParams
from tsrl.engine.game_loop import run_game
from tsrl.engine.types import Side

params = HybridParams()
defcon1_count = 0
total = 200
game_lengths = []

for i in range(total):
    try:
        result = run_game(
            us_policy=lambda ctx: choose_minimal_hybrid(ctx, params),
            ussr_policy=lambda ctx: choose_minimal_hybrid(ctx, params),
            seed=i
        )
        game_lengths.append(result.turn)
        if result.end_reason == 'defcon':
            defcon1_count += 1
    except Exception as e:
        pass

print(f'DEFCON-1 rate: {defcon1_count}/{total} = {defcon1_count/total:.1%}')
print(f'Mean game length: {sum(game_lengths)/len(game_lengths):.1f} turns')
print(f'Games reaching turn 8+: {sum(1 for t in game_lengths if t >= 8)}/{len(game_lengths)}')
"
```

**Target**: DEFCON-1 rate drops from 62% to below 30%. Mean turn ≥ 5.

Also run the existing DEFCON safety tests:
```bash
uv run pytest tests/python/test_heuristic_defcon_safety.py -v -n 0
```
All must still pass.

## Files to modify
- `python/tsrl/policies/minimal_hybrid.py` — only file to change

## Files NOT to touch
- `tests/python/test_heuristic_defcon_safety.py` — only run, don't modify unless tests genuinely break due to API change
- Any other files

## Status output
Write result summary to `.codex_tasks/defcon3-coup-fix/result.md` with:
- DEFCON-1 rate before (62%) and after
- Mean turn before/after
- Number of test failures (should be 0)
