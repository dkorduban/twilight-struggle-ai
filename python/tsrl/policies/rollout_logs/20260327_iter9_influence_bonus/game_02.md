# minimal_hybrid detailed rollout log

- seed: `20260541`
- winner: `USSR`
- final_vp: `9`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Fidel[8], Vietnam Revolts[9], Truman Doctrine[19], Decolonization[30], Red Scare/Purge[31], De-Stalinization[33], Nuclear Test Ban[34], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Independent Reds[22], Marshall Plan[23], Indo-Pakistani War[24], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Nuclear Test Ban [34] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Fidel[8], Vietnam Revolts[9], Truman Doctrine[19], Decolonization[30], De-Stalinization[33], Nuclear Test Ban[34], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban COUP Iran | 82.35 | 4.00 | 78.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus |
| 2 | Nuclear Test Ban INFLUENCE West Germany, Japan, South Korea, Thailand | 78.87 | 5.00 | 75.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |
| 3 | De-Stalinization COUP Iran | 77.00 | 4.00 | 73.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 4 | Fidel COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Vietnam Revolts COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+4/A+0`

## Step 4: T1 AR1 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Independent Reds[22], Indo-Pakistani War[24], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP North Korea | 30.40 | 4.00 | 26.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 2 | UN Intervention COUP North Korea | 30.40 | 4.00 | 26.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 3 | Independent Reds COUP North Korea | 30.25 | 4.00 | 26.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 4 | Indo-Pakistani War COUP North Korea | 30.25 | 4.00 | 26.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 5 | Independent Reds COUP Syria | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 5: T1 AR2 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china`
- hand: `Fidel[8], Vietnam Revolts[9], Truman Doctrine[19], Decolonization[30], De-Stalinization[33], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U4/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan, Thailand | 62.80 | 5.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 2 | Fidel INFLUENCE Japan, Thailand | 45.30 | 5.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 3 | Vietnam Revolts INFLUENCE Japan, Thailand | 45.30 | 5.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 4 | Decolonization INFLUENCE Japan, Thailand | 45.30 | 5.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 5 | Formosan Resolution INFLUENCE Japan, Thailand | 29.30 | 5.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Independent Reds [22] as COUP`
- flags: `none`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Independent Reds[22], Indo-Pakistani War[24], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U4/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 2 | Indo-Pakistani War COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 3 | UN Intervention INFLUENCE Indonesia | 25.70 | 5.00 | 20.85 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |
| 4 | Independent Reds INFLUENCE Indonesia | 25.55 | 5.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |
| 5 | Indo-Pakistani War INFLUENCE Indonesia | 25.55 | 5.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 7: T1 AR3 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china`
- hand: `Fidel[8], Vietnam Revolts[9], Truman Doctrine[19], Decolonization[30], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE South Korea, Thailand | 47.70 | 5.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand |
| 2 | Vietnam Revolts INFLUENCE South Korea, Thailand | 47.70 | 5.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand |
| 3 | Decolonization INFLUENCE South Korea, Thailand | 47.70 | 5.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand |
| 4 | Formosan Resolution INFLUENCE South Korea, Thailand | 31.70 | 5.00 | 43.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Fidel COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `none`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Indo-Pakistani War[24], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Indonesia | 25.70 | 5.00 | 20.85 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |
| 2 | Indo-Pakistani War INFLUENCE Indonesia | 25.55 | 5.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |
| 3 | Indo-Pakistani War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 4 | Blockade INFLUENCE Indonesia | 13.70 | 5.00 | 20.85 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, offside_ops_penalty |
| 5 | Indo-Pakistani War COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china`
- hand: `Vietnam Revolts[9], Truman Doctrine[19], Decolonization[30], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Pakistan, Thailand | 42.10 | 5.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45 |
| 2 | Decolonization INFLUENCE Pakistan, Thailand | 42.10 | 5.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45 |
| 3 | Vietnam Revolts COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 4 | Decolonization COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Formosan Resolution INFLUENCE Pakistan, Thailand | 26.10 | 5.00 | 37.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `none`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Indo-Pakistani War[24]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Italy | 24.15 | 5.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy |
| 2 | Indo-Pakistani War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 3 | Indo-Pakistani War COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |
| 4 | Indo-Pakistani War COUP Zimbabwe | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, empty_coup_penalty, expected_swing:3.5 |
| 5 | Indo-Pakistani War COUP Colombia | 12.30 | 4.00 | 8.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china`
- hand: `Truman Doctrine[19], Decolonization[30], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Pakistan, Thailand | 45.10 | 5.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45 |
| 2 | Formosan Resolution INFLUENCE Pakistan, Thailand | 29.10 | 5.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Decolonization COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 4 | Truman Doctrine INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Philippines | 12.30 | 5.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 2 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Korean War INFLUENCE Philippines | 8.15 | 5.00 | 19.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 5 | Arab-Israeli War INFLUENCE Philippines | 8.15 | 5.00 | 19.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE India, Thailand | 26.70 | 5.00 | 38.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Korean War [11] as SPACE`
- flags: `offside_ops_play, space_play`
- hand: `Korean War[11], Arab-Israeli War[13]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 2 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Korean War INFLUENCE North Korea | 6.25 | 5.00 | 17.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 4 | Arab-Israeli War INFLUENCE North Korea | 6.25 | 5.00 | 17.55 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty |
| 5 | Korean War COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-4/A-2`

## Step 15: T2 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `COMECON[14], Nasser[15], Warsaw Pact Formed[16], De Gaulle Leads France[17], Containment[25], US/Japan Mutual Defense Pact[27], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Five Year Plan[5], Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], NATO[21], East European Unrest[29], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Nasser[15], Warsaw Pact Formed[16], De Gaulle Leads France[17], Containment[25], US/Japan Mutual Defense Pact[27], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Italy, Philippines, Thailand | 55.23 | 5.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | De Gaulle Leads France INFLUENCE Italy, Philippines, Thailand | 55.23 | 5.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Suez Crisis INFLUENCE Italy, Philippines, Thailand | 55.23 | 5.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE Italy, Saudi Arabia, Philippines, Thailand | 47.38 | 5.00 | 69.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Warsaw Pact Formed COUP Philippines | 44.25 | 4.00 | 40.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Five Year Plan[5], Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Italy, North Korea, Philippines | 58.33 | 5.00 | 56.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, access_touch:North Korea, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 2 | Five Year Plan INFLUENCE Italy, North Korea, Philippines | 58.33 | 5.00 | 56.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, access_touch:North Korea, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 3 | East European Unrest INFLUENCE Italy, North Korea, Philippines | 58.33 | 5.00 | 56.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, access_touch:North Korea, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 4 | NORAD INFLUENCE Italy, North Korea, Philippines | 58.33 | 5.00 | 56.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, access_touch:North Korea, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 5 | Olympic Games INFLUENCE Italy, Philippines | 40.93 | 5.00 | 38.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Nasser[15], De Gaulle Leads France[17], Containment[25], US/Japan Mutual Defense Pact[27], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE North Korea, Saudi Arabia, Thailand | 58.65 | 5.00 | 57.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Suez Crisis INFLUENCE North Korea, Saudi Arabia, Thailand | 58.65 | 5.00 | 57.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | De Gaulle Leads France COUP Indonesia | 54.85 | 4.00 | 51.30 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5 |
| 4 | Suez Crisis COUP Indonesia | 54.85 | 4.00 | 51.30 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE Japan, North Korea, Saudi Arabia, Thailand | 50.65 | 5.00 | 73.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, Iraq | 51.75 | 5.00 | 50.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:3.20 |
| 2 | East European Unrest INFLUENCE East Germany, France, Iraq | 51.75 | 5.00 | 50.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:3.20 |
| 3 | NORAD INFLUENCE East Germany, France, Iraq | 51.75 | 5.00 | 50.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:3.20 |
| 4 | Five Year Plan COUP Philippines | 37.45 | 4.00 | 33.90 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:2.5 |
| 5 | East European Unrest COUP Philippines | 37.45 | 4.00 | 33.90 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Nasser[15], Containment[25], US/Japan Mutual Defense Pact[27], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, Iraq, Thailand | 60.35 | 5.00 | 59.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Suez Crisis COUP Indonesia | 55.15 | 4.00 | 51.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE East Germany, Japan, Iraq, Thailand | 52.35 | 5.00 | 75.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | The Cambridge Five COUP Indonesia | 49.80 | 4.00 | 46.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 5 | Nasser COUP Indonesia | 43.45 | 4.00 | 39.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Saudi Arabia, Panama | 49.20 | 5.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:4.00 |
| 2 | NORAD INFLUENCE Japan, Saudi Arabia, Panama | 49.20 | 5.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:4.00 |
| 3 | East European Unrest COUP Iran | 44.00 | 4.00 | 40.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | NORAD COUP Iran | 44.00 | 4.00 | 40.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games COUP Iran | 38.65 | 4.00 | 34.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Nasser[15], Containment[25], US/Japan Mutual Defense Pact[27], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Indonesia | 50.30 | 4.00 | 46.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Nasser COUP Indonesia | 43.95 | 4.00 | 40.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE UK, Japan, Indonesia, Thailand | 43.17 | 5.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | US/Japan Mutual Defense Pact COUP Indonesia | 37.00 | 4.00 | 57.60 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 5 | The Cambridge Five INFLUENCE Japan, Thailand | 35.97 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 24: T2 AR4 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Egypt, Indonesia | 46.92 | 5.00 | 47.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:5.33 |
| 2 | NORAD COUP Iran | 38.50 | 4.00 | 34.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Olympic Games COUP Iran | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Olympic Games INFLUENCE Japan, Indonesia | 31.37 | 5.00 | 32.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:5.33 |
| 5 | Captured Nazi Scientist COUP Iran | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Containment[25], US/Japan Mutual Defense Pact[27]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE UK, West Germany, Japan, Thailand | 48.30 | 5.00 | 67.90 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:13.65, access_touch:UK, influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Containment INFLUENCE UK, Japan, Thailand | 36.80 | 5.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Nasser COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 5 | US/Japan Mutual Defense Pact COUP Syria | 13.35 | 4.00 | 33.95 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Iran | 34.15 | 4.00 | 30.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Olympic Games INFLUENCE West Germany, Egypt | 30.05 | 5.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:14.00 |
| 3 | Captured Nazi Scientist COUP Iran | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Olympic Games COUP Lebanon | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Olympic Games COUP Iraq | 19.50 | 4.00 | 15.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 27: T2 AR6 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Containment[25]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Iran, Thailand | 39.85 | 5.00 | 55.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Containment SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Nasser REALIGN Cuba | 3.34 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window |
| 5 | Nasser EVENT | 2.35 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `none`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 25.50 | 5.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany |
| 2 | Romanian Abdication INFLUENCE West Germany | 13.50 | 5.00 | 20.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty |
| 3 | Captured Nazi Scientist COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Sudan | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Zimbabwe | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], US/Japan Mutual Defense Pact[27], East European Unrest[29], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Nasser[15], Suez Crisis[28], De-Stalinization[33], Nuclear Test Ban[34], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Korean War EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], US/Japan Mutual Defense Pact[27], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE West Germany, India, Japan, Thailand | 44.20 | 5.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Olympic Games COUP Indonesia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 3 | Olympic Games INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Romanian Abdication COUP Indonesia | 36.45 | 4.00 | 32.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Indonesia | 36.45 | 4.00 | 32.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Nasser[15], Suez Crisis[28], De-Stalinization[33], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, Egypt | 56.05 | 5.00 | 55.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:4.00 |
| 2 | NORAD COUP Indonesia | 49.15 | 4.00 | 45.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 3 | NORAD COUP Iran | 45.00 | 4.00 | 41.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | NORAD COUP Italy | 38.75 | 4.00 | 35.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 5 | NORAD COUP Philippines | 38.75 | 4.00 | 35.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Romanian Abdication[12], Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 43.10 | 4.00 | 39.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:3.5 |
| 2 | Olympic Games INFLUENCE India, Thailand | 40.90 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 3 | Five Year Plan INFLUENCE India, Japan, Thailand | 36.90 | 5.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | East European Unrest INFLUENCE India, Japan, Thailand | 36.90 | 5.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Romanian Abdication COUP Indonesia | 36.75 | 4.00 | 32.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 34: T3 AR2 US

- chosen: `Suez Crisis [28] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Nasser[15], Suez Crisis[28], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Indonesia | 36.45 | 4.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | De-Stalinization COUP Indonesia | 36.45 | 4.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Korean War COUP Indonesia | 34.10 | 4.00 | 46.40 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Indonesia | 34.10 | 4.00 | 46.40 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP Indonesia | 31.75 | 4.00 | 39.90 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 35: T3 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE India, Japan, Thailand | 39.70 | 5.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | East European Unrest INFLUENCE India, Japan, Thailand | 39.70 | 5.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Special Relationship INFLUENCE India, Thailand | 27.70 | 5.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Romanian Abdication INFLUENCE India | 23.40 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, control_break:India, non_coup_milops_penalty:2.00 |
| 5 | Captured Nazi Scientist INFLUENCE India | 23.40 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, control_break:India, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Nasser[15], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, Iran, Indonesia | 32.25 | 5.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty |
| 2 | Korean War INFLUENCE Japan, Indonesia | 20.70 | 5.00 | 32.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty |
| 3 | Arab-Israeli War INFLUENCE Japan, Indonesia | 20.70 | 5.00 | 32.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty |
| 4 | Blockade INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 5 | Nasser INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Iran, Thailand | 37.18 | 5.00 | 55.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Special Relationship INFLUENCE Iran, Thailand | 25.18 | 5.00 | 39.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Romanian Abdication COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 5 | Romanian Abdication INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Pakistan | 21.80 | 5.00 | 33.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty |
| 2 | Arab-Israeli War INFLUENCE Japan, Pakistan | 21.80 | 5.00 | 33.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty |
| 3 | Blockade INFLUENCE Pakistan | 9.80 | 5.00 | 16.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty |
| 4 | Nasser INFLUENCE Pakistan | 9.80 | 5.00 | 16.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty |
| 5 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | Special Relationship INFLUENCE Pakistan, Thailand | 22.10 | 5.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Romanian Abdication COUP Iran | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Iran | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE India, Japan | 22.40 | 5.00 | 33.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, offside_ops_penalty |
| 2 | Blockade INFLUENCE India | 10.40 | 5.00 | 17.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, offside_ops_penalty |
| 3 | Nasser INFLUENCE India | 10.40 | 5.00 | 17.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, offside_ops_penalty |
| 4 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Syria | 25.30 | 4.00 | 21.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Iran | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Special Relationship INFLUENCE India, Thailand | 18.70 | 5.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 4 | Captured Nazi Scientist COUP Iraq | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |
| 5 | Captured Nazi Scientist COUP Saudi Arabia | 18.65 | 4.00 | 14.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Nasser INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Blockade COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Blockade COUP SE African States | -4.55 | 4.00 | 3.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-2/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Containment[25], Red Scare/Purge[31], Formosan Resolution[35], Special Relationship[37], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Alliance for Progress EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Formosan Resolution EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Fidel[8], Vietnam Revolts[9], Independent Reds[22], East European Unrest[29], The Cambridge Five[36], Arms Race[42], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Containment[25], Formosan Resolution[35], Special Relationship[37], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Indonesia | 34.91 | 4.00 | 31.06 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:2.5 |
| 2 | Containment INFLUENCE India, Pakistan, Mexico | 33.93 | 5.00 | 53.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:13.80, control_break:India, influence:Pakistan:13.20, control_break:Pakistan, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 3 | Alliance for Progress INFLUENCE India, Pakistan, Mexico | 33.93 | 5.00 | 53.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:13.80, control_break:India, influence:Pakistan:13.20, control_break:Pakistan, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 4 | Containment COUP Indonesia | 27.61 | 4.00 | 44.06 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Indonesia | 27.61 | 4.00 | 44.06 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 46: T4 AR1 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Fidel[8], Vietnam Revolts[9], Independent Reds[22], The Cambridge Five[36], Arms Race[42], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE Mexico, Morocco | 33.73 | 5.00 | 33.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 2 | Ussuri River Skirmish INFLUENCE Mexico, Morocco | 33.73 | 5.00 | 33.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 3 | Arms Race COUP Iran | 31.71 | 4.00 | 28.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Iran | 31.71 | 4.00 | 28.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, expected_swing:2.5 |
| 5 | Arms Race COUP Colombia | 25.61 | 4.00 | 22.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.57, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Containment[25], Formosan Resolution[35], Special Relationship[37], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE India, Pakistan, Mexico | 34.50 | 5.00 | 53.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:13.80, control_break:India, influence:Pakistan:13.20, control_break:Pakistan, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Alliance for Progress INFLUENCE India, Pakistan, Mexico | 34.50 | 5.00 | 53.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:13.80, control_break:India, influence:Pakistan:13.20, control_break:Pakistan, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Formosan Resolution INFLUENCE India, Pakistan | 21.70 | 5.00 | 37.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:13.80, control_break:India, influence:Pakistan:13.20, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Special Relationship INFLUENCE India, Pakistan | 21.70 | 5.00 | 37.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:13.80, control_break:India, influence:Pakistan:13.20, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Camp David Accords INFLUENCE India, Pakistan | 21.70 | 5.00 | 37.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:13.80, control_break:India, influence:Pakistan:13.20, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Ussuri River Skirmish [77] as COUP`
- flags: `milops_shortfall:4`
- hand: `Socialist Governments[7], Fidel[8], Vietnam Revolts[9], Independent Reds[22], The Cambridge Five[36], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish COUP Mexico | 33.75 | 4.00 | 30.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5 |
| 2 | Ussuri River Skirmish INFLUENCE Algeria, South Africa | 32.22 | 5.00 | 33.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 3 | Ussuri River Skirmish COUP Iran | 32.00 | 4.00 | 28.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5 |
| 4 | Independent Reds COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | Ussuri River Skirmish COUP Colombia | 25.90 | 4.00 | 22.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.67, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 49: T4 AR3 USSR

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Formosan Resolution[35], Special Relationship[37], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE Mexico, Algeria, Morocco | 29.70 | 5.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Formosan Resolution INFLUENCE Mexico, Morocco | 17.65 | 5.00 | 33.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Special Relationship INFLUENCE Mexico, Morocco | 17.65 | 5.00 | 33.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Camp David Accords INFLUENCE Mexico, Morocco | 17.65 | 5.00 | 33.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Our Man in Tehran INFLUENCE Mexico, Morocco | 17.65 | 5.00 | 33.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Fidel[8], Vietnam Revolts[9], Independent Reds[22], The Cambridge Five[36], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Mexico | 23.05 | 5.00 | 19.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:1.60 |
| 2 | Socialist Governments INFLUENCE Mexico, South Africa | 19.70 | 5.00 | 36.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | Independent Reds COUP Colombia | 17.15 | 4.00 | 13.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:3.5 |
| 4 | Independent Reds COUP Saharan States | 17.15 | 4.00 | 13.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:3.5 |
| 5 | Independent Reds COUP SE African States | 17.15 | 4.00 | 13.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Formosan Resolution[35], Special Relationship[37], Camp David Accords[66], OAS Founded[71], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Algeria | 18.05 | 5.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Special Relationship INFLUENCE West Germany, Algeria | 18.05 | 5.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Camp David Accords INFLUENCE West Germany, Algeria | 18.05 | 5.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Our Man in Tehran INFLUENCE West Germany, Algeria | 18.05 | 5.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | OAS Founded INFLUENCE Algeria | 6.05 | 5.00 | 19.20 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Vietnam Revolts[9], The Cambridge Five[36], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, South Africa | 20.50 | 5.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Lone Gunman INFLUENCE West Germany | 12.00 | 5.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Fidel INFLUENCE West Germany | 7.85 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Vietnam Revolts INFLUENCE West Germany | 7.85 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | The Cambridge Five INFLUENCE West Germany | 7.85 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Special Relationship[37], Camp David Accords[66], OAS Founded[71], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 12.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Camp David Accords INFLUENCE East Germany, West Germany | 12.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 12.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Special Relationship COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Camp David Accords COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], The Cambridge Five[36], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE South Africa | 11.98 | 5.00 | 21.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Fidel INFLUENCE South Africa | 7.83 | 5.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Vietnam Revolts INFLUENCE South Africa | 7.83 | 5.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | The Cambridge Five INFLUENCE South Africa | 7.83 | 5.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Fidel SPACE | 5.03 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Camp David Accords[66], OAS Founded[71], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Saharan States | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Camp David Accords COUP Guatemala | 4.80 | 4.00 | 17.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Guatemala | 4.80 | 4.00 | 17.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | OAS Founded COUP Saharan States | 3.70 | 4.00 | 11.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 56: T4 AR6 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], The Cambridge Five[36]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 24.05 | 4.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Saharan States | 24.05 | 4.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Saharan States | 24.05 | 4.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Fidel INFLUENCE West Germany | 2.85 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | Vietnam Revolts INFLUENCE West Germany | 2.85 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `OAS Founded[71], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | OAS Founded COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | OAS Founded COUP Guatemala | 3.95 | 4.00 | 12.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Our Man in Tehran INFLUENCE East Germany, West Germany | -1.60 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], The Cambridge Five[36]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Colombia | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Saharan States | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP SE African States | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Sudan | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Zimbabwe | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 59: T5 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], SALT Negotiations[46], Muslim Revolution[59], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Shuttle Diplomacy[74]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], NORAD[38], Bear Trap[47], Junta[50], ABM Treaty[60], Lonely Hearts Club Band[65], Latin American Death Squads[70], Voice of America[75]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], SALT Negotiations[46], Muslim Revolution[59], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Shuttle Diplomacy[74]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Cuba | 61.49 | 5.00 | 62.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.71 |
| 2 | Muslim Revolution COUP Saharan States | 54.39 | 4.00 | 50.99 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:5.5 |
| 3 | De Gaulle Leads France COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 4 | SALT Negotiations COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 5 | Muslim Revolution COUP Mexico | 46.24 | 4.00 | 42.84 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `NORAD [38] as COUP`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], NORAD[38], Bear Trap[47], Junta[50], Lonely Hearts Club Band[65], Latin American Death Squads[70], Voice of America[75]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Indonesia | 55.04 | 4.00 | 51.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 2 | Bear Trap COUP Indonesia | 55.04 | 4.00 | 51.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 3 | NORAD INFLUENCE Brazil, Nigeria, South Africa | 52.44 | 5.00 | 53.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 4 | Bear Trap INFLUENCE Brazil, Nigeria, South Africa | 52.44 | 5.00 | 53.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 5 | Olympic Games COUP Indonesia | 48.69 | 4.00 | 44.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 63: T5 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], SALT Negotiations[46], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Shuttle Diplomacy[74]`
- state: `VP 0, DEFCON 4, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 50.13 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 2 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 50.13 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 3 | De Gaulle Leads France COUP Saharan States | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 4 | SALT Negotiations COUP Saharan States | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Libya | 41.18 | 5.00 | 67.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Libya:13.20, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Bear Trap[47], Junta[50], Lonely Hearts Club Band[65], Latin American Death Squads[70], Voice of America[75]`
- state: `VP 0, DEFCON 4, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE Brazil, Nigeria, South Africa | 55.48 | 5.00 | 53.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:2.67 |
| 2 | Bear Trap COUP Indonesia | 52.90 | 4.00 | 49.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:4.5 |
| 3 | Olympic Games COUP Indonesia | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 4 | Junta COUP Indonesia | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 5 | Lonely Hearts Club Band COUP Indonesia | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `SALT Negotiations [46] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Truman Doctrine[19], US/Japan Mutual Defense Pact[27], SALT Negotiations[46], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Shuttle Diplomacy[74]`
- state: `VP 0, DEFCON 4, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations COUP Saharan States | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 43.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | SALT Negotiations COUP Mexico | 40.75 | 4.00 | 37.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, expected_swing:2.5 |
| 4 | SALT Negotiations COUP Pakistan | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:5, milops_urgency:1.00, expected_swing:2.5 |
| 5 | SALT Negotiations COUP Iran | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:5, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 66: T5 AR3 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Junta[50], Lonely Hearts Club Band[65], Latin American Death Squads[70], Voice of America[75]`
- state: `VP 0, DEFCON 4, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 47.75 | 4.00 | 44.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Indonesia | 47.75 | 4.00 | 44.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 3 | Lonely Hearts Club Band COUP Indonesia | 47.75 | 4.00 | 44.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Indonesia | 47.75 | 4.00 | 44.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 5 | Voice of America COUP Indonesia | 47.75 | 4.00 | 44.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], US/Japan Mutual Defense Pact[27], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Shuttle Diplomacy[74]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Nigeria | 39.25 | 5.00 | 62.85 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | US/Japan Mutual Defense Pact COUP Nigeria | 30.25 | 4.00 | 50.85 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 3 | Sadat Expels Soviets COUP Nigeria | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Shuttle Diplomacy COUP Nigeria | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Nigeria | 27.85 | 5.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Junta[50], Lonely Hearts Club Band[65], Latin American Death Squads[70], Voice of America[75]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | Lonely Hearts Club Band COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Voice of America COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 5 | Junta INFLUENCE Brazil, Nigeria | 38.50 | 5.00 | 37.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Nigeria:13.60, control_break:Nigeria, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Shuttle Diplomacy[74]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Nigeria | 29.52 | 5.00 | 50.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Nigeria | 29.52 | 5.00 | 50.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Sadat Expels Soviets COUP Nigeria | 22.40 | 4.00 | 38.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:4.5, offside_ops_penalty |
| 4 | Shuttle Diplomacy COUP Nigeria | 22.40 | 4.00 | 38.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:4.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Nigeria | 21.05 | 4.00 | 33.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Lonely Hearts Club Band[65], Latin American Death Squads[70], Voice of America[75]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 3 | Voice of America COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 4 | Lonely Hearts Club Band COUP Nigeria | 37.05 | 4.00 | 33.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Nigeria | 37.05 | 4.00 | 33.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Shuttle Diplomacy [74] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68], Shuttle Diplomacy[74]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy COUP Saharan States | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Grain Sales to Soviets COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Saharan States | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Shuttle Diplomacy COUP Nigeria | 23.40 | 4.00 | 39.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:4.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Nigeria | 22.05 | 4.00 | 34.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Latin American Death Squads[70], Voice of America[75]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Voice of America COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Nigeria | 38.05 | 4.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:3.5 |
| 4 | Voice of America COUP Nigeria | 38.05 | 4.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, expected_swing:3.5 |
| 5 | Captured Nazi Scientist COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Nigeria | 25.05 | 4.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:3.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Nigeria | 22.70 | 4.00 | 30.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Syria | 18.15 | 4.00 | 30.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Syria | 15.80 | 4.00 | 23.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Mexico | 15.40 | 4.00 | 27.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Voice of America [75] as COUP`
- flags: `milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Voice of America[75]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 3 | Voice of America COUP Colombia | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Voice of America COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Voice of America COUP Sudan | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 75: T6 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Olympic Games[20], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], De-Stalinization[33], Special Relationship[37], We Will Bury You[53], OPEC[64], Liberation Theology[76]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], Suez Crisis[28], NORAD[38], Kitchen Debates[51], Missile Envy[52], South African Unrest[56], Ask Not What Your Country Can Do For You[78], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Olympic Games[20], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], De-Stalinization[33], Special Relationship[37], OPEC[64], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | OPEC COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 3 | De-Stalinization INFLUENCE East Germany, France, West Germany | 44.94 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 4 | OPEC INFLUENCE East Germany, France, West Germany | 44.94 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 5 | Olympic Games COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 78: T6 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], Suez Crisis[28], Kitchen Debates[51], Missile Envy[52], South African Unrest[56], Ask Not What Your Country Can Do For You[78], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Brazil, South Africa | 51.89 | 5.00 | 54.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | Missile Envy INFLUENCE Argentina, Brazil | 35.24 | 5.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.86 |
| 3 | Suez Crisis INFLUENCE Argentina, Brazil, South Africa | 31.89 | 5.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 4 | Ask Not What Your Country Can Do For You COUP Colombia | 26.47 | 4.00 | 22.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:0.86, empty_coup_penalty, expected_swing:4.5 |
| 5 | Ask Not What Your Country Can Do For You COUP Saharan States | 26.47 | 4.00 | 22.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Olympic Games[20], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Special Relationship[37], OPEC[64], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, West Germany, Pakistan | 50.45 | 5.00 | 49.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:4.00 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Pakistan | 41.85 | 5.00 | 65.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Olympic Games INFLUENCE West Germany, Pakistan | 35.05 | 5.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:4.00 |
| 4 | Indo-Pakistani War INFLUENCE West Germany, Pakistan | 35.05 | 5.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:4.00 |
| 5 | Liberation Theology INFLUENCE West Germany, Pakistan | 35.05 | 5.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], Suez Crisis[28], Kitchen Debates[51], Missile Envy[52], South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE Argentina, Chile | 36.70 | 5.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:8.00 |
| 2 | Suez Crisis INFLUENCE Argentina, Chile, South Africa | 33.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Korean War INFLUENCE Argentina, Chile | 20.70 | 5.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | South African Unrest INFLUENCE Argentina, Chile | 20.70 | 5.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Missile Envy COUP Colombia | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Olympic Games[20], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Special Relationship[37], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Pakistan | 41.05 | 5.00 | 65.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Olympic Games INFLUENCE West Germany, Pakistan | 34.25 | 5.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:4.80 |
| 3 | Indo-Pakistani War INFLUENCE West Germany, Pakistan | 34.25 | 5.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:4.80 |
| 4 | Liberation Theology INFLUENCE West Germany, Pakistan | 34.25 | 5.00 | 34.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, non_coup_milops_penalty:4.80 |
| 5 | Olympic Games COUP Cameroon | 19.35 | 4.00 | 15.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], Suez Crisis[28], Kitchen Debates[51], South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Argentina, Chile, South Africa | 24.75 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Kitchen Debates COUP Colombia | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Saharan States | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |
| 4 | Kitchen Debates COUP SE African States | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Sudan | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Olympic Games[20], Indo-Pakistani War[24], Special Relationship[37], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 35.40 | 5.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.00 |
| 2 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 35.40 | 5.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.00 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 35.40 | 5.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.00 |
| 4 | Nasser INFLUENCE West Germany | 20.00 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:6.00 |
| 5 | Olympic Games COUP Cameroon | 19.80 | 4.00 | 16.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], Kitchen Debates[51], South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Colombia | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Kitchen Debates COUP Saharan States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Kitchen Debates COUP SE African States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Sudan | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Zimbabwe | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 85: T6 AR5 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Indo-Pakistani War[24], Special Relationship[37], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 28.40 | 5.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Indo-Pakistani War COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Indo-Pakistani War COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Liberation Theology COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], South African Unrest[56], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP SE African States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Sudan | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Zimbabwe | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Liberation Theology [76] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Special Relationship[37], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Cameroon | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Liberation Theology COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Liberation Theology COUP Guatemala | 20.80 | 4.00 | 17.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Liberation Theology COUP Haiti | 20.80 | 4.00 | 17.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Nasser COUP Cameroon | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Korean War[11], South African Unrest[56]`
- state: `VP 3, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Colombia | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Korean War COUP Saharan States | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Korean War COUP SE African States | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Korean War COUP Sudan | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Korean War COUP Zimbabwe | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 89: T6 AR7 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Special Relationship[37]`
- state: `VP 3, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Cameroon | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Nasser COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Nasser COUP Guatemala | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Nasser COUP Haiti | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Special Relationship COUP Cameroon | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `South African Unrest [56] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `South African Unrest[56]`
- state: `VP 3, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Colombia | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | South African Unrest COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | South African Unrest COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Zimbabwe | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Suez Crisis[28], UN Intervention[32], Nuclear Test Ban[34], Nuclear Subs[44], Willy Brandt[58], Puppet Governments[67], One Small Step[81]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Duck and Cover[4], Warsaw Pact Formed[16], CIA Created[26], De-Stalinization[33], Brush War[39], Quagmire[45], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Suez Crisis[28], UN Intervention[32], Nuclear Subs[44], Willy Brandt[58], Puppet Governments[67], One Small Step[81]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, Congo/Zaire | 44.45 | 5.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 2 | Suez Crisis COUP Mexico | 40.75 | 4.00 | 37.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |
| 3 | Suez Crisis COUP Pakistan | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |
| 4 | Suez Crisis COUP Iran | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |
| 5 | Suez Crisis COUP Philippines | 38.50 | 4.00 | 34.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `milops_shortfall:7`
- hand: `Warsaw Pact Formed[16], CIA Created[26], De-Stalinization[33], Brush War[39], Quagmire[45], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | CIA Created COUP Indonesia | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | How I Learned to Stop Worrying COUP Algeria | 40.65 | 4.00 | 36.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 4 | Warsaw Pact Formed COUP Indonesia | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Indonesia | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 95: T7 AR2 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], UN Intervention[32], Nuclear Subs[44], Willy Brandt[58], Puppet Governments[67], One Small Step[81]`
- state: `VP 4, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE Angola, Congo/Zaire | 37.17 | 5.00 | 41.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:9.33 |
| 2 | One Small Step INFLUENCE Angola, Congo/Zaire | 37.17 | 5.00 | 41.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:9.33 |
| 3 | Willy Brandt COUP Syria | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:1.5 |
| 4 | One Small Step COUP Syria | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:1.5 |
| 5 | Willy Brandt COUP Mexico | 28.90 | 4.00 | 25.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:5`
- hand: `Warsaw Pact Formed[16], CIA Created[26], De-Stalinization[33], Brush War[39], Quagmire[45], Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 4, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Algeria | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Warsaw Pact Formed INFLUENCE Argentina, Chile, South Africa | 27.68 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 3 | De-Stalinization INFLUENCE Argentina, Chile, South Africa | 27.68 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 4 | Brush War INFLUENCE Argentina, Chile, South Africa | 27.68 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Quagmire INFLUENCE Argentina, Chile, South Africa | 27.68 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], UN Intervention[32], Nuclear Subs[44], Puppet Governments[67], One Small Step[81]`
- state: `VP 4, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE West Germany, Angola | 25.25 | 5.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:11.20 |
| 2 | One Small Step COUP Cameroon | 21.75 | 4.00 | 18.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP Saharan States | 21.75 | 4.00 | 18.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP SE African States | 21.75 | 4.00 | 18.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Guatemala | 20.50 | 4.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Warsaw Pact Formed[16], De-Stalinization[33], Brush War[39], Quagmire[45], Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 4, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Argentina, Chile, South Africa | 26.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | De-Stalinization INFLUENCE Argentina, Chile, South Africa | 26.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Brush War INFLUENCE Argentina, Chile, South Africa | 26.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Quagmire INFLUENCE Argentina, Chile, South Africa | 26.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Brezhnev Doctrine INFLUENCE Argentina, Chile, South Africa | 26.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], UN Intervention[32], Nuclear Subs[44], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Cameroon | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 2 | Romanian Abdication COUP Saharan States | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP SE African States | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Cameroon | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Saharan States | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 100: T7 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `De-Stalinization[33], Brush War[39], Quagmire[45], Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 4, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Argentina, Chile, South Africa | 24.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Brush War INFLUENCE Argentina, Chile, South Africa | 24.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Quagmire INFLUENCE Argentina, Chile, South Africa | 24.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Brezhnev Doctrine INFLUENCE Argentina, Chile, South Africa | 24.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Cultural Revolution INFLUENCE Argentina, Chile, South Africa | 24.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], Nuclear Subs[44], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Brush War[39], Quagmire[45], Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 4, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE Japan, Chile, South Africa | 24.22 | 5.00 | 53.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Quagmire INFLUENCE Japan, Chile, South Africa | 24.22 | 5.00 | 53.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Brezhnev Doctrine INFLUENCE Japan, Chile, South Africa | 24.22 | 5.00 | 53.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Cultural Revolution INFLUENCE Japan, Chile, South Africa | 24.22 | 5.00 | 53.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:14.40, control_break:Japan, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Brush War COUP Colombia | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], Nuclear Subs[44], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Cameroon | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Guatemala | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Haiti | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Quagmire [45] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Quagmire[45], Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 4, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Colombia | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Quagmire COUP Saharan States | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP SE African States | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP Sudan | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Zimbabwe | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 105: T7 AR7 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Nuclear Subs[44], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Cameroon | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Nuclear Subs COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Cameroon | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 106: T7 AR7 US

- chosen: `Brezhnev Doctrine [54] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Brezhnev Doctrine[54], Cultural Revolution[61]`
- state: `VP 4, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine COUP Colombia | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Brezhnev Doctrine COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Brezhnev Doctrine COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Brezhnev Doctrine COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Brezhnev Doctrine COUP Zimbabwe | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 107: T8 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Special Relationship[37], Cuban Missile Crisis[43], Muslim Revolution[59], OPEC[64], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Containment[25], NORAD[38], Arms Race[42], Kitchen Debates[51], U2 Incident[63], North Sea Oil[89], Solidarity[104], Lone Gunman[109]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Solidarity EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Special Relationship[37], Cuban Missile Crisis[43], OPEC[64], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Pakistan | 46.56 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:9.14 |
| 2 | OPEC INFLUENCE East Germany, West Germany, Pakistan | 46.56 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:9.14 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Pakistan | 46.56 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Pakistan:12.95, control_break:Pakistan, non_coup_milops_penalty:9.14 |
| 4 | Cuban Missile Crisis COUP Mexico | 33.68 | 4.00 | 30.13 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |
| 5 | OPEC COUP Mexico | 33.68 | 4.00 | 30.13 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], NORAD[38], Arms Race[42], Kitchen Debates[51], U2 Incident[63], North Sea Oil[89], Solidarity[104], Lone Gunman[109]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany, Algeria | 61.11 | 5.00 | 65.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:9.14 |
| 2 | Arms Race INFLUENCE East Germany, France, West Germany, Algeria | 61.11 | 5.00 | 65.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:9.14 |
| 3 | North Sea Oil INFLUENCE East Germany, France, West Germany, Algeria | 61.11 | 5.00 | 65.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:9.14 |
| 4 | Solidarity INFLUENCE East Germany, France, West Germany | 45.06 | 5.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | NORAD COUP Algeria | 41.43 | 4.00 | 37.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Special Relationship[37], OPEC[64], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, West Germany, Algeria | 46.28 | 5.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:10.67 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Algeria | 46.28 | 5.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:10.67 |
| 3 | OPEC COUP Algeria | 35.00 | 4.00 | 31.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Algeria | 35.00 | 4.00 | 31.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |
| 5 | OPEC COUP Mexico | 34.25 | 4.00 | 30.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Arms Race[42], Kitchen Debates[51], U2 Incident[63], North Sea Oil[89], Solidarity[104], Lone Gunman[109]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany, Cuba | 59.43 | 5.00 | 65.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.67 |
| 2 | North Sea Oil INFLUENCE East Germany, France, West Germany, Cuba | 59.43 | 5.00 | 65.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.67 |
| 3 | Solidarity INFLUENCE East Germany, France, West Germany | 43.53 | 5.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | Arms Race COUP Iran | 40.75 | 4.00 | 37.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | North Sea Oil COUP Iran | 40.75 | 4.00 | 37.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Special Relationship[37], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 41.25 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Ussuri River Skirmish COUP Algeria | 35.80 | 4.00 | 32.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:2.5 |
| 3 | Ussuri River Skirmish COUP Mexico | 35.05 | 4.00 | 31.50 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Angola | 31.20 | 4.00 | 27.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, empty_coup_penalty, expected_swing:4.5 |
| 5 | Ussuri River Skirmish COUP Nigeria | 31.20 | 4.00 | 27.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Kitchen Debates[51], U2 Incident[63], North Sea Oil[89], Solidarity[104], Lone Gunman[109]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany, Venezuela | 56.95 | 5.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, non_coup_milops_penalty:12.80 |
| 2 | North Sea Oil COUP Iran | 41.55 | 4.00 | 38.00 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Solidarity INFLUENCE East Germany, France, West Germany | 41.40 | 5.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 4 | U2 Incident INFLUENCE East Germany, France, West Germany, Venezuela | 36.95 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | North Sea Oil COUP Algeria | 35.80 | 4.00 | 32.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], Special Relationship[37], Ask Not What Your Country Can Do For You[78], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Algeria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | Blockade COUP Mexico | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Blockade COUP Morocco | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3 |
| 4 | Blockade COUP Cuba | 21.40 | 4.00 | 17.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3 |
| 5 | Blockade COUP Iraq | 20.90 | 4.00 | 17.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 116: T8 AR4 US

- chosen: `Solidarity [104] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Kitchen Debates[51], U2 Incident[63], Solidarity[104], Lone Gunman[109]`
- state: `VP 4, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity INFLUENCE East Germany, West Germany, Venezuela | 40.60 | 5.00 | 51.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, control_break:Venezuela, non_coup_milops_penalty:16.00 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany, Venezuela | 36.75 | 5.00 | 68.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Kitchen Debates INFLUENCE West Germany, Venezuela | 24.45 | 5.00 | 35.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, influence:Venezuela:13.70, control_break:Venezuela, non_coup_milops_penalty:16.00 |
| 4 | Solidarity COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Solidarity COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Special Relationship[37], Ask Not What Your Country Can Do For You[78], Defectors[108]`
- state: `VP 4, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 15.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Ask Not What Your Country Can Do For You COUP Cameroon | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Saharan States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP SE African States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP Guatemala | 10.15 | 4.00 | 26.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], Kitchen Debates[51], U2 Incident[63], Lone Gunman[109]`
- state: `VP 4, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, Italy, West Germany | 28.42 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | Kitchen Debates COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Kitchen Debates COUP SE African States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Zimbabwe | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Special Relationship[37], Defectors[108]`
- state: `VP 4, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Cameroon | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Special Relationship COUP Saharan States | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Special Relationship COUP SE African States | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Defectors COUP Cameroon | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Defectors COUP Saharan States | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 120: T8 AR6 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Kitchen Debates[51], Lone Gunman[109]`
- state: `VP 4, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Kitchen Debates COUP SE African States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Sudan | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Zimbabwe | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Colombia | 22.70 | 4.00 | 18.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 121: T8 AR7 USSR

- chosen: `Defectors [108] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Defectors[108]`
- state: `VP 4, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Defectors COUP Cameroon | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Defectors COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Defectors COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Defectors COUP Guatemala | 18.80 | 4.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Defectors COUP Haiti | 18.80 | 4.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Lone Gunman[109]`
- state: `VP 4, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Saharan States | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Nasser COUP SE African States | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Nasser COUP Sudan | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP Zimbabwe | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Lone Gunman COUP Saharan States | 20.20 | 4.00 | 28.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 123: T9 AR0 USSR

- chosen: `Brezhnev Doctrine [54] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Five Year Plan[5], Truman Doctrine[19], Nuclear Subs[44], Brezhnev Doctrine[54], Portuguese Empire Crumbles[55], Sadat Expels Soviets[73], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Sadat Expels Soviets EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Tear Down this Wall EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Romanian Abdication[12], US/Japan Mutual Defense Pact[27], UN Intervention[32], Formosan Resolution[35], Allende[57], ABM Treaty[60], Grain Sales to Soviets[68], An Evil Empire[100], Wargames[103]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | An Evil Empire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Five Year Plan[5], Truman Doctrine[19], Nuclear Subs[44], Portuguese Empire Crumbles[55], Sadat Expels Soviets[73], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, France, West Germany | 43.91 | 5.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | Portuguese Empire Crumbles COUP Saharan States | 43.41 | 4.00 | 39.71 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 3 | Five Year Plan INFLUENCE East Germany, France, Italy, West Germany | 39.46 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, France, Italy, West Germany | 39.46 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | Tear Down this Wall INFLUENCE East Germany, France, Italy, West Germany | 39.46 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Romanian Abdication[12], UN Intervention[32], Formosan Resolution[35], Allende[57], ABM Treaty[60], Grain Sales to Soviets[68], An Evil Empire[100], Wargames[103]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, Italy, West Germany | 59.31 | 5.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | Wargames INFLUENCE East Germany, France, Italy, West Germany | 59.31 | 5.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | ABM Treaty COUP Nigeria | 58.61 | 4.00 | 55.21 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:5.5 |
| 4 | Wargames COUP Nigeria | 58.61 | 4.00 | 55.21 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:5.5 |
| 5 | An Evil Empire COUP Nigeria | 52.26 | 4.00 | 48.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], Nuclear Subs[44], Sadat Expels Soviets[73], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, Italy, West Germany | 37.75 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, Italy, West Germany | 37.75 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Tear Down this Wall INFLUENCE East Germany, France, Italy, West Germany | 37.75 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Five Year Plan COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Sadat Expels Soviets COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Wargames [103] as COUP`
- flags: `milops_shortfall:9`
- hand: `Romanian Abdication[12], UN Intervention[32], Formosan Resolution[35], Allende[57], Grain Sales to Soviets[68], An Evil Empire[100], Wargames[103]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames COUP Nigeria | 59.25 | 4.00 | 55.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:5.5 |
| 2 | Wargames INFLUENCE East Germany, France, Italy, West Germany | 57.60 | 5.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | An Evil Empire COUP Nigeria | 52.90 | 4.00 | 49.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 4 | Wargames COUP Iran | 47.60 | 4.00 | 44.20 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:9, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 5 | Formosan Resolution COUP Nigeria | 46.55 | 4.00 | 42.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+4`

## Step 129: T9 AR3 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Truman Doctrine[19], Nuclear Subs[44], Sadat Expels Soviets[73], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U0/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, Italy, West Germany | 35.35 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 2 | Tear Down this Wall INFLUENCE East Germany, France, Italy, West Germany | 35.35 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | Sadat Expels Soviets COUP Saharan States | 31.30 | 4.00 | 47.75 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Tear Down this Wall COUP Saharan States | 31.30 | 4.00 | 47.75 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Nuclear Subs COUP Saharan States | 28.95 | 4.00 | 41.25 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.80, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `An Evil Empire [100] as COUP`
- flags: `milops_shortfall:5`
- hand: `Romanian Abdication[12], UN Intervention[32], Formosan Resolution[35], Allende[57], Grain Sales to Soviets[68], An Evil Empire[100]`
- state: `VP 5, DEFCON 2, MilOps U0/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | An Evil Empire COUP Cameroon | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | An Evil Empire INFLUENCE East Germany, France, West Germany | 46.05 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Formosan Resolution COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | UN Intervention COUP Cameroon | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Tear Down this Wall [99] as COUP`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Truman Doctrine[19], Nuclear Subs[44], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U0/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall COUP Saharan States | 32.65 | 4.00 | 49.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Tear Down this Wall INFLUENCE East Germany, France, Italy, West Germany | 31.75 | 5.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Nuclear Subs COUP Saharan States | 30.30 | 4.00 | 42.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 27.95 | 4.00 | 36.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Panama Canal Returned COUP Saharan States | 27.95 | 4.00 | 36.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:2.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 132: T9 AR4 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:5`
- hand: `Romanian Abdication[12], UN Intervention[32], Formosan Resolution[35], Allende[57], Grain Sales to Soviets[68]`
- state: `VP 5, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Cameroon | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | Formosan Resolution COUP Saharan States | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 3 | Grain Sales to Soviets COUP Cameroon | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Saharan States | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 5 | UN Intervention COUP Cameroon | 36.95 | 4.00 | 33.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Nuclear Subs[44], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany, India | 24.45 | 5.00 | 51.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:India:13.55, control_break:India, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Truman Doctrine INFLUENCE West Germany, India | 12.30 | 5.00 | 35.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, influence:India:13.55, control_break:India, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Panama Canal Returned INFLUENCE West Germany, India | 12.30 | 5.00 | 35.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, influence:India:13.55, control_break:India, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Nuclear Subs COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nuclear Subs COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:5`
- hand: `Romanian Abdication[12], UN Intervention[32], Allende[57], Grain Sales to Soviets[68]`
- state: `VP 5, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Cameroon | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Saharan States | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 3 | UN Intervention COUP Cameroon | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 4 | UN Intervention COUP Saharan States | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 5 | Romanian Abdication COUP Cameroon | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Cameroon | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Saharan States | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP SE African States | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Cameroon | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Panama Canal Returned COUP Saharan States | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:5`
- hand: `Romanian Abdication[12], UN Intervention[32], Allende[57]`
- state: `VP 5, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Cameroon | 40.70 | 4.00 | 36.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 40.70 | 4.00 | 36.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5 |
| 3 | Romanian Abdication COUP Cameroon | 28.70 | 4.00 | 36.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Saharan States | 28.70 | 4.00 | 36.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Allende COUP Cameroon | 28.70 | 4.00 | 36.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Panama Canal Returned[111]`
- state: `VP 5, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Cameroon | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Panama Canal Returned COUP Saharan States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP SE African States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Guatemala | 16.45 | 4.00 | 24.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Panama Canal Returned COUP Haiti | 16.45 | 4.00 | 24.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Romanian Abdication[12], Allende[57]`
- state: `VP 5, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Cameroon | 36.20 | 4.00 | 44.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Saharan States | 36.20 | 4.00 | 44.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Allende COUP Cameroon | 36.20 | 4.00 | 44.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Saharan States | 36.20 | 4.00 | 44.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP SE African States | 14.20 | 4.00 | 22.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-4`

## Step 139: T10 AR0 USSR

- chosen: `Glasnost [93] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Indo-Pakistani War[24], Brush War[39], Junta[50], Kitchen Debates[51], Missile Envy[52], Puppet Governments[67], Shuttle Diplomacy[74], Our Man in Tehran[84], Glasnost[93]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], CIA Created[26], Formosan Resolution[35], The Cambridge Five[36], Quagmire[45], SALT Negotiations[46], Missile Envy[52], Latin American Death Squads[70], One Small Step[81]`
- state: `VP 5, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +2, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brush War [39] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Indo-Pakistani War[24], Brush War[39], Junta[50], Kitchen Debates[51], Missile Envy[52], Puppet Governments[67], Shuttle Diplomacy[74], Our Man in Tehran[84]`
- state: `VP 7, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Nigeria | 58.69 | 4.00 | 55.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Indo-Pakistani War COUP Nigeria | 52.34 | 4.00 | 48.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 3 | Junta COUP Nigeria | 52.34 | 4.00 | 48.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Missile Envy COUP Nigeria | 52.34 | 4.00 | 48.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Brush War INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], CIA Created[26], Formosan Resolution[35], The Cambridge Five[36], Quagmire[45], Kitchen Debates[51], Missile Envy[52], Latin American Death Squads[70], One Small Step[81]`
- state: `VP 7, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 2 | Formosan Resolution COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 3 | Missile Envy COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | One Small Step COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 143: T10 AR2 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Indo-Pakistani War[24], Junta[50], Kitchen Debates[51], Missile Envy[52], Puppet Governments[67], Shuttle Diplomacy[74], Our Man in Tehran[84]`
- state: `VP 7, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, Indonesia | 30.62 | 5.00 | 35.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:9.33 |
| 2 | Junta INFLUENCE West Germany, Indonesia | 30.62 | 5.00 | 35.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:9.33 |
| 3 | Missile Envy INFLUENCE West Germany, Indonesia | 30.62 | 5.00 | 35.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:9.33 |
| 4 | Indo-Pakistani War COUP Algeria | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:1.5 |
| 5 | Junta COUP Algeria | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:8`
- hand: `CIA Created[26], Formosan Resolution[35], The Cambridge Five[36], Quagmire[45], Kitchen Debates[51], Missile Envy[52], Latin American Death Squads[70], One Small Step[81]`
- state: `VP 7, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | Missile Envy COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 4 | One Small Step COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 5 | CIA Created COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Junta [50] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Junta[50], Kitchen Debates[51], Missile Envy[52], Puppet Governments[67], Shuttle Diplomacy[74], Our Man in Tehran[84]`
- state: `VP 7, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Algeria | 28.85 | 4.00 | 25.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 2 | Missile Envy COUP Algeria | 28.85 | 4.00 | 25.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 3 | Junta COUP Mexico | 28.10 | 4.00 | 24.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 4 | Missile Envy COUP Mexico | 28.10 | 4.00 | 24.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 5 | Junta INFLUENCE East Germany, West Germany | 26.70 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Missile Envy [52] as COUP`
- flags: `milops_shortfall:8`
- hand: `CIA Created[26], The Cambridge Five[36], Quagmire[45], Kitchen Debates[51], Missile Envy[52], Latin American Death Squads[70], One Small Step[81]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Saharan States | 44.35 | 4.00 | 40.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 44.35 | 4.00 | 40.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:3.5 |
| 3 | One Small Step COUP Saharan States | 44.35 | 4.00 | 40.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:3.5 |
| 4 | CIA Created COUP Saharan States | 38.00 | 4.00 | 34.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Saharan States | 38.00 | 4.00 | 34.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Kitchen Debates[51], Missile Envy[52], Puppet Governments[67], Shuttle Diplomacy[74], Our Man in Tehran[84]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Saharan States | 44.80 | 4.00 | 41.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 2 | Shuttle Diplomacy COUP Saharan States | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Saharan States | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Saharan States | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Kitchen Debates COUP Saharan States | 26.45 | 4.00 | 34.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:8`
- hand: `CIA Created[26], The Cambridge Five[36], Quagmire[45], Kitchen Debates[51], Latin American Death Squads[70], One Small Step[81]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | CIA Created COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 5 | Quagmire COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Kitchen Debates[51], Puppet Governments[67], Shuttle Diplomacy[74], Our Man in Tehran[84]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 15.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Shuttle Diplomacy COUP Cameroon | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Shuttle Diplomacy COUP Saharan States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Shuttle Diplomacy COUP SE African States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Shuttle Diplomacy COUP Guatemala | 10.15 | 4.00 | 26.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:8`
- hand: `CIA Created[26], The Cambridge Five[36], Quagmire[45], Kitchen Debates[51], One Small Step[81]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 2 | One Small Step COUP SE African States | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP Sudan | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Zimbabwe | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Colombia | 25.05 | 4.00 | 21.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Kitchen Debates[51], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Kitchen Debates COUP Saharan States | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Cameroon | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Puppet Governments COUP SE African States | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:8`
- hand: `CIA Created[26], The Cambridge Five[36], Quagmire[45], Kitchen Debates[51]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 45.20 | 4.00 | 41.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:2.5 |
| 2 | Kitchen Debates COUP Saharan States | 45.20 | 4.00 | 41.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:2.5 |
| 3 | Quagmire COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP SE African States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Kitchen Debates[51], Our Man in Tehran[84]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Saharan States | 44.55 | 4.00 | 56.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Kitchen Debates COUP Saharan States | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Cameroon | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP SE African States | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Guatemala | 21.80 | 4.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:8`
- hand: `The Cambridge Five[36], Quagmire[45], Kitchen Debates[51]`
- state: `VP 7, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 57.20 | 4.00 | 53.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:8.00, coup_access_open, expected_swing:2.5 |
| 2 | Quagmire COUP Saharan States | 49.90 | 4.00 | 66.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:8.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Saharan States | 47.55 | 4.00 | 59.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:8.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Kitchen Debates COUP SE African States | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Kitchen Debates COUP Sudan | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +2, DEFCON +1, MilOps U-3/A-2`
