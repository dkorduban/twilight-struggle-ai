# minimal_hybrid detailed rollout log

- seed: `20260512`
- winner: `US`
- final_vp: `-7`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Fidel[8], Arab-Israeli War[13], Truman Doctrine[19], East European Unrest[29], Nuclear Test Ban[34], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], COMECON[14], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], NATO[21], Indo-Pakistani War[24], Red Scare/Purge[31]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +3, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Fidel[8], Arab-Israeli War[13], Truman Doctrine[19], East European Unrest[29], The Cambridge Five[36], NORAD[38]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Arab-Israeli War COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | The Cambridge Five COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Duck and Cover COUP Iran | 54.83 | 4.00 | 71.28 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | East European Unrest COUP Iran | 54.83 | 4.00 | 71.28 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], COMECON[14], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], Indo-Pakistani War[24], Red Scare/Purge[31]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE Turkey, North Korea, Indonesia, Philippines | 79.37 | 6.00 | 75.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Olympic Games INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Indo-Pakistani War INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 4 | COMECON INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Red Scare/Purge COUP Syria | 36.68 | 4.00 | 33.28 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Truman Doctrine[19], East European Unrest[29], The Cambridge Five[36], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE North Korea, Thailand | 48.70 | 6.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | The Cambridge Five INFLUENCE North Korea, Thailand | 48.70 | 6.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 3 | Arab-Israeli War COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | The Cambridge Five COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Duck and Cover INFLUENCE Japan, North Korea, Thailand | 46.70 | 6.00 | 61.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], COMECON[14], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], Indo-Pakistani War[24]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, France | 38.20 | 6.00 | 34.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, non_coup_milops_penalty:1.60 |
| 2 | Indo-Pakistani War INFLUENCE East Germany, France | 38.20 | 6.00 | 34.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, non_coup_milops_penalty:1.60 |
| 3 | COMECON INFLUENCE East Germany, France, Panama | 34.25 | 6.00 | 50.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Olympic Games COUP Syria | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Syria | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Duck and Cover[4], Truman Doctrine[19], East European Unrest[29], The Cambridge Five[36], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, Thailand | 51.20 | 6.00 | 45.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, control_break:Thailand |
| 2 | Duck and Cover INFLUENCE East Germany, Japan, Thailand | 49.20 | 6.00 | 63.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | East European Unrest INFLUENCE East Germany, Japan, Thailand | 49.20 | 6.00 | 63.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | NORAD INFLUENCE East Germany, Japan, Thailand | 49.20 | 6.00 | 63.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | The Cambridge Five COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], COMECON[14], Nasser[15], Captured Nazi Scientist[18], Indo-Pakistani War[24]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Italy, Panama | 36.35 | 6.00 | 32.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.00 |
| 2 | COMECON INFLUENCE Italy, Japan, Panama | 32.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Indo-Pakistani War COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Indonesia | 25.80 | 4.00 | 22.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | Captured Nazi Scientist COUP North Korea | 23.40 | 4.00 | 19.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Truman Doctrine[19], East European Unrest[29], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan, Thailand | 41.80 | 6.00 | 56.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | East European Unrest INFLUENCE West Germany, Japan, Thailand | 41.80 | 6.00 | 56.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE West Germany, Japan, Thailand | 41.80 | 6.00 | 56.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Duck and Cover COUP Iran | 33.50 | 4.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | East European Unrest COUP Iran | 33.50 | 4.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], COMECON[14], Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, West Germany, Japan | 39.13 | 6.00 | 56.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Vietnam Revolts INFLUENCE Italy, West Germany | 27.13 | 6.00 | 40.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Captured Nazi Scientist COUP Japan | 24.17 | 4.00 | 20.32 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.33 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 23.83 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:2.67 |
| 5 | Captured Nazi Scientist COUP North Korea | 23.57 | 4.00 | 19.72 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], East European Unrest[29], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Pakistan, South Korea, Thailand | 40.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE Pakistan, South Korea, Thailand | 40.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 3 | East European Unrest COUP Iran | 33.50 | 4.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 4 | NORAD COUP Iran | 33.50 | 4.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | Truman Doctrine COUP Iran | 30.80 | 4.00 | 38.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Japan | 24.50 | 4.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.50 |
| 2 | Captured Nazi Scientist COUP North Korea | 23.90 | 4.00 | 20.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.50 |
| 3 | Captured Nazi Scientist COUP South Korea | 23.90 | 4.00 | 20.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:1, milops_urgency:0.50 |
| 4 | Captured Nazi Scientist COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Indonesia | 20.95 | 4.00 | 17.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 13: T1 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], NORAD[38]`
- state: `VP 3, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE India, Pakistan, Thailand | 43.50 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | NORAD COUP Lebanon | 0.40 | 4.00 | 16.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15]`
- state: `VP 3, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Japan, Egypt | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 2 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Vietnam Revolts SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Syria | 8.65 | 4.00 | 20.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Nasser COUP Syria | 7.30 | 4.00 | 15.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Socialist Governments[7], Containment[25], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 4 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Blockade[10], Romanian Abdication[12], De Gaulle Leads France[17], Independent Reds[22], Marshall Plan[23], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Containment[25], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Italy, Israel, Philippines, Thailand | 48.98 | 6.00 | 70.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Five Year Plan INFLUENCE Italy, Israel, Thailand | 36.68 | 6.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Containment INFLUENCE Italy, Israel, Thailand | 36.68 | 6.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | UN Intervention COUP Philippines | 30.22 | 4.00 | 26.37 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Israel | 27.92 | 4.00 | 24.07 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Blockade[10], Romanian Abdication[12], De Gaulle Leads France[17], Independent Reds[22], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Egypt, Philippines | 41.18 | 6.00 | 38.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 2 | De Gaulle Leads France INFLUENCE Japan, Egypt, Philippines | 37.18 | 6.00 | 54.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Suez Crisis INFLUENCE Japan, Egypt, Philippines | 37.18 | 6.00 | 54.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | De-Stalinization INFLUENCE Japan, Egypt, Philippines | 37.18 | 6.00 | 54.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Independent Reds COUP Philippines | 31.57 | 4.00 | 27.87 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Containment[25], CIA Created[26], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Indonesia | 40.75 | 4.00 | 36.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 2 | Five Year Plan INFLUENCE Japan, Saudi Arabia, Thailand | 35.25 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Containment INFLUENCE Japan, Saudi Arabia, Thailand | 35.25 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Five Year Plan COUP Indonesia | 32.45 | 4.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Containment COUP Indonesia | 32.45 | 4.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 20: T2 AR2 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], De Gaulle Leads France[17], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Japan, Libya, Indonesia | 30.05 | 6.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 2 | Suez Crisis INFLUENCE Japan, Libya, Indonesia | 30.05 | 6.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | De-Stalinization INFLUENCE Japan, Libya, Indonesia | 30.05 | 6.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Decolonization INFLUENCE Japan, Indonesia | 18.50 | 6.00 | 32.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | De Gaulle Leads France COUP Syria | 12.80 | 4.00 | 29.25 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Containment[25], CIA Created[26], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Saudi Arabia, Thailand | 36.45 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Containment INFLUENCE Japan, Saudi Arabia, Thailand | 36.45 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Formosan Resolution INFLUENCE Saudi Arabia, Thailand | 24.45 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Special Relationship INFLUENCE Saudi Arabia, Thailand | 24.45 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | CIA Created INFLUENCE Thailand | 12.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, Libya | 32.05 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | De-Stalinization INFLUENCE West Germany, Japan, Libya | 32.05 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Decolonization INFLUENCE Japan, Libya | 20.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Suez Crisis COUP Syria | 13.00 | 4.00 | 29.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Syria | 13.00 | 4.00 | 29.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Containment[25], CIA Created[26], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Egypt, Thailand | 35.18 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Formosan Resolution INFLUENCE Japan, Thailand | 23.63 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 23.63 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | CIA Created INFLUENCE Thailand | 11.63 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Formosan Resolution SPACE | 6.03 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan, Egypt | 30.72 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Decolonization INFLUENCE Japan, Egypt | 19.22 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | De-Stalinization COUP Syria | 13.33 | 4.00 | 29.78 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Decolonization COUP Syria | 11.98 | 4.00 | 24.28 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Egypt | 10.83 | 4.00 | 27.28 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Thailand | 19.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Special Relationship INFLUENCE Japan, Thailand | 19.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Formosan Resolution COUP Libya | 13.15 | 4.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Special Relationship COUP Libya | 13.15 | 4.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | CIA Created COUP Libya | 11.80 | 4.00 | 19.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Decolonization[30]`
- state: `VP 4, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Blockade COUP Syria | 10.30 | 4.00 | 18.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Syria | 10.30 | 4.00 | 18.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Decolonization COUP Egypt | 10.15 | 4.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Blockade COUP Egypt | 7.80 | 4.00 | 15.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 27: T2 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `CIA Created[26], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan, Thailand | 15.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | Special Relationship COUP Libya | 14.15 | 4.00 | 26.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | CIA Created COUP Libya | 12.80 | 4.00 | 20.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Special Relationship COUP Egypt | 9.15 | 4.00 | 21.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | CIA Created COUP Egypt | 7.80 | 4.00 | 15.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP 4, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Blockade COUP Syria | 7.30 | 4.00 | 15.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Syria | 7.30 | 4.00 | 15.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Blockade COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Vietnam Revolts[9], Korean War[11], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Independent Reds[22], US/Japan Mutual Defense Pact[27], Decolonization[30], UN Intervention[32]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Blockade[10], Arab-Israeli War[13], COMECON[14], CIA Created[26], Suez Crisis[28], Red Scare/Purge[31]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Vietnam Revolts[9], Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], US/Japan Mutual Defense Pact[27], Decolonization[30], UN Intervention[32]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 2 | Korean War COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 3 | Decolonization COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 4 | Vietnam Revolts COUP Libya | 36.15 | 4.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 5 | Korean War COUP Libya | 36.15 | 4.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 32: T3 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Blockade[10], Arab-Israeli War[13], COMECON[14], CIA Created[26], Suez Crisis[28]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan, Indonesia | 49.20 | 6.00 | 47.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Five Year Plan INFLUENCE West Germany, Japan, Indonesia | 49.20 | 6.00 | 47.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 3 | Duck and Cover COUP Syria | 34.00 | 4.00 | 30.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | Five Year Plan COUP Syria | 34.00 | 4.00 | 30.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Duck and Cover COUP Egypt | 31.50 | 4.00 | 27.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], US/Japan Mutual Defense Pact[27], Decolonization[30], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Japan, Libya, Thailand | 32.10 | 6.00 | 52.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 24.70 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:1.60 |
| 3 | UN Intervention INFLUENCE Thailand | 24.70 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:1.60 |
| 4 | Korean War INFLUENCE Thailand | 24.55 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:1.60 |
| 5 | Decolonization INFLUENCE Thailand | 24.55 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Arab-Israeli War[13], COMECON[14], CIA Created[26], Suez Crisis[28]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan, Libya | 51.25 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.80 |
| 2 | Five Year Plan COUP Syria | 34.20 | 4.00 | 30.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 3 | Five Year Plan COUP Egypt | 31.70 | 4.00 | 28.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:2.5 |
| 4 | Five Year Plan COUP Libya | 31.70 | 4.00 | 28.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:2.5 |
| 5 | COMECON INFLUENCE West Germany, Japan, Libya | 31.25 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], Decolonization[30], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 24.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | UN Intervention INFLUENCE Thailand | 24.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Korean War INFLUENCE Thailand | 24.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | Decolonization INFLUENCE Thailand | 24.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Korean War COUP Lebanon | 16.55 | 4.00 | 12.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], COMECON[14], CIA Created[26], Suez Crisis[28]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan, North Korea | 31.90 | 6.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, North Korea | 31.90 | 6.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | CIA Created COUP Syria | 21.80 | 4.00 | 17.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:0.5 |
| 4 | CIA Created INFLUENCE Japan | 21.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:6.00 |
| 5 | Arab-Israeli War INFLUENCE West Germany, Japan | 20.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Korean War[11], Independent Reds[22], Decolonization[30], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE North Korea | 23.73 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:2.67 |
| 2 | Korean War INFLUENCE North Korea | 23.58 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:2.67 |
| 3 | Decolonization INFLUENCE North Korea | 23.58 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:2.67 |
| 4 | Korean War COUP Lebanon | 16.72 | 4.00 | 13.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Decolonization COUP Lebanon | 16.72 | 4.00 | 13.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], CIA Created[26], Suez Crisis[28]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, North Korea | 24.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | CIA Created COUP Syria | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 3 | CIA Created COUP Egypt | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | CIA Created COUP Libya | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | CIA Created COUP Israel | 18.25 | 4.00 | 14.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Korean War[11], Independent Reds[22], Decolonization[30]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Egypt | 24.15 | 4.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 2 | Korean War COUP Libya | 24.15 | 4.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 3 | Decolonization COUP Egypt | 24.15 | 4.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 4 | Decolonization COUP Libya | 24.15 | 4.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | Korean War INFLUENCE North Korea | 19.25 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Arab-Israeli War[13], CIA Created[26]`
- state: `VP 3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP SE African States | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | CIA Created COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | CIA Created COUP Zimbabwe | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | CIA Created COUP Colombia | 10.95 | 4.00 | 7.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Arab-Israeli War COUP SE African States | 1.80 | 4.00 | 14.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Independent Reds[22], Decolonization[30]`
- state: `VP 3, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Sudan | 15.80 | 4.00 | 12.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Decolonization INFLUENCE North Korea | 15.25 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:11.00 |
| 3 | Decolonization COUP Tunisia | 5.40 | 4.00 | 1.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:1.5 |
| 4 | Independent Reds COUP Sudan | -0.20 | 4.00 | 12.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Independent Reds INFLUENCE North Korea | -0.75 | 6.00 | 20.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13]`
- state: `VP 3, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Sudan | 22.80 | 4.00 | 35.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Blockade COUP Sudan | 20.45 | 4.00 | 28.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Mozambique | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP SE African States | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Zimbabwe | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-1`

## Step 43: T4 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Independent Reds[22], Red Scare/Purge[31], NORAD[38], Brush War[39], Quagmire[45], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], US/Japan Mutual Defense Pact[27], Suez Crisis[28], UN Intervention[32], Special Relationship[37], Junta[50], ABM Treaty[60], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Independent Reds[22], NORAD[38], Brush War[39], Quagmire[45], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE North Korea, Mexico, Ethiopia | 57.33 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Mexico:14.95, access_touch:Mexico, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |
| 2 | Quagmire INFLUENCE North Korea, Mexico, Ethiopia | 57.33 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Mexico:14.95, access_touch:Mexico, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |
| 3 | South African Unrest INFLUENCE North Korea, Ethiopia | 40.53 | 6.00 | 39.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |
| 4 | Willy Brandt INFLUENCE North Korea, Ethiopia | 40.53 | 6.00 | 39.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |
| 5 | Liberation Theology INFLUENCE North Korea, Ethiopia | 40.53 | 6.00 | 39.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Suez Crisis[28], UN Intervention[32], Special Relationship[37], Junta[50], ABM Treaty[60], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE Mexico, Angola, South Africa | 57.18 | 6.00 | 56.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 2 | ABM Treaty COUP Sudan | 51.39 | 4.00 | 47.99 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:5.5 |
| 3 | Duck and Cover COUP Sudan | 45.04 | 4.00 | 41.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:4.5 |
| 4 | ABM Treaty COUP Mexico | 44.24 | 4.00 | 40.84 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 5 | Duck and Cover INFLUENCE Mexico, Angola | 40.53 | 6.00 | 39.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Independent Reds[22], NORAD[38], Quagmire[45], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE UK, West Germany, Algeria | 48.72 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |
| 2 | Quagmire COUP Mexico | 33.08 | 4.00 | 29.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5 |
| 3 | South African Unrest INFLUENCE UK, Algeria | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |
| 4 | Willy Brandt INFLUENCE UK, Algeria | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |
| 5 | Liberation Theology INFLUENCE UK, Algeria | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Suez Crisis[28], UN Intervention[32], Special Relationship[37], Junta[50], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Sudan | 45.23 | 4.00 | 41.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 2 | Duck and Cover INFLUENCE UK, South Africa | 41.17 | 6.00 | 40.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 3 | Special Relationship COUP Sudan | 38.88 | 4.00 | 35.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 4 | Junta COUP Sudan | 38.88 | 4.00 | 35.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 5 | Lonely Hearts Club Band COUP Sudan | 38.88 | 4.00 | 35.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 49: T4 AR3 USSR

- chosen: `South African Unrest [56] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Independent Reds[22], NORAD[38], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Sudan | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 2 | Willy Brandt COUP Sudan | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 3 | Liberation Theology COUP Sudan | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 4 | South African Unrest INFLUENCE Algeria, Morocco | 35.30 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:6.40 |
| 5 | Willy Brandt INFLUENCE Algeria, Morocco | 35.30 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 50: T4 AR3 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Suez Crisis[28], UN Intervention[32], Special Relationship[37], Junta[50], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE South Africa | 26.05 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:1.60 |
| 2 | Special Relationship INFLUENCE South Africa | 25.90 | 6.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:1.60 |
| 3 | Junta INFLUENCE South Africa | 25.90 | 6.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:1.60 |
| 4 | Lonely Hearts Club Band INFLUENCE South Africa | 25.90 | 6.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:1.60 |
| 5 | Special Relationship COUP Syria | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Romanian Abdication[12], Independent Reds[22], NORAD[38], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE Algeria, Morocco | 37.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 2 | Liberation Theology INFLUENCE Algeria, Morocco | 37.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 3 | NORAD INFLUENCE West Germany, Algeria, Morocco | 33.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Willy Brandt COUP Mexico | 26.40 | 4.00 | 22.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | Liberation Theology COUP Mexico | 26.40 | 4.00 | 22.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:1`
- hand: `Suez Crisis[28], Special Relationship[37], Junta[50], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Syria | 25.65 | 4.00 | 21.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 2 | Junta COUP Syria | 25.65 | 4.00 | 21.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 3 | Lonely Hearts Club Band COUP Syria | 25.65 | 4.00 | 21.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 4 | Special Relationship INFLUENCE UK | 22.85 | 6.00 | 19.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, non_coup_milops_penalty:2.00 |
| 5 | Junta INFLUENCE UK | 22.85 | 6.00 | 19.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Romanian Abdication[12], Independent Reds[22], NORAD[38], Liberation Theology[76]`
- state: `VP 3, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 32.07 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 2 | NORAD INFLUENCE East Germany, France, West Germany | 27.47 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Liberation Theology COUP Mexico | 26.73 | 4.00 | 23.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 4 | Liberation Theology COUP Egypt | 24.98 | 4.00 | 21.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | Liberation Theology COUP Libya | 24.98 | 4.00 | 21.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Suez Crisis[28], Junta[50], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE UK | 22.18 | 6.00 | 19.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, non_coup_milops_penalty:2.67 |
| 2 | Lonely Hearts Club Band INFLUENCE UK | 22.18 | 6.00 | 19.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, non_coup_milops_penalty:2.67 |
| 3 | Suez Crisis INFLUENCE UK, South Africa | 18.83 | 6.00 | 35.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Junta COUP Colombia | 17.22 | 4.00 | 13.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Junta COUP Mozambique | 17.22 | 4.00 | 13.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Romanian Abdication[12], Independent Reds[22], NORAD[38]`
- state: `VP 3, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | Romanian Abdication COUP Egypt | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Romanian Abdication COUP Libya | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | NORAD INFLUENCE East Germany, France, West Germany | 18.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Romanian Abdication COUP Israel | 17.75 | 4.00 | 13.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:1`
- hand: `Suez Crisis[28], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Colombia | 17.55 | 4.00 | 13.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Lonely Hearts Club Band COUP Mozambique | 17.55 | 4.00 | 13.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Lonely Hearts Club Band COUP SE African States | 17.55 | 4.00 | 13.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Lonely Hearts Club Band COUP Sudan | 17.55 | 4.00 | 13.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Lonely Hearts Club Band COUP Zimbabwe | 17.55 | 4.00 | 13.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22], NORAD[38]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany | 10.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 2 | NORAD COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | NORAD COUP Sudan | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | NORAD COUP Guatemala | 5.65 | 4.00 | 22.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Independent Reds COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Suez Crisis[28], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Brazil, South Africa | 7.55 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | Suez Crisis COUP Colombia | 3.90 | 4.00 | 20.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Suez Crisis COUP Mozambique | 3.90 | 4.00 | 20.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Suez Crisis COUP SE African States | 3.90 | 4.00 | 20.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Suez Crisis COUP Sudan | 3.90 | 4.00 | 20.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 59: T5 AR0 USSR

- chosen: `Olympic Games [20] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], Olympic Games[20], CIA Created[26], US/Japan Mutual Defense Pact[27], Decolonization[30], Bear Trap[47], Portuguese Empire Crumbles[55], Latin American Death Squads[70], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], CIA Created[26], Decolonization[30], Red Scare/Purge[31], Cultural Revolution[61], Flower Power[62], Sadat Expels Soviets[73], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Cultural Revolution EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], CIA Created[26], US/Japan Mutual Defense Pact[27], Decolonization[30], Bear Trap[47], Portuguese Empire Crumbles[55], Latin American Death Squads[70], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany | 27.94 | 6.00 | 52.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 2 | Blockade INFLUENCE France | 20.69 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:5.71 |
| 3 | Decolonization INFLUENCE France | 20.54 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:5.71 |
| 4 | Portuguese Empire Crumbles INFLUENCE France | 20.54 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:5.71 |
| 5 | Latin American Death Squads INFLUENCE France | 20.54 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], CIA Created[26], Decolonization[30], Cultural Revolution[61], Flower Power[62], Sadat Expels Soviets[73], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE Argentina, Brazil, South Africa | 54.04 | 6.00 | 54.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Brazil, South Africa | 54.04 | 6.00 | 54.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Cultural Revolution INFLUENCE Argentina, Brazil, South Africa | 34.04 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 4 | Sadat Expels Soviets COUP Colombia | 25.33 | 4.00 | 21.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, empty_coup_penalty, expected_swing:4.5 |
| 5 | Sadat Expels Soviets COUP Mozambique | 25.33 | 4.00 | 21.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:0.71, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], CIA Created[26], Decolonization[30], Bear Trap[47], Portuguese Empire Crumbles[55], Latin American Death Squads[70], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Saharan States | 19.22 | 4.00 | 15.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 2 | Decolonization COUP Sudan | 19.22 | 4.00 | 15.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 3 | Portuguese Empire Crumbles COUP Saharan States | 19.22 | 4.00 | 15.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 4 | Portuguese Empire Crumbles COUP Sudan | 19.22 | 4.00 | 15.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Saharan States | 19.22 | 4.00 | 15.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 64: T5 AR2 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], CIA Created[26], Decolonization[30], Cultural Revolution[61], Flower Power[62], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Chile, South Africa | 55.68 | 6.00 | 56.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 2 | Cultural Revolution INFLUENCE Argentina, Chile, South Africa | 35.68 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 3 | Ask Not What Your Country Can Do For You COUP Colombia | 25.57 | 4.00 | 22.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:4.5 |
| 4 | Ask Not What Your Country Can Do For You COUP Mozambique | 25.57 | 4.00 | 22.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:4.5 |
| 5 | Ask Not What Your Country Can Do For You COUP SE African States | 25.57 | 4.00 | 22.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], CIA Created[26], Bear Trap[47], Portuguese Empire Crumbles[55], Latin American Death Squads[70], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Nigeria | 21.65 | 6.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.80 |
| 2 | Portuguese Empire Crumbles INFLUENCE Nigeria | 21.50 | 6.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.80 |
| 3 | Latin American Death Squads INFLUENCE Nigeria | 21.50 | 6.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.80 |
| 4 | Portuguese Empire Crumbles COUP Saharan States | 18.75 | 4.00 | 15.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | Portuguese Empire Crumbles COUP Sudan | 18.75 | 4.00 | 15.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], CIA Created[26], Decolonization[30], Cultural Revolution[61], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE Argentina, Chile, South Africa | 27.35 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Vietnam Revolts INFLUENCE Chile, South Africa | 15.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Decolonization INFLUENCE Chile, South Africa | 15.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Flower Power INFLUENCE Chile, South Africa | 15.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Colonial Rear Guards INFLUENCE Chile, South Africa | 15.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `CIA Created[26], Bear Trap[47], Portuguese Empire Crumbles[55], Latin American Death Squads[70], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Cameroon | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 2 | Portuguese Empire Crumbles COUP Saharan States | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 3 | Portuguese Empire Crumbles COUP Sudan | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Cameroon | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Saharan States | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], CIA Created[26], Decolonization[30], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Chile, South Africa | 18.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Decolonization INFLUENCE Chile, South Africa | 18.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Flower Power INFLUENCE Chile, South Africa | 18.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Colonial Rear Guards INFLUENCE Chile, South Africa | 18.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | CIA Created INFLUENCE Chile | 17.65 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `CIA Created[26], Bear Trap[47], Latin American Death Squads[70], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Cameroon | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Sudan | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Guatemala | 18.30 | 4.00 | 14.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads INFLUENCE Congo/Zaire | 13.90 | 6.00 | 16.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:5`
- hand: `CIA Created[26], Decolonization[30], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Colombia | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | CIA Created COUP Mozambique | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | CIA Created COUP SE African States | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | CIA Created COUP Sudan | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Zimbabwe | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 71: T5 AR6 USSR

- chosen: `Bear Trap [47] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Bear Trap[47], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Cameroon | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Bear Trap COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Bear Trap COUP Sudan | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Bear Trap COUP Guatemala | 5.65 | 4.00 | 22.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Cameroon | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 72: T5 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Decolonization[30], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Mozambique | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Decolonization COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Zimbabwe | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 73: T5 AR7 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Cameroon | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Guatemala | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Cameroon | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Flower Power COUP Mozambique | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Flower Power COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Zimbabwe | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 75: T6 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `COMECON[14], De Gaulle Leads France[17], Indo-Pakistani War[24], East European Unrest[29], UN Intervention[32], The Cambridge Five[36], We Will Bury You[53], Brezhnev Doctrine[54], Puppet Governments[67]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Korean War[11], Nasser[15], Captured Nazi Scientist[18], Containment[25], Cuban Missile Crisis[43], U2 Incident[63], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `COMECON[14], De Gaulle Leads France[17], Indo-Pakistani War[24], East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Brezhnev Doctrine[54], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, West Germany, Congo/Zaire | 46.59 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany, Congo/Zaire | 46.59 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Congo/Zaire | 46.59 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |
| 4 | Indo-Pakistani War INFLUENCE West Germany, Congo/Zaire | 31.19 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |
| 5 | The Cambridge Five INFLUENCE West Germany, Congo/Zaire | 31.19 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Korean War[11], Nasser[15], Captured Nazi Scientist[18], Cuban Missile Crisis[43], U2 Incident[63], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE Argentina, Chile, Venezuela, South Africa | 64.69 | 6.00 | 66.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | Nixon Plays the China Card INFLUENCE Argentina, Chile, South Africa | 48.64 | 6.00 | 49.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | U2 Incident INFLUENCE Argentina, Chile, Venezuela, South Africa | 44.69 | 6.00 | 66.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 4 | Vietnam Revolts INFLUENCE Argentina, Chile, South Africa | 32.64 | 6.00 | 49.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 5 | Korean War INFLUENCE Argentina, Chile, South Africa | 32.64 | 6.00 | 49.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `De Gaulle Leads France[17], Indo-Pakistani War[24], East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Brezhnev Doctrine[54], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Angola, Congo/Zaire | 50.50 | 6.00 | 52.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 2 | Brezhnev Doctrine INFLUENCE West Germany, Angola, Congo/Zaire | 50.50 | 6.00 | 52.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 3 | De Gaulle Leads France COUP SE African States | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 4 | Brezhnev Doctrine COUP SE African States | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 5 | Indo-Pakistani War COUP SE African States | 39.55 | 4.00 | 35.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Korean War[11], Nasser[15], Captured Nazi Scientist[18], U2 Incident[63], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE Chile, Venezuela, Angola | 54.30 | 6.00 | 56.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:8.00 |
| 2 | U2 Incident INFLUENCE Chile, Venezuela, Angola, South Africa | 50.95 | 6.00 | 73.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:Angola:15.60, control_break:Angola, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Vietnam Revolts INFLUENCE Chile, Venezuela, Angola | 38.30 | 6.00 | 56.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Korean War INFLUENCE Chile, Venezuela, Angola | 38.30 | 6.00 | 56.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Captured Nazi Scientist INFLUENCE Venezuela, Angola | 37.65 | 6.00 | 39.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Venezuela:14.20, control_break:Venezuela, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Brezhnev Doctrine [54] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Indo-Pakistani War[24], East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Brezhnev Doctrine[54], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine COUP SE African States | 46.30 | 4.00 | 42.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Angola | 43.25 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:9.60 |
| 3 | Indo-Pakistani War COUP SE African States | 39.95 | 4.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | The Cambridge Five COUP SE African States | 39.95 | 4.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 5 | UN Intervention COUP SE African States | 33.60 | 4.00 | 29.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 82: T6 AR3 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Korean War[11], Nasser[15], Captured Nazi Scientist[18], U2 Incident[63], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE Argentina, Chile, Algeria, South Africa | 41.95 | 6.00 | 66.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Vietnam Revolts INFLUENCE Argentina, Chile, South Africa | 29.90 | 6.00 | 49.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | Korean War INFLUENCE Argentina, Chile, South Africa | 29.90 | 6.00 | 49.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Captured Nazi Scientist INFLUENCE Chile, South Africa | 29.85 | 6.00 | 33.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 5 | Panama Canal Returned INFLUENCE Chile, South Africa | 29.85 | 6.00 | 33.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Indo-Pakistani War[24], East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, Algeria | 35.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, Algeria | 35.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |
| 3 | East European Unrest INFLUENCE West Germany, Algeria, Angola | 30.50 | 6.00 | 50.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | UN Intervention INFLUENCE Algeria | 19.05 | 6.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |
| 5 | Indo-Pakistani War COUP Cameroon | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Korean War[11], Nasser[15], Captured Nazi Scientist[18], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 34.20 | 4.00 | 30.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 34.20 | 4.00 | 30.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Vietnam Revolts INFLUENCE Chile, Morocco, South Africa | 28.10 | 6.00 | 50.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Korean War INFLUENCE Chile, Morocco, South Africa | 28.10 | 6.00 | 50.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Captured Nazi Scientist INFLUENCE Chile, Morocco | 27.45 | 6.00 | 33.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 85: T6 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, Angola | 29.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |
| 2 | East European Unrest INFLUENCE East Germany, West Germany, Angola | 24.85 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | The Cambridge Five COUP Cameroon | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | The Cambridge Five COUP SE African States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Korean War[11], Nasser[15], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, Chile, Angola | 34.92 | 6.00 | 58.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Korean War INFLUENCE West Germany, Chile, Angola | 34.92 | 6.00 | 58.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Panama Canal Returned COUP Saharan States | 34.53 | 4.00 | 30.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 4 | Panama Canal Returned INFLUENCE West Germany, Angola | 34.27 | 6.00 | 41.75 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:13.33 |
| 5 | Vietnam Revolts COUP Saharan States | 24.88 | 4.00 | 37.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `East European Unrest[29], UN Intervention[32], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Guatemala | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Nasser[15], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 2 | Korean War COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nasser COUP Saharan States | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Colombia | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP SE African States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `East European Unrest [29] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `East European Unrest[29], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | East European Unrest COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | East European Unrest COUP SE African States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | East European Unrest COUP Sudan | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | East European Unrest COUP Guatemala | 8.65 | 4.00 | 25.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Korean War[11], Nasser[15]`
- state: `VP 4, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Colombia | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Korean War COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Korean War COUP SE African States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Korean War COUP Sudan | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Korean War COUP Zimbabwe | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-1`

## Step 91: T7 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], COMECON[14], Independent Reds[22], Nuclear Subs[44], Summit[48], Kitchen Debates[51], Ussuri River Skirmish[77], One Small Step[81]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Duck and Cover[4], Five Year Plan[5], Socialist Governments[7], Suez Crisis[28], Arms Race[42], Grain Sales to Soviets[68], OAS Founded[71], Voice of America[75], Alliance for Progress[79]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], Independent Reds[22], Nuclear Subs[44], Summit[48], Kitchen Debates[51], Ussuri River Skirmish[77], One Small Step[81]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, West Germany, Angola | 44.85 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Angola | 44.85 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |
| 3 | Fidel INFLUENCE West Germany, Angola | 29.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |
| 4 | Arab-Israeli War INFLUENCE West Germany, Angola | 29.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |
| 5 | One Small Step INFLUENCE West Germany, Angola | 29.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Socialist Governments[7], Suez Crisis[28], Arms Race[42], Grain Sales to Soviets[68], OAS Founded[71], Voice of America[75], Alliance for Progress[79]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Chile, Angola | 56.10 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:8.00 |
| 2 | Arms Race INFLUENCE West Germany, Chile, Angola | 56.10 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:8.00 |
| 3 | Alliance for Progress INFLUENCE West Germany, Chile, Angola | 56.10 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:8.00 |
| 4 | Grain Sales to Soviets INFLUENCE West Germany, Angola | 39.45 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:8.00 |
| 5 | Voice of America INFLUENCE West Germany, Angola | 39.45 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], Independent Reds[22], Nuclear Subs[44], Kitchen Debates[51], Ussuri River Skirmish[77], One Small Step[81]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Angola | 43.52 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:9.33 |
| 2 | Fidel INFLUENCE West Germany, Angola | 28.12 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:9.33 |
| 3 | Arab-Israeli War INFLUENCE West Germany, Angola | 28.12 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:9.33 |
| 4 | One Small Step INFLUENCE West Germany, Angola | 28.12 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:9.33 |
| 5 | Ussuri River Skirmish COUP Cameroon | 26.23 | 4.00 | 22.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Suez Crisis[28], Arms Race[42], Grain Sales to Soviets[68], OAS Founded[71], Voice of America[75], Alliance for Progress[79]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE West Germany, Chile, Angola | 54.77 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:9.33 |
| 2 | Alliance for Progress INFLUENCE West Germany, Chile, Angola | 54.77 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:9.33 |
| 3 | Grain Sales to Soviets INFLUENCE West Germany, Angola | 38.12 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:9.33 |
| 4 | Voice of America INFLUENCE West Germany, Angola | 38.12 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:9.33 |
| 5 | Socialist Governments INFLUENCE West Germany, Chile, Angola | 34.77 | 6.00 | 58.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], Independent Reds[22], Nuclear Subs[44], Kitchen Debates[51], One Small Step[81]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Angola | 26.25 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:11.20 |
| 2 | Arab-Israeli War INFLUENCE West Germany, Angola | 26.25 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:11.20 |
| 3 | One Small Step INFLUENCE West Germany, Angola | 26.25 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:11.20 |
| 4 | Fidel COUP Cameroon | 20.35 | 4.00 | 16.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 5 | Fidel COUP Saharan States | 20.35 | 4.00 | 16.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Suez Crisis[28], Grain Sales to Soviets[68], OAS Founded[71], Voice of America[75], Alliance for Progress[79]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE West Germany, Chile, Angola | 52.90 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:11.20 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany, Angola | 36.25 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:11.20 |
| 3 | Voice of America INFLUENCE West Germany, Angola | 36.25 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:11.20 |
| 4 | Socialist Governments INFLUENCE West Germany, Chile, Angola | 32.90 | 6.00 | 58.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Suez Crisis INFLUENCE West Germany, Chile, Angola | 32.90 | 6.00 | 58.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Arab-Israeli War[13], Independent Reds[22], Nuclear Subs[44], Kitchen Debates[51], One Small Step[81]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, Angola | 23.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:14.00 |
| 2 | One Small Step INFLUENCE West Germany, Angola | 23.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:14.00 |
| 3 | Arab-Israeli War COUP Cameroon | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Saharan States | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Arab-Israeli War COUP SE African States | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Suez Crisis[28], Grain Sales to Soviets[68], OAS Founded[71], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE West Germany, Angola | 33.45 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:14.00 |
| 2 | Voice of America INFLUENCE West Germany, Angola | 33.45 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, control_break:Angola, non_coup_milops_penalty:14.00 |
| 3 | Socialist Governments INFLUENCE West Germany, Chile, Angola | 30.10 | 6.00 | 58.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Suez Crisis INFLUENCE West Germany, Chile, Angola | 30.10 | 6.00 | 58.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:Angola:15.60, control_break:Angola, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Grain Sales to Soviets COUP Colombia | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Independent Reds[22], Nuclear Subs[44], Kitchen Debates[51], One Small Step[81]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Cameroon | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP SE African States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Sudan | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Guatemala | 20.97 | 4.00 | 17.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 102: T7 AR5 US

- chosen: `Voice of America [75] as COUP`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Suez Crisis[28], OAS Founded[71], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Colombia | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Voice of America COUP Saharan States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Voice of America COUP SE African States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Voice of America COUP Sudan | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Voice of America COUP Zimbabwe | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 103: T7 AR6 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Independent Reds[22], Nuclear Subs[44], Kitchen Debates[51]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Cameroon | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Independent Reds COUP Saharan States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Independent Reds COUP SE African States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Independent Reds COUP Sudan | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nuclear Subs COUP Cameroon | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Suez Crisis[28], OAS Founded[71]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Colombia | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | OAS Founded COUP Saharan States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | OAS Founded COUP SE African States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP Sudan | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP Zimbabwe | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Nuclear Subs[44], Kitchen Debates[51]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Cameroon | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Nuclear Subs COUP SE African States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nuclear Subs COUP Sudan | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nuclear Subs COUP Guatemala | 10.30 | 4.00 | 22.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Socialist Governments [7] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Suez Crisis[28]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Colombia | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Socialist Governments COUP Saharan States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Socialist Governments COUP SE African States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Socialist Governments COUP Sudan | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Socialist Governments COUP Zimbabwe | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 107: T8 AR0 USSR

- chosen: `Wargames [103] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Socialist Governments[7], Allende[57], Willy Brandt[58], U2 Incident[63], Grain Sales to Soviets[68], Liberation Theology[76], Wargames[103], Solidarity[104]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], Cuban Missile Crisis[43], SALT Negotiations[46], North Sea Oil[89], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Vietnam Revolts EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Socialist Governments[7], Allende[57], U2 Incident[63], Grain Sales to Soviets[68], Liberation Theology[76], Solidarity[104]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Socialist Governments COUP Angola | 43.69 | 4.00 | 40.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:4.5 |
| 4 | U2 Incident COUP Angola | 43.69 | 4.00 | 40.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:4.5 |
| 5 | Liberation Theology COUP Angola | 37.34 | 4.00 | 33.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], Cuban Missile Crisis[43], SALT Negotiations[46], North Sea Oil[89], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Morocco | 51.41 | 6.00 | 55.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:9.14 |
| 2 | SALT Negotiations INFLUENCE East Germany, West Germany, Morocco | 51.41 | 6.00 | 55.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:9.14 |
| 3 | North Sea Oil INFLUENCE East Germany, West Germany, Morocco | 51.41 | 6.00 | 55.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:9.14 |
| 4 | Cuban Missile Crisis COUP Angola | 43.69 | 4.00 | 40.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:4.5 |
| 5 | SALT Negotiations COUP Angola | 43.69 | 4.00 | 40.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Allende[57], U2 Incident[63], Grain Sales to Soviets[68], Liberation Theology[76], Solidarity[104]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 44.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | U2 Incident COUP Angola | 44.07 | 4.00 | 40.52 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:4.5 |
| 3 | Liberation Theology COUP Angola | 37.72 | 4.00 | 34.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:3.5 |
| 4 | U2 Incident COUP Algeria | 33.67 | 4.00 | 30.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |
| 5 | U2 Incident COUP Mexico | 32.92 | 4.00 | 29.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], SALT Negotiations[46], North Sea Oil[89], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 49.38 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 2 | North Sea Oil INFLUENCE East Germany, France, West Germany | 49.38 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 3 | SALT Negotiations COUP Angola | 44.07 | 4.00 | 40.52 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:4.5 |
| 4 | North Sea Oil COUP Angola | 44.07 | 4.00 | 40.52 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:4.5 |
| 5 | SALT Negotiations COUP Congo/Zaire | 38.67 | 4.00 | 35.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Liberation Theology [76] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Allende[57], Grain Sales to Soviets[68], Liberation Theology[76], Solidarity[104]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Angola | 38.25 | 4.00 | 34.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:3.5 |
| 2 | Allende COUP Angola | 31.90 | 4.00 | 28.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:2.5 |
| 3 | Liberation Theology COUP Algeria | 27.85 | 4.00 | 24.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:1.5 |
| 4 | Liberation Theology COUP Mexico | 27.10 | 4.00 | 23.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:1.5 |
| 5 | Liberation Theology COUP Egypt | 26.60 | 4.00 | 22.90 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 114: T8 AR3 US

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], North Sea Oil[89], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 42.25 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | North Sea Oil COUP Saharan States | 27.10 | 4.00 | 23.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:4.5 |
| 3 | North Sea Oil COUP SE African States | 27.10 | 4.00 | 23.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:4.5 |
| 4 | North Sea Oil COUP Sudan | 27.10 | 4.00 | 23.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:4.5 |
| 5 | North Sea Oil COUP Zimbabwe | 27.10 | 4.00 | 23.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Duck and Cover[4], Allende[57], Grain Sales to Soviets[68], Solidarity[104]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 23.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Allende COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende COUP SE African States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Korean War INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Vietnam Revolts COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Allende[57], Grain Sales to Soviets[68], Solidarity[104]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Allende COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende COUP Sudan | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Guatemala | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Saharan States | 6.88 | 4.00 | 19.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Korean War COUP SE African States | 6.88 | 4.00 | 19.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Korean War COUP Sudan | 6.88 | 4.00 | 19.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Korean War COUP Zimbabwe | 6.88 | 4.00 | 19.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Latin American Debt Crisis COUP Saharan States | 6.88 | 4.00 | 19.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 119: T8 AR6 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Grain Sales to Soviets[68], Solidarity[104]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Solidarity COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Latin American Debt Crisis [98] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Debt Crisis COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Saharan States | 25.20 | 4.00 | 33.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Latin American Debt Crisis COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Latin American Debt Crisis COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Solidarity [104] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Solidarity[104]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity COUP Saharan States | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Solidarity COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Solidarity COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Solidarity COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Solidarity COUP Guatemala | 12.80 | 4.00 | 25.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Zimbabwe | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP Colombia | 13.05 | 4.00 | 25.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 123: T9 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Red Scare/Purge[31], UN Intervention[32], NORAD[38], Ask Not What Your Country Can Do For You[78], One Small Step[81], Ortega Elected in Nicaragua[94], Aldrich Ames Remix[101], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Aldrich Ames Remix EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Ortega Elected in Nicaragua EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:9`
- hand: `East European Unrest[29], Red Scare/Purge[31], NORAD[38], Quagmire[45], One Small Step[81], Reagan Bombs Libya[87], Tear Down this Wall[99], Defectors[108]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Tear Down this Wall EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Aldrich Ames Remix [101] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], NORAD[38], Ask Not What Your Country Can Do For You[78], One Small Step[81], Ortega Elected in Nicaragua[94], Aldrich Ames Remix[101], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Aldrich Ames Remix COUP Saharan States | 46.47 | 4.00 | 42.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Aldrich Ames Remix COUP Angola | 43.97 | 4.00 | 40.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:4.5 |
| 3 | One Small Step COUP Saharan States | 40.12 | 4.00 | 36.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Ortega Elected in Nicaragua COUP Saharan States | 40.12 | 4.00 | 36.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 5 | One Small Step COUP Angola | 37.62 | 4.00 | 33.92 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 126: T9 AR1 US

- chosen: `East European Unrest [29] as COUP`
- flags: `milops_shortfall:9`
- hand: `East European Unrest[29], NORAD[38], Quagmire[45], One Small Step[81], Reagan Bombs Libya[87], Tear Down this Wall[99], Defectors[108]`
- state: `VP 2, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Angola | 43.97 | 4.00 | 40.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:4.5 |
| 2 | NORAD COUP Angola | 43.97 | 4.00 | 40.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:4.5 |
| 3 | Tear Down this Wall COUP Angola | 43.97 | 4.00 | 40.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:4.5 |
| 4 | East European Unrest COUP Congo/Zaire | 38.57 | 4.00 | 35.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | NORAD COUP Congo/Zaire | 38.57 | 4.00 | 35.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 127: T9 AR2 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], NORAD[38], Ask Not What Your Country Can Do For You[78], One Small Step[81], Ortega Elected in Nicaragua[94], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Cameroon | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP SE African States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Sudan | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Ortega Elected in Nicaragua COUP Cameroon | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `NORAD[38], Quagmire[45], One Small Step[81], Reagan Bombs Libya[87], Tear Down this Wall[99], Defectors[108]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, West Germany | 30.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Tear Down this Wall INFLUENCE East Germany, West Germany | 30.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | NORAD COUP Saharan States | 25.90 | 4.00 | 22.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |
| 4 | NORAD COUP SE African States | 25.90 | 4.00 | 22.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |
| 5 | NORAD COUP Sudan | 25.90 | 4.00 | 22.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Ortega Elected in Nicaragua [94] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], NORAD[38], Ask Not What Your Country Can Do For You[78], Ortega Elected in Nicaragua[94], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ortega Elected in Nicaragua COUP Cameroon | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 2 | Ortega Elected in Nicaragua COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 3 | Ortega Elected in Nicaragua COUP SE African States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 4 | Ortega Elected in Nicaragua COUP Sudan | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 5 | Ortega Elected in Nicaragua COUP Guatemala | 19.20 | 4.00 | 15.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Tear Down this Wall [99] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Quagmire[45], One Small Step[81], Reagan Bombs Libya[87], Tear Down this Wall[99], Defectors[108]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall INFLUENCE East Germany, West Germany | 29.15 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Tear Down this Wall COUP Saharan States | 26.30 | 4.00 | 22.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:4.5 |
| 3 | Tear Down this Wall COUP SE African States | 26.30 | 4.00 | 22.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:4.5 |
| 4 | Tear Down this Wall COUP Sudan | 26.30 | 4.00 | 22.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:4.5 |
| 5 | Tear Down this Wall COUP Zimbabwe | 26.30 | 4.00 | 22.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], NORAD[38], Ask Not What Your Country Can Do For You[78], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP SE African States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:6`
- hand: `Quagmire[45], One Small Step[81], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | One Small Step COUP SE African States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP Sudan | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Zimbabwe | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Reagan Bombs Libya COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], NORAD[38], Ask Not What Your Country Can Do For You[78], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | NORAD COUP Saharan States | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Saharan States | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | UN Intervention COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Reagan Bombs Libya [87] as COUP`
- flags: `milops_shortfall:6`
- hand: `Quagmire[45], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Reagan Bombs Libya COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Reagan Bombs Libya COUP Sudan | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Reagan Bombs Libya COUP Zimbabwe | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Defectors COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `NORAD[38], Ask Not What Your Country Can Do For You[78], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Ask Not What Your Country Can Do For You COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Saharan States | 25.20 | 4.00 | 33.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | NORAD COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | NORAD COUP SE African States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Defectors [108] as COUP`
- flags: `milops_shortfall:6`
- hand: `Quagmire[45], Defectors[108]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Defectors COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Defectors COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Defectors COUP Sudan | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Defectors COUP Zimbabwe | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Defectors COUP Colombia | 23.05 | 4.00 | 19.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Ask Not What Your Country Can Do For You[78], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You COUP Saharan States | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Panama Canal Returned COUP Saharan States | 31.20 | 4.00 | 39.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Quagmire [45] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Quagmire[45]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Saharan States | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Quagmire COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP Zimbabwe | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Colombia | 15.40 | 4.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 139: T10 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Suez Crisis[28], Junta[50], OPEC[64], Latin American Death Squads[70], Liberation Theology[76], Iran-Contra Scandal[96], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Ussuri River Skirmish [77] as EVENT`
- flags: `milops_shortfall:10`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], Independent Reds[22], The Cambridge Five[36], Brush War[39], South African Unrest[56], U2 Incident[63], Ussuri River Skirmish[77], Star Wars[88]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Star Wars EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `OPEC [64] as COUP`
- flags: `milops_shortfall:10`
- hand: `Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Junta[50], OPEC[64], Latin American Death Squads[70], Liberation Theology[76], Iran-Contra Scandal[96], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Colombia | 46.26 | 4.00 | 42.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | OPEC COUP Angola | 44.26 | 4.00 | 40.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:10, milops_urgency:1.43, defcon_penalty:3, expected_swing:4.5 |
| 3 | OPEC INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | Indo-Pakistani War COUP Colombia | 39.91 | 4.00 | 36.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Junta COUP Colombia | 39.91 | 4.00 | 36.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], Independent Reds[22], The Cambridge Five[36], Brush War[39], South African Unrest[56], U2 Incident[63], Star Wars[88]`
- state: `VP 2, DEFCON 3, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Saharan States | 40.41 | 4.00 | 36.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 2 | Star Wars COUP Saharan States | 40.41 | 4.00 | 36.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 3 | Independent Reds COUP Angola | 37.91 | 4.00 | 34.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:10, milops_urgency:1.43, defcon_penalty:3, expected_swing:3.5 |
| 4 | Star Wars COUP Angola | 37.91 | 4.00 | 34.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:10, milops_urgency:1.43, defcon_penalty:3, expected_swing:3.5 |
| 5 | Truman Doctrine COUP Saharan States | 34.06 | 4.00 | 30.21 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 143: T10 AR2 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:7`
- hand: `Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Junta[50], Latin American Death Squads[70], Liberation Theology[76], Iran-Contra Scandal[96], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Saharan States | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Saharan States | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Saharan States | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 4 | Liberation Theology COUP Saharan States | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 5 | Iran-Contra Scandal COUP Saharan States | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Star Wars [88] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], The Cambridge Five[36], Brush War[39], South African Unrest[56], U2 Incident[63], Star Wars[88]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars COUP Nigeria | 42.72 | 4.00 | 39.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Star Wars COUP Angola | 37.72 | 4.00 | 34.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:3.5 |
| 3 | Truman Doctrine COUP Nigeria | 36.37 | 4.00 | 32.52 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Star Wars COUP Congo/Zaire | 32.32 | 4.00 | 28.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Truman Doctrine COUP Angola | 31.37 | 4.00 | 27.52 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:7`
- hand: `US/Japan Mutual Defense Pact[27], Junta[50], Latin American Death Squads[70], Liberation Theology[76], Iran-Contra Scandal[96], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Saharan States | 40.35 | 4.00 | 36.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 40.35 | 4.00 | 36.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 3 | Liberation Theology COUP Saharan States | 40.35 | 4.00 | 36.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 4 | Iran-Contra Scandal COUP Saharan States | 40.35 | 4.00 | 36.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 5 | Junta COUP Colombia | 39.85 | 4.00 | 36.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], The Cambridge Five[36], Brush War[39], South African Unrest[56], U2 Incident[63]`
- state: `VP 2, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Cameroon | 34.40 | 4.00 | 30.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 2 | Truman Doctrine COUP Saharan States | 34.40 | 4.00 | 30.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 3 | De Gaulle Leads France COUP Cameroon | 27.10 | 4.00 | 43.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | De Gaulle Leads France COUP Saharan States | 27.10 | 4.00 | 43.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Brush War COUP Cameroon | 27.10 | 4.00 | 43.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:7`
- hand: `US/Japan Mutual Defense Pact[27], Latin American Death Squads[70], Liberation Theology[76], Iran-Contra Scandal[96], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Colombia | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 2 | Liberation Theology COUP Colombia | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 3 | Iran-Contra Scandal COUP Colombia | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 4 | Lone Gunman COUP Colombia | 34.20 | 4.00 | 30.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Chile | 33.20 | 6.00 | 65.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `De Gaulle Leads France[17], The Cambridge Five[36], Brush War[39], South African Unrest[56], U2 Incident[63]`
- state: `VP 2, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Cameroon | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | De Gaulle Leads France COUP Saharan States | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Brush War COUP Cameroon | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Brush War COUP Saharan States | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | U2 Incident COUP Cameroon | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 149: T10 AR5 USSR

- chosen: `Liberation Theology [76] as COUP`
- flags: `milops_shortfall:7`
- hand: `US/Japan Mutual Defense Pact[27], Liberation Theology[76], Iran-Contra Scandal[96], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Colombia | 41.72 | 4.00 | 38.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5 |
| 2 | Iran-Contra Scandal COUP Colombia | 41.72 | 4.00 | 38.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5 |
| 3 | Lone Gunman COUP Colombia | 35.37 | 4.00 | 31.52 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5 |
| 4 | US/Japan Mutual Defense Pact COUP Colombia | 30.42 | 4.00 | 51.02 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 5 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Chile | 28.53 | 6.00 | 65.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Brush War [39] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `The Cambridge Five[36], Brush War[39], South African Unrest[56], U2 Incident[63]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Cameroon | 28.57 | 4.00 | 45.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Brush War COUP Saharan States | 28.57 | 4.00 | 45.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | U2 Incident COUP Cameroon | 28.57 | 4.00 | 45.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | U2 Incident COUP Saharan States | 28.57 | 4.00 | 45.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Cameroon | 26.22 | 4.00 | 38.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Iran-Contra Scandal [96] as COUP`
- flags: `milops_shortfall:7`
- hand: `US/Japan Mutual Defense Pact[27], Iran-Contra Scandal[96], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Contra Scandal COUP Colombia | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5 |
| 2 | Lone Gunman COUP Colombia | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5 |
| 3 | US/Japan Mutual Defense Pact COUP Colombia | 32.75 | 4.00 | 53.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 4 | Iran-Contra Scandal COUP Cameroon | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Iran-Contra Scandal COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `U2 Incident [63] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `The Cambridge Five[36], South African Unrest[56], U2 Incident[63]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident COUP Cameroon | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | U2 Incident COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `milops_shortfall:7`
- hand: `US/Japan Mutual Defense Pact[27], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Colombia | 44.70 | 4.00 | 40.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5 |
| 2 | US/Japan Mutual Defense Pact COUP Colombia | 39.75 | 4.00 | 60.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Cameroon | 25.20 | 4.00 | 21.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman COUP Saharan States | 25.20 | 4.00 | 21.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP SE African States | 25.20 | 4.00 | 21.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `The Cambridge Five[36], South African Unrest[56]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | South African Unrest COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Peru | 24.65 | 4.00 | 36.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP -9, DEFCON +1, MilOps U-3/A-3`
