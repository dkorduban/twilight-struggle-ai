# minimal_hybrid detailed rollout log

- seed: `20260514`
- winner: `US`
- final_vp: `-6`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Fidel[8], Vietnam Revolts[9], Olympic Games[20], Marshall Plan[23], De-Stalinization[33], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Romanian Abdication[12], De Gaulle Leads France[17], Captured Nazi Scientist[18], Independent Reds[22], Indo-Pakistani War[24], CIA Created[26], Red Scare/Purge[31], Nuclear Test Ban[34]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Fidel[8], Vietnam Revolts[9], Olympic Games[20], Marshall Plan[23], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Vietnam Revolts COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Olympic Games COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | The Cambridge Five COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Marshall Plan COUP Iran | 56.18 | 4.00 | 76.78 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Romanian Abdication[12], De Gaulle Leads France[17], Captured Nazi Scientist[18], Independent Reds[22], Indo-Pakistani War[24], CIA Created[26], Nuclear Test Ban[34]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Turkey, North Korea, Indonesia, Philippines | 79.37 | 6.00 | 75.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Independent Reds INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Indo-Pakistani War INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 4 | De Gaulle Leads France INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Nuclear Test Ban COUP Syria | 36.68 | 4.00 | 33.28 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Olympic Games[20], Marshall Plan[23], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Olympic Games COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | The Cambridge Five COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Marshall Plan INFLUENCE West Germany, Japan, Thailand | 42.65 | 6.00 | 61.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Marshall Plan COUP Iran | 34.85 | 4.00 | 55.45 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Romanian Abdication[12], De Gaulle Leads France[17], Captured Nazi Scientist[18], Independent Reds[22], Indo-Pakistani War[24], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, France | 38.20 | 6.00 | 34.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, non_coup_milops_penalty:1.60 |
| 2 | Indo-Pakistani War INFLUENCE East Germany, France | 38.20 | 6.00 | 34.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, non_coup_milops_penalty:1.60 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, France, Panama | 34.25 | 6.00 | 50.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Independent Reds COUP Syria | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Syria | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Olympic Games[20], Marshall Plan[23], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, Japan, Thailand | 45.05 | 6.00 | 63.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Olympic Games INFLUENCE Thailand | 31.15 | 6.00 | 25.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 3 | The Cambridge Five INFLUENCE Thailand | 31.15 | 6.00 | 25.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 4 | Five Year Plan INFLUENCE East Germany, Thailand | 31.05 | 6.00 | 45.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Special Relationship INFLUENCE Thailand | 15.15 | 6.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Romanian Abdication[12], De Gaulle Leads France[17], Captured Nazi Scientist[18], Indo-Pakistani War[24], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Italy, Panama | 36.35 | 6.00 | 32.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.00 |
| 2 | De Gaulle Leads France INFLUENCE Italy, Japan, Panama | 32.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Indo-Pakistani War COUP Syria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 4 | Captured Nazi Scientist COUP Syria | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 5 | CIA Created COUP Syria | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china`
- hand: `Five Year Plan[5], Olympic Games[20], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 2 | The Cambridge Five INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 3 | Five Year Plan INFLUENCE West Germany, Thailand | 23.65 | 6.00 | 38.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Olympic Games COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 5 | The Cambridge Five COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], De Gaulle Leads France[17], Captured Nazi Scientist[18], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, Japan, Egypt | 34.18 | 6.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Captured Nazi Scientist INFLUENCE Italy | 22.63 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.67 |
| 3 | CIA Created INFLUENCE Italy | 22.63 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.67 |
| 4 | Captured Nazi Scientist COUP Syria | 20.97 | 4.00 | 17.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 5 | CIA Created COUP Syria | 20.97 | 4.00 | 17.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Five Year Plan[5], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 2 | Five Year Plan INFLUENCE West Germany, Thailand | 23.65 | 6.00 | 38.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, offside_ops_penalty |
| 3 | The Cambridge Five COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 4 | The Cambridge Five COUP El Salvador | 12.55 | 4.00 | 8.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:El Salvador, empty_coup_penalty, expected_swing:3.5 |
| 5 | The Cambridge Five COUP Guatemala | 12.55 | 4.00 | 8.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist INFLUENCE Egypt | 17.55 | 6.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:7.00 |
| 4 | CIA Created INFLUENCE Egypt | 17.55 | 6.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:7.00 |
| 5 | Captured Nazi Scientist COUP Lebanon | 11.70 | 4.00 | 7.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 13: T1 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Thailand | 23.65 | 6.00 | 38.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE Thailand | 10.15 | 6.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Five Year Plan COUP Syria | 10.00 | 4.00 | 26.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Special Relationship COUP Syria | 8.65 | 4.00 | 20.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `none`
- hand: `Romanian Abdication[12], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE West Germany | 26.50 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany |
| 2 | Romanian Abdication INFLUENCE West Germany | 14.50 | 6.00 | 20.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty |
| 3 | CIA Created COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | CIA Created COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Sudan | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 15: T2 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Blockade[10], COMECON[14], Nasser[15], Warsaw Pact Formed[16], NATO[21], East European Unrest[29], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Truman Doctrine[19], Containment[25], Suez Crisis[28], Decolonization[30], Formosan Resolution[35], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Warsaw Pact Formed[16], NATO[21], East European Unrest[29], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Pakistan, South Korea, Thailand | 57.83 | 6.00 | 54.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | NATO INFLUENCE Italy, Pakistan, South Korea, Thailand | 50.13 | 6.00 | 71.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Warsaw Pact Formed COUP Philippines | 41.92 | 4.00 | 38.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 4 | Duck and Cover INFLUENCE Pakistan, South Korea, Thailand | 37.83 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | East European Unrest INFLUENCE Pakistan, South Korea, Thailand | 37.83 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Truman Doctrine[19], Suez Crisis[28], Decolonization[30], Formosan Resolution[35], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Egypt, Iraq, Libya | 69.73 | 6.00 | 66.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:2.67 |
| 2 | Formosan Resolution INFLUENCE Japan, Egypt, Iraq | 54.18 | 6.00 | 51.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 3 | Socialist Governments INFLUENCE Japan, Egypt, Iraq, Libya | 49.73 | 6.00 | 66.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Suez Crisis INFLUENCE Japan, Egypt, Iraq, Libya | 49.73 | 6.00 | 66.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Truman Doctrine INFLUENCE Egypt, Iraq | 38.18 | 6.00 | 35.00 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], NATO[21], East European Unrest[29], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Italy, India, Pakistan, Thailand | 52.60 | 6.00 | 74.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 2 | Duck and Cover INFLUENCE India, Pakistan, Thailand | 40.30 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | East European Unrest INFLUENCE India, Pakistan, Thailand | 40.30 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Blockade COUP Philippines | 30.35 | 4.00 | 26.50 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:0.5 |
| 5 | Nasser COUP Philippines | 30.35 | 4.00 | 26.50 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Truman Doctrine[19], Suez Crisis[28], Decolonization[30], Formosan Resolution[35]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Italy, Libya, Saudi Arabia | 56.95 | 6.00 | 54.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Libya:13.70, control_break:Libya, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.20 |
| 2 | Socialist Governments INFLUENCE Italy, Japan, Libya, Saudi Arabia | 52.95 | 6.00 | 70.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Suez Crisis INFLUENCE Italy, Japan, Libya, Saudi Arabia | 52.95 | 6.00 | 70.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Arab-Israeli War INFLUENCE Italy, Libya, Saudi Arabia | 40.95 | 6.00 | 54.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Libya:13.70, control_break:Libya, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Decolonization INFLUENCE Italy, Libya, Saudi Arabia | 40.95 | 6.00 | 54.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Libya:13.70, control_break:Libya, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], East European Unrest[29], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | East European Unrest INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Blockade COUP Philippines | 30.55 | 4.00 | 26.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 4 | Nasser COUP Philippines | 30.55 | 4.00 | 26.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Philippines | 30.55 | 4.00 | 26.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Truman Doctrine[19], Suez Crisis[28], Decolonization[30]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan, Iran, Philippines | 48.50 | 6.00 | 66.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, Iran, Philippines | 48.50 | 6.00 | 66.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Truman Doctrine INFLUENCE Japan, Philippines | 37.45 | 6.00 | 35.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:4.00 |
| 4 | Arab-Israeli War INFLUENCE Japan, Iran, Philippines | 37.00 | 6.00 | 51.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Decolonization INFLUENCE Japan, Iran, Philippines | 37.00 | 6.00 | 51.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Nasser[15], East European Unrest[29], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Indonesia | 41.28 | 4.00 | 37.43 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 2 | Nasser COUP Indonesia | 41.28 | 4.00 | 37.43 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Indonesia | 41.28 | 4.00 | 37.43 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 4 | East European Unrest COUP Indonesia | 32.98 | 4.00 | 49.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | East European Unrest INFLUENCE Japan, Indonesia, Thailand | 32.67 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 24: T2 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Suez Crisis[28], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, North Korea, Pakistan | 49.52 | 6.00 | 69.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Truman Doctrine INFLUENCE Japan, Pakistan | 38.62 | 6.00 | 38.10 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Pakistan:14.95, access_touch:Pakistan, non_coup_milops_penalty:5.33 |
| 3 | Arab-Israeli War INFLUENCE West Germany, Japan, Pakistan | 38.12 | 6.00 | 53.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Decolonization INFLUENCE West Germany, Japan, Pakistan | 38.12 | 6.00 | 53.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Truman Doctrine COUP Iran | 19.13 | 4.00 | 15.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], East European Unrest[29], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Pakistan, Thailand | 35.10 | 6.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 4 | Nasser INFLUENCE Thailand | 19.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |
| 5 | UN Intervention INFLUENCE Thailand | 19.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE India, Japan | 30.55 | 6.00 | 38.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:14.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany, India, Japan | 30.05 | 6.00 | 54.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:India:15.55, access_touch:India, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Decolonization INFLUENCE West Germany, India, Japan | 30.05 | 6.00 | 54.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:India:15.55, access_touch:India, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Truman Doctrine COUP Iran | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Truman Doctrine COUP Iraq | 17.65 | 4.00 | 13.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Syria | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Syria | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 3 | Nasser COUP Iran | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | UN Intervention COUP Iran | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Nasser COUP Iraq | 17.65 | 4.00 | 13.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, India, Japan | 15.05 | 6.00 | 47.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 2 | Decolonization INFLUENCE West Germany, India, Japan | 15.05 | 6.00 | 47.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 3 | Arab-Israeli War COUP Iran | 12.15 | 4.00 | 24.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 4 | Decolonization COUP Iran | 12.15 | 4.00 | 24.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Lebanon | 5.05 | 4.00 | 17.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 29: T3 AR0 USSR

- chosen: `Korean War [11] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Korean War[11], Romanian Abdication[12], Truman Doctrine[19], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], The Cambridge Five[36]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Fidel[8], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], Independent Reds[22], Decolonization[30], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Indonesia | 47.30 | 4.00 | 43.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | The Cambridge Five COUP Indonesia | 47.30 | 4.00 | 43.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE UK, Japan, Indonesia, Thailand | 45.50 | 6.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Romanian Abdication COUP Indonesia | 40.95 | 4.00 | 37.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Indo-Pakistani War INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 32: T3 AR1 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Fidel[8], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], Independent Reds[22], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Indonesia | 38.70 | 6.00 | 37.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan, Indonesia | 34.20 | 6.00 | 52.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Warsaw Pact Formed INFLUENCE West Germany, Japan, Indonesia | 34.20 | 6.00 | 52.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | De Gaulle Leads France INFLUENCE West Germany, Japan, Indonesia | 34.20 | 6.00 | 52.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Independent Reds COUP Iran | 25.15 | 4.00 | 21.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Duck and Cover[4], Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE UK, Japan, Indonesia, Thailand | 47.90 | 6.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 40.70 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:1.60 |
| 3 | Duck and Cover INFLUENCE Japan, Indonesia, Thailand | 36.40 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Five Year Plan INFLUENCE Japan, Indonesia, Thailand | 36.40 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Romanian Abdication INFLUENCE Thailand | 24.70 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE UK, Japan, Indonesia | 34.40 | 6.00 | 53.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Warsaw Pact Formed INFLUENCE UK, Japan, Indonesia | 34.40 | 6.00 | 53.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | De Gaulle Leads France INFLUENCE UK, Japan, Indonesia | 34.40 | 6.00 | 53.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Fidel INFLUENCE UK, Indonesia | 22.40 | 6.00 | 37.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:13.65, control_break:UK, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Decolonization INFLUENCE UK, Indonesia | 22.40 | 6.00 | 37.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:13.65, control_break:UK, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Thailand | 40.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Duck and Cover INFLUENCE West Germany, Japan, Thailand | 35.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 35.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Romanian Abdication INFLUENCE Thailand | 24.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | The Cambridge Five COUP El Salvador | 14.05 | 4.00 | 10.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:El Salvador, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, India, Japan | 26.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | De Gaulle Leads France INFLUENCE West Germany, India, Japan | 26.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Captured Nazi Scientist COUP Iran | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Iraq | 17.15 | 4.00 | 13.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3 |
| 5 | Captured Nazi Scientist COUP Saudi Arabia | 17.15 | 4.00 | 13.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Duck and Cover[4], Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan, Thailand | 35.13 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 35.13 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Romanian Abdication INFLUENCE Thailand | 23.63 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Truman Doctrine INFLUENCE Thailand | 11.63 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Romanian Abdication COUP El Salvador | 8.87 | 4.00 | 5.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], De Gaulle Leads France[17], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, India, Japan | 29.90 | 6.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, control_break:India, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Captured Nazi Scientist COUP Iran | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Fidel INFLUENCE India, Japan | 18.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Captured Nazi Scientist INFLUENCE India | 18.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, control_break:India, non_coup_milops_penalty:8.00 |
| 5 | Decolonization INFLUENCE India, Japan | 18.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 30.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Romanian Abdication INFLUENCE Thailand | 19.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |
| 3 | Romanian Abdication COUP Iran | 18.80 | 4.00 | 14.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |
| 4 | Romanian Abdication COUP Iraq | 16.65 | 4.00 | 12.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |
| 5 | Romanian Abdication COUP Saudi Arabia | 16.65 | 4.00 | 12.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Iran | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Iraq | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3 |
| 3 | Captured Nazi Scientist COUP Saudi Arabia | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3 |
| 4 | Captured Nazi Scientist COUP Lebanon | 13.70 | 4.00 | 9.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP SE African States | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Truman Doctrine[19]`
- state: `VP 1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 15.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 2 | Romanian Abdication COUP El Salvador | 10.20 | 4.00 | 6.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP Guatemala | 10.20 | 4.00 | 6.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication COUP Colombia | 9.95 | 4.00 | 6.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine INFLUENCE Thailand | 3.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Decolonization[30]`
- state: `VP 1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP SE African States | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Fidel COUP Sudan | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Fidel COUP Zimbabwe | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP SE African States | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Sudan | 2.80 | 4.00 | 15.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-1`

## Step 43: T4 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Nasser[15], De Gaulle Leads France[17], CIA Created[26], The Cambridge Five[36], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], One Small Step[81], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], De Gaulle Leads France[17], US/Japan Mutual Defense Pact[27], Nuclear Subs[44], Kitchen Debates[51], South African Unrest[56], U2 Incident[63], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Nasser[15], CIA Created[26], The Cambridge Five[36], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], One Small Step[81], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE France, Chile | 40.48 | 6.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.57 |
| 2 | The Cambridge Five INFLUENCE France, Chile | 40.48 | 6.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.57 |
| 3 | One Small Step INFLUENCE France, Chile | 40.48 | 6.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.57 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE France, Mexico, Chile | 37.28 | 6.00 | 56.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Arab-Israeli War COUP Iran | 24.79 | 4.00 | 21.09 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], De Gaulle Leads France[17], Nuclear Subs[44], Kitchen Debates[51], South African Unrest[56], U2 Incident[63], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE France, Angola | 41.28 | 6.00 | 40.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 2 | Puppet Governments INFLUENCE France, Angola | 41.28 | 6.00 | 40.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 3 | Grain Sales to Soviets INFLUENCE France, Angola | 41.28 | 6.00 | 40.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 4 | De Gaulle Leads France INFLUENCE France, Mexico, Angola | 38.08 | 6.00 | 57.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:Mexico:14.95, access_touch:Mexico, influence:Angola:15.60, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | U2 Incident INFLUENCE France, Mexico, Angola | 38.08 | 6.00 | 57.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:Mexico:14.95, access_touch:Mexico, influence:Angola:15.60, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], CIA Created[26], The Cambridge Five[36], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], One Small Step[81], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE France, Argentina | 39.12 | 6.00 | 38.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:5.33 |
| 2 | One Small Step INFLUENCE France, Argentina | 39.12 | 6.00 | 38.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:5.33 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE France, Mexico, Argentina | 35.92 | 6.00 | 55.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, access_touch:Argentina, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | The Cambridge Five COUP Iran | 24.98 | 4.00 | 21.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | One Small Step COUP Iran | 24.98 | 4.00 | 21.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], De Gaulle Leads France[17], Kitchen Debates[51], South African Unrest[56], U2 Incident[63], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE Mexico, South Africa | 34.12 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 2 | Grain Sales to Soviets INFLUENCE Mexico, South Africa | 34.12 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 3 | De Gaulle Leads France INFLUENCE Mexico, Algeria, South Africa | 30.17 | 6.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | U2 Incident INFLUENCE Mexico, Algeria, South Africa | 30.17 | 6.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Puppet Governments COUP Iran | 24.98 | 4.00 | 21.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], CIA Created[26], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], One Small Step[81], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Mexico, Argentina | 37.45 | 6.00 | 38.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:6.40 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Mexico, Argentina, Chile | 34.10 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | One Small Step COUP Mexico | 32.00 | 4.00 | 28.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Nasser COUP Mexico | 25.65 | 4.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | One Small Step COUP Iran | 25.25 | 4.00 | 21.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], De Gaulle Leads France[17], Kitchen Debates[51], South African Unrest[56], U2 Incident[63], Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Guatemala | 37.90 | 4.00 | 34.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets INFLUENCE Algeria, South Africa | 37.30 | 6.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:6.40 |
| 3 | De Gaulle Leads France INFLUENCE Algeria, Congo/Zaire, South Africa | 33.35 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | U2 Incident INFLUENCE Algeria, Congo/Zaire, South Africa | 33.35 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Kitchen Debates COUP Guatemala | 31.55 | 4.00 | 27.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 51: T4 AR4 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], CIA Created[26], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Guatemala | 31.95 | 4.00 | 28.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Brazil, Chile | 26.75 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Ask Not What Your Country Can Do For You COUP Guatemala | 24.65 | 4.00 | 41.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Guatemala | 22.30 | 4.00 | 34.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Guatemala | 22.30 | 4.00 | 34.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 52: T4 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], De Gaulle Leads France[17], Kitchen Debates[51], South African Unrest[56], U2 Incident[63]`
- state: `VP 1, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Algeria, Congo/Zaire, South Africa | 35.75 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | U2 Incident INFLUENCE Algeria, Congo/Zaire, South Africa | 35.75 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | South African Unrest INFLUENCE Algeria, South Africa | 23.70 | 6.00 | 38.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Kitchen Debates INFLUENCE South Africa | 23.65 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Kitchen Debates COUP Mexico | 20.05 | 4.00 | 16.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Brazil, Chile | 26.75 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Ask Not What Your Country Can Do For You COUP Guatemala | 24.65 | 4.00 | 41.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP Guatemala | 22.30 | 4.00 | 34.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Guatemala | 22.30 | 4.00 | 34.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Guatemala | 19.95 | 4.00 | 28.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Kitchen Debates[51], South African Unrest[56], U2 Incident[63]`
- state: `VP 1, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE Algeria, Congo/Zaire, Morocco | 35.42 | 6.00 | 55.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | South African Unrest INFLUENCE Algeria, Congo/Zaire | 22.77 | 6.00 | 38.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Kitchen Debates COUP Mexico | 20.38 | 4.00 | 16.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 4 | Kitchen Debates INFLUENCE Algeria | 19.72 | 6.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 5 | Kitchen Debates COUP Iran | 18.63 | 4.00 | 14.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Lonely Hearts Club Band[65], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Guatemala | 23.30 | 4.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Guatemala | 23.30 | 4.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Guatemala | 20.95 | 4.00 | 29.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Algeria | 16.65 | 4.00 | 28.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Algeria | 16.65 | 4.00 | 28.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 56: T4 AR6 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:2`
- hand: `Blockade[10], Kitchen Debates[51], South African Unrest[56]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Guatemala | 31.95 | 4.00 | 28.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | South African Unrest COUP Guatemala | 22.30 | 4.00 | 34.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Kitchen Debates COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Blockade COUP Guatemala | 19.95 | 4.00 | 28.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Kitchen Debates COUP Iran | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Algeria | 17.65 | 4.00 | 29.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | CIA Created COUP Algeria | 15.30 | 4.00 | 23.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Mexico | 13.40 | 4.00 | 25.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Iran | 11.65 | 4.00 | 23.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | CIA Created COUP Mexico | 11.05 | 4.00 | 19.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `South African Unrest [56] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], South African Unrest[56]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Guatemala | 24.30 | 4.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Blockade COUP Guatemala | 21.95 | 4.00 | 30.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | South African Unrest COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Cameroon | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Mozambique | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Decolonization [30] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Decolonization[30], The Cambridge Five[36], How I Learned to Stop Worrying[49], Flower Power[62], John Paul II Elected Pope[69], Sadat Expels Soviets[73]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Captured Nazi Scientist[18], We Will Bury You[53], ABM Treaty[60], Cultural Revolution[61], Camp David Accords[66], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | We Will Bury You EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], The Cambridge Five[36], How I Learned to Stop Worrying[49], Flower Power[62], John Paul II Elected Pope[69], Sadat Expels Soviets[73]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Brazil, Chile | 40.99 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 2 | How I Learned to Stop Worrying INFLUENCE Brazil, Chile | 40.99 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 3 | Flower Power INFLUENCE Brazil, Chile | 40.99 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 4 | The Cambridge Five COUP Indonesia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:3.5 |
| 5 | How I Learned to Stop Worrying COUP Indonesia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Captured Nazi Scientist[18], We Will Bury You[53], Cultural Revolution[61], Camp David Accords[66], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE West Germany, Algeria, South Africa, Philippines | 42.54 | 6.00 | 66.85 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, influence:Philippines:12.70, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 2 | Camp David Accords COUP Indonesia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:3.5 |
| 3 | Camp David Accords COUP Algeria | 37.08 | 4.00 | 33.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:1.5 |
| 4 | Captured Nazi Scientist COUP Indonesia | 34.63 | 4.00 | 30.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:2.5 |
| 5 | OAS Founded COUP Indonesia | 34.63 | 4.00 | 30.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], How I Learned to Stop Worrying[49], Flower Power[62], John Paul II Elected Pope[69], Sadat Expels Soviets[73]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Indonesia | 41.22 | 4.00 | 37.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.83, expected_swing:3.5 |
| 2 | Flower Power COUP Indonesia | 41.22 | 4.00 | 37.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.83, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP Libya | 36.32 | 4.00 | 32.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:1.5 |
| 4 | Flower Power COUP Libya | 36.32 | 4.00 | 32.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:1.5 |
| 5 | How I Learned to Stop Worrying INFLUENCE Chile, Algeria | 35.03 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 64: T5 AR2 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Captured Nazi Scientist[18], Cultural Revolution[61], Camp David Accords[66], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE West Germany, South Africa | 31.98 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 2 | Socialist Governments INFLUENCE West Germany, Angola, South Africa | 27.43 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 3 | Cultural Revolution INFLUENCE West Germany, Angola, South Africa | 27.43 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | Che INFLUENCE West Germany, Angola, South Africa | 27.43 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Camp David Accords COUP Mexico | 27.07 | 4.00 | 23.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Flower Power[62], John Paul II Elected Pope[69], Sadat Expels Soviets[73]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE Chile, Algeria | 36.90 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 2 | Five Year Plan INFLUENCE Argentina, Chile, Algeria | 32.95 | 6.00 | 52.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Sadat Expels Soviets INFLUENCE Argentina, Chile, Algeria | 32.95 | 6.00 | 52.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Flower Power COUP Libya | 29.85 | 4.00 | 26.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Flower Power COUP Mexico | 26.60 | 4.00 | 22.90 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Captured Nazi Scientist[18], Cultural Revolution[61], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Angola, South Africa | 26.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Cultural Revolution INFLUENCE West Germany, Angola, South Africa | 26.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Che INFLUENCE West Germany, Angola, South Africa | 26.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Captured Nazi Scientist COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | OAS Founded COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], John Paul II Elected Pope[69], Sadat Expels Soviets[73]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Argentina, Chile, Venezuela | 28.75 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Sadat Expels Soviets INFLUENCE Argentina, Chile, Venezuela | 28.75 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Captured Nazi Scientist COUP Libya | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Mexico | 20.55 | 4.00 | 16.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Algeria | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Cultural Revolution[61], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE West Germany, Angola, South Africa | 24.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Che INFLUENCE West Germany, Angola, South Africa | 24.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Captured Nazi Scientist COUP Mexico | 21.55 | 4.00 | 17.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:0.5 |
| 4 | OAS Founded COUP Mexico | 21.55 | 4.00 | 17.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Algeria | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Captured Nazi Scientist[18], John Paul II Elected Pope[69], Sadat Expels Soviets[73]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE Argentina, Chile, Venezuela | 29.75 | 6.00 | 52.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Captured Nazi Scientist COUP Libya | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Algeria | 20.30 | 4.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Iran | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Mexico | 22.38 | 4.00 | 18.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |
| 2 | OAS Founded COUP Mexico | 22.38 | 4.00 | 18.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Algeria | 21.63 | 4.00 | 17.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |
| 4 | OAS Founded COUP Algeria | 21.63 | 4.00 | 17.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |
| 5 | Che INFLUENCE West Germany, Angola, South Africa | 20.77 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 71: T5 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | John Paul II Elected Pope COUP Colombia | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:4`
- hand: `OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | OAS Founded COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | OAS Founded COUP Mozambique | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP Bolivia | -2.85 | 4.00 | 9.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope COUP Ecuador | -2.85 | 4.00 | 9.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Ecuador, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Che [83] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Colombia | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Che COUP Cameroon | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Che COUP Mozambique | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Che COUP Saharan States | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-1`

## Step 75: T6 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Fidel[8], Olympic Games[20], Decolonization[30], Red Scare/Purge[31], Cuban Missile Crisis[43], Summit[48], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Indo-Pakistani War[24], Quagmire[45], SALT Negotiations[46], Willy Brandt[58], OPEC[64], Latin American Death Squads[70], Liberation Theology[76], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Quagmire EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Fidel[8], Olympic Games[20], Decolonization[30], Cuban Missile Crisis[43], Summit[48], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Mexico, Panama, Chile | 49.39 | 6.00 | 50.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, non_coup_milops_penalty:6.86 |
| 2 | Cuban Missile Crisis INFLUENCE Mexico, Panama, Chile | 49.39 | 6.00 | 50.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, non_coup_milops_penalty:6.86 |
| 3 | Summit INFLUENCE Mexico, Panama, Chile | 49.39 | 6.00 | 50.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, non_coup_milops_penalty:6.86 |
| 4 | Socialist Governments COUP Mexico | 44.46 | 4.00 | 40.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |
| 5 | Socialist Governments COUP Panama | 44.46 | 4.00 | 40.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Panama, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Indo-Pakistani War[24], Quagmire[45], South African Unrest[56], Willy Brandt[58], OPEC[64], Latin American Death Squads[70], Liberation Theology[76], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Indonesia | 46.26 | 4.00 | 42.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Indonesia | 46.26 | 4.00 | 42.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 3 | Panama Canal Returned COUP Indonesia | 39.91 | 4.00 | 36.06 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |
| 4 | Indo-Pakistani War COUP Colombia | 39.26 | 4.00 | 35.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Colombia | 39.26 | 4.00 | 35.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 79: T6 AR2 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Olympic Games[20], Decolonization[30], Cuban Missile Crisis[43], Summit[48], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE West Germany, Argentina, Chile | 46.70 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 2 | Summit INFLUENCE West Germany, Argentina, Chile | 46.70 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 3 | Cuban Missile Crisis COUP Libya | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Summit COUP Libya | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Cuban Missile Crisis COUP Mexico | 33.75 | 4.00 | 30.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Quagmire[45], South African Unrest[56], Willy Brandt[58], OPEC[64], Latin American Death Squads[70], Liberation Theology[76], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Colombia | 38.88 | 4.00 | 35.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Panama Canal Returned COUP Colombia | 32.53 | 4.00 | 28.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 3 | Latin American Death Squads COUP Mexico | 26.73 | 4.00 | 23.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 4 | Latin American Death Squads COUP Panama | 26.73 | 4.00 | 23.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | Latin American Death Squads COUP Algeria | 25.98 | 4.00 | 22.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Olympic Games[20], Decolonization[30], Summit[48], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE West Germany, Argentina, Chile | 45.10 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:9.60 |
| 2 | Summit COUP Libya | 37.40 | 4.00 | 33.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Summit COUP Mexico | 34.15 | 4.00 | 30.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, expected_swing:2.5 |
| 4 | Summit COUP Panama | 34.15 | 4.00 | 30.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Panama, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, expected_swing:2.5 |
| 5 | Summit COUP Algeria | 33.40 | 4.00 | 29.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Quagmire[45], South African Unrest[56], Willy Brandt[58], OPEC[64], Liberation Theology[76], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 32.80 | 4.00 | 28.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:2.5 |
| 2 | Quagmire COUP Colombia | 25.50 | 4.00 | 41.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | OPEC COUP Colombia | 25.50 | 4.00 | 41.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Colombia | 23.15 | 4.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Colombia | 23.15 | 4.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Olympic Games[20], Decolonization[30], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Libya | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Olympic Games COUP Libya | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Decolonization COUP Libya | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Fidel COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | Fidel COUP Panama | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 84: T6 AR4 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], Quagmire[45], South African Unrest[56], Willy Brandt[58], OPEC[64], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE West Germany, South Africa | 10.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | OPEC INFLUENCE West Germany, South Africa | 10.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Quagmire COUP Colombia | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP Cameroon | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Mozambique | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Olympic Games[20], Decolonization[30], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Argentina, Chile | 28.03 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:10.67 |
| 2 | Decolonization INFLUENCE Argentina, Chile | 28.03 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:10.67 |
| 3 | Olympic Games COUP Colombia | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Olympic Games COUP Saharan States | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Olympic Games COUP Sudan | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], South African Unrest[56], Willy Brandt[58], OPEC[64], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE West Germany, South Africa | 7.83 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | OPEC COUP Colombia | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | OPEC COUP Cameroon | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | OPEC COUP Mozambique | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | OPEC COUP Saharan States | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Decolonization[30], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Colombia | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Decolonization COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Decolonization COUP Sudan | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Decolonization COUP Guatemala | 20.30 | 4.00 | 16.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Allende COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | South African Unrest COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Cameroon | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Colombia | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Allende COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman COUP Colombia | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `South African Unrest [56] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `South African Unrest[56], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Cameroon | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Mozambique | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], Romanian Abdication[12], Warsaw Pact Formed[16], Truman Doctrine[19], Marshall Plan[23], UN Intervention[32], Voice of America[75], Alliance for Progress[79]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], Independent Reds[22], Indo-Pakistani War[24], Nuclear Test Ban[34], Junta[50], Brezhnev Doctrine[54], Muslim Revolution[59], Shuttle Diplomacy[74]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Duck and Cover[4], Romanian Abdication[12], Truman Doctrine[19], Marshall Plan[23], UN Intervention[32], Voice of America[75], Alliance for Progress[79]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE France, West Germany, Argentina, Chile | 43.10 | 6.00 | 69.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Romanian Abdication COUP Indonesia | 40.20 | 4.00 | 36.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Indonesia | 40.20 | 4.00 | 36.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Marshall Plan COUP Indonesia | 35.25 | 4.00 | 55.85 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 5 | Duck and Cover COUP Indonesia | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], Independent Reds[22], Indo-Pakistani War[24], Junta[50], Brezhnev Doctrine[54], Muslim Revolution[59], Shuttle Diplomacy[74]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, South Africa | 48.05 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Shuttle Diplomacy COUP Colombia | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Shuttle Diplomacy COUP Italy | 39.75 | 4.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |
| 4 | Shuttle Diplomacy COUP Mexico | 39.75 | 4.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |
| 5 | Shuttle Diplomacy COUP Panama | 39.75 | 4.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Panama, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], Romanian Abdication[12], Truman Doctrine[19], UN Intervention[32], Voice of America[75], Alliance for Progress[79]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Indonesia | 40.53 | 4.00 | 36.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Indonesia | 40.53 | 4.00 | 36.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 3 | Duck and Cover COUP Indonesia | 33.23 | 4.00 | 49.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Indonesia | 33.23 | 4.00 | 49.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Voice of America COUP Indonesia | 30.88 | 4.00 | 43.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 96: T7 AR2 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], Independent Reds[22], Indo-Pakistani War[24], Junta[50], Brezhnev Doctrine[54], Muslim Revolution[59]`
- state: `VP -1, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Colombia | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | Indo-Pakistani War COUP Colombia | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 3 | Junta COUP Colombia | 39.88 | 4.00 | 36.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 4 | Muslim Revolution INFLUENCE East Germany, West Germany, Angola, South Africa | 36.17 | 6.00 | 64.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Independent Reds COUP Mexico | 33.73 | 4.00 | 30.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 97: T7 AR3 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Truman Doctrine[19], UN Intervention[32], Voice of America[75], Alliance for Progress[79]`
- state: `VP -1, DEFCON 4, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Indonesia | 40.60 | 4.00 | 36.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Colombia | 33.60 | 4.00 | 29.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 3 | Duck and Cover COUP Indonesia | 33.30 | 4.00 | 49.75 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Indonesia | 33.30 | 4.00 | 49.75 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Voice of America COUP Indonesia | 30.95 | 4.00 | 43.25 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], Indo-Pakistani War[24], Junta[50], Brezhnev Doctrine[54], Muslim Revolution[59]`
- state: `VP -1, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE West Germany, Brazil, Venezuela, South Africa | 38.75 | 6.00 | 65.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Indo-Pakistani War COUP Brazil | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Indo-Pakistani War COUP Venezuela | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Venezuela, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Junta COUP Brazil | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Junta COUP Venezuela | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Venezuela, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Duck and Cover[4], Truman Doctrine[19], Voice of America[75], Alliance for Progress[79]`
- state: `VP -1, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Brazil, Chile, Venezuela | 28.75 | 6.00 | 55.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Alliance for Progress INFLUENCE Brazil, Chile, Venezuela | 28.75 | 6.00 | 55.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Duck and Cover COUP Colombia | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Colombia | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Voice of America COUP Colombia | 24.55 | 4.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:5`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], Indo-Pakistani War[24], Junta[50], Brezhnev Doctrine[54]`
- state: `VP -1, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Argentina | 34.15 | 4.00 | 30.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Junta COUP Argentina | 34.15 | 4.00 | 30.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Indo-Pakistani War INFLUENCE Argentina, South Africa | 30.70 | 6.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 4 | Junta INFLUENCE Argentina, South Africa | 30.70 | 6.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 5 | Indo-Pakistani War COUP Peru | 29.65 | 4.00 | 25.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Voice of America[75], Alliance for Progress[79]`
- state: `VP -1, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Colombia | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Voice of America COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Colombia | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Alliance for Progress INFLUENCE West Germany, Argentina, Chile | 18.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Alliance for Progress COUP Saharan States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 102: T7 AR5 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:5`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], Junta[50], Brezhnev Doctrine[54]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Colombia | 40.88 | 4.00 | 37.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Peru | 30.48 | 4.00 | 26.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:1.5 |
| 3 | Junta INFLUENCE Argentina, South Africa | 27.37 | 6.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:13.33 |
| 4 | Warsaw Pact Formed COUP Colombia | 27.23 | 4.00 | 43.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Brezhnev Doctrine COUP Colombia | 27.23 | 4.00 | 43.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Voice of America [75] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], Voice of America[75]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Colombia | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Voice of America COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Voice of America COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Voice of America COUP Guatemala | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Warsaw Pact Formed [16] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], Brezhnev Doctrine[54]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed COUP Colombia | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Brezhnev Doctrine COUP Colombia | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Colombia | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Warsaw Pact Formed COUP Peru | 18.50 | 4.00 | 34.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Peru, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Brezhnev Doctrine COUP Peru | 18.50 | 4.00 | 34.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Peru, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 105: T7 AR7 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Colombia | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Saharan States | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Sudan | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Guatemala | 5.95 | 4.00 | 14.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Bolivia | -3.20 | 4.00 | 4.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Bolivia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Brezhnev Doctrine [54] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Brezhnev Doctrine[54]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine COUP Peru | 21.50 | 4.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Peru, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Peru | 16.80 | 4.00 | 24.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Peru, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Brezhnev Doctrine COUP Colombia | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Brezhnev Doctrine COUP Cameroon | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Brezhnev Doctrine COUP Mozambique | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 107: T8 AR0 USSR

- chosen: `Fidel [8] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Fidel[8], Nasser[15], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], Voice of America[75], Liberation Theology[76], Reagan Bombs Libya[87], Chernobyl[97], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Chernobyl EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Duck and Cover[4], Romanian Abdication[12], Independent Reds[22], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Flower Power[62], Voice of America[75], North Sea Oil[89]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Nasser[15], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], Voice of America[75], Liberation Theology[76], Reagan Bombs Libya[87], Chernobyl[97], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Colombia | 39.34 | 4.00 | 35.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 2 | Liberation Theology COUP Colombia | 39.34 | 4.00 | 35.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 3 | Nasser COUP Colombia | 32.99 | 4.00 | 29.14 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:2.5 |
| 4 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | Liberation Theology INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 110: T8 AR1 US

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Romanian Abdication[12], Independent Reds[22], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Flower Power[62], Voice of America[75], North Sea Oil[89]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | North Sea Oil COUP Colombia | 45.69 | 4.00 | 42.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 3 | Independent Reds COUP Colombia | 39.34 | 4.00 | 35.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 4 | How I Learned to Stop Worrying COUP Colombia | 39.34 | 4.00 | 35.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 5 | Voice of America COUP Colombia | 39.34 | 4.00 | 35.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Lonely Hearts Club Band[65], Voice of America[75], Liberation Theology[76], Reagan Bombs Libya[87], Chernobyl[97], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE France, West Germany | 35.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Chernobyl INFLUENCE East Germany, France, West Germany | 32.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Lonely Hearts Club Band INFLUENCE France, West Germany | 19.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Voice of America INFLUENCE France, West Germany | 19.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Reagan Bombs Libya INFLUENCE France, West Germany | 19.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:8`
- hand: `Romanian Abdication[12], Independent Reds[22], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Flower Power[62], Voice of America[75]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Colombia | 39.72 | 4.00 | 36.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Colombia | 39.72 | 4.00 | 36.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | Voice of America COUP Colombia | 39.72 | 4.00 | 36.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 4 | Independent Reds COUP Peru | 29.32 | 4.00 | 25.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:1.5 |
| 5 | How I Learned to Stop Worrying COUP Peru | 29.32 | 4.00 | 25.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 113: T8 AR3 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Lonely Hearts Club Band[65], Voice of America[75], Reagan Bombs Libya[87], Chernobyl[97], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Colombia | 33.10 | 4.00 | 29.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 2 | Chernobyl INFLUENCE East Germany, France, West Germany | 30.45 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | Chernobyl COUP Colombia | 25.80 | 4.00 | 42.25 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Colombia | 23.45 | 4.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Voice of America COUP Colombia | 23.45 | 4.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Flower Power[62], Voice of America[75]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 29.30 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | 29.30 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | How I Learned to Stop Worrying COUP Peru | 29.05 | 4.00 | 25.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 4 | Voice of America COUP Peru | 29.05 | 4.00 | 25.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 25.45 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], Voice of America[75], Reagan Bombs Libya[87], Chernobyl[97], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, France, West Germany | 23.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Voice of America INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Chernobyl COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Voice of America [75] as COUP`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Flower Power[62], Voice of America[75]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Peru | 29.65 | 4.00 | 25.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:1.5 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 23.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Voice of America COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Voice of America COUP Mozambique | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], Voice of America[75], Reagan Bombs Libya[87], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Peru | 14.65 | 4.00 | 26.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Voice of America COUP Peru | 14.65 | 4.00 | 26.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Peru | 14.65 | 4.00 | 26.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Peru | 12.30 | 4.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Flower Power[62]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, South Korea | 21.30 | 6.00 | 51.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:South Korea:13.55, control_break:South Korea, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Korea | 9.15 | 6.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:South Korea:13.55, control_break:South Korea, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Flower Power INFLUENCE West Germany, South Korea | 9.15 | 6.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:South Korea:13.55, control_break:South Korea, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Brezhnev Doctrine COUP Cameroon | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Brezhnev Doctrine COUP Mozambique | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Voice of America [75] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Voice of America[75], Reagan Bombs Libya[87], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Peru | 16.65 | 4.00 | 28.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Reagan Bombs Libya COUP Peru | 16.65 | 4.00 | 28.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Peru | 14.30 | 4.00 | 22.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Voice of America COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Voice of America COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Portuguese Empire Crumbles[55], Flower Power[62]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Portuguese Empire Crumbles COUP Mozambique | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Reagan Bombs Libya [87] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Reagan Bombs Libya[87], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya COUP Peru | 22.65 | 4.00 | 34.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Panama Canal Returned COUP Peru | 20.30 | 4.00 | 28.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Reagan Bombs Libya COUP Colombia | 13.05 | 4.00 | 25.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Flower Power[62]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Peru | 22.65 | 4.00 | 34.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Peru | 20.30 | 4.00 | 28.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Flower Power COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Mozambique | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 123: T9 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Truman Doctrine[19], Decolonization[30], Red Scare/Purge[31], Junta[50], ABM Treaty[60], Grain Sales to Soviets[68], Terrorism[95], Wargames[103]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Marshall Plan[23], Arms Race[42], Nuclear Subs[44], Junta[50], Flower Power[62], Grain Sales to Soviets[68], Alliance for Progress[79], One Small Step[81]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Truman Doctrine[19], Decolonization[30], Junta[50], ABM Treaty[60], Grain Sales to Soviets[68], Terrorism[95], Wargames[103]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, Italy, West Germany | 60.31 | 6.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | Wargames INFLUENCE East Germany, France, Italy, West Germany | 60.31 | 6.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | ABM Treaty COUP Algeria | 39.92 | 4.00 | 36.52 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:3.5 |
| 4 | Wargames COUP Algeria | 39.92 | 4.00 | 36.52 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:3.5 |
| 5 | ABM Treaty COUP Brazil | 39.42 | 4.00 | 36.02 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Arms Race [42] as COUP`
- flags: `milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Arms Race[42], Nuclear Subs[44], Junta[50], Flower Power[62], Grain Sales to Soviets[68], Alliance for Progress[79], One Small Step[81]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race COUP Argentina | 38.07 | 4.00 | 34.52 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | Alliance for Progress COUP Argentina | 38.07 | 4.00 | 34.52 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Arms Race COUP Peru | 35.57 | 4.00 | 32.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Peru, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |
| 4 | Alliance for Progress COUP Peru | 35.57 | 4.00 | 32.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Peru, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |
| 5 | Arms Race COUP Algeria | 33.57 | 4.00 | 30.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 127: T9 AR2 USSR

- chosen: `Wargames [103] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Truman Doctrine[19], Decolonization[30], Junta[50], Grain Sales to Soviets[68], Terrorism[95], Wargames[103]`
- state: `VP -3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames INFLUENCE East Germany, France, Italy, West Germany | 63.60 | 6.00 | 70.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Wargames COUP Saharan States | 33.25 | 4.00 | 29.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, empty_coup_penalty, expected_swing:5.5 |
| 3 | Wargames COUP Sudan | 33.25 | 4.00 | 29.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Sudan, milops_need:9, milops_urgency:1.50, empty_coup_penalty, expected_swing:5.5 |
| 4 | Wargames COUP Colombia | 32.75 | 4.00 | 29.35 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.50, empty_coup_penalty, expected_swing:5.5 |
| 5 | Wargames COUP Guatemala | 32.50 | 4.00 | 29.10 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:1.50, empty_coup_penalty, expected_swing:5.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Nuclear Subs[44], Junta[50], Flower Power[62], Grain Sales to Soviets[68], Alliance for Progress[79], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE Italy, Nigeria | 38.85 | 6.00 | 41.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 2 | Alliance for Progress COUP Peru | 35.00 | 4.00 | 31.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Nuclear Subs COUP Peru | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 4 | Junta COUP Peru | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 5 | Grain Sales to Soviets COUP Peru | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Truman Doctrine[19], Decolonization[30], Junta[50], Grain Sales to Soviets[68], Terrorism[95]`
- state: `VP -3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 24.50 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Junta INFLUENCE East Germany, West Germany | 24.50 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 3 | Terrorism INFLUENCE East Germany, West Germany | 24.50 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 4 | Decolonization COUP Saharan States | 21.15 | 4.00 | 17.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, empty_coup_penalty, expected_swing:3.5 |
| 5 | Decolonization COUP Sudan | 21.15 | 4.00 | 17.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:9, milops_urgency:1.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Nuclear Subs[44], Junta[50], Flower Power[62], Grain Sales to Soviets[68], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Peru | 29.05 | 4.00 | 25.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 2 | Junta COUP Peru | 29.05 | 4.00 | 25.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 3 | Grain Sales to Soviets COUP Peru | 29.05 | 4.00 | 25.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 4 | One Small Step COUP Peru | 29.05 | 4.00 | 25.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 5 | Captured Nazi Scientist COUP Peru | 22.70 | 4.00 | 18.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Peru, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Junta [50] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Truman Doctrine[19], Junta[50], Grain Sales to Soviets[68], Terrorism[95]`
- state: `VP -3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 2 | Junta COUP Sudan | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 3 | Terrorism COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 4 | Terrorism COUP Sudan | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | Junta COUP Colombia | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:2.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 132: T9 AR4 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Junta[50], Flower Power[62], Grain Sales to Soviets[68], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Saharan States | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Saharan States | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | One Small Step COUP Saharan States | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Saharan States | 34.20 | 4.00 | 30.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 5 | Flower Power COUP Saharan States | 24.55 | 4.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Terrorism [95] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Truman Doctrine[19], Grain Sales to Soviets[68], Terrorism[95]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Terrorism COUP Saharan States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Terrorism COUP Sudan | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Terrorism COUP Colombia | 21.72 | 4.00 | 18.02 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Terrorism COUP Guatemala | 21.47 | 4.00 | 17.77 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Terrorism COUP Haiti | 21.47 | 4.00 | 17.77 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Flower Power[62], Grain Sales to Soviets[68], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Captured Nazi Scientist COUP Saharan States | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 4 | Flower Power COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Cameroon | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Truman Doctrine[19], Grain Sales to Soviets[68]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Sudan | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP Colombia | 17.70 | 4.00 | 13.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Blockade COUP Guatemala | 17.45 | 4.00 | 13.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade COUP Haiti | 17.45 | 4.00 | 13.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Flower Power[62], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 3 | Flower Power COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | One Small Step COUP Cameroon | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Mozambique | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Sudan | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP Colombia | 15.05 | 4.00 | 27.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Guatemala | 14.80 | 4.00 | 27.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Flower Power[62]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5 |
| 2 | Flower Power COUP Saharan States | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Captured Nazi Scientist COUP Cameroon | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Mozambique | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP SE African States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 139: T10 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Five Year Plan[5], Socialist Governments[7], De Gaulle Leads France[17], UN Intervention[32], Summit[48], Puppet Governments[67], OAS Founded[71], Che[83], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], NATO[21], Independent Reds[22], We Will Bury You[53], Puppet Governments[67], Latin American Death Squads[70], Ussuri River Skirmish[77], Soviets Shoot Down KAL 007[92], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], UN Intervention[32], Summit[48], Puppet Governments[67], OAS Founded[71], Che[83], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Nigeria | 49.26 | 4.00 | 45.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | Summit COUP Nigeria | 49.26 | 4.00 | 45.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 3 | Che COUP Nigeria | 49.26 | 4.00 | 45.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 4 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Summit INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `Soviets Shoot Down KAL 007 [92] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], Independent Reds[22], We Will Bury You[53], Puppet Governments[67], Latin American Death Squads[70], Ussuri River Skirmish[77], Soviets Shoot Down KAL 007[92], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, France, Poland, West Germany | 59.77 | 6.00 | 65.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Soviets Shoot Down KAL 007 COUP Saharan States | 53.11 | 4.00 | 49.71 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 3 | Ussuri River Skirmish COUP Saharan States | 46.76 | 4.00 | 43.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Independent Reds COUP Saharan States | 40.41 | 4.00 | 36.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], UN Intervention[32], Summit[48], Puppet Governments[67], OAS Founded[71], Che[83], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, West Germany, Iran | 52.37 | 6.00 | 56.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, non_coup_milops_penalty:9.33 |
| 2 | Che INFLUENCE East Germany, West Germany, Iran | 52.37 | 6.00 | 56.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, non_coup_milops_penalty:9.33 |
| 3 | Summit COUP Cameroon | 46.23 | 4.00 | 42.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 4 | Che COUP Cameroon | 46.23 | 4.00 | 42.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 5 | UN Intervention COUP Cameroon | 33.53 | 4.00 | 29.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Ussuri River Skirmish [77] as COUP`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], Independent Reds[22], We Will Bury You[53], Puppet Governments[67], Latin American Death Squads[70], Ussuri River Skirmish[77], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish COUP Saharan States | 47.23 | 4.00 | 43.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:4.5 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Independent Reds COUP Saharan States | 40.88 | 4.00 | 37.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 4 | Puppet Governments COUP Saharan States | 40.88 | 4.00 | 37.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Saharan States | 40.88 | 4.00 | 37.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 145: T10 AR3 USSR

- chosen: `Che [83] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], UN Intervention[32], Puppet Governments[67], OAS Founded[71], Che[83], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Cameroon | 46.70 | 4.00 | 43.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5 |
| 2 | Che COUP Saharan States | 46.70 | 4.00 | 43.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5 |
| 3 | Che INFLUENCE East Germany, West Germany, Brazil | 46.25 | 6.00 | 51.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Brazil:13.70, control_break:Brazil, non_coup_milops_penalty:11.20 |
| 4 | UN Intervention COUP Cameroon | 34.00 | 4.00 | 30.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 34.00 | 4.00 | 30.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Independent Reds[22], We Will Bury You[53], Puppet Governments[67], Latin American Death Squads[70], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, West Germany, Cuba | 35.75 | 6.00 | 65.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 2 | Independent Reds INFLUENCE East Germany, West Germany | 27.70 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 27.70 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 4 | Latin American Death Squads INFLUENCE East Germany, West Germany | 27.70 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 5 | Iran-Iraq War INFLUENCE East Germany, West Germany | 27.70 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], UN Intervention[32], Puppet Governments[67], OAS Founded[71], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Cameroon | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 3 | Five Year Plan INFLUENCE East Germany, Cuba, Brazil | 30.60 | 6.00 | 59.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Cuba:14.05, control_break:Cuba, influence:Brazil:13.70, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Tear Down this Wall INFLUENCE East Germany, Cuba, Brazil | 30.60 | 6.00 | 59.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Cuba:14.05, control_break:Cuba, influence:Brazil:13.70, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Five Year Plan COUP Cameroon | 27.40 | 4.00 | 43.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Independent Reds[22], Puppet Governments[67], Latin American Death Squads[70], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | 24.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 2 | Puppet Governments INFLUENCE East Germany, West Germany | 24.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 24.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 4 | Iran-Iraq War INFLUENCE East Germany, West Germany | 24.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 5 | Independent Reds COUP Cameroon | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Five Year Plan [5] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Five Year Plan[5], Puppet Governments[67], OAS Founded[71], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan COUP Saharan States | 28.57 | 4.00 | 45.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Tear Down this Wall COUP Saharan States | 28.57 | 4.00 | 45.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Saharan States | 26.22 | 4.00 | 38.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | OAS Founded COUP Saharan States | 23.87 | 4.00 | 32.02 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Five Year Plan INFLUENCE West Germany, Cuba, Brazil | 21.53 | 6.00 | 54.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, control_break:Cuba, influence:Brazil:13.70, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Puppet Governments[67], Latin American Death Squads[70], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Cameroon | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Puppet Governments COUP Mozambique | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Puppet Governments COUP Saharan States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Puppet Governments COUP SE African States | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Puppet Governments COUP Sudan | 22.22 | 4.00 | 18.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Tear Down this Wall [99] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Puppet Governments[67], OAS Founded[71], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall COUP Cameroon | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Tear Down this Wall COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | OAS Founded COUP Cameroon | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Latin American Death Squads[70], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Cameroon | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5 |
| 2 | Iran-Iraq War COUP Cameroon | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5 |
| 3 | Nasser COUP Cameroon | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Latin American Death Squads COUP Mozambique | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Puppet Governments[67], OAS Founded[71]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Puppet Governments COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | OAS Founded COUP Cameroon | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | OAS Founded COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Sudan | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Iran-Iraq War [105] as COUP`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War COUP Cameroon | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Iran-Iraq War COUP Mozambique | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Iran-Iraq War COUP Saharan States | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Iran-Iraq War COUP SE African States | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Iran-Iraq War COUP Sudan | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP -3, DEFCON +1, MilOps U-3/A-3`
