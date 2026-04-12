# minimal_hybrid detailed rollout log

- seed: `20260522`
- winner: `US`
- final_vp: `-6`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Nasser[15], Captured Nazi Scientist[18], NATO[21], Marshall Plan[23], CIA Created[26]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Fidel[8], Romanian Abdication[12], Indo-Pakistani War[24], De-Stalinization[33], Nuclear Test Ban[34], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `COMECON [14] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Blockade[10], COMECON[14], Nasser[15], Captured Nazi Scientist[18], NATO[21], Marshall Plan[23], CIA Created[26]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Iran | 76.83 | 4.00 | 73.28 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Blockade COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Nasser COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | COMECON INFLUENCE West Germany, Japan, Thailand | 62.47 | 6.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Fidel[8], Romanian Abdication[12], Indo-Pakistani War[24], De-Stalinization[33], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE North Korea, Indonesia, Philippines | 62.07 | 6.00 | 57.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Indo-Pakistani War INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Formosan Resolution INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 4 | Special Relationship INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 5 | De-Stalinization INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Captured Nazi Scientist[18], NATO[21], Marshall Plan[23], CIA Created[26]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, Japan, North Korea, Thailand | 60.20 | 6.00 | 78.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, North Korea, Thailand | 60.20 | 6.00 | 78.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Blockade COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Nasser COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], Indo-Pakistani War[24], De-Stalinization[33], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 41.80 | 6.00 | 37.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:1.60 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 41.80 | 6.00 | 37.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:1.60 |
| 3 | Special Relationship INFLUENCE East Germany, West Germany | 41.80 | 6.00 | 37.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:1.60 |
| 4 | De-Stalinization INFLUENCE East Germany, France, West Germany | 38.70 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Indo-Pakistani War COUP Syria | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Captured Nazi Scientist[18], Marshall Plan[23], CIA Created[26]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, Pakistan, South Korea, Thailand | 61.40 | 6.00 | 80.00 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Blockade COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Nasser COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Marshall Plan COUP Iran | 34.85 | 4.00 | 55.45 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], De-Stalinization[33], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE France, Panama | 36.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.00 |
| 2 | Special Relationship INFLUENCE France, Panama | 36.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.00 |
| 3 | De-Stalinization INFLUENCE France, Japan, Panama | 32.95 | 6.00 | 49.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Formosan Resolution COUP Syria | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 5 | Special Relationship COUP Syria | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china`
- hand: `Blockade[10], Nasser[15], Captured Nazi Scientist[18], CIA Created[26]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 2 | Nasser COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | CIA Created COUP Iran | 30.80 | 4.00 | 38.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | Blockade COUP Philippines | 30.55 | 4.00 | 26.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], De-Stalinization[33], Special Relationship[37]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Italy, Japan | 35.63 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, non_coup_milops_penalty:2.67 |
| 2 | De-Stalinization INFLUENCE Italy, Japan, Egypt | 31.18 | 6.00 | 48.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Special Relationship COUP Syria | 28.32 | 4.00 | 24.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 4 | Fidel INFLUENCE Italy, Japan | 19.63 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Special Relationship COUP Lebanon | 16.72 | 4.00 | 13.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], Captured Nazi Scientist[18], CIA Created[26]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12], De-Stalinization[33]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, Japan, Egypt | 29.85 | 6.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Fidel INFLUENCE Italy, Japan | 18.30 | 6.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | De-Stalinization COUP Syria | 14.00 | 4.00 | 30.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Fidel COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Syria | 11.30 | 4.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china`
- hand: `Captured Nazi Scientist[18], CIA Created[26]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist REALIGN Israel | 3.04 | -1.00 | 4.20 | 0.00 | 0.00 | -0.15 | 0.00 |  |
| 5 | Captured Nazi Scientist EVENT | 2.35 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Syria | 13.65 | 4.00 | 25.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Fidel INFLUENCE Japan, Egypt | 13.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | Romanian Abdication COUP Syria | 12.30 | 4.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Fidel COUP Lebanon | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Romanian Abdication INFLUENCE Egypt | 1.55 | 6.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +1, DEFCON +1, MilOps U-3/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Independent Reds[22], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Korean War[11], Truman Doctrine[19], Olympic Games[20], Containment[25], US/Japan Mutual Defense Pact[27], Suez Crisis[28], NORAD[38]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], Independent Reds[22], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE India, Pakistan, Thailand | 60.83 | 6.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | De Gaulle Leads France COUP Philippines | 43.92 | 4.00 | 40.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 3 | Vietnam Revolts INFLUENCE Pakistan, Thailand | 43.43 | 6.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Arab-Israeli War INFLUENCE Pakistan, Thailand | 43.43 | 6.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 5 | Decolonization INFLUENCE Pakistan, Thailand | 43.43 | 6.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Korean War[11], Truman Doctrine[19], Olympic Games[20], Containment[25], Suez Crisis[28], NORAD[38]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, Egypt, Iraq | 54.93 | 6.00 | 52.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 2 | Containment INFLUENCE East Germany, Egypt, Iraq | 54.93 | 6.00 | 52.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 3 | NORAD INFLUENCE East Germany, Egypt, Iraq | 54.93 | 6.00 | 52.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 4 | Olympic Games INFLUENCE East Germany, Egypt | 38.78 | 6.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:2.67 |
| 5 | Suez Crisis INFLUENCE East Germany, Egypt, Iraq | 34.93 | 6.00 | 52.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Independent Reds[22], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Iraq, Thailand | 42.25 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Arab-Israeli War INFLUENCE Iraq, Thailand | 42.25 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | Decolonization INFLUENCE Iraq, Thailand | 42.25 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 4 | Vietnam Revolts COUP Philippines | 38.70 | 4.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | Arab-Israeli War COUP Philippines | 38.70 | 4.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Truman Doctrine[19], Olympic Games[20], Containment[25], Suez Crisis[28], NORAD[38]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Iran, Saudi Arabia | 50.50 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.20 |
| 2 | NORAD INFLUENCE Japan, Iran, Saudi Arabia | 50.50 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.20 |
| 3 | Containment COUP Iran | 43.30 | 4.00 | 39.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 4 | NORAD COUP Iran | 43.30 | 4.00 | 39.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games COUP Iran | 37.95 | 4.00 | 34.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Arab-Israeli War[13], Independent Reds[22], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Philippines | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 2 | Decolonization COUP Philippines | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 3 | Arab-Israeli War INFLUENCE Italy, Thailand | 38.60 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Decolonization INFLUENCE Italy, Thailand | 38.60 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | East European Unrest INFLUENCE Italy, Philippines, Thailand | 34.90 | 6.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 22: T2 AR3 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Truman Doctrine[19], Olympic Games[20], Suez Crisis[28], NORAD[38]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Pakistan, Philippines | 51.10 | 6.00 | 49.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:4.00 |
| 2 | Olympic Games INFLUENCE Pakistan, Philippines | 35.10 | 6.00 | 33.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:4.00 |
| 3 | Suez Crisis INFLUENCE Japan, Pakistan, Philippines | 31.10 | 6.00 | 49.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Philippines:14.45, access_touch:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | NORAD COUP Iran | 30.50 | 4.00 | 26.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:2.5 |
| 5 | Olympic Games COUP Iran | 25.15 | 4.00 | 21.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china`
- hand: `Independent Reds[22], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Pakistan, Thailand | 46.10 | 6.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45 |
| 2 | East European Unrest INFLUENCE Pakistan, Philippines, Thailand | 45.40 | 6.00 | 59.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Philippines:14.45, control_break:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Independent Reds INFLUENCE Pakistan, Thailand | 30.10 | 6.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Decolonization COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Truman Doctrine[19], Olympic Games[20], Suez Crisis[28]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE India, Japan | 34.07 | 6.00 | 33.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, non_coup_milops_penalty:5.33 |
| 2 | Suez Crisis INFLUENCE India, Japan, Libya | 29.62 | 6.00 | 49.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Olympic Games COUP Iran | 25.48 | 4.00 | 21.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 4 | Truman Doctrine COUP Iran | 19.13 | 4.00 | 15.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 5 | Olympic Games COUP Lebanon | 18.38 | 4.00 | 14.68 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], East European Unrest[29], UN Intervention[32]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Italy, Philippines, Thailand | 41.90 | 6.00 | 56.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, control_break:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Independent Reds INFLUENCE Philippines, Thailand | 29.60 | 6.00 | 39.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, control_break:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 3 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | East European Unrest COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Korean War[11], Truman Doctrine[19], Suez Crisis[28]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Italy, Japan, Libya | 22.85 | 6.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Truman Doctrine COUP Iran | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Iraq | 17.65 | 4.00 | 13.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |
| 4 | Truman Doctrine COUP Lebanon | 12.70 | 4.00 | 8.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Suez Crisis COUP Iran | 11.50 | 4.00 | 27.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], UN Intervention[32]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Saudi Arabia, Thailand | 26.45 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Independent Reds COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Truman Doctrine[19]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Iran | 21.80 | 4.00 | 17.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | Truman Doctrine COUP Iraq | 19.65 | 4.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3 |
| 3 | Truman Doctrine COUP Saudi Arabia | 19.65 | 4.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3 |
| 4 | Truman Doctrine COUP Lebanon | 14.70 | 4.00 | 10.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP SE African States | 12.45 | 4.00 | 8.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +0, MilOps U-2/A+0`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], COMECON[14], Indo-Pakistani War[24], Red Scare/Purge[31], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Nasser[15], Truman Doctrine[19], Marshall Plan[23], Decolonization[30], Nuclear Test Ban[34], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], COMECON[14], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Japan, Indonesia, Thailand | 54.00 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Fidel INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Vietnam Revolts INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Indo-Pakistani War INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | The Cambridge Five INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Nasser[15], Truman Doctrine[19], Decolonization[30], Nuclear Test Ban[34], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Turkey, Libya, Indonesia | 56.40 | 6.00 | 55.00 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Libya:13.70, control_break:Libya, influence:Indonesia:13.85, control_break:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Five Year Plan INFLUENCE Libya, Indonesia | 39.10 | 6.00 | 37.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Libya:13.70, control_break:Libya, influence:Indonesia:13.85, control_break:Indonesia, non_coup_milops_penalty:4.00 |
| 3 | NORAD INFLUENCE Libya, Indonesia | 39.10 | 6.00 | 37.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Libya:13.70, control_break:Libya, influence:Indonesia:13.85, control_break:Indonesia, non_coup_milops_penalty:4.00 |
| 4 | Nuclear Test Ban COUP Iran | 36.85 | 4.00 | 33.45 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:3.5 |
| 5 | Five Year Plan COUP Iran | 31.50 | 4.00 | 27.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | Vietnam Revolts INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 3 | Indo-Pakistani War INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 4 | The Cambridge Five INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 5 | Fidel COUP Syria | 29.85 | 4.00 | 26.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Nasser[15], Truman Doctrine[19], Decolonization[30], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan | 32.55 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:4.80 |
| 2 | NORAD INFLUENCE West Germany, Japan | 32.55 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:4.80 |
| 3 | Five Year Plan COUP Iran | 31.70 | 4.00 | 28.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:2.5 |
| 4 | NORAD COUP Iran | 31.70 | 4.00 | 28.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:2.5 |
| 5 | Five Year Plan COUP Lebanon | 24.60 | 4.00 | 21.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Japan, Thailand | 36.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | Indo-Pakistani War INFLUENCE Japan, Thailand | 36.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | The Cambridge Five INFLUENCE Japan, Thailand | 36.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 4 | Vietnam Revolts COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `NORAD [38] as COUP`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Nasser[15], Truman Doctrine[19], Decolonization[30], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Iran | 32.00 | 4.00 | 28.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:2.5 |
| 2 | NORAD INFLUENCE West Germany, Japan | 31.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 3 | NORAD COUP Lebanon | 24.90 | 4.00 | 21.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:4.5 |
| 4 | NORAD COUP SE African States | 22.65 | 4.00 | 19.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:4.5 |
| 5 | NORAD COUP Sudan | 22.65 | 4.00 | 19.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 37: T3 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan, Thailand | 34.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 34.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 3 | Romanian Abdication INFLUENCE Thailand | 18.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 4 | Special Relationship INFLUENCE Japan, Thailand | 18.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Special Relationship SPACE | 0.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `Socialist Governments[7], Nasser[15], Truman Doctrine[19], Decolonization[30]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 3 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Socialist Governments SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Thailand | 21.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:21.00 |
| 2 | Romanian Abdication INFLUENCE Thailand | 5.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:21.00 |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 5.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 4 | Special Relationship SPACE | -12.30 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 5 | Romanian Abdication REALIGN Cuba | -17.66 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Socialist Governments[7], Nasser[15], Decolonization[30]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Socialist Governments SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Decolonization INFLUENCE Japan | 5.85 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Special Relationship[37]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | -6.70 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:33.00 |
| 2 | Special Relationship INFLUENCE Japan, Thailand | -6.70 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:33.00 |
| 3 | Special Relationship SPACE | -24.30 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:33.00 |
| 4 | Romanian Abdication REALIGN Cuba | -29.66 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:33.00 |
| 5 | Romanian Abdication EVENT | -30.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:33.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Nasser [15] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Nasser[15], Decolonization[30]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Decolonization INFLUENCE Japan | 5.85 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Decolonization COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Sudan | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -2, DEFCON +1, MilOps U+0/A-3`

## Step 43: T4 AR0 USSR

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Fidel[8], Nasser[15], East European Unrest[29], SALT Negotiations[46], Missile Envy[52], Portuguese Empire Crumbles[55], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ussuri River Skirmish[77]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Independent Reds[22], Indo-Pakistani War[24], Red Scare/Purge[31], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Red Scare/Purge [31] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Fidel[8], Nasser[15], East European Unrest[29], Red Scare/Purge[31], Missile Envy[52], Portuguese Empire Crumbles[55], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ussuri River Skirmish[77]`
- state: `VP -3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge COUP Indonesia | 53.39 | 4.00 | 49.99 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:5.5 |
| 2 | Red Scare/Purge INFLUENCE UK, Mexico, Algeria | 50.13 | 6.00 | 49.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 3 | Ussuri River Skirmish COUP Indonesia | 47.04 | 4.00 | 43.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5 |
| 4 | Red Scare/Purge COUP Pakistan | 43.49 | 4.00 | 40.09 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:3.5 |
| 5 | Red Scare/Purge COUP Iran | 43.49 | 4.00 | 40.09 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+4/A+0`

## Step 46: T4 AR1 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Independent Reds[22], Indo-Pakistani War[24], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE Mexico, Algeria, South Africa | 50.93 | 6.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 2 | Independent Reds INFLUENCE Mexico, South Africa | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 3 | Indo-Pakistani War INFLUENCE Mexico, South Africa | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 4 | Nuclear Subs INFLUENCE Mexico, South Africa | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 5 | Junta INFLUENCE Mexico, South Africa | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china`
- hand: `Fidel[8], Nasser[15], East European Unrest[29], Missile Envy[52], Portuguese Empire Crumbles[55], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ussuri River Skirmish[77]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE Mexico, Algeria | 38.70 | 6.00 | 33.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria |
| 2 | Ussuri River Skirmish COUP Syria | 31.50 | 4.00 | 27.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5 |
| 3 | Fidel COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 4 | Missile Envy COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Portuguese Empire Crumbles COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Independent Reds[22], Indo-Pakistani War[24], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Morocco, South Africa | 38.97 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | Indo-Pakistani War INFLUENCE Morocco, South Africa | 38.97 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 3 | Nuclear Subs INFLUENCE Morocco, South Africa | 38.97 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 4 | Junta INFLUENCE Morocco, South Africa | 38.97 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 5 | John Paul II Elected Pope INFLUENCE Morocco, South Africa | 38.97 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china`
- hand: `Fidel[8], Nasser[15], East European Unrest[29], Missile Envy[52], Portuguese Empire Crumbles[55], Nixon Plays the China Card[72], Shuttle Diplomacy[74]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 2 | Missile Envy COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 3 | Portuguese Empire Crumbles COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 4 | Nasser INFLUENCE Morocco | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Morocco:14.80, access_touch:Morocco |
| 5 | Fidel INFLUENCE Morocco | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Indo-Pakistani War[24], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 32.25 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 2 | Nuclear Subs INFLUENCE West Germany, South Africa | 32.25 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 3 | Junta INFLUENCE West Germany, South Africa | 32.25 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 4 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 32.25 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 5 | Our Man in Tehran INFLUENCE West Germany, South Africa | 32.25 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china`
- hand: `Nasser[15], East European Unrest[29], Missile Envy[52], Portuguese Empire Crumbles[55], Nixon Plays the China Card[72], Shuttle Diplomacy[74]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 2 | Portuguese Empire Crumbles COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 3 | Nasser INFLUENCE Morocco | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Morocco:14.80, access_touch:Morocco |
| 4 | Missile Envy INFLUENCE Morocco | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco |
| 5 | Portuguese Empire Crumbles INFLUENCE Morocco | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Junta INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | Our Man in Tehran INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Nuclear Subs COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `holds_china`
- hand: `Nasser[15], East European Unrest[29], Portuguese Empire Crumbles[55], Nixon Plays the China Card[72], Shuttle Diplomacy[74]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 2 | Nasser INFLUENCE Morocco | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Morocco:14.80, access_touch:Morocco |
| 3 | Portuguese Empire Crumbles INFLUENCE Morocco | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco |
| 4 | Nasser COUP Syria | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | East European Unrest INFLUENCE UK, Morocco | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Junta[50], John Paul II Elected Pope[69], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Mexico | 28.07 | 4.00 | 24.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 2 | John Paul II Elected Pope COUP Mexico | 28.07 | 4.00 | 24.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 3 | Our Man in Tehran COUP Mexico | 28.07 | 4.00 | 24.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 4 | Junta INFLUENCE West Germany, South Africa | 27.98 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.67 |
| 5 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 27.98 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 55: T4 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], East European Unrest[29], Nixon Plays the China Card[72], Shuttle Diplomacy[74]`
- state: `VP -3, DEFCON 2, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Mexico | 22.80 | 6.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Mexico:14.95, access_touch:Mexico |
| 2 | East European Unrest INFLUENCE Mexico, Morocco | 19.30 | 6.00 | 33.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty |
| 3 | Shuttle Diplomacy INFLUENCE Mexico, Morocco | 19.30 | 6.00 | 33.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty |
| 4 | Nasser COUP Saharan States | 10.20 | 4.00 | 6.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nixon Plays the China Card SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], John Paul II Elected Pope[69], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 2, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 24.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 2 | Our Man in Tehran INFLUENCE West Germany, South Africa | 24.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 3 | John Paul II Elected Pope COUP Colombia | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | John Paul II Elected Pope COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | John Paul II Elected Pope COUP SE African States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `East European Unrest[29], Nixon Plays the China Card[72], Shuttle Diplomacy[74]`
- state: `VP -3, DEFCON 2, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE UK, Morocco | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty |
| 2 | Shuttle Diplomacy INFLUENCE UK, Morocco | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty |
| 3 | Nixon Plays the China Card SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | East European Unrest SPACE | 7.55 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Shuttle Diplomacy SPACE | 7.55 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 2, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Colombia | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Our Man in Tehran COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Our Man in Tehran COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Our Man in Tehran COUP Sudan | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Our Man in Tehran COUP Zimbabwe | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +1, MilOps U-4/A-2`

## Step 59: T5 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Socialist Governments[7], Olympic Games[20], Formosan Resolution[35], Special Relationship[37], Quagmire[45], South African Unrest[56], Willy Brandt[58], ABM Treaty[60], Liberation Theology[76]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], NORAD[38], Brush War[39], Summit[48], Allende[57], Camp David Accords[66]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Socialist Governments[7], Olympic Games[20], Formosan Resolution[35], Special Relationship[37], Quagmire[45], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | 47.09 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 2 | Quagmire INFLUENCE East Germany, France, West Germany | 47.09 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 3 | Socialist Governments COUP Libya | 44.43 | 4.00 | 40.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 4 | Quagmire COUP Libya | 44.43 | 4.00 | 40.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 5 | Socialist Governments COUP Mexico | 39.18 | 4.00 | 35.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Summit [48] as COUP`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], Brush War[39], Summit[48], Allende[57], Camp David Accords[66]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Indonesia | 54.33 | 4.00 | 50.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 2 | Summit INFLUENCE Brazil, Venezuela, South Africa | 49.04 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Indo-Pakistani War COUP Indonesia | 47.98 | 4.00 | 44.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 4 | Camp David Accords COUP Indonesia | 47.98 | 4.00 | 44.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 5 | UN Intervention COUP Indonesia | 41.63 | 4.00 | 37.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 63: T5 AR2 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Olympic Games[20], Formosan Resolution[35], Special Relationship[37], Quagmire[45], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP -2, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, France, West Germany | 46.13 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 2 | Quagmire COUP Libya | 38.67 | 4.00 | 35.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Quagmire COUP Mexico | 33.42 | 4.00 | 29.87 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:2.5 |
| 4 | Quagmire COUP Algeria | 32.67 | 4.00 | 29.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:2.5 |
| 5 | Olympic Games COUP Libya | 32.32 | 4.00 | 28.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], Brush War[39], Allende[57], Camp David Accords[66]`
- state: `VP -2, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Brazil, South Africa | 36.03 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:2.67 |
| 2 | Camp David Accords INFLUENCE Brazil, South Africa | 36.03 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:2.67 |
| 3 | Brush War INFLUENCE Brazil, Venezuela, South Africa | 32.08 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Fidel INFLUENCE Brazil, South Africa | 20.03 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | The Cambridge Five INFLUENCE Brazil, South Africa | 20.03 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Olympic Games[20], Formosan Resolution[35], Special Relationship[37], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP -2, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | South African Unrest COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Willy Brandt COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Liberation Theology COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Olympic Games INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 66: T5 AR3 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], UN Intervention[32], The Cambridge Five[36], Brush War[39], Allende[57], Camp David Accords[66]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE Mexico, Brazil | 41.65 | 6.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:3.20 |
| 2 | Brush War INFLUENCE Mexico, Argentina, Brazil | 39.70 | 6.00 | 57.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Fidel INFLUENCE Mexico, Brazil | 25.65 | 6.00 | 39.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Brazil:14.20, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | The Cambridge Five INFLUENCE Mexico, Brazil | 25.65 | 6.00 | 39.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Brazil:14.20, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | UN Intervention INFLUENCE Mexico | 22.60 | 6.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Formosan Resolution[35], Special Relationship[37], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 31.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Willy Brandt INFLUENCE East Germany, West Germany | 31.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 31.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | South African Unrest COUP Saharan States | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Willy Brandt COUP Saharan States | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], UN Intervention[32], The Cambridge Five[36], Brush War[39], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE Argentina, Algeria, South Africa | 35.75 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Fidel INFLUENCE Argentina, Algeria | 23.10 | 6.00 | 37.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | The Cambridge Five INFLUENCE Argentina, Algeria | 23.10 | 6.00 | 37.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | UN Intervention INFLUENCE Algeria | 21.05 | 6.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.00 |
| 5 | UN Intervention COUP Colombia | 12.20 | 4.00 | 8.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Formosan Resolution[35], Special Relationship[37], Willy Brandt[58], Liberation Theology[76]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Willy Brandt COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Liberation Theology COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Willy Brandt COUP Guatemala | 18.30 | 4.00 | 14.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], UN Intervention[32], The Cambridge Five[36], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Argentina, Chile | 24.37 | 6.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | The Cambridge Five INFLUENCE Argentina, Chile | 24.37 | 6.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | UN Intervention INFLUENCE Argentina | 21.72 | 6.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:5.33 |
| 4 | UN Intervention COUP Colombia | 12.53 | 4.00 | 8.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 12.53 | 4.00 | 8.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Liberation Theology [76] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Formosan Resolution[35], Special Relationship[37], Liberation Theology[76]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Liberation Theology COUP Guatemala | 19.30 | 4.00 | 15.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 16.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:21.00 |
| 4 | Liberation Theology COUP Tunisia | 10.15 | 4.00 | 6.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:1.5 |
| 5 | Formosan Resolution COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:2`
- hand: `UN Intervention[32], The Cambridge Five[36], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | The Cambridge Five COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | UN Intervention COUP Colombia | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP SE African States | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Formosan Resolution[35], Special Relationship[37]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Special Relationship COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Special Relationship COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Tunisia | -2.85 | 4.00 | 9.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `The Cambridge Five[36], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Zimbabwe | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Five Year Plan[5], Korean War[11], Truman Doctrine[19], Decolonization[30], Nuclear Test Ban[34], Special Relationship[37], How I Learned to Stop Worrying[49], Kitchen Debates[51], Grain Sales to Soviets[68]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Blockade[10], Romanian Abdication[12], COMECON[14], Containment[25], Suez Crisis[28], We Will Bury You[53], One Small Step[81]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | We Will Bury You EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Five Year Plan[5], Korean War[11], Truman Doctrine[19], Decolonization[30], Special Relationship[37], How I Learned to Stop Worrying[49], Kitchen Debates[51], Grain Sales to Soviets[68]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Egypt | 38.36 | 4.00 | 34.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:1.5 |
| 2 | Decolonization COUP Egypt | 38.36 | 4.00 | 34.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:1.5 |
| 3 | How I Learned to Stop Worrying COUP Egypt | 38.36 | 4.00 | 34.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:1.5 |
| 4 | Korean War INFLUENCE West Germany, Pakistan | 33.19 | 6.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:6.86 |
| 5 | Decolonization INFLUENCE West Germany, Pakistan | 33.19 | 6.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 78: T6 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Containment[25], Suez Crisis[28], We Will Bury You[53], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Argentina, Chile, South Africa | 48.49 | 6.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | We Will Bury You INFLUENCE Argentina, Chile, Venezuela, South Africa | 40.54 | 6.00 | 66.00 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 3 | Containment COUP Egypt | 38.71 | 4.00 | 35.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Containment COUP Libya | 38.71 | 4.00 | 35.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Containment COUP Mexico | 33.46 | 4.00 | 29.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Truman Doctrine[19], Decolonization[30], Special Relationship[37], How I Learned to Stop Worrying[49], Kitchen Debates[51], Grain Sales to Soviets[68]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Pakistan, Egypt | 36.77 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Egypt:13.20, control_break:Egypt, non_coup_milops_penalty:5.33 |
| 2 | How I Learned to Stop Worrying INFLUENCE Pakistan, Egypt | 36.77 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Egypt:13.20, control_break:Egypt, non_coup_milops_penalty:5.33 |
| 3 | Five Year Plan INFLUENCE Pakistan, Egypt, Israel | 33.02 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Egypt:13.20, control_break:Egypt, influence:Israel:14.40, access_touch:Israel, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Decolonization COUP Mexico | 26.73 | 4.00 | 23.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | How I Learned to Stop Worrying COUP Mexico | 26.73 | 4.00 | 23.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Suez Crisis[28], We Will Bury You[53], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE Argentina, Chile, Venezuela, South Africa | 44.40 | 6.00 | 71.00 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | One Small Step INFLUENCE Chile, South Africa | 36.30 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | One Small Step COUP Egypt | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | One Small Step COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | COMECON INFLUENCE Argentina, Chile, South Africa | 32.35 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Truman Doctrine[19], Special Relationship[37], How I Learned to Stop Worrying[49], Kitchen Debates[51], Grain Sales to Soviets[68]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE West Germany, Israel | 31.85 | 6.00 | 32.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, non_coup_milops_penalty:6.40 |
| 2 | Five Year Plan INFLUENCE East Germany, West Germany, Israel | 27.25 | 6.00 | 48.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | How I Learned to Stop Worrying COUP Mexico | 27.00 | 4.00 | 23.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 4 | How I Learned to Stop Worrying COUP Algeria | 26.25 | 4.00 | 22.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 5 | How I Learned to Stop Worrying COUP Iran | 25.25 | 4.00 | 21.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Suez Crisis[28], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Egypt | 33.05 | 4.00 | 29.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | One Small Step COUP Libya | 33.05 | 4.00 | 29.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | One Small Step INFLUENCE Chile, Venezuela | 32.10 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:9.60 |
| 4 | COMECON INFLUENCE Chile, Venezuela, South Africa | 28.75 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Suez Crisis INFLUENCE Chile, Venezuela, South Africa | 28.75 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 83: T6 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], Special Relationship[37], Kitchen Debates[51], Grain Sales to Soviets[68]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Special Relationship INFLUENCE East Germany, West Germany | 13.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 13.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Five Year Plan COUP Saharan States | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Five Year Plan COUP Sudan | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Suez Crisis[28]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Chile, Venezuela, South Africa | 30.35 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Suez Crisis INFLUENCE Chile, Venezuela, South Africa | 30.35 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | COMECON COUP Colombia | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | COMECON COUP Saharan States | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP SE African States | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37], Kitchen Debates[51], Grain Sales to Soviets[68]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 10.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 10.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Special Relationship COUP Saharan States | 4.22 | 4.00 | 16.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Special Relationship COUP Sudan | 4.22 | 4.00 | 16.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Saharan States | 4.22 | 4.00 | 16.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Suez Crisis[28]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Argentina, Chile, South Africa | 24.68 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Suez Crisis COUP Colombia | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Suez Crisis COUP Saharan States | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Suez Crisis COUP SE African States | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Suez Crisis COUP Zimbabwe | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], Kitchen Debates[51], Grain Sales to Soviets[68]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Grain Sales to Soviets COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Guatemala | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Sudan | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 25.20 | 4.00 | 33.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Saharan States | 25.20 | 4.00 | 33.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Blockade COUP Colombia | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Blockade COUP SE African States | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Blockade COUP Zimbabwe | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], Kitchen Debates[51]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Saharan States | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Sudan | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Kitchen Debates COUP Saharan States | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Kitchen Debates COUP Sudan | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Guatemala | 5.95 | 4.00 | 14.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Saharan States | 29.20 | 4.00 | 37.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Colombia | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP SE African States | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Zimbabwe | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Guatemala | 5.95 | 4.00 | 14.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Decolonization[30], De-Stalinization[33], Muslim Revolution[59], Lonely Hearts Club Band[65], Latin American Death Squads[70], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Arms Race [42] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], CIA Created[26], Arms Race[42], Bear Trap[47], Flower Power[62], Puppet Governments[67], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Decolonization[30], De-Stalinization[33], Lonely Hearts Club Band[65], Latin American Death Squads[70], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Iran, Nigeria | 52.50 | 6.00 | 54.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iran:13.20, control_break:Iran, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 2 | De Gaulle Leads France INFLUENCE West Germany, Iran, Nigeria | 52.50 | 6.00 | 54.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iran:13.20, control_break:Iran, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 3 | De-Stalinization INFLUENCE West Germany, Iran, Nigeria | 52.50 | 6.00 | 54.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iran:13.20, control_break:Iran, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 4 | Decolonization INFLUENCE Iran, Nigeria | 36.50 | 6.00 | 38.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 5 | Latin American Death Squads INFLUENCE Iran, Nigeria | 36.50 | 6.00 | 38.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Bear Trap [47] as COUP`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], CIA Created[26], Bear Trap[47], Flower Power[62], Puppet Governments[67], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Bear Trap INFLUENCE Argentina, Chile, South Africa | 47.35 | 6.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Puppet Governments COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Bear Trap COUP Egypt | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Bear Trap COUP Iran | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 95: T7 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], Decolonization[30], De-Stalinization[33], Lonely Hearts Club Band[65], Latin American Death Squads[70], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 43.47 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 2 | De-Stalinization INFLUENCE East Germany, France, West Germany | 43.47 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 3 | De Gaulle Leads France COUP Mexico | 34.08 | 4.00 | 30.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |
| 4 | De-Stalinization COUP Mexico | 34.08 | 4.00 | 30.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |
| 5 | De Gaulle Leads France COUP Algeria | 33.33 | 4.00 | 29.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], CIA Created[26], Flower Power[62], Puppet Governments[67], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 40.88 | 4.00 | 37.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Puppet Governments INFLUENCE West Germany, Chile | 38.32 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:5.33 |
| 3 | CIA Created COUP Saharan States | 34.53 | 4.00 | 30.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Saharan States | 34.53 | 4.00 | 30.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 5 | Puppet Governments COUP Egypt | 31.98 | 4.00 | 28.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Truman Doctrine[19], Decolonization[30], De-Stalinization[33], Lonely Hearts Club Band[65], Latin American Death Squads[70], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 46.60 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 2 | De-Stalinization COUP Mexico | 34.55 | 4.00 | 31.00 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:2.5 |
| 3 | De-Stalinization COUP Algeria | 33.80 | 4.00 | 30.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:2.5 |
| 4 | Decolonization INFLUENCE France, West Germany | 31.20 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 5 | Latin American Death Squads INFLUENCE France, West Germany | 31.20 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], CIA Created[26], Flower Power[62], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Egypt | 25.90 | 4.00 | 22.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created COUP Iran | 25.90 | 4.00 | 22.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | CIA Created COUP Libya | 25.90 | 4.00 | 22.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Panama Canal Returned COUP Egypt | 25.90 | 4.00 | 22.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Panama Canal Returned COUP Iran | 25.90 | 4.00 | 22.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Truman Doctrine[19], Decolonization[30], Lonely Hearts Club Band[65], Latin American Death Squads[70], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Egypt | 26.05 | 6.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Egypt:13.20, control_break:Egypt, non_coup_milops_penalty:14.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany, Egypt | 26.05 | 6.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Egypt:13.20, control_break:Egypt, non_coup_milops_penalty:14.00 |
| 3 | Decolonization COUP Cameroon | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Decolonization COUP Saharan States | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Decolonization COUP Sudan | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Flower Power[62], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Chile, South Africa | 15.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Flower Power INFLUENCE Chile, South Africa | 15.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Colonial Rear Guards INFLUENCE Chile, South Africa | 15.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Panama Canal Returned INFLUENCE Chile | 14.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 5 | Panama Canal Returned COUP Colombia | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Latin American Death Squads[70], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Cameroon | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Sudan | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Guatemala | 20.97 | 4.00 | 17.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads INFLUENCE East Germany, West Germany | 18.73 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 102: T7 AR5 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Flower Power[62], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP SE African States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Zimbabwe | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Flower Power INFLUENCE Chile, South Africa | 12.63 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Cameroon | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Lone Gunman COUP Saharan States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Lone Gunman COUP Sudan | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman COUP Guatemala | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lonely Hearts Club Band COUP Cameroon | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Flower Power COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Flower Power COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Zimbabwe | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Cameroon | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Lonely Hearts Club Band COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP Sudan | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Guatemala | 10.30 | 4.00 | 22.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Cameroon | 9.20 | 4.00 | 17.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Colombia | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP SE African States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Zimbabwe | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP Guatemala | 8.30 | 4.00 | 20.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 107: T8 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Independent Reds[22], Junta[50], Missile Envy[52], We Will Bury You[53], Portuguese Empire Crumbles[55], Ask Not What Your Country Can Do For You[78], Marine Barracks Bombing[91]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Arms Race [42] as EVENT`
- flags: `milops_shortfall:8`
- hand: `De-Stalinization[33], Formosan Resolution[35], Brush War[39], Arms Race[42], Quagmire[45], Junta[50], Muslim Revolution[59], Shuttle Diplomacy[74], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Independent Reds[22], Junta[50], Missile Envy[52], Portuguese Empire Crumbles[55], Ask Not What Your Country Can Do For You[78], Marine Barracks Bombing[91]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Junta INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Missile Envy INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De-Stalinization[33], Formosan Resolution[35], Brush War[39], Quagmire[45], Junta[50], Muslim Revolution[59], Shuttle Diplomacy[74], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 38.06 | 6.00 | 65.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 3 | Formosan Resolution INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Junta INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | Shuttle Diplomacy COUP Saharan States | 26.19 | 4.00 | 22.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Independent Reds[22], Junta[50], Missile Envy[52], Portuguese Empire Crumbles[55], Ask Not What Your Country Can Do For You[78], Marine Barracks Bombing[91]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE France, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Missile Envy INFLUENCE France, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | Marine Barracks Bombing INFLUENCE France, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 5 | Duck and Cover INFLUENCE East Germany, France, West Germany | 29.38 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `De-Stalinization[33], Formosan Resolution[35], Brush War[39], Quagmire[45], Junta[50], Muslim Revolution[59], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 36.53 | 6.00 | 65.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Junta INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | De-Stalinization INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Brush War INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Independent Reds[22], Missile Envy[52], Portuguese Empire Crumbles[55], Ask Not What Your Country Can Do For You[78], Marine Barracks Bombing[91]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 4 | Duck and Cover INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De-Stalinization[33], Formosan Resolution[35], Brush War[39], Quagmire[45], Junta[50], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Junta INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | De-Stalinization INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | Brush War INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Quagmire INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Independent Reds[22], Portuguese Empire Crumbles[55], Ask Not What Your Country Can Do For You[78], Marine Barracks Bombing[91]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Portuguese Empire Crumbles COUP Cameroon | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Portuguese Empire Crumbles COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Portuguese Empire Crumbles COUP Sudan | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De-Stalinization[33], Brush War[39], Quagmire[45], Junta[50], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Junta COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Junta COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Junta COUP Zimbabwe | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Junta COUP Colombia | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Marine Barracks Bombing [91] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Independent Reds[22], Ask Not What Your Country Can Do For You[78], Marine Barracks Bombing[91]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing COUP Cameroon | 22.88 | 4.00 | 19.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 2 | Marine Barracks Bombing COUP Saharan States | 22.88 | 4.00 | 19.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 3 | Marine Barracks Bombing COUP Sudan | 22.88 | 4.00 | 19.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | Marine Barracks Bombing COUP Guatemala | 22.13 | 4.00 | 18.43 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | Marine Barracks Bombing INFLUENCE West Germany, Pakistan | 19.22 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 118: T8 AR5 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:8`
- hand: `De-Stalinization[33], Brush War[39], Quagmire[45], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP SE African States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Zimbabwe | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Colombia | 16.03 | 4.00 | 12.18 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Guatemala | 15.78 | 4.00 | 11.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 119: T8 AR6 USSR

- chosen: `Duck and Cover [4] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Duck and Cover[4], Independent Reds[22], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Ask Not What Your Country Can Do For You COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Independent Reds COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Duck and Cover COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Duck and Cover COUP Sudan | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 120: T8 AR6 US

- chosen: `De-Stalinization [33] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `De-Stalinization[33], Brush War[39], Quagmire[45]`
- state: `VP 2, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Brush War COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | De-Stalinization COUP SE African States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Zimbabwe | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 121: T8 AR7 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Independent Reds[22], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You COUP Saharan States | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Independent Reds COUP Saharan States | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Cameroon | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP Sudan | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP Guatemala | 13.15 | 4.00 | 29.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Brush War [39] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Brush War[39], Quagmire[45]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Saharan States | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Quagmire COUP Saharan States | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Brush War COUP SE African States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Brush War COUP Zimbabwe | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP SE African States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 123: T9 AR0 USSR

- chosen: `Summit [48] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Nasser[15], Indo-Pakistani War[24], Bear Trap[47], Summit[48], Kitchen Debates[51], Lonely Hearts Club Band[65], Iranian Hostage Crisis[85], Tear Down this Wall[99], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Iranian Hostage Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Blockade[10], Arab-Israeli War[13], Nuclear Test Ban[34], Latin American Death Squads[70], Nixon Plays the China Card[72], Voice of America[75], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -3, DEFCON +2, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Nasser[15], Indo-Pakistani War[24], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Iranian Hostage Crisis[85], Tear Down this Wall[99], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE Poland, West Germany, Pakistan | 49.41 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:10.29 |
| 2 | Iranian Hostage Crisis COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | Indo-Pakistani War COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Colonial Rear Guards COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 5 | Iranian Hostage Crisis COUP Italy | 41.07 | 4.00 | 37.52 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:9, milops_urgency:1.29, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Alliance for Progress [79] as COUP`
- flags: `milops_shortfall:9`
- hand: `Blockade[10], Arab-Israeli War[13], Latin American Death Squads[70], Nixon Plays the China Card[72], Voice of America[75], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Nigeria | 56.97 | 4.00 | 53.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Indonesia | 54.72 | 4.00 | 51.17 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | Latin American Death Squads COUP Nigeria | 50.62 | 4.00 | 46.92 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Nixon Plays the China Card COUP Nigeria | 50.62 | 4.00 | 46.92 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 5 | Voice of America COUP Nigeria | 50.62 | 4.00 | 46.92 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 127: T9 AR2 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Nasser[15], Indo-Pakistani War[24], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Tear Down this Wall[99], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 4, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Nigeria | 51.05 | 4.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | Colonial Rear Guards COUP Nigeria | 51.05 | 4.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | Nasser COUP Nigeria | 44.70 | 4.00 | 40.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 4 | Indo-Pakistani War COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 128: T9 AR2 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Latin American Death Squads[70], Nixon Plays the China Card[72], Voice of America[75], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Nigeria | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Nixon Plays the China Card COUP Nigeria | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | Voice of America COUP Nigeria | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Egypt | 32.40 | 4.00 | 28.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Latin American Death Squads COUP Iran | 32.40 | 4.00 | 28.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Tear Down this Wall[99], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Saharan States | 42.35 | 4.00 | 38.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 2 | Nasser COUP Saharan States | 36.00 | 4.00 | 32.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 3 | Bear Trap COUP Saharan States | 28.70 | 4.00 | 45.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Tear Down this Wall COUP Saharan States | 28.70 | 4.00 | 45.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 27.70 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Nixon Plays the China Card[72], Voice of America[75], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | Voice of America COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 29.30 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 4 | Voice of America INFLUENCE East Germany, West Germany | 29.30 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | Arab-Israeli War COUP Saharan States | 25.95 | 4.00 | 38.25 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Tear Down this Wall[99]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Saharan States | 36.70 | 4.00 | 32.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 2 | Bear Trap COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Tear Down this Wall COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Saharan States | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Kitchen Debates COUP Saharan States | 24.70 | 4.00 | 32.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Voice of America[75], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Voice of America COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Voice of America COUP SE African States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Voice of America COUP Zimbabwe | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Voice of America COUP Colombia | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Tear Down this Wall[99]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 16.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 16.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Bear Trap COUP Cameroon | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Bear Trap COUP Saharan States | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Bear Trap COUP Sudan | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Arab-Israeli War COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Zimbabwe | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Colombia | 5.05 | 4.00 | 17.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Tear Down this Wall [99] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Kitchen Debates[51], Lonely Hearts Club Band[65], Tear Down this Wall[99]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall COUP Cameroon | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Tear Down this Wall COUP Saharan States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Tear Down this Wall COUP Sudan | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Tear Down this Wall COUP Guatemala | 10.15 | 4.00 | 26.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 136: T9 AR6 US

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Blockade COUP SE African States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Blockade COUP Zimbabwe | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Lone Gunman COUP Saharan States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Lone Gunman COUP SE African States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Kitchen Debates COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band COUP Guatemala | 12.80 | 4.00 | 25.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Lone Gunman [109] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Saharan States | 11.20 | 4.00 | 19.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Lone Gunman COUP SE African States | 11.20 | 4.00 | 19.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Zimbabwe | 11.20 | 4.00 | 19.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Lone Gunman COUP Colombia | 10.70 | 4.00 | 18.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Lone Gunman COUP Guatemala | 10.45 | 4.00 | 18.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 139: T10 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `COMECON[14], CIA Created[26], Brezhnev Doctrine[54], Allende[57], Willy Brandt[58], The Iron Lady[86], Reagan Bombs Libya[87], Soviets Shoot Down KAL 007[92], Terrorism[95]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Terrorism EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Allende EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Arab-Israeli War[13], Decolonization[30], Special Relationship[37], Cuban Missile Crisis[43], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], Willy Brandt[58], ABM Treaty[60]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brezhnev Doctrine [54] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `CIA Created[26], Brezhnev Doctrine[54], Allende[57], Willy Brandt[58], The Iron Lady[86], Reagan Bombs Libya[87], Soviets Shoot Down KAL 007[92], Terrorism[95]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine COUP Saharan States | 48.76 | 4.00 | 45.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 48.62 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | Willy Brandt COUP Saharan States | 42.41 | 4.00 | 38.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Terrorism COUP Saharan States | 42.41 | 4.00 | 38.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, France, West Germany, Congo/Zaire | 40.67 | 6.00 | 70.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `milops_shortfall:10`
- hand: `Arab-Israeli War[13], Decolonization[30], Special Relationship[37], Cuban Missile Crisis[43], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], Willy Brandt[58]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Nigeria | 57.26 | 4.00 | 53.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Cuban Missile Crisis COUP Indonesia | 55.01 | 4.00 | 51.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | Special Relationship COUP Nigeria | 50.91 | 4.00 | 47.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Nuclear Subs COUP Nigeria | 50.91 | 4.00 | 47.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Special Relationship COUP Indonesia | 48.66 | 4.00 | 44.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 143: T10 AR2 USSR

- chosen: `Soviets Shoot Down KAL 007 [92] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Allende[57], Willy Brandt[58], The Iron Lady[86], Reagan Bombs Libya[87], Soviets Shoot Down KAL 007[92], Terrorism[95]`
- state: `VP -2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, France, West Germany, Nigeria | 47.17 | 6.00 | 75.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 2 | Willy Brandt COUP Saharan States | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 3 | Terrorism COUP Saharan States | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 4 | Willy Brandt INFLUENCE France, Nigeria | 38.27 | 6.00 | 41.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:9.33 |
| 5 | Terrorism INFLUENCE France, Nigeria | 38.27 | 6.00 | 41.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], Decolonization[30], Special Relationship[37], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], Willy Brandt[58]`
- state: `VP -2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Nigeria | 44.38 | 4.00 | 40.68 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Nuclear Subs COUP Nigeria | 44.38 | 4.00 | 40.68 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | We Will Bury You INFLUENCE East Germany, France, West Germany, Morocco | 41.37 | 6.00 | 69.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Morocco:14.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | Kitchen Debates COUP Nigeria | 38.03 | 4.00 | 34.18 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | We Will Bury You COUP Nigeria | 33.08 | 4.00 | 53.68 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:5.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Willy Brandt [58] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], Allende[57], Willy Brandt[58], The Iron Lady[86], Reagan Bombs Libya[87], Terrorism[95]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Saharan States | 42.35 | 4.00 | 38.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 2 | Terrorism COUP Saharan States | 42.35 | 4.00 | 38.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 3 | Allende COUP Saharan States | 36.00 | 4.00 | 32.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 4 | The Iron Lady COUP Saharan States | 28.70 | 4.00 | 45.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 27.70 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], Willy Brandt[58]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Cameroon | 42.35 | 4.00 | 38.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 2 | We Will Bury You INFLUENCE East Germany, France, West Germany, Morocco | 39.50 | 6.00 | 69.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Morocco:14.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | Kitchen Debates COUP Cameroon | 36.00 | 4.00 | 32.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 4 | Nuclear Subs INFLUENCE West Germany, Morocco | 31.20 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Morocco:14.80, control_break:Morocco, non_coup_milops_penalty:11.20 |
| 5 | We Will Bury You COUP Cameroon | 31.05 | 4.00 | 51.65 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:5.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Terrorism [95] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], Allende[57], The Iron Lady[86], Reagan Bombs Libya[87], Terrorism[95]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Terrorism INFLUENCE East Germany, West Germany | 24.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 2 | Terrorism COUP Cameroon | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 3 | Terrorism COUP Saharan States | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Terrorism COUP Sudan | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | The Iron Lady INFLUENCE East Germany, France, West Germany | 21.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], Decolonization[30], Kitchen Debates[51], We Will Bury You[53], Willy Brandt[58]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Cameroon | 36.70 | 4.00 | 32.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 2 | We Will Bury You INFLUENCE East Germany, France, West Germany, Morocco | 36.70 | 6.00 | 69.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Morocco:14.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | We Will Bury You COUP Cameroon | 31.75 | 4.00 | 52.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Cameroon | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Cameroon | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Allende[57], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, France, West Germany | 16.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Allende COUP Cameroon | 15.87 | 4.00 | 12.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Saharan States | 15.87 | 4.00 | 12.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende COUP Sudan | 15.87 | 4.00 | 12.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Guatemala | 15.12 | 4.00 | 11.27 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `We Will Bury You [53] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], We Will Bury You[53], Willy Brandt[58]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You COUP Cameroon | 32.92 | 4.00 | 53.52 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 2 | We Will Bury You INFLUENCE East Germany, France, West Germany, Morocco | 32.03 | 6.00 | 69.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Morocco:14.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Arab-Israeli War COUP Cameroon | 28.22 | 4.00 | 40.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Cameroon | 28.22 | 4.00 | 40.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Cameroon | 28.22 | 4.00 | 40.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 151: T10 AR6 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], Allende[57], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Cameroon | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Allende COUP Saharan States | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Sudan | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende COUP Guatemala | 17.45 | 4.00 | 13.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Reagan Bombs Libya COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], Willy Brandt[58]`
- state: `VP -2, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Reagan Bombs Libya [87] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya COUP Cameroon | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Reagan Bombs Libya COUP Saharan States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Sudan | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP Guatemala | 14.80 | 4.00 | 27.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Cameroon | 13.20 | 4.00 | 21.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Decolonization[30], Willy Brandt[58]`
- state: `VP -2, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Decolonization COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Zimbabwe | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -4, DEFCON +1, MilOps U-3/A-4`
