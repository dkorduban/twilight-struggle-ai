# Task 124 Asia Scoring Diagnosis

Validator scope: `SCORING_VP_MISMATCH` rows with `card_id == 1` from the 51 `tsreplayer_*.txt` logs.

## Config Results

| Config | Tested facts | Residual count | Delta vs baseline 71 | Delta histogram |
|---|---|---:|---:|---|
| A | Baseline: SK=BG, SK-USA adj, PHI-USA adj | 71 | +0 | `{-6: 1, -2: 1, -1: 8, +1: 15, +2: 16, +3: 5, +4: 11, +5: 3, +6: 4, +7: 5, +10: 1, +12: 1}` |
| B | SK=not BG, keep adj | 83 | +12 | `{-7: 1, -5: 1, -3: 3, -1: 23, +1: 22, +2: 8, +3: 3, +4: 10, +5: 4, +6: 4, +7: 1, +8: 1, +9: 1, +10: 1}` |
| C | Remove SK-USA and PHI-USA adj, keep SK=BG | 85 | +14 | `{-7: 1, -2: 1, -1: 26, +1: 26, +2: 4, +3: 6, +4: 7, +5: 8, +6: 2, +7: 2, +9: 1, +11: 1}` |
| D | SK=not BG and remove adj | 73 | +2 | `{-8: 1, -6: 1, -4: 3, -2: 19, -1: 8, +1: 12, +2: 6, +3: 1, +4: 13, +5: 3, +6: 3, +8: 2, +10: 1}` |

## Conclusion

Config A minimizes residuals: 71 Asia card-1 mismatches with histogram `{-6: 1, -2: 1, -1: 8, +1: 15, +2: 16, +3: 5, +4: 11, +5: 3, +6: 4, +7: 5, +10: 1, +12: 1}`.

No tested config reduces the Asia card-1 residuals to <=10, so this run does not support applying only the SK/USA-adjacency hypotheses as a fix.

## TS PDF Spot Check

Source checked: GMT `TS_Rules-2015.pdf`.

- Setup lines 3.1-3.3 put the China Card with USSR, USSR influence 3 in North Korea, and US influence 1 each in Japan, Philippines, and South Korea.
- Rule 2.1.7 requires influence at least stability and at least stability more than the opponent to control a country.
- Rule 10.1.1/10.1.2 scores Presence/Domination/Control plus +1 per controlled battleground and +1 per controlled country adjacent to the enemy superpower.
- In `tsreplayer_16`, the T1 headline Asia Scoring occurs before any Asia changes beyond fixed setup and unrelated bid placements.
- With PDF control rules, US does not control Japan, South Korea, or Philippines at 1 influence each; USSR controls North Korea. That gives USSR Presence 3 + North Korea BG 1 = USSR +4 under the PDF scoring text. Under this repo's current Asia/China-card convention, add +1 for USSR holding China, yielding USSR +5. The log records USSR +1.

So the T1 spot check confirms a tsreplayer convention/implementation discrepancy against the PDF scoring/control rules; it does not independently validate the SK-as-not-BG hypothesis under normal control thresholds.

PDF references:

- https://s3-us-west-2.amazonaws.com/gmtwebsiteassets/nnts/TS_Rules-2015.pdf lines 209-215, 717-740, 757-776
