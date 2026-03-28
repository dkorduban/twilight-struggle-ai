# minimal_hybrid detailed rollout log

- seed: `20260404`
- winner: `USSR`
- final_vp: `1`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Socialist Governments[7], Nasser[15], Captured Nazi Scientist[18], Decolonization[30], Red Scare/Purge[31], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Independent Reds[22], East European Unrest[29], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Socialist Governments[7], Nasser[15], Captured Nazi Scientist[18], Decolonization[30], Formosan Resolution[35], NORAD[38]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Iran | 77.17 | 4.00 | 73.62 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Decolonization COUP Iran | 71.82 | 4.00 | 68.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Nasser COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Socialist Governments INFLUENCE West Germany, Japan, Thailand | 61.47 | 5.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Independent Reds[22], East European Unrest[29], The Cambridge Five[36]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Indonesia, Philippines | 43.52 | 5.00 | 40.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | East European Unrest COUP Syria | 33.67 | 4.00 | 30.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5 |
| 3 | East European Unrest COUP North Korea | 33.02 | 4.00 | 29.47 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5 |
| 4 | East European Unrest COUP Indonesia | 31.32 | 4.00 | 27.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.17, empty_coup_penalty, expected_swing:4.5 |
| 5 | Independent Reds COUP North Korea | 30.42 | 4.00 | 26.72 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china`
- hand: `Duck and Cover[4], Nasser[15], Captured Nazi Scientist[18], Decolonization[30], Formosan Resolution[35], NORAD[38]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Decolonization INFLUENCE Japan, Thailand | 45.30 | 5.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 3 | Nasser COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Duck and Cover INFLUENCE West Germany, Japan, Thailand | 42.80 | 5.00 | 58.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Independent Reds[22], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Syria | 28.45 | 4.00 | 24.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 2 | Independent Reds INFLUENCE North Korea | 20.65 | 5.00 | 17.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.60 |
| 3 | Warsaw Pact Formed INFLUENCE Turkey, North Korea | 17.95 | 5.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | De Gaulle Leads France INFLUENCE Turkey, North Korea | 17.95 | 5.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Independent Reds COUP Lebanon | 16.85 | 4.00 | 13.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 7: T1 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35], NORAD[38]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan, Thailand | 42.80 | 5.00 | 58.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | NORAD INFLUENCE West Germany, Japan, Thailand | 42.80 | 5.00 | 58.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE Japan, Thailand | 29.30 | 5.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Nasser INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 5 | Captured Nazi Scientist INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, North Korea | 22.75 | 5.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 2 | De Gaulle Leads France INFLUENCE West Germany, North Korea | 22.75 | 5.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 3 | Blockade INFLUENCE West Germany | 13.50 | 5.00 | 20.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty |
| 4 | Warsaw Pact Formed COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | De Gaulle Leads France COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35], NORAD[38]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE North Korea, South Korea, Thailand | 48.10 | 5.00 | 63.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE North Korea, Thailand | 34.70 | 5.00 | 46.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Nasser INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 5 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], De Gaulle Leads France[17], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, Turkey | 19.05 | 5.00 | 34.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty |
| 2 | De Gaulle Leads France COUP Syria | 12.00 | 4.00 | 28.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Korean War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Blockade INFLUENCE Turkey | 10.30 | 5.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, Thailand | 29.20 | 5.00 | 40.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Korean War [11] as COUP`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Blockade INFLUENCE France | 9.90 | 5.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.05, access_touch:France, offside_ops_penalty |
| 4 | Blockade COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], Captured Nazi Scientist[18]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | Nasser REALIGN Iraq | 2.71 | -1.00 | 3.87 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE France | 9.90 | 5.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.05, access_touch:France, offside_ops_penalty |
| 2 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | The Cambridge Five INFLUENCE France | 5.75 | 5.00 | 17.05 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, offside_ops_penalty |
| 4 | The Cambridge Five COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-3/A-2`

## Step 15: T2 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], Olympic Games[20], Marshall Plan[23], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], Romanian Abdication[12], Arab-Israeli War[13], Indo-Pakistani War[24], Containment[25], Suez Crisis[28], Special Relationship[37]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Olympic Games[20], Marshall Plan[23], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Italy, West Germany, Pakistan, Thailand | 49.23 | 5.00 | 71.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, access_touch:West Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE Italy, West Germany, Pakistan, Thailand | 49.23 | 5.00 | 71.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, access_touch:West Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Vietnam Revolts INFLUENCE West Germany, Thailand | 40.13 | 5.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Olympic Games INFLUENCE West Germany, Thailand | 40.13 | 5.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 5 | Vietnam Revolts COUP Philippines | 39.23 | 4.00 | 35.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Romanian Abdication[12], Arab-Israeli War[13], Indo-Pakistani War[24], Containment[25], Suez Crisis[28], Special Relationship[37]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Italy, Iraq, Panama | 50.83 | 5.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Iraq:14.30, access_touch:Iraq, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 2 | Indo-Pakistani War INFLUENCE Italy, Iraq | 34.78 | 5.00 | 32.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 3 | Special Relationship INFLUENCE Italy, Iraq | 34.78 | 5.00 | 32.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 4 | Containment COUP Iraq | 33.43 | 4.00 | 29.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 5 | Containment COUP Indonesia | 32.98 | 4.00 | 29.43 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Olympic Games[20], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE India, Pakistan, Iraq, Thailand | 54.45 | 5.00 | 77.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 2 | Vietnam Revolts INFLUENCE Pakistan, Thailand | 41.90 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | Olympic Games INFLUENCE Pakistan, Thailand | 41.90 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 4 | Vietnam Revolts COUP Philippines | 39.50 | 4.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | Olympic Games COUP Philippines | 39.50 | 4.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Romanian Abdication[12], Arab-Israeli War[13], Indo-Pakistani War[24], Suez Crisis[28], Special Relationship[37]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Iran | 38.75 | 4.00 | 35.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 2 | Special Relationship COUP Iran | 38.75 | 4.00 | 35.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 3 | Indo-Pakistani War INFLUENCE Japan, Saudi Arabia | 33.95 | 5.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.20 |
| 4 | Special Relationship INFLUENCE Japan, Saudi Arabia | 33.95 | 5.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.20 |
| 5 | Suez Crisis INFLUENCE Japan, Egypt, Saudi Arabia | 29.50 | 5.00 | 48.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 21: T2 AR3 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Olympic Games[20], CIA Created[26], UN Intervention[32]`
- state: `VP -2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Philippines, Thailand | 37.60 | 5.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Olympic Games INFLUENCE Philippines, Thailand | 37.60 | 5.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Vietnam Revolts COUP Syria | 30.65 | 4.00 | 26.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 4 | Olympic Games COUP Syria | 30.65 | 4.00 | 26.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 5 | UN Intervention COUP Syria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], Romanian Abdication[12], Arab-Israeli War[13], Suez Crisis[28], Special Relationship[37]`
- state: `VP -2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Saudi Arabia, Philippines | 40.45 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines |
| 2 | Suez Crisis INFLUENCE Japan, Saudi Arabia, Philippines | 36.45 | 5.00 | 51.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 3 | Fidel INFLUENCE Saudi Arabia, Philippines | 24.45 | 5.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 4 | Arab-Israeli War INFLUENCE Saudi Arabia, Philippines | 24.45 | 5.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 5 | Special Relationship COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Olympic Games[20], CIA Created[26], UN Intervention[32]`
- state: `VP -2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Saudi Arabia, Thailand | 36.12 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:5.33 |
| 2 | Olympic Games COUP Syria | 31.32 | 4.00 | 27.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 3 | Olympic Games COUP Saudi Arabia | 26.17 | 4.00 | 22.47 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open |
| 4 | UN Intervention COUP Saudi Arabia | 25.32 | 4.00 | 21.47 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open |
| 5 | UN Intervention COUP Syria | 24.97 | 4.00 | 21.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12], Arab-Israeli War[13], Suez Crisis[28]`
- state: `VP -2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Japan, Egypt, Iran | 32.10 | 5.00 | 47.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty |
| 2 | Fidel INFLUENCE Japan, Egypt | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 3 | Arab-Israeli War INFLUENCE Japan, Egypt | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 4 | Romanian Abdication INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 5 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP -2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Syria | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Iran | 21.80 | 4.00 | 17.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | UN Intervention COUP Iraq | 19.65 | 4.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |
| 4 | UN Intervention COUP Saudi Arabia | 19.65 | 4.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |
| 5 | CIA Created COUP Syria | 14.30 | 4.00 | 22.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 26: T2 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12], Arab-Israeli War[13]`
- state: `VP -2, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Pakistan, Egypt | 24.35 | 5.00 | 35.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 2 | Arab-Israeli War INFLUENCE Pakistan, Egypt | 24.35 | 5.00 | 35.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE Egypt | 11.55 | 5.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 4 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `CIA Created[26]`
- state: `VP -2, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Syria | 14.30 | 4.00 | 22.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 2 | CIA Created COUP Iran | 9.80 | 4.00 | 17.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 3 | CIA Created COUP Iraq | 7.65 | 4.00 | 15.80 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |
| 4 | CIA Created COUP Saudi Arabia | 7.65 | 4.00 | 15.80 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |
| 5 | CIA Created INFLUENCE Thailand | 2.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], Arab-Israeli War[13]`
- state: `VP -2, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE India, Japan | 22.40 | 5.00 | 33.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE India | 10.40 | 5.00 | 17.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, offside_ops_penalty |
| 3 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 29: T3 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], Olympic Games[20], NATO[21], Independent Reds[22], UN Intervention[32], De-Stalinization[33]`
- state: `VP -3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Warsaw Pact Formed[16], De Gaulle Leads France[17], US/Japan Mutual Defense Pact[27], Red Scare/Purge[31], Nuclear Test Ban[34], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP -3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], Olympic Games[20], NATO[21], Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Pakistan, Iraq, Saudi Arabia, Thailand | 52.40 | 5.00 | 76.00 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Iraq:14.30, control_break:Iraq, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Arab-Israeli War COUP Indonesia | 50.30 | 4.00 | 46.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | Olympic Games COUP Indonesia | 50.30 | 4.00 | 46.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Romanian Abdication COUP Indonesia | 43.95 | 4.00 | 40.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Nasser COUP Indonesia | 43.95 | 4.00 | 40.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Warsaw Pact Formed[16], De Gaulle Leads France[17], Red Scare/Purge[31], Nuclear Test Ban[34], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP -3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE West Germany, India, Japan, Libya | 63.45 | 5.00 | 63.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:4.00 |
| 2 | Nuclear Test Ban INFLUENCE West Germany, India, Japan, Libya | 63.45 | 5.00 | 63.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:4.00 |
| 3 | Red Scare/Purge COUP Pakistan | 45.10 | 4.00 | 41.70 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 4 | Nuclear Test Ban COUP Pakistan | 45.10 | 4.00 | 41.70 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 5 | Red Scare/Purge COUP Philippines | 44.60 | 4.00 | 41.20 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Indonesia | 50.70 | 4.00 | 47.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games COUP Indonesia | 50.70 | 4.00 | 47.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 3 | Romanian Abdication COUP Indonesia | 44.35 | 4.00 | 40.50 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 4 | Nasser COUP Indonesia | 44.35 | 4.00 | 40.50 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 5 | UN Intervention COUP Indonesia | 44.35 | 4.00 | 40.50 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 34: T3 AR2 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Warsaw Pact Formed[16], De Gaulle Leads France[17], Nuclear Test Ban[34], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Japan, Libya, Indonesia | 65.95 | 5.00 | 66.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.80 |
| 2 | Nuclear Test Ban COUP Tunisia | 40.50 | 4.00 | 37.10 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 3 | Nuclear Test Ban COUP Iran | 38.25 | 4.00 | 34.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:3.5 |
| 4 | Formosan Resolution INFLUENCE Japan, Libya | 34.75 | 5.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.80 |
| 5 | Nuclear Test Ban COUP Lebanon | 31.15 | 4.00 | 27.75 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Lebanon, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:5.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Nasser[15], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Thailand | 39.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Romanian Abdication INFLUENCE Thailand | 23.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Nasser INFLUENCE Thailand | 23.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | UN Intervention INFLUENCE Thailand | 23.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Independent Reds INFLUENCE Japan, Thailand | 23.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Warsaw Pact Formed[16], De Gaulle Leads France[17], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Japan | 30.50 | 5.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 2 | Formosan Resolution COUP Tunisia | 29.40 | 4.00 | 25.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:1.5 |
| 3 | Formosan Resolution COUP Iran | 27.15 | 4.00 | 23.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |
| 4 | Socialist Governments INFLUENCE West Germany, India, Japan | 25.90 | 5.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Warsaw Pact Formed INFLUENCE West Germany, India, Japan | 25.90 | 5.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Nasser[15], Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | Nasser INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | UN Intervention INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Independent Reds INFLUENCE Japan, Thailand | 22.63 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Romanian Abdication COUP El Salvador | 9.53 | 4.00 | 5.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Warsaw Pact Formed[16], De Gaulle Leads France[17], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, India, Japan | 23.90 | 5.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, India, Japan | 23.90 | 5.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, India, Japan | 23.90 | 5.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Socialist Governments COUP Tunisia | 16.75 | 4.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Warsaw Pact Formed COUP Tunisia | 16.75 | 4.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Libya | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Libya | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Nasser COUP Iran | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |
| 4 | UN Intervention COUP Iran | 19.80 | 4.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |
| 5 | Nasser INFLUENCE Thailand | 18.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Warsaw Pact Formed [16] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], The Cambridge Five[36]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed COUP Tunisia | 18.75 | 4.00 | 35.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | De Gaulle Leads France COUP Tunisia | 18.75 | 4.00 | 35.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Tunisia | 16.40 | 4.00 | 28.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Warsaw Pact Formed INFLUENCE West Germany, India, Japan | 15.90 | 5.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, control_break:India, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 5 | De Gaulle Leads France INFLUENCE West Germany, India, Japan | 15.90 | 5.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, control_break:India, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 14.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 2 | Independent Reds INFLUENCE Japan, Thailand | 14.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | UN Intervention COUP El Salvador | 12.20 | 4.00 | 8.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Guatemala | 12.20 | 4.00 | 8.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Nicaragua | 12.20 | 4.00 | 8.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nicaragua, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `De Gaulle Leads France[17], The Cambridge Five[36]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, India, Japan | 36.90 | 5.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, control_break:India, influence:Japan:16.15, offside_ops_penalty |
| 2 | The Cambridge Five INFLUENCE India, Japan | 25.40 | 5.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, offside_ops_penalty |
| 3 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | De Gaulle Leads France SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | De Gaulle Leads France COUP SE African States | -1.85 | 4.00 | 14.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Socialist Governments[7], Romanian Abdication[12], Nasser[15], De Gaulle Leads France[17], Olympic Games[20], Willy Brandt[58], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Red Scare/Purge[31], The Cambridge Five[36], Brezhnev Doctrine[54], Muslim Revolution[59], Nixon Plays the China Card[72], One Small Step[81], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Romanian Abdication[12], Nasser[15], De Gaulle Leads France[17], Olympic Games[20], Willy Brandt[58], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, Chile | 38.73 | 5.00 | 38.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.57 |
| 2 | De Gaulle Leads France COUP Iran | 32.29 | 4.00 | 28.74 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:2.5 |
| 3 | De Gaulle Leads France COUP Colombia | 26.19 | 4.00 | 22.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.57, empty_coup_penalty, expected_swing:4.5 |
| 4 | Olympic Games COUP Iran | 25.94 | 4.00 | 22.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:1.5 |
| 5 | Willy Brandt COUP Iran | 25.94 | 4.00 | 22.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], The Cambridge Five[36], Brezhnev Doctrine[54], Muslim Revolution[59], Nixon Plays the China Card[72], One Small Step[81], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE West Germany, Mexico, Algeria, South Africa | 41.93 | 5.00 | 66.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Nixon Plays the China Card INFLUENCE Mexico, South Africa | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 3 | One Small Step INFLUENCE Mexico, South Africa | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 4 | Brezhnev Doctrine INFLUENCE Mexico, Algeria, South Africa | 29.93 | 5.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Nixon Plays the China Card COUP Iran | 25.94 | 4.00 | 22.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Five Year Plan[5], Romanian Abdication[12], Nasser[15], Olympic Games[20], Willy Brandt[58], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Mexico | 35.07 | 4.00 | 31.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Willy Brandt COUP Mexico | 35.07 | 4.00 | 31.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Olympic Games COUP Algeria | 34.32 | 4.00 | 30.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Willy Brandt COUP Algeria | 34.32 | 4.00 | 30.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Romanian Abdication COUP Mexico | 28.72 | 4.00 | 24.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 48: T4 AR2 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], The Cambridge Five[36], Brezhnev Doctrine[54], Nixon Plays the China Card[72], One Small Step[81], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE Algeria, South Africa | 40.37 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | One Small Step INFLUENCE Algeria, South Africa | 40.37 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 3 | Brezhnev Doctrine INFLUENCE Mexico, Algeria, South Africa | 37.17 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | The Cambridge Five INFLUENCE Algeria, South Africa | 24.37 | 5.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Panama Canal Returned INFLUENCE South Africa | 21.32 | 5.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Romanian Abdication[12], Nasser[15], Willy Brandt[58], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Argentina | 19.85 | 5.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:3.20 |
| 2 | Nasser INFLUENCE Argentina | 19.85 | 5.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:3.20 |
| 3 | Willy Brandt INFLUENCE Argentina | 19.70 | 5.00 | 18.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:3.20 |
| 4 | Willy Brandt COUP Colombia | 19.15 | 4.00 | 15.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:3.5 |
| 5 | Willy Brandt COUP El Salvador | 17.90 | 4.00 | 14.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:El Salvador, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], The Cambridge Five[36], Brezhnev Doctrine[54], One Small Step[81], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Mexico, Morocco | 32.05 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:6.40 |
| 2 | Brezhnev Doctrine INFLUENCE Mexico, Morocco, South Africa | 28.70 | 5.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | One Small Step COUP Colombia | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Saharan States | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP SE African States | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Nasser[15], Willy Brandt[58], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Argentina | 22.05 | 5.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:4.00 |
| 2 | Willy Brandt INFLUENCE Argentina | 21.90 | 5.00 | 21.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:4.00 |
| 3 | Willy Brandt COUP Colombia | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Five Year Plan INFLUENCE Argentina, Chile | 18.55 | 5.00 | 38.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Alliance for Progress INFLUENCE Argentina, Chile | 18.55 | 5.00 | 38.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], The Cambridge Five[36], Brezhnev Doctrine[54], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Panama Canal Returned COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Sudan | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Willy Brandt [58] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Willy Brandt[58], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Colombia | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 2 | Willy Brandt INFLUENCE East Germany | 19.92 | 5.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, non_coup_milops_penalty:5.33 |
| 3 | Willy Brandt COUP El Salvador | 18.97 | 4.00 | 15.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:El Salvador, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | Willy Brandt COUP Guatemala | 18.97 | 4.00 | 15.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | Willy Brandt COUP Nicaragua | 18.97 | 4.00 | 15.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nicaragua, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 38.53 | 4.00 | 34.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 2 | The Cambridge Five COUP Colombia | 28.88 | 4.00 | 41.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Colombia | 26.53 | 4.00 | 34.68 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Saharan States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP SE African States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 55: T4 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, Chile | 7.90 | 5.00 | 37.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, Chile | 7.90 | 5.00 | 37.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Five Year Plan COUP Colombia | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Colombia | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Five Year Plan COUP El Salvador | 5.65 | 4.00 | 22.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:El Salvador, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP -3, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Zimbabwe | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 57: T4 AR7 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Colombia | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Colombia | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Alliance for Progress COUP El Salvador | 9.65 | 4.00 | 26.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:El Salvador, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Guatemala | 9.65 | 4.00 | 26.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Nicaragua | 9.65 | 4.00 | 26.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nicaragua, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 58: T4 AR7 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12]`
- state: `VP -3, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Colombia | 29.20 | 4.00 | 37.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Saharan States | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP SE African States | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Sudan | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Zimbabwe | 7.20 | 4.00 | 15.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], UN Intervention[32], Special Relationship[37], Cuban Missile Crisis[43], U2 Incident[63], OPEC[64], Puppet Governments[67]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Shuttle Diplomacy [74] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], Indo-Pakistani War[24], The Cambridge Five[36], Junta[50], Kitchen Debates[51], Missile Envy[52], Shuttle Diplomacy[74], Liberation Theology[76]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], UN Intervention[32], Special Relationship[37], U2 Incident[63], OPEC[64], Puppet Governments[67]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE Panama, Argentina, Chile | 53.79 | 5.00 | 54.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 2 | OPEC INFLUENCE Panama, Argentina, Chile | 53.79 | 5.00 | 54.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 3 | Arab-Israeli War INFLUENCE Panama, Chile | 37.74 | 5.00 | 38.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 4 | Decolonization INFLUENCE Panama, Chile | 37.74 | 5.00 | 38.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 5 | Special Relationship INFLUENCE Panama, Chile | 21.74 | 5.00 | 38.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], Indo-Pakistani War[24], The Cambridge Five[36], Junta[50], Kitchen Debates[51], Missile Envy[52], Liberation Theology[76]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Panama, South Africa | 35.74 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Junta INFLUENCE Panama, South Africa | 35.74 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Missile Envy INFLUENCE Panama, South Africa | 35.74 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 4 | Warsaw Pact Formed INFLUENCE West Germany, Panama, South Africa | 31.74 | 5.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 5 | The Cambridge Five INFLUENCE Panama, South Africa | 19.74 | 5.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], UN Intervention[32], Special Relationship[37], OPEC[64], Puppet Governments[67]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE Argentina, Brazil, Chile | 47.08 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:6.67 |
| 2 | Arab-Israeli War INFLUENCE Argentina, Chile | 31.03 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.67 |
| 3 | Decolonization INFLUENCE Argentina, Chile | 31.03 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.67 |
| 4 | Special Relationship INFLUENCE Argentina, Chile | 15.03 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Puppet Governments INFLUENCE Argentina, Chile | 15.03 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], The Cambridge Five[36], Junta[50], Kitchen Debates[51], Missile Envy[52], Liberation Theology[76]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE West Germany, South Africa | 30.98 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 2 | Missile Envy INFLUENCE West Germany, South Africa | 30.98 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 3 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, South Africa | 26.38 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | Captured Nazi Scientist INFLUENCE South Africa | 14.98 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 5 | The Cambridge Five INFLUENCE West Germany, South Africa | 14.98 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], UN Intervention[32], Special Relationship[37], Puppet Governments[67]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Brazil, Chile | 32.70 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 2 | Decolonization INFLUENCE Brazil, Chile | 32.70 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 3 | Special Relationship INFLUENCE Brazil, Chile | 16.70 | 5.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Puppet Governments INFLUENCE Brazil, Chile | 16.70 | 5.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | UN Intervention INFLUENCE Brazil | 16.05 | 5.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], The Cambridge Five[36], Kitchen Debates[51], Missile Envy[52], Liberation Theology[76]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Captured Nazi Scientist INFLUENCE South Africa | 13.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | The Cambridge Five INFLUENCE West Germany, South Africa | 13.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Kitchen Debates INFLUENCE South Africa | 13.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `CIA Created[26], Decolonization[30], UN Intervention[32], Special Relationship[37], Puppet Governments[67]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Argentina, Chile | 27.70 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:10.00 |
| 2 | Special Relationship INFLUENCE Argentina, Chile | 11.70 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Puppet Governments INFLUENCE Argentina, Chile | 11.70 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | UN Intervention INFLUENCE Chile | 11.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:10.00 |
| 5 | CIA Created INFLUENCE Chile | -0.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], The Cambridge Five[36], Kitchen Debates[51], Liberation Theology[76]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, South Africa | 23.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Captured Nazi Scientist INFLUENCE South Africa | 11.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 3 | The Cambridge Five INFLUENCE West Germany, South Africa | 11.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Kitchen Debates INFLUENCE South Africa | 11.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 5 | Liberation Theology INFLUENCE West Germany, South Africa | 11.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `CIA Created[26], UN Intervention[32], Special Relationship[37], Puppet Governments[67]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, Chile | 12.72 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Puppet Governments INFLUENCE East Germany, Chile | 12.72 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | UN Intervention INFLUENCE East Germany | 12.07 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, non_coup_milops_penalty:13.33 |
| 4 | CIA Created INFLUENCE East Germany | 0.07 | 5.00 | 20.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Special Relationship SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], The Cambridge Five[36], Kitchen Debates[51], Liberation Theology[76]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | 8.32 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:13.33 |
| 2 | The Cambridge Five INFLUENCE West Germany, South Africa | 8.32 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Kitchen Debates INFLUENCE South Africa | 8.32 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:13.33 |
| 4 | Liberation Theology INFLUENCE West Germany, South Africa | 8.32 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | The Cambridge Five SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `CIA Created[26], UN Intervention[32], Puppet Governments[67]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE Argentina, Chile | -13.30 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | UN Intervention INFLUENCE Chile | -13.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:35.00 |
| 3 | CIA Created INFLUENCE Chile | -25.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 4 | Puppet Governments SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | UN Intervention REALIGN Chile | -28.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `The Cambridge Five[36], Kitchen Debates[51], Liberation Theology[76]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, South Africa | -13.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | Kitchen Debates INFLUENCE South Africa | -13.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:35.00 |
| 3 | Liberation Theology INFLUENCE West Germany, South Africa | -13.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 4 | The Cambridge Five SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | Liberation Theology SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Chile | -33.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:55.00 |
| 2 | CIA Created INFLUENCE Chile | -45.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 3 | UN Intervention REALIGN Chile | -48.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:55.00 |
| 4 | UN Intervention EVENT | -52.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |
| 5 | CIA Created REALIGN Chile | -60.91 | -1.00 | 7.24 | 0.00 | -12.00 | -0.15 | 0.00 | defcon2_realign_window, offside_ops_penalty, non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Kitchen Debates [51] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Kitchen Debates[51], Liberation Theology[76]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates INFLUENCE South Africa | -33.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:55.00 |
| 2 | Liberation Theology INFLUENCE West Germany, South Africa | -33.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 3 | Liberation Theology SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 4 | Kitchen Debates REALIGN South Africa | -48.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:55.00 |
| 5 | Kitchen Debates EVENT | -52.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 75: T6 AR0 USSR

- chosen: `Fidel [8] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Marshall Plan[23], Containment[25], UN Intervention[32], Formosan Resolution[35], Nuclear Subs[44], Flower Power[62], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], De Gaulle Leads France[17], East European Unrest[29], Nuclear Test Ban[34], Formosan Resolution[35], We Will Bury You[53], Portuguese Empire Crumbles[55], Allende[57], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Marshall Plan[23], Containment[25], UN Intervention[32], Formosan Resolution[35], Nuclear Subs[44], Flower Power[62], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Argentina, Chile, Venezuela, Algeria | 38.94 | 5.00 | 65.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 2 | Flower Power INFLUENCE Argentina, Chile | 30.84 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.86 |
| 3 | Containment INFLUENCE Argentina, Chile, Venezuela | 26.89 | 5.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 4 | Formosan Resolution INFLUENCE Argentina, Chile | 14.84 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 5 | Nuclear Subs INFLUENCE Argentina, Chile | 14.84 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], De Gaulle Leads France[17], East European Unrest[29], Formosan Resolution[35], We Will Bury You[53], Portuguese Empire Crumbles[55], Allende[57], Latin American Death Squads[70]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Algeria, South Africa | 49.84 | 5.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | East European Unrest INFLUENCE West Germany, Algeria, South Africa | 49.84 | 5.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | We Will Bury You INFLUENCE East Germany, West Germany, Algeria, South Africa | 41.24 | 5.00 | 67.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 4 | Formosan Resolution INFLUENCE Algeria, South Africa | 33.84 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 5 | Latin American Death Squads INFLUENCE Algeria, South Africa | 33.84 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Containment[25], UN Intervention[32], Formosan Resolution[35], Nuclear Subs[44], Flower Power[62], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE Chile, Venezuela | 32.70 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 2 | Containment INFLUENCE Chile, Venezuela, Morocco | 29.35 | 5.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Formosan Resolution INFLUENCE Chile, Venezuela | 16.70 | 5.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Nuclear Subs INFLUENCE Chile, Venezuela | 16.70 | 5.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Grain Sales to Soviets INFLUENCE Chile, Venezuela | 16.70 | 5.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `De Gaulle Leads France[17], East European Unrest[29], Formosan Resolution[35], We Will Bury You[53], Portuguese Empire Crumbles[55], Allende[57], Latin American Death Squads[70]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, West Germany, South Africa | 45.05 | 5.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | We Will Bury You INFLUENCE East Germany, France, West Germany, South Africa | 36.45 | 5.00 | 64.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Formosan Resolution INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | Latin American Death Squads INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Containment[25], UN Intervention[32], Formosan Resolution[35], Nuclear Subs[44], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, Chile, Morocco | 29.10 | 5.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Formosan Resolution INFLUENCE East Germany, Chile | 16.45 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | Nuclear Subs INFLUENCE East Germany, Chile | 16.45 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, Chile | 16.45 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | UN Intervention INFLUENCE East Germany | 15.80 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `De Gaulle Leads France[17], Formosan Resolution[35], We Will Bury You[53], Portuguese Empire Crumbles[55], Allende[57], Latin American Death Squads[70]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, West Germany, South Africa | 34.85 | 5.00 | 64.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Formosan Resolution INFLUENCE West Germany, South Africa | 28.05 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 3 | Latin American Death Squads INFLUENCE West Germany, South Africa | 28.05 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 4 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 23.45 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 12.05 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `UN Intervention[32], Formosan Resolution[35], Nuclear Subs[44], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, Chile | 14.05 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Nuclear Subs INFLUENCE East Germany, Chile | 14.05 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, Chile | 14.05 | 5.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | UN Intervention INFLUENCE East Germany | 13.40 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, non_coup_milops_penalty:12.00 |
| 5 | OAS Founded INFLUENCE East Germany | 1.40 | 5.00 | 20.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `De Gaulle Leads France[17], Formosan Resolution[35], Portuguese Empire Crumbles[55], Allende[57], Latin American Death Squads[70]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, South Africa | 25.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany, South Africa | 25.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 21.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 9.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Allende INFLUENCE South Africa | -2.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `UN Intervention[32], Nuclear Subs[44], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE Argentina, Chile | 5.70 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Grain Sales to Soviets INFLUENCE Argentina, Chile | 5.70 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | UN Intervention INFLUENCE Chile | 5.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:16.00 |
| 4 | OAS Founded INFLUENCE Chile | -6.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Nuclear Subs SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `De Gaulle Leads France[17], Portuguese Empire Crumbles[55], Allende[57], Latin American Death Squads[70]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, South Africa | 21.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:16.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 17.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 5.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Allende INFLUENCE South Africa | -6.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Portuguese Empire Crumbles SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `UN Intervention[32], Grain Sales to Soviets[68], OAS Founded[71]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE Argentina, Chile | -20.30 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | UN Intervention INFLUENCE Chile | -20.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:42.00 |
| 3 | OAS Founded INFLUENCE Chile | -32.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Grain Sales to Soviets SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | UN Intervention REALIGN Chile | -37.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `De Gaulle Leads France[17], Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | -8.95 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | -20.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Allende INFLUENCE South Africa | -32.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Portuguese Empire Crumbles SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | De Gaulle Leads France SPACE | -34.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], OAS Founded[71]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE East Germany | -40.60 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, non_coup_milops_penalty:66.00 |
| 2 | OAS Founded INFLUENCE East Germany | -52.60 | 5.00 | 20.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | UN Intervention REALIGN Chile | -61.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |
| 4 | UN Intervention EVENT | -63.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |
| 5 | OAS Founded EVENT | -72.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | -44.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 2 | Allende INFLUENCE South Africa | -56.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | Portuguese Empire Crumbles SPACE | -58.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 4 | Allende EVENT | -72.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |
| 5 | Portuguese Empire Crumbles EVENT | -72.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 91: T7 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Warsaw Pact Formed[16], NORAD[38], How I Learned to Stop Worrying[49], Cultural Revolution[61], Sadat Expels Soviets[73], Voice of America[75], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Korean War[11], Suez Crisis[28], Nuclear Test Ban[34], Arms Race[42], Bear Trap[47], Summit[48], ABM Treaty[60], Colonial Rear Guards[110]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], NORAD[38], How I Learned to Stop Worrying[49], Cultural Revolution[61], Sadat Expels Soviets[73], Voice of America[75], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE UK, Argentina, Chile | 45.70 | 5.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 2 | Ussuri River Skirmish INFLUENCE UK, Argentina, Chile | 45.70 | 5.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 3 | How I Learned to Stop Worrying INFLUENCE Argentina, Chile | 29.70 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 4 | NORAD INFLUENCE UK, Argentina, Chile | 25.70 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Sadat Expels Soviets INFLUENCE UK, Argentina, Chile | 25.70 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Korean War[11], Suez Crisis[28], Arms Race[42], Bear Trap[47], Summit[48], ABM Treaty[60], Colonial Rear Guards[110]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, UK, West Germany, South Africa | 66.05 | 5.00 | 69.65 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Arms Race INFLUENCE East Germany, UK, South Africa | 50.05 | 5.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Bear Trap INFLUENCE East Germany, UK, South Africa | 50.05 | 5.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | Summit INFLUENCE East Germany, UK, South Africa | 50.05 | 5.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Socialist Governments INFLUENCE East Germany, UK, South Africa | 30.05 | 5.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], NORAD[38], How I Learned to Stop Worrying[49], Sadat Expels Soviets[73], Voice of America[75], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE West Germany, Argentina, Chile | 44.37 | 5.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:9.33 |
| 2 | How I Learned to Stop Worrying INFLUENCE Argentina, Chile | 28.37 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:9.33 |
| 3 | NORAD INFLUENCE West Germany, Argentina, Chile | 24.37 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | Sadat Expels Soviets INFLUENCE West Germany, Argentina, Chile | 24.37 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Voice of America INFLUENCE Argentina, Chile | 12.37 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Korean War[11], Suez Crisis[28], Arms Race[42], Bear Trap[47], Summit[48], Colonial Rear Guards[110]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, West Germany, South Africa | 43.72 | 5.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 43.72 | 5.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 3 | Summit INFLUENCE East Germany, West Germany, South Africa | 43.72 | 5.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 4 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 23.72 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 23.72 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], NORAD[38], How I Learned to Stop Worrying[49], Sadat Expels Soviets[73], Voice of America[75], Lone Gunman[109]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE Argentina, Chile | 26.50 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:11.20 |
| 2 | NORAD INFLUENCE West Germany, Argentina, Chile | 22.50 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | Sadat Expels Soviets INFLUENCE West Germany, Argentina, Chile | 22.50 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Voice of America INFLUENCE Argentina, Chile | 10.50 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Nasser INFLUENCE Chile | 10.45 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Korean War[11], Suez Crisis[28], Bear Trap[47], Summit[48], Colonial Rear Guards[110]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 41.85 | 5.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 2 | Summit INFLUENCE East Germany, West Germany, South Africa | 41.85 | 5.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 3 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 21.85 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 21.85 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Korean War INFLUENCE West Germany, South Africa | 10.45 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], NORAD[38], Sadat Expels Soviets[73], Voice of America[75], Lone Gunman[109]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Argentina, Chile | 19.70 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Sadat Expels Soviets INFLUENCE West Germany, Argentina, Chile | 19.70 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Voice of America INFLUENCE Argentina, Chile | 7.70 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Nasser INFLUENCE Chile | 7.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 5 | Lone Gunman INFLUENCE Chile | 7.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Korean War[11], Suez Crisis[28], Summit[48], Colonial Rear Guards[110]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, West Germany, South Africa | 39.05 | 5.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 2 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 19.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 19.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Korean War INFLUENCE West Germany, South Africa | 7.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 7.65 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Sadat Expels Soviets[73], Voice of America[75], Lone Gunman[109]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE West Germany, Argentina, Chile | 15.03 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Voice of America INFLUENCE Argentina, Chile | 3.03 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Nasser INFLUENCE Chile | 2.98 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:18.67 |
| 4 | Lone Gunman INFLUENCE Chile | 2.98 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:18.67 |
| 5 | Voice of America SPACE | -10.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], Korean War[11], Suez Crisis[28], Colonial Rear Guards[110]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 14.38 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 14.38 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Korean War INFLUENCE West Germany, South Africa | 2.98 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 4 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 2.98 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | Korean War SPACE | -10.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Voice of America[75], Lone Gunman[109]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE Argentina, Chile | -27.30 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Nasser INFLUENCE Chile | -27.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:49.00 |
| 3 | Lone Gunman INFLUENCE Chile | -27.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:49.00 |
| 4 | Voice of America SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 5 | Nasser REALIGN Chile | -44.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Korean War[11], Suez Crisis[28], Colonial Rear Guards[110]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | -15.95 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Korean War INFLUENCE West Germany, South Africa | -27.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 3 | Colonial Rear Guards INFLUENCE West Germany, South Africa | -27.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Korean War SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 5 | Colonial Rear Guards SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Lone Gunman[109]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Chile | -55.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:77.00 |
| 2 | Lone Gunman INFLUENCE Chile | -55.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:77.00 |
| 3 | Nasser REALIGN Chile | -72.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:77.00 |
| 4 | Lone Gunman REALIGN Chile | -72.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:77.00 |
| 5 | Nasser EVENT | -74.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Korean War[11], Colonial Rear Guards[110]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, South Africa | -55.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, South Africa | -55.35 | 5.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | Korean War SPACE | -69.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 4 | Colonial Rear Guards SPACE | -69.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 5 | Korean War EVENT | -83.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 107: T8 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Willy Brandt[58], Muslim Revolution[59], OPEC[64], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Liberation Theology[76], Che[83], Our Man in Tehran[84]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Arab-Israeli War[13], CIA Created[26], ABM Treaty[60], OAS Founded[71], Liberation Theology[76], Alliance for Progress[79], Soviets Shoot Down KAL 007[92], Iran-Contra Scandal[96], Chernobyl[97]`
- state: `VP -7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Chernobyl EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Willy Brandt[58], OPEC[64], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Liberation Theology[76], Che[83], Our Man in Tehran[84]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, West Germany, Pakistan | 46.56 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:9.14 |
| 2 | Che INFLUENCE East Germany, West Germany, Pakistan | 46.56 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:9.14 |
| 3 | Willy Brandt INFLUENCE West Germany, Pakistan | 30.41 | 5.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:9.14 |
| 4 | Liberation Theology INFLUENCE West Germany, Pakistan | 30.41 | 5.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:9.14 |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Pakistan | 26.56 | 5.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Soviets Shoot Down KAL 007 [92] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Arab-Israeli War[13], CIA Created[26], OAS Founded[71], Liberation Theology[76], Alliance for Progress[79], Soviets Shoot Down KAL 007[92], Iran-Contra Scandal[96], Chernobyl[97]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, France, Poland, West Germany | 61.06 | 5.00 | 65.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 44.91 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Chernobyl INFLUENCE East Germany, France, West Germany | 44.91 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Arab-Israeli War INFLUENCE East Germany, West Germany | 12.76 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 5 | Liberation Theology INFLUENCE East Germany, West Germany | 12.76 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Willy Brandt[58], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Liberation Theology[76], Che[83], Our Man in Tehran[84]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 43.38 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Willy Brandt INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 23.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Arab-Israeli War[13], CIA Created[26], OAS Founded[71], Liberation Theology[76], Alliance for Progress[79], Iran-Contra Scandal[96], Chernobyl[97]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 43.38 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Chernobyl INFLUENCE East Germany, France, West Germany | 43.38 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Arab-Israeli War INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Liberation Theology INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Iran-Contra Scandal INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Willy Brandt[58], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Liberation Theology[76], Our Man in Tehran[84]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 25.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 25.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 21.25 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 9.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Our Man in Tehran INFLUENCE East Germany, West Germany | 9.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Arab-Israeli War[13], CIA Created[26], OAS Founded[71], Liberation Theology[76], Iran-Contra Scandal[96], Chernobyl[97]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, France, West Germany | 46.25 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 14.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 3 | Liberation Theology INFLUENCE France, West Germany | 14.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | Iran-Contra Scandal INFLUENCE France, West Germany | 14.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | CIA Created INFLUENCE France | 13.35 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, control_break:France, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Liberation Theology[76], Our Man in Tehran[84]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Our Man in Tehran INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Blockade INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Arab-Israeli War[13], CIA Created[26], OAS Founded[71], Liberation Theology[76], Iran-Contra Scandal[96]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Iran-Contra Scandal INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | CIA Created INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | OAS Founded INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Our Man in Tehran[84]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 12.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 0.57 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 0.57 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | Blockade INFLUENCE West Germany | 0.42 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 5 | John Paul II Elected Pope SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `CIA Created[26], OAS Founded[71], Liberation Theology[76], Iran-Contra Scandal[96]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE France, West Germany | 5.57 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | Iran-Contra Scandal INFLUENCE France, West Germany | 5.57 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | CIA Created INFLUENCE France | 4.82 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, control_break:France, non_coup_milops_penalty:21.33 |
| 4 | OAS Founded INFLUENCE France | 4.82 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, control_break:France, non_coup_milops_penalty:21.33 |
| 5 | Liberation Theology SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], John Paul II Elected Pope[69], Our Man in Tehran[84]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -34.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | Our Man in Tehran INFLUENCE East Germany, West Germany | -34.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 3 | Blockade INFLUENCE West Germany | -34.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 4 | John Paul II Elected Pope SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | Our Man in Tehran SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Iran-Contra Scandal [96] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `CIA Created[26], OAS Founded[71], Iran-Contra Scandal[96]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Contra Scandal INFLUENCE East Germany, West Germany | -34.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | CIA Created INFLUENCE West Germany | -34.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 3 | OAS Founded INFLUENCE West Germany | -34.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 4 | Iran-Contra Scandal SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | CIA Created REALIGN West Germany | -51.85 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], Our Man in Tehran[84]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | -66.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 2 | Blockade INFLUENCE West Germany | -66.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 3 | Our Man in Tehran SPACE | -80.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 4 | Blockade REALIGN West Germany | -83.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 5 | Blockade EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `CIA Created[26], OAS Founded[71]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE West Germany | -66.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 2 | OAS Founded INFLUENCE West Germany | -66.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 3 | CIA Created REALIGN West Germany | -83.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 4 | OAS Founded REALIGN West Germany | -83.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 5 | CIA Created EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Warsaw Pact Formed[16], De Gaulle Leads France[17], Independent Reds[22], Suez Crisis[28], Voice of America[75], Iranian Hostage Crisis[85], Tear Down this Wall[99], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Iranian Hostage Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Tear Down this Wall EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], Nasser[15], Indo-Pakistani War[24], NORAD[38], One Small Step[81], Marine Barracks Bombing[91], Glasnost[93], Pershing II Deployed[102]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Glasnost EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Pershing II Deployed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `De Gaulle Leads France[17], Independent Reds[22], Suez Crisis[28], Voice of America[75], Iranian Hostage Crisis[85], Tear Down this Wall[99], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | Suez Crisis INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 23.76 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 23.76 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Glasnost [93] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Indo-Pakistani War[24], One Small Step[81], Marine Barracks Bombing[91], Glasnost[93], Pershing II Deployed[102]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost INFLUENCE East Germany, France, West Germany, Cuba | 40.66 | 5.00 | 70.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 2 | Indo-Pakistani War INFLUENCE France, West Germany | 32.61 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | One Small Step INFLUENCE France, West Germany | 32.61 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 28.76 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | Arab-Israeli War INFLUENCE France, West Germany | 16.61 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Independent Reds[22], Suez Crisis[28], Voice of America[75], Iranian Hostage Crisis[85], Tear Down this Wall[99], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, Cuba | 44.80 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, control_break:Cuba, non_coup_milops_penalty:12.00 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, West Germany, Cuba | 44.80 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, control_break:Cuba, non_coup_milops_penalty:12.00 |
| 3 | Tear Down this Wall INFLUENCE East Germany, West Germany, Cuba | 24.80 | 5.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, control_break:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | AWACS Sale to Saudis INFLUENCE East Germany, West Germany, Cuba | 24.80 | 5.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, control_break:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Independent Reds INFLUENCE West Germany, Cuba | 12.65 | 5.00 | 35.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, control_break:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], Nasser[15], Indo-Pakistani War[24], One Small Step[81], Marine Barracks Bombing[91], Pershing II Deployed[102]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | One Small Step INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 22.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Arab-Israeli War INFLUENCE East Germany, West Germany | 9.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 9.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Independent Reds[22], Voice of America[75], Iranian Hostage Crisis[85], Tear Down this Wall[99], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 39.65 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 19.65 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 19.65 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Independent Reds INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | Voice of America INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], Nasser[15], One Small Step[81], Marine Barracks Bombing[91], Pershing II Deployed[102]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE France, West Germany | 28.50 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 24.65 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | Arab-Israeli War INFLUENCE France, West Germany | 12.50 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Marine Barracks Bombing INFLUENCE France, West Germany | 12.50 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | Nasser INFLUENCE France | -0.25 | 5.00 | 21.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:16.30, control_break:France, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Tear Down this Wall [99] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Independent Reds[22], Voice of America[75], Tear Down this Wall[99], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 16.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 16.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Independent Reds INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Voice of America INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Solidarity INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Pershing II Deployed [102] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Marine Barracks Bombing[91], Pershing II Deployed[102]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 21.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 8.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Marine Barracks Bombing INFLUENCE France, West Germany | 8.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Nasser INFLUENCE France | -3.85 | 5.00 | 21.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:16.30, control_break:France, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Arab-Israeli War SPACE | -10.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Independent Reds[22], Voice of America[75], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 10.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Independent Reds INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Voice of America INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Solidarity INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Independent Reds SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Marine Barracks Bombing[91]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE France, West Germany | 2.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Marine Barracks Bombing INFLUENCE France, West Germany | 2.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Nasser INFLUENCE France | -9.85 | 5.00 | 21.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:16.30, control_break:France, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Arab-Israeli War SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Marine Barracks Bombing SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Independent Reds[22], Voice of America[75], Solidarity[104]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Solidarity INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Independent Reds SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Voice of America SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Marine Barracks Bombing [91] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Nasser[15], Marine Barracks Bombing[91]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Nasser INFLUENCE West Germany | -53.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Marine Barracks Bombing SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Nasser EVENT | -69.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:63.00 |
| 5 | Marine Barracks Bombing EVENT | -69.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Voice of America[75], Solidarity[104]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | -77.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Solidarity INFLUENCE East Germany, West Germany | -77.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 3 | Voice of America SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Solidarity SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 5 | Voice of America EVENT | -105.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Nasser [15] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Nasser[15]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE West Germany | -89.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Nasser EVENT | -105.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |
| 3 | Nasser REALIGN West Germany | -106.86 | -1.00 | 5.29 | 0.00 | -12.00 | -0.15 | 0.00 | offside_ops_penalty, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Summit [48] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Olympic Games[20], Marshall Plan[23], UN Intervention[32], Formosan Resolution[35], Summit[48], How I Learned to Stop Worrying[49], Cultural Revolution[61], Flower Power[62], Ortega Elected in Nicaragua[94]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Korean War[11], Romanian Abdication[12], Captured Nazi Scientist[18], Nuclear Test Ban[34], Special Relationship[37], Bear Trap[47], We Will Bury You[53], Portuguese Empire Crumbles[55], Puppet Governments[67]`
- state: `VP -8, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -5, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Olympic Games[20], Marshall Plan[23], UN Intervention[32], Formosan Resolution[35], How I Learned to Stop Worrying[49], Cultural Revolution[61], Flower Power[62], Ortega Elected in Nicaragua[94]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Marshall Plan INFLUENCE East Germany, France, Italy, West Germany | 34.17 | 5.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 3 | Olympic Games INFLUENCE East Germany, West Germany | 26.47 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 26.47 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Flower Power INFLUENCE East Germany, West Germany | 26.47 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Korean War[11], Romanian Abdication[12], Captured Nazi Scientist[18], Special Relationship[37], Bear Trap[47], We Will Bury You[53], Portuguese Empire Crumbles[55], Puppet Governments[67]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 47.62 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | We Will Bury You INFLUENCE East Germany, France, Italy, West Germany | 39.17 | 5.00 | 70.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 3 | Special Relationship INFLUENCE France, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | Puppet Governments INFLUENCE France, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Korean War INFLUENCE France, West Germany | 15.47 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Olympic Games[20], Marshall Plan[23], UN Intervention[32], Formosan Resolution[35], How I Learned to Stop Worrying[49], Flower Power[62], Ortega Elected in Nicaragua[94]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, France, Italy, West Germany | 32.27 | 5.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Olympic Games INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | Flower Power INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 5 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Captured Nazi Scientist[18], Special Relationship[37], We Will Bury You[53], Portuguese Empire Crumbles[55], Puppet Governments[67]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, Italy, West Germany | 37.27 | 5.00 | 70.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Special Relationship INFLUENCE France, West Germany | 29.57 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Puppet Governments INFLUENCE France, West Germany | 29.57 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | Korean War INFLUENCE France, West Germany | 13.57 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 13.57 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Olympic Games[20], UN Intervention[32], Formosan Resolution[35], How I Learned to Stop Worrying[49], Flower Power[62], Ortega Elected in Nicaragua[94]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | Formosan Resolution INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Korean War[11], Romanian Abdication[12], Captured Nazi Scientist[18], Special Relationship[37], Portuguese Empire Crumbles[55], Puppet Governments[67]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Puppet Governments INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Korean War INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Captured Nazi Scientist INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `UN Intervention[32], Formosan Resolution[35], How I Learned to Stop Worrying[49], Flower Power[62], Ortega Elected in Nicaragua[94]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 17.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Flower Power INFLUENCE East Germany, West Germany | 17.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 3 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 17.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 4 | Formosan Resolution INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | UN Intervention INFLUENCE West Germany | 1.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Korean War[11], Romanian Abdication[12], Captured Nazi Scientist[18], Portuguese Empire Crumbles[55], Puppet Governments[67]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 17.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Korean War INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 1.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 5 | Romanian Abdication INFLUENCE West Germany | -10.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `UN Intervention[32], Formosan Resolution[35], Flower Power[62], Ortega Elected in Nicaragua[94]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 2 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 3 | Formosan Resolution INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | UN Intervention INFLUENCE West Germany | -4.92 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 5 | Formosan Resolution SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Captured Nazi Scientist[18], Portuguese Empire Crumbles[55]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | -4.92 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 4 | Romanian Abdication INFLUENCE West Germany | -16.92 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 5 | Korean War SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Ortega Elected in Nicaragua [94] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `UN Intervention[32], Formosan Resolution[35], Ortega Elected in Nicaragua[94]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | -32.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | UN Intervention INFLUENCE West Germany | -48.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 4 | Formosan Resolution SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | UN Intervention REALIGN West Germany | -65.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Portuguese Empire Crumbles[55]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | -48.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | -60.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 4 | Portuguese Empire Crumbles SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | Captured Nazi Scientist REALIGN West Germany | -65.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `UN Intervention[32], Formosan Resolution[35]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | -88.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | UN Intervention INFLUENCE West Germany | -88.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 3 | Formosan Resolution SPACE | -102.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 4 | UN Intervention REALIGN West Germany | -105.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | UN Intervention EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18]`
- state: `VP -13, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | -88.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -100.25 | 5.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 3 | Captured Nazi Scientist REALIGN West Germany | -105.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 4 | Captured Nazi Scientist EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | Romanian Abdication EVENT | -116.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:110.00 |

- effects: `VP +14, DEFCON +0, MilOps U+0/A+0`
