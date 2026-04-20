# minimal_hybrid detailed rollout log

- seed: `20260534`
- winner: `USSR`
- final_vp: `1`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Socialist Governments[7], Romanian Abdication[12], COMECON[14], East European Unrest[29], UN Intervention[32], De-Stalinization[33], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Marshall Plan[23], Indo-Pakistani War[24], CIA Created[26], Suez Crisis[28], Red Scare/Purge[31]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +3, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Socialist Governments[7], Romanian Abdication[12], COMECON[14], East European Unrest[29], UN Intervention[32], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Iran | 77.00 | 4.00 | 73.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | COMECON COUP Iran | 77.00 | 4.00 | 73.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 3 | De-Stalinization COUP Iran | 77.00 | 4.00 | 73.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 4 | The Cambridge Five COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Romanian Abdication COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Indo-Pakistani War[24], CIA Created[26], Suez Crisis[28], Red Scare/Purge[31]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE Italy, North Korea, Indonesia, Philippines | 81.37 | 6.00 | 77.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Indo-Pakistani War INFLUENCE Italy, Indonesia | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:1.33 |
| 3 | Suez Crisis INFLUENCE Italy, Indonesia, Philippines | 43.97 | 6.00 | 59.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | Red Scare/Purge COUP Syria | 38.85 | 4.00 | 35.45 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5 |
| 5 | Red Scare/Purge COUP North Korea | 38.20 | 4.00 | 34.80 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], COMECON[14], East European Unrest[29], UN Intervention[32], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Japan, North Korea, Thailand | 66.70 | 6.00 | 61.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | De-Stalinization INFLUENCE Japan, North Korea, Thailand | 66.70 | 6.00 | 61.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 3 | COMECON COUP Iran | 53.50 | 4.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus |
| 4 | De-Stalinization COUP Iran | 53.50 | 4.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus |
| 5 | The Cambridge Five INFLUENCE North Korea, Thailand | 48.70 | 6.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Indo-Pakistani War[24], CIA Created[26], Suez Crisis[28]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, Turkey | 38.60 | 6.00 | 34.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, non_coup_milops_penalty:1.60 |
| 2 | Suez Crisis INFLUENCE East Germany, Turkey, Panama | 34.65 | 6.00 | 50.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | Indo-Pakistani War COUP Syria | 28.25 | 4.00 | 24.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Indonesia | 25.90 | 4.00 | 22.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:3.5 |
| 5 | CIA Created COUP Japan | 24.10 | 4.00 | 20.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], East European Unrest[29], UN Intervention[32], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, Thailand | 68.70 | 6.00 | 63.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand |
| 2 | De-Stalinization COUP Iran | 53.50 | 4.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus |
| 3 | The Cambridge Five INFLUENCE East Germany, Thailand | 51.20 | 6.00 | 45.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, control_break:Thailand |
| 4 | East European Unrest INFLUENCE East Germany, West Germany, Thailand | 48.70 | 6.00 | 63.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | The Cambridge Five COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], CIA Created[26], Suez Crisis[28]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, Panama | 36.55 | 6.00 | 53.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Korean War INFLUENCE West Germany, Panama | 24.55 | 6.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Arab-Israeli War INFLUENCE West Germany, Panama | 24.55 | 6.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | CIA Created INFLUENCE West Germany | 24.50 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:2.00 |
| 5 | CIA Created COUP Japan | 24.25 | 4.00 | 20.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.25 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china`
- hand: `Romanian Abdication[12], East European Unrest[29], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | The Cambridge Five INFLUENCE South Korea, Thailand | 43.70 | 6.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45 |
| 3 | Romanian Abdication COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | UN Intervention COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | East European Unrest INFLUENCE South Korea, Israel, Thailand | 40.45 | 6.00 | 54.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], CIA Created[26]`
- state: `VP 3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created INFLUENCE Japan | 19.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.67 |
| 3 | Korean War INFLUENCE Japan, Egypt | 18.88 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Arab-Israeli War INFLUENCE Japan, Egypt | 18.88 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Korean War COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 11: T1 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Romanian Abdication[12], East European Unrest[29], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Italy, South Korea, Thailand | 40.00 | 6.00 | 54.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Romanian Abdication COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Italy, Iraq | 25.45 | 6.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty |
| 2 | Arab-Israeli War INFLUENCE Italy, Iraq | 25.45 | 6.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty |
| 3 | Blockade INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 4 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Romanian Abdication COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | Romanian Abdication REALIGN Iraq | 2.71 | -1.00 | 3.87 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan, Saudi Arabia | 22.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty |
| 2 | Blockade INFLUENCE Saudi Arabia | 10.15 | 6.00 | 16.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty |
| 3 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +2, DEFCON +1, MilOps U-3/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Fidel [8] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Vietnam Revolts[9], Nasser[15], Olympic Games[20], NATO[21], Containment[25], Formosan Resolution[35], NORAD[38]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Warsaw Pact Formed[16], De Gaulle Leads France[17], Truman Doctrine[19], Independent Reds[22], US/Japan Mutual Defense Pact[27], Decolonization[30], Special Relationship[37]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15], Olympic Games[20], NATO[21], Containment[25], Formosan Resolution[35], NORAD[38]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Iraq, Saudi Arabia, Philippines, Thailand | 51.23 | 6.00 | 72.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Vietnam Revolts INFLUENCE Iraq, Thailand | 42.78 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Olympic Games INFLUENCE Iraq, Thailand | 42.78 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Containment INFLUENCE Iraq, Philippines, Thailand | 39.08 | 6.00 | 56.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | NORAD INFLUENCE Iraq, Philippines, Thailand | 39.08 | 6.00 | 56.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Warsaw Pact Formed[16], De Gaulle Leads France[17], Truman Doctrine[19], Independent Reds[22], Decolonization[30], Special Relationship[37]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Egypt, Philippines | 54.18 | 6.00 | 51.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 2 | Independent Reds INFLUENCE Japan, Philippines | 38.63 | 6.00 | 35.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 3 | Special Relationship INFLUENCE Japan, Philippines | 38.63 | 6.00 | 35.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 4 | Duck and Cover COUP Philippines | 37.25 | 4.00 | 33.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:2.5 |
| 5 | Warsaw Pact Formed INFLUENCE Japan, Egypt, Philippines | 34.18 | 6.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Nasser[15], Olympic Games[20], Containment[25], Formosan Resolution[35], NORAD[38]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Indonesia | 49.50 | 4.00 | 45.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games COUP Indonesia | 49.50 | 4.00 | 45.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 3 | Nasser COUP Indonesia | 43.15 | 4.00 | 39.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 4 | Vietnam Revolts INFLUENCE Japan, Thailand | 39.10 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 5 | Olympic Games INFLUENCE Japan, Thailand | 39.10 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 20: T2 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], Truman Doctrine[19], Independent Reds[22], Decolonization[30], Special Relationship[37]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Egypt | 37.35 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 2 | Special Relationship INFLUENCE Japan, Egypt | 37.35 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 3 | Warsaw Pact Formed INFLUENCE Japan, Egypt, Indonesia | 33.05 | 6.00 | 50.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | De Gaulle Leads France INFLUENCE Japan, Egypt, Indonesia | 33.05 | 6.00 | 50.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Truman Doctrine INFLUENCE Egypt | 21.35 | 6.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], Olympic Games[20], Containment[25], Formosan Resolution[35], NORAD[38]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Containment INFLUENCE Japan, Iran, Thailand | 37.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE Japan, Iran, Thailand | 37.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Olympic Games COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], Truman Doctrine[19], Decolonization[30], Special Relationship[37]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan, Indonesia | 33.70 | 6.00 | 32.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Warsaw Pact Formed INFLUENCE Japan, Iran, Indonesia | 29.25 | 6.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | De Gaulle Leads France INFLUENCE Japan, Iran, Indonesia | 29.25 | 6.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Special Relationship COUP Cuba | 22.50 | 4.00 | 18.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open |
| 5 | Truman Doctrine COUP Cuba | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Containment[25], Formosan Resolution[35], NORAD[38]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Iran, Thailand | 37.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE Japan, Iran, Thailand | 37.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], Truman Doctrine[19], Decolonization[30]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Japan, Iran, Libya | 27.77 | 6.00 | 47.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | De Gaulle Leads France INFLUENCE Japan, Iran, Libya | 27.77 | 6.00 | 47.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Truman Doctrine COUP Iran | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Truman Doctrine COUP Cuba | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open |
| 5 | Warsaw Pact Formed COUP Iran | 18.50 | 4.00 | 34.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Formosan Resolution[35], NORAD[38]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Pakistan, Thailand | 39.10 | 6.00 | 53.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Pakistan, Thailand | 27.10 | 6.00 | 37.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | NORAD COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], Decolonization[30]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Japan, Pakistan, Libya | 23.35 | 6.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Truman Doctrine COUP Cuba | 23.15 | 4.00 | 19.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, coup_access_open |
| 3 | Truman Doctrine COUP Iran | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Truman Doctrine COUP Iraq | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |
| 5 | Truman Doctrine COUP Saudi Arabia | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Formosan Resolution[35]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE India, Thailand | 27.70 | 6.00 | 38.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Truman Doctrine[19], Decolonization[30]`
- state: `VP 5, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Cuba | 26.15 | 4.00 | 22.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, coup_access_open |
| 2 | Truman Doctrine COUP Iran | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Iraq | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3 |
| 4 | Truman Doctrine COUP Saudi Arabia | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3 |
| 5 | Truman Doctrine COUP Lebanon | 16.70 | 4.00 | 12.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +0, MilOps U-2/A+0`

## Step 29: T3 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], Captured Nazi Scientist[18], Olympic Games[20], Indo-Pakistani War[24], Containment[25], UN Intervention[32], Special Relationship[37]`
- state: `VP 6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], COMECON[14], Warsaw Pact Formed[16], Independent Reds[22], CIA Created[26], East European Unrest[29], Nuclear Test Ban[34]`
- state: `VP 6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Olympic Games[20], Indo-Pakistani War[24], Containment[25], UN Intervention[32], Special Relationship[37]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 2 | Indo-Pakistani War COUP Indonesia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 3 | Olympic Games INFLUENCE France, Thailand | 42.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Indo-Pakistani War INFLUENCE France, Thailand | 42.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Five Year Plan INFLUENCE France, Japan, Thailand | 38.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 32: T3 AR1 US

- chosen: `East European Unrest [29] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], COMECON[14], Warsaw Pact Formed[16], Independent Reds[22], CIA Created[26], East European Unrest[29]`
- state: `VP 5, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Indonesia | 56.15 | 4.00 | 52.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | East European Unrest INFLUENCE France, India, Japan | 52.30 | 6.00 | 50.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:India:15.55, access_touch:India, influence:Japan:16.15, non_coup_milops_penalty:4.00 |
| 3 | Independent Reds COUP Indonesia | 49.80 | 4.00 | 46.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | CIA Created COUP Indonesia | 43.45 | 4.00 | 39.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | East European Unrest COUP Pakistan | 39.25 | 4.00 | 35.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 33: T3 AR2 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Indo-Pakistani War[24], Containment[25], UN Intervention[32], Special Relationship[37]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE France, Thailand | 44.60 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, non_coup_milops_penalty:1.60 |
| 2 | Five Year Plan INFLUENCE France, Japan, Thailand | 40.60 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | Containment INFLUENCE France, Japan, Thailand | 40.60 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Special Relationship INFLUENCE France, Thailand | 28.60 | 6.00 | 40.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Indo-Pakistani War COUP Syria | 28.25 | 4.00 | 24.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `none`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], COMECON[14], Warsaw Pact Formed[16], Independent Reds[22], CIA Created[26]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE France, India | 40.30 | 6.00 | 34.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:India:15.55, access_touch:India |
| 2 | COMECON INFLUENCE France, India, Japan | 36.30 | 6.00 | 50.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:India:15.55, access_touch:India, influence:Japan:16.15, offside_ops_penalty |
| 3 | Warsaw Pact Formed INFLUENCE France, India, Japan | 36.30 | 6.00 | 50.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:India:15.55, access_touch:India, influence:Japan:16.15, offside_ops_penalty |
| 4 | Vietnam Revolts INFLUENCE France, India | 24.30 | 6.00 | 34.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:India:15.55, access_touch:India, offside_ops_penalty |
| 5 | CIA Created INFLUENCE India | 23.40 | 6.00 | 17.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Containment[25], UN Intervention[32], Special Relationship[37]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE France, Japan, Thailand | 40.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Containment INFLUENCE France, Japan, Thailand | 40.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Special Relationship INFLUENCE France, Thailand | 28.20 | 6.00 | 40.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 24.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | UN Intervention INFLUENCE Thailand | 24.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], COMECON[14], Warsaw Pact Formed[16], CIA Created[26]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, India, Japan | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, India, Japan | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty |
| 3 | CIA Created INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 4 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 5 | Romanian Abdication INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Containment[25], UN Intervention[32], Special Relationship[37]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Indonesia, Thailand | 35.33 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 23.63 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | UN Intervention INFLUENCE Thailand | 23.63 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Special Relationship INFLUENCE Japan, Thailand | 23.63 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Captured Nazi Scientist COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Warsaw Pact Formed[16], CIA Created[26]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Japan, Indonesia | 36.20 | 6.00 | 50.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty |
| 2 | CIA Created INFLUENCE Indonesia | 24.70 | 6.00 | 18.85 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia |
| 3 | Vietnam Revolts INFLUENCE Japan, Indonesia | 24.70 | 6.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty |
| 4 | Romanian Abdication INFLUENCE Indonesia | 12.70 | 6.00 | 18.85 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty |
| 5 | CIA Created COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], Special Relationship[37]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 19.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |
| 4 | UN Intervention INFLUENCE Thailand | 19.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |
| 5 | Captured Nazi Scientist COUP Iran | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `none`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 3 | CIA Created COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Vietnam Revolts COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Romanian Abdication INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `UN Intervention[32], Special Relationship[37]`
- state: `VP 5, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Israel | 26.25 | 4.00 | 22.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open |
| 2 | UN Intervention COUP Iran | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | UN Intervention COUP Iraq | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |
| 4 | UN Intervention COUP Saudi Arabia | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |
| 5 | Special Relationship INFLUENCE Israel, Thailand | 16.05 | 6.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12]`
- state: `VP 5, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Vietnam Revolts SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Vietnam Revolts COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Sudan | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], Independent Reds[22], East European Unrest[29], Special Relationship[37], How I Learned to Stop Worrying[49], Allende[57], Nixon Plays the China Card[72], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Allende EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Containment[25], East European Unrest[29], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], SALT Negotiations[46], Flower Power[62]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Independent Reds[22], East European Unrest[29], Special Relationship[37], How I Learned to Stop Worrying[49], Allende[57], Nixon Plays the China Card[72], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE Israel, Mexico | 34.48 | 6.00 | 33.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:4.57 |
| 2 | One Small Step INFLUENCE Israel, Mexico | 34.48 | 6.00 | 33.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:4.57 |
| 3 | Colonial Rear Guards INFLUENCE Israel, Mexico | 34.48 | 6.00 | 33.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:4.57 |
| 4 | East European Unrest INFLUENCE Israel, Mexico, Algeria | 30.53 | 6.00 | 49.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | How I Learned to Stop Worrying COUP Iran | 25.36 | 4.00 | 21.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], East European Unrest[29], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], SALT Negotiations[46], Flower Power[62]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, Mexico, Algeria, South Africa | 68.48 | 6.00 | 67.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 2 | SALT Negotiations INFLUENCE East Germany, Mexico, Algeria, South Africa | 68.48 | 6.00 | 67.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 3 | Formosan Resolution INFLUENCE East Germany, Mexico, South Africa | 52.43 | 6.00 | 51.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 4 | De-Stalinization INFLUENCE East Germany, Mexico, Algeria, South Africa | 48.48 | 6.00 | 67.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | East European Unrest COUP Mexico | 40.46 | 4.00 | 36.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Independent Reds[22], East European Unrest[29], Special Relationship[37], Allende[57], Nixon Plays the China Card[72], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Algeria | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Colonial Rear Guards COUP Algeria | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | One Small Step INFLUENCE UK, Algeria | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |
| 4 | Colonial Rear Guards INFLUENCE UK, Algeria | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |
| 5 | One Small Step COUP Egypt | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 48: T4 AR2 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], SALT Negotiations[46], Flower Power[62]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, West Germany, Algeria, South Africa | 69.92 | 6.00 | 69.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | Formosan Resolution INFLUENCE West Germany, Algeria, South Africa | 54.52 | 6.00 | 54.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, Algeria, South Africa | 49.92 | 6.00 | 69.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Vietnam Revolts INFLUENCE West Germany, Algeria, South Africa | 38.52 | 6.00 | 54.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Decolonization INFLUENCE West Germany, Algeria, South Africa | 38.52 | 6.00 | 54.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Independent Reds[22], East European Unrest[29], Special Relationship[37], Allende[57], Nixon Plays the China Card[72], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, Morocco | 39.85 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.20 |
| 2 | East European Unrest INFLUENCE East Germany, UK, Morocco | 35.85 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:UK:14.15, access_touch:UK, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Independent Reds INFLUENCE East Germany, Morocco | 23.85 | 6.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Special Relationship INFLUENCE East Germany, Morocco | 23.85 | 6.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, Morocco | 23.85 | 6.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], Flower Power[62]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Morocco, South Africa | 49.05 | 6.00 | 49.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 2 | De-Stalinization INFLUENCE East Germany, West Germany, Morocco, South Africa | 44.45 | 6.00 | 65.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Vietnam Revolts INFLUENCE West Germany, Morocco, South Africa | 33.05 | 6.00 | 49.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Decolonization INFLUENCE West Germany, Morocco, South Africa | 33.05 | 6.00 | 49.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Flower Power INFLUENCE West Germany, Morocco, South Africa | 33.05 | 6.00 | 49.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22], East European Unrest[29], Special Relationship[37], Allende[57], Nixon Plays the China Card[72]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, UK, West Germany | 29.40 | 6.00 | 47.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Allende INFLUENCE UK | 18.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:UK:14.15, access_touch:UK, non_coup_milops_penalty:4.00 |
| 3 | Independent Reds INFLUENCE UK, West Germany | 18.00 | 6.00 | 32.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Special Relationship INFLUENCE UK, West Germany | 18.00 | 6.00 | 32.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Nixon Plays the China Card INFLUENCE UK, West Germany | 18.00 | 6.00 | 32.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Decolonization[30], De-Stalinization[33], Flower Power[62]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany, South Africa | 41.60 | 6.00 | 64.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany, South Africa | 30.20 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Decolonization INFLUENCE East Germany, West Germany, South Africa | 30.20 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Flower Power INFLUENCE East Germany, West Germany, South Africa | 30.20 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Romanian Abdication INFLUENCE West Germany, South Africa | 18.80 | 6.00 | 32.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22], Special Relationship[37], Allende[57], Nixon Plays the China Card[72]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE France, West Germany | 21.07 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Special Relationship INFLUENCE France, West Germany | 21.07 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Allende INFLUENCE France | 21.07 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:5.33 |
| 4 | Nixon Plays the China Card INFLUENCE France, West Germany | 21.07 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Allende COUP Saharan States | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Decolonization[30], Flower Power[62]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany, South Africa | 27.53 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Decolonization INFLUENCE East Germany, West Germany, South Africa | 27.53 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Flower Power INFLUENCE East Germany, West Germany, South Africa | 27.53 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Romanian Abdication INFLUENCE West Germany, South Africa | 16.13 | 6.00 | 32.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Vietnam Revolts COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Special Relationship[37], Allende[57], Nixon Plays the China Card[72]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Allende COUP Guatemala | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Haiti | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Special Relationship INFLUENCE East Germany, West Germany | 12.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Allende INFLUENCE East Germany | 12.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30], Flower Power[62]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Flower Power COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Decolonization INFLUENCE East Germany, West Germany, South Africa | 10.20 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 5 | Flower Power INFLUENCE East Germany, West Germany, South Africa | 10.20 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 57: T4 AR7 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Special Relationship[37], Nixon Plays the China Card[72]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Special Relationship COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Special Relationship COUP Haiti | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Flower Power[62]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Flower Power INFLUENCE East Germany, West Germany, South Africa | 16.20 | 6.00 | 48.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 4 | Flower Power COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Socialist Governments[7], UN Intervention[32], Brezhnev Doctrine[54], Willy Brandt[58], Muslim Revolution[59], ABM Treaty[60], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], CIA Created[26], Red Scare/Purge[31], Camp David Accords[66], OAS Founded[71], Ussuri River Skirmish[77]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Socialist Governments[7], UN Intervention[32], Brezhnev Doctrine[54], Willy Brandt[58], ABM Treaty[60], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, West Germany | 51.94 | 6.00 | 52.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 2 | ABM Treaty COUP Egypt | 45.49 | 4.00 | 42.09 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | ABM Treaty COUP Mexico | 40.24 | 4.00 | 36.84 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:3.5 |
| 4 | ABM Treaty COUP Algeria | 39.49 | 4.00 | 36.09 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:3.5 |
| 5 | Socialist Governments COUP Egypt | 39.14 | 4.00 | 35.59 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], CIA Created[26], Camp David Accords[66], OAS Founded[71], Ussuri River Skirmish[77]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE West Germany, Saudi Arabia, South Africa | 48.59 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Ussuri River Skirmish COUP Syria | 36.64 | 4.00 | 33.09 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 3 | Ussuri River Skirmish COUP Mexico | 33.89 | 4.00 | 30.34 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Algeria | 33.14 | 4.00 | 29.59 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 5 | Olympic Games INFLUENCE West Germany, South Africa | 32.94 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Socialist Governments[7], UN Intervention[32], Brezhnev Doctrine[54], Willy Brandt[58], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Egypt | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | Brezhnev Doctrine COUP Egypt | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Che COUP Egypt | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Socialist Governments COUP Mexico | 34.25 | 4.00 | 30.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:2.5 |
| 5 | Brezhnev Doctrine COUP Mexico | 34.25 | 4.00 | 30.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 64: T5 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], CIA Created[26], Camp David Accords[66], OAS Founded[71]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, South Africa | 31.98 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 2 | Camp David Accords INFLUENCE West Germany, South Africa | 31.98 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 3 | Olympic Games COUP Colombia | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 4 | Olympic Games COUP Saharan States | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 5 | Olympic Games COUP SE African States | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], UN Intervention[32], Brezhnev Doctrine[54], Willy Brandt[58], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE West Germany, Egypt | 36.70 | 6.00 | 34.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Egypt:13.20, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 2 | Che INFLUENCE West Germany, Egypt | 36.70 | 6.00 | 34.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Egypt:13.20, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 3 | Brezhnev Doctrine COUP Saharan States | 24.10 | 4.00 | 20.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:4.5 |
| 4 | Brezhnev Doctrine COUP Sudan | 24.10 | 4.00 | 20.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:4.5 |
| 5 | Che COUP Saharan States | 24.10 | 4.00 | 20.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], Camp David Accords[66], OAS Founded[71]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Camp David Accords COUP Colombia | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Camp David Accords COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Camp David Accords COUP SE African States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Camp David Accords COUP Zimbabwe | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], UN Intervention[32], Willy Brandt[58], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, West Germany | 33.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 2 | Che COUP Saharan States | 24.40 | 4.00 | 20.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 3 | Che COUP Sudan | 24.40 | 4.00 | 20.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 4 | Che COUP Guatemala | 23.15 | 4.00 | 19.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 5 | Che COUP Haiti | 23.15 | 4.00 | 19.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], OAS Founded[71]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP SE African States | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Zimbabwe | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Colombia | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 69: T5 AR5 USSR

- chosen: `Willy Brandt [58] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], UN Intervention[32], Willy Brandt[58], Ask Not What Your Country Can Do For You[78]`
- state: `VP 5, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 2 | Willy Brandt COUP Sudan | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 3 | Willy Brandt COUP Guatemala | 18.30 | 4.00 | 14.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | Willy Brandt COUP Haiti | 18.30 | 4.00 | 14.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | UN Intervention INFLUENCE West Germany | 16.67 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:4`
- hand: `Arab-Israeli War[13], Nasser[15], CIA Created[26], OAS Founded[71]`
- state: `VP 5, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 2 | OAS Founded COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 3 | Arab-Israeli War COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Nasser COUP Saharan States | 25.20 | 4.00 | 33.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | CIA Created COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], UN Intervention[32], Ask Not What Your Country Can Do For You[78]`
- state: `VP 5, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP Guatemala | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Haiti | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention INFLUENCE Nigeria | 12.45 | 6.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:4`
- hand: `Arab-Israeli War[13], Nasser[15], OAS Founded[71]`
- state: `VP 5, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Arab-Israeli War COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nasser COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | OAS Founded COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Five Year Plan [5] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Ask Not What Your Country Can Do For You[78]`
- state: `VP 5, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan COUP Saharan States | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Five Year Plan COUP Sudan | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Saharan States | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP Sudan | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Five Year Plan COUP Guatemala | 7.65 | 4.00 | 24.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15]`
- state: `VP 5, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nasser COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Colombia | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Zimbabwe | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-1`

## Step 75: T6 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Korean War[11], COMECON[14], Captured Nazi Scientist[18], Containment[25], Cuban Missile Crisis[43], Quagmire[45], Kitchen Debates[51], Missile Envy[52]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], NATO[21], Independent Reds[22], UN Intervention[32], Brush War[39], U2 Incident[63], Sadat Expels Soviets[73], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Korean War[11], Captured Nazi Scientist[18], Containment[25], Cuban Missile Crisis[43], Quagmire[45], Kitchen Debates[51], Missile Envy[52]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Nigeria | 50.99 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 2 | Quagmire INFLUENCE East Germany, West Germany, Nigeria | 50.99 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 3 | Korean War INFLUENCE West Germany, Nigeria | 35.59 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 4 | Missile Envy INFLUENCE West Germany, Nigeria | 35.59 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 5 | Cuban Missile Crisis COUP Mexico | 34.32 | 4.00 | 30.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Independent Reds[22], UN Intervention[32], Brush War[39], U2 Incident[63], Sadat Expels Soviets[73], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Sadat Expels Soviets COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 3 | Duck and Cover INFLUENCE Brazil, Venezuela, South Africa | 47.89 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 4 | Sadat Expels Soviets INFLUENCE Brazil, Venezuela, South Africa | 47.89 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 5 | Independent Reds COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 79: T6 AR2 USSR

- chosen: `Quagmire [45] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Korean War[11], Captured Nazi Scientist[18], Containment[25], Quagmire[45], Kitchen Debates[51], Missile Envy[52]`
- state: `VP 5, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Saharan States | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Quagmire INFLUENCE East Germany, France, West Germany | 44.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Korean War COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Missile Envy COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Blockade COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 80: T6 AR2 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Independent Reds[22], UN Intervention[32], Brush War[39], U2 Incident[63], Sadat Expels Soviets[73], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE Brazil, Venezuela, South Africa | 50.75 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | Sadat Expels Soviets COUP Saharan States | 47.40 | 4.00 | 43.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 3 | Independent Reds COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Sadat Expels Soviets COUP Egypt | 38.50 | 4.00 | 34.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Sadat Expels Soviets COUP Syria | 36.00 | 4.00 | 32.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Korean War[11], Captured Nazi Scientist[18], Containment[25], Kitchen Debates[51], Missile Envy[52]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 32.60 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 2 | Missile Envy INFLUENCE East Germany, West Germany | 32.60 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 3 | Containment INFLUENCE East Germany, France, West Germany | 28.00 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Korean War COUP Mexico | 27.20 | 4.00 | 23.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |
| 5 | Missile Envy COUP Mexico | 27.20 | 4.00 | 23.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:3`
- hand: `Independent Reds[22], UN Intervention[32], Brush War[39], U2 Incident[63], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Saharan States | 41.35 | 4.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 2 | Independent Reds INFLUENCE Brazil, Venezuela | 39.30 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:4.80 |
| 3 | Brush War INFLUENCE Argentina, Brazil, Venezuela | 37.35 | 6.00 | 56.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | U2 Incident INFLUENCE Argentina, Brazil, Venezuela | 37.35 | 6.00 | 56.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | UN Intervention COUP Saharan States | 35.00 | 4.00 | 31.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Containment[25], Kitchen Debates[51], Missile Envy[52]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Saharan States | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | Blockade COUP Saharan States | 35.45 | 4.00 | 31.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Saharan States | 35.45 | 4.00 | 31.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 4 | Missile Envy INFLUENCE East Germany, West Germany | 31.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Containment COUP Saharan States | 28.15 | 4.00 | 44.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `UN Intervention[32], Brush War[39], U2 Incident[63], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE Argentina, Brazil, Venezuela | 36.15 | 6.00 | 56.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | U2 Incident INFLUENCE Argentina, Brazil, Venezuela | 36.15 | 6.00 | 56.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | UN Intervention COUP Saharan States | 35.45 | 4.00 | 31.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Saharan States | 35.45 | 4.00 | 31.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 5 | Brush War COUP Saharan States | 28.15 | 4.00 | 44.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Containment[25], Kitchen Debates[51]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Blockade COUP Mexico | 22.05 | 4.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Mexico | 22.05 | 4.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Blockade COUP Algeria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Algeria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:3`
- hand: `UN Intervention[32], U2 Incident[63], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | U2 Incident INFLUENCE Argentina, Chile, South Africa | 34.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | U2 Incident COUP Saharan States | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | UN Intervention COUP Egypt | 27.30 | 4.00 | 23.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Kitchen Debates[51]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Mexico | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Mexico | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 3 | Blockade COUP Algeria | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Algeria | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 5 | Blockade COUP Iran | 21.80 | 4.00 | 17.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `U2 Incident[63], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE Mexico, Argentina, Chile | 21.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | Panama Canal Returned COUP Colombia | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Saharan States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP SE African States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Zimbabwe | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Kitchen Debates[51]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Sudan | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Guatemala | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Haiti | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:3`
- hand: `Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP SE African States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Zimbabwe | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Guatemala | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 91: T7 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], Romanian Abdication[12], Indo-Pakistani War[24], Nuclear Test Ban[34], Arms Race[42], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:7`
- hand: `COMECON[14], Indo-Pakistani War[24], Nuclear Test Ban[34], The Cambridge Five[36], Special Relationship[37], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69], Alliance for Progress[79]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Arms Race [42] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], Romanian Abdication[12], Indo-Pakistani War[24], Arms Race[42], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race COUP Indonesia | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:4.5 |
| 2 | Arms Race INFLUENCE East Germany, West Germany, Congo/Zaire | 45.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 3 | Indo-Pakistani War COUP Indonesia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:3.5 |
| 4 | South African Unrest COUP Indonesia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Indonesia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 94: T7 AR1 US

- chosen: `Alliance for Progress [79] as COUP`
- flags: `milops_shortfall:7`
- hand: `COMECON[14], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69], Alliance for Progress[79]`
- state: `VP 7, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Indonesia | 55.90 | 4.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Indo-Pakistani War COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Special Relationship COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Nuclear Subs COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Junta COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 95: T7 AR2 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Romanian Abdication[12], Indo-Pakistani War[24], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70]`
- state: `VP 7, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, Congo/Zaire | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:5.33 |
| 2 | South African Unrest INFLUENCE West Germany, Congo/Zaire | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:5.33 |
| 3 | Latin American Death Squads INFLUENCE West Germany, Congo/Zaire | 32.72 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:5.33 |
| 4 | Five Year Plan INFLUENCE East Germany, West Germany, Congo/Zaire | 28.12 | 6.00 | 47.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Indo-Pakistani War COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69]`
- state: `VP 7, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Chile, South Africa | 33.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 2 | Special Relationship INFLUENCE Chile, South Africa | 33.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 3 | Nuclear Subs INFLUENCE Chile, South Africa | 33.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 4 | Junta INFLUENCE Chile, South Africa | 33.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 5 | John Paul II Elected Pope INFLUENCE Chile, South Africa | 33.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Romanian Abdication[12], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70]`
- state: `VP 7, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE Angola, Congo/Zaire | 41.10 | 6.00 | 41.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:6.40 |
| 2 | Latin American Death Squads INFLUENCE Angola, Congo/Zaire | 41.10 | 6.00 | 41.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:6.40 |
| 3 | Five Year Plan INFLUENCE West Germany, Angola, Congo/Zaire | 37.10 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | South African Unrest COUP Mexico | 27.80 | 4.00 | 24.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 5 | Latin American Death Squads COUP Mexico | 27.80 | 4.00 | 24.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], The Cambridge Five[36], Special Relationship[37], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69]`
- state: `VP 7, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Chile, South Africa | 37.90 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 2 | Nuclear Subs INFLUENCE Chile, South Africa | 37.90 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 3 | Junta INFLUENCE Chile, South Africa | 37.90 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 4 | John Paul II Elected Pope INFLUENCE Chile, South Africa | 37.90 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 5 | COMECON INFLUENCE Argentina, Chile, South Africa | 33.95 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Romanian Abdication[12], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70]`
- state: `VP 7, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, Angola | 29.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |
| 2 | Latin American Death Squads COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 3 | Latin American Death Squads COUP Algeria | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Latin American Death Squads COUP Iran | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Latin American Death Squads COUP Angola | 25.05 | 4.00 | 21.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], The Cambridge Five[36], Nuclear Subs[44], Junta[50], John Paul II Elected Pope[69]`
- state: `VP 7, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Egypt | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Junta COUP Egypt | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | John Paul II Elected Pope COUP Egypt | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Nuclear Subs INFLUENCE Chile, South Africa | 31.30 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Junta INFLUENCE Chile, South Africa | 31.30 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, West Germany, Angola | 22.18 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Romanian Abdication COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Romanian Abdication COUP Sudan | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], The Cambridge Five[36], Junta[50], John Paul II Elected Pope[69]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE West Germany, Chile | 32.98 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:10.67 |
| 2 | John Paul II Elected Pope INFLUENCE West Germany, Chile | 32.98 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:10.67 |
| 3 | COMECON INFLUENCE West Germany, Chile, South Africa | 29.63 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Junta COUP Colombia | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Junta COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Romanian Abdication COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication COUP Sudan | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Romanian Abdication COUP Guatemala | 15.95 | 4.00 | 12.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], The Cambridge Five[36], John Paul II Elected Pope[69]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Colombia | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | John Paul II Elected Pope COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | John Paul II Elected Pope COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | John Paul II Elected Pope COUP Zimbabwe | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | John Paul II Elected Pope COUP Guatemala | 22.30 | 4.00 | 18.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Puppet Governments COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `COMECON [14] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `COMECON[14], The Cambridge Five[36]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Colombia | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | COMECON COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | COMECON COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | COMECON COUP Zimbabwe | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP Guatemala | 14.65 | 4.00 | 31.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 107: T8 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Independent Reds[22], Red Scare/Purge[31], SALT Negotiations[46], Liberation Theology[76], One Small Step[81], Che[83], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 7, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Romanian Abdication[12], Red Scare/Purge[31], Nuclear Subs[44], Kitchen Debates[51], Missile Envy[52], Willy Brandt[58], Puppet Governments[67], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `SALT Negotiations [46] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Independent Reds[22], SALT Negotiations[46], Liberation Theology[76], One Small Step[81], Che[83], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 7, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations COUP Algeria | 34.43 | 4.00 | 30.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |
| 2 | Che COUP Algeria | 34.43 | 4.00 | 30.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |
| 3 | SALT Negotiations COUP Mexico | 33.68 | 4.00 | 30.13 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |
| 4 | Che COUP Mexico | 33.68 | 4.00 | 30.13 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |
| 5 | SALT Negotiations COUP Iran | 33.18 | 4.00 | 29.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 110: T8 AR1 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:8`
- hand: `Romanian Abdication[12], Nuclear Subs[44], Kitchen Debates[51], Missile Envy[52], Willy Brandt[58], Puppet Governments[67], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Saharan States | 20.98 | 4.00 | 17.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:3.5 |
| 2 | Nuclear Subs COUP SE African States | 20.98 | 4.00 | 17.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:3.5 |
| 3 | Nuclear Subs COUP Zimbabwe | 20.98 | 4.00 | 17.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:3.5 |
| 4 | Missile Envy COUP Saharan States | 20.98 | 4.00 | 17.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:3.5 |
| 5 | Missile Envy COUP SE African States | 20.98 | 4.00 | 17.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 111: T8 AR2 USSR

- chosen: `Che [83] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Independent Reds[22], Liberation Theology[76], One Small Step[81], Che[83], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Saharan States | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 2 | Liberation Theology COUP Saharan States | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | One Small Step COUP Saharan States | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 4 | Ortega Elected in Nicaragua COUP Saharan States | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 5 | Lone Gunman COUP Saharan States | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Missile Envy [52] as COUP`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Missile Envy[52], Willy Brandt[58], Puppet Governments[67], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Puppet Governments COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Iran-Iraq War COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Kitchen Debates COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Willy Brandt COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Liberation Theology [76] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Independent Reds[22], Liberation Theology[76], One Small Step[81], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Liberation Theology COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Liberation Theology COUP SE African States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Liberation Theology COUP Sudan | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Willy Brandt[58], Puppet Governments[67], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 21.15 | 4.00 | 17.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 2 | Puppet Governments COUP SE African States | 21.15 | 4.00 | 17.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 3 | Puppet Governments COUP Zimbabwe | 21.15 | 4.00 | 17.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 4 | Iran-Iraq War COUP Saharan States | 21.15 | 4.00 | 17.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |
| 5 | Iran-Iraq War COUP SE African States | 21.15 | 4.00 | 17.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Independent Reds[22], One Small Step[81], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | Ortega Elected in Nicaragua COUP Saharan States | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 3 | Lone Gunman COUP Saharan States | 36.95 | 4.00 | 33.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 4 | Independent Reds COUP Saharan States | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Reagan Bombs Libya COUP Saharan States | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Iran-Iraq War [105] as COUP`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Willy Brandt[58], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Iran-Iraq War COUP SE African States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Iran-Iraq War COUP Zimbabwe | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Iran-Iraq War COUP Colombia | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Iran-Iraq War COUP Guatemala | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Ortega Elected in Nicaragua [94] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Independent Reds[22], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ortega Elected in Nicaragua COUP Saharan States | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 2 | Lone Gunman COUP Saharan States | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 3 | Independent Reds COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Ortega Elected in Nicaragua COUP Cameroon | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Willy Brandt[58], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Kitchen Debates COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Zimbabwe | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Colombia | 16.70 | 4.00 | 12.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Guatemala | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Independent Reds[22], Reagan Bombs Libya[87], Lone Gunman[109]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Saharan States | 40.70 | 4.00 | 36.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 2 | Independent Reds COUP Saharan States | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Saharan States | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Lone Gunman COUP Cameroon | 18.70 | 4.00 | 14.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP SE African States | 18.70 | 4.00 | 14.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Willy Brandt [58] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Willy Brandt[58], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Zimbabwe | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Independent Reds[22], Reagan Bombs Libya[87]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Saharan States | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Reagan Bombs Libya COUP Saharan States | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Independent Reds COUP Cameroon | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Independent Reds COUP SE African States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Independent Reds COUP Sudan | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP Zimbabwe | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Colombia | 19.05 | 4.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP Guatemala | 18.80 | 4.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 123: T9 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Korean War[11], Containment[25], East European Unrest[29], De-Stalinization[33], South African Unrest[56], Puppet Governments[67], Nixon Plays the China Card[72], North Sea Oil[89]`
- state: `VP 7, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | East European Unrest EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Duck and Cover[4], Special Relationship[37], Bear Trap[47], Latin American Death Squads[70], Our Man in Tehran[84], The Iron Lady[86], Star Wars[88], Tear Down this Wall[99]`
- state: `VP 7, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Tear Down this Wall EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Korean War[11], Containment[25], East European Unrest[29], South African Unrest[56], Puppet Governments[67], Nixon Plays the China Card[72], North Sea Oil[89]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Saharan States | 43.41 | 4.00 | 39.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 2 | South African Unrest COUP Saharan States | 43.41 | 4.00 | 39.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 3 | Containment COUP Saharan States | 29.76 | 4.00 | 46.21 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | East European Unrest COUP Saharan States | 29.76 | 4.00 | 46.21 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | North Sea Oil COUP Saharan States | 29.76 | 4.00 | 46.21 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 126: T9 AR1 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Special Relationship[37], Bear Trap[47], Latin American Death Squads[70], Our Man in Tehran[84], The Iron Lady[86], Star Wars[88], Tear Down this Wall[99]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Special Relationship INFLUENCE East Germany, West Germany | 28.61 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | Latin American Death Squads INFLUENCE East Germany, West Germany | 28.61 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `South African Unrest [56] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Containment[25], East European Unrest[29], South African Unrest[56], Puppet Governments[67], Nixon Plays the China Card[72], North Sea Oil[89]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Saharan States | 43.05 | 4.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | 29.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 3 | Containment COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | East European Unrest COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | North Sea Oil COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Special Relationship[37], Latin American Death Squads[70], Our Man in Tehran[84], The Iron Lady[86], Star Wars[88], Tear Down this Wall[99]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, France, West Germany | 43.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 43.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | The Iron Lady COUP Saharan States | 28.40 | 4.00 | 24.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5 |
| 4 | The Iron Lady COUP SE African States | 28.40 | 4.00 | 24.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:9, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5 |
| 5 | The Iron Lady COUP Zimbabwe | 28.40 | 4.00 | 24.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:9, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Containment [25] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Containment[25], East European Unrest[29], Puppet Governments[67], Nixon Plays the China Card[72], North Sea Oil[89]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment COUP Saharan States | 30.10 | 4.00 | 46.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | East European Unrest COUP Saharan States | 30.10 | 4.00 | 46.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | North Sea Oil COUP Saharan States | 30.10 | 4.00 | 46.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Saharan States | 27.75 | 4.00 | 40.05 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 27.75 | 4.00 | 40.05 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 130: T9 AR3 US

- chosen: `Tear Down this Wall [99] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Special Relationship[37], Latin American Death Squads[70], Our Man in Tehran[84], Star Wars[88], Tear Down this Wall[99]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 40.65 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Tear Down this Wall COUP Saharan States | 29.30 | 4.00 | 25.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, empty_coup_penalty, expected_swing:4.5 |
| 3 | Tear Down this Wall COUP SE African States | 29.30 | 4.00 | 25.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:9, milops_urgency:1.80, empty_coup_penalty, expected_swing:4.5 |
| 4 | Tear Down this Wall COUP Zimbabwe | 29.30 | 4.00 | 25.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:9, milops_urgency:1.80, empty_coup_penalty, expected_swing:4.5 |
| 5 | Tear Down this Wall COUP Colombia | 28.80 | 4.00 | 25.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.80, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `East European Unrest [29] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `East European Unrest[29], Puppet Governments[67], Nixon Plays the China Card[72], North Sea Oil[89]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | North Sea Oil COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | East European Unrest INFLUENCE East Germany, France, West Germany | 28.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:9`
- hand: `Special Relationship[37], Latin American Death Squads[70], Our Man in Tehran[84], Star Wars[88]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Saharan States | 24.30 | 4.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 2 | Special Relationship COUP SE African States | 24.30 | 4.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 3 | Special Relationship COUP Zimbabwe | 24.30 | 4.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Saharan States | 24.30 | 4.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP SE African States | 24.30 | 4.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 133: T9 AR5 USSR

- chosen: `North Sea Oil [89] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Puppet Governments[67], Nixon Plays the China Card[72], North Sea Oil[89]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Puppet Governments COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | North Sea Oil INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Puppet Governments INFLUENCE France, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:7`
- hand: `Latin American Death Squads[70], Our Man in Tehran[84], Star Wars[88]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP SE African States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Zimbabwe | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Our Man in Tehran COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Our Man in Tehran COUP SE African States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Puppet Governments[67], Nixon Plays the China Card[72]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Cameroon | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Sudan | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `milops_shortfall:7`
- hand: `Our Man in Tehran[84], Star Wars[88]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Saharan States | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Our Man in Tehran COUP SE African States | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Our Man in Tehran COUP Zimbabwe | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Star Wars COUP Saharan States | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Star Wars COUP SE African States | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Nixon Plays the China Card[72]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Saharan States | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Cameroon | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Sudan | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Guatemala | 18.80 | 4.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Star Wars [88] as COUP`
- flags: `milops_shortfall:7`
- hand: `Star Wars[88]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars COUP Saharan States | 60.55 | 4.00 | 56.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5 |
| 2 | Star Wars COUP SE African States | 38.55 | 4.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Star Wars COUP Zimbabwe | 38.55 | 4.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Star Wars COUP Colombia | 38.05 | 4.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Star Wars COUP Guatemala | 37.80 | 4.00 | 34.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 139: T10 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Blockade[10], CIA Created[26], East European Unrest[29], Nuclear Test Ban[34], Junta[50], Willy Brandt[58], Alliance for Progress[79], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Alliance for Progress [79] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Kitchen Debates[51], Brezhnev Doctrine[54], Allende[57], Camp David Accords[66], Alliance for Progress[79], Chernobyl[97]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Chernobyl EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -4, DEFCON +2, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Junta [50] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Blockade[10], CIA Created[26], East European Unrest[29], Junta[50], Willy Brandt[58], Alliance for Progress[79], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 2 | Willy Brandt COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 3 | Junta COUP Saharan States | 43.84 | 4.00 | 40.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Willy Brandt COUP Saharan States | 43.84 | 4.00 | 40.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Blockade COUP Indonesia | 43.74 | 4.00 | 39.89 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 142: T10 AR1 US

- chosen: `Chernobyl [97] as COUP`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Kitchen Debates[51], Brezhnev Doctrine[54], Allende[57], Camp David Accords[66], Chernobyl[97]`
- state: `VP 1, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl COUP Nigeria | 58.69 | 4.00 | 55.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Chernobyl COUP Indonesia | 56.44 | 4.00 | 52.89 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | Camp David Accords COUP Nigeria | 52.34 | 4.00 | 48.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Camp David Accords COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Chernobyl COUP Egypt | 47.04 | 4.00 | 43.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 143: T10 AR2 USSR

- chosen: `Willy Brandt [58] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], CIA Created[26], East European Unrest[29], Willy Brandt[58], Alliance for Progress[79], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Nigeria | 46.05 | 4.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Willy Brandt COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | Blockade COUP Nigeria | 39.70 | 4.00 | 35.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Lone Gunman COUP Nigeria | 39.70 | 4.00 | 35.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Blockade COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Kitchen Debates[51], Brezhnev Doctrine[54], Allende[57], Camp David Accords[66]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Cameroon | 43.05 | 4.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | CIA Created COUP Cameroon | 36.70 | 4.00 | 32.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Cameroon | 36.70 | 4.00 | 32.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 4 | Camp David Accords INFLUENCE East Germany, West Germany | 29.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 5 | Socialist Governments COUP Cameroon | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], CIA Created[26], East European Unrest[29], Alliance for Progress[79], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 38.00 | 4.00 | 34.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 2 | Lone Gunman COUP Saharan States | 38.00 | 4.00 | 34.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 3 | East European Unrest COUP Saharan States | 30.70 | 4.00 | 47.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Saharan States | 30.70 | 4.00 | 47.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | East European Unrest INFLUENCE East Germany, France, West Germany | 27.25 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Kitchen Debates[51], Brezhnev Doctrine[54], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Cameroon | 37.40 | 4.00 | 33.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 2 | CIA Created COUP Saharan States | 37.40 | 4.00 | 33.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Cameroon | 37.40 | 4.00 | 33.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Saharan States | 37.40 | 4.00 | 33.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 5 | Socialist Governments COUP Cameroon | 30.10 | 4.00 | 46.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `CIA Created[26], East European Unrest[29], Alliance for Progress[79], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Lone Gunman COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Kitchen Debates[51], Brezhnev Doctrine[54], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Cameroon | 38.45 | 4.00 | 34.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 2 | Kitchen Debates COUP Saharan States | 38.45 | 4.00 | 34.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 3 | Socialist Governments COUP Cameroon | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Socialist Governments COUP Saharan States | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Brezhnev Doctrine COUP Cameroon | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `CIA Created[26], Alliance for Progress[79], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Cameroon | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Lone Gunman COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Lone Gunman COUP SE African States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP Guatemala | 18.45 | 4.00 | 14.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Socialist Governments [7] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Brezhnev Doctrine[54], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Cameroon | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Socialist Governments COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Brezhnev Doctrine COUP Cameroon | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Brezhnev Doctrine COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Cameroon | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `CIA Created[26], Alliance for Progress[79], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Alliance for Progress COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Alliance for Progress COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Guatemala | 15.15 | 4.00 | 31.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 152: T10 AR6 US

- chosen: `Brezhnev Doctrine [54] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Vietnam Revolts[9], Brezhnev Doctrine[54], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine COUP Cameroon | 36.40 | 4.00 | 52.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Brezhnev Doctrine COUP Saharan States | 36.40 | 4.00 | 52.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Cameroon | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Allende COUP Cameroon | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Cameroon | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | CIA Created COUP Saharan States | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | CIA Created COUP SE African States | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP Sudan | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Panama Canal Returned COUP Cameroon | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Vietnam Revolts[9], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Cameroon | 44.55 | 4.00 | 56.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Saharan States | 44.55 | 4.00 | 56.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Cameroon | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Saharan States | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP SE African States | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`
