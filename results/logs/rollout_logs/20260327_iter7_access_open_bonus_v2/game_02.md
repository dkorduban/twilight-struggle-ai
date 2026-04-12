# minimal_hybrid detailed rollout log

- seed: `20260521`
- winner: `USSR`
- final_vp: `27`
- end_turn: `10`
- end_reason: `vp_threshold`

## Step 1: T1 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Fidel[8], COMECON[14], De Gaulle Leads France[17], Truman Doctrine[19], Containment[25], CIA Created[26], Suez Crisis[28]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15], NATO[21], Independent Reds[22], Decolonization[30], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Decolonization EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Fidel[8], De Gaulle Leads France[17], Truman Doctrine[19], Containment[25], CIA Created[26], Suez Crisis[28]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Iran | 76.83 | 4.00 | 73.28 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Suez Crisis COUP Iran | 76.83 | 4.00 | 73.28 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 3 | Fidel COUP Iran | 71.48 | 4.00 | 67.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | De Gaulle Leads France INFLUENCE West Germany, Japan, Thailand | 62.47 | 6.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |
| 5 | Suez Crisis INFLUENCE West Germany, Japan, Thailand | 62.47 | 6.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15], Independent Reds[22], Decolonization[30], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Special Relationship INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | UN Intervention COUP North Korea | 30.23 | 4.00 | 26.38 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 4 | Independent Reds COUP North Korea | 30.08 | 4.00 | 26.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 5 | Special Relationship COUP North Korea | 30.08 | 4.00 | 26.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china`
- hand: `Five Year Plan[5], Fidel[8], Truman Doctrine[19], Containment[25], CIA Created[26], Suez Crisis[28]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, Thailand | 63.80 | 6.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 2 | Suez Crisis COUP Iran | 53.50 | 4.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus |
| 3 | Fidel COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Fidel INFLUENCE Japan, Thailand | 46.30 | 6.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 5 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 43.80 | 6.00 | 58.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15], Decolonization[30], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, North Korea | 42.30 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.60 |
| 2 | UN Intervention COUP North Korea | 30.30 | 4.00 | 26.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.20, coup_access_open |
| 3 | Special Relationship COUP North Korea | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.20, coup_access_open |
| 4 | Special Relationship COUP Syria | 28.05 | 4.00 | 24.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 5 | Decolonization INFLUENCE West Germany, North Korea | 26.30 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china`
- hand: `Five Year Plan[5], Fidel[8], Truman Doctrine[19], Containment[25], CIA Created[26]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE North Korea, Thailand | 51.70 | 6.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 2 | Five Year Plan INFLUENCE North Korea, South Korea, Thailand | 49.10 | 6.00 | 63.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Containment INFLUENCE North Korea, South Korea, Thailand | 49.10 | 6.00 | 63.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Fidel COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Fidel COUP Philippines | 35.90 | 4.00 | 32.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15], Decolonization[30], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Japan | 24.00 | 4.00 | 20.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 2 | UN Intervention COUP North Korea | 23.40 | 4.00 | 19.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 3 | UN Intervention COUP Syria | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 4 | Decolonization INFLUENCE East Germany, Turkey | 22.20 | 6.00 | 34.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | UN Intervention INFLUENCE Turkey | 21.30 | 6.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Turkey:12.45, control_break:Turkey, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 9: T1 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], Containment[25], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Pakistan, South Korea, Thailand | 40.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Containment INFLUENCE Pakistan, South Korea, Thailand | 40.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Five Year Plan SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, Turkey | 24.20 | 6.00 | 34.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty |
| 2 | Blockade INFLUENCE Turkey | 11.30 | 6.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE Turkey | 11.30 | 6.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty |
| 4 | Nasser INFLUENCE Turkey | 11.30 | 6.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty |
| 5 | Decolonization COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Containment[25], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, Pakistan, Thailand | 46.00 | 6.00 | 60.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Containment SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Containment COUP Lebanon | 0.40 | 4.00 | 16.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE France | 10.90 | 6.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.05, access_touch:France, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE France | 10.90 | 6.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.05, access_touch:France, offside_ops_penalty |
| 3 | Nasser INFLUENCE France | 10.90 | 6.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.05, access_touch:France, offside_ops_penalty |
| 4 | Blockade COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 2 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Truman Doctrine COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine EVENT | -6.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Italy | 10.30 | 6.00 | 16.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |
| 2 | Nasser INFLUENCE Italy | 10.30 | 6.00 | 16.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |
| 3 | Romanian Abdication COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Nasser COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +2, DEFCON +1, MilOps U-3/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Vietnam Revolts[9], Arab-Israeli War[13], Captured Nazi Scientist[18], East European Unrest[29], Red Scare/Purge[31], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Warsaw Pact Formed[16], Marshall Plan[23], Indo-Pakistani War[24], De-Stalinization[33], Nuclear Test Ban[34], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Vietnam Revolts[9], Arab-Israeli War[13], Captured Nazi Scientist[18], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE India, Israel, Thailand | 57.78 | 6.00 | 54.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | Socialist Governments COUP Philippines | 43.92 | 4.00 | 40.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 3 | Vietnam Revolts INFLUENCE India, Thailand | 41.03 | 6.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Arab-Israeli War INFLUENCE India, Thailand | 41.03 | 6.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 5 | Vietnam Revolts COUP Philippines | 38.57 | 4.00 | 34.87 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Warsaw Pact Formed[16], Indo-Pakistani War[24], De-Stalinization[33], Nuclear Test Ban[34], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Italy, Japan, Panama | 54.53 | 6.00 | 51.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 2 | Nuclear Test Ban COUP Syria | 40.02 | 4.00 | 36.62 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 3 | Nuclear Test Ban COUP Indonesia | 37.67 | 4.00 | 34.27 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:5.5 |
| 4 | Nuclear Test Ban COUP North Korea | 32.37 | 4.00 | 28.97 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:1.5 |
| 5 | Nuclear Test Ban COUP South Korea | 32.37 | 4.00 | 28.97 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Arab-Israeli War[13], Captured Nazi Scientist[18], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Italy, Thailand | 39.40 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Arab-Israeli War INFLUENCE Italy, Thailand | 39.40 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | Vietnam Revolts COUP Philippines | 38.70 | 4.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 4 | Arab-Israeli War COUP Philippines | 38.70 | 4.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | Duck and Cover INFLUENCE Italy, Philippines, Thailand | 35.70 | 6.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Warsaw Pact Formed[16], Indo-Pakistani War[24], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Syria | 29.45 | 4.00 | 25.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 2 | Formosan Resolution COUP Syria | 29.45 | 4.00 | 25.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 3 | Indo-Pakistani War COUP Indonesia | 27.10 | 4.00 | 23.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:3.5 |
| 4 | Formosan Resolution COUP Indonesia | 27.10 | 4.00 | 23.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:3.5 |
| 5 | Indo-Pakistani War COUP Japan | 25.15 | 4.00 | 21.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:0.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 21: T2 AR3 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Captured Nazi Scientist[18], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Philippines | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 2 | Arab-Israeli War INFLUENCE Philippines, Thailand | 38.60 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Duck and Cover INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | East European Unrest INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | NORAD INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 22: T2 AR3 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `none`
- hand: `Korean War[11], Warsaw Pact Formed[16], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 2 | Formosan Resolution INFLUENCE Italy | 25.15 | 6.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy |
| 3 | Warsaw Pact Formed INFLUENCE Italy, Philippines | 21.45 | 6.00 | 35.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, access_touch:Philippines, offside_ops_penalty |
| 4 | De-Stalinization INFLUENCE Italy, Philippines | 21.45 | 6.00 | 35.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, access_touch:Philippines, offside_ops_penalty |
| 5 | Formosan Resolution COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Saudi Arabia, Thailand | 38.45 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | East European Unrest INFLUENCE Japan, Saudi Arabia, Thailand | 38.45 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE Japan, Saudi Arabia, Thailand | 38.45 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 5 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], Warsaw Pact Formed[16], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Italy, Philippines | 21.45 | 6.00 | 35.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, access_touch:Philippines, offside_ops_penalty |
| 2 | De-Stalinization INFLUENCE Italy, Philippines | 21.45 | 6.00 | 35.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, access_touch:Philippines, offside_ops_penalty |
| 3 | Warsaw Pact Formed COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | De-Stalinization COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Korean War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Philippines, Thailand | 41.60 | 6.00 | 56.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE Japan, Philippines, Thailand | 41.60 | 6.00 | 56.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | East European Unrest SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, Egypt | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 2 | De-Stalinization COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Korean War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Indonesia, Thailand | 38.00 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | NORAD SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Captured Nazi Scientist REALIGN Israel | 3.04 | -1.00 | 4.20 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Korean War [11] as COUP`
- flags: `offside_ops_play`
- hand: `Korean War[11], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Korean War INFLUENCE Indonesia | 8.55 | 6.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Olympic Games[20], Independent Reds[22], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32], Nuclear Test Ban[34]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], De Gaulle Leads France[17], Truman Doctrine[19], Containment[25], East European Unrest[29], Decolonization[30], Red Scare/Purge[31], De-Stalinization[33]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Olympic Games[20], Independent Reds[22], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 2 | Olympic Games COUP Egypt | 38.15 | 4.00 | 34.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 3 | UN Intervention COUP Indonesia | 35.95 | 4.00 | 32.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE Japan, Indonesia, Thailand | 32.85 | 6.00 | 55.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Olympic Games COUP Philippines | 31.90 | 4.00 | 28.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 32: T3 AR1 US

- chosen: `Containment [25] as COUP`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], De Gaulle Leads France[17], Truman Doctrine[19], Containment[25], East European Unrest[29], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment COUP Indonesia | 55.65 | 4.00 | 52.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | East European Unrest COUP Indonesia | 55.65 | 4.00 | 52.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 3 | Containment INFLUENCE Japan, Egypt, Iraq | 52.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:4.00 |
| 4 | East European Unrest INFLUENCE Japan, Egypt, Iraq | 52.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:4.00 |
| 5 | Truman Doctrine COUP Indonesia | 42.95 | 4.00 | 39.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 33: T3 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Duck and Cover[4], Five Year Plan[5], Independent Reds[22], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Japan, Indonesia, Thailand | 32.25 | 6.00 | 52.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 2 | UN Intervention INFLUENCE Thailand | 24.70 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:1.60 |
| 3 | UN Intervention COUP Syria | 22.70 | 4.00 | 18.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:0.5 |
| 4 | Duck and Cover INFLUENCE Japan, Thailand | 20.55 | 6.00 | 36.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Five Year Plan INFLUENCE Japan, Thailand | 20.55 | 6.00 | 36.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], De Gaulle Leads France[17], Truman Doctrine[19], East European Unrest[29], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Egypt, Iraq | 56.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq |
| 2 | De Gaulle Leads France INFLUENCE Japan, Egypt, Iraq | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty |
| 3 | De-Stalinization INFLUENCE Japan, Egypt, Iraq | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty |
| 4 | Fidel INFLUENCE Egypt, Iraq | 24.70 | 6.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty |
| 5 | Decolonization INFLUENCE Egypt, Iraq | 24.70 | 6.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Five Year Plan[5], Independent Reds[22], CIA Created[26], UN Intervention[32]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 24.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Duck and Cover INFLUENCE Iraq, Thailand | 23.30 | 6.00 | 39.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Five Year Plan INFLUENCE Iraq, Thailand | 23.30 | 6.00 | 39.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | UN Intervention COUP Syria | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 5 | Duck and Cover COUP Syria | 13.50 | 4.00 | 29.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], De Gaulle Leads France[17], Truman Doctrine[19], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Japan, Iran, Saudi Arabia | 33.70 | 6.00 | 48.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty |
| 2 | De-Stalinization INFLUENCE Japan, Iran, Saudi Arabia | 33.70 | 6.00 | 48.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty |
| 3 | Fidel INFLUENCE Japan, Saudi Arabia | 22.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty |
| 4 | Truman Doctrine INFLUENCE Saudi Arabia | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 5 | Decolonization INFLUENCE Japan, Saudi Arabia | 22.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Duck and Cover[4], Five Year Plan[5], Independent Reds[22], CIA Created[26]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Iraq, Thailand | 22.63 | 6.00 | 39.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Five Year Plan INFLUENCE Iraq, Thailand | 22.63 | 6.00 | 39.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Duck and Cover COUP Syria | 13.67 | 4.00 | 30.12 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Five Year Plan COUP Syria | 13.67 | 4.00 | 30.12 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Independent Reds COUP Syria | 12.32 | 4.00 | 24.62 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Truman Doctrine[19], Decolonization[30], De-Stalinization[33]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, Pakistan, Libya | 34.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Pakistan | 22.80 | 6.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan |
| 3 | Fidel INFLUENCE Japan, Pakistan | 22.80 | 6.00 | 33.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty |
| 4 | Decolonization INFLUENCE Japan, Pakistan | 22.80 | 6.00 | 33.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty |
| 5 | Truman Doctrine COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Independent Reds[22], CIA Created[26]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Pakistan, Thailand | 18.95 | 6.00 | 40.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Five Year Plan COUP Egypt | 16.50 | 4.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Independent Reds COUP Egypt | 15.15 | 4.00 | 27.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Five Year Plan COUP Syria | 14.00 | 4.00 | 30.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | CIA Created COUP Egypt | 13.80 | 4.00 | 21.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Truman Doctrine[19], Decolonization[30]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE India, Libya | 25.95 | 6.00 | 36.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 2 | Decolonization INFLUENCE India, Libya | 25.95 | 6.00 | 36.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 3 | Truman Doctrine INFLUENCE Libya | 24.55 | 6.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Libya:13.70, control_break:Libya |
| 4 | Truman Doctrine COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Egypt | 16.15 | 4.00 | 28.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | CIA Created COUP Egypt | 14.80 | 4.00 | 22.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Independent Reds COUP Syria | 13.65 | 4.00 | 25.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | CIA Created COUP Syria | 12.30 | 4.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Independent Reds COUP Iran | 9.15 | 4.00 | 21.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `Truman Doctrine[19], Decolonization[30]`
- state: `VP 4, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | Decolonization INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 3 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Truman Doctrine COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Sudan | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], East European Unrest[29], NORAD[38], Arms Race[42], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], Voice of America[75], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | East European Unrest EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], US/Japan Mutual Defense Pact[27], UN Intervention[32], SALT Negotiations[46], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], East European Unrest[29], NORAD[38], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], Voice of America[75], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE UK, Mexico, Algeria | 50.28 | 6.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 2 | Cuban Missile Crisis COUP Egypt | 38.14 | 4.00 | 34.59 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Cuban Missile Crisis COUP Syria | 35.64 | 4.00 | 32.09 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |
| 4 | How I Learned to Stop Worrying INFLUENCE Mexico, Algeria | 34.28 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 5 | Colonial Rear Guards INFLUENCE Mexico, Algeria | 34.28 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], UN Intervention[32], SALT Negotiations[46], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE UK, Mexico, Morocco | 53.88 | 6.00 | 52.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 2 | Ussuri River Skirmish INFLUENCE UK, Mexico, Morocco | 53.88 | 6.00 | 52.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 3 | SALT Negotiations COUP Mexico | 39.89 | 4.00 | 36.34 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Mexico | 39.89 | 4.00 | 36.34 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | SALT Negotiations COUP Algeria | 39.14 | 4.00 | 35.59 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], East European Unrest[29], NORAD[38], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], Voice of America[75], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE Algeria, Morocco | 36.37 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 2 | Colonial Rear Guards INFLUENCE Algeria, Morocco | 36.37 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 3 | East European Unrest INFLUENCE West Germany, Algeria, Morocco | 32.37 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | NORAD INFLUENCE West Germany, Algeria, Morocco | 32.37 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | How I Learned to Stop Worrying COUP Egypt | 31.98 | 4.00 | 28.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], UN Intervention[32], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE West Germany, Algeria, South Africa | 49.37 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 2 | Ussuri River Skirmish COUP Algeria | 39.33 | 4.00 | 35.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | John Paul II Elected Pope INFLUENCE Algeria, South Africa | 33.37 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 4 | Nixon Plays the China Card INFLUENCE Algeria, South Africa | 33.37 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 5 | Ussuri River Skirmish COUP Mexico | 33.08 | 4.00 | 29.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], East European Unrest[29], NORAD[38], Lonely Hearts Club Band[65], Voice of America[75], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE West Germany, Algeria | 34.65 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 2 | Colonial Rear Guards COUP Egypt | 32.25 | 4.00 | 28.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Colonial Rear Guards COUP Libya | 32.25 | 4.00 | 28.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | East European Unrest INFLUENCE East Germany, West Germany, Algeria | 30.05 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | NORAD INFLUENCE East Germany, West Germany, Algeria | 30.05 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], UN Intervention[32], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 37.25 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:6.40 |
| 2 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 37.25 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:6.40 |
| 3 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, South Africa | 32.65 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 32.65 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | John Paul II Elected Pope COUP Mexico | 27.00 | 4.00 | 23.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], East European Unrest[29], NORAD[38], Lonely Hearts Club Band[65], Voice of America[75]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | NORAD INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | East European Unrest COUP Egypt | 19.00 | 4.00 | 35.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | East European Unrest COUP Libya | 19.00 | 4.00 | 35.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | NORAD COUP Egypt | 19.00 | 4.00 | 35.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], UN Intervention[32], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Nixon Plays the China Card COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 3 | Nixon Plays the China Card COUP Algeria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, South Africa | 26.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 26.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], NORAD[38], Lonely Hearts Club Band[65], Voice of America[75]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany | 22.13 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | NORAD COUP Egypt | 19.67 | 4.00 | 36.12 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | NORAD COUP Libya | 19.67 | 4.00 | 36.12 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Egypt | 17.32 | 4.00 | 29.62 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band COUP Libya | 17.32 | 4.00 | 29.62 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], UN Intervention[32], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, South Africa | 23.38 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 23.38 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | UN Intervention COUP Mexico | 21.72 | 4.00 | 17.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |
| 4 | Panama Canal Returned COUP Mexico | 21.72 | 4.00 | 17.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |
| 5 | UN Intervention COUP Algeria | 20.97 | 4.00 | 17.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Voice of America[75]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Egypt | 18.65 | 4.00 | 30.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Lonely Hearts Club Band COUP Libya | 18.65 | 4.00 | 30.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Voice of America COUP Egypt | 18.65 | 4.00 | 30.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Voice of America COUP Libya | 18.65 | 4.00 | 30.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Egypt | 16.30 | 4.00 | 24.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 56: T4 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], UN Intervention[32], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Zimbabwe | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 57: T4 AR7 USSR

- chosen: `Voice of America [75] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Voice of America COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Voice of America COUP Guatemala | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Sudan | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:3`
- hand: `De Gaulle Leads France[17], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | De Gaulle Leads France COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Zimbabwe | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 59: T5 AR0 USSR

- chosen: `Brush War [39] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Romanian Abdication[12], Brush War[39], Junta[50], Kitchen Debates[51], Missile Envy[52], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Olympic Games[20], CIA Created[26], US/Japan Mutual Defense Pact[27], Decolonization[30], Special Relationship[37], Quagmire[45], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Romanian Abdication[12], Junta[50], Kitchen Debates[51], Missile Envy[52], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 3 | Missile Envy COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 4 | Liberation Theology COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 5 | One Small Step COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 62: T5 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Olympic Games[20], CIA Created[26], Decolonization[30], Special Relationship[37], Quagmire[45], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, South Africa | 48.34 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Ask Not What Your Country Can Do For You COUP Colombia | 47.33 | 4.00 | 43.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 3 | Olympic Games COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 4 | Special Relationship COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 5 | CIA Created COUP Colombia | 34.63 | 4.00 | 30.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Junta[50], Kitchen Debates[51], Missile Envy[52], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE Panama, Brazil | 34.85 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Brazil:14.20, access_touch:Brazil, non_coup_milops_penalty:4.00 |
| 2 | Missile Envy INFLUENCE Panama, Brazil | 34.85 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Brazil:14.20, access_touch:Brazil, non_coup_milops_penalty:4.00 |
| 3 | Liberation Theology INFLUENCE Panama, Brazil | 34.85 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Brazil:14.20, access_touch:Brazil, non_coup_milops_penalty:4.00 |
| 4 | One Small Step INFLUENCE Panama, Brazil | 34.85 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Brazil:14.20, access_touch:Brazil, non_coup_milops_penalty:4.00 |
| 5 | Camp David Accords INFLUENCE Panama, Brazil | 18.85 | 6.00 | 33.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Brazil:14.20, access_touch:Brazil, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Olympic Games[20], CIA Created[26], Decolonization[30], Special Relationship[37], Quagmire[45], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Colombia | 41.22 | 4.00 | 37.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 2 | Special Relationship COUP Colombia | 41.22 | 4.00 | 37.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | Olympic Games INFLUENCE Panama, South Africa | 35.78 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 4 | Special Relationship INFLUENCE Panama, South Africa | 35.78 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 5 | CIA Created COUP Colombia | 34.87 | 4.00 | 31.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 65: T5 AR3 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Missile Envy[52], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Colombia | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 2 | Liberation Theology COUP Colombia | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 3 | One Small Step COUP Colombia | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 4 | Missile Envy INFLUENCE Argentina, Brazil | 38.30 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:4.80 |
| 5 | Liberation Theology INFLUENCE Argentina, Brazil | 38.30 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], Special Relationship[37], Quagmire[45], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Panama, South Africa | 37.65 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Quagmire INFLUENCE Panama, Brazil, South Africa | 33.70 | 6.00 | 52.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Arab-Israeli War INFLUENCE Panama, South Africa | 21.65 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Decolonization INFLUENCE Panama, South Africa | 21.65 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | CIA Created INFLUENCE Panama | 21.00 | 6.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Panama:14.95, control_break:Panama, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Liberation Theology [76] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Camp David Accords[66], Liberation Theology[76], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Colombia | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Colombia | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 3 | Liberation Theology INFLUENCE Argentina, Brazil | 37.10 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.00 |
| 4 | One Small Step INFLUENCE Argentina, Brazil | 37.10 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.00 |
| 5 | Romanian Abdication COUP Colombia | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:3`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], Quagmire[45], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Colombia | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 2 | Quagmire INFLUENCE East Germany, West Germany, South Africa | 28.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Quagmire COUP Colombia | 27.40 | 4.00 | 43.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Colombia | 25.05 | 4.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Colombia | 25.05 | 4.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Camp David Accords[66], One Small Step[81]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Argentina, Brazil | 35.10 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:8.00 |
| 2 | One Small Step COUP Colombia | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Sudan | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Camp David Accords INFLUENCE Argentina, Brazil | 19.10 | 6.00 | 37.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], Quagmire[45], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, West Germany, South Africa | 26.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany, South Africa | 14.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Decolonization INFLUENCE West Germany, South Africa | 14.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Quagmire COUP Colombia | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Saharan States | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Camp David Accords[66]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Colombia | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Romanian Abdication COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication COUP Guatemala | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Camp David Accords INFLUENCE East Germany, Argentina | 10.45 | 6.00 | 41.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Argentina:16.20, control_break:Argentina, offside_ops_penalty, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Colombia | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Colombia | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Colombia | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP SE African States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Kitchen Debates[51], Camp David Accords[66]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Kitchen Debates COUP Colombia | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Camp David Accords COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Camp David Accords COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Camp David Accords COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Decolonization[30], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Lone Gunman COUP Colombia | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Decolonization COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Zimbabwe | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 75: T6 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Five Year Plan[5], Blockade[10], Containment[25], Decolonization[30], De-Stalinization[33], OPEC[64], Puppet Governments[67], Sadat Expels Soviets[73], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Red Scare/Purge[31], De-Stalinization[33], Nuclear Test Ban[34], Formosan Resolution[35], Brezhnev Doctrine[54], South African Unrest[56], Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `OPEC [64] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Five Year Plan[5], Blockade[10], Containment[25], Decolonization[30], OPEC[64], Puppet Governments[67], Sadat Expels Soviets[73], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Colombia | 47.61 | 4.00 | 44.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Che COUP Colombia | 47.61 | 4.00 | 44.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 3 | Decolonization COUP Colombia | 41.26 | 4.00 | 37.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 4 | OPEC COUP Libya | 38.71 | 4.00 | 35.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Che COUP Libya | 38.71 | 4.00 | 35.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 78: T6 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], De-Stalinization[33], Nuclear Test Ban[34], Formosan Resolution[35], Brezhnev Doctrine[54], South African Unrest[56], Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE East Germany, France, West Germany, South Africa | 62.59 | 6.00 | 64.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | Nuclear Test Ban COUP Colombia | 53.96 | 4.00 | 50.56 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:5.5 |
| 3 | Duck and Cover COUP Colombia | 47.61 | 4.00 | 44.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 4 | Duck and Cover INFLUENCE East Germany, West Germany, South Africa | 47.19 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 5 | Nuclear Test Ban COUP Egypt | 45.06 | 4.00 | 41.66 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Che [83] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Containment[25], Decolonization[30], Puppet Governments[67], Sadat Expels Soviets[73], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Libya | 38.00 | 4.00 | 34.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | Che INFLUENCE Argentina, Chile | 36.55 | 6.00 | 35.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.00 |
| 3 | Che COUP Syria | 35.50 | 4.00 | 31.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | Che COUP Mexico | 32.75 | 4.00 | 29.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:2.5 |
| 5 | Che COUP Panama | 32.75 | 4.00 | 29.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Panama, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], De-Stalinization[33], Formosan Resolution[35], Brezhnev Doctrine[54], South African Unrest[56], Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Colombia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Duck and Cover INFLUENCE East Germany, West Germany, South Africa | 46.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Formosan Resolution COUP Colombia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Formosan Resolution INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | De-Stalinization COUP Colombia | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 81: T6 AR3 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Containment[25], Decolonization[30], Puppet Governments[67], Sadat Expels Soviets[73]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Chile | 19.85 | 6.00 | 18.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.80 |
| 2 | Decolonization INFLUENCE Chile | 19.70 | 6.00 | 18.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.80 |
| 3 | Decolonization COUP Colombia | 18.75 | 4.00 | 15.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 4 | Decolonization COUP Saharan States | 18.75 | 4.00 | 15.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | Decolonization COUP Sudan | 18.75 | 4.00 | 15.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:3`
- hand: `De-Stalinization[33], Formosan Resolution[35], Brezhnev Doctrine[54], South African Unrest[56], Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Colombia | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 2 | Formosan Resolution INFLUENCE West Germany, South Africa | 33.85 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 29.25 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, South Africa | 29.25 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | De-Stalinization COUP Colombia | 27.10 | 4.00 | 43.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Containment[25], Decolonization[30], Puppet Governments[67], Sadat Expels Soviets[73]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Colombia | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 2 | Decolonization COUP Saharan States | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 3 | Decolonization COUP Sudan | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Decolonization COUP Guatemala | 17.80 | 4.00 | 14.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Decolonization INFLUENCE Chile | 16.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `De-Stalinization[33], Brezhnev Doctrine[54], South African Unrest[56], Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 28.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, South Africa | 28.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | De-Stalinization COUP Colombia | 27.40 | 4.00 | 43.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Brezhnev Doctrine COUP Colombia | 27.40 | 4.00 | 43.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | South African Unrest COUP Colombia | 25.05 | 4.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Containment[25], Puppet Governments[67], Sadat Expels Soviets[73]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Argentina, Chile | 10.55 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Containment INFLUENCE Argentina, Chile | 10.55 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Sadat Expels Soviets INFLUENCE Argentina, Chile | 10.55 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Five Year Plan COUP Colombia | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Five Year Plan COUP Saharan States | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Brezhnev Doctrine [54] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Brezhnev Doctrine[54], South African Unrest[56], Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine COUP Colombia | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, South Africa | 26.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | South African Unrest COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Willy Brandt COUP Colombia | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Allende COUP Colombia | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Containment [25] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Containment[25], Puppet Governments[67], Sadat Expels Soviets[73]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment COUP Colombia | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Containment COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Containment COUP Sudan | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Sadat Expels Soviets COUP Colombia | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Sadat Expels Soviets COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `South African Unrest [56] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `South African Unrest[56], Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Colombia | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Colombia | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Colombia | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | South African Unrest COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP SE African States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Sadat Expels Soviets [73] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Puppet Governments[67], Sadat Expels Soviets[73]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets COUP Colombia | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Sadat Expels Soviets COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Sadat Expels Soviets COUP Sudan | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Sadat Expels Soviets COUP Guatemala | 8.65 | 4.00 | 25.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Willy Brandt [58] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Allende[57], Willy Brandt[58]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Allende COUP Colombia | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Willy Brandt COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Zimbabwe | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 91: T7 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], Socialist Governments[7], Fidel[8], Vietnam Revolts[9], Nuclear Test Ban[34], Bear Trap[47], Cultural Revolution[61], Flower Power[62], Shuttle Diplomacy[74]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Red Scare/Purge[31], UN Intervention[32], ABM Treaty[60], Grain Sales to Soviets[68]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], Socialist Governments[7], Fidel[8], Vietnam Revolts[9], Bear Trap[47], Cultural Revolution[61], Flower Power[62], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Indonesia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:4.5 |
| 2 | Cultural Revolution COUP Indonesia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:4.5 |
| 3 | Socialist Governments COUP Libya | 45.00 | 4.00 | 41.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Cultural Revolution COUP Libya | 45.00 | 4.00 | 41.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Fidel COUP Indonesia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 94: T7 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], UN Intervention[32], ABM Treaty[60], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, West Germany, South Africa | 61.45 | 6.00 | 64.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | ABM Treaty COUP Indonesia | 61.25 | 4.00 | 57.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:5.5 |
| 3 | ABM Treaty COUP Colombia | 54.25 | 4.00 | 50.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:5.5 |
| 4 | ABM Treaty COUP Egypt | 51.35 | 4.00 | 47.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Olympic Games COUP Indonesia | 48.55 | 4.00 | 44.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Cultural Revolution [61] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Fidel[8], Vietnam Revolts[9], Bear Trap[47], Cultural Revolution[61], Flower Power[62], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Libya | 44.33 | 4.00 | 40.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 2 | Cultural Revolution COUP Mexico | 39.08 | 4.00 | 35.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:2.5 |
| 3 | Cultural Revolution COUP Panama | 39.08 | 4.00 | 35.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Panama, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:2.5 |
| 4 | Cultural Revolution COUP Algeria | 38.33 | 4.00 | 34.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:2.5 |
| 5 | Cultural Revolution INFLUENCE Argentina, Chile | 38.22 | 6.00 | 38.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], UN Intervention[32], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Colombia | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | Independent Reds COUP Colombia | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 3 | Grain Sales to Soviets COUP Colombia | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Colombia | 35.53 | 4.00 | 31.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Colombia | 35.53 | 4.00 | 31.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 97: T7 AR3 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Fidel[8], Vietnam Revolts[9], Bear Trap[47], Flower Power[62], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Syria | 29.75 | 4.00 | 26.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:1.5 |
| 2 | Vietnam Revolts COUP Syria | 29.75 | 4.00 | 26.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:1.5 |
| 3 | Flower Power COUP Syria | 29.75 | 4.00 | 26.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:1.5 |
| 4 | Fidel COUP Mexico | 27.00 | 4.00 | 23.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 5 | Fidel COUP Panama | 27.00 | 4.00 | 23.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Independent Reds[22], UN Intervention[32], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Egypt | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Independent Reds COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Grain Sales to Soviets COUP Egypt | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Grain Sales to Soviets COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Independent Reds INFLUENCE West Germany, South Africa | 30.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Bear Trap[47], Flower Power[62], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Colombia | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Vietnam Revolts COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Vietnam Revolts COUP Sudan | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Flower Power COUP Colombia | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Flower Power COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], UN Intervention[32], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Colombia | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 3 | Truman Doctrine COUP Colombia | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 4 | UN Intervention COUP Colombia | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 5 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 28.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Flower Power [62] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Bear Trap[47], Flower Power[62], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Colombia | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Flower Power COUP Saharan States | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Flower Power COUP Sudan | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Flower Power COUP Guatemala | 18.97 | 4.00 | 15.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Flower Power INFLUENCE Chile | 16.83 | 6.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 36.53 | 4.00 | 32.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 2 | Truman Doctrine COUP Colombia | 36.53 | 4.00 | 32.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Colombia | 36.53 | 4.00 | 32.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 4 | De Gaulle Leads France COUP Colombia | 29.23 | 4.00 | 45.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 20.72 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Duck and Cover [4] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Colombia | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Duck and Cover COUP Saharan States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Duck and Cover COUP Sudan | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Bear Trap COUP Colombia | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Bear Trap COUP Saharan States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Colombia | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Colombia | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 3 | De Gaulle Leads France COUP Colombia | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP SE African States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Bear Trap [47] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Colombia | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Bear Trap COUP Saharan States | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Bear Trap COUP Sudan | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Shuttle Diplomacy COUP Colombia | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Shuttle Diplomacy COUP Saharan States | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:5`
- hand: `De Gaulle Leads France[17], UN Intervention[32]`
- state: `VP 6, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Colombia | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5 |
| 2 | De Gaulle Leads France COUP Colombia | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | UN Intervention COUP Saharan States | 21.20 | 4.00 | 17.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP SE African States | 21.20 | 4.00 | 17.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Zimbabwe | 21.20 | 4.00 | 17.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 107: T8 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], Truman Doctrine[19], Decolonization[30], Nuclear Test Ban[34], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Shuttle Diplomacy[74]`
- state: `VP 6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Junta [50] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Junta[50], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Yuri and Samantha[106], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], Truman Doctrine[19], Decolonization[30], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Shuttle Diplomacy[74]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, Chile | 48.91 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, control_break:Chile, non_coup_milops_penalty:9.14 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Chile | 48.91 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, control_break:Chile, non_coup_milops_penalty:9.14 |
| 3 | Warsaw Pact Formed COUP Algeria | 39.29 | 4.00 | 35.74 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, expected_swing:2.5 |
| 4 | Brezhnev Doctrine COUP Algeria | 39.29 | 4.00 | 35.74 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, expected_swing:2.5 |
| 5 | Warsaw Pact Formed COUP Mexico | 38.54 | 4.00 | 34.99 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.14, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Yuri and Samantha[106], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Indonesia | 48.09 | 4.00 | 44.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Indonesia | 48.09 | 4.00 | 44.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 3 | Panama Canal Returned COUP Indonesia | 41.74 | 4.00 | 37.89 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:2.5 |
| 4 | Lonely Hearts Club Band COUP Colombia | 41.34 | 4.00 | 37.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 5 | Grain Sales to Soviets COUP Colombia | 41.34 | 4.00 | 37.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 111: T8 AR2 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Truman Doctrine[19], Decolonization[30], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Shuttle Diplomacy[74]`
- state: `VP 7, DEFCON 4, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 44.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Brezhnev Doctrine COUP Algeria | 39.67 | 4.00 | 36.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, expected_swing:2.5 |
| 3 | Brezhnev Doctrine COUP Mexico | 38.92 | 4.00 | 35.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, expected_swing:2.5 |
| 4 | Brezhnev Doctrine COUP Panama | 38.92 | 4.00 | 35.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Panama, battleground_coup, milops_need:8, milops_urgency:1.33, expected_swing:2.5 |
| 5 | Brezhnev Doctrine COUP Pakistan | 38.42 | 4.00 | 34.87 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:8, milops_urgency:1.33, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Grain Sales to Soviets[68], Yuri and Samantha[106], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 4, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Indonesia | 47.80 | 4.00 | 44.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Panama Canal Returned COUP Indonesia | 41.45 | 4.00 | 37.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Grain Sales to Soviets COUP Colombia | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Egypt | 38.40 | 4.00 | 34.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 5 | Grain Sales to Soviets COUP Libya | 38.40 | 4.00 | 34.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Truman Doctrine[19], Decolonization[30], How I Learned to Stop Worrying[49], Shuttle Diplomacy[74]`
- state: `VP 7, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Syria | 31.10 | 4.00 | 27.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:1.5 |
| 2 | How I Learned to Stop Worrying COUP Syria | 31.10 | 4.00 | 27.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:1.5 |
| 3 | Decolonization COUP Algeria | 27.85 | 4.00 | 24.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:1.5 |
| 4 | How I Learned to Stop Worrying COUP Algeria | 27.85 | 4.00 | 24.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:1.5 |
| 5 | Decolonization COUP Mexico | 27.10 | 4.00 | 23.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 114: T8 AR3 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Yuri and Samantha[106], Panama Canal Returned[111]`
- state: `VP 7, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 35.10 | 4.00 | 31.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 2 | De Gaulle Leads France COUP Colombia | 27.80 | 4.00 | 44.25 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Colombia | 27.80 | 4.00 | 44.25 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Egypt | 26.45 | 4.00 | 22.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Panama Canal Returned COUP Libya | 26.45 | 4.00 | 22.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Truman Doctrine[19], How I Learned to Stop Worrying[49], Shuttle Diplomacy[74]`
- state: `VP 7, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Algeria | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | How I Learned to Stop Worrying COUP Mexico | 26.90 | 4.00 | 23.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 4 | How I Learned to Stop Worrying COUP Panama | 26.90 | 4.00 | 23.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | How I Learned to Stop Worrying COUP Iran | 26.40 | 4.00 | 22.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Yuri and Samantha[106]`
- state: `VP 7, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Colombia | 28.40 | 4.00 | 44.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Quagmire COUP Colombia | 28.40 | 4.00 | 44.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Colombia | 26.05 | 4.00 | 38.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Colombia | 26.05 | 4.00 | 38.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Yuri and Samantha COUP Colombia | 26.05 | 4.00 | 38.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 117: T8 AR5 USSR

- chosen: `Shuttle Diplomacy [74] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Shuttle Diplomacy[74]`
- state: `VP 7, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy COUP Colombia | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Colombia | 24.70 | 4.00 | 32.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Shuttle Diplomacy COUP Saharan States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Shuttle Diplomacy COUP Sudan | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 118: T8 AR5 US

- chosen: `Quagmire [45] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Quagmire[45], Yuri and Samantha[106]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Colombia | 28.73 | 4.00 | 45.18 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Colombia | 26.38 | 4.00 | 38.68 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Colombia | 26.38 | 4.00 | 38.68 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Yuri and Samantha COUP Colombia | 26.38 | 4.00 | 38.68 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Quagmire INFLUENCE East Germany, France, West Germany | 21.72 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Truman Doctrine[19]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Colombia | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Saharan States | 4.20 | 4.00 | 12.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Sudan | 4.20 | 4.00 | 12.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Guatemala | 3.45 | 4.00 | 11.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Tunisia | -6.20 | 4.00 | 1.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Yuri and Samantha[106]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Colombia | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Colombia | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Yuri and Samantha COUP Colombia | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Saharan States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP SE African States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Yuri and Samantha[106]`
- state: `VP 7, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Peru | 22.65 | 4.00 | 34.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Yuri and Samantha COUP Peru | 22.65 | 4.00 | 34.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Peru, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP SE African States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Zimbabwe | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 122: T9 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], ABM Treaty[60], OPEC[64], Voice of America[75], Ussuri River Skirmish[77], Che[83], Defectors[108]`
- state: `VP 7, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 123: T9 AR0 US

- chosen: `Soviets Shoot Down KAL 007 [92] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], East European Unrest[29], UN Intervention[32], NORAD[38], Arms Race[42], Cultural Revolution[61], Puppet Governments[67], Grain Sales to Soviets[68], Soviets Shoot Down KAL 007[92]`
- state: `VP 7, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR1 USSR

- chosen: `OPEC [64] as COUP`
- flags: `milops_shortfall:9`
- hand: `Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], OPEC[64], Voice of America[75], Ussuri River Skirmish[77], Che[83], Defectors[108]`
- state: `VP 6, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Colombia | 47.97 | 4.00 | 44.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Ussuri River Skirmish COUP Colombia | 47.97 | 4.00 | 44.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | Che COUP Colombia | 47.97 | 4.00 | 44.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | OPEC INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 125: T9 AR1 US

- chosen: `East European Unrest [29] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Fidel[8], East European Unrest[29], UN Intervention[32], NORAD[38], Arms Race[42], Cultural Revolution[61], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 3, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Colombia | 47.97 | 4.00 | 44.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | NORAD COUP Colombia | 47.97 | 4.00 | 44.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | Arms Race COUP Colombia | 47.97 | 4.00 | 44.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | East European Unrest INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | NORAD INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 126: T9 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], Voice of America[75], Ussuri River Skirmish[77], Che[83], Defectors[108]`
- state: `VP 6, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Ussuri River Skirmish COUP Algeria | 33.00 | 4.00 | 29.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |
| 4 | Che COUP Algeria | 33.00 | 4.00 | 29.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |
| 5 | Ussuri River Skirmish COUP Mexico | 32.25 | 4.00 | 28.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 US

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], UN Intervention[32], NORAD[38], Arms Race[42], Cultural Revolution[61], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Colombia | 47.40 | 4.00 | 43.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Arms Race COUP Colombia | 47.40 | 4.00 | 43.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | NORAD INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Arms Race INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 5 | Puppet Governments COUP Colombia | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR3 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], Voice of America[75], Che[83], Defectors[108]`
- state: `VP 6, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 50.45 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Che COUP Colombia | 47.80 | 4.00 | 44.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 3 | Vietnam Revolts COUP Colombia | 41.45 | 4.00 | 37.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Colombia | 41.45 | 4.00 | 37.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 5 | Blockade COUP Colombia | 35.10 | 4.00 | 31.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], UN Intervention[32], Arms Race[42], Cultural Revolution[61], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany | 45.45 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Arms Race COUP Brazil | 39.90 | 4.00 | 36.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Arms Race COUP Venezuela | 39.90 | 4.00 | 36.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Venezuela, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Arms Race COUP Egypt | 39.15 | 4.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Arms Race COUP Libya | 39.15 | 4.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR4 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], Voice of America[75], Defectors[108]`
- state: `VP 6, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | Blockade COUP Colombia | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 4 | Vietnam Revolts INFLUENCE East Germany, West Germany | 31.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Arab-Israeli War INFLUENCE East Germany, West Germany | 31.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], UN Intervention[32], Cultural Revolution[61], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Egypt | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Puppet Governments COUP Libya | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Grain Sales to Soviets COUP Egypt | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Grain Sales to Soviets COUP Libya | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Puppet Governments COUP Syria | 30.90 | 4.00 | 27.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 132: T9 AR5 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Voice of America[75], Defectors[108]`
- state: `VP 6, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Arab-Israeli War COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Arab-Israeli War COUP Colombia | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Guatemala | 20.80 | 4.00 | 17.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Blockade COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], UN Intervention[32], Cultural Revolution[61], Grain Sales to Soviets[68]`
- state: `VP 6, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Grain Sales to Soviets COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Grain Sales to Soviets COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Zimbabwe | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Grain Sales to Soviets COUP Colombia | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR6 USSR

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Voice of America[75], Defectors[108]`
- state: `VP 6, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Colombia | 16.70 | 4.00 | 12.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP Guatemala | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Voice of America COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Defectors COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], UN Intervention[32], Cultural Revolution[61]`
- state: `VP 6, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Cultural Revolution COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Fidel COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | UN Intervention COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Zimbabwe | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR7 USSR

- chosen: `Voice of America [75] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Voice of America[75], Defectors[108]`
- state: `VP 6, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Defectors COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Voice of America COUP Colombia | 13.05 | 4.00 | 25.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Defectors COUP Colombia | 13.05 | 4.00 | 25.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Voice of America COUP Guatemala | 12.80 | 4.00 | 25.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 US

- chosen: `Cultural Revolution [61] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Fidel[8], Cultural Revolution[61]`
- state: `VP 6, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Fidel COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Cultural Revolution COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Cultural Revolution COUP Zimbabwe | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Cultural Revolution COUP Colombia | 15.40 | 4.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 138: T10 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], CIA Created[26], Nuclear Test Ban[34], We Will Bury You[53], Nixon Plays the China Card[72], Alliance for Progress[79], Reagan Bombs Libya[87], Chernobyl[97]`
- state: `VP 6, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Alliance for Progress EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 139: T10 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Duck and Cover[4], Fidel[8], Olympic Games[20], CIA Created[26], UN Intervention[32], Summit[48], Voice of America[75], North Sea Oil[89], Colonial Rear Guards[110]`
- state: `VP 6, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 140: T10 AR1 USSR

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], CIA Created[26], We Will Bury You[53], Nixon Plays the China Card[72], Alliance for Progress[79], Reagan Bombs Libya[87], Chernobyl[97]`
- state: `VP 7, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, West Germany, Cuba | 64.52 | 6.00 | 70.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:11.43 |
| 2 | We Will Bury You COUP Indonesia | 61.36 | 4.00 | 57.96 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 3 | We Will Bury You COUP Saharan States | 55.11 | 4.00 | 51.71 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 4 | We Will Bury You COUP Algeria | 46.21 | 4.00 | 42.81 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:10, milops_urgency:1.43, expected_swing:3.5 |
| 5 | We Will Bury You COUP Mexico | 45.46 | 4.00 | 42.06 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:10, milops_urgency:1.43, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Olympic Games[20], CIA Created[26], UN Intervention[32], Summit[48], Voice of America[75], North Sea Oil[89], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, West Germany, Nigeria | 47.92 | 6.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:11.43 |
| 2 | North Sea Oil INFLUENCE East Germany, West Germany, Nigeria | 47.92 | 6.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:11.43 |
| 3 | Summit COUP Libya | 45.61 | 4.00 | 42.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |
| 4 | North Sea Oil COUP Libya | 45.61 | 4.00 | 42.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |
| 5 | Summit COUP Algeria | 39.86 | 4.00 | 36.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:10, milops_urgency:1.43, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR2 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:10`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], CIA Created[26], Nixon Plays the China Card[72], Alliance for Progress[79], Reagan Bombs Libya[87], Chernobyl[97]`
- state: `VP 7, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Indonesia | 42.78 | 4.00 | 38.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 36.53 | 4.00 | 32.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Haiti | 35.78 | 4.00 | 31.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 4 | Duck and Cover COUP Indonesia | 35.48 | 4.00 | 51.93 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Indonesia | 35.48 | 4.00 | 51.93 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 143: T10 AR2 US

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Olympic Games[20], CIA Created[26], UN Intervention[32], Voice of America[75], North Sea Oil[89], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 3, MilOps U1/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | North Sea Oil COUP Libya | 40.08 | 4.00 | 36.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:10, milops_urgency:1.67, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | North Sea Oil COUP Syria | 37.58 | 4.00 | 34.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 4 | North Sea Oil COUP Algeria | 34.33 | 4.00 | 30.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:10, milops_urgency:1.67, defcon_penalty:3, expected_swing:2.5 |
| 5 | Olympic Games COUP Libya | 33.73 | 4.00 | 30.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:10, milops_urgency:1.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR3 USSR

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Duck and Cover[4], CIA Created[26], Nixon Plays the China Card[72], Alliance for Progress[79], Reagan Bombs Libya[87], Chernobyl[97]`
- state: `VP 7, DEFCON 3, MilOps U1/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Saharan States | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Alliance for Progress COUP Saharan States | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Chernobyl COUP Saharan States | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Duck and Cover COUP Haiti | 28.75 | 4.00 | 45.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Haiti | 28.75 | 4.00 | 45.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 145: T10 AR3 US

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Olympic Games[20], CIA Created[26], UN Intervention[32], Voice of America[75], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 3, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Voice of America COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | CIA Created COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 4 | UN Intervention COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games COUP Libya | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:10, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 146: T10 AR4 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Nixon Plays the China Card[72], Alliance for Progress[79], Reagan Bombs Libya[87], Chernobyl[97]`
- state: `VP 7, DEFCON 3, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Chernobyl COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Alliance for Progress COUP Haiti | 28.65 | 4.00 | 45.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Chernobyl COUP Haiti | 28.65 | 4.00 | 45.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 US

- chosen: `Voice of America [75] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Fidel[8], CIA Created[26], UN Intervention[32], Voice of America[75], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 3, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | CIA Created COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 4 | Voice of America COUP Libya | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Voice of America COUP Syria | 31.90 | 4.00 | 28.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR5 USSR

- chosen: `Chernobyl [97] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Nixon Plays the China Card[72], Reagan Bombs Libya[87], Chernobyl[97]`
- state: `VP 7, DEFCON 3, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl COUP Nigeria | 33.07 | 4.00 | 49.52 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:2.33, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Nigeria | 30.72 | 4.00 | 43.02 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:2.33, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Nigeria | 30.72 | 4.00 | 43.02 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:2.33, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Chernobyl COUP Haiti | 29.82 | 4.00 | 46.27 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | CIA Created COUP Nigeria | 28.37 | 4.00 | 36.52 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:2.33, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 149: T10 AR5 US

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Fidel[8], CIA Created[26], UN Intervention[32], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 38.53 | 4.00 | 34.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 38.53 | 4.00 | 34.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:2.5 |
| 3 | Fidel COUP Saharan States | 28.88 | 4.00 | 41.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Saharan States | 28.88 | 4.00 | 41.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP SE African States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR6 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Nixon Plays the China Card[72], Reagan Bombs Libya[87]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Haiti | 29.80 | 4.00 | 42.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Reagan Bombs Libya COUP Haiti | 29.80 | 4.00 | 42.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Haiti | 27.45 | 4.00 | 35.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Fidel[8], UN Intervention[32], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 41.20 | 4.00 | 37.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:2.5 |
| 2 | Fidel COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | UN Intervention COUP SE African States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Zimbabwe | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR7 USSR

- chosen: `Reagan Bombs Libya [87] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Reagan Bombs Libya[87]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya COUP Cameroon | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Reagan Bombs Libya COUP Saharan States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Colombia | 15.05 | 4.00 | 27.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP Dominican Republic | 14.80 | 4.00 | 27.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Dominican Republic, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Reagan Bombs Libya COUP Guatemala | 14.80 | 4.00 | 27.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 US

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Fidel[8], Colonial Rear Guards[110]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Fidel COUP SE African States | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Fidel COUP Zimbabwe | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Saharan States | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP SE African States | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +20, DEFCON +1, MilOps U-3/A-2`
