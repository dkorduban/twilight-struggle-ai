# minimal_hybrid detailed rollout log

- seed: `20260510`
- winner: `US`
- final_vp: `-10`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], NATO[21], Suez Crisis[28], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], US/Japan Mutual Defense Pact[27], Red Scare/Purge[31], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], NATO[21], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Arab-Israeli War COUP Iran | 69.48 | 4.00 | 65.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Blockade COUP Iran | 64.13 | 4.00 | 60.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Romanian Abdication COUP Iran | 64.13 | 4.00 | 60.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Nasser COUP Iran | 64.13 | 4.00 | 60.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Red Scare/Purge[31], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE North Korea, Iran, Indonesia, Philippines | 80.62 | 6.00 | 76.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Olympic Games INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Warsaw Pact Formed INFLUENCE Iran, Indonesia, Philippines | 43.22 | 6.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | Red Scare/Purge COUP Syria | 36.68 | 4.00 | 33.28 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5 |
| 5 | Red Scare/Purge COUP Indonesia | 36.33 | 4.00 | 32.93 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.17, empty_coup_penalty, expected_swing:5.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Nasser[15], NATO[21], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Iran | 68.15 | 4.00 | 64.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Blockade COUP Iran | 62.80 | 4.00 | 58.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Romanian Abdication COUP Iran | 62.80 | 4.00 | 58.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Nasser COUP Iran | 62.80 | 4.00 | 58.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | NATO INFLUENCE West Germany, Japan, North Korea, Thailand | 60.20 | 6.00 | 78.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, Turkey | 38.60 | 6.00 | 34.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, non_coup_milops_penalty:1.60 |
| 2 | Warsaw Pact Formed INFLUENCE East Germany, France, Turkey | 35.50 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | Olympic Games COUP Syria | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 4 | Korean War INFLUENCE East Germany, Turkey | 22.60 | 6.00 | 34.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | The Cambridge Five INFLUENCE East Germany, Turkey | 22.60 | 6.00 | 34.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15], NATO[21], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE East Germany, Japan, North Korea, Thailand | 62.60 | 6.00 | 81.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE North Korea, Thailand | 32.70 | 6.00 | 43.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Blockade INFLUENCE Thailand | 28.30 | 6.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 4 | Romanian Abdication INFLUENCE Thailand | 28.30 | 6.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 5 | Nasser INFLUENCE Thailand | 28.30 | 6.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Truman Doctrine[19], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE France, Japan, Pakistan | 38.70 | 6.00 | 55.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, control_break:Japan, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Korean War INFLUENCE France, Japan | 25.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | The Cambridge Five INFLUENCE France, Japan | 25.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Captured Nazi Scientist INFLUENCE Japan | 25.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.00 |
| 5 | Truman Doctrine INFLUENCE Japan | 25.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Thailand | 32.80 | 6.00 | 43.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Blockade INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 3 | Romanian Abdication INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 4 | Nasser INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 5 | Blockade COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Captured Nazi Scientist[18], Truman Doctrine[19], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, Pakistan | 27.63 | 6.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | The Cambridge Five INFLUENCE West Germany, Pakistan | 27.63 | 6.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 23.83 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:2.67 |
| 4 | Truman Doctrine INFLUENCE West Germany | 23.83 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:2.67 |
| 5 | Captured Nazi Scientist COUP Syria | 20.97 | 4.00 | 17.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china`
- hand: `Blockade[10], Romanian Abdication[12], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Blockade COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Romanian Abdication COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Iraq | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open |
| 2 | Truman Doctrine COUP Iraq | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open |
| 3 | Captured Nazi Scientist COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 4 | Truman Doctrine COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 5 | The Cambridge Five INFLUENCE Italy, India | 16.70 | 6.00 | 34.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 13: T1 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Romanian Abdication REALIGN Cuba | 3.34 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window |
| 4 | Nasser REALIGN Cuba | 3.34 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window |
| 5 | Romanian Abdication EVENT | 2.35 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Truman Doctrine[19], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Italy, India | 23.70 | 6.00 | 34.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE India | 23.40 | 6.00 | 17.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India |
| 3 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Truman Doctrine COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Zimbabwe | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 15: T2 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], De Gaulle Leads France[17], Independent Reds[22], Marshall Plan[23], Indo-Pakistani War[24], CIA Created[26], East European Unrest[29], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], COMECON[14], Containment[25], De-Stalinization[33], Nuclear Test Ban[34], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Independent Reds[22], Marshall Plan[23], Indo-Pakistani War[24], CIA Created[26], East European Unrest[29], Decolonization[30]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE France, South Korea, Israel, Thailand | 53.68 | 6.00 | 74.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.05, control_break:France, influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Indo-Pakistani War INFLUENCE France, Thailand | 43.53 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Decolonization INFLUENCE France, Thailand | 43.53 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Duck and Cover INFLUENCE France, South Korea, Thailand | 40.93 | 6.00 | 58.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | East European Unrest INFLUENCE France, South Korea, Thailand | 40.93 | 6.00 | 58.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], COMECON[14], Containment[25], De-Stalinization[33], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE France, Italy, Iraq | 55.68 | 6.00 | 52.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Italy:14.45, control_break:Italy, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 2 | Containment INFLUENCE France, Italy, Iraq | 55.68 | 6.00 | 52.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Italy:14.45, control_break:Italy, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 3 | NORAD INFLUENCE France, Italy, Iraq | 55.68 | 6.00 | 52.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Italy:14.45, control_break:Italy, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:2.67 |
| 4 | Special Relationship INFLUENCE France, Italy | 39.53 | 6.00 | 36.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.67 |
| 5 | COMECON INFLUENCE France, Italy, Iraq | 35.68 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Italy:14.45, control_break:Italy, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Independent Reds[22], Indo-Pakistani War[24], CIA Created[26], East European Unrest[29], Decolonization[30]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE France, Thailand | 43.00 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Decolonization INFLUENCE France, Thailand | 43.00 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | Duck and Cover INFLUENCE France, Iraq, Thailand | 42.15 | 6.00 | 59.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | East European Unrest INFLUENCE France, Iraq, Thailand | 42.15 | 6.00 | 59.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Indo-Pakistani War COUP Italy | 36.70 | 4.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], COMECON[14], Containment[25], De-Stalinization[33], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Saudi Arabia, Panama | 51.00 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:3.20 |
| 2 | NORAD INFLUENCE Japan, Saudi Arabia, Panama | 51.00 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:3.20 |
| 3 | Special Relationship INFLUENCE Saudi Arabia, Panama | 35.00 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:3.20 |
| 4 | Containment COUP Syria | 32.80 | 4.00 | 29.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 5 | NORAD COUP Syria | 32.80 | 4.00 | 29.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Independent Reds[22], CIA Created[26], East European Unrest[29], Decolonization[30]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Iraq, Thailand | 41.45 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Duck and Cover INFLUENCE Italy, Iraq, Thailand | 37.75 | 6.00 | 56.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | East European Unrest INFLUENCE Italy, Iraq, Thailand | 37.75 | 6.00 | 56.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Decolonization COUP Italy | 36.90 | 4.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 5 | Decolonization COUP Philippines | 36.90 | 4.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], COMECON[14], De-Stalinization[33], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, Egypt | 49.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:4.00 |
| 2 | Special Relationship INFLUENCE Japan, Egypt | 33.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:4.00 |
| 3 | NORAD COUP Syria | 33.00 | 4.00 | 29.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | NORAD COUP Indonesia | 32.65 | 4.00 | 29.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |
| 5 | NORAD COUP Poland | 29.85 | 4.00 | 26.30 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Poland, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Independent Reds[22], CIA Created[26], East European Unrest[29]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Italy, Philippines, Thailand | 33.57 | 6.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | East European Unrest INFLUENCE Italy, Philippines, Thailand | 33.57 | 6.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Duck and Cover COUP Italy | 22.58 | 4.00 | 39.03 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Duck and Cover COUP Philippines | 22.58 | 4.00 | 39.03 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | East European Unrest COUP Italy | 22.58 | 4.00 | 39.03 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], COMECON[14], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Italy, Philippines | 39.27 | 6.00 | 38.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:5.33 |
| 2 | COMECON INFLUENCE Italy, Egypt, Philippines | 37.82 | 6.00 | 57.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | De-Stalinization INFLUENCE Italy, Egypt, Philippines | 37.82 | 6.00 | 57.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Special Relationship COUP Italy | 32.23 | 4.00 | 28.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.67, expected_swing:1.5 |
| 5 | Special Relationship COUP Philippines | 32.23 | 4.00 | 28.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.67, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26], East European Unrest[29]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Indonesia | 33.65 | 4.00 | 50.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Independent Reds COUP Indonesia | 32.30 | 4.00 | 44.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Indonesia | 29.95 | 4.00 | 38.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | East European Unrest INFLUENCE Japan, Saudi Arabia, Thailand | 24.45 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | East European Unrest COUP Egypt | 22.50 | 4.00 | 38.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 26: T2 AR5 US

- chosen: `COMECON [14] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], COMECON[14], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Indonesia | 33.65 | 4.00 | 50.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | De-Stalinization COUP Indonesia | 33.65 | 4.00 | 50.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Fidel COUP Indonesia | 32.30 | 4.00 | 44.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | COMECON INFLUENCE Japan, Egypt, Indonesia | 22.25 | 6.00 | 50.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | De-Stalinization INFLUENCE Japan, Egypt, Indonesia | 22.25 | 6.00 | 50.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 27: T2 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Saudi Arabia, Thailand | 26.45 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Independent Reds COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, Egypt, Libya | 36.10 | 6.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty |
| 2 | Fidel INFLUENCE Japan, Egypt | 24.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 3 | De-Stalinization COUP Syria | 10.00 | 4.00 | 26.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Fidel COUP Syria | 8.65 | 4.00 | 20.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], Captured Nazi Scientist[18], CIA Created[26], Red Scare/Purge[31], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Nasser[15], Warsaw Pact Formed[16], NATO[21], Independent Reds[22], Decolonization[30], De-Stalinization[33], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Japan, Indonesia, Thailand | 54.00 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Socialist Governments COUP Indonesia | 53.65 | 4.00 | 50.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 3 | Fidel COUP Indonesia | 47.30 | 4.00 | 43.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Socialist Governments COUP Egypt | 42.50 | 4.00 | 38.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Socialist Governments COUP Iran | 42.50 | 4.00 | 38.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `NORAD [38] as COUP`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Nasser[15], Warsaw Pact Formed[16], Independent Reds[22], Decolonization[30], De-Stalinization[33], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Indonesia | 48.65 | 4.00 | 45.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 2 | Independent Reds COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 3 | NORAD COUP Philippines | 38.25 | 4.00 | 34.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 4 | NORAD INFLUENCE Japan, Libya | 36.40 | 6.00 | 34.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 5 | NORAD COUP Syria | 34.00 | 4.00 | 30.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 33: T3 AR2 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Blockade[10], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | Fidel COUP Egypt | 30.35 | 4.00 | 26.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Fidel COUP Iran | 30.35 | 4.00 | 26.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Blockade COUP Egypt | 24.00 | 4.00 | 20.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Blockade COUP Iran | 24.00 | 4.00 | 20.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Independent Reds [22] as COUP`
- flags: `none`
- hand: `Romanian Abdication[12], Nasser[15], Warsaw Pact Formed[16], Independent Reds[22], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Syria | 24.65 | 4.00 | 20.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 2 | Independent Reds INFLUENCE Libya | 24.40 | 6.00 | 18.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Libya:13.70, control_break:Libya |
| 3 | Warsaw Pact Formed INFLUENCE Japan, Libya | 20.40 | 6.00 | 34.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 4 | De-Stalinization INFLUENCE Japan, Libya | 20.40 | 6.00 | 34.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 5 | Independent Reds COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Egypt | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Blockade COUP Iran | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Egypt | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Iran | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Egypt | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 36: T3 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Warsaw Pact Formed[16], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Egypt, Libya | 22.95 | 6.00 | 37.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 2 | De-Stalinization INFLUENCE Egypt, Libya | 22.95 | 6.00 | 37.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE Egypt | 12.55 | 6.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 4 | Nasser INFLUENCE Egypt | 12.55 | 6.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty |
| 5 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 20.97 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:5.33 |
| 2 | UN Intervention INFLUENCE Thailand | 20.97 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:5.33 |
| 3 | Formosan Resolution INFLUENCE Japan, Thailand | 20.97 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | CIA Created INFLUENCE Thailand | 8.97 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Formosan Resolution SPACE | 3.37 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | De-Stalinization SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `CIA Created[26], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 12.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:14.00 |
| 2 | Formosan Resolution INFLUENCE Japan, Thailand | 12.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | CIA Created INFLUENCE Thailand | 0.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Formosan Resolution SPACE | -5.30 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | UN Intervention REALIGN Cuba | -10.66 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Decolonization[30]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Decolonization INFLUENCE Japan | 5.85 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 5 | Decolonization COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Thailand | 4.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 2 | CIA Created INFLUENCE Thailand | -7.70 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 3 | Formosan Resolution SPACE | -13.30 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 4 | CIA Created EVENT | -28.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:22.00 |
| 5 | Formosan Resolution EVENT | -28.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:22.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Nasser [15] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Nasser[15], Decolonization[30]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 3 | Decolonization INFLUENCE Japan | 5.85 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Decolonization COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Sudan | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-3`

## Step 43: T4 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Socialist Governments[7], Blockade[10], Arab-Israeli War[13], UN Intervention[32], How I Learned to Stop Worrying[49], ABM Treaty[60], Cultural Revolution[61], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Independent Reds [22] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Nasser[15], Warsaw Pact Formed[16], Independent Reds[22], De-Stalinization[33], Portuguese Empire Crumbles[55], OAS Founded[71], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Socialist Governments[7], Blockade[10], Arab-Israeli War[13], UN Intervention[32], How I Learned to Stop Worrying[49], Cultural Revolution[61], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Indonesia | 52.04 | 4.00 | 48.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:4.5 |
| 2 | Cultural Revolution COUP Indonesia | 52.04 | 4.00 | 48.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:4.5 |
| 3 | Socialist Governments INFLUENCE UK, Mexico, Algeria | 50.28 | 6.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 4 | Cultural Revolution INFLUENCE UK, Mexico, Algeria | 50.28 | 6.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 5 | Arab-Israeli War COUP Indonesia | 45.69 | 4.00 | 41.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 46: T4 AR1 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Nasser[15], Warsaw Pact Formed[16], De-Stalinization[33], Portuguese Empire Crumbles[55], OAS Founded[71], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE Mexico, Philippines | 35.78 | 6.00 | 34.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Philippines:12.70, control_break:Philippines, non_coup_milops_penalty:4.57 |
| 2 | Warsaw Pact Formed INFLUENCE Mexico, South Africa, Philippines | 32.43 | 6.00 | 51.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, influence:Philippines:12.70, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 3 | De-Stalinization INFLUENCE Mexico, South Africa, Philippines | 32.43 | 6.00 | 51.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, influence:Philippines:12.70, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 4 | Korean War INFLUENCE Mexico, Philippines | 19.78 | 6.00 | 34.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Philippines:12.70, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Portuguese Empire Crumbles INFLUENCE Mexico, Philippines | 19.78 | 6.00 | 34.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Philippines:12.70, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Blockade[10], Arab-Israeli War[13], UN Intervention[32], How I Learned to Stop Worrying[49], Cultural Revolution[61], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE UK, Mexico, Algeria | 53.52 | 6.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.33 |
| 2 | Arab-Israeli War INFLUENCE Mexico, Algeria | 37.52 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.33 |
| 3 | How I Learned to Stop Worrying INFLUENCE Mexico, Algeria | 37.52 | 6.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.33 |
| 4 | Shuttle Diplomacy INFLUENCE UK, Mexico, Algeria | 33.52 | 6.00 | 49.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE UK, Mexico, Algeria | 33.52 | 6.00 | 49.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Nasser[15], Warsaw Pact Formed[16], De-Stalinization[33], Portuguese Empire Crumbles[55], OAS Founded[71]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Algeria, South Africa | 29.37 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | De-Stalinization INFLUENCE West Germany, Algeria, South Africa | 29.37 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | OAS Founded COUP Algeria | 24.63 | 4.00 | 20.78 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | OAS Founded COUP Mexico | 20.38 | 4.00 | 16.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 5 | Korean War INFLUENCE Algeria, South Africa | 17.37 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Blockade[10], Arab-Israeli War[13], UN Intervention[32], How I Learned to Stop Worrying[49], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, Morocco | 37.05 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:1.60 |
| 2 | How I Learned to Stop Worrying INFLUENCE West Germany, Morocco | 37.05 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:1.60 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Morocco | 32.45 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Morocco | 32.45 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Blockade INFLUENCE Morocco | 21.05 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Nasser[15], De-Stalinization[33], Portuguese Empire Crumbles[55], OAS Founded[71]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Morocco, South Africa | 33.90 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 2 | OAS Founded COUP Morocco | 22.75 | 4.00 | 18.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open |
| 3 | Korean War INFLUENCE Morocco, South Africa | 21.90 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Portuguese Empire Crumbles INFLUENCE Morocco, South Africa | 21.90 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | OAS Founded INFLUENCE South Africa | 21.25 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Blockade[10], UN Intervention[32], How I Learned to Stop Worrying[49], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 35.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 30.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 30.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Blockade INFLUENCE West Germany | 20.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 5 | UN Intervention INFLUENCE West Germany | 20.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Nasser[15], Portuguese Empire Crumbles[55], OAS Founded[71]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | OAS Founded COUP Algeria | 20.30 | 4.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | OAS Founded COUP Morocco | 18.15 | 4.00 | 14.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3 |
| 4 | OAS Founded COUP Israel | 17.75 | 4.00 | 13.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3 |
| 5 | OAS Founded COUP Iraq | 17.15 | 4.00 | 13.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 53: T4 AR5 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], UN Intervention[32], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 30.13 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 30.13 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Blockade INFLUENCE West Germany | 19.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.67 |
| 4 | UN Intervention INFLUENCE West Germany | 19.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.67 |
| 5 | Blockade COUP Saharan States | 11.87 | 4.00 | 8.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Korean War[11], Nasser[15], Portuguese Empire Crumbles[55]`
- state: `VP 0, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, South Africa | 14.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 14.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Korean War COUP Colombia | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Korean War COUP Saharan States | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Korean War COUP SE African States | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], UN Intervention[32], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 25.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Blockade INFLUENCE West Germany | 15.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:7.00 |
| 3 | UN Intervention INFLUENCE West Germany | 15.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:7.00 |
| 4 | Blockade COUP Saharan States | 12.20 | 4.00 | 8.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 12.20 | 4.00 | 8.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Portuguese Empire Crumbles[55]`
- state: `VP 0, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Colombia | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Portuguese Empire Crumbles COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP SE African States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP Sudan | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Zimbabwe | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 57: T4 AR7 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Blockade[10], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP Guatemala | 11.95 | 4.00 | 8.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Guatemala | 11.95 | 4.00 | 8.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade INFLUENCE West Germany | 11.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Nasser COUP Colombia | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Nasser COUP SE African States | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP Sudan | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP Zimbabwe | 3.20 | 4.00 | 11.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], Red Scare/Purge[31], De-Stalinization[33], Muslim Revolution[59], Flower Power[62], OPEC[64]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:5`
- hand: `UN Intervention[32], NORAD[38], Brush War[39], Bear Trap[47], We Will Bury You[53], Lonely Hearts Club Band[65], Camp David Accords[66], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], De-Stalinization[33], Muslim Revolution[59], Flower Power[62], OPEC[64]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Cuba | 62.49 | 6.00 | 62.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.71 |
| 2 | Muslim Revolution COUP Saharan States | 51.68 | 4.00 | 48.28 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:5.5 |
| 3 | De-Stalinization INFLUENCE East Germany, France, West Germany | 47.09 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 4 | OPEC INFLUENCE East Germany, France, West Germany | 47.09 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 5 | De-Stalinization COUP Saharan States | 45.33 | 4.00 | 41.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `UN Intervention[32], Brush War[39], Bear Trap[47], We Will Bury You[53], Lonely Hearts Club Band[65], Camp David Accords[66], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE Nigeria, South Africa | 37.24 | 6.00 | 37.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Bear Trap COUP Mexico | 33.18 | 4.00 | 29.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 3 | Bear Trap COUP Algeria | 32.43 | 4.00 | 28.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 4 | We Will Bury You INFLUENCE Brazil, Nigeria, South Africa | 29.29 | 6.00 | 53.60 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 5 | Bear Trap COUP Nigeria | 27.83 | 4.00 | 24.28 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], De-Stalinization[33], Flower Power[62], OPEC[64]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 46.13 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 46.13 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 3 | De-Stalinization COUP Saharan States | 45.57 | 4.00 | 42.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 4 | OPEC COUP Saharan States | 45.57 | 4.00 | 42.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 5 | Flower Power COUP Saharan States | 39.22 | 4.00 | 35.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `UN Intervention[32], Brush War[39], We Will Bury You[53], Lonely Hearts Club Band[65], Camp David Accords[66], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE West Germany, Brazil, South Africa | 28.88 | 6.00 | 54.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 2 | Lonely Hearts Club Band COUP Mexico | 27.07 | 4.00 | 23.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:1.5 |
| 3 | Camp David Accords COUP Mexico | 27.07 | 4.00 | 23.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:1.5 |
| 4 | Lonely Hearts Club Band COUP Algeria | 26.32 | 4.00 | 22.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:1.5 |
| 5 | Camp David Accords COUP Algeria | 26.32 | 4.00 | 22.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `OPEC [64] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], Flower Power[62], OPEC[64]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Saharan States | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 44.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Flower Power COUP Saharan States | 39.55 | 4.00 | 35.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | OPEC COUP Egypt | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | OPEC COUP Iran | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 66: T5 AR3 US

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:5`
- hand: `UN Intervention[32], Brush War[39], Lonely Hearts Club Band[65], Camp David Accords[66], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Saharan States | 39.55 | 4.00 | 35.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Camp David Accords COUP Saharan States | 39.55 | 4.00 | 35.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | UN Intervention COUP Saharan States | 33.20 | 4.00 | 29.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Lonely Hearts Club Band COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Camp David Accords COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 67: T5 AR4 USSR

- chosen: `Flower Power [62] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], Flower Power[62]`
- state: `VP 0, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Nigeria | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Romanian Abdication COUP Nigeria | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Nigeria | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Flower Power INFLUENCE West Germany, Nigeria | 33.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, access_touch:Nigeria, non_coup_milops_penalty:4.00 |
| 5 | Flower Power COUP Egypt | 29.65 | 4.00 | 25.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:3`
- hand: `UN Intervention[32], Brush War[39], Camp David Accords[66], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 39.05 | 4.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | UN Intervention COUP Saharan States | 32.70 | 4.00 | 28.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 3 | Brush War COUP Saharan States | 25.40 | 4.00 | 41.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Saharan States | 23.05 | 4.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP Saharan States | 23.05 | 4.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | 16.67 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | 16.67 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 3 | Independent Reds INFLUENCE East Germany, West Germany | 16.07 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Romanian Abdication COUP Cameroon | 12.53 | 4.00 | 8.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Romanian Abdication COUP Saharan States | 12.53 | 4.00 | 8.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:3`
- hand: `UN Intervention[32], Brush War[39], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 33.20 | 4.00 | 29.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Brush War COUP Saharan States | 25.90 | 4.00 | 42.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Saharan States | 23.55 | 4.00 | 35.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Saharan States | 23.55 | 4.00 | 35.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | UN Intervention INFLUENCE West Germany | 19.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Independent Reds[22]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Cameroon | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Guatemala | 11.95 | 4.00 | 8.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Haiti | 11.95 | 4.00 | 8.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist INFLUENCE West Germany | 8.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Brush War [39] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Brush War[39], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Colombia | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Brush War COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Brush War COUP SE African States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Brush War COUP Sudan | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Brush War COUP Zimbabwe | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 73: T5 AR7 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Cameroon | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Independent Reds COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Independent Reds COUP Guatemala | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Independent Reds COUP Haiti | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Independent Reds INFLUENCE West Germany, Congo/Zaire | 0.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:22.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Liberation Theology [76] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Liberation Theology COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Liberation Theology COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Liberation Theology COUP Zimbabwe | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 75: T6 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], COMECON[14], CIA Created[26], Quagmire[45], Kitchen Debates[51], Latin American Death Squads[70], Sadat Expels Soviets[73], Alliance for Progress[79], Che[83]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Nasser[15], Olympic Games[20], Indo-Pakistani War[24], East European Unrest[29], Decolonization[30], The Cambridge Five[36], Special Relationship[37], Willy Brandt[58]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Fidel EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `COMECON[14], CIA Created[26], Quagmire[45], Kitchen Debates[51], Latin American Death Squads[70], Sadat Expels Soviets[73], Alliance for Progress[79], Che[83]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, West Germany, Congo/Zaire | 46.59 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |
| 2 | Quagmire INFLUENCE East Germany, West Germany, Congo/Zaire | 46.59 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |
| 3 | Che INFLUENCE East Germany, West Germany, Congo/Zaire | 46.59 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:6.86 |
| 4 | COMECON COUP Egypt | 36.71 | 4.00 | 33.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | COMECON COUP Iran | 36.71 | 4.00 | 33.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Nasser[15], Olympic Games[20], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36], Special Relationship[37], Willy Brandt[58]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Argentina, Brazil | 36.24 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.86 |
| 2 | Indo-Pakistani War INFLUENCE Argentina, Brazil | 36.24 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.86 |
| 3 | Special Relationship INFLUENCE Argentina, Brazil | 36.24 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.86 |
| 4 | Olympic Games COUP Mexico | 27.11 | 4.00 | 23.41 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Mexico | 27.11 | 4.00 | 23.41 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `CIA Created[26], Quagmire[45], Kitchen Debates[51], Latin American Death Squads[70], Sadat Expels Soviets[73], Alliance for Progress[79], Che[83]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE West Germany, Angola, Congo/Zaire | 55.50 | 6.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 2 | Che INFLUENCE West Germany, Angola, Congo/Zaire | 55.50 | 6.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 3 | Latin American Death Squads INFLUENCE Angola, Congo/Zaire | 39.50 | 6.00 | 41.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 4 | Quagmire COUP Egypt | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Quagmire COUP Iran | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Nasser[15], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36], Special Relationship[37], Willy Brandt[58]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Argentina, Chile | 37.70 | 6.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:8.00 |
| 2 | Special Relationship INFLUENCE Argentina, Chile | 37.70 | 6.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:8.00 |
| 3 | Indo-Pakistani War COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Special Relationship COUP Mexico | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Algeria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `CIA Created[26], Kitchen Debates[51], Latin American Death Squads[70], Sadat Expels Soviets[73], Alliance for Progress[79], Che[83]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, West Germany, Angola | 43.25 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:9.60 |
| 2 | Che COUP Egypt | 37.40 | 4.00 | 33.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Che COUP Iran | 37.40 | 4.00 | 33.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Che COUP Libya | 37.40 | 4.00 | 33.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Che COUP Mexico | 34.15 | 4.00 | 30.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Nasser[15], Decolonization[30], The Cambridge Five[36], Special Relationship[37], Willy Brandt[58]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Chile, South Africa | 29.70 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.60 |
| 2 | Special Relationship COUP Mexico | 27.80 | 4.00 | 24.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, expected_swing:1.5 |
| 3 | Special Relationship COUP Algeria | 27.05 | 4.00 | 23.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, expected_swing:1.5 |
| 4 | Special Relationship COUP Cuba | 23.15 | 4.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open |
| 5 | Special Relationship COUP Colombia | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `CIA Created[26], Kitchen Debates[51], Latin American Death Squads[70], Sadat Expels Soviets[73], Alliance for Progress[79]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Egypt | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Latin American Death Squads COUP Iran | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Latin American Death Squads COUP Libya | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Latin American Death Squads COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | Latin American Death Squads COUP Algeria | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 84: T6 AR4 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Fidel[8], Nasser[15], Decolonization[30], The Cambridge Five[36], Willy Brandt[58]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Chile, South Africa | 16.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Decolonization INFLUENCE Chile, South Africa | 16.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | The Cambridge Five INFLUENCE Chile, South Africa | 16.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Willy Brandt INFLUENCE Chile, South Africa | 16.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Fidel COUP Colombia | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51], Sadat Expels Soviets[73], Alliance for Progress[79]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Angola | 22.18 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Alliance for Progress INFLUENCE East Germany, West Germany, Angola | 22.18 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Sadat Expels Soviets COUP Cameroon | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Sadat Expels Soviets COUP Saharan States | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Sadat Expels Soviets COUP SE African States | 6.57 | 4.00 | 23.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Nasser[15], Decolonization[30], The Cambridge Five[36], Willy Brandt[58]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Chile, South Africa | 7.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | The Cambridge Five INFLUENCE Chile, South Africa | 7.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Willy Brandt INFLUENCE Chile, South Africa | 7.30 | 6.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Decolonization COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51], Alliance for Progress[79]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Cameroon | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Alliance for Progress COUP Saharan States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Alliance for Progress COUP SE African States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Guatemala | 6.65 | 4.00 | 23.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Alliance for Progress COUP Haiti | 6.65 | 4.00 | 23.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 88: T6 AR6 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Nasser[15], The Cambridge Five[36], Willy Brandt[58]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Zimbabwe | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 89: T6 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Cameroon | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | CIA Created COUP Saharan States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | CIA Created COUP SE African States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Kitchen Debates COUP Cameroon | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Kitchen Debates COUP Saharan States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Willy Brandt [58] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Nasser[15], Willy Brandt[58]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Colombia | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP SE African States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Willy Brandt COUP Sudan | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Zimbabwe | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], CIA Created[26], Arms Race[42], Cuban Missile Crisis[43], Nuclear Subs[44], Missile Envy[52], South African Unrest[56], Puppet Governments[67], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Fidel[8], Blockade[10], Captured Nazi Scientist[18], Containment[25], Decolonization[30], Nuclear Test Ban[34], Formosan Resolution[35], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], CIA Created[26], Cuban Missile Crisis[43], Nuclear Subs[44], Missile Envy[52], South African Unrest[56], Puppet Governments[67], Lone Gunman[109]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Indonesia | 52.90 | 4.00 | 49.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Missile Envy COUP Indonesia | 46.55 | 4.00 | 42.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | South African Unrest COUP Indonesia | 46.55 | 4.00 | 42.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Angola | 44.85 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:8.00 |
| 5 | Cuban Missile Crisis COUP Egypt | 43.00 | 4.00 | 39.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 94: T7 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Fidel[8], Blockade[10], Captured Nazi Scientist[18], Containment[25], Decolonization[30], Formosan Resolution[35], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Argentina, Chile, South Africa | 47.35 | 6.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Ussuri River Skirmish INFLUENCE Argentina, Chile, South Africa | 47.35 | 6.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Containment COUP Mexico | 39.75 | 4.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Mexico | 39.75 | 4.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |
| 5 | Containment COUP Algeria | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], CIA Created[26], Nuclear Subs[44], Missile Envy[52], South African Unrest[56], Puppet Governments[67], Lone Gunman[109]`
- state: `VP -1, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Indonesia | 45.88 | 4.00 | 42.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | South African Unrest COUP Indonesia | 45.88 | 4.00 | 42.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 3 | Lone Gunman COUP Indonesia | 39.53 | 4.00 | 35.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 4 | Missile Envy COUP Egypt | 35.98 | 4.00 | 32.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 5 | Missile Envy COUP Iran | 35.98 | 4.00 | 32.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Fidel[8], Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Formosan Resolution[35], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE Argentina, Chile, South Africa | 46.02 | 6.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | Ussuri River Skirmish COUP Mexico | 34.08 | 4.00 | 30.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |
| 3 | Ussuri River Skirmish COUP Algeria | 33.33 | 4.00 | 29.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |
| 4 | Formosan Resolution INFLUENCE Chile, South Africa | 29.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 5 | Formosan Resolution COUP Mexico | 27.73 | 4.00 | 24.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], CIA Created[26], Nuclear Subs[44], South African Unrest[56], Puppet Governments[67], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE West Germany, Angola | 31.05 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, non_coup_milops_penalty:6.40 |
| 2 | South African Unrest COUP Egypt | 30.25 | 4.00 | 26.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | South African Unrest COUP Iran | 30.25 | 4.00 | 26.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | South African Unrest COUP Libya | 30.25 | 4.00 | 26.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | South African Unrest COUP Mexico | 27.00 | 4.00 | 23.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:7`
- hand: `Fidel[8], Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Formosan Resolution[35], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Mexico | 28.20 | 4.00 | 24.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 2 | Formosan Resolution INFLUENCE Chile, South Africa | 28.10 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 3 | Formosan Resolution COUP Algeria | 27.45 | 4.00 | 23.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 4 | Formosan Resolution COUP Cuba | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open |
| 5 | Captured Nazi Scientist COUP Cuba | 22.70 | 4.00 | 18.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 99: T7 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], CIA Created[26], Nuclear Subs[44], Puppet Governments[67], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, West Germany, Angola | 24.85 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Lone Gunman INFLUENCE West Germany | 14.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Nuclear Subs INFLUENCE West Germany, Angola | 13.45 | 6.00 | 31.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Puppet Governments INFLUENCE West Germany, Angola | 13.45 | 6.00 | 31.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Lone Gunman COUP Cameroon | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 13.70 | 4.00 | 9.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 13.70 | 4.00 | 9.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP SE African States | 13.70 | 4.00 | 9.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Sudan | 13.70 | 4.00 | 9.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Zimbabwe | 13.70 | 4.00 | 9.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `CIA Created[26], Nuclear Subs[44], Puppet Governments[67], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE West Germany | 16.33 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 2 | Nuclear Subs INFLUENCE West Germany, Angola | 15.78 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Puppet Governments INFLUENCE West Germany, Angola | 15.78 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Lone Gunman COUP Cameroon | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP Saharan States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Blockade[10], Decolonization[30], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP SE African States | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Sudan | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Zimbabwe | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `CIA Created[26], Nuclear Subs[44], Puppet Governments[67]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Cameroon | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Nuclear Subs COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Cameroon | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Blockade[10], Decolonization[30]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Colombia | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Fidel COUP Saharan States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Fidel COUP SE African States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Fidel COUP Sudan | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Fidel COUP Zimbabwe | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `CIA Created[26], Puppet Governments[67]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Cameroon | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Puppet Governments COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP SE African States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Guatemala | 8.30 | 4.00 | 20.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Haiti | 8.30 | 4.00 | 20.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Decolonization[30]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Colombia | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Decolonization COUP SE African States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Sudan | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Zimbabwe | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 107: T8 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Nasser[15], Independent Reds[22], Willy Brandt[58], Muslim Revolution[59], Cultural Revolution[61], OAS Founded[71], Liberation Theology[76], Reagan Bombs Libya[87], AWACS Sale to Saudis[107]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Duck and Cover[4], Warsaw Pact Formed[16], Olympic Games[20], CIA Created[26], Junta[50], We Will Bury You[53], South African Unrest[56], Puppet Governments[67], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Nasser[15], Independent Reds[22], Willy Brandt[58], Cultural Revolution[61], OAS Founded[71], Liberation Theology[76], Reagan Bombs Libya[87], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Willy Brandt INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Cultural Revolution COUP Cameroon | 26.19 | 4.00 | 22.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:4.5 |
| 5 | Cultural Revolution COUP Saharan States | 26.19 | 4.00 | 22.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Warsaw Pact Formed[16], Olympic Games[20], CIA Created[26], Junta[50], We Will Bury You[53], South African Unrest[56], Puppet Governments[67], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, Poland, West Germany | 38.06 | 6.00 | 65.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 2 | Olympic Games INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Junta INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Puppet Governments INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | One Small Step INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Nasser[15], Independent Reds[22], Willy Brandt[58], OAS Founded[71], Liberation Theology[76], Reagan Bombs Libya[87], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Willy Brandt COUP Cameroon | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Willy Brandt COUP Saharan States | 20.22 | 4.00 | 16.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], Olympic Games[20], CIA Created[26], Junta[50], South African Unrest[56], Puppet Governments[67], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Junta INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | One Small Step INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 5 | Warsaw Pact Formed INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Nasser[15], Independent Reds[22], OAS Founded[71], Liberation Theology[76], Reagan Bombs Libya[87], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 3 | Liberation Theology COUP Cameroon | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:3.5 |
| 4 | Liberation Theology COUP Saharan States | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | Liberation Theology COUP SE African States | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], CIA Created[26], Junta[50], South African Unrest[56], Puppet Governments[67], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Puppet Governments INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 4 | Warsaw Pact Formed INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Junta COUP Saharan States | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], Independent Reds[22], OAS Founded[71], Reagan Bombs Libya[87], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Nasser COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Nasser COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Nasser COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nasser COUP Guatemala | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56], Puppet Governments[67], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | One Small Step INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Puppet Governments COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Puppet Governments COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Puppet Governments COUP Sudan | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Nasser[15], Independent Reds[22], OAS Founded[71], Reagan Bombs Libya[87]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Cameroon | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Nasser COUP Saharan States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Nasser COUP SE African States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Nasser COUP Guatemala | 15.78 | 4.00 | 11.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nasser COUP Haiti | 15.78 | 4.00 | 11.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 118: T8 AR5 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:8`
- hand: `Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 22.88 | 4.00 | 19.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 2 | One Small Step COUP SE African States | 22.88 | 4.00 | 19.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP Sudan | 22.88 | 4.00 | 19.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Zimbabwe | 22.88 | 4.00 | 19.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Colombia | 22.38 | 4.00 | 18.68 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 119: T8 AR6 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Independent Reds[22], OAS Founded[71], Reagan Bombs Libya[87]`
- state: `VP -3, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Reagan Bombs Libya COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | OAS Founded COUP Saharan States | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Independent Reds COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Independent Reds COUP SE African States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 120: T8 AR6 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:6`
- hand: `Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | CIA Created COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | CIA Created COUP Sudan | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | CIA Created COUP Zimbabwe | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Colombia | 16.70 | 4.00 | 12.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Reagan Bombs Libya [87] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `OAS Founded[71], Reagan Bombs Libya[87]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya COUP Saharan States | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | OAS Founded COUP Saharan States | 31.20 | 4.00 | 39.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Reagan Bombs Libya COUP Guatemala | 12.80 | 4.00 | 25.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Warsaw Pact Formed [16] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Warsaw Pact Formed[16], South African Unrest[56]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Warsaw Pact Formed COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Warsaw Pact Formed COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Warsaw Pact Formed COUP Zimbabwe | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Warsaw Pact Formed COUP Colombia | 15.40 | 4.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 123: T9 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], UN Intervention[32], De-Stalinization[33], Brush War[39], Lonely Hearts Club Band[65], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Duck and Cover[4], Korean War[11], COMECON[14], Marshall Plan[23], De-Stalinization[33], Voice of America[75], Alliance for Progress[79], The Iron Lady[86], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Fidel[8], Blockade[10], UN Intervention[32], De-Stalinization[33], Brush War[39], Lonely Hearts Club Band[65], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Saharan States | 46.47 | 4.00 | 42.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Brush War COUP Saharan States | 46.47 | 4.00 | 42.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | De-Stalinization INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Brush War INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | Fidel COUP Saharan States | 40.12 | 4.00 | 36.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 126: T9 AR1 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:9`
- hand: `Duck and Cover[4], Korean War[11], COMECON[14], De-Stalinization[33], Voice of America[75], Alliance for Progress[79], The Iron Lady[86], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Nigeria | 48.97 | 4.00 | 45.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Nigeria | 48.97 | 4.00 | 45.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 3 | The Iron Lady COUP Nigeria | 48.97 | 4.00 | 45.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 4 | Duck and Cover INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 127: T9 AR2 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Blockade[10], UN Intervention[32], Brush War[39], Lonely Hearts Club Band[65], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Brush War COUP Saharan States | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Fidel COUP Saharan States | 39.55 | 4.00 | 35.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Blockade COUP Saharan States | 33.20 | 4.00 | 29.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 33.20 | 4.00 | 29.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], De-Stalinization[33], Voice of America[75], Alliance for Progress[79], The Iron Lady[86], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Alliance for Progress COUP Cameroon | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 4 | The Iron Lady COUP Cameroon | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 5 | Voice of America COUP Cameroon | 39.55 | 4.00 | 35.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Blockade[10], UN Intervention[32], Lonely Hearts Club Band[65], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 39.95 | 4.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | Blockade COUP Saharan States | 33.60 | 4.00 | 29.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Saharan States | 33.60 | 4.00 | 29.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 4 | Fidel INFLUENCE East Germany, West Germany | 29.30 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | Lonely Hearts Club Band COUP Saharan States | 23.95 | 4.00 | 36.25 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `The Iron Lady [86] as COUP`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], De-Stalinization[33], Voice of America[75], The Iron Lady[86], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady COUP Cameroon | 46.30 | 4.00 | 42.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 45.45 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | Voice of America COUP Cameroon | 39.95 | 4.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | Panama Canal Returned COUP Cameroon | 33.60 | 4.00 | 29.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 5 | Voice of America INFLUENCE East Germany, West Germany | 29.30 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], UN Intervention[32], Lonely Hearts Club Band[65], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP SE African States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Voice of America [75] as COUP`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], De-Stalinization[33], Voice of America[75], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Cameroon | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | Panama Canal Returned COUP Cameroon | 34.20 | 4.00 | 30.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Voice of America INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | COMECON COUP Cameroon | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Cameroon | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], Lonely Hearts Club Band[65], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Guatemala | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Haiti | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], De-Stalinization[33], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Cameroon | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | COMECON COUP Cameroon | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | De-Stalinization COUP Cameroon | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Korean War COUP Cameroon | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | COMECON INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Lonely Hearts Club Band COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Camp David Accords COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Camp David Accords COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `COMECON [14] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], COMECON[14], De-Stalinization[33]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Cameroon | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | De-Stalinization COUP Cameroon | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Korean War COUP Cameroon | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | COMECON COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP SE African States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Camp David Accords COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Camp David Accords COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `De-Stalinization [33] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], De-Stalinization[33]`
- state: `VP -3, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Cameroon | 35.90 | 4.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Korean War COUP Cameroon | 33.55 | 4.00 | 45.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | De-Stalinization COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | De-Stalinization COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 139: T10 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `CIA Created[26], East European Unrest[29], We Will Bury You[53], Brezhnev Doctrine[54], Willy Brandt[58], Ussuri River Skirmish[77], Our Man in Tehran[84], Terrorism[95], Solidarity[104]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Terrorism EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], Red Scare/Purge[31], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Allende[57], Grain Sales to Soviets[68], Soviets Shoot Down KAL 007[92], Wargames[103]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `CIA Created[26], East European Unrest[29], Brezhnev Doctrine[54], Willy Brandt[58], Ussuri River Skirmish[77], Our Man in Tehran[84], Terrorism[95], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE Poland, West Germany | 30.32 | 6.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Ussuri River Skirmish INFLUENCE Poland, West Germany | 30.32 | 6.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | Brezhnev Doctrine COUP Cameroon | 26.76 | 4.00 | 23.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 4 | Brezhnev Doctrine COUP Saharan States | 26.76 | 4.00 | 23.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 5 | Brezhnev Doctrine COUP SE African States | 26.76 | 4.00 | 23.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Soviets Shoot Down KAL 007 [92] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Allende[57], Grain Sales to Soviets[68], Soviets Shoot Down KAL 007[92], Wargames[103]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, France, West Germany, Cuba | 59.52 | 6.00 | 65.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:11.43 |
| 2 | Wargames INFLUENCE East Germany, France, West Germany, Cuba | 59.52 | 6.00 | 65.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:11.43 |
| 3 | Soviets Shoot Down KAL 007 COUP Cameroon | 53.11 | 4.00 | 49.71 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 4 | Wargames COUP Cameroon | 53.11 | 4.00 | 49.71 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:5.5 |
| 5 | Summit COUP Cameroon | 46.76 | 4.00 | 43.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `CIA Created[26], East European Unrest[29], Willy Brandt[58], Ussuri River Skirmish[77], Our Man in Tehran[84], Terrorism[95], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish COUP Cameroon | 27.23 | 4.00 | 23.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5 |
| 2 | Ussuri River Skirmish COUP Saharan States | 27.23 | 4.00 | 23.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5 |
| 3 | Ussuri River Skirmish COUP SE African States | 27.23 | 4.00 | 23.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5 |
| 4 | Ussuri River Skirmish COUP Guatemala | 26.48 | 4.00 | 22.93 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5 |
| 5 | Ussuri River Skirmish COUP Haiti | 26.48 | 4.00 | 22.93 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 144: T10 AR2 US

- chosen: `Wargames [103] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Allende[57], Grain Sales to Soviets[68], Wargames[103]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames INFLUENCE East Germany, France, West Germany, Venezuela | 57.27 | 6.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, non_coup_milops_penalty:13.33 |
| 2 | Wargames COUP Cameroon | 53.58 | 4.00 | 50.18 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:5.5 |
| 3 | Summit COUP Cameroon | 47.23 | 4.00 | 43.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:4.5 |
| 4 | Summit INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 5 | Grain Sales to Soviets COUP Cameroon | 40.88 | 4.00 | 37.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Willy Brandt [58] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], Willy Brandt[58], Our Man in Tehran[84], Terrorism[95], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Cameroon | 20.35 | 4.00 | 16.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 2 | Willy Brandt COUP Saharan States | 20.35 | 4.00 | 16.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 3 | Willy Brandt COUP SE African States | 20.35 | 4.00 | 16.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 4 | Terrorism COUP Cameroon | 20.35 | 4.00 | 16.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 5 | Terrorism COUP Saharan States | 20.35 | 4.00 | 16.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Summit [48] as COUP`
- flags: `milops_shortfall:10`
- hand: `Nasser[15], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Allende[57], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Cameroon | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:4.5 |
| 2 | Grain Sales to Soviets COUP Cameroon | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Summit INFLUENCE East Germany, West Germany, Venezuela | 41.45 | 6.00 | 51.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, control_break:Venezuela, non_coup_milops_penalty:16.00 |
| 4 | Kitchen Debates COUP Cameroon | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 5 | Summit COUP Saharan States | 27.90 | 4.00 | 24.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 147: T10 AR4 USSR

- chosen: `Terrorism [95] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], Our Man in Tehran[84], Terrorism[95], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Terrorism COUP Cameroon | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 2 | Terrorism COUP Saharan States | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 3 | Terrorism COUP SE African States | 21.05 | 4.00 | 17.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Terrorism COUP Guatemala | 20.30 | 4.00 | 16.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Terrorism COUP Haiti | 20.30 | 4.00 | 16.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], The Cambridge Five[36], Kitchen Debates[51], Allende[57], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Cameroon | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 2 | Kitchen Debates COUP Cameroon | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 3 | Grain Sales to Soviets INFLUENCE West Germany, Venezuela | 27.30 | 6.00 | 35.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Venezuela:13.70, control_break:Venezuela, non_coup_milops_penalty:14.00 |
| 4 | The Cambridge Five COUP Cameroon | 25.05 | 4.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nasser COUP Cameroon | 22.70 | 4.00 | 30.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `East European Unrest [29] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], East European Unrest[29], Our Man in Tehran[84], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Cameroon | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | East European Unrest COUP Saharan States | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | East European Unrest COUP SE African States | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | East European Unrest COUP Guatemala | 7.82 | 4.00 | 24.27 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | East European Unrest COUP Haiti | 7.82 | 4.00 | 24.27 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], The Cambridge Five[36], Kitchen Debates[51], Allende[57]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Cameroon | 35.87 | 4.00 | 32.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5 |
| 2 | The Cambridge Five COUP Cameroon | 26.22 | 4.00 | 38.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nasser COUP Cameroon | 23.87 | 4.00 | 32.02 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Cameroon | 23.87 | 4.00 | 32.02 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Kitchen Debates COUP Saharan States | 15.87 | 4.00 | 12.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Our Man in Tehran[84], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Saharan States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP SE African States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Solidarity COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Solidarity COUP Saharan States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], The Cambridge Five[36], Allende[57]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nasser COUP Cameroon | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Allende COUP Cameroon | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Saharan States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP SE African States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Solidarity [104] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity COUP Cameroon | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Solidarity COUP Saharan States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Solidarity COUP SE African States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Solidarity COUP Guatemala | 14.80 | 4.00 | 27.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Solidarity COUP Haiti | 14.80 | 4.00 | 27.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Allende[57]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Cameroon | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Allende COUP Cameroon | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Nasser COUP Saharan States | 13.20 | 4.00 | 21.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP SE African States | 13.20 | 4.00 | 21.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP Sudan | 13.20 | 4.00 | 21.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP -10, DEFCON +1, MilOps U-3/A-3`
