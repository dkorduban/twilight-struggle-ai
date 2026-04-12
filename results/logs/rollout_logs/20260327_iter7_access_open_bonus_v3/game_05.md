# minimal_hybrid detailed rollout log

- seed: `20260524`
- winner: `USSR`
- final_vp: `7`
- end_turn: `7`
- end_reason: `europe_control`

## Step 1: T1 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Arab-Israeli War[13], COMECON[14], Captured Nazi Scientist[18], Marshall Plan[23], US/Japan Mutual Defense Pact[27], Suez Crisis[28], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17], Olympic Games[20], Independent Reds[22], Red Scare/Purge[31], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Captured Nazi Scientist[18], Marshall Plan[23], US/Japan Mutual Defense Pact[27], Suez Crisis[28], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Iran | 76.83 | 4.00 | 73.28 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Arab-Israeli War COUP Iran | 71.48 | 4.00 | 67.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Captured Nazi Scientist COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Marshall Plan COUP Iran | 58.18 | 4.00 | 78.78 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | US/Japan Mutual Defense Pact COUP Iran | 58.18 | 4.00 | 78.78 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17], Olympic Games[20], Independent Reds[22], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Independent Reds INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Special Relationship INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 4 | De Gaulle Leads France INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Olympic Games COUP North Korea | 30.08 | 4.00 | 26.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Captured Nazi Scientist[18], Marshall Plan[23], US/Japan Mutual Defense Pact[27], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Marshall Plan INFLUENCE West Germany, Japan, Thailand | 39.65 | 6.00 | 58.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Thailand | 39.65 | 6.00 | 58.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Philippines | 35.90 | 4.00 | 32.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17], Independent Reds[22], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Turkey, North Korea | 39.10 | 6.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.60 |
| 2 | Special Relationship INFLUENCE Turkey, North Korea | 39.10 | 6.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.60 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, Turkey, North Korea | 36.00 | 6.00 | 52.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Independent Reds COUP Syria | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 5 | Special Relationship COUP Syria | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Marshall Plan[23], US/Japan Mutual Defense Pact[27], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, North Korea, Thailand | 42.55 | 6.00 | 61.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | US/Japan Mutual Defense Pact INFLUENCE Japan, North Korea, Thailand | 42.55 | 6.00 | 61.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Five Year Plan INFLUENCE North Korea, Thailand | 28.55 | 6.00 | 43.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 28.30 | 6.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 5 | Formosan Resolution INFLUENCE Thailand | 12.15 | 6.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, France | 37.80 | 6.00 | 34.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, non_coup_milops_penalty:2.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, France, Panama | 33.85 | 6.00 | 50.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Special Relationship COUP Syria | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 4 | Fidel INFLUENCE East Germany, France | 21.80 | 6.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Vietnam Revolts INFLUENCE East Germany, France | 21.80 | 6.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], US/Japan Mutual Defense Pact[27], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE West Germany, South Korea, Thailand | 42.05 | 6.00 | 60.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 3 | Five Year Plan INFLUENCE West Germany, Thailand | 28.65 | 6.00 | 43.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Formosan Resolution INFLUENCE Thailand | 15.15 | 6.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, West Germany, Panama | 36.18 | 6.00 | 53.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, control_break:West Germany, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Fidel INFLUENCE Italy, West Germany | 24.13 | 6.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Vietnam Revolts INFLUENCE Italy, West Germany | 24.13 | 6.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | De Gaulle Leads France COUP Syria | 13.67 | 4.00 | 30.12 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Fidel COUP Syria | 12.32 | 4.00 | 24.62 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Five Year Plan INFLUENCE Pakistan, Thailand | 22.95 | 6.00 | 37.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE Thailand | 10.15 | 6.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Italy, Japan | 18.30 | 6.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Vietnam Revolts INFLUENCE Italy, Japan | 18.30 | 6.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Fidel COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Blockade COUP Syria | 11.30 | 4.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Pakistan, Thailand | 22.95 | 6.00 | 37.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Thailand | 10.15 | 6.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Five Year Plan SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Five Year Plan COUP Lebanon | 0.40 | 4.00 | 16.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Syria | 13.65 | 4.00 | 25.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Blockade COUP Syria | 12.30 | 4.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Vietnam Revolts INFLUENCE Japan, Egypt | 10.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 4 | Vietnam Revolts COUP Lebanon | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP Lebanon | 0.70 | 4.00 | 8.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-3/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Containment[25], CIA Created[26], East European Unrest[29], De-Stalinization[33], Nuclear Test Ban[34], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Nasser[15], Truman Doctrine[19], NATO[21], Indo-Pakistani War[24], Decolonization[30], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Decolonization EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Containment[25], CIA Created[26], East European Unrest[29], De-Stalinization[33], NORAD[38]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE India, Pakistan, Thailand | 60.83 | 6.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | De-Stalinization INFLUENCE India, Pakistan, Thailand | 60.83 | 6.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Socialist Governments COUP Philippines | 43.92 | 4.00 | 40.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 4 | De-Stalinization COUP Philippines | 43.92 | 4.00 | 40.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 5 | Duck and Cover INFLUENCE India, Pakistan, Thailand | 40.83 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Decolonization[30], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan, Egypt | 34.88 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.67 |
| 2 | Indo-Pakistani War COUP Syria | 29.32 | 4.00 | 25.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 3 | Indo-Pakistani War COUP Poland | 28.92 | 4.00 | 25.22 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Poland, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open |
| 4 | Truman Doctrine COUP Poland | 28.07 | 4.00 | 24.22 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Poland, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open |
| 5 | UN Intervention COUP Poland | 28.07 | 4.00 | 24.22 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Poland, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Containment[25], CIA Created[26], East European Unrest[29], De-Stalinization[33], NORAD[38]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, Israel, Thailand | 56.15 | 6.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | De-Stalinization COUP Philippines | 44.05 | 4.00 | 40.50 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 3 | Duck and Cover INFLUENCE Italy, Israel, Thailand | 36.15 | 6.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Containment INFLUENCE Italy, Israel, Thailand | 36.15 | 6.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | East European Unrest INFLUENCE Italy, Israel, Thailand | 36.15 | 6.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Decolonization[30], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Poland | 28.20 | 4.00 | 24.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Poland, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open |
| 2 | UN Intervention COUP Poland | 28.20 | 4.00 | 24.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Poland, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open |
| 3 | Truman Doctrine COUP Italy | 25.35 | 4.00 | 21.50 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:0.5 |
| 4 | UN Intervention COUP Italy | 25.35 | 4.00 | 21.50 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:0.5 |
| 5 | Decolonization INFLUENCE Italy, Egypt | 24.65 | 6.00 | 38.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 21: T2 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Containment[25], CIA Created[26], East European Unrest[29], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Containment INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | East European Unrest INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | NORAD INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Duck and Cover COUP Philippines | 24.25 | 4.00 | 40.70 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Decolonization[30], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 3, DEFCON 4, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Italy, Philippines | 26.60 | 6.00 | 38.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | The Cambridge Five INFLUENCE Italy, Philippines | 26.60 | 6.00 | 38.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | UN Intervention COUP Philippines | 25.05 | 4.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:1, milops_urgency:0.25, expected_swing:0.5 |
| 4 | UN Intervention COUP Japan | 24.00 | 4.00 | 20.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 5 | UN Intervention COUP North Korea | 23.40 | 4.00 | 19.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Containment [25] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Containment[25], CIA Created[26], East European Unrest[29], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment COUP Indonesia | 34.98 | 4.00 | 51.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | East European Unrest COUP Indonesia | 34.98 | 4.00 | 51.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | NORAD COUP Indonesia | 34.98 | 4.00 | 51.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Containment INFLUENCE Japan, Indonesia, Thailand | 32.67 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | East European Unrest INFLUENCE Japan, Indonesia, Thailand | 32.67 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 24: T2 AR4 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:1`
- hand: `Romanian Abdication[12], Nasser[15], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Syria | 22.97 | 4.00 | 19.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention INFLUENCE Egypt | 21.88 | 6.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:2.67 |
| 3 | The Cambridge Five INFLUENCE Japan, Egypt | 21.88 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | The Cambridge Five COUP Syria | 12.32 | 4.00 | 24.62 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | UN Intervention COUP Lebanon | 11.37 | 4.00 | 7.52 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `CIA Created[26], East European Unrest[29], NORAD[38]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Egypt, Thailand | 37.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE Japan, Egypt, Thailand | 37.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty |
| 3 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | East European Unrest SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | NORAD SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], The Cambridge Five[36]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Indonesia | 14.70 | 6.00 | 32.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | The Cambridge Five COUP Egypt | 8.15 | 4.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Egypt | 6.80 | 4.00 | 14.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 4 | Nasser COUP Egypt | 6.80 | 4.00 | 14.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Israel | 5.25 | 4.00 | 13.40 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `CIA Created[26], NORAD[38]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Indonesia, Thailand | 41.00 | 6.00 | 55.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | NORAD COUP Lebanon | 0.40 | 4.00 | 16.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | NORAD COUP Sudan | -1.85 | 4.00 | 14.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Egypt | 7.80 | 4.00 | 15.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 2 | Nasser COUP Egypt | 7.80 | 4.00 | 15.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Israel | 6.25 | 4.00 | 14.40 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |
| 4 | Nasser COUP Israel | 6.25 | 4.00 | 14.40 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | 0.70 | 4.00 | 8.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +0, MilOps U-3/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Romanian Abdication[12], Nasser[15], US/Japan Mutual Defense Pact[27], Red Scare/Purge[31], De-Stalinization[33], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Korean War[11], De Gaulle Leads France[17], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Japan, Egypt, Thailand | 53.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | De Gaulle Leads France COUP Egypt | 38.50 | 4.00 | 34.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Fidel INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Vietnam Revolts INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Korean War INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Romanian Abdication[12], Nasser[15], Red Scare/Purge[31], De-Stalinization[33], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE West Germany, Japan, North Korea, Libya | 69.45 | 6.00 | 68.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:4.00 |
| 2 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, Libya | 69.45 | 6.00 | 68.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:4.00 |
| 3 | Duck and Cover INFLUENCE West Germany, Japan, Libya | 54.05 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:4.00 |
| 4 | Special Relationship INFLUENCE Japan, Libya | 38.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:4.00 |
| 5 | Red Scare/Purge COUP Egypt | 36.85 | 4.00 | 33.45 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Korean War[11], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE North Korea, Thailand | 41.90 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | Vietnam Revolts INFLUENCE North Korea, Thailand | 41.90 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 3 | Korean War INFLUENCE North Korea, Thailand | 41.90 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 4 | Decolonization INFLUENCE North Korea, Thailand | 41.90 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 5 | The Cambridge Five INFLUENCE North Korea, Thailand | 41.90 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Romanian Abdication[12], Nasser[15], De-Stalinization[33], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, Libya | 66.65 | 6.00 | 66.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.80 |
| 2 | Duck and Cover INFLUENCE West Germany, Japan, Libya | 51.25 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.80 |
| 3 | Nuclear Test Ban COUP Egypt | 37.05 | 4.00 | 33.65 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:3.5 |
| 4 | Special Relationship INFLUENCE Japan, Libya | 35.75 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.80 |
| 5 | Duck and Cover COUP Egypt | 31.70 | 4.00 | 28.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Vietnam Revolts[9], Korean War[11], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE North Korea, Thailand | 40.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | Korean War INFLUENCE North Korea, Thailand | 40.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Decolonization INFLUENCE North Korea, Thailand | 40.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 4 | The Cambridge Five INFLUENCE North Korea, Thailand | 40.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 5 | NORAD INFLUENCE Japan, North Korea, Thailand | 36.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Romanian Abdication[12], Nasser[15], De-Stalinization[33], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan, North Korea | 46.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:6.00 |
| 2 | Duck and Cover COUP Egypt | 32.00 | 4.00 | 28.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:2.5 |
| 3 | Special Relationship INFLUENCE West Germany, Japan | 31.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 4 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 26.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Special Relationship COUP Egypt | 25.65 | 4.00 | 21.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Korean War[11], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE North Korea, Thailand | 38.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 2 | Decolonization INFLUENCE North Korea, Thailand | 38.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 3 | The Cambridge Five INFLUENCE North Korea, Thailand | 38.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 4 | NORAD INFLUENCE Japan, North Korea, Thailand | 34.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Korean War COUP Libya | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Nasser[15], De-Stalinization[33], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, Japan | 29.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:8.00 |
| 2 | Special Relationship COUP Egypt | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 3 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 24.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Special Relationship COUP Israel | 19.10 | 4.00 | 15.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3 |
| 5 | Special Relationship COUP Lebanon | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Libya | 34.15 | 4.00 | 30.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | The Cambridge Five COUP Libya | 34.15 | 4.00 | 30.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Decolonization COUP Egypt | 27.15 | 4.00 | 23.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 4 | The Cambridge Five COUP Egypt | 27.15 | 4.00 | 23.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | Decolonization INFLUENCE Japan, Thailand | 21.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 40: T3 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], De-Stalinization[33]`
- state: `VP 4, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan, Libya | 12.05 | 6.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | De-Stalinization COUP SE African States | 4.15 | 4.00 | 20.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | De-Stalinization COUP Sudan | 4.15 | 4.00 | 20.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | De-Stalinization COUP Zimbabwe | 4.15 | 4.00 | 20.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Colombia | 3.65 | 4.00 | 20.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `The Cambridge Five[36], NORAD[38]`
- state: `VP 4, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Libya, Thailand | 33.85 | 6.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Libya:13.70, control_break:Libya, influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 2 | NORAD INFLUENCE Japan, Libya, Thailand | 29.85 | 6.00 | 55.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | The Cambridge Five COUP Sudan | 15.80 | 4.00 | 12.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Tunisia | 5.40 | 4.00 | 1.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:1.5 |
| 5 | NORAD COUP Sudan | 1.15 | 4.00 | 17.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 4, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP SE African States | 2.45 | 4.00 | 10.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Sudan | 2.45 | 4.00 | 10.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Zimbabwe | 2.45 | 4.00 | 10.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP SE African States | 2.45 | 4.00 | 10.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP Sudan | 2.45 | 4.00 | 10.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-2/A+0`

## Step 43: T4 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], East European Unrest[29], Decolonization[30], Red Scare/Purge[31], De-Stalinization[33], NORAD[38], Willy Brandt[58], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Fidel[8], Formosan Resolution[35], Cuban Missile Crisis[43], Allende[57], Cultural Revolution[61], OPEC[64], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Cultural Revolution EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], East European Unrest[29], Decolonization[30], De-Stalinization[33], NORAD[38], Willy Brandt[58], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE UK, Mexico, Algeria | 50.28 | 6.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 2 | Decolonization INFLUENCE Mexico, Algeria | 34.28 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 3 | Willy Brandt INFLUENCE Mexico, Algeria | 34.28 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 4 | East European Unrest INFLUENCE UK, Mexico, Algeria | 30.28 | 6.00 | 49.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | NORAD INFLUENCE UK, Mexico, Algeria | 30.28 | 6.00 | 49.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Fidel[8], Formosan Resolution[35], Allende[57], Cultural Revolution[61], OPEC[64], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Angola | 23.73 | 6.00 | 22.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 2 | Camp David Accords INFLUENCE Angola | 23.73 | 6.00 | 22.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 3 | One Small Step INFLUENCE Angola | 23.73 | 6.00 | 22.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 4 | Cultural Revolution INFLUENCE UK, Angola | 22.73 | 6.00 | 41.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Angola:15.60, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | OPEC INFLUENCE UK, Angola | 22.73 | 6.00 | 41.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Angola:15.60, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], East European Unrest[29], Decolonization[30], NORAD[38], Willy Brandt[58], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Mexico, Algeria | 39.52 | 6.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 2 | Willy Brandt INFLUENCE Mexico, Algeria | 39.52 | 6.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 3 | East European Unrest INFLUENCE Mexico, Algeria, Morocco | 36.17 | 6.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | NORAD INFLUENCE Mexico, Algeria, Morocco | 36.17 | 6.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Shuttle Diplomacy INFLUENCE Mexico, Algeria, Morocco | 36.17 | 6.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Fidel[8], Allende[57], Cultural Revolution[61], OPEC[64], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE UK | 19.52 | 6.00 | 19.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, non_coup_milops_penalty:5.33 |
| 2 | One Small Step INFLUENCE UK | 19.52 | 6.00 | 19.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, non_coup_milops_penalty:5.33 |
| 3 | Cultural Revolution INFLUENCE UK, Mexico | 16.32 | 6.00 | 36.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | OPEC INFLUENCE UK, Mexico | 16.32 | 6.00 | 36.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Allende INFLUENCE UK | 7.67 | 6.00 | 19.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:UK:14.15, control_break:UK, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], East European Unrest[29], NORAD[38], Willy Brandt[58], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE West Germany, Morocco | 32.25 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:6.40 |
| 2 | East European Unrest INFLUENCE East Germany, West Germany, Morocco | 27.65 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | NORAD INFLUENCE East Germany, West Germany, Morocco | 27.65 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Morocco | 27.65 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Blockade INFLUENCE Morocco | 16.25 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Fidel[8], Allende[57], Cultural Revolution[61], OPEC[64], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Mexico | 16.25 | 6.00 | 16.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:6.40 |
| 2 | Cultural Revolution INFLUENCE Mexico, South Africa | 12.90 | 6.00 | 33.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | OPEC INFLUENCE Mexico, South Africa | 12.90 | 6.00 | 33.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Allende INFLUENCE Mexico | 4.40 | 6.00 | 16.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Fidel SPACE | 1.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], East European Unrest[29], NORAD[38], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, West Germany, Mexico | 29.20 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | NORAD INFLUENCE East Germany, West Germany, Mexico | 29.20 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Mexico | 29.20 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Blockade INFLUENCE Mexico | 17.80 | 6.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:8.00 |
| 5 | East European Unrest SPACE | -0.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Fidel[8], Allende[57], Cultural Revolution[61], OPEC[64], Liberation Theology[76]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE Algeria, South Africa | 10.55 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | OPEC INFLUENCE Algeria, South Africa | 10.55 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Allende INFLUENCE South Africa | 2.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Fidel SPACE | -0.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Liberation Theology SPACE | -0.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], NORAD[38], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, West Germany, Algeria | 25.78 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Algeria | 25.78 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Blockade INFLUENCE Algeria | 14.38 | 6.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:10.67 |
| 4 | NORAD SPACE | -3.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Shuttle Diplomacy SPACE | -3.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Fidel[8], Allende[57], OPEC[64], Liberation Theology[76]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE Morocco, South Africa | 13.48 | 6.00 | 38.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Allende INFLUENCE South Africa | 4.98 | 6.00 | 21.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Fidel INFLUENCE South Africa | 0.83 | 6.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Liberation Theology INFLUENCE South Africa | 0.83 | 6.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Fidel SPACE | -2.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 4.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 2 | Blockade INFLUENCE West Germany | -6.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:28.00 |
| 3 | Shuttle Diplomacy SPACE | -20.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 4 | Blockade REALIGN Mexico | -22.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:28.00 |
| 5 | Blockade EVENT | -25.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Allende [57] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Fidel[8], Allende[57], Liberation Theology[76]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE South Africa | -17.35 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 2 | Fidel SPACE | -20.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 3 | Liberation Theology SPACE | -20.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 4 | Fidel INFLUENCE South Africa | -21.50 | 6.00 | 16.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 5 | Liberation Theology INFLUENCE South Africa | -21.50 | 6.00 | 16.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | -22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:44.00 |
| 2 | Blockade REALIGN Mexico | -38.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:44.00 |
| 3 | Blockade EVENT | -41.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:44.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Fidel [8] as SPACE`
- flags: `milops_shortfall:4, offside_ops_play, space_play`
- hand: `Fidel[8], Liberation Theology[76]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel SPACE | -36.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 2 | Liberation Theology SPACE | -36.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 3 | Fidel INFLUENCE South Africa | -37.50 | 6.00 | 16.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 4 | Liberation Theology INFLUENCE South Africa | -37.50 | 6.00 | 16.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 5 | Fidel EVENT | -50.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:44.00 |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 59: T5 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Duck and Cover[4], Socialist Governments[7], CIA Created[26], Nuclear Test Ban[34], Special Relationship[37], Brush War[39], Bear Trap[47], ABM Treaty[60], Grain Sales to Soviets[68]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Olympic Games[20], Independent Reds[22], Decolonization[30], Red Scare/Purge[31], South African Unrest[56], Flower Power[62], Sadat Expels Soviets[73], Alliance for Progress[79]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Duck and Cover[4], Socialist Governments[7], CIA Created[26], Special Relationship[37], Brush War[39], Bear Trap[47], ABM Treaty[60], Grain Sales to Soviets[68]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, West Germany | 46.94 | 6.00 | 47.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 2 | Socialist Governments INFLUENCE East Germany, West Germany | 31.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 3 | Brush War INFLUENCE East Germany, West Germany | 31.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 4 | Duck and Cover INFLUENCE East Germany, West Germany | 11.54 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 5 | Bear Trap INFLUENCE East Germany, West Germany | 11.54 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Olympic Games[20], Independent Reds[22], Decolonization[30], South African Unrest[56], Flower Power[62], Sadat Expels Soviets[73], Alliance for Progress[79]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE West Germany, Congo/Zaire, South Africa | 53.99 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Alliance for Progress INFLUENCE West Germany, Congo/Zaire, South Africa | 53.99 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Olympic Games INFLUENCE West Germany, South Africa | 37.94 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 4 | Independent Reds INFLUENCE West Germany, South Africa | 37.94 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 5 | Korean War INFLUENCE West Germany, South Africa | 21.94 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Duck and Cover[4], Socialist Governments[7], CIA Created[26], Special Relationship[37], Brush War[39], Bear Trap[47], Grain Sales to Soviets[68]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE France, West Germany | 35.58 | 6.00 | 36.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 2 | Brush War INFLUENCE France, West Germany | 35.58 | 6.00 | 36.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 3 | Duck and Cover INFLUENCE France, West Germany | 15.58 | 6.00 | 36.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | Bear Trap INFLUENCE France, West Germany | 15.58 | 6.00 | 36.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | CIA Created INFLUENCE France | 7.73 | 6.00 | 20.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Olympic Games[20], Independent Reds[22], Decolonization[30], South African Unrest[56], Flower Power[62], Alliance for Progress[79]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE West Germany, Congo/Zaire, South Africa | 56.03 | 6.00 | 57.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 2 | Olympic Games INFLUENCE West Germany, Congo/Zaire | 39.38 | 6.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:6.67 |
| 3 | Independent Reds INFLUENCE West Germany, Congo/Zaire | 39.38 | 6.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:6.67 |
| 4 | Korean War INFLUENCE West Germany, Congo/Zaire | 23.38 | 6.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Decolonization INFLUENCE West Germany, Congo/Zaire | 23.38 | 6.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Duck and Cover[4], CIA Created[26], Special Relationship[37], Brush War[39], Bear Trap[47], Grain Sales to Soviets[68]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, West Germany | 29.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Duck and Cover INFLUENCE East Germany, West Germany | 9.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Bear Trap INFLUENCE East Germany, West Germany | 9.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Special Relationship SPACE | 4.20 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Grain Sales to Soviets SPACE | 4.20 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Olympic Games[20], Independent Reds[22], Decolonization[30], South African Unrest[56], Flower Power[62]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, South Africa | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Independent Reds INFLUENCE West Germany, South Africa | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Korean War INFLUENCE West Germany, South Africa | 19.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Decolonization INFLUENCE West Germany, South Africa | 19.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | South African Unrest INFLUENCE West Germany, South Africa | 19.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `Duck and Cover[4], CIA Created[26], Special Relationship[37], Bear Trap[47], Grain Sales to Soviets[68]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, West Germany | 7.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Bear Trap INFLUENCE East Germany, West Germany | 7.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Special Relationship SPACE | 2.20 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Grain Sales to Soviets SPACE | 2.20 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Duck and Cover SPACE | 2.05 | 1.00 | 4.00 | 0.00 | 7.50 | -0.45 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Independent Reds[22], Decolonization[30], South African Unrest[56], Flower Power[62]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, South Africa | 33.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 2 | Korean War INFLUENCE West Germany, South Africa | 17.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Decolonization INFLUENCE West Germany, South Africa | 17.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | South African Unrest INFLUENCE West Germany, South Africa | 17.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Flower Power INFLUENCE West Germany, South Africa | 17.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Special Relationship[37], Bear Trap[47], Grain Sales to Soviets[68]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, West Germany | 3.92 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Special Relationship SPACE | -1.13 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Grain Sales to Soviets SPACE | -1.13 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Bear Trap SPACE | -1.28 | 1.00 | 4.00 | 0.00 | 7.50 | -0.45 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | CIA Created INFLUENCE West Germany | -3.33 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Korean War[11], Decolonization[30], South African Unrest[56], Flower Power[62]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, South Africa | 14.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Decolonization INFLUENCE West Germany, South Africa | 14.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | South African Unrest INFLUENCE West Germany, South Africa | 14.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Flower Power INFLUENCE West Germany, South Africa | 14.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Korean War SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Special Relationship [37] as SPACE`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play, space_play`
- hand: `CIA Created[26], Special Relationship[37], Grain Sales to Soviets[68]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship SPACE | -22.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | Grain Sales to Soviets SPACE | -22.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 3 | CIA Created INFLUENCE West Germany | -25.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 4 | Special Relationship INFLUENCE West Germany | -29.15 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | Grain Sales to Soviets INFLUENCE West Germany | -29.15 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Decolonization[30], South African Unrest[56], Flower Power[62]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | -12.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | South African Unrest INFLUENCE West Germany, South Africa | -12.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 3 | Flower Power INFLUENCE West Germany, South Africa | -12.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 4 | Decolonization SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | South African Unrest SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Grain Sales to Soviets[68]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE West Germany | -45.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany | -49.15 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 3 | CIA Created EVENT | -61.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:55.00 |
| 4 | Grain Sales to Soviets EVENT | -61.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:55.00 |
| 5 | CIA Created REALIGN East Germany | -63.60 | -1.00 | 4.55 | 0.00 | -12.00 | -0.15 | 0.00 | offside_ops_penalty, non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `South African Unrest[56], Flower Power[62]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE West Germany, South Africa | -32.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 2 | Flower Power INFLUENCE West Germany, South Africa | -32.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 3 | South African Unrest SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 4 | Flower Power SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 5 | South African Unrest EVENT | -61.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Fidel[8], Vietnam Revolts[9], Nuclear Test Ban[34], Arms Race[42], Nuclear Subs[44], Junta[50], Missile Envy[52], Muslim Revolution[59], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Romanian Abdication[12], Arab-Israeli War[13], Marshall Plan[23], Suez Crisis[28], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +3, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Fidel[8], Vietnam Revolts[9], Arms Race[42], Nuclear Subs[44], Junta[50], Missile Envy[52], Muslim Revolution[59], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Cuba | 61.34 | 6.00 | 62.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.86 |
| 2 | Arms Race INFLUENCE East Germany, France, West Germany | 45.94 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 3 | Fidel INFLUENCE East Germany, West Germany | 30.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 4 | Vietnam Revolts INFLUENCE East Germany, West Germany | 30.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 5 | Junta INFLUENCE East Germany, West Germany | 30.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Romanian Abdication[12], Arab-Israeli War[13], Suez Crisis[28], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Angola, South Africa | 47.24 | 6.00 | 48.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Angola, South Africa | 47.24 | 6.00 | 48.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | Latin American Death Squads INFLUENCE West Germany, South Africa | 31.79 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 4 | Suez Crisis INFLUENCE West Germany, Angola, South Africa | 27.24 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 5 | Che INFLUENCE West Germany, Angola, South Africa | 27.24 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Fidel[8], Vietnam Revolts[9], Arms Race[42], Nuclear Subs[44], Junta[50], Missile Envy[52], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany | 44.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Fidel INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Vietnam Revolts INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Junta INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Missile Envy INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Arab-Israeli War[13], Suez Crisis[28], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Angola, South Africa | 46.10 | 6.00 | 48.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Suez Crisis INFLUENCE West Germany, Angola, South Africa | 26.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Che INFLUENCE West Germany, Angola, South Africa | 26.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Vietnam Revolts INFLUENCE West Germany, South Africa | 14.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Fidel[8], Vietnam Revolts[9], Nuclear Subs[44], Junta[50], Missile Envy[52], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 3 | Junta INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 4 | Missile Envy INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 5 | Nuclear Subs INFLUENCE East Germany, West Germany | 11.80 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Arab-Israeli War[13], Suez Crisis[28], Latin American Death Squads[70], Che[83]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, South Africa | 29.05 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 2 | Suez Crisis INFLUENCE West Germany, Angola, South Africa | 24.50 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | Che INFLUENCE West Germany, Angola, South Africa | 24.50 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Vietnam Revolts INFLUENCE West Germany, South Africa | 13.05 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Arab-Israeli War INFLUENCE West Germany, South Africa | 13.05 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Vietnam Revolts[9], Nuclear Subs[44], Junta[50], Missile Envy[52], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 25.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 2 | Junta INFLUENCE East Germany, West Germany | 25.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 3 | Missile Envy INFLUENCE East Germany, West Germany | 25.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 4 | Nuclear Subs INFLUENCE East Germany, West Germany | 9.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Nuclear Subs SPACE | 0.20 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Arab-Israeli War[13], Suez Crisis[28], Che[83]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Angola, South Africa | 22.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Che INFLUENCE West Germany, Angola, South Africa | 22.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Vietnam Revolts INFLUENCE West Germany, South Africa | 10.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Arab-Israeli War INFLUENCE West Germany, South Africa | 10.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Romanian Abdication INFLUENCE South Africa | -1.35 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Nuclear Subs[44], Junta[50], Missile Envy[52], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:16.00 |
| 2 | Missile Envy INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:16.00 |
| 3 | Nuclear Subs INFLUENCE East Germany, West Germany | 5.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Nuclear Subs SPACE | -3.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Panama Canal Returned INFLUENCE West Germany | -6.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Arab-Israeli War[13], Che[83]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE West Germany, Angola, South Africa | 18.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Vietnam Revolts INFLUENCE West Germany, South Africa | 6.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Arab-Israeli War INFLUENCE West Germany, South Africa | 6.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Romanian Abdication INFLUENCE South Africa | -5.35 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Vietnam Revolts SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Nuclear Subs[44], Missile Envy[52], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | -4.60 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:42.00 |
| 2 | Nuclear Subs INFLUENCE East Germany, West Germany | -20.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Nuclear Subs SPACE | -29.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Panama Canal Returned INFLUENCE West Germany | -32.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Missile Envy SPACE | -36.80 | 1.00 | 2.00 | 0.00 | 2.50 | -0.30 | 0.00 | space_when_behind, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Arab-Israeli War[13]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, South Africa | -19.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany, South Africa | -19.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Romanian Abdication INFLUENCE South Africa | -31.35 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Vietnam Revolts SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Arab-Israeli War SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space, offside_ops_play`
- hand: `Nuclear Subs[44], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | -44.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 2 | Nuclear Subs SPACE | -53.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | Panama Canal Returned INFLUENCE West Germany | -56.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 4 | Panama Canal Returned EVENT | -72.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |
| 5 | Nuclear Subs EVENT | -72.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Arab-Israeli War[13]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, South Africa | -43.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 2 | Romanian Abdication INFLUENCE South Africa | -55.35 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | Arab-Israeli War SPACE | -58.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 4 | Romanian Abdication EVENT | -72.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |
| 5 | Arab-Israeli War EVENT | -72.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 91: T7 AR0 USSR

- chosen: `How I Learned to Stop Worrying [49] as EVENT`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Romanian Abdication[12], Containment[25], How I Learned to Stop Worrying[49], Kitchen Debates[51], Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], De Gaulle Leads France[17], Indo-Pakistani War[24], UN Intervention[32], Special Relationship[37], SALT Negotiations[46], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Ussuri River Skirmish[77]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON -4, MilOps U+5/A+0`
