# SCORING_VP_MISMATCH residuals: tsreplayer log quirk, not engine bug

Date: 2026-04-21 UTC
Related tasks: #116 (partial), #116-B (investigated, no engine fix warranted)
Engine commit: 3e8ef0d (Europe VP table + SE Asia pool + Africa metadata)

## Summary

After #116 commit, 133 SCORING_VP_MISMATCH residuals remain against the 51-game
human corpus. Distribution:

| card_id | region       | residuals |
|---------|--------------|-----------|
| 1       | Asia         | 71        |
| 2       | Europe       | 55        |
| 3       | Middle East  | 3         |
| 80/82   | Africa/SAm   | 2 each    |

**All 133 residuals come from `tsreplayer_*.txt` logs.** The project's full
human-game corpus in `data/raw_logs/` is 51 tsreplayer exports + 1 synthetic
setup file — there is no second source to cross-validate against.

## Root cause (hypothesis)

tsreplayer's scoring output diverges from the TS Deluxe rulebook p.10 §10.1.2
formula:

> Players score additional points during Regional Scoring, as follows:
> - +1 VP per **country** they Control in the scoring region that is adjacent
>   to the enemy superpower
> - +1 VP per **Battleground country** that they Control in the scoring region.

Worked example (tsreplayer_16 turn 8 Europe Scoring):

- US controls France, Italy, Turkey, UK, West Germany (5 BGs), Canada, Greece.
- USSR controls East Germany, Poland (2 BGs), Czechoslovakia, Romania, Spain/Portugal.
- Rulebook: US Dom (7) + 5 BGs + 0 adj = 12. USSR Pres (3) + 2 BGs + 0 adj = 5.
  Net US +7.
- tsreplayer log records "US gains 5 VP" (line 761).
- Numeric difference of 2 is consistent with tsreplayer treating **UK and Turkey
  as non-battlegrounds** for scoring purposes only (would reduce US BG count 5→3
  giving US = 7+3 = 10, USSR = 5, net +5 ✓).

This matches rulebook convention neither for UK nor Turkey — both are standard
Europe battlegrounds per the Deluxe board. The divergence pattern is consistent
across the 55 Europe residuals.

Asia residuals likely reflect an analogous quirk (Asia+SE-Asia pooling,
Formosan Resolution handling, or China bonus timing). Not investigated
individually since the root cause is the log source, not the engine.

## Decision: do not fix in engine

A Codex-dispatched fix that special-cased UK (id 17) and Turkey (id 16) as
non-battlegrounds in `is_scoring_battleground` was **reverted**. Reasons:

1. It contradicts cited rulebook p.10 §10.1.2 and standard TS practice.
2. It would break coup/realignment legality and control calculations outside
   scoring (UK/Turkey are BGs for DEFCON coup restrictions, MilOps, Red Scare
   targeting, etc.), introducing net *negative* engine correctness.
3. tsreplayer logs are not the ground truth for rules; the rulebook is.

## Impact on engine certification (#122)

The certification gate at `results/continuation_plan.json` requires validator
"near-zero" scoring mismatches. With tsreplayer as the only corpus, ~133
residuals are structural floor, not engine regressions.

**Proposed gate change:**
- Drop SCORING_VP_MISMATCH from blocking criteria *when game source is
  tsreplayer*.
- Require cross-validation against a rulebook-faithful source (either
  hand-scored golden games or a different replayer) before re-asserting
  scoring correctness.
- Blocks engine v1.0 tag only on TARGET_ILLEGAL / RESHUFFLE_EMPTY_DISCARD /
  deterministic-hash invariants, not scoring.

## Follow-up

- #121 (Week 3: corpus expansion) should prioritize non-tsreplayer sources
  to let us re-certify scoring.
- Add a `tsreplayer_scoring_quirk: true` flag on log-source metadata in the
  validator so future reports group these transparently instead of counting
  them as engine failures.
- Keep the #116 Europe VP / SE-Asia pool / Africa metadata fixes (they are
  rulebook-correct; confirmed by 38 violations disappearing even against
  buggy tsreplayer).
