# minimal_hybrid detailed rollout log

- seed: `20260544`
- winner: `US`
- final_vp: `-11`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Nasser[15], CIA Created[26], Suez Crisis[28], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:1`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Marshall Plan[23], Containment[25], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Nasser[15], CIA Created[26], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | The Cambridge Five COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Nasser COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Five Year Plan COUP Iran | 57.00 | 4.00 | 73.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | East European Unrest COUP Iran | 57.00 | 4.00 | 73.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Containment[25], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Iran, Indonesia, Philippines | 62.22 | 5.00 | 59.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | NORAD INFLUENCE Iran, Indonesia, Philippines | 62.22 | 5.00 | 59.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Olympic Games INFLUENCE Indonesia, Philippines | 43.67 | 5.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 4 | De Gaulle Leads France INFLUENCE Iran, Indonesia, Philippines | 42.22 | 5.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Containment COUP Syria | 33.50 | 4.00 | 29.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china`
- hand: `Five Year Plan[5], Nasser[15], CIA Created[26], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Iran | 70.15 | 4.00 | 66.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Nasser COUP Iran | 64.80 | 4.00 | 60.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Five Year Plan COUP Iran | 55.50 | 4.00 | 71.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 4 | East European Unrest COUP Iran | 55.50 | 4.00 | 71.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | Formosan Resolution COUP Iran | 54.15 | 4.00 | 66.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, UK, North Korea | 56.20 | 5.00 | 53.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:UK:13.65, control_break:UK, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.60 |
| 2 | Olympic Games INFLUENCE UK, North Korea | 39.30 | 5.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:13.65, control_break:UK, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.60 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, UK, North Korea | 36.20 | 5.00 | 53.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:UK:13.65, control_break:UK, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | NORAD COUP Syria | 33.60 | 4.00 | 30.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games COUP Syria | 28.25 | 4.00 | 24.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Nasser[15], CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, North Korea, Thailand | 47.60 | 5.00 | 63.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | East European Unrest INFLUENCE East Germany, North Korea, Thailand | 47.60 | 5.00 | 63.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE North Korea, Thailand | 31.70 | 5.00 | 43.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Nasser INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 5 | CIA Created INFLUENCE Thailand | 15.30 | 5.00 | 22.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE France, Panama | 35.95 | 5.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.00 |
| 2 | De Gaulle Leads France INFLUENCE France, Japan, Panama | 31.95 | 5.00 | 49.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Olympic Games COUP Syria | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 4 | Captured Nazi Scientist COUP Syria | 23.05 | 4.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 5 | Truman Doctrine COUP Syria | 23.05 | 4.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Iran, Thailand | 46.85 | 5.00 | 62.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Iran, Thailand | 32.85 | 5.00 | 44.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Nasser INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 4 | CIA Created INFLUENCE Thailand | 18.30 | 5.00 | 25.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, West Germany, Japan | 30.13 | 5.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Captured Nazi Scientist COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 4 | UN Intervention COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist INFLUENCE Italy | 18.63 | 5.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], CIA Created[26], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Thailand | 26.80 | 5.00 | 38.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | CIA Created INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | Truman Doctrine COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | UN Intervention COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist INFLUENCE Italy | 17.30 | 5.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:7.00 |
| 5 | Truman Doctrine INFLUENCE Italy | 17.30 | 5.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 13: T1 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | CIA Created INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Nasser REALIGN Iraq | 2.71 | -1.00 | 3.87 | 0.00 | 0.00 | -0.15 | 0.00 |  |
| 4 | Nasser EVENT | 2.35 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 |  |
| 5 | Nasser COUP Jordan | -0.70 | 4.00 | -4.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Jordan, empty_coup_penalty, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `Truman Doctrine[19], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Italy | 24.30 | 5.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy |
| 2 | UN Intervention INFLUENCE Italy | 24.30 | 5.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy |
| 3 | Truman Doctrine COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP Zimbabwe | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Blockade[10], Korean War[11], Romanian Abdication[12], US/Japan Mutual Defense Pact[27], Red Scare/Purge[31], Nuclear Test Ban[34]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Independent Reds [22] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Arab-Israeli War[13], COMECON[14], Warsaw Pact Formed[16], Independent Reds[22], Indo-Pakistani War[24], Decolonization[30], De-Stalinization[33]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Blockade[10], Korean War[11], Romanian Abdication[12], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Italy, Pakistan, South Korea, Thailand | 73.13 | 5.00 | 71.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | Socialist Governments INFLUENCE Pakistan, South Korea, Thailand | 56.83 | 5.00 | 54.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Nuclear Test Ban COUP Philippines | 49.60 | 4.00 | 46.20 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE Italy, Pakistan, South Korea, Thailand | 49.13 | 5.00 | 71.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Socialist Governments COUP Philippines | 44.25 | 4.00 | 40.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Arab-Israeli War[13], COMECON[14], Warsaw Pact Formed[16], Indo-Pakistani War[24], Decolonization[30], De-Stalinization[33]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Indonesia | 27.30 | 4.00 | 23.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Indo-Pakistani War COUP Japan | 25.35 | 4.00 | 21.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:0.33 |
| 3 | Indo-Pakistani War COUP North Korea | 24.75 | 4.00 | 21.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:2, milops_urgency:0.33 |
| 4 | Indo-Pakistani War COUP South Korea | 24.75 | 4.00 | 21.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:2, milops_urgency:0.33 |
| 5 | Indo-Pakistani War INFLUENCE Italy | 21.48 | 5.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 19: T2 AR2 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Blockade[10], Korean War[11], Romanian Abdication[12], US/Japan Mutual Defense Pact[27]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE India, Pakistan, Thailand | 59.30 | 5.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE India, Pakistan, Philippines, Thailand | 51.60 | 5.00 | 74.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Korean War INFLUENCE Pakistan, Thailand | 41.90 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 4 | Duck and Cover INFLUENCE India, Pakistan, Thailand | 39.30 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Blockade INFLUENCE Thailand | 22.10 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], COMECON[14], Warsaw Pact Formed[16], Decolonization[30], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, Japan | 20.15 | 5.00 | 35.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty |
| 2 | Warsaw Pact Formed INFLUENCE Italy, Japan | 20.15 | 5.00 | 35.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty |
| 3 | De-Stalinization INFLUENCE Italy, Japan | 20.15 | 5.00 | 35.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty |
| 4 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Korean War[11], Romanian Abdication[12], US/Japan Mutual Defense Pact[27]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Japan, Saudi Arabia, Philippines, Thailand | 45.75 | 5.00 | 69.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Korean War INFLUENCE Philippines, Thailand | 37.60 | 5.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Duck and Cover INFLUENCE Saudi Arabia, Philippines, Thailand | 33.75 | 5.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Blockade INFLUENCE Thailand | 21.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Romanian Abdication INFLUENCE Thailand | 21.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Warsaw Pact Formed[16], Decolonization[30], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Japan, Philippines | 20.15 | 5.00 | 35.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 2 | De-Stalinization INFLUENCE Japan, Philippines | 20.15 | 5.00 | 35.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 3 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Blockade[10], Korean War[11], Romanian Abdication[12]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Thailand | 35.97 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:5.33 |
| 2 | Duck and Cover INFLUENCE Japan, Indonesia, Thailand | 31.67 | 5.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Blockade INFLUENCE Thailand | 19.97 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:5.33 |
| 4 | Romanian Abdication INFLUENCE Thailand | 19.97 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:5.33 |
| 5 | Korean War COUP Iran | 11.15 | 4.00 | 7.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Decolonization[30], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan | 16.35 | 5.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | De-Stalinization SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Romanian Abdication[12]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Indonesia, Thailand | 23.00 | 5.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Blockade INFLUENCE Thailand | 11.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:14.00 |
| 3 | Romanian Abdication INFLUENCE Thailand | 11.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:14.00 |
| 4 | Blockade COUP Iran | 5.80 | 4.00 | 1.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5 |
| 5 | Romanian Abdication COUP Iran | 5.80 | 4.00 | 1.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Fidel [8] as SPACE`
- flags: `offside_ops_play, space_play`
- hand: `Fidel[8], Arab-Israeli War[13], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 2 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Fidel INFLUENCE Japan | 4.85 | 5.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 5 | Arab-Israeli War INFLUENCE Japan | 4.85 | 5.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |

- effects: `VP -2, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP -1, DEFCON 3, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Iran | 8.80 | 4.00 | 4.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5 |
| 2 | Romanian Abdication COUP Iran | 8.80 | 4.00 | 4.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5 |
| 3 | Blockade COUP Iraq | 6.65 | 4.00 | 2.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, empty_coup_penalty |
| 4 | Blockade COUP Saudi Arabia | 6.65 | 4.00 | 2.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, empty_coup_penalty |
| 5 | Romanian Abdication COUP Iraq | 6.65 | 4.00 | 2.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, empty_coup_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 28: T2 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30]`
- state: `VP -1, DEFCON 2, MilOps U1/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan | 4.85 | 5.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Decolonization INFLUENCE Japan | 4.85 | 5.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Arab-Israeli War COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Zimbabwe | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Fidel[8], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], NATO[21], Indo-Pakistani War[24], Red Scare/Purge[31], Special Relationship[37]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Arab-Israeli War[13], COMECON[14], Truman Doctrine[19], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Fidel[8], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], NATO[21], Indo-Pakistani War[24], Special Relationship[37]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE UK, Japan, Thailand | 52.80 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | De Gaulle Leads France INFLUENCE UK, Japan, Thailand | 52.80 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | NATO INFLUENCE UK, West Germany, Japan, Thailand | 44.30 | 5.00 | 67.90 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:13.65, access_touch:UK, influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Fidel INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Indo-Pakistani War INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Arab-Israeli War[13], COMECON[14], Truman Doctrine[19], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE UK, Japan | 35.35 | 5.00 | 34.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, non_coup_milops_penalty:4.00 |
| 2 | East European Unrest INFLUENCE UK, Japan | 35.35 | 5.00 | 34.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, non_coup_milops_penalty:4.00 |
| 3 | NORAD INFLUENCE UK, Japan | 35.35 | 5.00 | 34.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, non_coup_milops_penalty:4.00 |
| 4 | Five Year Plan COUP SE African States | 22.65 | 4.00 | 19.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 5 | Five Year Plan COUP Zimbabwe | 22.65 | 4.00 | 19.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Fidel[8], De Gaulle Leads France[17], Captured Nazi Scientist[18], NATO[21], Indo-Pakistani War[24], Special Relationship[37]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan, Thailand | 52.00 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | NATO INFLUENCE West Germany, India, Japan, Thailand | 43.40 | 5.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Fidel INFLUENCE Japan, Thailand | 36.50 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 4 | Indo-Pakistani War INFLUENCE Japan, Thailand | 36.50 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 5 | Captured Nazi Scientist INFLUENCE Thailand | 20.50 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Arab-Israeli War[13], COMECON[14], Truman Doctrine[19], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan | 31.55 | 5.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:4.80 |
| 2 | NORAD INFLUENCE West Germany, Japan | 31.55 | 5.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:4.80 |
| 3 | East European Unrest COUP SE African States | 22.95 | 4.00 | 19.40 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:4.5 |
| 4 | East European Unrest COUP Zimbabwe | 22.95 | 4.00 | 19.40 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:4.5 |
| 5 | NORAD COUP SE African States | 22.95 | 4.00 | 19.40 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space, offside_ops_play`
- hand: `Fidel[8], Captured Nazi Scientist[18], NATO[21], Indo-Pakistani War[24], Special Relationship[37]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, India, Japan, Thailand | 42.20 | 5.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Fidel INFLUENCE Japan, Thailand | 35.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Indo-Pakistani War INFLUENCE Japan, Thailand | 35.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 19.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 5 | Special Relationship INFLUENCE Japan, Thailand | 19.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Arab-Israeli War[13], COMECON[14], Truman Doctrine[19], Formosan Resolution[35], NORAD[38]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan | 30.35 | 5.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 2 | NORAD COUP SE African States | 23.40 | 4.00 | 19.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:4.5 |
| 3 | NORAD COUP Zimbabwe | 23.40 | 4.00 | 19.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:4.5 |
| 4 | NORAD COUP Colombia | 22.90 | 4.00 | 19.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:4.5 |
| 5 | Formosan Resolution COUP SE African States | 17.05 | 4.00 | 13.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Fidel[8], Captured Nazi Scientist[18], Indo-Pakistani War[24], Special Relationship[37]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE India, Thailand | 37.70 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 2 | Indo-Pakistani War INFLUENCE India, Thailand | 37.70 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 3 | Special Relationship INFLUENCE India, Thailand | 21.70 | 5.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Captured Nazi Scientist INFLUENCE India | 17.40 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, control_break:India, non_coup_milops_penalty:8.00 |
| 5 | Special Relationship SPACE | 5.20 | 1.00 | 5.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:3`
- hand: `Arab-Israeli War[13], COMECON[14], Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP SE African States | 17.80 | 4.00 | 14.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Formosan Resolution COUP Zimbabwe | 17.80 | 4.00 | 14.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Formosan Resolution COUP Colombia | 17.30 | 4.00 | 13.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Truman Doctrine INFLUENCE Japan | 13.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:8.00 |
| 5 | Formosan Resolution INFLUENCE Japan | 12.85 | 5.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 39: T3 AR5 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Captured Nazi Scientist[18], Indo-Pakistani War[24], Special Relationship[37]`
- state: `VP -4, DEFCON 2, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan, Thailand | 20.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:21.00 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 4.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:21.00 |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 4.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 4 | Special Relationship SPACE | -7.80 | 1.00 | 5.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 5 | Indo-Pakistani War SPACE | -14.80 | 1.00 | 3.00 | 0.00 | 2.50 | -0.30 | 0.00 | space_when_behind, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Arab-Israeli War[13], COMECON[14], Truman Doctrine[19]`
- state: `VP -4, DEFCON 2, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Angola | 15.70 | 5.00 | 17.85 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Angola:10.85, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:7.00 |
| 2 | COMECON INFLUENCE Japan, Angola | 11.55 | 5.00 | 34.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Angola:10.85, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Truman Doctrine COUP Mozambique | 9.95 | 4.00 | 6.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP SE African States | 9.95 | 4.00 | 6.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Zimbabwe | 9.95 | 4.00 | 6.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Captured Nazi Scientist[18], Special Relationship[37]`
- state: `VP -4, DEFCON 2, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | -7.70 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:33.00 |
| 2 | Special Relationship INFLUENCE Japan, Thailand | -7.70 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:33.00 |
| 3 | Special Relationship SPACE | -19.80 | 1.00 | 5.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:33.00 |
| 4 | Captured Nazi Scientist REALIGN Cuba | -29.66 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:33.00 |
| 5 | Captured Nazi Scientist EVENT | -30.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:33.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], COMECON[14]`
- state: `VP -4, DEFCON 2, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan | 5.35 | 5.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | COMECON COUP Mozambique | 2.15 | 4.00 | 18.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | COMECON COUP SE African States | 2.15 | 4.00 | 18.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | COMECON COUP Zimbabwe | 2.15 | 4.00 | 18.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP Colombia | 1.65 | 4.00 | 18.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP -2, DEFCON +1, MilOps U+0/A-2`

## Step 43: T4 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Fidel[8], Truman Doctrine[19], East European Unrest[29], Nuclear Test Ban[34], Formosan Resolution[35], Arms Race[42], Quagmire[45], John Paul II Elected Pope[69], Liberation Theology[76]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Five Year Plan[5], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], East European Unrest[29], Brush War[39], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Fidel[8], East European Unrest[29], Formosan Resolution[35], Arms Race[42], Quagmire[45], John Paul II Elected Pope[69], Liberation Theology[76]`
- state: `VP -5, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE West Germany, Mexico, Algeria | 49.28 | 5.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 2 | Quagmire INFLUENCE West Germany, Mexico, Algeria | 49.28 | 5.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 3 | Arms Race COUP Indonesia | 47.61 | 4.00 | 44.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5 |
| 4 | Quagmire COUP Indonesia | 47.61 | 4.00 | 44.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5 |
| 5 | Arms Race COUP Turkey | 44.46 | 4.00 | 40.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Turkey, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], East European Unrest[29], Brush War[39], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Che[83]`
- state: `VP -5, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Mexico, Morocco, South Africa | 50.53 | 5.00 | 50.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 2 | East European Unrest COUP Indonesia | 47.61 | 4.00 | 44.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5 |
| 3 | East European Unrest COUP Mexico | 46.46 | 4.00 | 42.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |
| 4 | East European Unrest COUP Algeria | 45.71 | 4.00 | 42.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |
| 5 | Grain Sales to Soviets COUP Indonesia | 41.26 | 4.00 | 37.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Fidel[8], East European Unrest[29], Formosan Resolution[35], Quagmire[45], John Paul II Elected Pope[69], Liberation Theology[76]`
- state: `VP -5, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE West Germany, Algeria, Morocco | 51.37 | 5.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 2 | Quagmire COUP Indonesia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:4.5 |
| 3 | Quagmire COUP Turkey | 44.75 | 4.00 | 41.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Turkey, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 4 | Fidel COUP Indonesia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:3.5 |
| 5 | Liberation Theology COUP Indonesia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], Brush War[39], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Che[83]`
- state: `VP -5, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Indonesia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Algeria | 39.65 | 4.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 3 | Grain Sales to Soviets INFLUENCE Algeria, South Africa | 37.37 | 5.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 4 | Truman Doctrine COUP Indonesia | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:2.5 |
| 5 | De Gaulle Leads France INFLUENCE Algeria, Congo/Zaire, South Africa | 33.42 | 5.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 49: T4 AR3 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Fidel[8], East European Unrest[29], Formosan Resolution[35], John Paul II Elected Pope[69], Liberation Theology[76]`
- state: `VP -5, DEFCON 4, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Indonesia | 48.95 | 4.00 | 45.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 2 | Liberation Theology COUP Indonesia | 48.95 | 4.00 | 45.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 3 | East European Unrest COUP Indonesia | 35.30 | 4.00 | 51.75 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Fidel COUP Mexico | 33.80 | 4.00 | 30.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, expected_swing:1.5 |
| 5 | Liberation Theology COUP Mexico | 33.80 | 4.00 | 30.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 50: T4 AR3 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], Brush War[39], Portuguese Empire Crumbles[55], Che[83]`
- state: `VP -5, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Algeria, Congo/Zaire, South Africa | 35.55 | 5.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 2 | Brush War INFLUENCE Algeria, Congo/Zaire, South Africa | 35.55 | 5.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Che INFLUENCE Algeria, Congo/Zaire, South Africa | 35.55 | 5.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Portuguese Empire Crumbles INFLUENCE Algeria, South Africa | 23.50 | 5.00 | 38.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Truman Doctrine INFLUENCE South Africa | 23.45 | 5.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, behind_on_space`
- hand: `East European Unrest[29], Formosan Resolution[35], John Paul II Elected Pope[69], Liberation Theology[76]`
- state: `VP -5, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE West Germany, Algeria | 36.05 | 5.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.00 |
| 2 | East European Unrest INFLUENCE East Germany, West Germany, Algeria | 31.45 | 5.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Liberation Theology COUP Mexico | 26.90 | 4.00 | 23.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 4 | Liberation Theology COUP Algeria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | Formosan Resolution INFLUENCE West Germany, Algeria | 20.05 | 5.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Truman Doctrine[19], Brush War[39], Portuguese Empire Crumbles[55], Che[83]`
- state: `VP -5, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE West Germany, Congo/Zaire, South Africa | 32.70 | 5.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Che INFLUENCE West Germany, Congo/Zaire, South Africa | 32.70 | 5.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE Congo/Zaire, South Africa | 20.70 | 5.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Truman Doctrine COUP Mexico | 20.55 | 4.00 | 16.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |
| 5 | Truman Doctrine INFLUENCE Congo/Zaire | 20.05 | 5.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, behind_on_space, offside_ops_play`
- hand: `East European Unrest[29], Formosan Resolution[35], John Paul II Elected Pope[69]`
- state: `VP -5, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 26.47 | 5.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 15.07 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 15.07 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | East European Unrest COUP Mexico | 12.75 | 4.00 | 29.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |
| 5 | East European Unrest COUP Algeria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Truman Doctrine[19], Portuguese Empire Crumbles[55], Che[83]`
- state: `VP -5, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE West Germany, Angola, South Africa | 27.77 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Truman Doctrine COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Algeria | 20.30 | 4.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 4 | Truman Doctrine COUP Morocco | 18.15 | 4.00 | 14.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3 |
| 5 | Truman Doctrine COUP Angola | 17.70 | 4.00 | 13.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space, offside_ops_play`
- hand: `Formosan Resolution[35], John Paul II Elected Pope[69]`
- state: `VP -5, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Mexico | 12.40 | 4.00 | 24.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP Mexico | 12.40 | 4.00 | 24.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Algeria | 11.65 | 4.00 | 23.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP Algeria | 11.65 | 4.00 | 23.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Formosan Resolution INFLUENCE East Germany, West Germany | 6.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Blockade[10], Truman Doctrine[19], Portuguese Empire Crumbles[55]`
- state: `VP -5, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Colombia | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Truman Doctrine COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Truman Doctrine COUP Mozambique | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP SE African States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space, offside_ops_play`
- hand: `John Paul II Elected Pope[69]`
- state: `VP -5, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -1.60 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 4 | John Paul II Elected Pope COUP Tunisia | -2.85 | 4.00 | 9.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope SPACE | -9.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:22.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Portuguese Empire Crumbles[55]`
- state: `VP -5, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Blockade COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Mozambique | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 59: T5 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `De Gaulle Leads France[17], NATO[21], Special Relationship[37], SALT Negotiations[46], We Will Bury You[53], Brezhnev Doctrine[54], South African Unrest[56], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -5, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], COMECON[14], Nasser[15], Containment[25], Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], Flower Power[62]`
- state: `VP -5, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `De Gaulle Leads France[17], NATO[21], Special Relationship[37], SALT Negotiations[46], Brezhnev Doctrine[54], South African Unrest[56], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 46.09 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 2 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 46.09 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 46.09 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 4 | NATO INFLUENCE East Germany, France, West Germany, Cuba | 37.49 | 5.00 | 62.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 5 | South African Unrest INFLUENCE East Germany, West Germany | 30.69 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], COMECON[14], Nasser[15], Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE Brazil, Venezuela, South Africa | 48.19 | 5.00 | 49.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Socialist Governments INFLUENCE West Germany, Brazil, Venezuela, South Africa | 44.19 | 5.00 | 65.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 3 | COMECON INFLUENCE West Germany, Brazil, Venezuela, South Africa | 44.19 | 5.00 | 65.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 4 | Fidel INFLUENCE Brazil, Venezuela, South Africa | 32.19 | 5.00 | 49.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 5 | Decolonization INFLUENCE Brazil, Venezuela, South Africa | 32.19 | 5.00 | 49.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `NATO[21], Special Relationship[37], SALT Negotiations[46], Brezhnev Doctrine[54], South African Unrest[56], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 50.13 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 50.13 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 3 | NATO INFLUENCE East Germany, France, West Germany, Cuba | 41.53 | 5.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | South African Unrest INFLUENCE France, West Germany | 34.73 | 5.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 5 | SALT Negotiations COUP Saharan States | 26.40 | 4.00 | 22.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], COMECON[14], Nasser[15], Decolonization[30], Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Argentina, Brazil, Venezuela | 55.63 | 5.00 | 77.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 2 | COMECON INFLUENCE West Germany, Argentina, Brazil, Venezuela | 55.63 | 5.00 | 77.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 3 | Fidel INFLUENCE West Germany, Brazil, Venezuela | 41.58 | 5.00 | 59.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | Decolonization INFLUENCE West Germany, Brazil, Venezuela | 41.58 | 5.00 | 59.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Flower Power INFLUENCE West Germany, Brazil, Venezuela | 41.58 | 5.00 | 59.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `NATO[21], Special Relationship[37], Brezhnev Doctrine[54], South African Unrest[56], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | NATO INFLUENCE East Germany, France, West Germany, Cuba | 35.20 | 5.00 | 62.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Brezhnev Doctrine COUP Saharan States | 26.90 | 4.00 | 23.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |
| 5 | Brezhnev Doctrine COUP Guatemala | 25.65 | 4.00 | 22.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], COMECON[14], Nasser[15], Decolonization[30], Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Argentina, Chile, South Africa | 54.50 | 5.00 | 77.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Fidel INFLUENCE West Germany, Argentina, Chile | 41.85 | 5.00 | 61.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Decolonization INFLUENCE West Germany, Argentina, Chile | 41.85 | 5.00 | 61.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Flower Power INFLUENCE West Germany, Argentina, Chile | 41.85 | 5.00 | 61.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Kitchen Debates INFLUENCE West Germany, Argentina | 39.20 | 5.00 | 42.35 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `NATO[21], Special Relationship[37], South African Unrest[56], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE East Germany, France, West Germany, Cuba | 33.20 | 5.00 | 62.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | 26.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 3 | South African Unrest COUP Saharan States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 4 | South African Unrest COUP Guatemala | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | South African Unrest COUP Tunisia | 10.90 | 4.00 | 7.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Nasser[15], Decolonization[30], Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Chile, South Africa | 33.45 | 5.00 | 54.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Decolonization INFLUENCE West Germany, Chile, South Africa | 33.45 | 5.00 | 54.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Flower Power INFLUENCE West Germany, Chile, South Africa | 33.45 | 5.00 | 54.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Kitchen Debates INFLUENCE West Germany, Chile | 32.80 | 5.00 | 37.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:10.00 |
| 5 | Nasser INFLUENCE West Germany, Chile | 20.80 | 5.00 | 37.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Special Relationship[37], South African Unrest[56], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 23.07 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:13.33 |
| 2 | South African Unrest COUP Saharan States | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |
| 3 | South African Unrest COUP Guatemala | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | South African Unrest COUP Haiti | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | South African Unrest COUP Tunisia | 12.15 | 4.00 | 8.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Nasser[15], Decolonization[30], Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Chile, South Africa | 35.12 | 5.00 | 59.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Flower Power INFLUENCE West Germany, Chile, South Africa | 35.12 | 5.00 | 59.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Kitchen Debates INFLUENCE West Germany, Chile | 34.47 | 5.00 | 42.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:13.33 |
| 4 | Nasser INFLUENCE West Germany, Chile | 22.47 | 5.00 | 42.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Kitchen Debates COUP Colombia | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `Special Relationship[37], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Saharan States | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Saharan States | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Special Relationship COUP Guatemala | 7.80 | 4.00 | 20.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Special Relationship COUP Haiti | 7.80 | 4.00 | 20.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 72: T5 AR6 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:5`
- hand: `Nasser[15], Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 2, MilOps U2/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 40.70 | 4.00 | 36.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 2 | Flower Power COUP Saharan States | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nasser COUP Saharan States | 28.70 | 4.00 | 36.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Kitchen Debates COUP Colombia | 18.70 | 4.00 | 14.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Cameroon | 18.70 | 4.00 | 14.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 73: T5 AR7 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space, offside_ops_play`
- hand: `Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 2, MilOps U2/A1, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Guatemala | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Haiti | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Guatemala | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Nasser[15], Flower Power[62]`
- state: `VP -2, DEFCON 2, MilOps U2/A1, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nasser COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Flower Power COUP Colombia | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Mozambique | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-1`

## Step 75: T6 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Romanian Abdication[12], Olympic Games[20], Red Scare/Purge[31], Bear Trap[47], Summit[48], Muslim Revolution[59], Shuttle Diplomacy[74], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Warsaw Pact Formed[16], CIA Created[26], US/Japan Mutual Defense Pact[27], Allende[57], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Romanian Abdication[12], Olympic Games[20], Bear Trap[47], Summit[48], Muslim Revolution[59], Shuttle Diplomacy[74], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Nigeria | 65.39 | 5.00 | 67.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 2 | Summit INFLUENCE East Germany, West Germany, Nigeria | 49.99 | 5.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 3 | Muslim Revolution COUP Mexico | 40.67 | 4.00 | 37.27 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:3.5 |
| 4 | Muslim Revolution COUP Algeria | 39.92 | 4.00 | 36.52 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:3.5 |
| 5 | Muslim Revolution COUP Nigeria | 35.32 | 4.00 | 31.92 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, empty_coup_penalty, expected_swing:5.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Warsaw Pact Formed[16], CIA Created[26], Allende[57], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 3 | Camp David Accords COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 4 | CIA Created COUP Saharan States | 35.77 | 4.00 | 31.92 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |
| 5 | OAS Founded COUP Saharan States | 35.77 | 4.00 | 31.92 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 79: T6 AR2 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Romanian Abdication[12], Olympic Games[20], Bear Trap[47], Summit[48], Shuttle Diplomacy[74], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Summit COUP Mexico | 34.75 | 4.00 | 31.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |
| 3 | Summit COUP Algeria | 34.00 | 4.00 | 30.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |
| 4 | Summit COUP Nigeria | 29.40 | 4.00 | 25.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, empty_coup_penalty, expected_swing:4.5 |
| 5 | Olympic Games INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Alliance for Progress [79] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Warsaw Pact Formed[16], CIA Created[26], Allende[57], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79]`
- state: `VP -2, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Saharan States | 47.40 | 4.00 | 43.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | Camp David Accords COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | CIA Created COUP Saharan States | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | OAS Founded COUP Saharan States | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Alliance for Progress INFLUENCE Chile, South Africa | 34.15 | 5.00 | 33.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Romanian Abdication[12], Olympic Games[20], Bear Trap[47], Shuttle Diplomacy[74], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Saharan States | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Saharan States | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | Romanian Abdication COUP Saharan States | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 5 | Bear Trap COUP Saharan States | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 82: T6 AR3 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Warsaw Pact Formed[16], CIA Created[26], Allende[57], Camp David Accords[66], OAS Founded[71]`
- state: `VP -2, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 41.35 | 4.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 2 | CIA Created COUP Saharan States | 35.00 | 4.00 | 31.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 3 | OAS Founded COUP Saharan States | 35.00 | 4.00 | 31.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 4 | Warsaw Pact Formed COUP Saharan States | 27.70 | 4.00 | 44.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Camp David Accords COUP Mexico | 27.20 | 4.00 | 23.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Romanian Abdication[12], Bear Trap[47], Shuttle Diplomacy[74], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | One Small Step COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Colonial Rear Guards COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | One Small Step COUP Algeria | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Warsaw Pact Formed[16], CIA Created[26], Allende[57], OAS Founded[71]`
- state: `VP -2, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 35.45 | 4.00 | 31.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 2 | OAS Founded COUP Saharan States | 35.45 | 4.00 | 31.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 3 | Warsaw Pact Formed COUP Saharan States | 28.15 | 4.00 | 44.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Saharan States | 25.80 | 4.00 | 38.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Cuba | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Romanian Abdication[12], Bear Trap[47], Shuttle Diplomacy[74], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | Romanian Abdication COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 3 | Bear Trap COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Shuttle Diplomacy COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP Mexico | 29.40 | 4.00 | 25.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Warsaw Pact Formed[16], Allende[57], OAS Founded[71]`
- state: `VP -2, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Warsaw Pact Formed COUP Saharan States | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | OAS Founded COUP Cuba | 24.90 | 4.00 | 21.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open |
| 5 | Allende COUP Saharan States | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Romanian Abdication[12], Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP -2, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Mexico | 25.05 | 4.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | Romanian Abdication COUP Algeria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Romanian Abdication COUP Morocco | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3 |
| 4 | Romanian Abdication COUP Nigeria | 19.70 | 4.00 | 15.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, empty_coup_penalty, expected_swing:2.5 |
| 5 | Bear Trap COUP Mexico | 17.75 | 4.00 | 34.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Warsaw Pact Formed [16] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Warsaw Pact Formed[16], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Saharan States | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Warsaw Pact Formed COUP Colombia | 8.40 | 4.00 | 24.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Warsaw Pact Formed COUP Cameroon | 8.40 | 4.00 | 24.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Bear Trap [47] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space, offside_ops_play`
- hand: `Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP -2, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Shuttle Diplomacy COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Bear Trap COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Shuttle Diplomacy COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Bear Trap COUP Guatemala | 14.65 | 4.00 | 31.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 90: T6 AR7 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Allende COUP Saharan States | 30.20 | 4.00 | 38.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Colombia | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Cameroon | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Mozambique | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 91: T7 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Indo-Pakistani War[24], Special Relationship[37], NORAD[38], Missile Envy[52], ABM Treaty[60], Cultural Revolution[61], Latin American Death Squads[70]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Red Scare/Purge[31], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36], Cuban Missile Crisis[43], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Cultural Revolution [61] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Indo-Pakistani War[24], Special Relationship[37], NORAD[38], Missile Envy[52], Cultural Revolution[61], Latin American Death Squads[70]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Indonesia | 55.90 | 4.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Indo-Pakistani War COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Missile Envy COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Captured Nazi Scientist COUP Indonesia | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 94: T7 AR1 US

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36], Cuban Missile Crisis[43], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE UK, Mexico, Chile | 49.45 | 5.00 | 52.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 2 | Cuban Missile Crisis COUP Saharan States | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Formosan Resolution COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Cuban Missile Crisis COUP Mexico | 41.75 | 4.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Indo-Pakistani War[24], Special Relationship[37], NORAD[38], Missile Envy[52], Latin American Death Squads[70]`
- state: `VP -1, DEFCON 3, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 2 | Missile Envy COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 3 | Latin American Death Squads COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Algeria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | Missile Envy COUP Algeria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 43.05 | 4.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 36.70 | 4.00 | 32.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Saharan States | 36.70 | 4.00 | 32.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 4 | De-Stalinization COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Formosan Resolution INFLUENCE Chile, South Africa | 28.97 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 97: T7 AR3 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], NORAD[38], Missile Envy[52], Latin American Death Squads[70]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Cameroon | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 2 | Missile Envy COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Cameroon | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 5 | Missile Envy COUP Guatemala | 18.70 | 4.00 | 15.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], De-Stalinization[33], The Cambridge Five[36], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Cameroon | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | De-Stalinization COUP Cameroon | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], NORAD[38], Latin American Death Squads[70]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Guatemala | 19.30 | 4.00 | 15.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Haiti | 19.30 | 4.00 | 15.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Captured Nazi Scientist COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], De-Stalinization[33], The Cambridge Five[36], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Cameroon | 36.95 | 4.00 | 33.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 36.95 | 4.00 | 33.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 3 | De-Stalinization COUP Cameroon | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | De-Stalinization COUP Saharan States | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Cameroon | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], NORAD[38]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Guatemala | 13.95 | 4.00 | 10.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Haiti | 13.95 | 4.00 | 10.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist INFLUENCE Congo/Zaire | 10.38 | 5.00 | 16.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `De-Stalinization [33] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], De-Stalinization[33], The Cambridge Five[36], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Cameroon | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | De-Stalinization COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 103: T7 AR6 USSR

- chosen: `Duck and Cover [4] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space, offside_ops_play`
- hand: `Duck and Cover[4], Special Relationship[37], NORAD[38]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Duck and Cover COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | NORAD COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | NORAD COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Duck and Cover COUP Guatemala | 8.65 | 4.00 | 25.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Arab-Israeli War[13], The Cambridge Five[36], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Lone Gunman COUP Cameroon | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space, offside_ops_play`
- hand: `Special Relationship[37], NORAD[38]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | NORAD COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | NORAD COUP Guatemala | 14.65 | 4.00 | 31.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | NORAD COUP Haiti | 14.65 | 4.00 | 31.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Special Relationship COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `The Cambridge Five[36], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Cameroon | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Lone Gunman COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Colombia | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 107: T8 AR0 USSR

- chosen: `The Reformer [90] as EVENT`
- flags: `holds_china, milops_shortfall:8, behind_on_space`
- hand: `Blockade[10], Romanian Abdication[12], Captured Nazi Scientist[18], Indo-Pakistani War[24], Formosan Resolution[35], Bear Trap[47], Latin American Death Squads[70], Alliance for Progress[79], The Reformer[90]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], NORAD[38], South African Unrest[56], Willy Brandt[58], Flower Power[62], John Paul II Elected Pope[69], Iran-Contra Scandal[96], Aldrich Ames Remix[101], Solidarity[104]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Solidarity EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Aldrich Ames Remix EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:8, behind_on_space`
- hand: `Blockade[10], Romanian Abdication[12], Captured Nazi Scientist[18], Indo-Pakistani War[24], Formosan Resolution[35], Bear Trap[47], Latin American Death Squads[70], Alliance for Progress[79]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Congo/Zaire | 41.08 | 4.00 | 37.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:1.5 |
| 2 | Latin American Death Squads COUP Congo/Zaire | 41.08 | 4.00 | 37.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:1.5 |
| 3 | Blockade COUP Congo/Zaire | 34.73 | 4.00 | 30.88 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:0.5 |
| 4 | Romanian Abdication COUP Congo/Zaire | 34.73 | 4.00 | 30.88 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Congo/Zaire | 34.73 | 4.00 | 30.88 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 110: T8 AR1 US

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], South African Unrest[56], Willy Brandt[58], Flower Power[62], John Paul II Elected Pope[69], Iran-Contra Scandal[96], Aldrich Ames Remix[101], Solidarity[104]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Cameroon | 42.98 | 4.00 | 39.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 2 | John Paul II Elected Pope COUP Saharan States | 42.98 | 4.00 | 39.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 3 | Solidarity COUP Cameroon | 42.98 | 4.00 | 39.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 4 | Solidarity COUP Saharan States | 42.98 | 4.00 | 39.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 5 | Warsaw Pact Formed COUP Cameroon | 29.33 | 4.00 | 45.78 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 111: T8 AR2 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Blockade[10], Romanian Abdication[12], Captured Nazi Scientist[18], Formosan Resolution[35], Bear Trap[47], Latin American Death Squads[70], Alliance for Progress[79]`
- state: `VP -1, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Congo/Zaire | 34.65 | 4.00 | 30.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Latin American Death Squads INFLUENCE East Germany, West Germany | 29.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Blockade COUP Congo/Zaire | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Romanian Abdication COUP Congo/Zaire | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Congo/Zaire | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Solidarity [104] as COUP`
- flags: `milops_shortfall:6`
- hand: `Warsaw Pact Formed[16], South African Unrest[56], Willy Brandt[58], Flower Power[62], Iran-Contra Scandal[96], Aldrich Ames Remix[101], Solidarity[104]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Solidarity COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Solidarity INFLUENCE West Germany, Congo/Zaire | 32.80 | 5.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 4 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, Congo/Zaire | 28.95 | 5.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Aldrich Ames Remix INFLUENCE East Germany, West Germany, Congo/Zaire | 28.95 | 5.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Blockade[10], Romanian Abdication[12], Captured Nazi Scientist[18], Formosan Resolution[35], Bear Trap[47], Alliance for Progress[79]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Cameroon | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 2 | Romanian Abdication COUP Cameroon | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Cameroon | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 4 | Bear Trap COUP Cameroon | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Cameroon | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Warsaw Pact Formed [16] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Warsaw Pact Formed[16], South African Unrest[56], Willy Brandt[58], Flower Power[62], Iran-Contra Scandal[96], Aldrich Ames Remix[101]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed COUP Cameroon | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Warsaw Pact Formed COUP Saharan States | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Aldrich Ames Remix COUP Cameroon | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Aldrich Ames Remix COUP Saharan States | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, Congo/Zaire | 27.35 | 5.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 115: T8 AR4 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Formosan Resolution[35], Bear Trap[47], Alliance for Progress[79]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Cameroon | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Cameroon | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Bear Trap COUP Cameroon | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Cameroon | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Cameroon | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Aldrich Ames Remix [101] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `South African Unrest[56], Willy Brandt[58], Flower Power[62], Iran-Contra Scandal[96], Aldrich Ames Remix[101]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Aldrich Ames Remix INFLUENCE West Germany, Congo/Zaire, Morocco | 30.45 | 5.00 | 55.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:Morocco:14.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Aldrich Ames Remix COUP Cameroon | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Aldrich Ames Remix COUP Saharan States | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | South African Unrest COUP Cameroon | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Saharan States | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35], Bear Trap[47], Alliance for Progress[79]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Captured Nazi Scientist COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Guatemala | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `South African Unrest [56] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `South African Unrest[56], Willy Brandt[58], Flower Power[62], Iran-Contra Scandal[96]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | South African Unrest COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Willy Brandt COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35], Alliance for Progress[79]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Alliance for Progress COUP Cameroon | 34.90 | 4.00 | 51.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Cameroon | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Captured Nazi Scientist COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Guatemala | 19.45 | 4.00 | 15.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Willy Brandt [58] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Willy Brandt[58], Flower Power[62], Iran-Contra Scandal[96]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Cameroon | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Saharan States | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Flower Power COUP Cameroon | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Saharan States | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Iran-Contra Scandal COUP Cameroon | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space, offside_ops_play`
- hand: `Formosan Resolution[35], Alliance for Progress[79]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Cameroon | 43.90 | 4.00 | 60.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Formosan Resolution COUP Cameroon | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Alliance for Progress COUP Saharan States | 21.90 | 4.00 | 38.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Guatemala | 21.15 | 4.00 | 37.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Haiti | 21.15 | 4.00 | 37.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 122: T8 AR7 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Flower Power[62], Iran-Contra Scandal[96]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Cameroon | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Flower Power COUP Saharan States | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Iran-Contra Scandal COUP Cameroon | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Iran-Contra Scandal COUP Saharan States | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Mozambique | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 123: T9 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Socialist Governments[7], Red Scare/Purge[31], Brush War[39], Arms Race[42], Allende[57], Flower Power[62], Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99], Yuri and Samantha[106]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Sadat Expels Soviets [73] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Muslim Revolution[59], OAS Founded[71], Sadat Expels Soviets[73], Chernobyl[97], Defectors[108]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Chernobyl EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Defectors EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Socialist Governments[7], Brush War[39], Arms Race[42], Allende[57], Flower Power[62], Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99], Yuri and Samantha[106]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | Brush War INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | Arms Race INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Socialist Governments COUP Congo/Zaire | 41.86 | 4.00 | 38.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Brush War COUP Congo/Zaire | 41.86 | 4.00 | 38.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Chernobyl [97] as COUP`
- flags: `milops_shortfall:9`
- hand: `Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Muslim Revolution[59], OAS Founded[71], Chernobyl[97], Defectors[108]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl COUP Cameroon | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Chernobyl COUP Saharan States | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | Defectors COUP Cameroon | 43.41 | 4.00 | 39.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Defectors COUP Saharan States | 43.41 | 4.00 | 39.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 5 | OAS Founded COUP Cameroon | 37.06 | 4.00 | 33.21 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 127: T9 AR2 USSR

- chosen: `Brush War [39] as COUP`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Brush War[39], Arms Race[42], Allende[57], Flower Power[62], Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99], Yuri and Samantha[106]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Cameroon | 50.40 | 4.00 | 46.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:4.5 |
| 2 | Arms Race COUP Cameroon | 50.40 | 4.00 | 46.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:4.5 |
| 3 | Flower Power COUP Cameroon | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 4 | Yuri and Samantha COUP Cameroon | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 5 | Brush War INFLUENCE East Germany, France, West Germany | 42.05 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 128: T9 AR2 US

- chosen: `Defectors [108] as COUP`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Muslim Revolution[59], OAS Founded[71], Defectors[108]`
- state: `VP -1, DEFCON 3, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Defectors COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Defectors COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | OAS Founded COUP Cameroon | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | OAS Founded COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Muslim Revolution COUP Cameroon | 31.25 | 4.00 | 51.85 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:5.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Arms Race [42] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Arms Race[42], Allende[57], Flower Power[62], Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99], Yuri and Samantha[106]`
- state: `VP -1, DEFCON 3, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race COUP Cameroon | 49.50 | 4.00 | 45.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 2 | Arms Race INFLUENCE East Germany, France, West Germany | 44.45 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | Flower Power COUP Cameroon | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | Yuri and Samantha COUP Cameroon | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 5 | Allende COUP Cameroon | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Muslim Revolution[59], OAS Founded[71]`
- state: `VP -1, DEFCON 3, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Nigeria | 39.30 | 4.00 | 35.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | OAS Founded COUP Saharan States | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 3 | Muslim Revolution COUP Nigeria | 34.35 | 4.00 | 54.95 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 4 | De Gaulle Leads France COUP Nigeria | 32.00 | 4.00 | 48.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Nigeria | 32.00 | 4.00 | 48.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Allende[57], Flower Power[62], Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99], Yuri and Samantha[106]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE West Germany, Nigeria | 30.20 | 5.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:12.00 |
| 2 | Yuri and Samantha INFLUENCE West Germany, Nigeria | 30.20 | 5.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:12.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Nigeria | 26.35 | 5.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Tear Down this Wall INFLUENCE East Germany, West Germany, Nigeria | 26.35 | 5.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Flower Power COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Muslim Revolution [59] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45], Muslim Revolution[59]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution COUP Saharan States | 32.75 | 4.00 | 53.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 2 | De Gaulle Leads France COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP Saharan States | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 133: T9 AR5 USSR

- chosen: `Yuri and Samantha [106] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Allende[57], Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99], Yuri and Samantha[106]`
- state: `VP -1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha COUP Cameroon | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Yuri and Samantha COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Allende COUP Cameroon | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 4 | Allende COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 5 | Ask Not What Your Country Can Do For You COUP Cameroon | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Quagmire[45]`
- state: `VP -1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Cameroon | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Quagmire COUP Cameroon | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Blockade COUP Cameroon | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | De Gaulle Leads France COUP Mozambique | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Allende[57], Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99]`
- state: `VP -1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Cameroon | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Allende COUP Saharan States | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 3 | Ask Not What Your Country Can Do For You COUP Cameroon | 34.90 | 4.00 | 51.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP Saharan States | 34.90 | 4.00 | 51.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Tear Down this Wall COUP Cameroon | 34.90 | 4.00 | 51.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Quagmire [45] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], Quagmire[45]`
- state: `VP -1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Cameroon | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Quagmire COUP Mozambique | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Saharan States | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP SE African States | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Sudan | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space, offside_ops_play`
- hand: `Ask Not What Your Country Can Do For You[78], Tear Down this Wall[99]`
- state: `VP -1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You COUP Cameroon | 43.90 | 4.00 | 60.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Ask Not What Your Country Can Do For You COUP Saharan States | 43.90 | 4.00 | 60.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Tear Down this Wall COUP Cameroon | 43.90 | 4.00 | 60.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Tear Down this Wall COUP Saharan States | 43.90 | 4.00 | 60.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP Guatemala | 21.15 | 4.00 | 37.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13]`
- state: `VP -1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Cameroon | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Mozambique | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Saharan States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP SE African States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Sudan | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-4`

## Step 139: T10 AR0 USSR

- chosen: `Glasnost [93] as EVENT`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Duck and Cover[4], CIA Created[26], Formosan Resolution[35], Brush War[39], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Kitchen Debates[51], Cultural Revolution[61], Glasnost[93]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Olympic Games[20], NATO[21], Red Scare/Purge[31], OPEC[64], Grain Sales to Soviets[68], Liberation Theology[76], Wargames[103], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brush War [39] as COUP`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Duck and Cover[4], CIA Created[26], Formosan Resolution[35], Brush War[39], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Kitchen Debates[51], Cultural Revolution[61]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Cameroon | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Brush War COUP Saharan States | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | Cuban Missile Crisis COUP Cameroon | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 4 | Cuban Missile Crisis COUP Saharan States | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 5 | Cultural Revolution COUP Cameroon | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `Red Scare/Purge [31] as COUP`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Olympic Games[20], Red Scare/Purge[31], OPEC[64], Grain Sales to Soviets[68], Liberation Theology[76], Wargames[103], Lone Gunman[109]`
- state: `VP 1, DEFCON 4, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge COUP Nigeria | 65.04 | 4.00 | 61.64 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 2 | Wargames COUP Nigeria | 65.04 | 4.00 | 61.64 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 3 | Red Scare/Purge COUP Indonesia | 62.79 | 4.00 | 59.39 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 4 | Wargames COUP Indonesia | 62.79 | 4.00 | 59.39 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 5 | Red Scare/Purge INFLUENCE East Germany, France, West Germany, Egypt | 60.42 | 5.00 | 67.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+4`

## Step 143: T10 AR2 USSR

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Duck and Cover[4], CIA Created[26], Formosan Resolution[35], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Kitchen Debates[51], Cultural Revolution[61]`
- state: `VP 1, DEFCON 3, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Saharan States | 49.40 | 4.00 | 45.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 2 | Cultural Revolution COUP Saharan States | 49.40 | 4.00 | 45.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 3 | Cuban Missile Crisis INFLUENCE East Germany, France, West Germany | 44.72 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 4 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 44.72 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 5 | How I Learned to Stop Worrying COUP Saharan States | 43.05 | 4.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Wargames [103] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Olympic Games[20], OPEC[64], Grain Sales to Soviets[68], Liberation Theology[76], Wargames[103], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames INFLUENCE East Germany, France, West Germany, Egypt | 63.85 | 5.00 | 67.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:8.00 |
| 2 | Wargames COUP Saharan States | 55.25 | 4.00 | 51.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:5.5 |
| 3 | Olympic Games COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Wargames COUP Algeria | 40.35 | 4.00 | 36.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Cultural Revolution [61] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Duck and Cover[4], CIA Created[26], Formosan Resolution[35], How I Learned to Stop Worrying[49], Kitchen Debates[51], Cultural Revolution[61]`
- state: `VP 1, DEFCON 3, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Nigeria | 52.60 | 4.00 | 49.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | How I Learned to Stop Worrying COUP Nigeria | 46.25 | 4.00 | 42.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 42.85 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 4 | Cultural Revolution COUP Algeria | 35.20 | 4.00 | 31.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:2.5 |
| 5 | Cultural Revolution COUP Mexico | 34.45 | 4.00 | 30.90 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Olympic Games[20], OPEC[64], Grain Sales to Soviets[68], Liberation Theology[76], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Saharan States | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Saharan States | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | OPEC COUP Saharan States | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Olympic Games INFLUENCE East Germany, West Germany | 28.30 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 28.30 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Duck and Cover[4], CIA Created[26], Formosan Resolution[35], How I Learned to Stop Worrying[49], Kitchen Debates[51]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Cameroon | 44.80 | 4.00 | 41.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Saharan States | 44.80 | 4.00 | 41.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 3 | Duck and Cover COUP Cameroon | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Duck and Cover COUP Saharan States | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Cameroon | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], OPEC[64], Grain Sales to Soviets[68], Liberation Theology[76], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Cameroon | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | OPEC COUP Cameroon | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Cameroon | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Cameroon | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Duck and Cover [4] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space, offside_ops_play`
- hand: `Duck and Cover[4], CIA Created[26], Formosan Resolution[35], Kitchen Debates[51]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Cameroon | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Duck and Cover COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Cameroon | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Saharan States | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Cameroon | 28.20 | 4.00 | 36.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], OPEC[64], Liberation Theology[76], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | OPEC COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | OPEC COUP Mozambique | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | OPEC COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | OPEC COUP SE African States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35], Kitchen Debates[51]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Cameroon | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Formosan Resolution COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Cameroon | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP Saharan States | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Kitchen Debates COUP Cameroon | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Liberation Theology[76], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Cameroon | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Liberation Theology COUP Cameroon | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Cameroon | 30.20 | 4.00 | 38.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Mozambique | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Cameroon | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | CIA Created COUP Saharan States | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Kitchen Debates COUP Cameroon | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Kitchen Debates COUP Saharan States | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | CIA Created COUP Guatemala | 19.45 | 4.00 | 27.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Liberation Theology [76] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Liberation Theology[76], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Cameroon | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Lone Gunman COUP Cameroon | 39.20 | 4.00 | 47.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Mozambique | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Liberation Theology COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -12, DEFCON +1, MilOps U-3/A-4`
