# minimal_hybrid detailed rollout log

- seed: `20260401`
- winner: `USSR`
- final_vp: `15`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], Arab-Israeli War[13], COMECON[14], Nasser[15], Independent Reds[22], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Olympic Games[20], Indo-Pakistani War[24], Red Scare/Purge[31], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], Independent Reds[22], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Iran | 71.82 | 4.00 | 68.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Arab-Israeli War COUP Iran | 71.82 | 4.00 | 68.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Romanian Abdication COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Nasser COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | East European Unrest COUP Iran | 57.17 | 4.00 | 73.62 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Olympic Games[20], Indo-Pakistani War[24], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Indonesia, Philippines | 43.67 | 5.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Indo-Pakistani War INFLUENCE Indonesia, Philippines | 43.67 | 5.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Warsaw Pact Formed INFLUENCE Iran, Indonesia, Philippines | 42.22 | 5.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | De Gaulle Leads France INFLUENCE Iran, Indonesia, Philippines | 42.22 | 5.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | De-Stalinization INFLUENCE Iran, Indonesia, Philippines | 42.22 | 5.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], Independent Reds[22], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Iran | 70.15 | 4.00 | 66.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Romanian Abdication COUP Iran | 64.80 | 4.00 | 60.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Nasser COUP Iran | 64.80 | 4.00 | 60.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | East European Unrest COUP Iran | 55.50 | 4.00 | 71.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | Independent Reds COUP Iran | 54.15 | 4.00 | 66.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Indo-Pakistani War[24], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE North Korea, Iran | 39.35 | 5.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran, non_coup_milops_penalty:1.60 |
| 2 | Warsaw Pact Formed INFLUENCE Turkey, North Korea, Iran | 36.65 | 5.00 | 53.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | De Gaulle Leads France INFLUENCE Turkey, North Korea, Iran | 36.65 | 5.00 | 53.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | De-Stalinization INFLUENCE Turkey, North Korea, Iran | 36.65 | 5.00 | 53.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Indo-Pakistani War COUP Syria | 28.45 | 4.00 | 24.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Independent Reds[22], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE North Korea, Thailand | 27.55 | 5.00 | 43.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 3 | Nasser INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 4 | Independent Reds INFLUENCE Thailand | 11.15 | 5.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | Formosan Resolution INFLUENCE Thailand | 11.15 | 5.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE East Germany, France, Turkey | 34.10 | 5.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, France, Turkey | 34.10 | 5.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | De-Stalinization INFLUENCE East Germany, France, Turkey | 34.10 | 5.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | UN Intervention COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |
| 5 | Korean War INFLUENCE East Germany, Turkey | 21.20 | 5.00 | 34.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Nasser[15], Independent Reds[22], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 2 | Nasser INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 3 | Independent Reds INFLUENCE Thailand | 14.15 | 5.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Formosan Resolution INFLUENCE Thailand | 14.15 | 5.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], De Gaulle Leads France[17], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, Pakistan, Iraq | 31.58 | 5.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | De-Stalinization INFLUENCE Italy, Pakistan, Iraq | 31.58 | 5.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | UN Intervention COUP Syria | 23.63 | 4.00 | 19.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 4 | Korean War INFLUENCE Italy, Pakistan | 19.43 | 5.00 | 33.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | UN Intervention INFLUENCE Pakistan | 19.13 | 5.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], Independent Reds[22], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 3 | Independent Reds INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Formosan Resolution INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, India, Pakistan | 34.50 | 5.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | UN Intervention COUP Syria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | Korean War INFLUENCE Italy, Pakistan | 21.10 | 5.00 | 39.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | UN Intervention INFLUENCE Pakistan | 17.80 | 5.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, non_coup_milops_penalty:7.00 |
| 5 | UN Intervention COUP Iraq | 17.65 | 4.00 | 13.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Independent Reds COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Syria | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Iraq | 19.65 | 4.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |
| 3 | Korean War COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | UN Intervention COUP Lebanon | 14.70 | 4.00 | 10.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP SE African States | 12.45 | 4.00 | 8.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +1, MilOps U-2/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Decolonization [30] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Truman Doctrine[19], NATO[21], Containment[25], US/Japan Mutual Defense Pact[27], Decolonization[30], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 3 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 4 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Vietnam Revolts[9], Marshall Plan[23], CIA Created[26], Suez Crisis[28], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], NATO[21], Containment[25], US/Japan Mutual Defense Pact[27], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Japan, Iraq, Angola, Thailand | 53.48 | 5.00 | 75.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Iraq:14.30, control_break:Iraq, influence:Angola:10.85, control_break:Angola, access_touch:Angola, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE Japan, Iraq, Angola, Thailand | 53.48 | 5.00 | 75.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Iraq:14.30, control_break:Iraq, influence:Angola:10.85, control_break:Angola, access_touch:Angola, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Five Year Plan INFLUENCE Japan, Iraq, Thailand | 39.78 | 5.00 | 57.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Containment INFLUENCE Japan, Iraq, Thailand | 39.78 | 5.00 | 57.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | NORAD INFLUENCE Japan, Iraq, Thailand | 39.78 | 5.00 | 57.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Suez Crisis[28], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Japan, Egypt, Saudi Arabia, Panama | 66.08 | 5.00 | 64.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 2 | Duck and Cover INFLUENCE Japan, Saudi Arabia, Panama | 50.53 | 5.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 3 | Nuclear Test Ban COUP SE African States | 48.83 | 4.00 | 45.43 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:5.5 |
| 4 | Duck and Cover COUP SE African States | 43.48 | 4.00 | 39.93 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:4.5 |
| 5 | Nuclear Test Ban COUP Syria | 40.68 | 4.00 | 37.28 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], Containment[25], US/Japan Mutual Defense Pact[27], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE West Germany, South Korea, Ethiopia, Thailand | 50.70 | 5.00 | 73.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 2 | Five Year Plan INFLUENCE West Germany, Ethiopia, Thailand | 37.30 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Containment INFLUENCE West Germany, Ethiopia, Thailand | 37.30 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | NORAD INFLUENCE West Germany, Ethiopia, Thailand | 37.30 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | US/Japan Mutual Defense Pact COUP Philippines | 26.20 | 4.00 | 46.80 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan, Egypt | 56.85 | 5.00 | 55.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 2 | Duck and Cover COUP SE African States | 43.75 | 4.00 | 40.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5 |
| 3 | Socialist Governments INFLUENCE West Germany, Japan, Egypt | 36.85 | 5.00 | 55.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Suez Crisis INFLUENCE West Germany, Japan, Egypt | 36.85 | 5.00 | 55.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Duck and Cover COUP Syria | 35.60 | 4.00 | 32.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], Containment[25], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Italy, Israel, Thailand | 34.35 | 5.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Containment INFLUENCE Italy, Israel, Thailand | 34.35 | 5.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | NORAD INFLUENCE Italy, Israel, Thailand | 34.35 | 5.00 | 53.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Five Year Plan COUP Philippines | 25.25 | 4.00 | 41.70 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Containment COUP Philippines | 25.25 | 4.00 | 41.70 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP SE African States | 32.45 | 4.00 | 28.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan, Libya | 28.05 | 5.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Suez Crisis INFLUENCE West Germany, Japan, Libya | 28.05 | 5.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | CIA Created COUP Japan | 25.50 | 4.00 | 21.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:0.50 |
| 5 | CIA Created COUP North Korea | 24.90 | 4.00 | 21.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:2, milops_urgency:0.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 23: T2 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], Containment[25], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Saudi Arabia, Philippines, Thailand | 32.42 | 5.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | NORAD INFLUENCE Saudi Arabia, Philippines, Thailand | 32.42 | 5.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Containment COUP Philippines | 25.92 | 4.00 | 42.37 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | NORAD COUP Philippines | 25.92 | 4.00 | 42.37 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Containment COUP Egypt | 25.17 | 4.00 | 41.62 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Japan, Libya, Philippines | 33.18 | 5.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Suez Crisis INFLUENCE Japan, Libya, Philippines | 33.18 | 5.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Socialist Governments COUP Angola | 30.98 | 4.00 | 47.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Suez Crisis COUP Angola | 30.98 | 4.00 | 47.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Angola | 29.63 | 4.00 | 41.93 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Indonesia | 37.65 | 4.00 | 54.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Special Relationship COUP Indonesia | 36.30 | 4.00 | 48.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Indonesia | 33.95 | 4.00 | 42.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | NORAD COUP Egypt | 26.50 | 4.00 | 42.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | NORAD COUP Iran | 26.50 | 4.00 | 42.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 26: T2 AR5 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Japan, Libya, Indonesia | 33.25 | 5.00 | 55.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, control_break:Libya, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Suez Crisis COUP Angola | 25.65 | 4.00 | 42.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Angola | 24.30 | 4.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Angola | 24.30 | 4.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts INFLUENCE Japan, Libya | 21.55 | 5.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan, Thailand | 25.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship COUP SE African States | 18.80 | 4.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP SE African States | 17.45 | 4.00 | 25.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Truman Doctrine INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Angola | 26.30 | 4.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Angola | 26.30 | 4.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Vietnam Revolts INFLUENCE West Germany, Japan | 14.50 | 5.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON +0, MilOps U-3/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Korean War [11] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Korean War[11], Captured Nazi Scientist[18], Olympic Games[20], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Truman Doctrine[19], East European Unrest[29], Decolonization[30], Formosan Resolution[35], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Fidel EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], Olympic Games[20], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP SE African States | 38.80 | 4.00 | 35.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Olympic Games COUP Egypt | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Olympic Games COUP Iran | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Olympic Games COUP Libya | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 32: T3 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Truman Doctrine[19], Decolonization[30], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, India, Japan | 52.90 | 5.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.00 |
| 2 | Formosan Resolution INFLUENCE West Germany, Japan | 37.50 | 5.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.00 |
| 3 | NORAD COUP Syria | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | NORAD COUP Tunisia | 34.75 | 4.00 | 31.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Formosan Resolution COUP Syria | 30.65 | 4.00 | 26.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 35.25 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 2 | Blockade COUP SE African States | 31.25 | 4.00 | 27.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP SE African States | 31.25 | 4.00 | 27.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5 |
| 4 | UN Intervention COUP SE African States | 31.25 | 4.00 | 27.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5 |
| 5 | Blockade INFLUENCE Thailand | 23.70 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Truman Doctrine[19], Decolonization[30], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE India, Japan | 41.60 | 5.00 | 41.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.80 |
| 2 | Formosan Resolution COUP Syria | 31.05 | 4.00 | 27.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |
| 3 | Formosan Resolution COUP Tunisia | 28.80 | 4.00 | 25.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |
| 4 | Formosan Resolution COUP Egypt | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |
| 5 | Fidel INFLUENCE India, Japan | 25.60 | 5.00 | 41.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Blockade[10], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP SE African States | 31.45 | 4.00 | 27.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP SE African States | 31.45 | 4.00 | 27.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 31.45 | 4.00 | 27.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5 |
| 4 | Blockade INFLUENCE Thailand | 23.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Captured Nazi Scientist INFLUENCE Thailand | 23.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Truman Doctrine[19], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Syria | 25.30 | 4.00 | 21.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:0.5 |
| 2 | Truman Doctrine COUP Tunisia | 23.05 | 4.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Egypt | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:0.5 |
| 4 | Truman Doctrine COUP Israel | 19.25 | 4.00 | 15.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3 |
| 5 | Truman Doctrine COUP Iraq | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 37: T3 AR4 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP SE African States | 31.78 | 4.00 | 27.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP SE African States | 31.78 | 4.00 | 27.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | UN Intervention INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 5 | Special Relationship INFLUENCE Japan, Thailand | 22.63 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP SE African States | 23.47 | 4.00 | 35.77 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP SE African States | 23.47 | 4.00 | 35.77 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Decolonization COUP SE African States | 23.47 | 4.00 | 35.77 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP SE African States | 21.12 | 4.00 | 29.27 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Fidel INFLUENCE Japan, Egypt | 18.22 | 5.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 39: T3 AR5 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP SE African States | 32.45 | 4.00 | 28.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Iran | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | UN Intervention COUP Libya | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Special Relationship COUP SE African States | 21.80 | 4.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP SE African States | 20.45 | 4.00 | 28.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Japan, Egypt | 16.55 | 5.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Decolonization INFLUENCE Japan, Egypt | 16.55 | 5.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Vietnam Revolts COUP Tunisia | 11.40 | 4.00 | 23.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Decolonization COUP Tunisia | 11.40 | 4.00 | 23.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Tunisia | 10.05 | 4.00 | 18.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `CIA Created[26], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP SE African States | 23.80 | 4.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | CIA Created COUP SE African States | 22.45 | 4.00 | 30.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Special Relationship COUP Iran | 18.15 | 4.00 | 30.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Special Relationship COUP Libya | 18.15 | 4.00 | 30.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | CIA Created COUP Iran | 16.80 | 4.00 | 24.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP SE African States | 23.80 | 4.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP SE African States | 22.45 | 4.00 | 30.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Decolonization COUP Tunisia | 13.40 | 4.00 | 25.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Tunisia | 12.05 | 4.00 | 20.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Decolonization COUP Egypt | 11.15 | 4.00 | 23.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 43: T4 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Romanian Abdication[12], Arab-Israeli War[13], NATO[21], Containment[25], UN Intervention[32], Special Relationship[37], ABM Treaty[60], Alliance for Progress[79]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Arms Race [42] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], CIA Created[26], Decolonization[30], UN Intervention[32], Formosan Resolution[35], Arms Race[42], U2 Incident[63]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Romanian Abdication[12], Arab-Israeli War[13], NATO[21], Containment[25], UN Intervention[32], Special Relationship[37], Alliance for Progress[79]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE UK, Mexico, Algeria, South Africa | 41.93 | 5.00 | 66.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Arab-Israeli War COUP SE African States | 41.84 | 4.00 | 38.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |
| 3 | Arab-Israeli War COUP Indonesia | 41.84 | 4.00 | 38.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Iran | 38.94 | 4.00 | 35.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:1.5 |
| 5 | Arab-Israeli War COUP Libya | 38.94 | 4.00 | 35.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], CIA Created[26], Decolonization[30], UN Intervention[32], Formosan Resolution[35], U2 Incident[63]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Indonesia | 41.84 | 4.00 | 38.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:3.5 |
| 2 | Formosan Resolution COUP Mexico | 40.69 | 4.00 | 36.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:1.5 |
| 3 | Formosan Resolution COUP Algeria | 39.94 | 4.00 | 36.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:1.5 |
| 4 | CIA Created COUP Indonesia | 35.49 | 4.00 | 31.64 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:2.5 |
| 5 | UN Intervention COUP Indonesia | 35.49 | 4.00 | 31.64 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 47: T4 AR2 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Romanian Abdication[12], Arab-Israeli War[13], Containment[25], UN Intervention[32], Special Relationship[37], Alliance for Progress[79]`
- state: `VP 1, DEFCON 4, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP SE African States | 42.22 | 4.00 | 38.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Indonesia | 42.22 | 4.00 | 38.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:3.5 |
| 3 | Arab-Israeli War COUP Iran | 39.32 | 4.00 | 35.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 4 | Arab-Israeli War COUP Libya | 39.32 | 4.00 | 35.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 5 | Arab-Israeli War INFLUENCE Mexico, Algeria | 38.52 | 5.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 48: T4 AR2 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], CIA Created[26], Decolonization[30], UN Intervention[32], U2 Incident[63]`
- state: `VP 1, DEFCON 4, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP SE African States | 34.53 | 4.00 | 30.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 2 | CIA Created COUP Indonesia | 34.53 | 4.00 | 30.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 34.53 | 4.00 | 30.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 4 | UN Intervention COUP Indonesia | 34.53 | 4.00 | 30.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:2.5 |
| 5 | CIA Created COUP Mexico | 33.38 | 4.00 | 29.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Romanian Abdication[12], Containment[25], UN Intervention[32], Special Relationship[37], Alliance for Progress[79]`
- state: `VP 1, DEFCON 4, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Angola | 45.30 | 4.00 | 41.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Angola | 45.30 | 4.00 | 41.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 3 | Duck and Cover INFLUENCE Mexico, Algeria, Angola | 38.10 | 5.00 | 56.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Angola:15.60, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Containment INFLUENCE Mexico, Algeria, Angola | 38.10 | 5.00 | 56.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Angola:15.60, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Alliance for Progress INFLUENCE Mexico, Algeria, Angola | 38.10 | 5.00 | 56.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Angola:15.60, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], Decolonization[30], UN Intervention[32], U2 Incident[63]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP SE African States | 34.80 | 4.00 | 30.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 2 | Socialist Governments INFLUENCE Mexico, Algeria, South Africa | 31.30 | 5.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | U2 Incident INFLUENCE Mexico, Algeria, South Africa | 31.30 | 5.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Socialist Governments COUP SE African States | 26.50 | 4.00 | 42.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | U2 Incident COUP SE African States | 26.50 | 4.00 | 42.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Containment[25], UN Intervention[32], Special Relationship[37], Alliance for Progress[79]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Mexico, Algeria, Morocco | 36.50 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Containment INFLUENCE Mexico, Algeria, Morocco | 36.50 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Alliance for Progress INFLUENCE Mexico, Algeria, Morocco | 36.50 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | UN Intervention COUP Iran | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Libya | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], Decolonization[30], U2 Incident[63]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Mexico, Algeria, South Africa | 30.50 | 5.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | U2 Incident INFLUENCE Mexico, Algeria, South Africa | 30.50 | 5.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Socialist Governments COUP SE African States | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | U2 Incident COUP SE African States | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Fidel COUP SE African States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Containment[25], UN Intervention[32], Special Relationship[37], Alliance for Progress[79]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Mexico, Algeria, South Africa | 35.17 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Alliance for Progress INFLUENCE Mexico, Algeria, South Africa | 35.17 | 5.00 | 55.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | UN Intervention COUP Iran | 26.97 | 4.00 | 23.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | UN Intervention COUP Libya | 26.97 | 4.00 | 23.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Special Relationship INFLUENCE Mexico, Algeria | 22.52 | 5.00 | 39.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Blockade[10], Decolonization[30], U2 Incident[63]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE West Germany, Morocco, South Africa | 28.97 | 5.00 | 49.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | U2 Incident COUP SE African States | 27.57 | 4.00 | 44.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Fidel COUP SE African States | 26.22 | 4.00 | 38.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP SE African States | 26.22 | 4.00 | 38.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP SE African States | 23.87 | 4.00 | 32.02 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `UN Intervention[32], Special Relationship[37], Alliance for Progress[79]`
- state: `VP 1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Iran | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Libya | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | UN Intervention COUP Mexico | 23.05 | 4.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | UN Intervention COUP Algeria | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | UN Intervention COUP South Africa | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Blockade[10], Decolonization[30]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP SE African States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP SE African States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Blockade COUP SE African States | 25.20 | 4.00 | 33.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Fidel COUP Tunisia | 17.15 | 4.00 | 29.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Decolonization COUP Tunisia | 17.15 | 4.00 | 29.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Special Relationship[37], Alliance for Progress[79]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP SE African States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Special Relationship COUP SE African States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Alliance for Progress INFLUENCE Iran, Congo/Zaire, South Africa | 13.75 | 5.00 | 51.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 4 | Alliance for Progress COUP Saharan States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Sudan | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 58: T4 AR7 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Decolonization[30]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Tunisia | 21.15 | 4.00 | 33.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Blockade COUP Tunisia | 18.80 | 4.00 | 26.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Decolonization COUP Colombia | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Mozambique | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Brush War [39] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Olympic Games[20], Decolonization[30], Brush War[39], Kitchen Debates[51], Cultural Revolution[61], John Paul II Elected Pope[69], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Independent Reds [22] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Independent Reds[22], De-Stalinization[33], Special Relationship[37], Junta[50], OAS Founded[71], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Olympic Games[20], Decolonization[30], Kitchen Debates[51], Cultural Revolution[61], John Paul II Elected Pope[69], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE Iran, Congo/Zaire, South Africa | 50.04 | 5.00 | 51.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Cultural Revolution COUP SE African States | 48.76 | 4.00 | 45.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 3 | Fidel COUP SE African States | 42.41 | 4.00 | 38.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 4 | Olympic Games COUP SE African States | 42.41 | 4.00 | 38.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 5 | Decolonization COUP SE African States | 42.41 | 4.00 | 38.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], De-Stalinization[33], Special Relationship[37], Junta[50], OAS Founded[71], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Angola | 46.91 | 4.00 | 43.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Angola | 46.91 | 4.00 | 43.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | Nixon Plays the China Card COUP Angola | 46.91 | 4.00 | 43.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 4 | Our Man in Tehran COUP Angola | 46.91 | 4.00 | 43.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 5 | Captured Nazi Scientist COUP Angola | 40.56 | 4.00 | 36.71 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 63: T5 AR2 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Olympic Games[20], Decolonization[30], Kitchen Debates[51], John Paul II Elected Pope[69], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP SE African States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games COUP SE African States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | Decolonization COUP SE African States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP SE African States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 5 | Fidel INFLUENCE Congo/Zaire, South Africa | 34.03 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 64: T5 AR2 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], De-Stalinization[33], Junta[50], OAS Founded[71], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE West Germany, South Africa | 33.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 33.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 3 | Our Man in Tehran INFLUENCE West Germany, South Africa | 33.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 4 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 29.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Junta COUP Colombia | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Olympic Games[20], Decolonization[30], Kitchen Debates[51], John Paul II Elected Pope[69], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Congo/Zaire, South Africa | 35.90 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Decolonization INFLUENCE Congo/Zaire, South Africa | 35.90 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | Latin American Death Squads INFLUENCE Congo/Zaire, South Africa | 35.90 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Congo/Zaire, South Africa | 31.90 | 5.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Olympic Games COUP Cameroon | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], De-Stalinization[33], OAS Founded[71], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 32.85 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Our Man in Tehran INFLUENCE West Germany, South Africa | 32.85 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 28.25 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Nixon Plays the China Card COUP Colombia | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | Nixon Plays the China Card COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Decolonization[30], Kitchen Debates[51], John Paul II Elected Pope[69], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 31.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany, South Africa | 31.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Angola, South Africa | 27.10 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Decolonization COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Decolonization COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], De-Stalinization[33], OAS Founded[71], Our Man in Tehran[84]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE West Germany, South Africa | 31.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 27.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Our Man in Tehran COUP Colombia | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Our Man in Tehran COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Our Man in Tehran COUP SE African States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Kitchen Debates[51], John Paul II Elected Pope[69], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Angola, South Africa | 25.10 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Latin American Death Squads COUP Cameroon | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], De-Stalinization[33], OAS Founded[71]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Captured Nazi Scientist COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Sudan | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Kitchen Debates[51], John Paul II Elected Pope[69], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, South Africa | 17.05 | 5.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | Ask Not What Your Country Can Do For You COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP SE African States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP Sudan | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], OAS Founded[71]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Sudan | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Zimbabwe | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Kitchen Debates[51], John Paul II Elected Pope[69]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope COUP Zimbabwe | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], OAS Founded[71]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Colombia | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | OAS Founded COUP Saharan States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | OAS Founded COUP SE African States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP Sudan | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP Zimbabwe | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 75: T6 AR0 USSR

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Indo-Pakistani War[24], East European Unrest[29], Cuban Missile Crisis[43], Brezhnev Doctrine[54], Camp David Accords[66], One Small Step[81], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Red Scare/Purge[31], How I Learned to Stop Worrying[49], Allende[57], Willy Brandt[58], Flower Power[62], Lonely Hearts Club Band[65], Puppet Governments[67], Shuttle Diplomacy[74]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Indo-Pakistani War[24], East European Unrest[29], Brezhnev Doctrine[54], Camp David Accords[66], One Small Step[81], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE Nigeria, South Africa | 35.09 | 5.00 | 37.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | Captured Nazi Scientist INFLUENCE Nigeria | 18.59 | 5.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 3 | Lone Gunman INFLUENCE Nigeria | 18.59 | 5.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 4 | Indo-Pakistani War INFLUENCE Nigeria | 18.44 | 5.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 5 | One Small Step INFLUENCE Nigeria | 18.44 | 5.00 | 20.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], How I Learned to Stop Worrying[49], Allende[57], Willy Brandt[58], Flower Power[62], Lonely Hearts Club Band[65], Puppet Governments[67], Shuttle Diplomacy[74]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE Brazil, Venezuela, South Africa | 46.89 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | How I Learned to Stop Worrying INFLUENCE Brazil, South Africa | 30.84 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | Lonely Hearts Club Band INFLUENCE Brazil, South Africa | 30.84 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 4 | Puppet Governments INFLUENCE Brazil, South Africa | 30.84 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 5 | Willy Brandt INFLUENCE Brazil, South Africa | 14.84 | 5.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Indo-Pakistani War[24], East European Unrest[29], Camp David Accords[66], One Small Step[81], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | 13.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Lone Gunman INFLUENCE South Africa | 13.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Indo-Pakistani War INFLUENCE South Africa | 13.50 | 5.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | One Small Step INFLUENCE South Africa | 13.50 | 5.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Colonial Rear Guards INFLUENCE South Africa | 13.50 | 5.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], How I Learned to Stop Worrying[49], Allende[57], Willy Brandt[58], Flower Power[62], Lonely Hearts Club Band[65], Puppet Governments[67]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE Brazil, Venezuela | 35.10 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 2 | Lonely Hearts Club Band INFLUENCE Brazil, Venezuela | 35.10 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 3 | Puppet Governments INFLUENCE Brazil, Venezuela | 35.10 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 4 | Willy Brandt INFLUENCE Brazil, Venezuela | 19.10 | 5.00 | 38.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Flower Power INFLUENCE Brazil, Venezuela | 19.10 | 5.00 | 38.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Indo-Pakistani War[24], East European Unrest[29], Camp David Accords[66], One Small Step[81], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE South Africa | 17.05 | 5.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:9.60 |
| 2 | Indo-Pakistani War INFLUENCE South Africa | 16.90 | 5.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:9.60 |
| 3 | One Small Step INFLUENCE South Africa | 16.90 | 5.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:9.60 |
| 4 | Colonial Rear Guards INFLUENCE South Africa | 16.90 | 5.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:9.60 |
| 5 | East European Unrest INFLUENCE West Germany, South Africa | 12.90 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Allende[57], Willy Brandt[58], Flower Power[62], Lonely Hearts Club Band[65], Puppet Governments[67]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE Argentina, South Africa | 30.10 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 2 | Puppet Governments INFLUENCE Argentina, South Africa | 30.10 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 3 | Willy Brandt INFLUENCE Argentina, South Africa | 14.10 | 5.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Flower Power INFLUENCE Argentina, South Africa | 14.10 | 5.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Truman Doctrine INFLUENCE Argentina | 13.45 | 5.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Indo-Pakistani War[24], East European Unrest[29], Camp David Accords[66], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE South Africa | 14.50 | 5.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:12.00 |
| 2 | One Small Step INFLUENCE South Africa | 14.50 | 5.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:12.00 |
| 3 | Colonial Rear Guards INFLUENCE South Africa | 14.50 | 5.00 | 21.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:12.00 |
| 4 | East European Unrest INFLUENCE West Germany, South Africa | 10.50 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Camp David Accords INFLUENCE South Africa | -1.50 | 5.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Allende[57], Willy Brandt[58], Flower Power[62], Puppet Governments[67]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE Argentina, Chile | 32.70 | 5.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:12.00 |
| 2 | Willy Brandt INFLUENCE Argentina, Chile | 16.70 | 5.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Flower Power INFLUENCE Argentina, Chile | 16.70 | 5.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Truman Doctrine INFLUENCE Argentina | 14.05 | 5.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:12.00 |
| 5 | Allende INFLUENCE Argentina | 2.05 | 5.00 | 21.20 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Argentina:16.20, control_break:Argentina, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `East European Unrest[29], Camp David Accords[66], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE South Africa | 5.50 | 5.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:16.00 |
| 2 | Colonial Rear Guards INFLUENCE South Africa | 5.50 | 5.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:16.00 |
| 3 | East European Unrest INFLUENCE West Germany, South Africa | 1.50 | 5.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Camp David Accords SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | East European Unrest SPACE | -8.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Allende[57], Willy Brandt[58], Flower Power[62]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE Chile, South Africa | 6.30 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Flower Power INFLUENCE Chile, South Africa | 6.30 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Truman Doctrine INFLUENCE Chile | 5.65 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:16.00 |
| 4 | Allende INFLUENCE Chile | -6.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Willy Brandt SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `East European Unrest[29], Camp David Accords[66], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE South Africa | -20.50 | 5.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 2 | East European Unrest INFLUENCE West Germany, South Africa | -24.50 | 5.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Camp David Accords SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | East European Unrest SPACE | -34.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Colonial Rear Guards REALIGN South Africa | -36.06 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Allende[57], Flower Power[62]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE Chile, South Africa | -14.70 | 5.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Truman Doctrine INFLUENCE Chile | -15.35 | 5.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:42.00 |
| 3 | Allende INFLUENCE Chile | -27.35 | 5.00 | 21.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Flower Power SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Truman Doctrine REALIGN Chile | -35.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `East European Unrest[29], Camp David Accords[66]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, South Africa | -48.50 | 5.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 2 | Camp David Accords SPACE | -58.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | East European Unrest SPACE | -58.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 4 | Camp David Accords INFLUENCE South Africa | -60.50 | 5.00 | 16.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 5 | Camp David Accords EVENT | -72.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Chile | -44.35 | 5.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:66.00 |
| 2 | Allende INFLUENCE Chile | -56.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | Truman Doctrine REALIGN Chile | -59.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:66.00 |
| 4 | Truman Doctrine EVENT | -63.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |
| 5 | Allende REALIGN Chile | -71.91 | -1.00 | 7.24 | 0.00 | -12.00 | -0.15 | 0.00 | defcon2_realign_window, offside_ops_penalty, non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 91: T7 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Suez Crisis[28], East European Unrest[29], NORAD[38], We Will Bury You[53], Portuguese Empire Crumbles[55], Sadat Expels Soviets[73], Che[83], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Formosan Resolution[35], NORAD[38], Nuclear Subs[44], SALT Negotiations[46], Missile Envy[52], Muslim Revolution[59], Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Suez Crisis[28], East European Unrest[29], NORAD[38], Portuguese Empire Crumbles[55], Sadat Expels Soviets[73], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Angola, South Africa | 45.10 | 5.00 | 48.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Angola, South Africa | 45.10 | 5.00 | 48.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | East European Unrest INFLUENCE West Germany, Angola, South Africa | 25.10 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | NORAD INFLUENCE West Germany, Angola, South Africa | 25.10 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Formosan Resolution[35], NORAD[38], Nuclear Subs[44], SALT Negotiations[46], Missile Envy[52], Muslim Revolution[59], Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Argentina, Chile, South Africa | 46.35 | 5.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | SALT Negotiations INFLUENCE Argentina, Chile, South Africa | 46.35 | 5.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Muslim Revolution INFLUENCE West Germany, Argentina, Chile, South Africa | 38.35 | 5.00 | 65.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Formosan Resolution INFLUENCE Chile, South Africa | 30.30 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Nuclear Subs INFLUENCE Chile, South Africa | 30.30 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Suez Crisis[28], East European Unrest[29], NORAD[38], Portuguese Empire Crumbles[55], Sadat Expels Soviets[73], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Angola, South Africa | 43.77 | 5.00 | 48.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 28.32 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 3 | East European Unrest INFLUENCE West Germany, Angola, South Africa | 23.77 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | NORAD INFLUENCE West Germany, Angola, South Africa | 23.77 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Sadat Expels Soviets INFLUENCE West Germany, Angola, South Africa | 23.77 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Formosan Resolution[35], Nuclear Subs[44], SALT Negotiations[46], Missile Envy[52], Muslim Revolution[59], Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE Argentina, Chile, South Africa | 45.02 | 5.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | Muslim Revolution INFLUENCE West Germany, Argentina, Chile, South Africa | 37.02 | 5.00 | 65.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 3 | Formosan Resolution INFLUENCE Chile, South Africa | 28.97 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 4 | Nuclear Subs INFLUENCE Chile, South Africa | 28.97 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 5 | Missile Envy INFLUENCE Chile, South Africa | 28.97 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `East European Unrest[29], NORAD[38], Portuguese Empire Crumbles[55], Sadat Expels Soviets[73], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 26.45 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 2 | East European Unrest INFLUENCE West Germany, Angola, South Africa | 21.90 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | NORAD INFLUENCE West Germany, Angola, South Africa | 21.90 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Sadat Expels Soviets INFLUENCE West Germany, Angola, South Africa | 21.90 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Panama Canal Returned INFLUENCE South Africa | -1.55 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Formosan Resolution[35], Nuclear Subs[44], Missile Envy[52], Muslim Revolution[59], Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE West Germany, Argentina, Chile, South Africa | 40.15 | 5.00 | 70.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 2 | Formosan Resolution INFLUENCE West Germany, Chile | 31.45 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:11.20 |
| 3 | Nuclear Subs INFLUENCE West Germany, Chile | 31.45 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:11.20 |
| 4 | Missile Envy INFLUENCE West Germany, Chile | 31.45 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:11.20 |
| 5 | Grain Sales to Soviets INFLUENCE West Germany, Chile | 31.45 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `East European Unrest[29], NORAD[38], Sadat Expels Soviets[73], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Angola, South Africa | 19.10 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | NORAD INFLUENCE West Germany, Angola, South Africa | 19.10 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Sadat Expels Soviets INFLUENCE West Germany, Angola, South Africa | 19.10 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Panama Canal Returned INFLUENCE South Africa | -4.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | East European Unrest SPACE | -6.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Formosan Resolution[35], Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Chile | 28.65 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 2 | Nuclear Subs INFLUENCE West Germany, Chile | 28.65 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 3 | Missile Envy INFLUENCE West Germany, Chile | 28.65 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 4 | Grain Sales to Soviets INFLUENCE West Germany, Chile | 28.65 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 5 | Voice of America INFLUENCE West Germany, Chile | 28.65 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `NORAD[38], Sadat Expels Soviets[73], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Angola, South Africa | 14.43 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Sadat Expels Soviets INFLUENCE West Germany, Angola, South Africa | 14.43 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Panama Canal Returned INFLUENCE South Africa | -9.02 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 4 | NORAD SPACE | -11.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | Sadat Expels Soviets SPACE | -11.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE West Germany, Chile | 23.98 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:18.67 |
| 2 | Missile Envy INFLUENCE West Germany, Chile | 23.98 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:18.67 |
| 3 | Grain Sales to Soviets INFLUENCE West Germany, Chile | 23.98 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:18.67 |
| 4 | Voice of America INFLUENCE West Germany, Chile | 23.98 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:18.67 |
| 5 | Nuclear Subs REALIGN Chile | -12.73 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Sadat Expels Soviets[73], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE West Germany, Angola, South Africa | -15.90 | 5.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Panama Canal Returned INFLUENCE South Africa | -39.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 3 | Sadat Expels Soviets SPACE | -41.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Panama Canal Returned REALIGN South Africa | -54.91 | -1.00 | 7.24 | 0.00 | -12.00 | -0.15 | 0.00 | defcon2_realign_window, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 5 | Panama Canal Returned EVENT | -55.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Missile Envy[52], Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE West Germany, Chile | -6.35 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:49.00 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany, Chile | -6.35 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:49.00 |
| 3 | Voice of America INFLUENCE West Germany, Chile | -6.35 | 5.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:49.00 |
| 4 | Missile Envy REALIGN Chile | -43.06 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:49.00 |
| 5 | Grain Sales to Soviets REALIGN Chile | -43.06 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE South Africa | -67.35 | 5.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 2 | Panama Canal Returned REALIGN South Africa | -82.91 | -1.00 | 7.24 | 0.00 | -12.00 | -0.15 | 0.00 | defcon2_realign_window, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | Panama Canal Returned EVENT | -83.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Grain Sales to Soviets[68], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE Chile, South Africa | -38.70 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:77.00 |
| 2 | Voice of America INFLUENCE Chile, South Africa | -38.70 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:77.00 |
| 3 | Grain Sales to Soviets REALIGN Chile | -71.06 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:77.00 |
| 4 | Voice of America REALIGN Chile | -71.06 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:77.00 |
| 5 | Grain Sales to Soviets EVENT | -74.80 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 0.00 | non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 107: T8 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Containment[25], De-Stalinization[33], Cultural Revolution[61], Flower Power[62], U2 Incident[63], Latin American Death Squads[70], Che[83], Iranian Hostage Crisis[85]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Iranian Hostage Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Olympic Games[20], SALT Negotiations[46], Kitchen Debates[51], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78], One Small Step[81], Yuri and Samantha[106]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Containment[25], Cultural Revolution[61], Flower Power[62], U2 Incident[63], Latin American Death Squads[70], Che[83], Iranian Hostage Crisis[85]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE France, West Germany, Ethiopia | 51.21 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:West Germany:16.90, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:9.14 |
| 2 | U2 Incident INFLUENCE France, West Germany, Ethiopia | 51.21 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:West Germany:16.90, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:9.14 |
| 3 | Che INFLUENCE France, West Germany, Ethiopia | 51.21 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:West Germany:16.90, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:9.14 |
| 4 | Iranian Hostage Crisis INFLUENCE France, West Germany, Ethiopia | 51.21 | 5.00 | 55.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:West Germany:16.90, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:9.14 |
| 5 | Flower Power INFLUENCE France, Ethiopia | 34.46 | 5.00 | 38.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, access_touch:France, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Olympic Games[20], Kitchen Debates[51], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78], One Small Step[81], Yuri and Samantha[106]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 44.91 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Olympic Games INFLUENCE East Germany, West Germany | 28.76 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 28.76 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | One Small Step INFLUENCE East Germany, West Germany | 28.76 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 12.76 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Containment[25], Flower Power[62], U2 Incident[63], Latin American Death Squads[70], Che[83], Iranian Hostage Crisis[85]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 43.38 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 43.38 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 43.38 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | Flower Power INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 5 | Latin American Death Squads INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Olympic Games[20], Kitchen Debates[51], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], One Small Step[81], Yuri and Samantha[106]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 27.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Yuri and Samantha INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Containment[25], Flower Power[62], Latin American Death Squads[70], Che[83], Iranian Hostage Crisis[85]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 41.25 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 41.25 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 25.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 4 | Latin American Death Squads INFLUENCE East Germany, West Germany | 25.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 5 | Containment INFLUENCE East Germany, France, West Germany | 21.25 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Kitchen Debates[51], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], One Small Step[81], Yuri and Samantha[106]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 25.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | One Small Step INFLUENCE East Germany, West Germany | 25.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 9.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | Yuri and Samantha INFLUENCE East Germany, West Germany | 9.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Kitchen Debates INFLUENCE West Germany | 8.95 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Containment[25], Flower Power[62], Latin American Death Squads[70], Iranian Hostage Crisis[85]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 38.05 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Flower Power INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | Containment INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Romanian Abdication INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Kitchen Debates[51], Portuguese Empire Crumbles[55], One Small Step[81], Yuri and Samantha[106]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Yuri and Samantha INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Kitchen Debates INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | Portuguese Empire Crumbles SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Containment[25], Flower Power[62], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | 16.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 2 | Latin American Death Squads INFLUENCE East Germany, West Germany | 16.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 3 | Containment INFLUENCE East Germany, France, West Germany | 12.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | Romanian Abdication INFLUENCE West Germany | 0.42 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 5 | Containment SPACE | -13.78 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Kitchen Debates[51], Portuguese Empire Crumbles[55], Yuri and Samantha[106]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 0.57 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | Yuri and Samantha INFLUENCE East Germany, West Germany | 0.57 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | Kitchen Debates INFLUENCE West Germany | 0.42 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 4 | Portuguese Empire Crumbles SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 5 | Yuri and Samantha SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Containment[25], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | -18.10 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 2 | Containment INFLUENCE East Germany, France, West Germany | -21.95 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | -34.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 4 | Containment SPACE | -48.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | Romanian Abdication REALIGN Morocco | -53.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Yuri and Samantha [106] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Kitchen Debates[51], Yuri and Samantha[106]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha INFLUENCE East Germany, West Germany | -34.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | Kitchen Debates INFLUENCE West Germany | -34.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 3 | Yuri and Samantha SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 4 | Kitchen Debates REALIGN Morocco | -53.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |
| 5 | Kitchen Debates EVENT | -53.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Romanian Abdication[12], Containment[25]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | -53.95 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -66.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 3 | Containment SPACE | -80.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 4 | Romanian Abdication REALIGN Morocco | -85.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 5 | Romanian Abdication EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Kitchen Debates [51] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Kitchen Debates[51]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates INFLUENCE West Germany | -66.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 2 | Kitchen Debates REALIGN Morocco | -85.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 3 | Kitchen Debates EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Arms Race[42], SALT Negotiations[46], Muslim Revolution[59], Camp David Accords[66], Sadat Expels Soviets[73], An Evil Empire[100], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Vietnam Revolts[9], NATO[21], Missile Envy[52], South African Unrest[56], Willy Brandt[58], Puppet Governments[67], Sadat Expels Soviets[73], One Small Step[81], Glasnost[93]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Arms Race[42], SALT Negotiations[46], Camp David Accords[66], Sadat Expels Soviets[73], An Evil Empire[100], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE France, West Germany, Egypt | 50.41 | 5.00 | 56.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:10.29 |
| 2 | SALT Negotiations INFLUENCE France, West Germany, Egypt | 50.41 | 5.00 | 56.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:10.29 |
| 3 | Decolonization INFLUENCE France, Egypt | 33.66 | 5.00 | 39.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:10.29 |
| 4 | Sadat Expels Soviets INFLUENCE France, West Germany, Egypt | 30.41 | 5.00 | 56.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | An Evil Empire INFLUENCE France, West Germany, Egypt | 30.41 | 5.00 | 56.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Vietnam Revolts[9], Missile Envy[52], South African Unrest[56], Willy Brandt[58], Puppet Governments[67], Sadat Expels Soviets[73], One Small Step[81], Glasnost[93]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 43.76 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | Glasnost INFLUENCE East Germany, France, West Germany, Cuba | 35.66 | 5.00 | 65.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 3 | Missile Envy INFLUENCE East Germany, West Germany | 27.61 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Puppet Governments INFLUENCE East Germany, West Germany | 27.61 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | One Small Step INFLUENCE East Germany, West Germany | 27.61 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Decolonization[30], SALT Negotiations[46], Camp David Accords[66], Sadat Expels Soviets[73], An Evil Empire[100], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 47.05 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Decolonization INFLUENCE France, West Germany | 30.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 27.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | An Evil Empire INFLUENCE East Germany, France, West Germany | 27.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Camp David Accords INFLUENCE France, West Germany | 14.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Glasnost [93] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Vietnam Revolts[9], Missile Envy[52], South African Unrest[56], Willy Brandt[58], Puppet Governments[67], One Small Step[81], Glasnost[93]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost INFLUENCE East Germany, France, West Germany, Cuba | 33.95 | 5.00 | 65.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Missile Envy INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | One Small Step INFLUENCE East Germany, West Germany | 25.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Vietnam Revolts INFLUENCE East Germany, West Germany | 9.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Camp David Accords[66], Sadat Expels Soviets[73], An Evil Empire[100], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE France, West Germany | 28.50 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 24.65 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | An Evil Empire INFLUENCE East Germany, France, West Germany | 24.65 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Camp David Accords INFLUENCE France, West Germany | 12.50 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | Defectors INFLUENCE France, West Germany | 12.50 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Vietnam Revolts[9], Missile Envy[52], South African Unrest[56], Willy Brandt[58], Puppet Governments[67], One Small Step[81]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 23.50 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Puppet Governments INFLUENCE East Germany, West Germany | 23.50 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 23.50 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 4 | Vietnam Revolts INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | South African Unrest INFLUENCE East Germany, West Germany | 7.50 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Camp David Accords[66], Sadat Expels Soviets[73], An Evil Empire[100], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 21.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | An Evil Empire INFLUENCE East Germany, France, West Germany | 21.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Camp David Accords INFLUENCE East Germany, West Germany | 8.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Defectors INFLUENCE East Germany, West Germany | 8.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Captured Nazi Scientist INFLUENCE East Germany | 8.15 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Vietnam Revolts[9], South African Unrest[56], Willy Brandt[58], Puppet Governments[67], One Small Step[81]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 19.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 2 | One Small Step INFLUENCE East Germany, West Germany | 19.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 3 | Vietnam Revolts INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 3.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `An Evil Empire [100] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Camp David Accords[66], An Evil Empire[100], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | An Evil Empire INFLUENCE East Germany, France, West Germany | 15.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Camp David Accords INFLUENCE East Germany, West Germany | 2.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Defectors INFLUENCE East Germany, West Germany | 2.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Captured Nazi Scientist INFLUENCE East Germany | 2.15 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:24.00 |
| 5 | Camp David Accords SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Vietnam Revolts[9], South African Unrest[56], Willy Brandt[58], One Small Step[81]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 13.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Willy Brandt INFLUENCE East Germany, West Germany | -2.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Vietnam Revolts SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Camp David Accords[66], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE East Germany, West Germany | -36.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Defectors INFLUENCE East Germany, West Germany | -36.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Captured Nazi Scientist INFLUENCE East Germany | -36.85 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:63.00 |
| 4 | Camp David Accords SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Defectors SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Vietnam Revolts[9], South African Unrest[56], Willy Brandt[58]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | -41.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Vietnam Revolts SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | South African Unrest SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Defectors [108] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Defectors[108]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Defectors INFLUENCE East Germany, West Germany | -72.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Captured Nazi Scientist INFLUENCE East Germany | -72.85 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:99.00 |
| 3 | Defectors SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Captured Nazi Scientist REALIGN East Germany | -95.19 | -1.00 | 4.96 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |
| 5 | Captured Nazi Scientist EVENT | -96.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `South African Unrest[56], Willy Brandt[58]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | -77.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Willy Brandt INFLUENCE East Germany, West Germany | -77.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 3 | South African Unrest SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Willy Brandt SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 5 | South African Unrest EVENT | -105.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Brush War [39] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `US/Japan Mutual Defense Pact[27], Formosan Resolution[35], Brush War[39], Junta[50], Kitchen Debates[51], Brezhnev Doctrine[54], Reagan Bombs Libya[87], North Sea Oil[89], Marine Barracks Bombing[91]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Marine Barracks Bombing EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Suez Crisis[28], Bear Trap[47], How I Learned to Stop Worrying[49], ABM Treaty[60], U2 Incident[63], Pershing II Deployed[102], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON -1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `US/Japan Mutual Defense Pact[27], Formosan Resolution[35], Junta[50], Kitchen Debates[51], Brezhnev Doctrine[54], Reagan Bombs Libya[87], North Sea Oil[89], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 47.62 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Cuba | 39.52 | 5.00 | 70.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 3 | Junta INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | North Sea Oil INFLUENCE East Germany, France, West Germany | 27.62 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Suez Crisis[28], Bear Trap[47], How I Learned to Stop Worrying[49], U2 Incident[63], Pershing II Deployed[102], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 26.47 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | Suez Crisis INFLUENCE East Germany, France, West Germany | 22.62 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 4 | U2 Incident INFLUENCE East Germany, France, West Germany | 22.62 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 5 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 22.62 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `US/Japan Mutual Defense Pact[27], Formosan Resolution[35], Junta[50], Kitchen Debates[51], Reagan Bombs Libya[87], North Sea Oil[89], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Cuba | 37.62 | 5.00 | 70.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Junta INFLUENCE East Germany, West Germany | 29.57 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 29.57 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | North Sea Oil INFLUENCE East Germany, France, West Germany | 25.72 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Formosan Resolution INFLUENCE East Germany, West Germany | 13.57 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Vietnam Revolts[9], Suez Crisis[28], How I Learned to Stop Worrying[49], U2 Incident[63], Pershing II Deployed[102], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | Suez Crisis INFLUENCE East Germany, France, West Germany | 20.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | U2 Incident INFLUENCE East Germany, France, West Germany | 20.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 20.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Vietnam Revolts INFLUENCE East Germany, West Germany | 8.57 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Formosan Resolution[35], Junta[50], Kitchen Debates[51], Reagan Bombs Libya[87], North Sea Oil[89], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 26.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 26.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | North Sea Oil INFLUENCE East Germany, France, West Germany | 23.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Formosan Resolution INFLUENCE East Germany, West Germany | 10.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 10.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Vietnam Revolts[9], Suez Crisis[28], U2 Incident[63], Pershing II Deployed[102], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Vietnam Revolts INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Panama Canal Returned INFLUENCE West Germany | 5.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Marine Barracks Bombing [91] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Formosan Resolution[35], Kitchen Debates[51], Reagan Bombs Libya[87], North Sea Oil[89], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 22.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | North Sea Oil INFLUENCE East Germany, France, West Germany | 19.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Formosan Resolution INFLUENCE East Germany, West Germany | 6.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 6.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Kitchen Debates INFLUENCE East Germany | -5.85 | 5.00 | 21.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Vietnam Revolts[9], U2 Incident[63], Pershing II Deployed[102], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 14.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 14.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Vietnam Revolts INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Panama Canal Returned INFLUENCE West Germany | 1.75 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 5 | Vietnam Revolts SPACE | -12.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Formosan Resolution[35], Kitchen Debates[51], Reagan Bombs Libya[87], North Sea Oil[89]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 12.38 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 0.23 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 0.23 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | Kitchen Debates INFLUENCE East Germany | -12.52 | 5.00 | 21.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 5 | Formosan Resolution SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Pershing II Deployed [102] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Vietnam Revolts[9], Pershing II Deployed[102], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 7.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | Panama Canal Returned INFLUENCE West Germany | -4.92 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 4 | Vietnam Revolts SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 5 | Pershing II Deployed SPACE | -19.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Formosan Resolution[35], Kitchen Debates[51], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | -43.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | -43.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | Kitchen Debates INFLUENCE East Germany | -55.85 | 5.00 | 21.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 4 | Formosan Resolution SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | Reagan Bombs Libya SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Vietnam Revolts[9], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | -48.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 3 | Vietnam Revolts SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 4 | Panama Canal Returned REALIGN Morocco | -67.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |
| 5 | Panama Canal Returned EVENT | -67.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Reagan Bombs Libya [87] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Kitchen Debates[51], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | -83.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | Kitchen Debates INFLUENCE East Germany | -95.85 | 5.00 | 21.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 3 | Reagan Bombs Libya SPACE | -102.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 4 | Kitchen Debates EVENT | -116.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:110.00 |
| 5 | Reagan Bombs Libya EVENT | -116.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:110.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE West Germany | -88.25 | 5.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 2 | Panama Canal Returned REALIGN Morocco | -107.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 3 | Panama Canal Returned EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP +12, DEFCON +1, MilOps U+0/A+0`
