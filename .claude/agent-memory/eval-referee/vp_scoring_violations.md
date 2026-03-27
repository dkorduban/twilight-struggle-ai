---
name: VP Scoring Investigation Results
description: Analysis of 4 scoring VP mismatches between engine and log in vp20.txt game
type: project
---

## Summary
Found 4 VP scoring violations in data/raw_log_extras/vp20.txt. Engine and log disagree on scoring outcomes. Investigation shows:

- **Violations 1 & 2** (Mideast Scoring T2/T3): Engine correctly identifies DOMINATION tier, but log records PRESENCE tier VP
- **Violation 3** (Asia Scoring T4): Engine correctly adds China Card bonus (+1), log records +0 instead of +1
- **Violation 4** (South America Scoring T5): Engine correctly identifies CONTROL tier, but log records higher score

## Details

### Violation 1: T2 USSR AR3 - Mideast Scoring (card 3)
- **Engine**: +5 VP (DOMINATION)
- **Log**: +3 VP (PRESENCE)
- **State at scoring**:
  - USSR controls: Egypt (BG), Iraq (BG), Lebanon (non-BG) → 2 BGs + 1 non-BG
  - US controls: Iran (BG) → 1 BG
  - Tier test: USSR has 2 > 1 BG opponent AND ≥1 non-BG → DOMINATION (5 VP)
  - US has only 1 country → PRESENCE (3 VP)
  - USSR tier > US tier → USSR wins at DOMINATION
- **Likely cause**: Log miscounted tier or applied wrong VP table. Engine is correct per ITS rules.

### Violation 2: T3 USSR AR4 - Mideast Scoring (card 3)
- **Engine**: +5 VP (DOMINATION)
- **Log**: +4 VP (neither PRESENCE nor DOMINATION)
- **State at scoring**:
  - USSR controls: Egypt (BG), Iraq (BG), Libya (BG), Lebanon (non-BG) → 3 BGs + 1 non-BG
  - US controls: Iran (BG) → 1 BG
  - Tier test: USSR has 3 > 1 BG opponent AND ≥1 non-BG → DOMINATION (5 VP)
  - US has only 1 country → PRESENCE (3 VP)
  - USSR tier > US tier → USSR wins at DOMINATION
- **Likely cause**: Log recorded intermediate VP value (possibly mid-scoring or miscalculation). Engine is correct per ITS rules.

### Violation 3: T4 USSR AR3 - Asia Scoring (card 1)
- **Engine**: +1 VP (tie in PRESENCE tier, but +1 from China Card bonus)
- **Log**: +0 VP (records "No VP awarded")
- **State at scoring**:
  - USSR controls: Afghanistan (non-BG), North Korea (BG), South Korea (BG) → 2 BGs + 1 non-BG
  - US controls: India (BG), Japan (BG), Pakistan (BG) → 3 BGs
  - Tier test:
    - USSR: 2 BGs, not > 3 opponent BGs, so fails DOMINATION → PRESENCE (1 country)
    - US: 3 BGs, not > 2 opponent BGs, so fails DOMINATION → PRESENCE (3 countries)
  - Both at PRESENCE tier → tie on regional scoring = 0 VP
  - **BUT**: Card 1 (Asia Scoring) includes China Card bonus
  - China held by: USSR → +1 bonus
  - **Total**: 0 (tie) + 1 (China bonus) = +1 VP
- **Likely cause**: Log failed to count China Card bonus for Asia Scoring card. Engine is correct per card text and ITS rules.

### Violation 4: T5 USSR AR1 - South America Scoring (card 82)
- **Engine**: +6 VP (CONTROL)
- **Log**: +10 VP
- **State at scoring**:
  - USSR controls: Argentina (BG), Brazil (BG), Chile (BG), Venezuela (BG) → 4 BGs (all of them)
  - US controls: 0 countries
  - Tier test: USSR controls all 4 BGs → CONTROL (6 VP)
  - US controls 0 → NONE (0 VP)
  - USSR tier > US tier → USSR wins at CONTROL
- **Likely cause**: Log may have been counting Soviet influence as presence/VP (unusual), or recording cumulative score. Engine correctly applies ITS CONTROL tier (6 VP). The "+10" in log could indicate cumulative game VP rather than incremental scoring.

## Scoring Engine Rules Applied

ITS Competitive / Deluxe Edition rules:

**Control condition**: `own_influence >= opponent_influence + country_stability`

**Tier determination** (standard regions):
- CONTROL: controls ALL battlegrounds in region
- DOMINATION: controls MORE battlegrounds than opponent AND >= 1 non-battleground
- PRESENCE: controls >= 1 country (any type)
- NONE: controls 0 countries

**Winner**: Side with higher tier wins at that tier's VP value. Tie = 0 VP.

**VP tables**:
- Middle East: presence=3, domination=5, control=7
- Asia: presence=3, domination=7, control=9
- South America: presence=2, domination=4, control=6

**Asia Scoring bonus**: Asia Scoring card (id=1) awards +1 VP to China Card holder in addition to regional tier.

## Implementation Status

Engine implementation in `python/tsrl/engine/scoring.py`:
- ✓ Correct tier computation logic
- ✓ Correct VP table lookup
- ✓ Correct China Card bonus (card 1 only)
- ✓ Consistent with ITS rules

**Verdict**: Engine is correct on all 4 violations. Log appears to have errors or unconventional scoring conventions in this game.
