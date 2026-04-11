---
# Opus Analysis: Best Fixtures and Update Algorithm
Date: 2026-04-09
Question: What are the best fixtures for the current PPO run, and what is the algorithm for updating them?

## Executive Summary

The current fixture set (v8/v14/v22/heuristic) is reasonable but has a gap: v8 and v14 are clustered within 75 Elo of each other (1942 vs 2018), while the jump from v14 to v22 is only 78 Elo, and the jump from heuristic to v8 is 257 Elo. The biggest issue is not the specific checkpoints but the **fixture fadeout at iteration 50**, which removes all external diversity for the final 75% of training -- exactly when echo-chamber collapse risk is highest. For v27+, the recommended fixture set is **heuristic / v8 / v14 / v22** (the current set is already correct), but fixture fadeout should be raised to 150 or disabled entirely, and one slot should be reserved for a "stepping stone" checkpoint that is updated when the frontier moves.

## Findings

### 1. Current Elo Landscape

| Model     | Elo   | Delta vs v22 |
|-----------|-------|--------------|
| v22       | 2096  | 0            |
| v19       | 2079  | -17          |
| v14       | 2018  | -78          |
| v12       | 2001  | -95          |
| v8        | 1942  | -154         |
| v25       | 1820  | -276         |
| v24       | 1757  | -339         |
| heuristic | 1685  | -411         |

v24/v25 regressed badly due to entropy collapse (v23 log_prob bug contaminated the lineage). v19 is very close to v22 and offers little diversity. v12 is close to v14 (only 17 Elo apart).

### 2. What Makes a Good Fixture Set

A fixture set should satisfy five properties:

1. **Elo spread coverage**: fixtures should span the range from "easy" to "near-frontier" so the learning model always has opponents it can beat (for positive reward signal) AND opponents it struggles against (for gradient signal on weaknesses).

2. **Strategy diversity**: different checkpoints may exploit different strategies. Even two models at similar Elo may play differently (e.g., one is USSR-dominant, another is symmetric). Ideally fixtures cover different play styles.

3. **Floor anchor**: at least one fixture should be weak enough that even a regressing model can still get positive reward from it. This prevents total gradient collapse. The heuristic (Elo 1685) serves this role perfectly -- it cannot be beaten by "cheap tricks" the way a weak neural model can, because it follows fixed rules.

4. **Frontier anchor**: at least one fixture should be at or near the training model's current strength, so there is always a hard opponent in the pool even before the model generates its own iter_*.pt checkpoints. This is v22 currently.

5. **No redundancy**: fixtures that are too close in Elo to each other waste training games. The PFSP mechanism will upweight the harder one anyway, but having both dilutes the pool unnecessarily.

### 3. Analysis of Current Fixtures

**Heuristic (1685)**: Essential. Provides the floor, prevents total collapse, and tests qualitatively different play (rules-based, not neural). Keep permanently.

**v8 (1942)**: Good "easy neural" anchor. 257 Elo above heuristic, 154 below frontier. Model should beat v8 >70% if it is anywhere near frontier strength. Provides warm-up gradient signal. The 257-Elo gap to heuristic is large but acceptable -- there is nothing useful between them (v1-v7 are too weak/unstable).

**v14 (2018)**: Good "medium" anchor. 76 Elo above v8, 78 below frontier. A model at frontier should beat it ~60-65% of the time. Provides the "challenging but winnable" tier.

**v22 (2096)**: Frontier anchor. Essential for preventing the echo chamber. A model at v22 strength should go 50/50 against it. If the training model surpasses v22, this becomes the "upper medium" tier.

**Assessment**: The current 4-fixture set provides a well-spaced ladder: 1685 / 1942 / 2018 / 2096. The gaps are 257 / 76 / 78. This is a reasonable distribution with one large gap at the bottom (heuristic to v8). The set is **correct for v27**.

### 4. The Real Problem: Fixture Fadeout

The current `fixture_fadeout=50` removes ALL fixtures after iteration 50 of a 200-iteration run. This means:
- Iterations 0-49: training against heuristic + v8 + v14 + v22 + past-self checkpoints
- Iterations 50-199: training ONLY against past-self checkpoints

This is dangerous. The entire purpose of fixtures is to prevent echo-chamber collapse, and they are removed for 75% of training. The v24/v25 collapse (from v22's 2096 down to 1757/1820) happened in runs with this fadeout. While the root cause was a log_prob bug, the fadeout removes the safety net that could have limited the damage.

**Recommendation**: Raise `fixture_fadeout` to 150 (keep fixtures for 75% of training) or set it to 999 (effectively never fade out). The PFSP mechanism already naturally downweights fixtures the model dominates -- there is no need for a hard cutoff.

### 5. How Many Fixtures Is Too Many

With `league-mix-k=4` (4 opponents per iteration), the opponent budget is:
- Slot 0: always self-play (current model)
- Slots 1-3: sampled from pool (past-self + fixtures)

Fixtures get approximately 50% of the past-self weight mass (see line 999 of train_ppo.py). With 4 fixtures and ~10-20 past-self checkpoints, each fixture gets roughly 1-3% of total opponent sampling weight. This means adding a 5th fixture would reduce each fixture's share from ~2.5% to ~2%.

**Practical limit**: 3-5 fixtures is the sweet spot. Below 3, you lack coverage. Above 5, each fixture gets so little sampling weight that it barely contributes training signal, and you are better off relying on PFSP to weight the existing ones.

### 6. When v19 vs v14 -- Are Both Needed?

v19 (2079) is only 17 Elo below v22 (2096). Having both v14 and v22 already covers the 2018-2096 range. v19 adds very little:
- It is only 61 Elo above v14 and 17 below v22
- Its win rates against other models are nearly identical to v22's
- It wastes a fixture slot that could be used for a future checkpoint

The previous fixture set (before the 2026-04-09 update) used v4/v8/v12. The update to v8/v14/v19 was already an improvement. The current v8/v14/v22 is better than v8/v14/v19 because v22 is actually distinct from the cluster.

**Verdict**: Do NOT add v19 as a fixture. The current v8/v14/v22/heuristic set is optimal.

## Conclusions

1. **The current fixture set (heuristic/v8/v14/v22) is correct for v27 and near-term training.** The Elo spread (1685/1942/2018/2096) provides floor, easy, medium, and frontier tiers. No changes needed to the checkpoint selection.

2. **Fixture fadeout is the biggest risk, not fixture selection.** `fixture_fadeout=50` removes all external diversity for 75% of training. Raise to 150 or 999.

3. **4 fixtures is the right count for mix-k=4.** Going to 5+ dilutes per-fixture sampling weight below usefulness. Going below 3 loses coverage.

4. **Heuristic is irreplaceable as a fixture.** It is the only non-neural opponent and provides qualitatively different play patterns. Never remove it.

5. **v22 as frontier fixture is correct now, but will need updating when a new model surpasses it by 50+ Elo.** At that point, the new frontier becomes the fixture and v22 slides into the "upper medium" tier (potentially replacing v14 if the ladder gets too crowded).

6. **v19 should NOT be added as a fixture.** It is too close to v22 (17 Elo) and adds no diversity.

7. **v24/v25 should NEVER be used as fixtures.** They regressed and would teach bad habits. Only use checkpoints that are confirmed-strong via the Elo ladder.

## Recommendations

### Concrete Fixture Update Algorithm

```
ALGORITHM: FixtureUpdate(current_fixtures, elo_ladder, new_model)

CONSTANTS:
  MAX_FIXTURES = 4  (including heuristic)
  FRONTIER_GAP_TRIGGER = 50  (Elo points above current frontier fixture)
  MIN_SPACING = 40  (minimum Elo gap between adjacent fixtures)
  FIXTURE_FADEOUT = 150  (or 999 to effectively disable)

TRIGGER CONDITION:
  Update fixtures when BOTH:
    (a) new_model.elo > frontier_fixture.elo + FRONTIER_GAP_TRIGGER
    (b) new_model is confirmed top-of-ladder (not a regression)

SELECTION RULE:
  1. heuristic is ALWAYS a fixture (never removed)
  2. The new frontier model becomes the new FRONTIER_FIXTURE
  3. The old frontier fixture slides down into the mid-range
  4. If the mid-range now has 3+ neural fixtures, remove the one
     that is closest in Elo to another fixture (least unique)
  5. Target Elo distribution: roughly evenly spaced between
     heuristic and frontier, with slight bias toward harder opponents

EXAMPLE for current state (frontier = v22 = 2096):
  If v30 reaches 2150 (>2096+50):
    - FRONTIER_FIXTURE = v30 (2150)
    - v22 slides to upper-mid
    - Remove v14 (now too close to v8 relative to the new spread)
    - New set: heuristic(1685) / v8(1942) / v22(2096) / v30(2150)
    
  If v30 reaches 2200 (>2096+100):
    - FRONTIER_FIXTURE = v30 (2200)
    - v22 slides to mid
    - v14 is now well-spaced: 1685 / 1942 / 2018 / 2096 / 2200
    - But that is 5 fixtures. Remove v14 (smallest unique contribution):
    - New set: heuristic(1685) / v8(1942) / v22(2096) / v30(2200)

IMPLEMENTATION (in ppo_loop_step.sh):
  After each ELO update:
  1. Read elo_full_ladder.json
  2. Get current FRONTIER_FIXTURE Elo
  3. If new_model.elo > frontier_elo + 50 AND new_model is rank 1:
     a. Log "FIXTURE UPDATE TRIGGERED" to autonomous_decisions.log
     b. Set FRONTIER_FIXTURE = new_model scripted path
     c. Re-evaluate mid fixtures using MIN_SPACING rule
     d. Update WEAKEST_FIXTURE / MID_FIXTURE / FRONTIER_FIXTURE variables
  4. Otherwise: no change
```

### Immediate Action Items

1. **Raise fixture_fadeout from 50 to 150** in `ppo_loop_step.sh` line 235 (`--league-fixture-fadeout 50` -> `--league-fixture-fadeout 150`). This is the single highest-impact change.

2. **Keep current fixtures as-is** for v27: heuristic / v8 / v14 / v22. No checkpoint changes needed.

3. **Add fixture update logic to ppo_loop_step.sh** as a post-ELO-update check. The script already reads `elo_full_ladder.json` -- add a Python one-liner that checks if the frontier gap trigger is met and updates the variables.

4. **Document the algorithm** in a comment block at the top of the fixture section of `ppo_loop_step.sh` so future automated runs know why the fixtures are what they are.

## Open Questions

1. **Should fixture fadeout be completely disabled (999)?** The argument for ANY fadeout is that once the model is much stronger than all fixtures, playing against them wastes training time. But PFSP already handles this by downweighting dominated opponents. A hard cutoff is redundant and dangerous. The only case for keeping a fadeout is if training is compute-limited and you want to guarantee 100% self-play in the final phase.

2. **Should fixture weight share be configurable independently from past-self?** Currently fixtures get a fixed 50% of past-self mass (line 999). If the model dominates all fixtures, this 50% is wasted on easy opponents. An alternative: give fixtures their own PFSP-weighted mass that scales independently. This is a code change, not a config change.

3. **Should there be an asymmetric fixture?** v24/v25 have extreme USSR/US asymmetry (v25: USSR=1915, US=1682). While they are weak overall, training against an asymmetric opponent could help the model learn to exploit or defend against lopsided strategies. This is speculative and low priority.

4. **Is v8 still useful when the model is 150+ Elo above it?** At v22 strength, the model beats v8 ~72% of the time. This is still useful (28% loss rate = real gradient signal). But if the frontier reaches 2200+, v8 at 1942 would be beaten ~80%+. At that point, v8 could be replaced by a stronger "weak" anchor (e.g., v12 or v14). The algorithm above handles this via the MIN_SPACING rule.
---
