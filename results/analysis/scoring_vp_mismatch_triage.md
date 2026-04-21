# SCORING_VP_MISMATCH Triage

Generated from `results/validator_violations.jsonl` after re-running `scripts/validate_replays.py` on `data/raw_logs` filtered to `tsreplayer_*` logs.

Conventions: `expected_vp` is the VP delta logged by the human replay corpus; `actual_vp` is the engine/validator scoring delta; `delta = actual_vp - expected_vp`.

## Summary

| Card | Region | Violations | Delta pattern | Primary hypothesis |
|---:|---|---:|---|---|
| 1 | Asia | 85 | +5 x15, +4 x12, +2 x9, +3 x9, +7 x8 | Asia scoring pool likely excludes Southeast Asia countries that the log scores with Asia. |
| 2 | Europe | 65 | +3 x19, -1 x11, +1 x10, -2 x10, +2 x5 | Europe VP table uses 1/3 base values instead of 3/7. |
| 80 | Africa | 15 | +6 x4, +1 x4, -1 x3, +4 x2, +2 x1 | Africa country metadata likely has wrong battleground/stability inputs for score_region(). |

## Card 1: Asia Scoring

| game_id | turn | region | expected_vp | actual_vp | delta | influence_summary |
|---|---:|---|---:|---:|---:|---|
| f8aa2f9ff2e1 | 7 | Asia | 1 | 8 | 7 | US Domination BG[India, Indonesia, Thailand, Vietnam] ctrl[India, Burma, Indonesia, Laos/Cambodia, Thailand, Vietnam, Malaysia]; USSR Presence BG[North Korea, Pakistan, South Korea] ctrl[Afghanistan, North Korea, Pakistan, South Korea] |
| 12ab145e62a8 | 2 | Asia | 2 | 4 | 2 | US Presence BG[Japan, Indonesia, Philippines, Thailand] ctrl[Japan, Burma, Indonesia, Philippines, Thailand, Malaysia]; USSR Presence BG[India, Pakistan, South Korea, Vietnam] ctrl[India, Pakistan, South Korea, Laos/Cambodia, Vietnam] |
| 12ab145e62a8 | 5 | Asia | 1 | 8 | 7 | US Presence BG[Japan, Indonesia, Philippines, Thailand] ctrl[Japan, Burma, Indonesia, Laos/Cambodia, Philippines, Thailand, Malaysia]; USSR Presence BG[India, Pakistan, South Korea, Vietnam] ctrl[India, Pakistan, South Korea, Vietnam] |
| c9c4f45d2e1a | 2 | Asia | 3 | 7 | 4 | US Presence BG[Indonesia, Philippines, Thailand, Vietnam] ctrl[Indonesia, Philippines, Thailand, Vietnam, Malaysia]; USSR Presence BG[India, North Korea, Pakistan, South Korea] ctrl[India, North Korea, Pakistan, South Korea, Laos/Cambodia] |
| c9c4f45d2e1a | 3 | Asia | 6 | 3 | -3 | US Presence BG[Japan, Philippines, Thailand] ctrl[Japan, Philippines, Thailand]; USSR Domination BG[India, North Korea, Pakistan, South Korea] ctrl[India, North Korea, Pakistan, South Korea, Laos/Cambodia] |
| 55fe8addeb2c | 1 | Asia | 1 | 5 | 4 | US None BG[-] ctrl[-]; USSR Presence BG[North Korea] ctrl[North Korea] |
| 55fe8addeb2c | 6 | Asia | 0 | -3 | -3 | US Domination BG[North Korea, South Korea, Indonesia, Philippines, Taiwan] ctrl[North Korea, South Korea, Burma, Indonesia, Laos/Cambodia, Philippines, Malaysia, Taiwan]; USSR Presence BG[India, Pakistan, Thailand, Vietnam] ctrl[India, Pakistan, Thailand, Vietnam] |
| 55fe8addeb2c | 9 | Asia | -7 | -8 | -1 | US Domination BG[Japan, North Korea, South Korea, Philippines, Taiwan] ctrl[Afghanistan, Japan, North Korea, South Korea, Burma, Laos/Cambodia, Philippines, Malaysia, Taiwan]; USSR Presence BG[India, Pakistan, Thailand, Vietnam] ctrl[India, Pakistan, Thailand, Vietnam] |
| ed16373d1b09 | 3 | Asia | 2 | 7 | 5 | US Presence BG[Indonesia, Thailand] ctrl[Indonesia, Laos/Cambodia, Thailand]; USSR Presence BG[India, North Korea, Pakistan] ctrl[India, North Korea, Pakistan] |
| ed16373d1b09 | 7 | Asia | 1 | 13 | 12 | US Domination BG[Japan, Indonesia, Philippines, Thailand, Vietnam] ctrl[Japan, Indonesia, Laos/Cambodia, Philippines, Thailand, Vietnam, Malaysia]; USSR Presence BG[India, North Korea, Pakistan, South Korea] ctrl[India, North Korea, Pakistan, South Korea] |

Root-cause hypothesis: 68/85 deltas are positive, meaning the engine usually awards more USSR VP than the log. The largest examples have heavy US control in Southeast Asia (Indonesia, Thailand, Vietnam, Philippines/Malaysia) while `actual_vp` still favors the USSR from the non-SE Asia pool. This points at the current `Region::Asia` scoring pool excluding `Region::SoutheastAsia` countries for card 1.

Most likely source: `cpp/tscore/scoring.cpp::apply_scoring_card()` dispatches card 1 to `score_region(Region::Asia)` at lines 231-236; `score_region()` builds `region_ids` by exact country region at lines 141-153. The mirrored Python validator path has the same behavior in `python/tsrl/engine/scoring.py::score_region()` lines 202-211 and `apply_scoring_card()` lines 483-488.

## Card 2: Europe Scoring

| game_id | turn | region | expected_vp | actual_vp | delta | influence_summary |
|---|---:|---|---:|---:|---:|---|
| 15117c0472b0 | 2 | Europe | -5 | -3 | 2 | US Domination BG[France, Italy, West Germany] ctrl[France, Greece, Italy, West Germany]; USSR Presence BG[East Germany, Poland] ctrl[East Germany, Poland, Romania] |
| 12ab145e62a8 | 5 | Europe | -5 | -4 | 1 | US Domination BG[France, Italy, UK, West Germany] ctrl[Canada, France, Italy, UK, West Germany]; USSR Presence BG[East Germany, Poland] ctrl[East Germany, Poland] |
| 55fe8addeb2c | 2 | Europe | -5 | -4 | 1 | US Domination BG[France, Italy, UK, West Germany] ctrl[France, Greece, Italy, UK, West Germany]; USSR Presence BG[East Germany, Poland] ctrl[East Germany, Poland, Romania, Yugoslavia] |
| 55fe8addeb2c | 3 | Europe | -5 | -4 | 1 | US Domination BG[France, Italy, UK, West Germany] ctrl[France, Greece, Italy, UK, West Germany]; USSR Presence BG[East Germany, Poland] ctrl[East Germany, Poland, Yugoslavia] |
| 55fe8addeb2c | 8 | Europe | 0 | -3 | -3 | US Domination BG[Italy, UK, West Germany] ctrl[Greece, Italy, UK, West Germany]; USSR Presence BG[East Germany, France] ctrl[East Germany, France, Yugoslavia] |
| ed16373d1b09 | 3 | Europe | 5 | 0 | -5 | US Presence BG[Italy, UK] ctrl[Italy, UK]; USSR Presence BG[East Germany, Poland] ctrl[East Germany, Poland, Romania] |
| f56f6ebd06c6 | 3 | Europe | -5 | -2 | 3 | US Presence BG[France, Italy, UK, West Germany] ctrl[France, Italy, UK, West Germany]; USSR Presence BG[East Germany, Poland] ctrl[East Germany, Poland] |
| 24181cce3c92 | 3 | Europe | 6 | 0 | -6 | US Presence BG[Turkey, UK, West Germany] ctrl[Canada, Turkey, UK, West Germany]; USSR Presence BG[East Germany, Italy, Poland] ctrl[East Germany, Italy, Poland, Spain/Portugal, Yugoslavia] |
| 24181cce3c92 | 9 | Europe | 7 | 3 | -4 | US Presence BG[Turkey, UK, West Germany] ctrl[Canada, Turkey, UK, West Germany]; USSR Domination BG[East Germany, France, Italy, Poland] ctrl[East Germany, France, Italy, Poland, Romania, Spain/Portugal] |
| be034874e282 | 3 | Europe | -5 | -2 | 3 | US Presence BG[France, Italy, UK, West Germany] ctrl[France, Italy, UK, West Germany]; USSR Presence BG[East Germany, Poland] ctrl[East Germany, Poland, Romania] |

Root-cause hypothesis: the repeated pairs `expected=-5, actual=-2/-3/-4` and `expected=5/6/7, actual=0/3` match a Europe base-table error. The engine scores Europe presence/domination as 1/3, so domination-vs-presence gaps are compressed by about 2-6 VP depending on both sides' tiers and battleground counts. The corpus expects the standard Europe presence/domination base values of 3/7, with control still an auto-win sentinel.

Most likely source: `cpp/tscore/scoring.cpp::kRegionVp` first row at lines 23-29 is `{1, 3, kGameWinEurope}` for Europe. The mirrored Python table is `python/tsrl/engine/scoring.py::_REGION_VP` line 81.

## Card 80: Africa Scoring

| game_id | turn | region | expected_vp | actual_vp | delta | influence_summary |
|---|---:|---|---:|---:|---:|---|
| 12ab145e62a8 | 6 | Africa | 0 | 4 | 4 | US Presence BG[Algeria, Nigeria] ctrl[Algeria, Nigeria, Saharan States]; USSR Domination BG[Angola, Congo/Zaire, South Africa] ctrl[Angola, Cameroon, Congo/Zaire, South Africa] |
| 55fe8addeb2c | 4 | Africa | -4 | -5 | -1 | US Domination BG[Algeria, Nigeria, South Africa] ctrl[Algeria, Nigeria, South Africa, Zimbabwe]; USSR Presence BG[Angola] ctrl[Angola] |
| 24181cce3c92 | 4 | Africa | -10 | -4 | 6 | US Presence BG[Algeria, Angola, Nigeria, South Africa] ctrl[Algeria, Angola, Nigeria, South Africa]; USSR Presence BG[-] ctrl[Saharan States] |
| ee8828e70aa2 | 7 | Africa | -6 | -2 | 4 | US Presence BG[Algeria, Angola, Nigeria] ctrl[Algeria, Angola, Ivory Coast, Nigeria]; USSR Presence BG[South Africa] ctrl[Cameroon, Saharan States, South Africa, Sudan] |
| e21f34ec5186 | 7 | Africa | -11 | -9 | 2 | US Domination BG[Algeria, Angola, Congo/Zaire, Nigeria, South Africa] ctrl[Algeria, Angola, Congo/Zaire, Nigeria, Saharan States, South Africa]; USSR None BG[-] ctrl[-] |
| 5a8e16231aff | 6 | Africa | -1 | 0 | 1 | US Presence BG[Angola, South Africa] ctrl[Angola, South Africa, Tunisia]; USSR Presence BG[Algeria, Nigeria] ctrl[Algeria, Ivory Coast, Nigeria, Saharan States, Sudan] |
| 5a8e16231aff | 8 | Africa | -1 | 0 | 1 | US Presence BG[Angola, South Africa] ctrl[Angola, South Africa, Tunisia]; USSR Presence BG[Algeria, Nigeria] ctrl[Algeria, Ivory Coast, Nigeria, Saharan States, Sudan] |
| 66dca28a6d20 | 4 | Africa | 3 | 2 | -1 | US Presence BG[South Africa] ctrl[South Africa]; USSR Presence BG[Algeria, Angola, Nigeria] ctrl[Algeria, Angola, Nigeria] |
| 66dca28a6d20 | 8 | Africa | -10 | -7 | 3 | US Domination BG[Algeria, Angola, Nigeria, South Africa] ctrl[Algeria, Angola, Cameroon, Nigeria, South Africa, Zimbabwe]; USSR Presence BG[-] ctrl[Botswana] |
| 0ee818b3635d | 5 | Africa | -11 | -5 | 6 | US Presence BG[Algeria, Angola, Nigeria, South Africa] ctrl[Algeria, Angola, Nigeria, South Africa]; USSR None BG[-] ctrl[-] |

Root-cause hypothesis: high positive deltas (`actual` less favorable to US than the log) line up with Africa metadata rather than the Africa VP base table. Example patterns like `expected=-11, actual=-5` are explained if the log treats Zaire/Congo as stability 1 and Africa as having five battlegrounds (Algeria, Angola, Zaire/Congo, Nigeria, South Africa). Current metadata has Congo/Zaire stability 2 and marks Ethiopia/Morocco as battlegrounds, so `score_region()` with current specs denies Africa control and undercounts controlled battlegrounds. Raw logs also show Zaire coup formulas using `2x1` stability.

Most likely source: `cpp/tscore/scoring.cpp::score_region()` lines 141-156 and `is_scoring_battleground()` lines 32-33 consume `country_spec()` for region, stability, and battleground status. The suspect inputs are `data/spec/countries.csv` lines 131-137 and 151-152, not a local scoring arithmetic branch. The mirrored Python path uses the same metadata in `python/tsrl/engine/scoring.py::score_region()` lines 194-216.
