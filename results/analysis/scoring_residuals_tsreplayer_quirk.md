# SCORING_VP_MISMATCH residuals: RETRACTED — tsreplayer was correct, spec was wrong

Date: 2026-04-21 UTC (retracted)
Related tasks: #116, #116-B, #123
Engine commit: 3e8ef0d (Europe VP table + SE Asia pool + Africa metadata)

## Retraction

This doc originally claimed the 133 SCORING_VP_MISMATCH residuals remaining after
commit 3e8ef0d were a *tsreplayer log quirk* — specifically that tsreplayer was
wrongly treating UK (id 17) and Turkey (id 16) as non-battlegrounds. That claim was
inverted:

- **tsreplayer was computing regional scores correctly.**
- **`data/spec/countries.csv` had UK and Turkey incorrectly flagged as
  `is_battleground=true`.** Standard Twilight Struggle (Deluxe) has five Europe
  battlegrounds: France, Italy, West Germany, East Germany, Poland. UK and Turkey
  are not battlegrounds.
- **`docs/ts_rules_scoring.md` had the Europe VP row as `1 / 3 / GAME WIN`** with a
  fabricated "empirically verified from 51 TSEspionage logs" annotation. The
  engine's own `cpp/tscore/scoring.cpp` `kRegionVp` had `{3, 7, GAME WIN}` all along,
  which is correct. The two files silently disagreed.

The original empirical "verification" worked only because both errors cancelled:
counting UK+Turkey as BGs while also using the wrong `(1,3)` Europe tier reproduced
tsreplayer's scores for a subset of positions. The cancellation broke on cards where
UK/Turkey were not both controlled by the same side, producing the 133 residuals
this doc originally blamed on tsreplayer.

Worked example, corrected (tsreplayer_16 turn 8 Europe Scoring):

- US controls France, Italy, West Germany (3 standard BGs), Canada, Greece, UK, Turkey.
  USSR controls East Germany, Poland (2 standard BGs), Czechoslovakia, Romania,
  Spain/Portugal.
- Rulebook: US Dom (7) + 3 BGs = 10. USSR Pres (3) + 2 BGs = 5. Net US +5.
- tsreplayer log: "US gains 5 VP" — matches exactly.

## Fix applied

Three-file coordinated correction (replaces the reverted Codex #116-B patch, which
was actually correct):

1. `data/spec/countries.csv`: demote Turkey (id 16) and UK (id 17) `is_battleground`
   from `true` to `false`.
2. `docs/ts_rules_scoring.md`: change Europe VP row to `3 / 7 / GAME WIN`, remove the
   false empirical-verification note, point at `scoring.cpp` as authoritative.
3. No change needed in `cpp/tscore/scoring.cpp`.

## Impact on engine certification (#122)

With UK and Turkey demoted, the residual SCORING_VP_MISMATCH count should drop
substantially on the tsreplayer corpus — roughly matching the 78-row output
Codex's original #116-B fix produced (filename still parked at
`results/validator_violations_post116b_CODEX_HACK_OUTPUT.jsonl.stale` under a
wrongly disparaging suffix).

The #122 certification gate can now require near-zero SCORING_VP_MISMATCH on the
tsreplayer corpus as a blocking criterion again — the earlier proposal to drop
scoring from blocking was predicated on the (wrong) tsreplayer-quirk hypothesis.

## Process lessons

- **Pattern to watch for:** LLM-authored rules docs that include an "empirically
  verified from N logs" footnote but no verification script in the repo. The claim
  is rhetorical, not reproducible.
- **Structural check we should add:** a test that compares `docs/ts_rules_scoring.md`
  VP tables against `cpp/tscore/scoring.cpp` `kRegionVp` on every build. A silent
  drift between them cost a week of wrong conclusions.
- **When Codex proposes a diff that moves the needle on a validator metric,
  verify against primary rules (PDF + tsreplayer log math), not against the repo's
  existing spec files** — the spec may be the thing that's wrong.
