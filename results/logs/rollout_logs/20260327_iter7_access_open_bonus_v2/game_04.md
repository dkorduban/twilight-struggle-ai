# minimal_hybrid detailed rollout log

- seed: `20260523`
- winner: `USSR`
- final_vp: `5`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], COMECON[14], Nasser[15], NATO[21], Marshall Plan[23], Decolonization[30], Red Scare/Purge[31], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], Indo-Pakistani War[24], De-Stalinization[33], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `COMECON [14] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], COMECON[14], Nasser[15], NATO[21], Marshall Plan[23], Decolonization[30], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Iran | 76.83 | 4.00 | 73.28 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Vietnam Revolts COUP Iran | 71.48 | 4.00 | 67.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Decolonization COUP Iran | 71.48 | 4.00 | 67.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Nasser COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | UN Intervention COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], Indo-Pakistani War[24], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP North Korea | 30.23 | 4.00 | 26.38 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 2 | Indo-Pakistani War COUP North Korea | 30.08 | 4.00 | 26.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 3 | Indo-Pakistani War COUP Syria | 27.98 | 4.00 | 24.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Indonesia | 25.63 | 4.00 | 21.93 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.17, empty_coup_penalty, expected_swing:3.5 |
| 5 | Captured Nazi Scientist INFLUENCE Indonesia | 25.37 | 6.00 | 20.85 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 5: T1 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15], NATO[21], Marshall Plan[23], Decolonization[30], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, Japan, South Korea, Thailand | 57.20 | 6.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, South Korea, Thailand | 57.20 | 6.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Vietnam Revolts INFLUENCE Japan, Thailand | 46.30 | 6.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 4 | Decolonization INFLUENCE Japan, Thailand | 46.30 | 6.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 5 | Nasser INFLUENCE Thailand | 28.30 | 6.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], Indo-Pakistani War[24], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Indonesia | 27.05 | 6.00 | 41.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, offside_ops_penalty |
| 2 | De Gaulle Leads France INFLUENCE West Germany, Indonesia | 27.05 | 6.00 | 41.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, offside_ops_penalty |
| 3 | De-Stalinization INFLUENCE West Germany, Indonesia | 27.05 | 6.00 | 41.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, offside_ops_penalty |
| 4 | Indo-Pakistani War COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War INFLUENCE Indonesia | 26.55 | 6.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15], Marshall Plan[23], Decolonization[30], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Italy, Israel, Philippines, Thailand | 56.65 | 6.00 | 75.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Vietnam Revolts INFLUENCE Israel, Thailand | 48.05 | 6.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |
| 3 | Decolonization INFLUENCE Israel, Thailand | 48.05 | 6.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |
| 4 | Nasser INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 5 | UN Intervention INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `none`
- hand: `Korean War[11], Romanian Abdication[12], De Gaulle Leads France[17], Indo-Pakistani War[24], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 2 | Indo-Pakistani War INFLUENCE North Korea | 23.25 | 6.00 | 17.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea |
| 3 | De Gaulle Leads France INFLUENCE Turkey, North Korea | 20.55 | 6.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 4 | De-Stalinization INFLUENCE Turkey, North Korea | 20.55 | 6.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 5 | Indo-Pakistani War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 9: T1 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china`
- hand: `Vietnam Revolts[9], Nasser[15], Decolonization[30], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Italy, Thailand | 45.60 | 6.00 | 39.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Thailand:20.45 |
| 2 | Decolonization INFLUENCE Italy, Thailand | 45.60 | 6.00 | 39.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Thailand:20.45 |
| 3 | Vietnam Revolts COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 4 | Decolonization COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], De Gaulle Leads France[17], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Turkey, North Korea | 20.55 | 6.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 2 | De-Stalinization INFLUENCE Turkey, North Korea | 20.55 | 6.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE North Korea | 11.40 | 6.00 | 17.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 4 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | De Gaulle Leads France SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], Decolonization[30], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 2 | Decolonization COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 3 | Nasser INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea |
| 4 | UN Intervention INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea |
| 5 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France | 19.65 | 6.00 | 34.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE East Germany | 10.90 | 6.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, offside_ops_penalty |
| 3 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | De-Stalinization SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Korean War INFLUENCE East Germany | 6.75 | 6.00 | 17.05 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12]`
- state: `VP 0, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Italy | 10.30 | 6.00 | 16.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |
| 2 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Korean War INFLUENCE Italy | 6.15 | 6.00 | 16.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |
| 4 | Korean War COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-3/A-2`

## Step 15: T2 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], Olympic Games[20], Independent Reds[22], US/Japan Mutual Defense Pact[27], Suez Crisis[28], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], Truman Doctrine[19], Containment[25], CIA Created[26], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Olympic Games[20], Independent Reds[22], US/Japan Mutual Defense Pact[27], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, Italy, Saudi Arabia, Thailand | 54.98 | 6.00 | 76.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Italy:14.45, control_break:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Olympic Games COUP Indonesia | 48.97 | 4.00 | 45.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 3 | Olympic Games INFLUENCE East Germany, Thailand | 43.53 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Five Year Plan INFLUENCE East Germany, Italy, Thailand | 42.83 | 6.00 | 59.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Italy:14.45, control_break:Italy, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Blockade COUP Indonesia | 42.62 | 4.00 | 38.77 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], Truman Doctrine[19], Containment[25], CIA Created[26], The Cambridge Five[36]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE France, Iraq, Panama | 52.43 | 6.00 | 49.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Iraq:14.30, access_touch:Iraq, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 2 | Containment COUP Italy | 36.92 | 4.00 | 33.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:2.5 |
| 3 | Containment COUP Philippines | 36.92 | 4.00 | 33.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:2.5 |
| 4 | Containment COUP France | 33.52 | 4.00 | 29.97 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:France, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 5 | Containment COUP Iraq | 32.77 | 4.00 | 29.22 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], Olympic Games[20], Independent Reds[22], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 49.10 | 4.00 | 45.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 2 | Blockade COUP Indonesia | 42.75 | 4.00 | 38.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 3 | Olympic Games INFLUENCE Iraq, Thailand | 42.25 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 4 | Five Year Plan INFLUENCE Japan, Iraq, Thailand | 38.25 | 6.00 | 55.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Olympic Games COUP Turkey | 36.70 | 4.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Turkey, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 20: T2 AR2 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], Truman Doctrine[19], CIA Created[26], The Cambridge Five[36]`
- state: `VP -1, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Indonesia | 42.75 | 4.00 | 38.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 2 | CIA Created COUP Indonesia | 42.75 | 4.00 | 38.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 3 | Socialist Governments COUP Indonesia | 34.45 | 4.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Fidel COUP Indonesia | 33.10 | 4.00 | 45.40 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Indonesia | 33.10 | 4.00 | 45.40 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 21: T2 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Independent Reds[22], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Iraq, Thailand | 41.45 | 6.00 | 55.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Independent Reds INFLUENCE Iraq, Thailand | 29.45 | 6.00 | 39.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE Iraq, Thailand | 29.45 | 6.00 | 39.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Special Relationship INFLUENCE Iraq, Thailand | 29.45 | 6.00 | 39.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], CIA Created[26], The Cambridge Five[36]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Japan, Egypt, Saudi Arabia | 31.70 | 6.00 | 48.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Fidel INFLUENCE Japan, Saudi Arabia | 20.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Arab-Israeli War INFLUENCE Japan, Saudi Arabia | 20.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | CIA Created INFLUENCE Saudi Arabia | 20.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:2.00 |
| 5 | The Cambridge Five INFLUENCE Japan, Saudi Arabia | 20.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china`
- hand: `Blockade[10], Independent Reds[22], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Independent Reds INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Blockade COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], The Cambridge Five[36]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Egypt | 21.88 | 6.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:2.67 |
| 2 | Fidel INFLUENCE Japan, Egypt | 21.88 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Arab-Israeli War INFLUENCE Japan, Egypt | 21.88 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | The Cambridge Five INFLUENCE Japan, Egypt | 21.88 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | CIA Created COUP Lebanon | 11.37 | 4.00 | 7.52 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Independent Reds COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], The Cambridge Five[36]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Iran | 14.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Arab-Israeli War INFLUENCE Japan, Iran | 14.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | The Cambridge Five INFLUENCE Japan, Iran | 14.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Fidel SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | Arab-Israeli War SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Special Relationship COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], The Cambridge Five[36]`
- state: `VP -1, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Pakistan, Iran | 14.35 | 6.00 | 35.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | The Cambridge Five INFLUENCE Pakistan, Iran | 14.35 | 6.00 | 35.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | Arab-Israeli War COUP Israel | 2.10 | 4.00 | 14.40 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |
| 4 | The Cambridge Five COUP Israel | 2.10 | 4.00 | 14.40 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Lebanon | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], Romanian Abdication[12], Warsaw Pact Formed[16], East European Unrest[29], Red Scare/Purge[31], Nuclear Test Ban[34]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Nasser[15], De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], NATO[21], Containment[25], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], Romanian Abdication[12], Warsaw Pact Formed[16], East European Unrest[29], Nuclear Test Ban[34]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Japan, Egypt, Indonesia, Thailand | 69.55 | 6.00 | 68.15 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Nuclear Test Ban COUP Indonesia | 61.00 | 4.00 | 57.60 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:5.5 |
| 3 | Warsaw Pact Formed COUP Indonesia | 55.65 | 4.00 | 52.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 4 | Warsaw Pact Formed INFLUENCE Japan, Indonesia, Thailand | 54.00 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Nuclear Test Ban COUP Egypt | 49.85 | 4.00 | 46.45 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Containment [25] as COUP`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Nasser[15], De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Containment[25], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment COUP Indonesia | 48.65 | 4.00 | 45.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 2 | Formosan Resolution COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 3 | Containment INFLUENCE Pakistan, Egypt | 40.20 | 6.00 | 38.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:4.00 |
| 4 | Containment COUP Philippines | 38.25 | 4.00 | 34.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 5 | Containment COUP Egypt | 37.50 | 4.00 | 33.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 33: T3 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], Romanian Abdication[12], Warsaw Pact Formed[16], East European Unrest[29]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Japan, Indonesia, Thailand | 53.20 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | Warsaw Pact Formed COUP Iran | 38.70 | 4.00 | 35.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Fidel INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 4 | Warsaw Pact Formed COUP Syria | 36.20 | 4.00 | 32.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 5 | Duck and Cover INFLUENCE Japan, Indonesia, Thailand | 33.20 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `none`
- hand: `Blockade[10], Nasser[15], De Gaulle Leads France[17], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Pakistan | 25.80 | 6.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan |
| 2 | Truman Doctrine INFLUENCE Pakistan | 25.80 | 6.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan |
| 3 | Formosan Resolution INFLUENCE Pakistan | 25.65 | 6.00 | 19.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan |
| 4 | De Gaulle Leads France INFLUENCE Pakistan, Egypt | 24.20 | 6.00 | 38.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 5 | Formosan Resolution COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], Romanian Abdication[12], East European Unrest[29]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 41.30 | 6.00 | 41.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | Duck and Cover INFLUENCE Japan, Iran, Thailand | 36.85 | 6.00 | 57.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Five Year Plan INFLUENCE Japan, Iran, Thailand | 36.85 | 6.00 | 57.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | East European Unrest INFLUENCE Japan, Iran, Thailand | 36.85 | 6.00 | 57.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Fidel COUP Iran | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `Blockade[10], Nasser[15], De Gaulle Leads France[17], Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Egypt | 24.55 | 6.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt |
| 2 | Formosan Resolution INFLUENCE Egypt | 24.40 | 6.00 | 18.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt |
| 3 | De Gaulle Leads France INFLUENCE India, Egypt | 21.80 | 6.00 | 36.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 4 | Formosan Resolution COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 5 | Formosan Resolution COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Duck and Cover[4], Five Year Plan[5], Romanian Abdication[12], East European Unrest[29]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Iran, Thailand | 29.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Five Year Plan INFLUENCE Japan, Iran, Thailand | 29.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | East European Unrest INFLUENCE Japan, Iran, Thailand | 29.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Romanian Abdication COUP Iran | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Romanian Abdication COUP Syria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `none`
- hand: `Blockade[10], Nasser[15], De Gaulle Leads France[17], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Iran | 24.40 | 6.00 | 18.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran |
| 2 | De Gaulle Leads France INFLUENCE India, Iran | 21.80 | 6.00 | 36.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Iran:13.70, control_break:Iran, offside_ops_penalty |
| 3 | Formosan Resolution COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 4 | Formosan Resolution COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |
| 5 | Formosan Resolution COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Romanian Abdication[12], East European Unrest[29]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Syria | 25.30 | 4.00 | 21.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 2 | Romanian Abdication COUP Egypt | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 3 | Romanian Abdication COUP Iran | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 4 | Romanian Abdication COUP Israel | 19.25 | 4.00 | 15.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3 |
| 5 | Romanian Abdication COUP Iraq | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 40: T3 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Nasser[15], De Gaulle Leads France[17]`
- state: `VP 0, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE India, Japan | 19.25 | 6.00 | 33.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, offside_ops_penalty |
| 2 | Blockade INFLUENCE India | 11.40 | 6.00 | 17.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, offside_ops_penalty |
| 3 | Nasser INFLUENCE India | 11.40 | 6.00 | 17.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, offside_ops_penalty |
| 4 | De Gaulle Leads France SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | De Gaulle Leads France COUP Lebanon | 0.40 | 4.00 | 16.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Five Year Plan [5] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], East European Unrest[29]`
- state: `VP 0, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan COUP Syria | 18.00 | 4.00 | 34.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | East European Unrest COUP Syria | 18.00 | 4.00 | 34.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Five Year Plan INFLUENCE Japan, Pakistan, Thailand | 17.10 | 6.00 | 53.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 4 | East European Unrest INFLUENCE Japan, Pakistan, Thailand | 17.10 | 6.00 | 53.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 5 | Five Year Plan COUP Egypt | 13.50 | 4.00 | 29.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 42: T3 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Blockade COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Nasser COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Blockade COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Captured Nazi Scientist[18], Marshall Plan[23], Containment[25], Cuban Missile Crisis[43], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Liberation Theology[76], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Ussuri River Skirmish [77] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], Muslim Revolution[59], OPEC[64], Grain Sales to Soviets[68], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON -2, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Marshall Plan[23], Containment[25], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Liberation Theology[76], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE UK, Japan, Mexico, Algeria | 45.53 | 6.00 | 68.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Japan:14.40, control_break:Japan, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Liberation Theology INFLUENCE Japan, Mexico | 37.48 | 6.00 | 36.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:4.57 |
| 3 | Containment INFLUENCE Japan, Mexico, Algeria | 33.53 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 4 | Shuttle Diplomacy INFLUENCE Japan, Mexico, Algeria | 33.53 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Alliance for Progress INFLUENCE Japan, Mexico, Algeria | 33.53 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], Muslim Revolution[59], OPEC[64], Grain Sales to Soviets[68], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE West Germany, Mexico, Algeria, South Africa | 42.93 | 6.00 | 66.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Grain Sales to Soviets INFLUENCE Mexico, South Africa | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 3 | OPEC INFLUENCE Mexico, Algeria, South Africa | 30.93 | 6.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 4 | The Cambridge Five INFLUENCE Mexico, South Africa | 18.88 | 6.00 | 33.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Captured Nazi Scientist INFLUENCE Mexico | 18.23 | 6.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Captured Nazi Scientist[18], Containment[25], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Liberation Theology[76], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE West Germany, Morocco | 33.32 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 2 | Containment INFLUENCE East Germany, West Germany, Morocco | 28.72 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Morocco | 28.72 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Alliance for Progress INFLUENCE East Germany, West Germany, Morocco | 28.72 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Captured Nazi Scientist INFLUENCE Morocco | 17.32 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], OPEC[64], Grain Sales to Soviets[68], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE India, South Africa | 40.97 | 6.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:13.80, control_break:India, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | OPEC INFLUENCE India, Morocco, South Africa | 37.62 | 6.00 | 57.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:13.80, control_break:India, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | The Cambridge Five INFLUENCE India, South Africa | 24.97 | 6.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:13.80, control_break:India, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Captured Nazi Scientist INFLUENCE South Africa | 22.32 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 5 | CIA Created INFLUENCE South Africa | 22.32 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Containment[25], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 26.40 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 26.40 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 26.40 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 15.60 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.40 |
| 5 | Lone Gunman INFLUENCE West Germany | 15.60 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], OPEC[64], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE West Germany, Morocco, South Africa | 33.90 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 2 | The Cambridge Five INFLUENCE West Germany, Morocco | 21.25 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 20.60 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.40 |
| 4 | CIA Created INFLUENCE West Germany | 20.60 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.40 |
| 5 | Panama Canal Returned INFLUENCE West Germany | 20.60 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 14.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Lone Gunman INFLUENCE West Germany | 14.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 13.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, Mexico | 22.80 | 6.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | 19.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 3 | CIA Created INFLUENCE West Germany | 19.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 4 | Panama Canal Returned INFLUENCE West Germany | 19.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 5 | Nasser INFLUENCE West Germany | 7.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Nixon Plays the China Card[72], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 27.13 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Captured Nazi Scientist INFLUENCE France | 15.73 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:10.67 |
| 3 | Nixon Plays the China Card INFLUENCE France, West Germany | 15.73 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Lone Gunman INFLUENCE France | 15.73 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:10.67 |
| 5 | Nixon Plays the China Card SPACE | -2.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Captured Nazi Scientist[18], CIA Created[26], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 16.33 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 2 | CIA Created INFLUENCE West Germany | 16.33 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 3 | Panama Canal Returned INFLUENCE West Germany | 16.33 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 4 | Nasser INFLUENCE West Germany | 4.33 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Captured Nazi Scientist REALIGN South Africa | -4.58 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Captured Nazi Scientist[18], Nixon Plays the China Card[72], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | -6.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:28.00 |
| 2 | Lone Gunman INFLUENCE West Germany | -6.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:28.00 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | -6.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 4 | Nixon Plays the China Card SPACE | -20.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 5 | Captured Nazi Scientist REALIGN Mexico | -22.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], CIA Created[26], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE West Germany | -1.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:28.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | -1.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:28.00 |
| 3 | Nasser INFLUENCE West Germany | -13.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 4 | CIA Created REALIGN South Africa | -21.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:28.00 |
| 5 | Panama Canal Returned REALIGN South Africa | -21.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:28.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Nixon Plays the China Card[72], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE West Germany | -22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:44.00 |
| 2 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | -22.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 3 | Nixon Plays the China Card SPACE | -36.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 4 | Lone Gunman REALIGN Mexico | -38.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:44.00 |
| 5 | Lone Gunman EVENT | -41.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:44.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE West Germany | -17.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:44.00 |
| 2 | Nasser INFLUENCE West Germany | -29.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:44.00 |
| 3 | Panama Canal Returned REALIGN South Africa | -37.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:44.00 |
| 4 | Panama Canal Returned EVENT | -41.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:44.00 |
| 5 | Nasser REALIGN South Africa | -49.91 | -1.00 | 7.24 | 0.00 | -12.00 | -0.15 | 0.00 | defcon2_realign_window, offside_ops_penalty, non_coup_milops_penalty:44.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 59: T5 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Truman Doctrine[19], East European Unrest[29], UN Intervention[32], Arms Race[42], Quagmire[45], Portuguese Empire Crumbles[55], U2 Incident[63], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], East European Unrest[29], Red Scare/Purge[31], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Truman Doctrine[19], East European Unrest[29], UN Intervention[32], Quagmire[45], Portuguese Empire Crumbles[55], U2 Incident[63], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, West Germany | 31.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 2 | U2 Incident INFLUENCE East Germany, West Germany | 31.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 3 | UN Intervention INFLUENCE West Germany | 16.29 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 4 | Portuguese Empire Crumbles INFLUENCE West Germany | 16.14 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 5 | East European Unrest INFLUENCE East Germany, West Germany | 11.54 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], East European Unrest[29], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, West Germany, South Africa | 53.34 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | East European Unrest INFLUENCE East Germany, West Germany, South Africa | 53.34 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 37.94 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 4 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 33.34 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 5 | Che INFLUENCE East Germany, West Germany, South Africa | 33.34 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Truman Doctrine[19], East European Unrest[29], UN Intervention[32], Portuguese Empire Crumbles[55], U2 Incident[63], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, West Germany | 30.58 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 2 | UN Intervention INFLUENCE West Germany | 15.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany | 15.18 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 4 | East European Unrest INFLUENCE East Germany, West Germany | 10.58 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Truman Doctrine INFLUENCE West Germany | 3.33 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], Indo-Pakistani War[24], East European Unrest[29], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, West Germany, South Africa | 52.38 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 2 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 36.98 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 32.38 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | Che INFLUENCE East Germany, West Germany, South Africa | 32.38 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Vietnam Revolts INFLUENCE West Germany, South Africa | 20.98 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Truman Doctrine[19], East European Unrest[29], UN Intervention[32], Portuguese Empire Crumbles[55], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | 14.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany | 13.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | East European Unrest INFLUENCE East Germany, West Germany | 9.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Truman Doctrine INFLUENCE West Germany | 2.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Puppet Governments SPACE | -0.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], Indo-Pakistani War[24], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 31.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Che INFLUENCE East Germany, West Germany, South Africa | 31.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Vietnam Revolts INFLUENCE West Germany, South Africa | 19.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 19.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Truman Doctrine[19], East European Unrest[29], Portuguese Empire Crumbles[55], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany | 11.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 2 | East European Unrest INFLUENCE East Germany, West Germany | 7.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Truman Doctrine INFLUENCE West Germany | -0.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Puppet Governments SPACE | -2.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Our Man in Tehran SPACE | -2.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 29.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Che INFLUENCE East Germany, West Germany, South Africa | 29.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Vietnam Revolts INFLUENCE West Germany, South Africa | 17.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 17.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | OAS Founded INFLUENCE West Germany | 17.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Truman Doctrine[19], East European Unrest[29], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, West Germany | 3.92 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Truman Doctrine INFLUENCE West Germany | -3.33 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Puppet Governments SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Our Man in Tehran SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | East European Unrest SPACE | -5.78 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], OAS Founded[71], Che[83], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, West Germany, South Africa | 25.72 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Vietnam Revolts INFLUENCE West Germany, South Africa | 14.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 14.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | OAS Founded INFLUENCE West Germany | 13.67 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:13.33 |
| 5 | Vietnam Revolts SPACE | -5.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Truman Doctrine[19], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE West Germany | -25.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | Puppet Governments SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 3 | Our Man in Tehran SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 4 | Puppet Governments INFLUENCE West Germany | -29.15 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | Our Man in Tehran INFLUENCE West Germany | -29.15 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], OAS Founded[71], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, South Africa | -7.35 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, South Africa | -7.35 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 3 | OAS Founded INFLUENCE West Germany | -8.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:35.00 |
| 4 | Vietnam Revolts SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |
| 5 | Colonial Rear Guards SPACE | -27.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:35.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Puppet Governments [67] as SPACE`
- flags: `milops_shortfall:5, offside_ops_play, space_play`
- hand: `Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 2 | Our Man in Tehran SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 3 | Puppet Governments INFLUENCE West Germany | -49.15 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 4 | Our Man in Tehran INFLUENCE West Germany | -49.15 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 5 | Puppet Governments EVENT | -61.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `OAS Founded [71] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `OAS Founded[71], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded INFLUENCE South Africa | -32.35 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:55.00 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, South Africa | -32.35 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 3 | Colonial Rear Guards SPACE | -47.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:55.00 |
| 4 | OAS Founded REALIGN South Africa | -50.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |
| 5 | OAS Founded EVENT | -52.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:55.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 75: T6 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Romanian Abdication[12], De Gaulle Leads France[17], Red Scare/Purge[31], We Will Bury You[53], Brezhnev Doctrine[54], ABM Treaty[60], Flower Power[62]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Ask Not What Your Country Can Do For You [78] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], COMECON[14], Warsaw Pact Formed[16], Olympic Games[20], Independent Reds[22], Formosan Resolution[35], How I Learned to Stop Worrying[49], Willy Brandt[58], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Romanian Abdication[12], De Gaulle Leads France[17], We Will Bury You[53], Brezhnev Doctrine[54], ABM Treaty[60], Flower Power[62]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, West Germany, Pakistan | 60.99 | 6.00 | 62.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Pakistan:13.20, access_touch:Pakistan, non_coup_milops_penalty:6.86 |
| 2 | ABM Treaty INFLUENCE East Germany, France, West Germany, Pakistan | 60.99 | 6.00 | 62.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Pakistan:13.20, access_touch:Pakistan, non_coup_milops_penalty:6.86 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 45.94 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 45.94 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 5 | Flower Power INFLUENCE East Germany, West Germany | 30.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Korean War[11], Arab-Israeli War[13], Olympic Games[20], Independent Reds[22], Nuclear Test Ban[34], Nuclear Subs[44], Summit[48]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Pakistan, South Africa | 54.69 | 6.00 | 56.15 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Pakistan:13.20, control_break:Pakistan, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | Duck and Cover INFLUENCE West Germany, Pakistan | 38.04 | 6.00 | 39.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:6.86 |
| 3 | Summit INFLUENCE West Germany, Pakistan | 38.04 | 6.00 | 39.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:6.86 |
| 4 | Olympic Games INFLUENCE West Germany | 19.99 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.86 |
| 5 | Independent Reds INFLUENCE West Germany | 19.99 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Romanian Abdication[12], De Gaulle Leads France[17], Brezhnev Doctrine[54], ABM Treaty[60], Flower Power[62]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, West Germany, India | 60.45 | 6.00 | 63.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:India:13.80, access_touch:India, non_coup_milops_penalty:8.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany, India | 45.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:India:13.80, access_touch:India, non_coup_milops_penalty:8.00 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, India | 45.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:India:13.80, access_touch:India, non_coup_milops_penalty:8.00 |
| 4 | Flower Power INFLUENCE West Germany, India | 29.65 | 6.00 | 31.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:India:13.80, access_touch:India, non_coup_milops_penalty:8.00 |
| 5 | Five Year Plan INFLUENCE East Germany, West Germany, India | 25.05 | 6.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:India:13.80, access_touch:India, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Korean War[11], Arab-Israeli War[13], Olympic Games[20], Independent Reds[22], Nuclear Subs[44], Summit[48]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, India | 37.50 | 6.00 | 39.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:India:13.80, control_break:India, non_coup_milops_penalty:8.00 |
| 2 | Summit INFLUENCE West Germany, India | 37.50 | 6.00 | 39.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:India:13.80, control_break:India, non_coup_milops_penalty:8.00 |
| 3 | Olympic Games INFLUENCE West Germany | 18.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 4 | Independent Reds INFLUENCE West Germany | 18.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 5 | Nuclear Subs INFLUENCE West Germany | 18.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Romanian Abdication[12], De Gaulle Leads France[17], Brezhnev Doctrine[54], Flower Power[62]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 43.20 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 43.20 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 4 | Five Year Plan INFLUENCE East Germany, France, West Germany | 23.20 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Romanian Abdication INFLUENCE West Germany | 12.40 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Arab-Israeli War[13], Olympic Games[20], Independent Reds[22], Nuclear Subs[44], Summit[48]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE West Germany, South Africa | 33.90 | 6.00 | 37.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 2 | Olympic Games INFLUENCE West Germany | 17.25 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 3 | Independent Reds INFLUENCE West Germany | 17.25 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 4 | Nuclear Subs INFLUENCE West Germany | 17.25 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 5 | Korean War INFLUENCE West Germany | 1.25 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Romanian Abdication[12], Brezhnev Doctrine[54], Flower Power[62]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 40.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 2 | Flower Power INFLUENCE East Germany, West Germany | 25.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 3 | Five Year Plan INFLUENCE East Germany, France, West Germany | 20.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Romanian Abdication INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 5 | Five Year Plan SPACE | -4.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Arab-Israeli War[13], Olympic Games[20], Independent Reds[22], Nuclear Subs[44]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany | 14.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 2 | Independent Reds INFLUENCE West Germany | 14.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 3 | Nuclear Subs INFLUENCE West Germany | 14.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 4 | Korean War INFLUENCE West Germany | -1.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Arab-Israeli War INFLUENCE West Germany | -1.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Romanian Abdication[12], Flower Power[62]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:16.00 |
| 2 | Five Year Plan INFLUENCE East Germany, France, West Germany | 16.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | 6.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:16.00 |
| 4 | Five Year Plan SPACE | -8.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Romanian Abdication REALIGN Mexico | -12.93 | -1.00 | 4.22 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Arab-Israeli War[13], Independent Reds[22], Nuclear Subs[44]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany | 10.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 2 | Nuclear Subs INFLUENCE West Germany | 10.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 3 | Korean War INFLUENCE West Germany | -5.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Arab-Israeli War INFLUENCE West Germany | -5.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Korean War SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | -9.20 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -20.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:42.00 |
| 3 | Five Year Plan SPACE | -34.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Romanian Abdication REALIGN Mexico | -38.93 | -1.00 | 4.22 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:42.00 |
| 5 | Romanian Abdication EVENT | -39.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Arab-Israeli War[13], Nuclear Subs[44]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE West Germany | -15.15 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:42.00 |
| 2 | Korean War INFLUENCE West Germany | -31.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Arab-Israeli War INFLUENCE West Germany | -31.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Korean War SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Arab-Israeli War SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | -44.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:66.00 |
| 2 | Romanian Abdication REALIGN Mexico | -62.93 | -1.00 | 4.22 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |
| 3 | Romanian Abdication EVENT | -63.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany | -55.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany | -55.15 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | Korean War SPACE | -58.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 4 | Arab-Israeli War SPACE | -58.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 5 | Korean War EVENT | -72.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 91: T7 AR0 USSR

- chosen: `Brush War [39] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Duck and Cover[4], US/Japan Mutual Defense Pact[27], Special Relationship[37], Brush War[39], Missile Envy[52], Cultural Revolution[61], Sadat Expels Soviets[73], Voice of America[75], One Small Step[81]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], Socialist Governments[7], Fidel[8], Nasser[15], Nuclear Test Ban[34], SALT Negotiations[46], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Latin American Death Squads[70]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Duck and Cover[4], US/Japan Mutual Defense Pact[27], Special Relationship[37], Missile Envy[52], Cultural Revolution[61], Sadat Expels Soviets[73], Voice of America[75], One Small Step[81]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, West Germany, Nigeria | 49.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Nigeria | 41.25 | 6.00 | 67.85 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Missile Envy INFLUENCE West Germany, Nigeria | 34.45 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 4 | One Small Step INFLUENCE West Germany, Nigeria | 34.45 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 5 | Duck and Cover INFLUENCE East Germany, West Germany, Nigeria | 29.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], Socialist Governments[7], Fidel[8], Nasser[15], SALT Negotiations[46], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, West Germany, South Africa | 51.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | SALT Negotiations INFLUENCE East Germany, West Germany, South Africa | 51.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Latin American Death Squads INFLUENCE West Germany, South Africa | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Duck and Cover[4], US/Japan Mutual Defense Pact[27], Special Relationship[37], Missile Envy[52], Sadat Expels Soviets[73], Voice of America[75], One Small Step[81]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Libya | 34.52 | 6.00 | 62.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Libya:13.20, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 2 | Missile Envy INFLUENCE East Germany, West Germany | 28.07 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 28.07 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 4 | Duck and Cover INFLUENCE East Germany, France, West Germany | 23.47 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 23.47 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Nasser[15], SALT Negotiations[46], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, West Germany, South Africa | 49.72 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 34.32 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 3 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 34.32 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 4 | Latin American Death Squads INFLUENCE West Germany, South Africa | 34.32 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 5 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 29.72 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Duck and Cover[4], Special Relationship[37], Missile Envy[52], Sadat Expels Soviets[73], Voice of America[75], One Small Step[81]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE West Germany, Libya | 28.85 | 6.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Libya:13.20, control_break:Libya, non_coup_milops_penalty:11.20 |
| 2 | One Small Step INFLUENCE West Germany, Libya | 28.85 | 6.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Libya:13.20, control_break:Libya, non_coup_milops_penalty:11.20 |
| 3 | Duck and Cover INFLUENCE East Germany, West Germany, Libya | 24.25 | 6.00 | 49.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Libya:13.20, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Libya | 24.25 | 6.00 | 49.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Libya:13.20, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Special Relationship INFLUENCE West Germany, Libya | 12.85 | 6.00 | 34.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Libya:13.20, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Nasser[15], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 32.45 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 2 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 32.45 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 3 | Latin American Death Squads INFLUENCE West Germany, South Africa | 32.45 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 4 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 27.85 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Fidel INFLUENCE West Germany, South Africa | 16.45 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Duck and Cover[4], Special Relationship[37], Sadat Expels Soviets[73], Voice of America[75], One Small Step[81]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 23.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 2 | Duck and Cover INFLUENCE East Germany, France, West Germany | 18.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 18.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Special Relationship INFLUENCE East Germany, West Germany | 7.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Voice of America INFLUENCE East Germany, West Germany | 7.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Nasser[15], John Paul II Elected Pope[69], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 29.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany, South Africa | 29.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 3 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 25.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Fidel INFLUENCE West Germany, South Africa | 13.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Nasser INFLUENCE West Germany | 1.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Duck and Cover[4], Special Relationship[37], Sadat Expels Soviets[73], Voice of America[75]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 14.13 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 14.13 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Special Relationship INFLUENCE East Germany, West Germany | 2.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 4 | Voice of America INFLUENCE East Germany, West Germany | 2.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | Special Relationship SPACE | -10.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Nasser[15], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, South Africa | 24.98 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:18.67 |
| 2 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 20.38 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Fidel INFLUENCE West Germany, South Africa | 8.98 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 4 | Nasser INFLUENCE West Germany | -3.67 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | Fidel SPACE | -10.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Special Relationship[37], Sadat Expels Soviets[73], Voice of America[75]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | -16.20 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Special Relationship INFLUENCE East Germany, West Germany | -27.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 3 | Voice of America INFLUENCE East Germany, West Germany | -27.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Special Relationship SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 5 | Voice of America SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Nasser[15]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | -9.95 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Fidel INFLUENCE West Germany, South Africa | -21.35 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 3 | Nasser INFLUENCE West Germany | -34.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Fidel SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 5 | Socialist Governments SPACE | -41.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Special Relationship[37], Voice of America[75]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | -55.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | -55.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | Special Relationship SPACE | -69.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 4 | Voice of America SPACE | -69.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 5 | Special Relationship EVENT | -83.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Fidel[8], Nasser[15]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, South Africa | -49.35 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 2 | Nasser INFLUENCE West Germany | -62.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | Fidel SPACE | -69.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 4 | Nasser EVENT | -83.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |
| 5 | Fidel EVENT | -83.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 107: T8 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `milops_shortfall:8`
- hand: `UN Intervention[32], Muslim Revolution[59], Cultural Revolution[61], Camp David Accords[66], Reagan Bombs Libya[87], North Sea Oil[89], Latin American Debt Crisis[98], Solidarity[104], Colonial Rear Guards[110]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Latin American Debt Crisis EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Red Scare/Purge[31], UN Intervention[32], Nuclear Test Ban[34], Formosan Resolution[35], Special Relationship[37], How I Learned to Stop Worrying[49], Glasnost[93]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `UN Intervention[32], Cultural Revolution[61], Camp David Accords[66], Reagan Bombs Libya[87], North Sea Oil[89], Latin American Debt Crisis[98], Solidarity[104], Colonial Rear Guards[110]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE West Germany, Saudi Arabia | 31.86 | 6.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Saudi Arabia:13.55, control_break:Saudi Arabia, non_coup_milops_penalty:9.14 |
| 2 | UN Intervention INFLUENCE Saudi Arabia | 15.26 | 6.00 | 18.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Saudi Arabia:13.55, control_break:Saudi Arabia, non_coup_milops_penalty:9.14 |
| 3 | Latin American Debt Crisis INFLUENCE Saudi Arabia | 15.11 | 6.00 | 18.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:13.55, control_break:Saudi Arabia, non_coup_milops_penalty:9.14 |
| 4 | Colonial Rear Guards INFLUENCE Saudi Arabia | 15.11 | 6.00 | 18.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:13.55, control_break:Saudi Arabia, non_coup_milops_penalty:9.14 |
| 5 | North Sea Oil INFLUENCE West Germany, Saudi Arabia | 11.86 | 6.00 | 35.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Saudi Arabia:13.55, control_break:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Socialist Governments[7], Vietnam Revolts[9], UN Intervention[32], Nuclear Test Ban[34], Formosan Resolution[35], Special Relationship[37], How I Learned to Stop Worrying[49], Glasnost[93]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE East Germany, France, Poland, West Germany | 67.06 | 6.00 | 70.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 2 | Glasnost INFLUENCE East Germany, France, Poland, West Germany | 43.06 | 6.00 | 70.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 3 | Formosan Resolution INFLUENCE East Germany, West Germany | 34.76 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 4 | Special Relationship INFLUENCE East Germany, West Germany | 34.76 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 5 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 34.76 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `UN Intervention[32], Camp David Accords[66], Reagan Bombs Libya[87], North Sea Oil[89], Latin American Debt Crisis[98], Solidarity[104], Colonial Rear Guards[110]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | 12.08 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Latin American Debt Crisis INFLUENCE West Germany | 11.93 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Colonial Rear Guards INFLUENCE West Germany | 11.93 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | North Sea Oil INFLUENCE East Germany, West Germany | 8.08 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Camp David Accords SPACE | -2.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Glasnost [93] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], UN Intervention[32], Formosan Resolution[35], Special Relationship[37], How I Learned to Stop Worrying[49], Glasnost[93]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost INFLUENCE East Germany, France, West Germany, Cuba | 41.28 | 6.00 | 70.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 3 | Special Relationship INFLUENCE East Germany, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 4 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 5 | Socialist Governments INFLUENCE East Germany, France, West Germany | 29.38 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Latin American Debt Crisis [98] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Camp David Accords[66], Reagan Bombs Libya[87], North Sea Oil[89], Latin American Debt Crisis[98], Solidarity[104], Colonial Rear Guards[110]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Debt Crisis INFLUENCE West Germany | 9.80 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Colonial Rear Guards INFLUENCE West Germany | 9.80 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | North Sea Oil INFLUENCE East Germany, West Germany | 5.95 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | Camp David Accords SPACE | -5.10 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Reagan Bombs Libya SPACE | -5.10 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Socialist Governments[7], Vietnam Revolts[9], UN Intervention[32], Formosan Resolution[35], Special Relationship[37], How I Learned to Stop Worrying[49]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | 31.10 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 2 | Special Relationship INFLUENCE East Germany, West Germany | 31.10 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 31.10 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 4 | Socialist Governments INFLUENCE East Germany, France, West Germany | 27.25 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Vietnam Revolts INFLUENCE East Germany, West Germany | 15.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Camp David Accords[66], Reagan Bombs Libya[87], North Sea Oil[89], Solidarity[104], Colonial Rear Guards[110]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE West Germany | 6.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | North Sea Oil INFLUENCE East Germany, West Germany | 2.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Camp David Accords SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Reagan Bombs Libya SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Solidarity SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Socialist Governments[7], Vietnam Revolts[9], UN Intervention[32], Special Relationship[37], How I Learned to Stop Worrying[49]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 3 | Socialist Governments INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Vietnam Revolts INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | UN Intervention INFLUENCE West Germany | 11.75 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Camp David Accords[66], Reagan Bombs Libya[87], North Sea Oil[89], Solidarity[104]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, West Germany | -2.58 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | Camp David Accords SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | Reagan Bombs Libya SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | Solidarity SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 5 | North Sea Oil SPACE | -13.78 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Socialist Governments[7], Vietnam Revolts[9], UN Intervention[32], How I Learned to Stop Worrying[49]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 22.57 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:21.33 |
| 2 | Socialist Governments INFLUENCE East Germany, France, West Germany | 18.72 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | Vietnam Revolts INFLUENCE East Germany, West Germany | 6.57 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | UN Intervention INFLUENCE West Germany | 6.42 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:21.33 |
| 5 | Vietnam Revolts SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Camp David Accords [66] as SPACE`
- flags: `milops_shortfall:8, offside_ops_play, space_play`
- hand: `Camp David Accords[66], Reagan Bombs Libya[87], Solidarity[104]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | Reagan Bombs Libya SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 3 | Solidarity SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 4 | Camp David Accords INFLUENCE West Germany | -49.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | Reagan Bombs Libya INFLUENCE West Germany | -49.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |

- effects: `VP +2, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, behind_on_space, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], UN Intervention[32]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | -20.95 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany | -33.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 3 | UN Intervention INFLUENCE West Germany | -33.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 4 | Vietnam Revolts SPACE | -43.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | Socialist Governments SPACE | -43.95 | 1.00 | 4.00 | 0.00 | 7.50 | -0.45 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Reagan Bombs Libya [87] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Reagan Bombs Libya[87], Solidarity[104]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya INFLUENCE West Germany | -81.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 2 | Solidarity INFLUENCE West Germany | -81.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 3 | Reagan Bombs Libya EVENT | -94.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:88.00 |
| 4 | Solidarity EVENT | -94.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:88.00 |
| 5 | Reagan Bombs Libya REALIGN East Germany | -100.33 | -1.00 | 4.96 | 0.00 | -16.00 | -0.30 | 0.00 | offside_ops_penalty, non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, behind_on_space, offside_ops_play`
- hand: `Vietnam Revolts[9], UN Intervention[32]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | -65.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 2 | UN Intervention INFLUENCE West Germany | -65.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 3 | Vietnam Revolts SPACE | -75.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 4 | UN Intervention REALIGN West Germany | -83.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 5 | UN Intervention EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:9`
- hand: `COMECON[14], Captured Nazi Scientist[18], Olympic Games[20], SALT Negotiations[46], South African Unrest[56], ABM Treaty[60], Puppet Governments[67], Grain Sales to Soviets[68], Wargames[103]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], Red Scare/Purge[31], The Cambridge Five[36], SALT Negotiations[46], How I Learned to Stop Worrying[49], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Wargames [103] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `COMECON[14], Captured Nazi Scientist[18], Olympic Games[20], SALT Negotiations[46], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68], Wargames[103]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames INFLUENCE East Germany, France, West Germany | 44.61 | 6.00 | 49.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | COMECON INFLUENCE East Germany, West Germany | 28.46 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | SALT Negotiations INFLUENCE East Germany, West Germany | 28.46 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 12.46 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | Olympic Games INFLUENCE West Germany | 12.31 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], The Cambridge Five[36], SALT Negotiations[46], How I Learned to Stop Worrying[49], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 28.61 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Fidel INFLUENCE East Germany, West Germany | 12.61 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | The Cambridge Five INFLUENCE East Germany, West Germany | 12.61 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `COMECON[14], Captured Nazi Scientist[18], Olympic Games[20], SALT Negotiations[46], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, West Germany | 26.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | SALT Negotiations INFLUENCE East Germany, West Germany | 26.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 10.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Olympic Games INFLUENCE West Germany | 10.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | South African Unrest INFLUENCE West Germany | 10.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], The Cambridge Five[36], SALT Negotiations[46], How I Learned to Stop Worrying[49], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 43.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Fidel INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | The Cambridge Five INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Captured Nazi Scientist INFLUENCE West Germany | 10.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], SALT Negotiations[46], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, West Germany | 24.35 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | 8.35 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 3 | Olympic Games INFLUENCE West Germany | 8.20 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 4 | South African Unrest INFLUENCE West Germany | 8.20 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 5 | Puppet Governments SPACE | -6.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], The Cambridge Five[36], How I Learned to Stop Worrying[49], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 24.50 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Fidel INFLUENCE East Germany, West Germany | 8.50 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 8.50 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 8.35 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 5 | Panama Canal Returned INFLUENCE West Germany | 8.35 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 4.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 2 | Olympic Games INFLUENCE West Germany | 4.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 3 | South African Unrest INFLUENCE West Germany | 4.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 4 | Puppet Governments SPACE | -10.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Grain Sales to Soviets SPACE | -10.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space, offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12], Captured Nazi Scientist[18], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE East Germany, West Germany | 4.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | The Cambridge Five INFLUENCE East Germany, West Germany | 4.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 4.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 4 | Panama Canal Returned INFLUENCE West Germany | 4.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 5 | Fidel SPACE | -5.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Olympic Games[20], South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany | -1.40 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 2 | South African Unrest INFLUENCE West Germany | -1.40 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 3 | Puppet Governments SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Grain Sales to Soviets SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Puppet Governments INFLUENCE West Germany | -17.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space, offside_ops_play`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | -1.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | -1.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 3 | Panama Canal Returned INFLUENCE West Germany | -1.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 4 | The Cambridge Five SPACE | -11.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Romanian Abdication INFLUENCE West Germany | -13.25 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `South African Unrest[56], Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE West Germany | -40.40 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 2 | Puppet Governments SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Grain Sales to Soviets SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Puppet Governments INFLUENCE West Germany | -56.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Grain Sales to Soviets INFLUENCE West Germany | -56.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | -40.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | -40.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | -52.25 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Captured Nazi Scientist REALIGN West Germany | -58.85 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:63.00 |
| 5 | Panama Canal Returned REALIGN West Germany | -58.85 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Puppet Governments [67] as SPACE`
- flags: `milops_shortfall:9, offside_ops_play, space_play`
- hand: `Puppet Governments[67], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U1/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Grain Sales to Soviets SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 3 | Puppet Governments INFLUENCE West Germany | -92.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Grain Sales to Soviets INFLUENCE West Germany | -92.40 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 5 | Puppet Governments EVENT | -105.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Romanian Abdication[12], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE West Germany | -76.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:99.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -88.25 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 3 | Panama Canal Returned REALIGN West Germany | -94.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |
| 4 | Panama Canal Returned EVENT | -96.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |
| 5 | Romanian Abdication EVENT | -105.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], De Gaulle Leads France[17], Marshall Plan[23], Decolonization[30], Arms Race[42], John Paul II Elected Pope[69], Latin American Death Squads[70], Che[83], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Korean War[11], East European Unrest[29], Bear Trap[47], Flower Power[62], Puppet Governments[67], OAS Founded[71], Voice of America[75], The Iron Lady[86], Aldrich Ames Remix[101]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], Marshall Plan[23], Decolonization[30], Arms Race[42], John Paul II Elected Pope[69], Latin American Death Squads[70], Che[83], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, Poland, West Germany | 46.62 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Che INFLUENCE East Germany, Poland, West Germany | 46.62 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | Marshall Plan INFLUENCE East Germany, France, Poland, West Germany | 38.77 | 6.00 | 68.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 4 | Decolonization INFLUENCE Poland, West Germany | 30.47 | 6.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Latin American Death Squads INFLUENCE Poland, West Germany | 30.47 | 6.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Korean War[11], Bear Trap[47], Flower Power[62], Puppet Governments[67], OAS Founded[71], Voice of America[75], The Iron Lady[86], Aldrich Ames Remix[101]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | Voice of America INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 23.62 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], Marshall Plan[23], Decolonization[30], John Paul II Elected Pope[69], Latin American Death Squads[70], Che[83], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | Marshall Plan INFLUENCE East Germany, France, Italy, West Germany | 33.27 | 6.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Decolonization INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | Latin American Death Squads INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 5 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Korean War[11], Flower Power[62], Puppet Governments[67], OAS Founded[71], Voice of America[75], The Iron Lady[86], Aldrich Ames Remix[101]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | Puppet Governments INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Voice of America INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 21.72 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Korean War INFLUENCE East Germany, West Germany | 9.57 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Nasser[15], Marshall Plan[23], Decolonization[30], John Paul II Elected Pope[69], Latin American Death Squads[70], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, France, Italy, West Germany | 30.60 | 6.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Decolonization INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Korean War[11], Flower Power[62], Puppet Governments[67], OAS Founded[71], Voice of America[75], Aldrich Ames Remix[101]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Korean War INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Flower Power INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], Decolonization[30], John Paul II Elected Pope[69], Latin American Death Squads[70], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 18.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Latin American Death Squads INFLUENCE East Germany, West Germany | 18.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 3 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 18.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 2.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Nasser INFLUENCE West Germany | 2.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Korean War[11], Flower Power[62], OAS Founded[71], Voice of America[75], Aldrich Ames Remix[101]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 18.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 15.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Korean War INFLUENCE East Germany, West Germany | 2.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Flower Power INFLUENCE East Germany, West Germany | 2.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | OAS Founded INFLUENCE West Germany | 2.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], John Paul II Elected Pope[69], Latin American Death Squads[70], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | 12.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 2 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 12.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -3.77 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | Nasser INFLUENCE West Germany | -3.92 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 5 | Nasser REALIGN East Germany | -22.85 | -1.00 | 4.96 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Aldrich Ames Remix [101] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Korean War[11], Flower Power[62], OAS Founded[71], Aldrich Ames Remix[101]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 8.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Korean War INFLUENCE East Germany, West Germany | -3.77 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | -3.77 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | OAS Founded INFLUENCE West Germany | -3.92 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 5 | Korean War SPACE | -14.47 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Marine Barracks Bombing [91] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], John Paul II Elected Pope[69], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | -31.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -47.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | Nasser INFLUENCE West Germany | -47.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 4 | Nasser REALIGN East Germany | -66.19 | -1.00 | 4.96 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |
| 5 | Marine Barracks Bombing REALIGN East Germany | -66.33 | -1.00 | 4.96 | 0.00 | 0.00 | -0.30 | 0.00 | non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Korean War[11], Flower Power[62], OAS Founded[71]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | -47.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | Flower Power INFLUENCE East Germany, West Germany | -47.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | OAS Founded INFLUENCE West Germany | -47.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 4 | Korean War SPACE | -57.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | Flower Power SPACE | -57.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Nasser[15], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -87.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | Nasser INFLUENCE West Germany | -87.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 3 | Nasser REALIGN East Germany | -106.19 | -1.00 | 4.96 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 4 | Nasser EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | John Paul II Elected Pope EVENT | -116.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:110.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Flower Power[62], OAS Founded[71]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U2/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | -87.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | OAS Founded INFLUENCE West Germany | -87.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 3 | Flower Power SPACE | -97.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 4 | OAS Founded REALIGN West Germany | -105.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | OAS Founded EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP +5, DEFCON +0, MilOps U+0/A+0`
