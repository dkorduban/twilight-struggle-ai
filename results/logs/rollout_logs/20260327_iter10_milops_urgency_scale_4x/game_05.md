# minimal_hybrid detailed rollout log

- seed: `20260405`
- winner: `US`
- final_vp: `-2`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Socialist Governments[7], Blockade[10], Nasser[15], Suez Crisis[28], Decolonization[30], De-Stalinization[33], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], Captured Nazi Scientist[18], NATO[21], East European Unrest[29], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Blockade[10], Nasser[15], Suez Crisis[28], Decolonization[30], De-Stalinization[33], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Iran | 77.17 | 4.00 | 73.62 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | De-Stalinization COUP Iran | 77.17 | 4.00 | 73.62 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 3 | Decolonization COUP Iran | 71.82 | 4.00 | 68.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Blockade COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Nasser COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], Captured Nazi Scientist[18], East European Unrest[29], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Iran, Indonesia, Philippines | 62.22 | 5.00 | 59.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Formosan Resolution INFLUENCE Indonesia, Philippines | 43.67 | 5.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Warsaw Pact Formed INFLUENCE Iran, Indonesia, Philippines | 42.22 | 5.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | East European Unrest COUP Syria | 33.67 | 4.00 | 30.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5 |
| 5 | East European Unrest COUP North Korea | 33.02 | 4.00 | 29.47 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china`
- hand: `Five Year Plan[5], Blockade[10], Nasser[15], Decolonization[30], De-Stalinization[33], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Iran | 75.50 | 4.00 | 71.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Decolonization COUP Iran | 70.15 | 4.00 | 66.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Blockade COUP Iran | 64.80 | 4.00 | 60.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Nasser COUP Iran | 64.80 | 4.00 | 60.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | De-Stalinization INFLUENCE West Germany, Japan, Thailand | 62.80 | 5.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], Captured Nazi Scientist[18], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Turkey, North Korea | 38.10 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.60 |
| 2 | Warsaw Pact Formed INFLUENCE East Germany, Turkey, North Korea | 35.00 | 5.00 | 52.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | Formosan Resolution COUP Syria | 28.45 | 4.00 | 24.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 4 | Captured Nazi Scientist COUP Syria | 23.10 | 4.00 | 19.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Syria | 23.10 | 4.00 | 19.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china`
- hand: `Five Year Plan[5], Blockade[10], Nasser[15], Decolonization[30], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE North Korea, Thailand | 47.70 | 5.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 45.70 | 5.00 | 61.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | NORAD INFLUENCE Japan, North Korea, Thailand | 45.70 | 5.00 | 61.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Blockade INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 5 | Nasser INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE East Germany, France, Panama | 32.85 | 5.00 | 50.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Captured Nazi Scientist COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 3 | UN Intervention COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 4 | Korean War INFLUENCE East Germany, France | 20.80 | 5.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Arab-Israeli War INFLUENCE East Germany, France | 20.80 | 5.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Nasser[15], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, Japan, Thailand | 48.20 | 5.00 | 63.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | NORAD INFLUENCE East Germany, Japan, Thailand | 48.20 | 5.00 | 63.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Blockade INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 4 | Nasser INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 5 | Blockade COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Syria | 23.63 | 4.00 | 19.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Syria | 23.63 | 4.00 | 19.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist INFLUENCE Italy | 18.63 | 5.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.67 |
| 4 | UN Intervention INFLUENCE Italy | 18.63 | 5.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.67 |
| 5 | Korean War INFLUENCE Italy, Japan | 18.63 | 5.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 11: T1 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Nasser[15], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, South Korea, Thailand | 40.20 | 5.00 | 55.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Blockade INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Blockade COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Italy, West Germany | 25.80 | 5.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty |
| 2 | Arab-Israeli War INFLUENCE Italy, West Germany | 25.80 | 5.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty |
| 3 | UN Intervention INFLUENCE West Germany | 25.50 | 5.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany |
| 4 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Blockade COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | Blockade REALIGN Iraq | 2.71 | -1.00 | 3.87 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Arab-Israeli War[13], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Italy, Iraq | 24.45 | 5.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty |
| 2 | UN Intervention INFLUENCE Italy | 24.30 | 5.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy |
| 3 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | UN Intervention COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +2, DEFCON +1, MilOps U-3/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], COMECON[14], Independent Reds[22], Containment[25], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Truman Doctrine[19], Olympic Games[20], Marshall Plan[23], Indo-Pakistani War[24]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], COMECON[14], Independent Reds[22], Containment[25], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Pakistan, Iraq, Thailand | 58.58 | 5.00 | 56.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE Italy, Pakistan, Iraq, Thailand | 50.88 | 5.00 | 73.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | COMECON COUP Philippines | 44.58 | 4.00 | 41.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 4 | Fidel INFLUENCE Iraq, Thailand | 41.78 | 5.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 5 | The Cambridge Five INFLUENCE Iraq, Thailand | 41.78 | 5.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Truman Doctrine[19], Olympic Games[20], Indo-Pakistani War[24]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Egypt, Saudi Arabia | 50.03 | 5.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:2.67 |
| 2 | Duck and Cover COUP Iran | 43.83 | 4.00 | 40.28 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 3 | Olympic Games COUP Iran | 38.48 | 4.00 | 34.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Iran | 38.48 | 4.00 | 34.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 5 | Olympic Games INFLUENCE Japan, Saudi Arabia | 34.48 | 5.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Independent Reds[22], Containment[25], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Italy, India, Pakistan, Thailand | 51.60 | 5.00 | 74.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 2 | Fidel INFLUENCE Pakistan, Thailand | 41.90 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | The Cambridge Five INFLUENCE Pakistan, Thailand | 41.90 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 4 | Fidel COUP Philippines | 39.50 | 4.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | The Cambridge Five COUP Philippines | 39.50 | 4.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Truman Doctrine[19], Olympic Games[20], Indo-Pakistani War[24]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Italy, Egypt | 39.65 | 5.00 | 38.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 2 | Indo-Pakistani War INFLUENCE Italy, Egypt | 39.65 | 5.00 | 38.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 3 | Olympic Games COUP Iran | 38.75 | 4.00 | 35.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Iran | 38.75 | 4.00 | 35.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | De Gaulle Leads France INFLUENCE Italy, Japan, Egypt | 35.65 | 5.00 | 54.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Independent Reds[22], Containment[25], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Philippines | 39.90 | 4.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 2 | The Cambridge Five COUP Philippines | 39.90 | 4.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 3 | Fidel INFLUENCE Philippines, Thailand | 37.60 | 5.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | The Cambridge Five INFLUENCE Philippines, Thailand | 37.60 | 5.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Containment INFLUENCE Saudi Arabia, Philippines, Thailand | 33.75 | 5.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 22: T2 AR3 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Truman Doctrine[19], Indo-Pakistani War[24]`
- state: `VP 4, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Philippines | 39.90 | 4.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 2 | Indo-Pakistani War COUP Iran | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 3 | Truman Doctrine COUP Philippines | 33.55 | 4.00 | 29.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 4 | Indo-Pakistani War INFLUENCE Japan, Philippines | 33.30 | 5.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:4.00 |
| 5 | Truman Doctrine COUP Iran | 32.80 | 4.00 | 28.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 23: T2 AR4 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Independent Reds[22], Containment[25], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Philippines, Thailand | 41.60 | 5.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 2 | Containment INFLUENCE Saudi Arabia, Philippines, Thailand | 37.75 | 5.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 3 | The Cambridge Five COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 4 | Independent Reds INFLUENCE Philippines, Thailand | 25.60 | 5.00 | 36.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Special Relationship INFLUENCE Philippines, Thailand | 25.60 | 5.00 | 36.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Truman Doctrine[19]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Japan, Iran, Libya | 32.10 | 5.00 | 47.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Japan | 21.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 3 | Vietnam Revolts INFLUENCE Japan, Iran | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty |
| 4 | Truman Doctrine COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Romanian Abdication INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], Containment[25], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Saudi Arabia, Thailand | 37.45 | 5.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Independent Reds INFLUENCE Saudi Arabia, Thailand | 25.45 | 5.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Special Relationship INFLUENCE Saudi Arabia, Thailand | 25.45 | 5.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Containment COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Independent Reds COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Truman Doctrine[19]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Pakistan, Libya | 24.35 | 5.00 | 35.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Libya | 23.55 | 5.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Libya:13.70, control_break:Libya |
| 3 | Romanian Abdication INFLUENCE Libya | 11.55 | 5.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 4 | Truman Doctrine COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Vietnam Revolts SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Pakistan, Thailand | 29.10 | 5.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE Pakistan, Thailand | 29.10 | 5.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Independent Reds COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Special Relationship COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `Romanian Abdication[12], Truman Doctrine[19]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE India | 22.40 | 5.00 | 17.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India |
| 2 | Romanian Abdication INFLUENCE India | 10.40 | 5.00 | 17.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, offside_ops_penalty |
| 3 | Truman Doctrine COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Sudan | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Olympic Games[20], Indo-Pakistani War[24], CIA Created[26], Decolonization[30], Red Scare/Purge[31], Formosan Resolution[35]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Olympic Games[20], Indo-Pakistani War[24], CIA Created[26], Decolonization[30], Formosan Resolution[35]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Indonesia | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | De Gaulle Leads France COUP Indonesia | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 3 | Socialist Governments INFLUENCE Japan, Indonesia, Thailand | 53.00 | 5.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | De Gaulle Leads France INFLUENCE Japan, Indonesia, Thailand | 53.00 | 5.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Olympic Games COUP Indonesia | 50.30 | 4.00 | 46.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 32: T3 AR1 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], Special Relationship[37]`
- state: `VP 2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Indonesia | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | Five Year Plan COUP Indonesia | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 3 | East European Unrest COUP Indonesia | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 4 | Special Relationship COUP Indonesia | 50.30 | 4.00 | 46.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 5 | Captured Nazi Scientist COUP Indonesia | 43.95 | 4.00 | 40.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 33: T3 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china`
- hand: `De Gaulle Leads France[17], Olympic Games[20], Indo-Pakistani War[24], CIA Created[26], Decolonization[30], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Japan, Indonesia, Thailand | 57.00 | 5.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |
| 2 | Olympic Games INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Indo-Pakistani War INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Decolonization INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 5 | De Gaulle Leads France COUP Syria | 32.00 | 4.00 | 28.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `none`
- hand: `Five Year Plan[5], Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan | 36.35 | 5.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | East European Unrest INFLUENCE West Germany, Japan | 36.35 | 5.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 3 | Captured Nazi Scientist INFLUENCE Japan | 21.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 4 | Special Relationship INFLUENCE Japan | 20.85 | 5.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 5 | Five Year Plan COUP Lebanon | 20.40 | 4.00 | 16.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china`
- hand: `Olympic Games[20], Indo-Pakistani War[24], CIA Created[26], Decolonization[30], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Indo-Pakistani War INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Decolonization INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Olympic Games COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan | 36.35 | 5.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | Captured Nazi Scientist INFLUENCE Japan | 21.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 3 | Special Relationship INFLUENCE Japan | 20.85 | 5.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 4 | East European Unrest COUP Lebanon | 20.40 | 4.00 | 16.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5 |
| 5 | East European Unrest COUP SE African States | 18.15 | 4.00 | 14.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china`
- hand: `Indo-Pakistani War[24], CIA Created[26], Decolonization[30], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Decolonization INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Indo-Pakistani War COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 4 | Decolonization COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Formosan Resolution INFLUENCE Japan, Thailand | 25.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Japan | 21.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | Special Relationship INFLUENCE Japan | 20.85 | 5.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 3 | Special Relationship COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 4 | Special Relationship COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |
| 5 | Special Relationship COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china`
- hand: `CIA Created[26], Decolonization[30], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Decolonization COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 3 | Formosan Resolution INFLUENCE Japan, Thailand | 25.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 4 | CIA Created INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], Romanian Abdication[12], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan | 20.85 | 5.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 2 | Special Relationship COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 3 | Special Relationship COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |
| 4 | Special Relationship COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |
| 5 | Special Relationship COUP Zimbabwe | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Thailand | 25.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | CIA Created INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | CIA Created COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Fidel INFLUENCE Japan | 4.85 | 5.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Fidel COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Fidel[8], Romanian Abdication[12], Arms Race[42], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Shuttle Diplomacy[74], Voice of America[75], Che[83]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Vietnam Revolts[9], De Gaulle Leads France[17], Containment[25], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Cuban Missile Crisis[43], U2 Incident[63], OAS Founded[71]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Fidel[8], Romanian Abdication[12], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Shuttle Diplomacy[74], Voice of America[75], Che[83]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE Mexico, Algeria, Morocco | 49.93 | 5.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 2 | Che COUP Indonesia | 48.19 | 4.00 | 44.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5 |
| 3 | Fidel COUP Indonesia | 41.84 | 4.00 | 38.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:3.5 |
| 4 | Portuguese Empire Crumbles COUP Indonesia | 41.84 | 4.00 | 38.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:3.5 |
| 5 | Che COUP Pakistan | 38.29 | 4.00 | 34.74 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Vietnam Revolts[9], De Gaulle Leads France[17], Containment[25], The Cambridge Five[36], Cuban Missile Crisis[43], U2 Incident[63], OAS Founded[71]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Mexico, Morocco, South Africa | 50.53 | 5.00 | 50.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 2 | Cuban Missile Crisis INFLUENCE Mexico, Morocco, South Africa | 50.53 | 5.00 | 50.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 3 | Containment COUP Indonesia | 48.19 | 4.00 | 44.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5 |
| 4 | Cuban Missile Crisis COUP Indonesia | 48.19 | 4.00 | 44.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5 |
| 5 | Containment COUP Mexico | 47.04 | 4.00 | 43.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Fidel[8], Romanian Abdication[12], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Shuttle Diplomacy[74], Voice of America[75]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Indonesia | 42.22 | 4.00 | 38.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:3.5 |
| 2 | Portuguese Empire Crumbles COUP Indonesia | 42.22 | 4.00 | 38.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:3.5 |
| 3 | Fidel COUP Libya | 39.32 | 4.00 | 35.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 4 | Portuguese Empire Crumbles COUP Libya | 39.32 | 4.00 | 35.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 5 | Romanian Abdication COUP Indonesia | 35.87 | 4.00 | 32.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 48: T4 AR2 US

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Vietnam Revolts[9], De Gaulle Leads France[17], The Cambridge Five[36], Cuban Missile Crisis[43], U2 Incident[63], OAS Founded[71]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE West Germany, Algeria, South Africa | 53.37 | 5.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | Cuban Missile Crisis COUP Algeria | 40.67 | 4.00 | 37.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Cuban Missile Crisis COUP Mexico | 34.42 | 4.00 | 30.87 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5 |
| 4 | Socialist Governments INFLUENCE West Germany, Algeria, South Africa | 33.37 | 5.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | De Gaulle Leads France INFLUENCE West Germany, Algeria, South Africa | 33.37 | 5.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Romanian Abdication[12], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Shuttle Diplomacy[74], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE UK, West Germany | 33.80 | 5.00 | 32.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, non_coup_milops_penalty:3.20 |
| 2 | Portuguese Empire Crumbles COUP Syria | 29.75 | 4.00 | 26.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 3 | Five Year Plan INFLUENCE East Germany, UK, West Germany | 29.20 | 5.00 | 47.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, UK, West Germany | 29.20 | 5.00 | 47.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Romanian Abdication COUP Syria | 23.40 | 4.00 | 19.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], De Gaulle Leads France[17], The Cambridge Five[36], U2 Incident[63], OAS Founded[71]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE UK, West Germany, South Africa | 30.25 | 5.00 | 52.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 2 | De Gaulle Leads France INFLUENCE UK, West Germany, South Africa | 30.25 | 5.00 | 52.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | U2 Incident INFLUENCE UK, West Germany, South Africa | 30.25 | 5.00 | 52.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | OAS Founded COUP Mexico | 22.25 | 4.00 | 18.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:0.5 |
| 5 | OAS Founded COUP Algeria | 21.50 | 4.00 | 17.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Lonely Hearts Club Band[65], Shuttle Diplomacy[74], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 27.80 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 27.80 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Romanian Abdication COUP Libya | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Romanian Abdication COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 5 | Romanian Abdication COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], The Cambridge Five[36], U2 Incident[63], OAS Founded[71]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | OAS Founded COUP Mexico | 23.05 | 4.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | OAS Founded COUP Algeria | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | OAS Founded COUP Iran | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Romanian Abdication[12], Lonely Hearts Club Band[65], Shuttle Diplomacy[74], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Libya | 26.97 | 4.00 | 23.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 26.47 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Romanian Abdication COUP Syria | 24.47 | 4.00 | 20.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:0.5 |
| 4 | Romanian Abdication COUP Mexico | 21.72 | 4.00 | 17.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 5 | Romanian Abdication COUP Algeria | 20.97 | 4.00 | 17.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], The Cambridge Five[36], U2 Incident[63], OAS Founded[71]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE West Germany, Libya, South Africa | 25.03 | 5.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Libya:13.20, control_break:Libya, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | OAS Founded COUP Colombia | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | OAS Founded COUP Saharan States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP SE African States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP Sudan | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], Shuttle Diplomacy[74], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 17.80 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Shuttle Diplomacy COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 6.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Voice of America INFLUENCE East Germany, West Germany | 6.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Shuttle Diplomacy COUP Guatemala | 5.65 | 4.00 | 22.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], The Cambridge Five[36], OAS Founded[71]`
- state: `VP 2, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Colombia | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | OAS Founded COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | OAS Founded COUP SE African States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP Zimbabwe | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 57: T4 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Voice of America COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP Guatemala | 8.30 | 4.00 | 20.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Voice of America COUP Guatemala | 8.30 | 4.00 | 20.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band COUP Tunisia | -0.85 | 4.00 | 11.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], The Cambridge Five[36]`
- state: `VP 2, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Colombia | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-1`

## Step 59: T5 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], Formosan Resolution[35], Special Relationship[37], How I Learned to Stop Worrying[49], Missile Envy[52], ABM Treaty[60], Flower Power[62], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Indo-Pakistani War[24], Red Scare/Purge[31], Formosan Resolution[35], SALT Negotiations[46], Junta[50], Latin American Death Squads[70]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], Formosan Resolution[35], Special Relationship[37], How I Learned to Stop Worrying[49], Missile Envy[52], Flower Power[62], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Libya | 39.51 | 4.00 | 35.81 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:1.5 |
| 2 | Missile Envy COUP Libya | 39.51 | 4.00 | 35.81 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:1.5 |
| 3 | Flower Power COUP Libya | 39.51 | 4.00 | 35.81 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:1.5 |
| 4 | How I Learned to Stop Worrying COUP Mexico | 34.26 | 4.00 | 30.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:1.5 |
| 5 | Missile Envy COUP Mexico | 34.26 | 4.00 | 30.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 62: T5 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Indo-Pakistani War[24], Formosan Resolution[35], SALT Negotiations[46], Junta[50], Latin American Death Squads[70]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE Brazil, Venezuela, South Africa | 48.04 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | SALT Negotiations COUP Mexico | 34.61 | 4.00 | 31.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 3 | SALT Negotiations COUP Algeria | 33.86 | 4.00 | 30.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 4 | SALT Negotiations COUP Iran | 32.86 | 4.00 | 29.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 5 | Indo-Pakistani War INFLUENCE Brazil, South Africa | 31.99 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], Formosan Resolution[35], Special Relationship[37], Missile Envy[52], Flower Power[62], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Flower Power COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Missile Envy COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 4 | Flower Power COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 5 | Missile Envy COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Indo-Pakistani War[24], Formosan Resolution[35], Junta[50], Latin American Death Squads[70]`
- state: `VP 3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Brazil, Venezuela | 36.43 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 2 | Formosan Resolution INFLUENCE Brazil, Venezuela | 36.43 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 3 | Junta INFLUENCE Brazil, Venezuela | 36.43 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 4 | Latin American Death Squads INFLUENCE Brazil, Venezuela | 36.43 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 5 | Socialist Governments INFLUENCE Argentina, Brazil, Venezuela | 34.48 | 5.00 | 56.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Flower Power [62] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], Formosan Resolution[35], Special Relationship[37], Flower Power[62], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 2 | Flower Power COUP Guatemala | 18.70 | 4.00 | 15.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 3 | Captured Nazi Scientist INFLUENCE Philippines | 17.75 | 5.00 | 17.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Philippines:12.70, control_break:Philippines, non_coup_milops_penalty:4.80 |
| 4 | Flower Power INFLUENCE Philippines | 17.60 | 5.00 | 17.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:12.70, control_break:Philippines, non_coup_milops_penalty:4.80 |
| 5 | Captured Nazi Scientist COUP Saharan States | 13.60 | 4.00 | 9.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Formosan Resolution[35], Junta[50], Latin American Death Squads[70]`
- state: `VP 3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Truman Doctrine COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Formosan Resolution INFLUENCE Argentina, South Africa | 31.70 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 67: T5 AR4 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], Formosan Resolution[35], Special Relationship[37], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 2 | Independent Reds COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Special Relationship COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Junta[50], Latin American Death Squads[70]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 3 | Truman Doctrine COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 4 | Junta INFLUENCE Argentina, South Africa | 33.70 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Latin American Death Squads INFLUENCE Argentina, South Africa | 33.70 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Independent Reds[22], Formosan Resolution[35], Special Relationship[37], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Formosan Resolution COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Special Relationship COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Independent Reds COUP Guatemala | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19], Latin American Death Squads[70]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Truman Doctrine COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Latin American Death Squads INFLUENCE Argentina, South Africa | 31.70 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | Socialist Governments COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | De Gaulle Leads France COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Formosan Resolution[35], Special Relationship[37], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Special Relationship COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Special Relationship COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], De Gaulle Leads France[17], Truman Doctrine[19]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Socialist Governments COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | De Gaulle Leads France COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Special Relationship[37], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Special Relationship COUP Guatemala | 12.30 | 4.00 | 24.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Guatemala | 12.30 | 4.00 | 24.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Special Relationship COUP Ivory Coast | 3.15 | 4.00 | 15.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Socialist Governments [7] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], De Gaulle Leads France[17]`
- state: `VP 3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | De Gaulle Leads France COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Socialist Governments COUP Colombia | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Socialist Governments COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Socialist Governments COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Warsaw Pact Formed[16], Olympic Games[20], Indo-Pakistani War[24], Suez Crisis[28], Nuclear Test Ban[34], Brush War[39], We Will Bury You[53], Cultural Revolution[61]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Sadat Expels Soviets [73] as EVENT`
- flags: `milops_shortfall:6`
- hand: `COMECON[14], Captured Nazi Scientist[18], Decolonization[30], Brezhnev Doctrine[54], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Ussuri River Skirmish[77], Alliance for Progress[79], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Warsaw Pact Formed[16], Olympic Games[20], Indo-Pakistani War[24], Suez Crisis[28], Brush War[39], We Will Bury You[53], Cultural Revolution[61]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, West Germany, Philippines | 62.49 | 5.00 | 64.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Philippines:12.70, control_break:Philippines, non_coup_milops_penalty:6.86 |
| 2 | We Will Bury You COUP Libya | 52.78 | 4.00 | 49.38 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 3 | We Will Bury You COUP Mexico | 47.53 | 4.00 | 44.13 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:3.5 |
| 4 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, Philippines | 47.09 | 5.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Philippines:12.70, control_break:Philippines, non_coup_milops_penalty:6.86 |
| 5 | Suez Crisis INFLUENCE East Germany, West Germany, Philippines | 47.09 | 5.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Philippines:12.70, control_break:Philippines, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Ussuri River Skirmish [77] as COUP`
- flags: `milops_shortfall:6`
- hand: `COMECON[14], Captured Nazi Scientist[18], Decolonization[30], Brezhnev Doctrine[54], Grain Sales to Soviets[68], Ussuri River Skirmish[77], Alliance for Progress[79], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish COUP Indonesia | 56.33 | 4.00 | 52.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Indonesia | 56.33 | 4.00 | 52.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 3 | Grain Sales to Soviets COUP Indonesia | 49.98 | 4.00 | 46.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 4 | Ussuri River Skirmish INFLUENCE West Germany, Argentina, South Africa | 48.84 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 5 | Alliance for Progress INFLUENCE West Germany, Argentina, South Africa | 48.84 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 79: T6 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Warsaw Pact Formed[16], Olympic Games[20], Indo-Pakistani War[24], Suez Crisis[28], Brush War[39], Cultural Revolution[61]`
- state: `VP 4, DEFCON 4, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE France, West Germany, Indonesia | 52.35 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 2 | Suez Crisis INFLUENCE France, West Germany, Indonesia | 52.35 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 3 | Brush War INFLUENCE France, West Germany, Indonesia | 52.35 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 4 | Cultural Revolution INFLUENCE France, West Germany, Indonesia | 52.35 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 5 | Warsaw Pact Formed COUP Libya | 47.00 | 4.00 | 43.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Alliance for Progress [79] as COUP`
- flags: `milops_shortfall:3`
- hand: `COMECON[14], Captured Nazi Scientist[18], Decolonization[30], Brezhnev Doctrine[54], Grain Sales to Soviets[68], Alliance for Progress[79], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Indonesia | 54.90 | 4.00 | 51.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress INFLUENCE West Germany, Argentina, South Africa | 51.70 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 3 | Grain Sales to Soviets COUP Indonesia | 48.55 | 4.00 | 44.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Indonesia | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Indonesia | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Olympic Games[20], Indo-Pakistani War[24], Suez Crisis[28], Brush War[39], Cultural Revolution[61]`
- state: `VP 4, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, West Germany | 42.20 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 2 | Brush War INFLUENCE East Germany, France, West Germany | 42.20 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 3 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 42.20 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 4 | Suez Crisis COUP Libya | 41.80 | 4.00 | 38.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Brush War COUP Libya | 41.80 | 4.00 | 38.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `COMECON[14], Captured Nazi Scientist[18], Decolonization[30], Brezhnev Doctrine[54], Grain Sales to Soviets[68], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE Argentina, South Africa | 34.90 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | COMECON INFLUENCE West Germany, Argentina, South Africa | 30.90 | 5.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Brezhnev Doctrine INFLUENCE West Germany, Argentina, South Africa | 30.90 | 5.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Grain Sales to Soviets COUP Mexico | 27.80 | 4.00 | 24.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |
| 5 | Grain Sales to Soviets COUP Algeria | 27.05 | 4.00 | 23.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Brush War [39] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Olympic Games[20], Indo-Pakistani War[24], Brush War[39], Cultural Revolution[61]`
- state: `VP 4, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Libya | 43.00 | 4.00 | 39.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | Cultural Revolution COUP Libya | 43.00 | 4.00 | 39.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Brush War COUP Syria | 40.50 | 4.00 | 36.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 4 | Cultural Revolution COUP Syria | 40.50 | 4.00 | 36.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 5 | Brush War INFLUENCE East Germany, France, West Germany | 39.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 84: T6 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `COMECON[14], Captured Nazi Scientist[18], Decolonization[30], Brezhnev Doctrine[54], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Argentina, Chile, South Africa | 35.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Brezhnev Doctrine INFLUENCE Argentina, Chile, South Africa | 35.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Decolonization INFLUENCE Argentina, Chile | 22.70 | 5.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Captured Nazi Scientist INFLUENCE Argentina | 20.05 | 5.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:6.00 |
| 5 | Panama Canal Returned INFLUENCE Argentina | 20.05 | 5.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Olympic Games[20], Indo-Pakistani War[24], Cultural Revolution[61]`
- state: `VP 4, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Olympic Games INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Cultural Revolution COUP Saharan States | 27.90 | 4.00 | 24.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |
| 5 | Cultural Revolution COUP Guatemala | 26.65 | 4.00 | 23.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Brezhnev Doctrine[54], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE Argentina, Chile, South Africa | 26.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Captured Nazi Scientist COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Sudan | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Olympic Games[20], Indo-Pakistani War[24]`
- state: `VP 4, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Indo-Pakistani War COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Olympic Games COUP Guatemala | 22.30 | 4.00 | 18.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Indo-Pakistani War COUP Guatemala | 22.30 | 4.00 | 18.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Blockade COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Decolonization COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Captured Nazi Scientist COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Indo-Pakistani War[24]`
- state: `VP 4, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Saharan States | 51.55 | 4.00 | 47.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5 |
| 2 | Blockade COUP Saharan States | 45.20 | 4.00 | 41.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 3 | Indo-Pakistani War COUP Guatemala | 28.30 | 4.00 | 24.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Blockade COUP Guatemala | 21.95 | 4.00 | 18.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Indo-Pakistani War COUP Tunisia | 19.15 | 4.00 | 15.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:3`
- hand: `Decolonization[30], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 45.20 | 4.00 | 41.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Decolonization COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Colombia | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP SE African States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Sudan | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 91: T7 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], De-Stalinization[33], Nuclear Test Ban[34], Quagmire[45], Summit[48], OPEC[64], Our Man in Tehran[84]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Duck and Cover[4], Korean War[11], Romanian Abdication[12], Olympic Games[20], East European Unrest[29], Decolonization[30], Kitchen Debates[51], John Paul II Elected Pope[69], Lone Gunman[109]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], De-Stalinization[33], Quagmire[45], Summit[48], OPEC[64], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Indonesia | 56.90 | 4.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Quagmire COUP Indonesia | 56.90 | 4.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Summit COUP Indonesia | 56.90 | 4.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 4 | OPEC COUP Indonesia | 56.90 | 4.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 5 | Fidel COUP Indonesia | 50.55 | 4.00 | 46.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 94: T7 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Korean War[11], Romanian Abdication[12], Olympic Games[20], East European Unrest[29], Decolonization[30], Kitchen Debates[51], John Paul II Elected Pope[69], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Chile, Nigeria, South Africa | 55.75 | 5.00 | 59.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | East European Unrest COUP Libya | 41.00 | 4.00 | 37.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Olympic Games INFLUENCE Chile, Nigeria | 39.10 | 5.00 | 42.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 4 | John Paul II Elected Pope INFLUENCE Chile, Nigeria | 39.10 | 5.00 | 42.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 5 | East European Unrest COUP Mexico | 35.75 | 4.00 | 32.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Quagmire [45] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], Quagmire[45], Summit[48], OPEC[64], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Saharan States | 48.57 | 4.00 | 45.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 2 | Summit COUP Saharan States | 48.57 | 4.00 | 45.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 3 | OPEC COUP Saharan States | 48.57 | 4.00 | 45.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 4 | Quagmire INFLUENCE East Germany, France, West Germany | 46.47 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 5 | Summit INFLUENCE East Germany, France, West Germany | 46.47 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:7`
- hand: `Korean War[11], Romanian Abdication[12], Olympic Games[20], Decolonization[30], Kitchen Debates[51], John Paul II Elected Pope[69], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Saharan States | 44.22 | 4.00 | 40.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | John Paul II Elected Pope COUP Saharan States | 44.22 | 4.00 | 40.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 3 | Kitchen Debates COUP Saharan States | 37.87 | 4.00 | 34.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 4 | Olympic Games COUP Libya | 35.32 | 4.00 | 31.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | John Paul II Elected Pope COUP Libya | 35.32 | 4.00 | 31.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 97: T7 AR3 USSR

- chosen: `Summit [48] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], Summit[48], OPEC[64], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Saharan States | 49.10 | 4.00 | 45.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5 |
| 2 | OPEC COUP Saharan States | 49.10 | 4.00 | 45.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5 |
| 3 | Summit INFLUENCE East Germany, France, West Germany | 45.40 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.40 |
| 4 | OPEC INFLUENCE East Germany, France, West Germany | 45.40 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.40 |
| 5 | Fidel COUP Saharan States | 42.75 | 4.00 | 39.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], Decolonization[30], Kitchen Debates[51], John Paul II Elected Pope[69], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Kitchen Debates COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | John Paul II Elected Pope COUP Libya | 34.65 | 4.00 | 30.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | John Paul II Elected Pope INFLUENCE Chile, South Africa | 30.30 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | John Paul II Elected Pope COUP Mexico | 29.40 | 4.00 | 25.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `OPEC [64] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], OPEC[64], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Saharan States | 49.90 | 4.00 | 46.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Fidel COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | OPEC COUP Egypt | 41.00 | 4.00 | 37.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], Decolonization[30], Kitchen Debates[51], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 2 | Kitchen Debates COUP Libya | 29.30 | 4.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Korean War COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Saharan States | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Nigeria | 47.38 | 4.00 | 43.68 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Nigeria | 47.38 | 4.00 | 43.68 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | Fidel COUP Egypt | 35.98 | 4.00 | 32.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Arab-Israeli War COUP Egypt | 35.98 | 4.00 | 32.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Fidel COUP Syria | 33.48 | 4.00 | 29.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Decolonization[30], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Saharan States | 30.22 | 4.00 | 42.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Saharan States | 30.22 | 4.00 | 42.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Saharan States | 27.87 | 4.00 | 36.02 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Lone Gunman COUP Saharan States | 27.87 | 4.00 | 36.02 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Korean War INFLUENCE Chile, South Africa | 8.97 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], CIA Created[26], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Saharan States | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Guatemala | 24.30 | 4.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Arab-Israeli War COUP Ivory Coast | 15.15 | 4.00 | 11.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:1.5 |
| 4 | Arab-Israeli War COUP Tunisia | 15.15 | 4.00 | 11.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:1.5 |
| 5 | Arab-Israeli War INFLUENCE West Germany, Nigeria | 13.45 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Saharan States | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Saharan States | 31.20 | 4.00 | 39.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Saharan States | 31.20 | 4.00 | 39.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Decolonization COUP Colombia | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP SE African States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `CIA Created[26], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Saharan States | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Guatemala | 16.30 | 4.00 | 28.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Saharan States | 15.20 | 4.00 | 23.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP Guatemala | 13.95 | 4.00 | 22.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Ivory Coast | 7.15 | 4.00 | 19.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Romanian Abdication[12], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Saharan States | 41.20 | 4.00 | 49.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Lone Gunman COUP Saharan States | 41.20 | 4.00 | 49.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Colombia | 19.20 | 4.00 | 27.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP SE African States | 19.20 | 4.00 | 27.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Sudan | 19.20 | 4.00 | 27.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 107: T8 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Red Scare/Purge[31], Portuguese Empire Crumbles[55], Cultural Revolution[61], Ussuri River Skirmish[77], One Small Step[81], Star Wars[88], Ortega Elected in Nicaragua[94], Yuri and Samantha[106], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Wargames [103] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Special Relationship[37], Summit[48], Kitchen Debates[51], Latin American Death Squads[70], Liberation Theology[76], Our Man in Tehran[84], The Reformer[90], Wargames[103]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Portuguese Empire Crumbles[55], Cultural Revolution[61], Ussuri River Skirmish[77], One Small Step[81], Star Wars[88], Ortega Elected in Nicaragua[94], Yuri and Samantha[106], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, West Germany, Nigeria | 49.21 | 5.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:9.14 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Nigeria | 49.21 | 5.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:9.14 |
| 3 | Cultural Revolution COUP Egypt | 41.32 | 4.00 | 37.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Egypt | 41.32 | 4.00 | 37.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Cultural Revolution COUP Syria | 38.82 | 4.00 | 35.27 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Summit [48] as COUP`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Special Relationship[37], Summit[48], Kitchen Debates[51], Latin American Death Squads[70], Liberation Theology[76], Our Man in Tehran[84], The Reformer[90]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Saharan States | 50.47 | 4.00 | 46.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 2 | Special Relationship COUP Saharan States | 44.12 | 4.00 | 40.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Saharan States | 44.12 | 4.00 | 40.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 4 | Our Man in Tehran COUP Saharan States | 44.12 | 4.00 | 40.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 5 | Summit COUP Libya | 41.32 | 4.00 | 37.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 111: T8 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Portuguese Empire Crumbles[55], Ussuri River Skirmish[77], One Small Step[81], Star Wars[88], Ortega Elected in Nicaragua[94], Yuri and Samantha[106], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish COUP Saharan States | 51.23 | 4.00 | 47.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:4.5 |
| 2 | Portuguese Empire Crumbles COUP Saharan States | 44.88 | 4.00 | 41.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | One Small Step COUP Saharan States | 44.88 | 4.00 | 41.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 4 | Ortega Elected in Nicaragua COUP Saharan States | 44.88 | 4.00 | 41.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 5 | Yuri and Samantha COUP Saharan States | 44.88 | 4.00 | 41.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 112: T8 AR2 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Special Relationship[37], Kitchen Debates[51], Latin American Death Squads[70], Liberation Theology[76], Our Man in Tehran[84], The Reformer[90]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Saharan States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | Our Man in Tehran COUP Saharan States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 4 | Kitchen Debates COUP Saharan States | 36.53 | 4.00 | 32.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:2.5 |
| 5 | Special Relationship COUP Libya | 33.73 | 4.00 | 30.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Portuguese Empire Crumbles[55], One Small Step[81], Star Wars[88], Ortega Elected in Nicaragua[94], Yuri and Samantha[106], Lone Gunman[109]`
- state: `VP 5, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | One Small Step COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Ortega Elected in Nicaragua COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Yuri and Samantha COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Portuguese Empire Crumbles COUP Syria | 31.90 | 4.00 | 28.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Kitchen Debates[51], Latin American Death Squads[70], Liberation Theology[76], Our Man in Tehran[84], The Reformer[90]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Sudan | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Zimbabwe | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Our Man in Tehran COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `One Small Step[81], Star Wars[88], Ortega Elected in Nicaragua[94], Yuri and Samantha[106], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | Ortega Elected in Nicaragua COUP Saharan States | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 3 | Yuri and Samantha COUP Saharan States | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 4 | Lone Gunman COUP Saharan States | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 5 | Star Wars COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Kitchen Debates[51], Liberation Theology[76], Our Man in Tehran[84], The Reformer[90]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Saharan States | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | Kitchen Debates COUP Saharan States | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 3 | The Reformer COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP Saharan States | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Ortega Elected in Nicaragua [94] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Star Wars[88], Ortega Elected in Nicaragua[94], Yuri and Samantha[106], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ortega Elected in Nicaragua COUP Saharan States | 46.22 | 4.00 | 42.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 2 | Yuri and Samantha COUP Saharan States | 46.22 | 4.00 | 42.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 3 | Lone Gunman COUP Saharan States | 39.87 | 4.00 | 36.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 4 | Star Wars COUP Saharan States | 30.22 | 4.00 | 42.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Kitchen Debates[51], Liberation Theology[76], The Reformer[90]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 17.87 | 4.00 | 14.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Kitchen Debates COUP SE African States | 17.87 | 4.00 | 14.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Sudan | 17.87 | 4.00 | 14.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Zimbabwe | 17.87 | 4.00 | 14.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Colombia | 17.37 | 4.00 | 13.52 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Yuri and Samantha [106] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Star Wars[88], Yuri and Samantha[106], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha COUP Saharan States | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5 |
| 2 | Lone Gunman COUP Saharan States | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 3 | Star Wars COUP Saharan States | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Yuri and Samantha COUP Cameroon | 27.55 | 4.00 | 23.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Yuri and Samantha COUP Guatemala | 26.80 | 4.00 | 23.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `The Reformer [90] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Liberation Theology[76], The Reformer[90]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer COUP Saharan States | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Liberation Theology COUP Saharan States | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Blockade COUP Saharan States | 31.20 | 4.00 | 39.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | The Reformer COUP SE African States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | The Reformer COUP Sudan | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Star Wars[88], Lone Gunman[109]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Cameroon | 31.20 | 4.00 | 27.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Lone Gunman COUP Saharan States | 31.20 | 4.00 | 27.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Lone Gunman COUP Guatemala | 30.45 | 4.00 | 26.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Star Wars COUP Cameroon | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Star Wars COUP Saharan States | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Liberation Theology [76] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Liberation Theology[76]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Saharan States | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Liberation Theology COUP SE African States | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Sudan | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Zimbabwe | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Liberation Theology COUP Colombia | 21.05 | 4.00 | 33.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 123: T9 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Formosan Resolution[35], Arms Race[42], Junta[50], U2 Incident[63], Nixon Plays the China Card[72], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Chernobyl [97] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Truman Doctrine[19], Indo-Pakistani War[24], Muslim Revolution[59], Latin American Death Squads[70], Che[83], Chernobyl[97]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `U2 Incident [63] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Formosan Resolution[35], Junta[50], U2 Incident[63], Nixon Plays the China Card[72], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident COUP Saharan States | 51.04 | 4.00 | 47.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Vietnam Revolts COUP Saharan States | 44.69 | 4.00 | 40.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 3 | Junta COUP Saharan States | 44.69 | 4.00 | 40.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Colonial Rear Guards COUP Saharan States | 44.69 | 4.00 | 40.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 5 | U2 Incident INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 126: T9 AR1 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:9`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Truman Doctrine[19], Indo-Pakistani War[24], Muslim Revolution[59], Latin American Death Squads[70], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Saharan States | 44.69 | 4.00 | 40.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 44.69 | 4.00 | 40.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 3 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 40.91 | 5.00 | 70.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 4 | Truman Doctrine COUP Saharan States | 38.34 | 4.00 | 34.49 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |
| 5 | Indo-Pakistani War COUP Libya | 35.54 | 4.00 | 31.84 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 127: T9 AR2 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Formosan Resolution[35], Junta[50], Nixon Plays the China Card[72], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Vietnam Revolts COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Truman Doctrine[19], Muslim Revolution[59], Latin American Death Squads[70], Che[83]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 44.22 | 4.00 | 40.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 41.87 | 5.00 | 70.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 3 | Truman Doctrine COUP Saharan States | 37.87 | 4.00 | 34.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 4 | Latin American Death Squads COUP Libya | 35.07 | 4.00 | 31.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Latin American Death Squads INFLUENCE East Germany, West Germany | 33.57 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Junta [50] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35], Junta[50], Nixon Plays the China Card[72], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Egypt | 35.20 | 4.00 | 31.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Colonial Rear Guards COUP Egypt | 35.20 | 4.00 | 31.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Junta COUP Syria | 32.70 | 4.00 | 29.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 4 | Colonial Rear Guards COUP Syria | 32.70 | 4.00 | 29.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 5 | Junta COUP Algeria | 29.45 | 4.00 | 25.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Truman Doctrine[19], Muslim Revolution[59], Che[83]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 40.00 | 5.00 | 70.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 2 | COMECON INFLUENCE East Germany, France, West Germany | 27.85 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | Che INFLUENCE East Germany, France, West Germany | 27.85 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Truman Doctrine COUP Saharan States | 16.80 | 4.00 | 12.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP SE African States | 16.80 | 4.00 | 12.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35], Nixon Plays the China Card[72], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE West Germany, Egypt | 27.55 | 5.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:12.00 |
| 2 | Colonial Rear Guards COUP Cameroon | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Colonial Rear Guards COUP Sudan | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Guatemala | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Truman Doctrine[19], Che[83]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, France, West Germany | 25.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 25.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Truman Doctrine COUP Saharan States | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP SE African States | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Zimbabwe | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Guatemala | 18.45 | 4.00 | 14.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Formosan Resolution COUP Cameroon | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Romanian Abdication[12], Truman Doctrine[19], Che[83]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Saharan States | 20.53 | 4.00 | 16.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | Truman Doctrine COUP SE African States | 20.53 | 4.00 | 16.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Truman Doctrine COUP Zimbabwe | 20.53 | 4.00 | 16.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP Colombia | 20.03 | 4.00 | 16.18 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Guatemala | 19.78 | 4.00 | 15.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Formosan Resolution[35], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Che [83] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Che[83]`
- state: `VP 5, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Saharan States | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Che COUP SE African States | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Che COUP Zimbabwe | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Che COUP Colombia | 17.40 | 4.00 | 33.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Che COUP Guatemala | 17.15 | 4.00 | 33.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 137: T9 AR7 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Saharan States | 47.55 | 4.00 | 59.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Panama Canal Returned COUP Saharan States | 45.20 | 4.00 | 53.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Cameroon | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Guatemala | 24.80 | 4.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP 5, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Blockade COUP SE African States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Blockade COUP Zimbabwe | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP SE African States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 139: T10 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Five Year Plan[5], Korean War[11], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Brush War[39], How I Learned to Stop Worrying[49], Grain Sales to Soviets[68], Our Man in Tehran[84], Latin American Debt Crisis[98]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Debt Crisis EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Soviets Shoot Down KAL 007 [92] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Independent Reds[22], East European Unrest[29], NORAD[38], Junta[50], Portuguese Empire Crumbles[55], OPEC[64], Alliance for Progress[79], Soviets Shoot Down KAL 007[92], Iran-Iraq War[105]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brush War [39] as COUP`
- flags: `milops_shortfall:10`
- hand: `Five Year Plan[5], Korean War[11], Captured Nazi Scientist[18], Brush War[39], How I Learned to Stop Worrying[49], Grain Sales to Soviets[68], Our Man in Tehran[84], Latin American Debt Crisis[98]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Saharan States | 51.61 | 4.00 | 48.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Korean War COUP Saharan States | 45.26 | 4.00 | 41.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP Saharan States | 45.26 | 4.00 | 41.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Debt Crisis COUP Saharan States | 45.26 | 4.00 | 41.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Brush War INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Independent Reds[22], East European Unrest[29], NORAD[38], Junta[50], Portuguese Empire Crumbles[55], OPEC[64], Alliance for Progress[79], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | NORAD INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | East European Unrest COUP Saharan States | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 5 | East European Unrest COUP SE African States | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Korean War[11], Captured Nazi Scientist[18], How I Learned to Stop Worrying[49], Grain Sales to Soviets[68], Our Man in Tehran[84], Latin American Debt Crisis[98]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Saharan States | 44.22 | 4.00 | 40.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Saharan States | 44.22 | 4.00 | 40.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Debt Crisis COUP Saharan States | 44.22 | 4.00 | 40.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Saharan States | 37.87 | 4.00 | 34.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 5 | Korean War INFLUENCE France, West Germany | 33.57 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Independent Reds[22], NORAD[38], Junta[50], Portuguese Empire Crumbles[55], OPEC[64], Alliance for Progress[79], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Saharan States | 52.57 | 4.00 | 49.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Saharan States | 52.57 | 4.00 | 49.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:4.5 |
| 3 | Independent Reds COUP Saharan States | 46.22 | 4.00 | 42.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 4 | Junta COUP Saharan States | 46.22 | 4.00 | 42.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 5 | Iran-Iraq War COUP Saharan States | 46.22 | 4.00 | 42.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 145: T10 AR3 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], How I Learned to Stop Worrying[49], Grain Sales to Soviets[68], Our Man in Tehran[84], Latin American Debt Crisis[98]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Saharan States | 45.15 | 4.00 | 41.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Debt Crisis COUP Saharan States | 45.15 | 4.00 | 41.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 3 | Captured Nazi Scientist COUP Saharan States | 38.80 | 4.00 | 34.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 4 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 31.70 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 5 | Latin American Debt Crisis INFLUENCE France, West Germany | 31.70 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Independent Reds[22], Junta[50], Portuguese Empire Crumbles[55], OPEC[64], Alliance for Progress[79], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 42.85 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 2 | Alliance for Progress COUP Saharan States | 29.50 | 4.00 | 25.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:4.5 |
| 3 | Alliance for Progress COUP SE African States | 29.50 | 4.00 | 25.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:4.5 |
| 4 | Alliance for Progress COUP Zimbabwe | 29.50 | 4.00 | 25.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:4.5 |
| 5 | Alliance for Progress COUP Colombia | 29.00 | 4.00 | 25.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Latin American Debt Crisis [98] as COUP`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Grain Sales to Soviets[68], Our Man in Tehran[84], Latin American Debt Crisis[98]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Debt Crisis COUP Cameroon | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 2 | Latin American Debt Crisis COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 3 | Latin American Debt Crisis COUP Sudan | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 23.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 5 | Latin American Debt Crisis COUP Guatemala | 23.80 | 4.00 | 20.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Independent Reds[22], Junta[50], Portuguese Empire Crumbles[55], OPEC[64], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 2 | Independent Reds COUP SE African States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 3 | Independent Reds COUP Zimbabwe | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Junta COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Junta COUP SE African States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Grain Sales to Soviets[68], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 42.53 | 4.00 | 38.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5 |
| 2 | Five Year Plan COUP Saharan States | 35.23 | 4.00 | 51.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Saharan States | 32.88 | 4.00 | 45.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Saharan States | 32.88 | 4.00 | 45.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Cameroon | 20.53 | 4.00 | 16.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Junta [50] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Junta[50], Portuguese Empire Crumbles[55], OPEC[64], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Saharan States | 48.88 | 4.00 | 45.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5 |
| 2 | Iran-Iraq War COUP Saharan States | 48.88 | 4.00 | 45.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5 |
| 3 | OPEC COUP Saharan States | 35.23 | 4.00 | 51.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP Saharan States | 32.88 | 4.00 | 45.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Junta COUP SE African States | 26.88 | 4.00 | 23.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Five Year Plan [5] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Five Year Plan[5], Grain Sales to Soviets[68], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan COUP Cameroon | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Five Year Plan COUP Saharan States | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Five Year Plan COUP Sudan | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Five Year Plan COUP Guatemala | 17.15 | 4.00 | 33.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Cameroon | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Iran-Iraq War [105] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Portuguese Empire Crumbles[55], OPEC[64], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War COUP Saharan States | 53.55 | 4.00 | 49.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5 |
| 2 | OPEC COUP Saharan States | 39.90 | 4.00 | 56.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP Saharan States | 37.55 | 4.00 | 49.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Iran-Iraq War COUP SE African States | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Iran-Iraq War COUP Zimbabwe | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Grain Sales to Soviets[68], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 51.55 | 4.00 | 63.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Saharan States | 51.55 | 4.00 | 63.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP Sudan | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `OPEC [64] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], OPEC[64]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | OPEC COUP SE African States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | OPEC COUP Zimbabwe | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | OPEC COUP Colombia | 31.40 | 4.00 | 47.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | OPEC COUP Guatemala | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP -5, DEFCON +1, MilOps U-3/A-3`
