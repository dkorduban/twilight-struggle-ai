# minimal_hybrid detailed rollout log

- seed: `20260402`
- winner: `USSR`
- final_vp: `4`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], NATO[21], East European Unrest[29], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Romanian Abdication[12], Truman Doctrine[19], Independent Reds[22], CIA Created[26], US/Japan Mutual Defense Pact[27], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Arab-Israeli War[13], De Gaulle Leads France[17], Captured Nazi Scientist[18], NATO[21], East European Unrest[29], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Iran | 77.17 | 4.00 | 73.62 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Arab-Israeli War COUP Iran | 71.82 | 4.00 | 68.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Captured Nazi Scientist COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | UN Intervention COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | De Gaulle Leads France INFLUENCE West Germany, Japan, Thailand | 61.47 | 5.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Romanian Abdication[12], Truman Doctrine[19], Independent Reds[22], CIA Created[26], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Indonesia, Philippines | 43.67 | 5.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Special Relationship INFLUENCE Indonesia, Philippines | 43.67 | 5.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Socialist Governments INFLUENCE North Korea, Indonesia, Philippines | 41.07 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | De-Stalinization INFLUENCE North Korea, Indonesia, Philippines | 41.07 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Truman Doctrine COUP North Korea | 30.57 | 4.00 | 26.72 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Captured Nazi Scientist[18], NATO[21], East European Unrest[29], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, Japan, South Korea, Thailand | 56.20 | 5.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Arab-Israeli War INFLUENCE Japan, Thailand | 45.30 | 5.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 4 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | UN Intervention COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Romanian Abdication[12], Truman Doctrine[19], CIA Created[26], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, Japan | 44.90 | 5.00 | 41.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:1.60 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan, North Korea | 42.30 | 5.00 | 59.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 42.30 | 5.00 | 59.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Truman Doctrine COUP North Korea | 30.70 | 4.00 | 26.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.20, coup_access_open |
| 5 | CIA Created COUP North Korea | 30.70 | 4.00 | 26.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.20, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Captured Nazi Scientist[18], East European Unrest[29], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Arab-Israeli War INFLUENCE Pakistan, Thailand | 47.10 | 5.00 | 42.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, control_break:Thailand |
| 3 | Five Year Plan INFLUENCE Pakistan, Israel, Thailand | 43.85 | 5.00 | 59.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | East European Unrest INFLUENCE Pakistan, Israel, Thailand | 43.85 | 5.00 | 59.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], Romanian Abdication[12], Truman Doctrine[19], CIA Created[26], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, Turkey, North Korea | 34.60 | 5.00 | 52.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | De-Stalinization INFLUENCE East Germany, Turkey, North Korea | 34.60 | 5.00 | 52.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Truman Doctrine COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 4 | CIA Created COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 5 | Truman Doctrine INFLUENCE North Korea | 20.40 | 5.00 | 17.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], East European Unrest[29], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, North Korea, Thailand | 50.60 | 5.00 | 66.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | East European Unrest INFLUENCE East Germany, North Korea, Thailand | 50.60 | 5.00 | 66.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 4 | UN Intervention INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 5 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Truman Doctrine[19], CIA Created[26], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE France, Japan, Panama | 31.28 | 5.00 | 49.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Truman Doctrine COUP Syria | 23.63 | 4.00 | 19.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 3 | CIA Created COUP Syria | 23.63 | 4.00 | 19.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 4 | Truman Doctrine INFLUENCE France | 19.23 | 5.00 | 17.05 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.05, access_touch:France, non_coup_milops_penalty:2.67 |
| 5 | CIA Created INFLUENCE France | 19.23 | 5.00 | 17.05 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.05, access_touch:France, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], East European Unrest[29], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Pakistan, Israel, Thailand | 38.85 | 5.00 | 54.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | UN Intervention INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:1`
- hand: `Romanian Abdication[12], Truman Doctrine[19], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Syria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created COUP Syria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Israel | 18.25 | 4.00 | 14.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |
| 4 | CIA Created COUP Israel | 18.25 | 4.00 | 14.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |
| 5 | Truman Doctrine INFLUENCE Italy | 14.30 | 5.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 13: T1 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china`
- hand: `Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist REALIGN Israel | 3.04 | -1.00 | 4.20 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `none`
- hand: `Romanian Abdication[12], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Italy | 21.30 | 5.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy |
| 2 | CIA Created COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 3 | CIA Created COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication INFLUENCE Italy | 9.30 | 5.00 | 16.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |
| 5 | Romanian Abdication COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +2, DEFCON +1, MilOps U-3/A-1`

## Step 15: T2 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Korean War[11], COMECON[14], Olympic Games[20], Containment[25], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Blockade[10], Nasser[15], Marshall Plan[23], Decolonization[30], Red Scare/Purge[31], Nuclear Test Ban[34]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Vietnam Revolts EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Korean War[11], Olympic Games[20], Containment[25], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Pakistan, Thailand | 42.43 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | Korean War INFLUENCE Pakistan, Thailand | 42.43 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Olympic Games INFLUENCE Pakistan, Thailand | 42.43 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | The Cambridge Five INFLUENCE Pakistan, Thailand | 42.43 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 5 | Containment INFLUENCE India, Pakistan, Thailand | 39.83 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Blockade[10], Nasser[15], Decolonization[30], Red Scare/Purge[31], Nuclear Test Ban[34]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE West Germany, Japan, North Korea, Egypt | 64.78 | 5.00 | 63.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.67 |
| 2 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, Egypt | 64.78 | 5.00 | 63.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.67 |
| 3 | Duck and Cover INFLUENCE West Germany, Japan, Egypt | 49.38 | 5.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.67 |
| 4 | Red Scare/Purge COUP Syria | 40.68 | 4.00 | 37.28 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 5 | Nuclear Test Ban COUP Syria | 40.68 | 4.00 | 37.28 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Korean War[11], Olympic Games[20], Containment[25], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE North Korea, Thailand | 42.50 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Olympic Games INFLUENCE North Korea, Thailand | 42.50 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | The Cambridge Five INFLUENCE North Korea, Thailand | 42.50 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 4 | Containment INFLUENCE India, North Korea, Thailand | 39.90 | 5.00 | 58.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | NORAD INFLUENCE India, North Korea, Thailand | 39.90 | 5.00 | 58.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Blockade[10], Nasser[15], Decolonization[30], Nuclear Test Ban[34]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Japan, Egypt, Libya | 67.40 | 5.00 | 66.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:3.20 |
| 2 | Duck and Cover INFLUENCE Japan, Egypt, Libya | 51.90 | 5.00 | 50.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:3.20 |
| 3 | Nuclear Test Ban COUP Syria | 40.95 | 4.00 | 37.55 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 4 | Nuclear Test Ban COUP Indonesia | 38.60 | 4.00 | 35.20 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:5.5 |
| 5 | Duck and Cover COUP Syria | 35.60 | 4.00 | 32.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Olympic Games[20], Containment[25], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Philippines | 39.90 | 4.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 2 | The Cambridge Five COUP Philippines | 39.90 | 4.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 3 | Olympic Games COUP Egypt | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 4 | The Cambridge Five COUP Egypt | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 5 | Olympic Games INFLUENCE India, Thailand | 38.70 | 5.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 22: T2 AR3 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Blockade[10], Nasser[15], Decolonization[30]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Libya, Philippines | 51.85 | 5.00 | 51.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:4.00 |
| 2 | Duck and Cover COUP Syria | 36.00 | 4.00 | 32.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 3 | Duck and Cover COUP Lebanon | 24.40 | 4.00 | 20.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 4 | Duck and Cover COUP SE African States | 22.15 | 4.00 | 18.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 5 | Duck and Cover COUP Sudan | 22.15 | 4.00 | 18.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Containment[25], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE India, Thailand | 42.70 | 5.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45 |
| 2 | Containment INFLUENCE Italy, India, Thailand | 39.00 | 5.00 | 54.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE Italy, India, Thailand | 39.00 | 5.00 | 54.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Formosan Resolution INFLUENCE India, Thailand | 26.70 | 5.00 | 38.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, offside_ops_penalty |
| 5 | The Cambridge Five COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], Nasser[15], Decolonization[30]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Japan, Philippines | 18.97 | 5.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Decolonization INFLUENCE Japan, Philippines | 18.97 | 5.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Vietnam Revolts COUP Syria | 15.32 | 4.00 | 27.62 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Decolonization COUP Syria | 15.32 | 4.00 | 27.62 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Blockade COUP Syria | 12.97 | 4.00 | 21.12 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Containment[25], Formosan Resolution[35], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Italy, Philippines, Thailand | 37.90 | 5.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE Italy, Philippines, Thailand | 37.90 | 5.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE Italy, Thailand | 25.60 | 5.00 | 36.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Containment SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Decolonization[30]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Syria | 16.65 | 4.00 | 28.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Blockade COUP Syria | 14.30 | 4.00 | 22.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Nasser COUP Syria | 14.30 | 4.00 | 22.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Decolonization INFLUENCE Italy, Philippines | 13.60 | 5.00 | 38.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Blockade COUP Israel | 8.25 | 4.00 | 16.40 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 27: T2 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Formosan Resolution[35], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Saudi Arabia, Thailand | 37.45 | 5.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Saudi Arabia, Thailand | 25.45 | 5.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Italy | 12.30 | 5.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 2 | Nasser INFLUENCE Italy | 12.30 | 5.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 3 | Blockade COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Blockade COUP SE African States | -4.55 | 4.00 | 3.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Truman Doctrine[19], Olympic Games[20], Indo-Pakistani War[24], Suez Crisis[28], Decolonization[30], Red Scare/Purge[31], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Socialist Governments[7], Romanian Abdication[12], Nasser[15], Containment[25], UN Intervention[32], De-Stalinization[33], Special Relationship[37]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON -1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Truman Doctrine[19], Olympic Games[20], Indo-Pakistani War[24], Suez Crisis[28], Decolonization[30], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Japan, Indonesia, Thailand | 53.00 | 5.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Suez Crisis COUP Egypt | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Olympic Games INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Indo-Pakistani War INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Decolonization INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Romanian Abdication[12], Nasser[15], Containment[25], UN Intervention[32], De-Stalinization[33], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Indonesia, Philippines | 38.85 | 5.00 | 38.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:4.00 |
| 2 | Containment COUP Iraq | 29.10 | 4.00 | 25.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Special Relationship COUP Iraq | 25.50 | 4.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open |
| 4 | Containment COUP Lebanon | 25.40 | 4.00 | 21.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 5 | UN Intervention COUP Iraq | 24.65 | 4.00 | 20.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Truman Doctrine[19], Olympic Games[20], Indo-Pakistani War[24], Decolonization[30], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Thailand | 36.50 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | Indo-Pakistani War INFLUENCE Japan, Thailand | 36.50 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 3 | Decolonization INFLUENCE Japan, Thailand | 36.50 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 4 | Olympic Games COUP Egypt | 33.55 | 4.00 | 29.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Egypt | 33.55 | 4.00 | 29.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Romanian Abdication[12], Nasser[15], UN Intervention[32], De-Stalinization[33], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Iraq | 25.90 | 4.00 | 22.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open |
| 2 | UN Intervention COUP Iraq | 25.05 | 4.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open |
| 3 | Special Relationship COUP Israel | 19.50 | 4.00 | 15.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3 |
| 4 | Special Relationship COUP Lebanon | 19.45 | 4.00 | 15.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | UN Intervention COUP Israel | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 35: T3 AR3 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Truman Doctrine[19], Indo-Pakistani War[24], Decolonization[30], NORAD[38]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan, Thailand | 35.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | Decolonization INFLUENCE Japan, Thailand | 35.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 30.85 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | NORAD INFLUENCE Japan, Egypt, Thailand | 30.85 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Truman Doctrine INFLUENCE Thailand | 7.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Romanian Abdication[12], Nasser[15], UN Intervention[32], De-Stalinization[33]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Iraq | 19.15 | 5.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.00 |
| 2 | Socialist Governments INFLUENCE Japan, Iraq | 15.00 | 5.00 | 32.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | De-Stalinization INFLUENCE Japan, Iraq | 15.00 | 5.00 | 32.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | UN Intervention COUP SE African States | 9.45 | 4.00 | 5.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Sudan | 9.45 | 4.00 | 5.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Truman Doctrine[19], Decolonization[30], NORAD[38]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Iraq, Thailand | 36.45 | 5.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 2 | Five Year Plan INFLUENCE Japan, Iraq, Thailand | 32.45 | 5.00 | 55.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | NORAD INFLUENCE Japan, Iraq, Thailand | 32.45 | 5.00 | 55.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Truman Doctrine INFLUENCE Thailand | 5.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Five Year Plan SPACE | 0.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], Romanian Abdication[12], Nasser[15], De-Stalinization[33]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Japan, Saudi Arabia | 14.33 | 5.00 | 32.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | De-Stalinization INFLUENCE Japan, Saudi Arabia | 14.33 | 5.00 | 32.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Romanian Abdication INFLUENCE Saudi Arabia | 6.48 | 5.00 | 16.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Nasser INFLUENCE Saudi Arabia | 6.48 | 5.00 | 16.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Socialist Governments SPACE | 5.88 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], NORAD[38]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 15.85 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | NORAD INFLUENCE Japan, Egypt, Thailand | 15.85 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 3 | Truman Doctrine INFLUENCE Thailand | -7.70 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 4 | Five Year Plan SPACE | -12.45 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 5 | NORAD SPACE | -12.45 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], De-Stalinization[33]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, Egypt | 12.40 | 5.00 | 34.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Romanian Abdication INFLUENCE Egypt | 4.55 | 5.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Nasser INFLUENCE Egypt | 4.55 | 5.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | De-Stalinization SPACE | 1.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | De-Stalinization COUP SE African States | 1.15 | 4.00 | 17.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], NORAD[38]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Sudan | 13.15 | 4.00 | 29.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Sudan | 8.45 | 4.00 | 16.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | NORAD INFLUENCE Japan, Libya, Thailand | 3.85 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:33.00 |
| 4 | Truman Doctrine INFLUENCE Thailand | -19.70 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:33.00 |
| 5 | NORAD SPACE | -24.45 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:33.00 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 42: T3 AR6 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Sudan | 22.45 | 4.00 | 30.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Nasser COUP Sudan | 22.45 | 4.00 | 30.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP SE African States | 0.45 | 4.00 | 8.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Zimbabwe | 0.45 | 4.00 | 8.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP SE African States | 0.45 | 4.00 | 8.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 43: T4 AR0 USSR

- chosen: `Brezhnev Doctrine [54] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Allende[57], Flower Power[62], Nixon Plays the China Card[72], Sadat Expels Soviets[73], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Allende EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Independent Reds[22], Indo-Pakistani War[24], Special Relationship[37], Cuban Missile Crisis[43], South African Unrest[56], Muslim Revolution[59], U2 Incident[63], Liberation Theology[76]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Portuguese Empire Crumbles[55], Allende[57], Flower Power[62], Nixon Plays the China Card[72], Sadat Expels Soviets[73], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE UK, Mexico, Algeria | 49.43 | 5.00 | 49.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 2 | Portuguese Empire Crumbles INFLUENCE UK, Mexico, Algeria | 49.43 | 5.00 | 49.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 3 | Flower Power INFLUENCE UK, Mexico, Algeria | 49.43 | 5.00 | 49.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 4 | Sadat Expels Soviets INFLUENCE UK, West Germany, Mexico, Algeria | 45.43 | 5.00 | 65.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Alliance for Progress INFLUENCE UK, West Germany, Mexico, Algeria | 45.43 | 5.00 | 65.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Independent Reds[22], Indo-Pakistani War[24], Special Relationship[37], South African Unrest[56], Muslim Revolution[59], U2 Incident[63], Liberation Theology[76]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE Mexico, Algeria, Morocco, South Africa | 42.58 | 5.00 | 66.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Independent Reds INFLUENCE Mexico, Morocco | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 3 | Indo-Pakistani War INFLUENCE Mexico, Morocco | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 4 | Special Relationship INFLUENCE Mexico, Morocco | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 5 | U2 Incident INFLUENCE Mexico, Morocco, South Africa | 30.53 | 5.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Portuguese Empire Crumbles[55], Allende[57], Flower Power[62], Nixon Plays the China Card[72], Sadat Expels Soviets[73], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany, Morocco | 47.87 | 5.00 | 48.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 2 | Flower Power INFLUENCE East Germany, West Germany, Morocco | 47.87 | 5.00 | 48.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany, Morocco | 43.27 | 5.00 | 64.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Alliance for Progress INFLUENCE East Germany, France, West Germany, Morocco | 43.27 | 5.00 | 64.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Allende INFLUENCE West Germany, Morocco | 32.47 | 5.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Independent Reds[22], Indo-Pakistani War[24], Special Relationship[37], South African Unrest[56], U2 Incident[63], Liberation Theology[76]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, South Africa | 37.32 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 37.32 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 3 | Special Relationship INFLUENCE West Germany, South Africa | 37.32 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 4 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 32.72 | 5.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Korean War INFLUENCE West Germany, South Africa | 21.32 | 5.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Allende[57], Flower Power[62], Nixon Plays the China Card[72], Sadat Expels Soviets[73], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, France, West Germany | 45.55 | 5.00 | 47.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.40 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany, Cuba | 40.95 | 5.00 | 62.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Alliance for Progress INFLUENCE East Germany, France, West Germany, Cuba | 40.95 | 5.00 | 62.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Allende INFLUENCE East Germany, West Germany | 30.15 | 5.00 | 31.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.40 |
| 5 | Lone Gunman INFLUENCE East Germany, West Germany | 30.15 | 5.00 | 31.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Indo-Pakistani War[24], Special Relationship[37], South African Unrest[56], U2 Incident[63], Liberation Theology[76]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 31.25 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 2 | Special Relationship INFLUENCE West Germany, South Africa | 31.25 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 3 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 26.65 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Korean War INFLUENCE West Germany, South Africa | 15.25 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | South African Unrest INFLUENCE West Germany, South Africa | 15.25 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Allende[57], Nixon Plays the China Card[72], Sadat Expels Soviets[73], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany, Cuba | 39.35 | 5.00 | 62.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany, Cuba | 39.35 | 5.00 | 62.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Allende INFLUENCE East Germany, West Germany | 28.55 | 5.00 | 31.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Lone Gunman INFLUENCE East Germany, West Germany | 28.55 | 5.00 | 31.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, France, West Germany | 27.95 | 5.00 | 47.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Special Relationship[37], South African Unrest[56], U2 Incident[63], Liberation Theology[76]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Korean War INFLUENCE West Germany, South Africa | 13.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | South African Unrest INFLUENCE West Germany, South Africa | 13.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Liberation Theology INFLUENCE West Germany, South Africa | 13.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Allende[57], Nixon Plays the China Card[72], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany, Libya | 36.33 | 5.00 | 62.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Libya:13.20, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Allende INFLUENCE East Germany, West Germany | 25.88 | 5.00 | 31.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.67 |
| 3 | Lone Gunman INFLUENCE East Germany, West Germany | 25.88 | 5.00 | 31.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.67 |
| 4 | Nixon Plays the China Card INFLUENCE East Germany, France, West Germany | 25.28 | 5.00 | 47.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Nixon Plays the China Card SPACE | -2.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], South African Unrest[56], U2 Incident[63], Liberation Theology[76]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE West Germany, Libya, South Africa | 25.03 | 5.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Libya:13.20, control_break:Libya, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Korean War INFLUENCE Libya, South Africa | 13.03 | 5.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | South African Unrest INFLUENCE Libya, South Africa | 13.03 | 5.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Liberation Theology INFLUENCE Libya, South Africa | 13.03 | 5.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Korean War SPACE | -2.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Allende [57] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Allende[57], Nixon Plays the China Card[72], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE France, West Germany | 13.55 | 5.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:28.00 |
| 2 | Lone Gunman INFLUENCE France, West Germany | 13.55 | 5.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:28.00 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, France, West Germany | 12.95 | 5.00 | 52.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 4 | Nixon Plays the China Card SPACE | -20.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 5 | Allende REALIGN Mexico | -22.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], South African Unrest[56], Liberation Theology[76]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, South Africa | -6.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 2 | South African Unrest INFLUENCE West Germany, South Africa | -6.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 3 | Liberation Theology INFLUENCE West Germany, South Africa | -6.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 4 | Korean War SPACE | -20.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 5 | South African Unrest SPACE | -20.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nixon Plays the China Card[72], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE East Germany, West Germany | -7.45 | 5.00 | 31.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:44.00 |
| 2 | Nixon Plays the China Card INFLUENCE East Germany, France, West Germany | -8.05 | 5.00 | 47.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 3 | Nixon Plays the China Card SPACE | -36.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 4 | Lone Gunman REALIGN Mexico | -38.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:44.00 |
| 5 | Lone Gunman EVENT | -41.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:44.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `South African Unrest[56], Liberation Theology[76]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE West Germany, South Africa | -22.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 2 | Liberation Theology INFLUENCE West Germany, South Africa | -22.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 3 | South African Unrest SPACE | -36.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 4 | Liberation Theology SPACE | -36.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 5 | South African Unrest EVENT | -50.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:44.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 59: T5 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Romanian Abdication[12], NATO[21], Decolonization[30], De-Stalinization[33], Nuclear Test Ban[34], Special Relationship[37], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Summit [48] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], Suez Crisis[28], The Cambridge Five[36], Summit[48], We Will Bury You[53], Lonely Hearts Club Band[65], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | We Will Bury You EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Romanian Abdication[12], NATO[21], Decolonization[30], De-Stalinization[33], Special Relationship[37], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 46.09 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 2 | NATO INFLUENCE East Germany, France, West Germany, Mexico | 36.89 | 5.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 3 | Decolonization INFLUENCE East Germany, West Germany | 30.69 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 4 | Latin American Death Squads INFLUENCE East Germany, West Germany | 30.69 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 30.69 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], Suez Crisis[28], The Cambridge Five[36], We Will Bury You[53], Lonely Hearts Club Band[65], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, West Germany, South Africa | 38.74 | 5.00 | 64.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 2 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 31.94 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 27.34 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 4 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 27.34 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 5 | Fidel INFLUENCE West Germany, South Africa | 15.94 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Duck and Cover[4], Romanian Abdication[12], NATO[21], Decolonization[30], Special Relationship[37], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE East Germany, France, West Germany, Mexico | 35.93 | 5.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 2 | Decolonization INFLUENCE East Germany, West Germany | 29.73 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 29.73 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 29.73 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 5 | Duck and Cover INFLUENCE East Germany, France, West Germany | 25.13 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], Suez Crisis[28], The Cambridge Five[36], Lonely Hearts Club Band[65], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 30.98 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 2 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 26.38 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 26.38 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | Fidel INFLUENCE West Germany, South Africa | 14.98 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Arab-Israeli War INFLUENCE West Germany, South Africa | 14.98 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Romanian Abdication[12], Decolonization[30], Special Relationship[37], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Mexico | 32.80 | 5.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:8.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany, Mexico | 32.80 | 5.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:8.00 |
| 3 | Colonial Rear Guards INFLUENCE West Germany, Mexico | 32.80 | 5.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:8.00 |
| 4 | Duck and Cover INFLUENCE East Germany, West Germany, Mexico | 28.20 | 5.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Romanian Abdication INFLUENCE Mexico | 16.80 | 5.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], Suez Crisis[28], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Fidel INFLUENCE West Germany, South Africa | 13.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Arab-Israeli War INFLUENCE West Germany, South Africa | 13.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | The Cambridge Five INFLUENCE West Germany, South Africa | 13.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Romanian Abdication[12], Special Relationship[37], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | 26.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 26.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 3 | Duck and Cover INFLUENCE East Germany, France, West Germany | 21.80 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Romanian Abdication INFLUENCE West Germany | 11.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 5 | Special Relationship INFLUENCE East Germany, West Germany | 10.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Suez Crisis[28], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 23.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Fidel INFLUENCE West Germany, South Africa | 11.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Arab-Israeli War INFLUENCE West Germany, South Africa | 11.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | The Cambridge Five INFLUENCE West Germany, South Africa | 11.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Panama Canal Returned INFLUENCE South Africa | 11.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Romanian Abdication[12], Special Relationship[37], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 23.07 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:13.33 |
| 2 | Duck and Cover INFLUENCE East Germany, France, West Germany | 18.47 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Romanian Abdication INFLUENCE West Germany | 7.67 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:13.33 |
| 4 | Special Relationship INFLUENCE East Germany, West Germany | 7.07 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Special Relationship SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, South Africa | 8.32 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Arab-Israeli War INFLUENCE West Germany, South Africa | 8.32 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | The Cambridge Five INFLUENCE West Germany, South Africa | 8.32 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Panama Canal Returned INFLUENCE South Africa | 8.32 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:13.33 |
| 5 | Fidel SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Duck and Cover[4], Romanian Abdication[12], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | -3.20 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -14.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:35.00 |
| 3 | Special Relationship INFLUENCE East Germany, West Germany | -14.60 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 4 | Special Relationship SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | Duck and Cover SPACE | -27.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, South Africa | -13.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, South Africa | -13.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 3 | Panama Canal Returned INFLUENCE South Africa | -13.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:35.00 |
| 4 | Arab-Israeli War SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | The Cambridge Five SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | -34.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:55.00 |
| 2 | Special Relationship INFLUENCE East Germany, West Germany | -34.60 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 3 | Special Relationship SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 4 | Romanian Abdication REALIGN Mexico | -51.93 | -1.00 | 4.22 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |
| 5 | Romanian Abdication EVENT | -52.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, South Africa | -33.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 2 | Panama Canal Returned INFLUENCE South Africa | -33.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:55.00 |
| 3 | The Cambridge Five SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 4 | Panama Canal Returned REALIGN South Africa | -50.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |
| 5 | Panama Canal Returned EVENT | -52.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 75: T6 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Truman Doctrine[19], CIA Created[26], Suez Crisis[28], De-Stalinization[33], Bear Trap[47], OPEC[64], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Socialist Governments[7], De Gaulle Leads France[17], Captured Nazi Scientist[18], Containment[25], UN Intervention[32], Nuclear Subs[44], OAS Founded[71], Voice of America[75]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Truman Doctrine[19], CIA Created[26], De-Stalinization[33], Bear Trap[47], OPEC[64], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 44.94 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 44.94 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 29.54 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 4 | Bear Trap INFLUENCE East Germany, France, West Germany | 24.94 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 5 | Nasser INFLUENCE West Germany | 14.14 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Captured Nazi Scientist[18], Containment[25], UN Intervention[32], Nuclear Subs[44], OAS Founded[71], Voice of America[75]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Israel, South Africa | 47.04 | 5.00 | 49.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | Nuclear Subs INFLUENCE Israel, South Africa | 31.04 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | Voice of America INFLUENCE Israel, South Africa | 31.04 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 4 | Socialist Governments INFLUENCE West Germany, Israel, South Africa | 27.04 | 5.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 5 | De Gaulle Leads France INFLUENCE West Germany, Israel, South Africa | 27.04 | 5.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Truman Doctrine[19], CIA Created[26], Bear Trap[47], OPEC[64], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | One Small Step INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Bear Trap INFLUENCE East Germany, France, West Germany | 23.80 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Nasser INFLUENCE West Germany | 13.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 12.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Captured Nazi Scientist[18], UN Intervention[32], Nuclear Subs[44], OAS Founded[71], Voice of America[75]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Voice of America INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Captured Nazi Scientist INFLUENCE South Africa | 13.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Truman Doctrine[19], CIA Created[26], Bear Trap[47], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 26.80 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 2 | Bear Trap INFLUENCE East Germany, France, West Germany | 22.20 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | Nasser INFLUENCE West Germany | 11.40 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 10.80 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Truman Doctrine INFLUENCE West Germany | -0.60 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Captured Nazi Scientist[18], UN Intervention[32], OAS Founded[71], Voice of America[75]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, South Africa | 28.05 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 2 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 23.45 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 23.45 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Captured Nazi Scientist INFLUENCE South Africa | 12.05 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 5 | UN Intervention INFLUENCE South Africa | 12.05 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Nasser[15], Truman Doctrine[19], CIA Created[26], Bear Trap[47], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 19.80 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Nasser INFLUENCE West Germany | 9.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 8.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Truman Doctrine INFLUENCE West Germany | -3.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | CIA Created INFLUENCE West Germany | -3.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Captured Nazi Scientist[18], UN Intervention[32], OAS Founded[71]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 21.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 21.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Captured Nazi Scientist INFLUENCE South Africa | 9.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 4 | UN Intervention INFLUENCE South Africa | 9.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 5 | OAS Founded INFLUENCE South Africa | 9.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Truman Doctrine[19], CIA Created[26], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE West Germany | 5.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:16.00 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 4.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Truman Doctrine INFLUENCE West Germany | -7.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | CIA Created INFLUENCE West Germany | -7.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | John Paul II Elected Pope SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], UN Intervention[32], OAS Founded[71]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 17.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Captured Nazi Scientist INFLUENCE South Africa | 5.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:16.00 |
| 3 | UN Intervention INFLUENCE South Africa | 5.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:16.00 |
| 4 | OAS Founded INFLUENCE South Africa | 5.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:16.00 |
| 5 | De Gaulle Leads France SPACE | -8.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -21.60 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Truman Doctrine INFLUENCE West Germany | -33.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | CIA Created INFLUENCE West Germany | -33.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | John Paul II Elected Pope SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Truman Doctrine EVENT | -48.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], OAS Founded[71]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | -20.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 2 | UN Intervention INFLUENCE South Africa | -20.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 3 | OAS Founded INFLUENCE South Africa | -20.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 4 | Captured Nazi Scientist REALIGN South Africa | -37.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:42.00 |
| 5 | UN Intervention REALIGN South Africa | -37.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE West Germany | -57.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 2 | CIA Created INFLUENCE West Germany | -57.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | Truman Doctrine EVENT | -72.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |
| 4 | CIA Created EVENT | -72.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |
| 5 | Truman Doctrine REALIGN Mexico | -74.93 | -1.00 | 4.22 | 0.00 | -12.00 | -0.15 | 0.00 | offside_ops_penalty, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `UN Intervention[32], OAS Founded[71]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE South Africa | -44.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:66.00 |
| 2 | OAS Founded INFLUENCE South Africa | -44.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:66.00 |
| 3 | UN Intervention REALIGN South Africa | -61.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |
| 4 | OAS Founded REALIGN South Africa | -61.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |
| 5 | UN Intervention EVENT | -63.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 91: T7 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19], Red Scare/Purge[31], Brush War[39], ABM Treaty[60], Ussuri River Skirmish[77], Che[83]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Romanian Abdication[12], Olympic Games[20], Decolonization[30], UN Intervention[32], NORAD[38], Arms Race[42], How I Learned to Stop Worrying[49], Cultural Revolution[61]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19], Brush War[39], Ussuri River Skirmish[77], Che[83]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Che INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Blockade INFLUENCE West Germany | 13.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Nasser INFLUENCE West Germany | 13.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Olympic Games[20], Decolonization[30], UN Intervention[32], NORAD[38], Arms Race[42], How I Learned to Stop Worrying[49], Cultural Revolution[61]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, South Africa | 34.50 | 5.00 | 37.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Arms Race INFLUENCE West Germany, South Africa | 34.50 | 5.00 | 37.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | UN Intervention INFLUENCE West Germany | 18.00 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 4 | Olympic Games INFLUENCE West Germany | 17.85 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 5 | How I Learned to Stop Worrying INFLUENCE West Germany | 17.85 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19], Ussuri River Skirmish[77], Che[83]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 42.47 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 42.47 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 3 | Blockade INFLUENCE West Germany | 11.67 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 4 | Nasser INFLUENCE West Germany | 11.67 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 5 | Truman Doctrine INFLUENCE West Germany | -0.33 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Olympic Games[20], Decolonization[30], UN Intervention[32], Arms Race[42], How I Learned to Stop Worrying[49], Cultural Revolution[61]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE West Germany, South Africa | 33.17 | 5.00 | 37.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | UN Intervention INFLUENCE West Germany | 16.67 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:9.33 |
| 3 | Olympic Games INFLUENCE West Germany | 16.52 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:9.33 |
| 4 | How I Learned to Stop Worrying INFLUENCE West Germany | 16.52 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:9.33 |
| 5 | Cultural Revolution INFLUENCE West Germany, South Africa | 13.17 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19], Che[83]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 40.60 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 2 | Blockade INFLUENCE West Germany | 9.80 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 3 | Nasser INFLUENCE West Germany | 9.80 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 4 | Truman Doctrine INFLUENCE West Germany | -2.20 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Blockade REALIGN West Germany | -7.47 | -1.00 | 4.88 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Olympic Games[20], Decolonization[30], UN Intervention[32], How I Learned to Stop Worrying[49], Cultural Revolution[61]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | 14.80 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:11.20 |
| 2 | Olympic Games INFLUENCE West Germany | 14.65 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:11.20 |
| 3 | How I Learned to Stop Worrying INFLUENCE West Germany | 14.65 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:11.20 |
| 4 | Cultural Revolution INFLUENCE West Germany, South Africa | 11.30 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Romanian Abdication INFLUENCE West Germany | 2.80 | 5.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | 7.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 2 | Nasser INFLUENCE West Germany | 7.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 3 | Truman Doctrine INFLUENCE West Germany | -5.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Blockade REALIGN West Germany | -10.27 | -1.00 | 4.88 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:14.00 |
| 5 | Nasser REALIGN West Germany | -10.27 | -1.00 | 4.88 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Olympic Games[20], Decolonization[30], How I Learned to Stop Worrying[49], Cultural Revolution[61]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany | 11.85 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:14.00 |
| 2 | How I Learned to Stop Worrying INFLUENCE West Germany | 11.85 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:14.00 |
| 3 | Cultural Revolution INFLUENCE West Germany, South Africa | 8.50 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Romanian Abdication INFLUENCE West Germany | -0.00 | 5.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Decolonization INFLUENCE West Germany | -4.15 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Truman Doctrine[19]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE West Germany | 2.33 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:18.67 |
| 2 | Truman Doctrine INFLUENCE West Germany | -9.67 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Nasser REALIGN West Germany | -14.93 | -1.00 | 4.88 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:18.67 |
| 4 | Nasser EVENT | -16.32 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:18.67 |
| 5 | Truman Doctrine EVENT | -24.82 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], Decolonization[30], How I Learned to Stop Worrying[49], Cultural Revolution[61]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE West Germany | 7.18 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:18.67 |
| 2 | Cultural Revolution INFLUENCE West Germany, South Africa | 3.83 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Romanian Abdication INFLUENCE West Germany | -4.67 | 5.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 4 | Decolonization INFLUENCE West Germany | -8.82 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | Decolonization SPACE | -10.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Truman Doctrine[19]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE West Germany | -40.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Truman Doctrine EVENT | -55.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:49.00 |
| 3 | Truman Doctrine REALIGN West Germany | -57.27 | -1.00 | 4.88 | 0.00 | -12.00 | -0.15 | 0.00 | offside_ops_penalty, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30], Cultural Revolution[61]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE West Germany, South Africa | -26.50 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -35.00 | 5.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 3 | Decolonization INFLUENCE West Germany | -39.15 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Decolonization SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 5 | Cultural Revolution SPACE | -41.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE South Africa | -67.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 2 | Decolonization SPACE | -69.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | Decolonization INFLUENCE South Africa | -71.50 | 5.00 | 16.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 4 | Romanian Abdication EVENT | -83.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |
| 5 | Decolonization EVENT | -83.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T8 AR0 USSR

- chosen: `Aldrich Ames Remix [101] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Five Year Plan[5], UN Intervention[32], Bear Trap[47], South African Unrest[56], Allende[57], Marine Barracks Bombing[91], Tear Down this Wall[99], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Aldrich Ames Remix EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Marine Barracks Bombing EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 107: T8 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Containment[25], Brush War[39], Summit[48], How I Learned to Stop Worrying[49], Junta[50], Grain Sales to Soviets[68], OAS Founded[71], North Sea Oil[89]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR1 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Five Year Plan[5], UN Intervention[32], Bear Trap[47], South African Unrest[56], Allende[57], Marine Barracks Bombing[91], Tear Down this Wall[99], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 28.76 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 28.76 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 28.76 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Five Year Plan INFLUENCE East Germany, France, West Germany | 24.91 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 5 | Bear Trap INFLUENCE East Germany, France, West Germany | 24.91 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 US

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Brush War[39], How I Learned to Stop Worrying[49], Junta[50], Grain Sales to Soviets[68], OAS Founded[71], North Sea Oil[89]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, Poland, West Germany | 66.21 | 5.00 | 70.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, France, West Germany | 50.06 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 3 | Junta INFLUENCE East Germany, France, West Germany | 50.06 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, France, West Germany | 50.06 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 5 | Brush War INFLUENCE East Germany, France, Poland, West Germany | 46.21 | 5.00 | 70.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR2 USSR

- chosen: `Marine Barracks Bombing [91] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Five Year Plan[5], UN Intervention[32], Bear Trap[47], Allende[57], Marine Barracks Bombing[91], Tear Down this Wall[99], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Five Year Plan INFLUENCE East Germany, France, West Germany | 23.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Bear Trap INFLUENCE East Germany, France, West Germany | 23.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 23.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Brush War[39], How I Learned to Stop Worrying[49], Junta[50], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, France, West Germany | 48.53 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 2 | Junta INFLUENCE East Germany, France, West Germany | 48.53 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, France, West Germany | 48.53 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 4 | Brush War INFLUENCE East Germany, France, West Germany, Cuba | 44.43 | 5.00 | 70.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | OAS Founded INFLUENCE East Germany, West Germany | 32.38 | 5.00 | 38.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR3 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Five Year Plan[5], UN Intervention[32], Bear Trap[47], Allende[57], Tear Down this Wall[99], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 25.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Five Year Plan INFLUENCE East Germany, France, West Germany | 21.25 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 3 | Bear Trap INFLUENCE East Germany, France, West Germany | 21.25 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 21.25 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | UN Intervention INFLUENCE West Germany | 8.95 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Brush War[39], Junta[50], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, France, West Germany | 46.40 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 2 | Grain Sales to Soviets INFLUENCE East Germany, France, West Germany | 46.40 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 3 | Brush War INFLUENCE East Germany, France, West Germany, Cuba | 42.30 | 5.00 | 70.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | OAS Founded INFLUENCE East Germany, West Germany | 30.25 | 5.00 | 38.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 5 | Brush War SPACE | -5.25 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Five Year Plan[5], UN Intervention[32], Bear Trap[47], Allende[57], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Bear Trap INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | UN Intervention INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | Allende INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Brush War[39], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, France, West Germany | 43.20 | 5.00 | 54.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 2 | Brush War INFLUENCE East Germany, France, West Germany, Cuba | 39.10 | 5.00 | 70.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | OAS Founded INFLUENCE East Germany, West Germany | 27.05 | 5.00 | 38.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 4 | Brush War SPACE | -8.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | OAS Founded REALIGN West Germany | -11.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR5 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `UN Intervention[32], Bear Trap[47], Allende[57], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 12.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 12.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | UN Intervention INFLUENCE West Germany | 0.42 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 4 | Allende INFLUENCE West Germany | 0.42 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 5 | Bear Trap SPACE | -13.78 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Brush War[39], OAS Founded[71]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany, Cuba | 33.77 | 5.00 | 70.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | OAS Founded INFLUENCE East Germany, West Germany | 21.72 | 5.00 | 38.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:21.33 |
| 3 | Brush War SPACE | -13.78 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | OAS Founded REALIGN West Germany | -17.19 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:21.33 |
| 5 | OAS Founded EVENT | -18.98 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR6 USSR

- chosen: `Tear Down this Wall [99] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `UN Intervention[32], Allende[57], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | -21.95 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | UN Intervention INFLUENCE West Germany | -34.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 3 | Allende INFLUENCE West Germany | -34.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 4 | Tear Down this Wall SPACE | -48.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | UN Intervention REALIGN West Germany | -51.85 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 US

- chosen: `OAS Founded [71] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `OAS Founded[71]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded INFLUENCE East Germany, West Germany | -12.95 | 5.00 | 38.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:56.00 |
| 2 | OAS Founded REALIGN West Germany | -51.85 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |
| 3 | OAS Founded EVENT | -53.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR7 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `UN Intervention[32], Allende[57]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | -66.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 2 | Allende INFLUENCE West Germany | -66.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 3 | UN Intervention REALIGN West Germany | -83.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 4 | Allende REALIGN West Germany | -83.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 5 | UN Intervention EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T9 AR0 USSR

- chosen: `Missile Envy [52] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Nasser[15], NATO[21], Missile Envy[52], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Puppet Governments[67], Star Wars[88], Iran-Iraq War[105]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T9 AR0 US

- chosen: `Latin American Death Squads [70] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Truman Doctrine[19], U2 Incident[63], OPEC[64], Latin American Death Squads[70], Nixon Plays the China Card[72], Iranian Hostage Crisis[85]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | U2 Incident EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 123: T9 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Blockade[10], Nasser[15], NATO[21], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Puppet Governments[67], Star Wars[88], Iran-Iraq War[105]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE East Germany, France, West Germany, Indonesia | 35.96 | 5.00 | 65.85 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, Indonesia | 27.66 | 5.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, non_coup_milops_penalty:10.29 |
| 3 | Iran-Iraq War INFLUENCE West Germany, Indonesia | 27.66 | 5.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, non_coup_milops_penalty:10.29 |
| 4 | Lonely Hearts Club Band INFLUENCE West Germany, Indonesia | 11.66 | 5.00 | 33.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | Puppet Governments INFLUENCE West Germany, Indonesia | 11.66 | 5.00 | 33.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR1 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Truman Doctrine[19], U2 Incident[63], OPEC[64], Nixon Plays the China Card[72], Iranian Hostage Crisis[85]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 27.61 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 23.76 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 3 | U2 Incident INFLUENCE East Germany, France, West Germany | 23.76 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 4 | OPEC INFLUENCE East Germany, France, West Germany | 23.76 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 23.76 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR2 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Nasser[15], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Puppet Governments[67], Star Wars[88], Iran-Iraq War[105]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Iran-Iraq War INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 9.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Puppet Governments INFLUENCE East Germany, West Germany | 9.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Star Wars INFLUENCE East Germany, West Germany | 9.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR2 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Truman Doctrine[19], U2 Incident[63], OPEC[64], Iranian Hostage Crisis[85]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 22.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 22.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | OPEC INFLUENCE East Germany, France, West Germany | 22.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 22.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Korean War INFLUENCE East Germany, West Germany | 9.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR3 USSR

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Nasser[15], Lonely Hearts Club Band[65], Puppet Governments[67], Star Wars[88], Iran-Iraq War[105]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, West Germany | 23.50 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Star Wars INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | Blockade INFLUENCE West Germany | 7.35 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR3 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Truman Doctrine[19], U2 Incident[63], OPEC[64], Iranian Hostage Crisis[85]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 19.65 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 19.65 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 19.65 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Korean War INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | Arab-Israeli War INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR4 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Lonely Hearts Club Band[65], Puppet Governments[67], Star Wars[88]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Puppet Governments INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Star Wars INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Blockade INFLUENCE West Germany | 3.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 5 | Nasser INFLUENCE West Germany | 3.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR4 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Truman Doctrine[19], OPEC[64], Iranian Hostage Crisis[85]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 16.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 16.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Korean War INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Arab-Israeli War INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Truman Doctrine INFLUENCE West Germany | 3.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR5 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Puppet Governments[67], Star Wars[88]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Star Wars INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Blockade INFLUENCE West Germany | -2.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 4 | Nasser INFLUENCE West Germany | -2.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 5 | Puppet Governments SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR5 US

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Truman Doctrine[19], Iranian Hostage Crisis[85]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 10.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Korean War INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Arab-Israeli War INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Truman Doctrine INFLUENCE West Germany | -2.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 5 | Korean War SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR6 USSR

- chosen: `Star Wars [88] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Star Wars[88]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Blockade INFLUENCE West Germany | -41.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 3 | Nasser INFLUENCE West Germany | -41.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 4 | Star Wars SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Blockade REALIGN West Germany | -58.85 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR6 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Truman Doctrine[19]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Arab-Israeli War INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Truman Doctrine INFLUENCE West Germany | -41.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 4 | Korean War SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Arab-Israeli War SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR7 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | -77.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:99.00 |
| 2 | Nasser INFLUENCE West Germany | -77.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:99.00 |
| 3 | Blockade REALIGN West Germany | -94.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |
| 4 | Nasser REALIGN West Germany | -94.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |
| 5 | Blockade EVENT | -96.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR7 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Truman Doctrine[19]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | -77.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Truman Doctrine INFLUENCE West Germany | -77.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:99.00 |
| 3 | Arab-Israeli War SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Truman Doctrine REALIGN West Germany | -94.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |
| 5 | Truman Doctrine EVENT | -96.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T10 AR0 USSR

- chosen: `Fidel [8] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Indo-Pakistani War[24], CIA Created[26], UN Intervention[32], Special Relationship[37], Nuclear Subs[44], Lonely Hearts Club Band[65], Latin American Death Squads[70], Alliance for Progress[79]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Alliance for Progress EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T10 AR0 US

- chosen: `Bear Trap [47] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Decolonization[30], Special Relationship[37], Quagmire[45], Bear Trap[47], How I Learned to Stop Worrying[49], South African Unrest[56], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 139: T10 AR1 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Decolonization[30], Special Relationship[37], Quagmire[45], How I Learned to Stop Worrying[49], South African Unrest[56], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 3 | Voice of America INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 4 | Quagmire INFLUENCE East Germany, France, West Germany | 27.62 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 5 | Vietnam Revolts INFLUENCE East Germany, West Germany | 15.47 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR2 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Decolonization[30], Quagmire[45], How I Learned to Stop Worrying[49], South African Unrest[56], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Quagmire INFLUENCE East Germany, France, West Germany | 20.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Vietnam Revolts INFLUENCE East Germany, West Germany | 8.57 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Decolonization INFLUENCE East Germany, West Germany | 8.57 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR3 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Decolonization[30], Quagmire[45], South African Unrest[56], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Quagmire INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Vietnam Revolts INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Decolonization INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | South African Unrest INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR4 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `CIA Created[26], UN Intervention[32], Special Relationship[37], Lonely Hearts Club Band[65], Latin American Death Squads[70]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | 17.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Special Relationship INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | UN Intervention INFLUENCE West Germany | 1.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 5 | CIA Created INFLUENCE West Germany | -10.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR4 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Vietnam Revolts[9], Decolonization[30], Quagmire[45], South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, France, West Germany | 14.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Decolonization INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Panama Canal Returned INFLUENCE West Germany | 1.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR5 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `CIA Created[26], UN Intervention[32], Special Relationship[37], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | UN Intervention INFLUENCE West Germany | -4.92 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 4 | CIA Created INFLUENCE West Germany | -16.92 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 5 | Special Relationship SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR5 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Vietnam Revolts[9], Decolonization[30], South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Decolonization INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | Panama Canal Returned INFLUENCE West Germany | -4.92 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 5 | Vietnam Revolts SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `CIA Created[26], UN Intervention[32], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | UN Intervention INFLUENCE West Germany | -48.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 3 | CIA Created INFLUENCE West Germany | -60.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 4 | Lonely Hearts Club Band SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | UN Intervention REALIGN West Germany | -65.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | Panama Canal Returned INFLUENCE West Germany | -48.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 4 | Decolonization SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | South African Unrest SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR7 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | -88.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 2 | CIA Created INFLUENCE West Germany | -100.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 3 | UN Intervention REALIGN West Germany | -105.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 4 | UN Intervention EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | CIA Created EVENT | -116.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:110.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | -88.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | -88.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 3 | South African Unrest SPACE | -102.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 4 | Panama Canal Returned REALIGN West Germany | -105.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | Panama Canal Returned EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP +4, DEFCON +0, MilOps U+0/A+0`
