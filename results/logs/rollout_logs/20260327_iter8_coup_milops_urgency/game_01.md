# minimal_hybrid detailed rollout log

- seed: `20260530`
- winner: `US`
- final_vp: `-10`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Socialist Governments[7], Blockade[10], Captured Nazi Scientist[18], NATO[21], Decolonization[30], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Independent Reds [22] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Independent Reds[22], Indo-Pakistani War[24], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Blockade[10], Captured Nazi Scientist[18], NATO[21], Decolonization[30], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Blockade COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Captured Nazi Scientist COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | NATO COUP Iran | 58.35 | 4.00 | 78.95 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | Duck and Cover COUP Iran | 57.00 | 4.00 | 73.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | De-Stalinization INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 3 | Truman Doctrine COUP North Korea | 30.40 | 4.00 | 26.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 4 | UN Intervention COUP North Korea | 30.40 | 4.00 | 26.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |
| 5 | Indo-Pakistani War COUP North Korea | 30.25 | 4.00 | 26.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Captured Nazi Scientist[18], NATO[21], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, Japan, South Korea, Thailand | 57.20 | 6.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Duck and Cover INFLUENCE West Germany, Japan, Thailand | 43.80 | 6.00 | 58.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | NORAD INFLUENCE West Germany, Japan, Thailand | 43.80 | 6.00 | 58.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Blockade COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12], Nasser[15], Truman Doctrine[19], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Turkey, West Germany, North Korea | 39.60 | 6.00 | 55.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 2 | Truman Doctrine COUP North Korea | 30.50 | 4.00 | 26.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.20, coup_access_open |
| 3 | UN Intervention COUP North Korea | 30.50 | 4.00 | 26.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.20, coup_access_open |
| 4 | Fidel INFLUENCE West Germany, North Korea | 26.30 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Truman Doctrine INFLUENCE West Germany | 24.90 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Captured Nazi Scientist[18], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE North Korea, Pakistan, Thailand | 48.50 | 6.00 | 62.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | NORAD INFLUENCE North Korea, Pakistan, Thailand | 48.50 | 6.00 | 62.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Blockade COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Special Relationship INFLUENCE North Korea, Thailand | 35.70 | 6.00 | 46.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Romanian Abdication[12], Nasser[15], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Japan | 24.25 | 4.00 | 20.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 2 | UN Intervention COUP Japan | 24.25 | 4.00 | 20.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 3 | Truman Doctrine COUP North Korea | 23.65 | 4.00 | 19.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 4 | Truman Doctrine COUP South Korea | 23.65 | 4.00 | 19.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 5 | UN Intervention COUP North Korea | 23.65 | 4.00 | 19.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 9: T1 AR4 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE India, Pakistan, Thailand | 43.50 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE Pakistan, Thailand | 30.10 | 6.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 5 | Blockade COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Romanian Abdication[12], Nasser[15], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE East Germany, France | 23.80 | 6.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, offside_ops_penalty |
| 2 | UN Intervention INFLUENCE East Germany | 22.90 | 6.00 | 17.05 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.05, access_touch:East Germany |
| 3 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Romanian Abdication INFLUENCE East Germany | 10.90 | 6.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, offside_ops_penalty |
| 5 | Nasser INFLUENCE East Germany | 10.90 | 6.00 | 17.05 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, Thailand | 30.20 | 6.00 | 40.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Blockade COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `none`
- hand: `Romanian Abdication[12], Nasser[15], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Italy | 22.30 | 6.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy |
| 2 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 3 | Romanian Abdication INFLUENCE Italy | 10.30 | 6.00 | 16.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |
| 4 | Nasser INFLUENCE Italy | 10.30 | 6.00 | 16.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |
| 5 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china`
- hand: `Blockade[10], Captured Nazi Scientist[18]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Blockade COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade REALIGN Israel | 3.04 | -1.00 | 4.20 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 2 | Nasser INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 3 | Romanian Abdication COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Nasser COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 15: T2 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Korean War[11], Arab-Israeli War[13], COMECON[14], De Gaulle Leads France[17], Containment[25], CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Warsaw Pact Formed[16], Olympic Games[20], Marshall Plan[23], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Containment[25], CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, Israel, Thailand | 56.68 | 6.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | De Gaulle Leads France COUP Philippines | 44.25 | 4.00 | 40.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 3 | Korean War INFLUENCE Israel, Thailand | 40.38 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Arab-Israeli War INFLUENCE Israel, Thailand | 40.38 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 5 | Korean War COUP Philippines | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Warsaw Pact Formed[16], Olympic Games[20], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Italy, Japan, Egypt, Panama | 70.23 | 6.00 | 67.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 2 | Nuclear Test Ban INFLUENCE Italy, Japan, Egypt, Panama | 70.23 | 6.00 | 67.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 3 | Five Year Plan INFLUENCE Italy, Japan, Panama | 54.68 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 4 | US/Japan Mutual Defense Pact COUP Syria | 40.35 | 4.00 | 36.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 5 | Nuclear Test Ban COUP Syria | 40.35 | 4.00 | 36.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Korean War[11], Arab-Israeli War[13], Containment[25], CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Philippines, Thailand | 39.40 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Arab-Israeli War INFLUENCE Philippines, Thailand | 39.40 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 3 | Korean War COUP Philippines | 39.10 | 4.00 | 35.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 4 | Arab-Israeli War COUP Philippines | 39.10 | 4.00 | 35.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | Korean War COUP Egypt | 38.35 | 4.00 | 34.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Warsaw Pact Formed[16], Olympic Games[20], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Japan, Egypt, Libya, Philippines | 72.20 | 6.00 | 70.00 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.20 |
| 2 | Five Year Plan INFLUENCE Japan, Egypt, Philippines | 56.65 | 6.00 | 54.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.20 |
| 3 | Nuclear Test Ban COUP Philippines | 42.80 | 4.00 | 39.40 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:3.5 |
| 4 | Olympic Games INFLUENCE Egypt, Philippines | 40.65 | 6.00 | 38.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.20 |
| 5 | Nuclear Test Ban COUP Syria | 40.55 | 4.00 | 37.15 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Arab-Israeli War[13], Containment[25], CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Indonesia | 49.80 | 4.00 | 46.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Egypt | 38.65 | 4.00 | 34.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 3 | Arab-Israeli War INFLUENCE Saudi Arabia, Thailand | 38.45 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Containment COUP Indonesia | 35.15 | 4.00 | 51.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | East European Unrest COUP Indonesia | 35.15 | 4.00 | 51.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 22: T2 AR3 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Warsaw Pact Formed[16], Olympic Games[20], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Libya, Indonesia | 52.25 | 6.00 | 50.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Olympic Games INFLUENCE Japan, Libya | 36.55 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 3 | Five Year Plan COUP Syria | 35.50 | 4.00 | 31.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | Warsaw Pact Formed INFLUENCE Japan, Libya, Indonesia | 32.25 | 6.00 | 50.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Olympic Games COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Containment[25], CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Saudi Arabia, Indonesia, Thailand | 41.15 | 6.00 | 55.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, offside_ops_penalty |
| 2 | East European Unrest INFLUENCE Saudi Arabia, Indonesia, Thailand | 41.15 | 6.00 | 55.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE Indonesia, Thailand | 29.00 | 6.00 | 39.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, offside_ops_penalty |
| 4 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Warsaw Pact Formed[16], Olympic Games[20], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, Japan | 37.17 | 6.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:5.33 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, Japan, North Korea | 32.57 | 6.00 | 52.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Olympic Games COUP Syria | 30.65 | 4.00 | 26.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 4 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.17 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | The Cambridge Five INFLUENCE West Germany, Japan | 21.17 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `CIA Created[26], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Egypt, Thailand | 37.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 3 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | East European Unrest SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Warsaw Pact Formed[16], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Japan, Egypt | 27.05 | 6.00 | 55.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Warsaw Pact Formed COUP Syria | 17.00 | 4.00 | 33.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Vietnam Revolts INFLUENCE Japan, Egypt | 15.55 | 6.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Formosan Resolution COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Syria | 18.65 | 4.00 | 30.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Syria | 18.65 | 4.00 | 30.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Egypt | 14.15 | 4.00 | 26.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Egypt | 14.15 | 4.00 | 26.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Israel | 7.10 | 4.00 | 19.40 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A+0`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Nasser[15], Captured Nazi Scientist[18], Suez Crisis[28], Red Scare/Purge[31], UN Intervention[32], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], US/Japan Mutual Defense Pact[27], De-Stalinization[33]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Nasser[15], Captured Nazi Scientist[18], Suez Crisis[28], UN Intervention[32], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Japan, Libya, Thailand | 53.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Suez Crisis COUP Indonesia | 49.15 | 4.00 | 45.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 3 | Suez Crisis COUP Libya | 45.00 | 4.00 | 41.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | Fidel COUP Indonesia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 5 | Suez Crisis COUP Philippines | 38.75 | 4.00 | 35.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Five Year Plan [5] as COUP`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], De-Stalinization[33]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan COUP Indonesia | 49.15 | 4.00 | 45.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 2 | Containment COUP Indonesia | 49.15 | 4.00 | 45.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 3 | Indo-Pakistani War COUP Indonesia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 4 | Five Year Plan INFLUENCE Japan, Libya | 41.40 | 6.00 | 39.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 5 | Containment INFLUENCE Japan, Libya | 41.40 | 6.00 | 39.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 33: T3 AR2 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Nasser[15], Captured Nazi Scientist[18], UN Intervention[32], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | NORAD INFLUENCE Japan, Indonesia, Thailand | 33.20 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Fidel COUP Egypt | 25.95 | 4.00 | 22.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |
| 4 | Fidel COUP Libya | 25.95 | 4.00 | 22.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:1.5 |
| 5 | Nasser INFLUENCE Thailand | 21.50 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `none`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Libya | 40.40 | 6.00 | 34.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya |
| 2 | Indo-Pakistani War INFLUENCE Libya | 24.40 | 6.00 | 18.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Libya:13.70, control_break:Libya |
| 3 | Containment COUP Lebanon | 20.40 | 4.00 | 16.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5 |
| 4 | Warsaw Pact Formed INFLUENCE Japan, Libya | 20.40 | 6.00 | 34.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |
| 5 | De Gaulle Leads France INFLUENCE Japan, Libya | 20.40 | 6.00 | 34.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], UN Intervention[32], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Indonesia, Thailand | 32.00 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Nasser INFLUENCE Thailand | 20.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 20.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 4 | UN Intervention INFLUENCE Thailand | 20.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 5 | Special Relationship INFLUENCE Japan, Thailand | 20.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `none`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Indo-Pakistani War[24], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 3 | De Gaulle Leads France INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 4 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 5 | Indo-Pakistani War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Captured Nazi Scientist[18], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Egypt | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | Nasser COUP Libya | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Egypt | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Libya | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | UN Intervention COUP Egypt | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 38: T3 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], De-Stalinization[33]`
- state: `VP 1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Japan, Egypt | 22.40 | 6.00 | 36.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 2 | De Gaulle Leads France INFLUENCE Japan, Egypt | 22.40 | 6.00 | 36.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 3 | De-Stalinization INFLUENCE Japan, Egypt | 22.40 | 6.00 | 36.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 4 | Arab-Israeli War INFLUENCE Japan | 10.85 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 5 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 12.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:14.00 |
| 2 | UN Intervention INFLUENCE Thailand | 12.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:14.00 |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 12.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Captured Nazi Scientist COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], De-Stalinization[33]`
- state: `VP 1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 3 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | De Gaulle Leads France SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | De-Stalinization SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Sudan | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Special Relationship COUP Sudan | 4.80 | 4.00 | 17.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | UN Intervention INFLUENCE Thailand | 4.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:22.00 |
| 4 | Special Relationship INFLUENCE Japan, Thailand | 4.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 5 | UN Intervention COUP Tunisia | 4.05 | 4.00 | 0.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `De-Stalinization [33] as COUP`
- flags: `offside_ops_play`
- hand: `Arab-Israeli War[13], De-Stalinization[33]`
- state: `VP 1, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Sudan | 20.15 | 4.00 | 36.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Sudan | 18.80 | 4.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 4 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | De-Stalinization SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], NATO[21], CIA Created[26], Red Scare/Purge[31], UN Intervention[32], Nuclear Subs[44], Missile Envy[52], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Sadat Expels Soviets [73] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Decolonization[30], Special Relationship[37], We Will Bury You[53], OPEC[64], OAS Founded[71], Sadat Expels Soviets[73]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | We Will Bury You EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], NATO[21], CIA Created[26], UN Intervention[32], Nuclear Subs[44], Missile Envy[52], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE UK, Mexico, Algeria, Morocco | 42.93 | 6.00 | 66.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Vietnam Revolts INFLUENCE Mexico, Morocco | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 3 | Missile Envy INFLUENCE Mexico, Morocco | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 4 | Willy Brandt INFLUENCE Mexico, Morocco | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 5 | Vietnam Revolts COUP Egypt | 32.36 | 4.00 | 28.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Decolonization[30], Special Relationship[37], We Will Bury You[53], OPEC[64], OAS Founded[71]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Mexico | 34.11 | 4.00 | 30.41 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Special Relationship COUP Algeria | 33.36 | 4.00 | 29.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | We Will Bury You INFLUENCE Mexico, Ethiopia, South Africa | 31.18 | 6.00 | 54.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 4 | Captured Nazi Scientist COUP Mexico | 27.76 | 4.00 | 23.91 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | OAS Founded COUP Mexico | 27.76 | 4.00 | 23.91 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 47: T4 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], CIA Created[26], UN Intervention[32], Nuclear Subs[44], Missile Envy[52], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Mexico, Algeria | 36.52 | 6.00 | 36.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 2 | Missile Envy INFLUENCE Mexico, Algeria | 36.52 | 6.00 | 36.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 3 | Willy Brandt INFLUENCE Mexico, Algeria | 36.52 | 6.00 | 36.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 4 | Nuclear Subs INFLUENCE Mexico, Algeria | 20.52 | 6.00 | 36.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Nixon Plays the China Card INFLUENCE Mexico, Algeria | 20.52 | 6.00 | 36.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Decolonization[30], We Will Bury You[53], OPEC[64], OAS Founded[71]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE Algeria, Ethiopia, South Africa | 32.33 | 6.00 | 53.60 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Captured Nazi Scientist INFLUENCE Ethiopia | 23.78 | 6.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:2.67 |
| 3 | OAS Founded INFLUENCE Ethiopia | 23.78 | 6.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:2.67 |
| 4 | OPEC INFLUENCE Ethiopia, South Africa | 20.28 | 6.00 | 37.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Captured Nazi Scientist COUP Colombia | 12.20 | 4.00 | 8.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `CIA Created[26], UN Intervention[32], Nuclear Subs[44], Missile Envy[52], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE West Germany, Algeria | 34.65 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 2 | Willy Brandt INFLUENCE West Germany, Algeria | 34.65 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 3 | Missile Envy COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 4 | Willy Brandt COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 5 | Missile Envy COUP Guatemala | 18.70 | 4.00 | 15.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Decolonization[30], OPEC[64], OAS Founded[71]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | 24.45 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:3.20 |
| 2 | OAS Founded INFLUENCE South Africa | 24.45 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:3.20 |
| 3 | OPEC INFLUENCE Morocco, South Africa | 20.95 | 6.00 | 38.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Romanian Abdication INFLUENCE South Africa | 12.45 | 6.00 | 21.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Captured Nazi Scientist COUP Colombia | 12.40 | 4.00 | 8.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `CIA Created[26], UN Intervention[32], Nuclear Subs[44], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Willy Brandt COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Willy Brandt COUP Guatemala | 19.30 | 4.00 | 15.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | UN Intervention COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention INFLUENCE West Germany | 14.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `OAS Founded [71] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Decolonization[30], OPEC[64], OAS Founded[71]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded INFLUENCE Morocco | 18.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 2 | OPEC INFLUENCE Morocco, South Africa | 15.15 | 6.00 | 33.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | OAS Founded COUP Colombia | 12.70 | 4.00 | 8.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP Saharan States | 12.70 | 4.00 | 8.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP SE African States | 12.70 | 4.00 | 8.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `CIA Created[26], UN Intervention[32], Nuclear Subs[44], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Guatemala | 13.95 | 4.00 | 10.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention INFLUENCE West Germany | 11.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.67 |
| 4 | Nuclear Subs INFLUENCE East Germany, West Germany | 10.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 10.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 54: T4 AR5 US

- chosen: `OPEC [64] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30], OPEC[64]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Saharan States | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Decolonization COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | OPEC INFLUENCE West Germany, South Africa | 13.17 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Romanian Abdication INFLUENCE South Africa | 5.32 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 55: T4 AR6 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Nuclear Subs[44], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Saharan States | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Nuclear Subs COUP Guatemala | 4.80 | 4.00 | 17.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Guatemala | 4.80 | 4.00 | 17.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 56: T4 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30]`
- state: `VP 0, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Saharan States | 24.05 | 4.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Saharan States | 22.70 | 4.00 | 30.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE South Africa | 3.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Decolonization COUP Colombia | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP SE African States | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | CIA Created COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | CIA Created COUP Guatemala | 3.95 | 4.00 | 12.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | -0.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Romanian Abdication[12]`
- state: `VP 0, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Nigeria | 3.45 | 6.00 | 20.60 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | Romanian Abdication COUP Colombia | 2.20 | 4.00 | 10.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Saharan States | 2.20 | 4.00 | 10.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP SE African States | 2.20 | 4.00 | 10.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Sudan | 2.20 | 4.00 | 10.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 59: T5 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], Korean War[11], De Gaulle Leads France[17], Captured Nazi Scientist[18], Formosan Resolution[35], The Cambridge Five[36], Allende[57], Cultural Revolution[61]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Duck and Cover[4], De Gaulle Leads France[17], Olympic Games[20], Nuclear Test Ban[34], Brush War[39], SALT Negotiations[46], Our Man in Tehran[84], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], Korean War[11], Captured Nazi Scientist[18], Formosan Resolution[35], The Cambridge Five[36], Allende[57], Cultural Revolution[61]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 52.09 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 2 | Cultural Revolution COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 3 | Cultural Revolution COUP Indonesia | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:4.5 |
| 4 | Cultural Revolution COUP Egypt | 45.14 | 4.00 | 41.59 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 5 | Cultural Revolution COUP Turkey | 44.89 | 4.00 | 41.34 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Turkey, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Duck and Cover[4], De Gaulle Leads France[17], Olympic Games[20], Brush War[39], SALT Negotiations[46], Our Man in Tehran[84], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE France, West Germany, South Africa | 50.34 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | SALT Negotiations INFLUENCE France, West Germany, South Africa | 50.34 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Duck and Cover COUP Indonesia | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:4.5 |
| 4 | SALT Negotiations COUP Indonesia | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:4.5 |
| 5 | Olympic Games COUP Indonesia | 41.69 | 4.00 | 37.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], Korean War[11], Captured Nazi Scientist[18], Formosan Resolution[35], The Cambridge Five[36], Allende[57]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Saharan States | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 2 | Korean War COUP Indonesia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.83, expected_swing:3.5 |
| 3 | The Cambridge Five COUP Saharan States | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Indonesia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.83, expected_swing:3.5 |
| 5 | Korean War COUP Egypt | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 64: T5 AR2 US

- chosen: `SALT Negotiations [46] as COUP`
- flags: `milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Olympic Games[20], Brush War[39], SALT Negotiations[46], Our Man in Tehran[84], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 5, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations COUP Saharan States | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 2 | SALT Negotiations COUP Indonesia | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.83, expected_swing:4.5 |
| 3 | SALT Negotiations INFLUENCE East Germany, West Germany, South Africa | 47.38 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 4 | Olympic Games COUP Saharan States | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 5 | Olympic Games COUP Indonesia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.83, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 65: T5 AR3 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], Formosan Resolution[35], The Cambridge Five[36], Allende[57]`
- state: `VP -1, DEFCON 5, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Saharan States | 41.35 | 4.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 2 | The Cambridge Five COUP Indonesia | 41.35 | 4.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:3.5 |
| 3 | The Cambridge Five COUP Egypt | 38.45 | 4.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |
| 4 | The Cambridge Five COUP Turkey | 38.20 | 4.00 | 34.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Turkey, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |
| 5 | The Cambridge Five INFLUENCE France, West Germany | 37.60 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:2`
- hand: `De Gaulle Leads France[17], Olympic Games[20], Brush War[39], Our Man in Tehran[84], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 5, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:3.5 |
| 2 | Our Man in Tehran COUP Indonesia | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:3.5 |
| 3 | Olympic Games INFLUENCE West Germany, South Africa | 35.45 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:3.20 |
| 4 | Our Man in Tehran INFLUENCE West Germany, South Africa | 35.45 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:3.20 |
| 5 | Panama Canal Returned COUP Indonesia | 34.40 | 4.00 | 30.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], Formosan Resolution[35], Allende[57]`
- state: `VP -1, DEFCON 4, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Indonesia | 42.45 | 4.00 | 38.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Indonesia | 42.45 | 4.00 | 38.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 3 | Allende COUP Indonesia | 42.45 | 4.00 | 38.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 4 | Five Year Plan COUP Indonesia | 35.15 | 4.00 | 51.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Indonesia | 32.80 | 4.00 | 45.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `De Gaulle Leads France[17], Brush War[39], Our Man in Tehran[84], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE West Germany, South Africa | 34.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 30.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Brush War INFLUENCE East Germany, West Germany, South Africa | 30.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Our Man in Tehran COUP Mexico | 26.90 | 4.00 | 23.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 5 | Our Man in Tehran COUP Algeria | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Formosan Resolution[35], Allende[57]`
- state: `VP -1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 29.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Captured Nazi Scientist COUP Egypt | 27.30 | 4.00 | 23.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Allende COUP Egypt | 27.30 | 4.00 | 23.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Mexico | 22.05 | 4.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Allende COUP Mexico | 22.05 | 4.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `De Gaulle Leads France[17], Brush War[39], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 28.72 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Brush War INFLUENCE East Germany, West Germany, South Africa | 28.72 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Panama Canal Returned COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 4 | Panama Canal Returned COUP Algeria | 20.30 | 4.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |
| 5 | Panama Canal Returned COUP Libya | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35], Allende[57]`
- state: `VP -1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Egypt | 28.80 | 4.00 | 24.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Allende COUP Egypt | 28.80 | 4.00 | 24.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Mexico | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 4 | Allende COUP Mexico | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Algeria | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Brush War[39], Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, West Germany, South Africa | 20.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Panama Canal Returned COUP Colombia | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP SE African States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Formosan Resolution[35], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Allende COUP Guatemala | 18.95 | 4.00 | 15.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Formosan Resolution COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Allende COUP Tunisia | 9.80 | 4.00 | 5.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:0.5 |
| 5 | Formosan Resolution COUP Guatemala | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:2`
- hand: `Lone Gunman[109], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Lone Gunman COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 75: T6 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Warsaw Pact Formed[16], Truman Doctrine[19], Indo-Pakistani War[24], Red Scare/Purge[31], De-Stalinization[33], Bear Trap[47], Summit[48], South African Unrest[56]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Arab-Israeli War[13], Nasser[15], Suez Crisis[28], NORAD[38], Arms Race[42], Quagmire[45], Flower Power[62], Camp David Accords[66], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Warsaw Pact Formed[16], Truman Doctrine[19], Indo-Pakistani War[24], De-Stalinization[33], Bear Trap[47], Summit[48], South African Unrest[56]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Warsaw Pact Formed COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 3 | De-Stalinization COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 4 | Summit COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 5 | Socialist Governments INFLUENCE East Germany, France, West Germany | 45.94 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 78: T6 AR1 US

- chosen: `Arms Race [42] as COUP`
- flags: `milops_shortfall:6`
- hand: `Arab-Israeli War[13], Nasser[15], Suez Crisis[28], Arms Race[42], Quagmire[45], Flower Power[62], Camp David Accords[66], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Camp David Accords COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 3 | One Small Step COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 4 | Arms Race COUP Mexico | 34.32 | 4.00 | 30.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:2.5 |
| 5 | Arms Race COUP Algeria | 33.57 | 4.00 | 30.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 79: T6 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Warsaw Pact Formed[16], Truman Doctrine[19], Indo-Pakistani War[24], De-Stalinization[33], Bear Trap[47], Summit[48], South African Unrest[56]`
- state: `VP -1, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed COUP Nigeria | 49.90 | 4.00 | 46.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | De-Stalinization COUP Nigeria | 49.90 | 4.00 | 46.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 3 | Summit COUP Nigeria | 49.90 | 4.00 | 46.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 4 | Warsaw Pact Formed INFLUENCE East Germany, West Germany, Nigeria | 48.85 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, access_touch:Nigeria, non_coup_milops_penalty:4.00 |
| 5 | De-Stalinization INFLUENCE East Germany, West Germany, Nigeria | 48.85 | 6.00 | 47.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, access_touch:Nigeria, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:3`
- hand: `Arab-Israeli War[13], Nasser[15], Suez Crisis[28], Quagmire[45], Flower Power[62], Camp David Accords[66], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | Suez Crisis COUP Saharan States | 27.40 | 4.00 | 43.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP Saharan States | 27.40 | 4.00 | 43.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Saharan States | 25.05 | 4.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Truman Doctrine[19], Indo-Pakistani War[24], De-Stalinization[33], Bear Trap[47], Summit[48], South African Unrest[56]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 48.00 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 2 | Summit INFLUENCE East Germany, France, West Germany | 48.00 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 3 | De-Stalinization COUP Saharan States | 47.70 | 4.00 | 44.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5 |
| 4 | Summit COUP Saharan States | 47.70 | 4.00 | 44.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5 |
| 5 | Indo-Pakistani War COUP Saharan States | 41.35 | 4.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:3`
- hand: `Arab-Israeli War[13], Nasser[15], Suez Crisis[28], Quagmire[45], Flower Power[62], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Colombia | 19.35 | 4.00 | 15.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 19.35 | 4.00 | 15.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 3 | One Small Step COUP SE African States | 19.35 | 4.00 | 15.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Sudan | 19.35 | 4.00 | 15.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Zimbabwe | 19.35 | 4.00 | 15.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Summit [48] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Truman Doctrine[19], Indo-Pakistani War[24], Bear Trap[47], Summit[48], South African Unrest[56]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Saharan States | 48.15 | 4.00 | 44.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5 |
| 2 | Summit INFLUENCE East Germany, France, West Germany | 46.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Indo-Pakistani War COUP Saharan States | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 4 | South African Unrest COUP Saharan States | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 5 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 31.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Suez Crisis [28] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Suez Crisis[28], Quagmire[45], Flower Power[62]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Saharan States | 28.15 | 4.00 | 44.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Quagmire COUP Saharan States | 28.15 | 4.00 | 44.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Saharan States | 25.80 | 4.00 | 38.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Saharan States | 25.80 | 4.00 | 38.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nasser COUP Saharan States | 23.45 | 4.00 | 31.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Truman Doctrine[19], Indo-Pakistani War[24], Bear Trap[47], South African Unrest[56]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | South African Unrest COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Bear Trap COUP Saharan States | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Quagmire[45], Flower Power[62]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE Brazil, South Africa | 10.55 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Quagmire COUP Colombia | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP SE African States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Sudan | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `South African Unrest [56] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Truman Doctrine[19], Bear Trap[47], South African Unrest[56]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Cameroon | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | South African Unrest COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | South African Unrest COUP Guatemala | 20.80 | 4.00 | 17.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 16.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:21.00 |
| 5 | Bear Trap INFLUENCE East Germany, France, West Germany | 11.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Flower Power[62]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Colombia | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Saharan States | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP SE African States | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Sudan | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Zimbabwe | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Bear Trap [47] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], Bear Trap[47]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Cameroon | 12.90 | 4.00 | 29.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Bear Trap COUP Saharan States | 12.90 | 4.00 | 29.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Bear Trap COUP Guatemala | 11.65 | 4.00 | 28.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Cameroon | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Saharan States | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Flower Power[62]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Colombia | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Flower Power COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Flower Power COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Sudan | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Zimbabwe | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 91: T7 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Warsaw Pact Formed[16], Containment[25], East European Unrest[29], De-Stalinization[33], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], UN Intervention[32], NORAD[38], Brezhnev Doctrine[54], Muslim Revolution[59], U2 Incident[63], Che[83], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 4 | Brezhnev Doctrine EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | U2 Incident EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Containment[25], East European Unrest[29], De-Stalinization[33], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, Congo/Zaire | 45.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 2 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Congo/Zaire | 45.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, non_coup_milops_penalty:8.00 |
| 3 | De-Stalinization COUP Egypt | 40.00 | 4.00 | 36.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Cuban Missile Crisis COUP Egypt | 40.00 | 4.00 | 36.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | De-Stalinization COUP Mexico | 34.75 | 4.00 | 31.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], UN Intervention[32], Brezhnev Doctrine[54], Muslim Revolution[59], U2 Incident[63], Che[83], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, Argentina, Brazil, South Africa | 45.15 | 6.00 | 71.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, Argentina, Brazil | 32.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | U2 Incident INFLUENCE East Germany, Argentina, Brazil | 32.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Che INFLUENCE East Germany, Argentina, Brazil | 32.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, access_touch:East Germany, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | UN Intervention COUP Mexico | 22.05 | 4.00 | 18.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Containment[25], East European Unrest[29], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE West Germany, Angola, Congo/Zaire | 54.17 | 6.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:9.33 |
| 2 | Cuban Missile Crisis COUP Egypt | 40.50 | 4.00 | 36.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | How I Learned to Stop Worrying INFLUENCE Angola, Congo/Zaire | 38.17 | 6.00 | 41.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, non_coup_milops_penalty:9.33 |
| 4 | Cuban Missile Crisis COUP Mexico | 35.25 | 4.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |
| 5 | Cuban Missile Crisis COUP Algeria | 34.50 | 4.00 | 30.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], UN Intervention[32], Brezhnev Doctrine[54], U2 Incident[63], Che[83], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE Argentina, Chile, South Africa | 33.02 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 2 | U2 Incident INFLUENCE Argentina, Chile, South Africa | 33.02 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 3 | Che INFLUENCE Argentina, Chile, South Africa | 33.02 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | UN Intervention COUP Mexico | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:0.5 |
| 5 | UN Intervention COUP Algeria | 21.80 | 4.00 | 17.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nasser[15], Containment[25], East European Unrest[29], How I Learned to Stop Worrying[49], Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Egypt | 34.85 | 4.00 | 31.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | How I Learned to Stop Worrying COUP Mexico | 29.60 | 4.00 | 25.90 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 3 | How I Learned to Stop Worrying COUP Algeria | 28.85 | 4.00 | 25.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 4 | Nasser COUP Egypt | 28.50 | 4.00 | 24.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | How I Learned to Stop Worrying COUP Libya | 27.85 | 4.00 | 24.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 98: T7 AR3 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], UN Intervention[32], U2 Incident[63], Che[83], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE Argentina, Chile, South Africa | 24.15 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 2 | Che INFLUENCE Argentina, Chile, South Africa | 24.15 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | UN Intervention COUP Colombia | 15.40 | 4.00 | 11.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Saharan States | 15.40 | 4.00 | 11.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP SE African States | 15.40 | 4.00 | 11.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Nasser[15], Containment[25], East European Unrest[29], Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, West Germany, Angola | 22.85 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | East European Unrest INFLUENCE East Germany, West Germany, Angola | 22.85 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Nasser COUP Cameroon | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 4 | Nasser COUP Saharan States | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nasser COUP SE African States | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], UN Intervention[32], Che[83], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE Argentina, Chile, South Africa | 26.35 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | UN Intervention COUP Colombia | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP Saharan States | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP SE African States | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Sudan | 16.45 | 4.00 | 12.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Nasser[15], East European Unrest[29], Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, West Germany, Angola | 19.52 | 6.00 | 47.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Nasser COUP Cameroon | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Nasser COUP Saharan States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Nasser COUP SE African States | 16.20 | 4.00 | 12.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nasser COUP Guatemala | 14.95 | 4.00 | 11.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:7`
- hand: `Fidel[8], Arab-Israeli War[13], UN Intervention[32], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Colombia | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Sudan | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Zimbabwe | 18.20 | 4.00 | 14.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 103: T7 AR6 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Nasser[15], Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Cameroon | 18.70 | 4.00 | 14.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Nasser COUP Saharan States | 18.70 | 4.00 | 14.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Nasser COUP SE African States | 18.70 | 4.00 | 14.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Nasser COUP Guatemala | 17.45 | 4.00 | 13.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lonely Hearts Club Band COUP Cameroon | 9.05 | 4.00 | 21.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Colombia | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Fidel COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Fidel COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Fidel COUP Sudan | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Fidel COUP Zimbabwe | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 105: T7 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Cameroon | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Lonely Hearts Club Band COUP Saharan States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP SE African States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP Cameroon | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope COUP Saharan States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Colombia | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Saharan States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP SE African States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Sudan | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Zimbabwe | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 107: T8 AR0 USSR

- chosen: `Cultural Revolution [61] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], UN Intervention[32], Formosan Resolution[35], South African Unrest[56], Cultural Revolution[61], OPEC[64], Liberation Theology[76], The Reformer[90], Solidarity[104]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | The Reformer EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `North Sea Oil [89] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Romanian Abdication[12], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], De-Stalinization[33], The Cambridge Five[36], Lonely Hearts Club Band[65], One Small Step[81], North Sea Oil[89]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], UN Intervention[32], Formosan Resolution[35], South African Unrest[56], OPEC[64], Liberation Theology[76], The Reformer[90], Solidarity[104]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | The Reformer INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | OPEC COUP Egypt | 40.18 | 4.00 | 36.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | The Reformer COUP Egypt | 40.18 | 4.00 | 36.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | OPEC COUP Algeria | 34.43 | 4.00 | 30.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Romanian Abdication[12], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], De-Stalinization[33], The Cambridge Five[36], Lonely Hearts Club Band[65], One Small Step[81]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE West Germany, South Korea | 32.01 | 6.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:South Korea:13.55, control_break:South Korea, non_coup_milops_penalty:9.14 |
| 2 | One Small Step INFLUENCE West Germany, South Korea | 32.01 | 6.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:South Korea:13.55, control_break:South Korea, non_coup_milops_penalty:9.14 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, South Korea | 28.16 | 6.00 | 51.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:South Korea:13.55, control_break:South Korea, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 4 | Lonely Hearts Club Band COUP Algeria | 28.08 | 4.00 | 24.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:1.5 |
| 5 | One Small Step COUP Algeria | 28.08 | 4.00 | 24.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `The Reformer [90] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], UN Intervention[32], Formosan Resolution[35], South African Unrest[56], Liberation Theology[76], The Reformer[90], Solidarity[104]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer INFLUENCE East Germany, France, West Germany | 44.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | The Reformer COUP Egypt | 40.75 | 4.00 | 37.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | The Reformer COUP Algeria | 35.00 | 4.00 | 31.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |
| 4 | South African Unrest COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Liberation Theology COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:8`
- hand: `Romanian Abdication[12], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], De-Stalinization[33], The Cambridge Five[36], One Small Step[81]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Algeria | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 2 | One Small Step INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | One Small Step COUP Mexico | 27.90 | 4.00 | 24.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 4 | One Small Step COUP Libya | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 5 | De-Stalinization INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 113: T8 AR3 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], UN Intervention[32], Formosan Resolution[35], South African Unrest[56], Liberation Theology[76], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | South African Unrest COUP Cameroon | 22.35 | 4.00 | 18.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:3.5 |
| 4 | South African Unrest COUP Saharan States | 22.35 | 4.00 | 18.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | South African Unrest COUP SE African States | 22.35 | 4.00 | 18.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:1.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 25.45 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Captured Nazi Scientist COUP Saharan States | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP SE African States | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Sudan | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Zimbabwe | 14.80 | 4.00 | 10.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Liberation Theology [76] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Blockade[10], UN Intervention[32], Formosan Resolution[35], Liberation Theology[76], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Cameroon | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Liberation Theology COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Liberation Theology COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Liberation Theology INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | Liberation Theology COUP Guatemala | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 116: T8 AR4 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP SE African States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Sudan | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Zimbabwe | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Saharan States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], UN Intervention[32], Formosan Resolution[35], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:6`
- hand: `Romanian Abdication[12], Nasser[15], CIA Created[26], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | CIA Created COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | CIA Created COUP Sudan | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | CIA Created COUP Zimbabwe | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Colombia | 16.70 | 4.00 | 12.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], Formosan Resolution[35], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Formosan Resolution COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Solidarity COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | UN Intervention COUP Cameroon | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP SE African States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Sudan | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Zimbabwe | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Colombia | 10.05 | 4.00 | 22.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Formosan Resolution[35], Solidarity[104]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Solidarity COUP Saharan States | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Cameroon | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Solidarity COUP Cameroon | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Saharan States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP SE African States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Sudan | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Zimbabwe | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP Saharan States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 123: T8 AR7 US

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Saharan States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Nasser COUP SE African States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Nasser COUP Sudan | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP Zimbabwe | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP Colombia | 16.70 | 4.00 | 24.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 124: T9 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Truman Doctrine[19], Nuclear Test Ban[34], Formosan Resolution[35], Nuclear Subs[44], Quagmire[45], Camp David Accords[66], John Paul II Elected Pope[69], Iran-Iraq War[105]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |
| 5 | Nuclear Subs EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR0 US

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], SALT Negotiations[46], How I Learned to Stop Worrying[49], Missile Envy[52], Voice of America[75], Ask Not What Your Country Can Do For You[78], Pershing II Deployed[102], Defectors[108]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 126: T9 AR1 USSR

- chosen: `Quagmire [45] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Truman Doctrine[19], Formosan Resolution[35], Nuclear Subs[44], Quagmire[45], Camp David Accords[66], John Paul II Elected Pope[69], Iran-Iraq War[105]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Indonesia | 56.01 | 4.00 | 52.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Quagmire COUP Saharan States | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | Iran-Iraq War COUP Indonesia | 49.66 | 4.00 | 45.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Quagmire COUP Turkey | 47.36 | 4.00 | 43.81 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Turkey, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |
| 5 | Quagmire COUP Egypt | 46.61 | 4.00 | 43.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 127: T9 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as COUP`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], How I Learned to Stop Worrying[49], Missile Envy[52], Voice of America[75], Ask Not What Your Country Can Do For You[78], Pershing II Deployed[102], Solidarity[104], Defectors[108]`
- state: `VP 1, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You COUP Nigeria | 58.26 | 4.00 | 54.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Ask Not What Your Country Can Do For You COUP Indonesia | 56.01 | 4.00 | 52.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | How I Learned to Stop Worrying COUP Nigeria | 51.91 | 4.00 | 48.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Missile Envy COUP Nigeria | 51.91 | 4.00 | 48.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 5 | Voice of America COUP Nigeria | 51.91 | 4.00 | 48.21 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 128: T9 AR2 USSR

- chosen: `Iran-Iraq War [105] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Truman Doctrine[19], Formosan Resolution[35], Nuclear Subs[44], Camp David Accords[66], John Paul II Elected Pope[69], Iran-Iraq War[105]`
- state: `VP 1, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Iran-Iraq War INFLUENCE West Germany, Nigeria | 35.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 3 | Iran-Iraq War COUP Egypt | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Iran-Iraq War COUP Algeria | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Iran-Iraq War COUP Mexico | 26.90 | 4.00 | 23.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR2 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], How I Learned to Stop Worrying[49], Missile Envy[52], Voice of America[75], Pershing II Deployed[102], Solidarity[104], Defectors[108]`
- state: `VP 1, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE West Germany, Nigeria | 35.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 2 | Missile Envy INFLUENCE West Germany, Nigeria | 35.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 3 | Voice of America INFLUENCE West Germany, Nigeria | 35.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 4 | Solidarity INFLUENCE West Germany, Nigeria | 35.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |
| 5 | Defectors INFLUENCE West Germany, Nigeria | 35.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35], Nuclear Subs[44], Camp David Accords[66], John Paul II Elected Pope[69]`
- state: `VP 1, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Nigeria | 29.65 | 4.00 | 41.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Nigeria | 29.65 | 4.00 | 41.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Camp David Accords COUP Nigeria | 29.65 | 4.00 | 41.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP Nigeria | 29.65 | 4.00 | 41.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Nigeria | 27.30 | 4.00 | 35.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 131: T9 AR3 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Missile Envy[52], Voice of America[75], Pershing II Deployed[102], Solidarity[104], Defectors[108]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 34.30 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | 34.30 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 3 | Solidarity INFLUENCE East Germany, West Germany | 34.30 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 4 | Defectors INFLUENCE East Germany, West Germany | 34.30 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 5 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 30.45 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Nuclear Subs[44], Camp David Accords[66], John Paul II Elected Pope[69]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Camp David Accords COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Nuclear Subs INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR4 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Voice of America[75], Pershing II Deployed[102], Solidarity[104], Defectors[108]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Solidarity INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Defectors INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 23.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Voice of America COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 USSR

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Camp David Accords[66], John Paul II Elected Pope[69]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Camp David Accords COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Camp David Accords COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR5 US

- chosen: `Solidarity [104] as COUP`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Pershing II Deployed[102], Solidarity[104], Defectors[108]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Defectors COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Pershing II Deployed COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Fidel COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Solidarity COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 USSR

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], John Paul II Elected Pope[69]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Saharan States | 30.20 | 4.00 | 38.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope COUP Cameroon | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope COUP Guatemala | 9.80 | 4.00 | 22.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR6 US

- chosen: `Defectors [108] as COUP`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Pershing II Deployed[102], Defectors[108]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Defectors COUP Saharan States | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Defectors COUP SE African States | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Defectors COUP Sudan | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Defectors COUP Zimbabwe | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Defectors COUP Colombia | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Saharan States | 39.20 | 4.00 | 47.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Cameroon | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP SE African States | 17.20 | 4.00 | 25.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Guatemala | 16.45 | 4.00 | 24.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Botswana | 6.80 | 4.00 | 14.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Botswana, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 139: T9 AR7 US

- chosen: `Pershing II Deployed [102] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Fidel[8], Pershing II Deployed[102]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed COUP Saharan States | 21.90 | 4.00 | 38.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Pershing II Deployed COUP SE African States | 21.90 | 4.00 | 38.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Pershing II Deployed COUP Sudan | 21.90 | 4.00 | 38.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Pershing II Deployed COUP Zimbabwe | 21.90 | 4.00 | 38.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Pershing II Deployed COUP Colombia | 21.40 | 4.00 | 37.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 140: T10 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Warsaw Pact Formed[16], Brush War[39], Willy Brandt[58], ABM Treaty[60], U2 Incident[63], Nixon Plays the China Card[72], Our Man in Tehran[84], Star Wars[88], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Five Year Plan[5], Suez Crisis[28], Cuban Missile Crisis[43], Junta[50], Allende[57], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Tear Down this Wall EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 142: T10 AR1 USSR

- chosen: `Warsaw Pact Formed [16] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Warsaw Pact Formed[16], Willy Brandt[58], U2 Incident[63], Nixon Plays the China Card[72], Our Man in Tehran[84], Star Wars[88], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed COUP Saharan States | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | U2 Incident COUP Saharan States | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | Warsaw Pact Formed COUP Egypt | 47.04 | 4.00 | 43.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |
| 4 | U2 Incident COUP Egypt | 47.04 | 4.00 | 43.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |
| 5 | Willy Brandt COUP Saharan States | 43.84 | 4.00 | 40.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 143: T10 AR1 US

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `milops_shortfall:10`
- hand: `Suez Crisis[28], Cuban Missile Crisis[43], Junta[50], Allende[57], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Indonesia | 56.44 | 4.00 | 52.89 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Tear Down this Wall COUP Indonesia | 56.44 | 4.00 | 52.89 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | Cuban Missile Crisis COUP Saharan States | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 4 | Tear Down this Wall COUP Saharan States | 50.19 | 4.00 | 46.64 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 5 | Junta COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 144: T10 AR2 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Willy Brandt[58], U2 Incident[63], Nixon Plays the China Card[72], Our Man in Tehran[84], Star Wars[88], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, West Germany, Indonesia | 47.77 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Indonesia:11.35, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:9.33 |
| 2 | U2 Incident COUP Egypt | 40.25 | 4.00 | 36.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | U2 Incident COUP Algeria | 34.50 | 4.00 | 30.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |
| 4 | Willy Brandt COUP Egypt | 33.90 | 4.00 | 30.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Colonial Rear Guards COUP Egypt | 33.90 | 4.00 | 30.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR2 US

- chosen: `Tear Down this Wall [99] as COUP`
- flags: `milops_shortfall:7`
- hand: `Suez Crisis[28], Junta[50], Allende[57], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Tear Down this Wall[99], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall COUP Saharan States | 49.40 | 4.00 | 45.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 2 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 45.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 3 | Junta COUP Saharan States | 43.05 | 4.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 4 | Panama Canal Returned COUP Saharan States | 36.70 | 4.00 | 32.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 5 | Tear Down this Wall COUP Algeria | 34.50 | 4.00 | 30.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 USSR

- chosen: `Willy Brandt [58] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Willy Brandt[58], Nixon Plays the China Card[72], Our Man in Tehran[84], Star Wars[88], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Saharan States | 43.75 | 4.00 | 40.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 2 | Colonial Rear Guards COUP Saharan States | 43.75 | 4.00 | 40.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 3 | Willy Brandt COUP Egypt | 34.60 | 4.00 | 30.90 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Colonial Rear Guards COUP Egypt | 34.60 | 4.00 | 30.90 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Willy Brandt COUP Algeria | 28.85 | 4.00 | 25.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR3 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:7`
- hand: `Suez Crisis[28], Junta[50], Allende[57], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Nigeria | 46.25 | 4.00 | 42.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Panama Canal Returned COUP Nigeria | 39.90 | 4.00 | 36.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Suez Crisis COUP Nigeria | 32.60 | 4.00 | 49.05 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Marine Barracks Bombing COUP Nigeria | 30.25 | 4.00 | 42.55 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Ortega Elected in Nicaragua COUP Nigeria | 30.25 | 4.00 | 42.55 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 148: T10 AR4 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Nixon Plays the China Card[72], Our Man in Tehran[84], Star Wars[88], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Saharan States | 44.80 | 4.00 | 41.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 2 | Nixon Plays the China Card COUP Saharan States | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Saharan States | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Star Wars COUP Saharan States | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 24.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR4 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:7`
- hand: `Suez Crisis[28], Allende[57], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Cameroon | 38.45 | 4.00 | 34.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Saharan States | 38.45 | 4.00 | 34.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:2.5 |
| 3 | Suez Crisis COUP Cameroon | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Suez Crisis COUP Saharan States | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Marine Barracks Bombing COUP Cameroon | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Nixon Plays the China Card[72], Our Man in Tehran[84], Star Wars[88]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP SE African States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Cameroon | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Saharan States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR5 US

- chosen: `Suez Crisis [28] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Suez Crisis[28], Allende[57], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Cameroon | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Suez Crisis COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Marine Barracks Bombing COUP Cameroon | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Marine Barracks Bombing COUP Saharan States | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Ortega Elected in Nicaragua COUP Cameroon | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Our Man in Tehran[84], Star Wars[88]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Cameroon | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Saharan States | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP SE African States | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Star Wars COUP Cameroon | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Star Wars COUP Saharan States | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR6 US

- chosen: `Marine Barracks Bombing [91] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Allende[57], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing COUP Cameroon | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Marine Barracks Bombing COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Ortega Elected in Nicaragua COUP Cameroon | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Ortega Elected in Nicaragua COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Allende COUP Cameroon | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 USSR

- chosen: `Star Wars [88] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Star Wars[88]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars COUP Cameroon | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Star Wars COUP Saharan States | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Star Wars COUP SE African States | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Star Wars COUP Guatemala | 21.80 | 4.00 | 34.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Star Wars COUP Botswana | 12.15 | 4.00 | 24.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Botswana, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 155: T10 AR7 US

- chosen: `Ortega Elected in Nicaragua [94] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Allende[57], Ortega Elected in Nicaragua[94]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ortega Elected in Nicaragua COUP Cameroon | 44.55 | 4.00 | 56.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Ortega Elected in Nicaragua COUP Saharan States | 44.55 | 4.00 | 56.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Cameroon | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Saharan States | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Ortega Elected in Nicaragua COUP SE African States | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -12, DEFCON +1, MilOps U-3/A-3`
