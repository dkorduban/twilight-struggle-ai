# minimal_hybrid detailed rollout log

- seed: `20260403`
- winner: `US`
- final_vp: `-16`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Vietnam Revolts [9] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | East European Unrest EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Blockade[10], Korean War[11], NATO[21], Suez Crisis[28], Decolonization[30], Red Scare/Purge[31], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Iran | 71.82 | 4.00 | 68.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Captured Nazi Scientist COUP Iran | 66.47 | 4.00 | 62.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Olympic Games INFLUENCE West Germany, Japan, Thailand | 61.62 | 5.00 | 58.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |
| 4 | Five Year Plan INFLUENCE West Germany, Japan, South Korea, Thailand | 59.02 | 5.00 | 75.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | East European Unrest INFLUENCE West Germany, Japan, South Korea, Thailand | 59.02 | 5.00 | 75.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Blockade[10], Korean War[11], Suez Crisis[28], Decolonization[30], Red Scare/Purge[31], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE North Korea, Iran, Indonesia, Philippines | 79.62 | 5.00 | 76.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Duck and Cover INFLUENCE Iran, Indonesia, Philippines | 62.22 | 5.00 | 59.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Suez Crisis INFLUENCE Iran, Indonesia, Philippines | 42.22 | 5.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | De-Stalinization INFLUENCE Iran, Indonesia, Philippines | 42.22 | 5.00 | 59.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Red Scare/Purge COUP Syria | 39.02 | 4.00 | 35.62 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Truman Doctrine[19], Independent Reds[22], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Iran | 64.80 | 4.00 | 60.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 2 | Five Year Plan INFLUENCE West Germany, Japan, North Korea, Thailand | 63.35 | 5.00 | 78.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | East European Unrest INFLUENCE West Germany, Japan, North Korea, Thailand | 63.35 | 5.00 | 78.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Five Year Plan COUP Iran | 55.50 | 4.00 | 71.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | East European Unrest COUP Iran | 55.50 | 4.00 | 71.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Blockade[10], Korean War[11], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, Turkey | 54.50 | 5.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, non_coup_milops_penalty:1.60 |
| 2 | Suez Crisis INFLUENCE East Germany, France, Turkey | 34.50 | 5.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | De-Stalinization INFLUENCE East Germany, France, Turkey | 34.50 | 5.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Duck and Cover COUP Syria | 33.80 | 4.00 | 30.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5 |
| 5 | Duck and Cover COUP Lebanon | 22.20 | 4.00 | 18.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], Independent Reds[22], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, Japan, North Korea, Thailand | 65.75 | 5.00 | 81.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | East European Unrest INFLUENCE East Germany, Japan, North Korea, Thailand | 65.75 | 5.00 | 81.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Independent Reds INFLUENCE East Germany, North Korea, Thailand | 51.75 | 5.00 | 63.05 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Special Relationship INFLUENCE East Germany, North Korea, Thailand | 51.75 | 5.00 | 63.05 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | Truman Doctrine INFLUENCE North Korea, Thailand | 35.85 | 5.00 | 43.00 | 0.00 | -12.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Italy, Pakistan, Iraq | 32.25 | 5.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | De-Stalinization INFLUENCE Italy, Pakistan, Iraq | 32.25 | 5.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Korean War INFLUENCE Italy, Pakistan | 20.10 | 5.00 | 33.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Decolonization INFLUENCE Italy, Pakistan | 20.10 | 5.00 | 33.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Suez Crisis COUP Syria | 14.00 | 4.00 | 30.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Independent Reds[22], East European Unrest[29], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, South Korea, Iraq, Thailand | 64.50 | 5.00 | 79.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Independent Reds INFLUENCE West Germany, Iraq, Thailand | 51.10 | 5.00 | 62.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Special Relationship INFLUENCE West Germany, Iraq, Thailand | 51.10 | 5.00 | 62.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Truman Doctrine INFLUENCE Iraq, Thailand | 37.60 | 5.00 | 44.75 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, West Germany, Pakistan | 41.93 | 5.00 | 60.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, control_break:West Germany, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Korean War INFLUENCE West Germany, Pakistan | 26.63 | 5.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Decolonization INFLUENCE West Germany, Pakistan | 26.63 | 5.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | De-Stalinization COUP Syria | 14.33 | 4.00 | 30.78 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Korean War COUP Syria | 12.98 | 4.00 | 25.28 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Independent Reds[22], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Italy, Israel, Thailand | 42.50 | 5.00 | 53.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE Italy, Israel, Thailand | 42.50 | 5.00 | 53.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Truman Doctrine INFLUENCE Israel, Thailand | 30.20 | 5.00 | 37.35 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Italy, India | 18.70 | 5.00 | 37.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:India:15.55, access_touch:India, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Decolonization INFLUENCE Italy, India | 18.70 | 5.00 | 37.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:India:15.55, access_touch:India, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Korean War COUP Syria | 13.65 | 4.00 | 25.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Decolonization COUP Syria | 13.65 | 4.00 | 25.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Blockade COUP Syria | 12.30 | 4.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Saudi Arabia, Philippines, Thailand | 41.90 | 5.00 | 53.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Philippines, Thailand | 29.75 | 5.00 | 36.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Special Relationship COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Blockade COUP Saudi Arabia | 14.65 | 4.00 | 22.80 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, offside_ops_penalty |
| 3 | Blockade COUP Syria | 14.30 | 4.00 | 22.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Decolonization INFLUENCE Saudi Arabia, Philippines | 13.45 | 5.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 5 | Decolonization COUP Saudi Arabia | 10.50 | 4.00 | 22.80 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Arab-Israeli War[13], COMECON[14], Nasser[15], Marshall Plan[23], Containment[25], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], CIA Created[26], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `COMECON [14] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Arab-Israeli War[13], COMECON[14], Nasser[15], Marshall Plan[23], Containment[25], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Indonesia | 54.98 | 4.00 | 51.43 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:4.5 |
| 2 | COMECON INFLUENCE Japan, Indonesia, Thailand | 54.33 | 5.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Fidel COUP Indonesia | 49.63 | 4.00 | 45.93 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Indonesia | 49.63 | 4.00 | 45.93 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 5 | Marshall Plan INFLUENCE Japan, Egypt, Indonesia, Thailand | 45.88 | 5.00 | 68.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], CIA Created[26], Nuclear Test Ban[34], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Japan, Saudi Arabia, Panama, Philippines | 69.83 | 5.00 | 68.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 2 | NORAD INFLUENCE Saudi Arabia, Panama, Philippines | 53.83 | 5.00 | 51.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Panama:11.20, control_break:Panama, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 3 | Indo-Pakistani War INFLUENCE Saudi Arabia, Philippines | 37.78 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 4 | Formosan Resolution INFLUENCE Saudi Arabia, Philippines | 37.78 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 5 | Nuclear Test Ban COUP Lebanon | 29.08 | 4.00 | 25.68 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:5.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Nasser[15], Marshall Plan[23], Containment[25], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, Egypt, Iran, Thailand | 48.40 | 5.00 | 68.00 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Fidel INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Arab-Israeli War INFLUENCE Japan, Thailand | 41.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Containment INFLUENCE Japan, Egypt, Thailand | 36.85 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Fidel COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], CIA Created[26], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Iran, Indonesia | 52.05 | 5.00 | 50.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:3.20 |
| 2 | Indo-Pakistani War INFLUENCE Japan, Iran | 36.35 | 5.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, control_break:Iran, non_coup_milops_penalty:3.20 |
| 3 | Formosan Resolution INFLUENCE Japan, Iran | 36.35 | 5.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, control_break:Iran, non_coup_milops_penalty:3.20 |
| 4 | NORAD COUP Lebanon | 24.00 | 4.00 | 20.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:4.5 |
| 5 | NORAD COUP SE African States | 21.75 | 4.00 | 18.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china`
- hand: `Fidel[8], Arab-Israeli War[13], Nasser[15], Containment[25], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Egypt, Thailand | 43.85 | 5.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Thailand:20.45 |
| 2 | Arab-Israeli War INFLUENCE Egypt, Thailand | 43.85 | 5.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Thailand:20.45 |
| 3 | Containment INFLUENCE Pakistan, Egypt, Thailand | 40.65 | 5.00 | 56.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Egypt:13.70, control_break:Egypt, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Fidel COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |
| 5 | Arab-Israeli War COUP Syria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], CIA Created[26], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Egypt | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Formosan Resolution COUP Egypt | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Indo-Pakistani War INFLUENCE Japan, Egypt | 32.55 | 5.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:4.00 |
| 4 | Formosan Resolution INFLUENCE Japan, Egypt | 32.55 | 5.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:4.00 |
| 5 | CIA Created COUP Egypt | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 23: T2 AR4 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china`
- hand: `Arab-Israeli War[13], Nasser[15], Containment[25], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Pakistan, Thailand | 42.10 | 5.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45 |
| 2 | Containment INFLUENCE Japan, Pakistan, Thailand | 38.10 | 5.00 | 53.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | UN Intervention INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 5 | Containment SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `none`
- hand: `Romanian Abdication[12], CIA Created[26], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Pakistan | 40.80 | 5.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan |
| 2 | CIA Created INFLUENCE Pakistan | 24.80 | 5.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan |
| 3 | The Cambridge Five INFLUENCE Japan, Pakistan | 24.80 | 5.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, offside_ops_penalty |
| 4 | Formosan Resolution COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |
| 5 | Formosan Resolution COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Containment[25], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE India, Japan, Thailand | 38.70 | 5.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | UN Intervention INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Containment SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Nasser REALIGN Cuba | 3.34 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `none`
- hand: `Romanian Abdication[12], CIA Created[26], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Japan | 21.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | The Cambridge Five INFLUENCE Japan, Libya | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | CIA Created COUP SE African States | 7.45 | 4.00 | 3.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Nasser REALIGN Cuba | 3.34 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window |
| 4 | UN Intervention REALIGN Cuba | 3.34 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window |
| 5 | Nasser EVENT | 2.35 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Libya | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | The Cambridge Five COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Sudan | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], Olympic Games[20], Independent Reds[22], Marshall Plan[23], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Blockade[10], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Red Scare/Purge[31], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], De Gaulle Leads France[17], Olympic Games[20], Independent Reds[22], Marshall Plan[23], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Egypt | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | De Gaulle Leads France INFLUENCE Japan, Thailand | 37.15 | 5.00 | 36.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | De Gaulle Leads France COUP Syria | 37.00 | 4.00 | 33.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | Olympic Games COUP Egypt | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | The Cambridge Five COUP Egypt | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 32: T3 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Blockade[10], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, Japan, Libya | 52.45 | 5.00 | 51.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 2 | Indo-Pakistani War INFLUENCE East Germany, Libya | 36.45 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 3 | Formosan Resolution INFLUENCE East Germany, Libya | 36.45 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 4 | Socialist Governments INFLUENCE East Germany, Japan, Libya | 32.45 | 5.00 | 51.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Five Year Plan COUP SE African States | 23.15 | 4.00 | 19.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Romanian Abdication[12], Olympic Games[20], Independent Reds[22], Marshall Plan[23], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, Egypt, Thailand | 32.70 | 5.00 | 52.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Olympic Games INFLUENCE Thailand | 25.15 | 5.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE Thailand | 25.15 | 5.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 5 | Marshall Plan SPACE | 9.40 | 1.00 | 3.00 | 0.00 | 6.00 | -0.60 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Blockade[10], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan, Egypt | 31.75 | 5.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:4.80 |
| 2 | Formosan Resolution INFLUENCE Japan, Egypt | 31.75 | 5.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:4.80 |
| 3 | Socialist Governments INFLUENCE West Germany, Japan, Egypt | 27.25 | 5.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Indo-Pakistani War COUP SE African States | 17.20 | 4.00 | 13.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | Indo-Pakistani War COUP Zimbabwe | 17.20 | 4.00 | 13.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Olympic Games[20], Independent Reds[22], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Olympic Games INFLUENCE Thailand | 25.15 | 5.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE Thailand | 25.15 | 5.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 4 | Olympic Games COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |
| 5 | The Cambridge Five COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Blockade[10], Nasser[15], Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Japan | 30.50 | 5.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 2 | Socialist Governments INFLUENCE West Germany, India, Japan | 25.90 | 5.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Formosan Resolution COUP SE African States | 17.80 | 4.00 | 14.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Formosan Resolution COUP Sudan | 17.80 | 4.00 | 14.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Formosan Resolution COUP Zimbabwe | 17.80 | 4.00 | 14.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china`
- hand: `Olympic Games[20], Independent Reds[22], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Thailand | 25.15 | 5.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 2 | The Cambridge Five INFLUENCE Thailand | 25.15 | 5.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 3 | Olympic Games COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |
| 5 | Independent Reds INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Blockade[10], Nasser[15], Truman Doctrine[19]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, India, Japan | 23.90 | 5.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Truman Doctrine INFLUENCE Japan | 13.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:8.00 |
| 3 | Truman Doctrine COUP SE African States | 12.45 | 4.00 | 8.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP Sudan | 12.45 | 4.00 | 8.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Zimbabwe | 12.45 | 4.00 | 8.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Independent Reds[22], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Thailand | 25.15 | 5.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 2 | The Cambridge Five COUP Sudan | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5 |
| 3 | Independent Reds INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Special Relationship INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP SE African States | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Truman Doctrine COUP Sudan | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Truman Doctrine COUP Zimbabwe | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP Colombia | 13.95 | 4.00 | 10.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Botswana | 4.05 | 4.00 | 0.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Botswana, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Independent Reds[22], Special Relationship[37]`
- state: `VP 0, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE Thailand | 9.15 | 5.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Independent Reds COUP Sudan | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Mozambique | 4.45 | 4.00 | 12.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Blockade COUP SE African States | 4.45 | 4.00 | 12.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Blockade COUP Sudan | 4.45 | 4.00 | 12.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Blockade COUP Zimbabwe | 4.45 | 4.00 | 12.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP Mozambique | 4.45 | 4.00 | 12.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-3/A-1`

## Step 43: T4 AR0 USSR

- chosen: `Indo-Pakistani War [24] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Marshall Plan[23], Indo-Pakistani War[24], Formosan Resolution[35], Kitchen Debates[51], Allende[57], Ask Not What Your Country Can Do For You[78], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Allende EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Five Year Plan[5], Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], South African Unrest[56], OAS Founded[71], Sadat Expels Soviets[73], Alliance for Progress[79]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Marshall Plan[23], Formosan Resolution[35], Allende[57], Ask Not What Your Country Can Do For You[78], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE UK, West Germany, Mexico, Algeria | 41.28 | 5.00 | 65.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | One Small Step INFLUENCE Mexico, Algeria | 33.28 | 5.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 3 | Colonial Rear Guards INFLUENCE Mexico, Algeria | 33.28 | 5.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 4 | One Small Step COUP Libya | 32.94 | 4.00 | 29.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Colonial Rear Guards COUP Libya | 32.94 | 4.00 | 29.24 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], South African Unrest[56], OAS Founded[71], Sadat Expels Soviets[73], Alliance for Progress[79]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE UK, Mexico, Angola | 58.68 | 5.00 | 58.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 2 | Alliance for Progress INFLUENCE UK, Mexico, Angola | 58.68 | 5.00 | 58.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 3 | Independent Reds INFLUENCE UK, Angola | 41.88 | 5.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 4 | Sadat Expels Soviets COUP Mexico | 41.04 | 4.00 | 37.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Alliance for Progress COUP Mexico | 41.04 | 4.00 | 37.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Formosan Resolution[35], Allende[57], Ask Not What Your Country Can Do For You[78], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Algeria, Morocco | 35.37 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 2 | Colonial Rear Guards INFLUENCE Algeria, Morocco | 35.37 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 3 | One Small Step COUP Libya | 33.32 | 4.00 | 29.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Colonial Rear Guards COUP Libya | 33.32 | 4.00 | 29.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Algeria, Morocco | 31.37 | 5.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], South African Unrest[56], OAS Founded[71], Alliance for Progress[79]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE Algeria, Congo/Zaire, South Africa | 48.42 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 2 | Alliance for Progress COUP Algeria | 40.67 | 4.00 | 37.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Alliance for Progress COUP Mexico | 34.42 | 4.00 | 30.87 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5 |
| 4 | Independent Reds COUP Algeria | 34.32 | 4.00 | 30.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Alliance for Progress COUP Egypt | 32.67 | 4.00 | 29.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Formosan Resolution[35], Allende[57], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Libya | 33.85 | 4.00 | 30.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, Algeria | 33.65 | 5.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 3 | Colonial Rear Guards COUP Syria | 31.35 | 4.00 | 27.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:1.5 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Algeria | 29.05 | 5.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Colonial Rear Guards COUP Mexico | 28.60 | 4.00 | 24.90 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 50: T4 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], South African Unrest[56], OAS Founded[71]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Congo/Zaire, South Africa | 39.30 | 5.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:6.40 |
| 2 | Korean War INFLUENCE Congo/Zaire, South Africa | 23.30 | 5.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | South African Unrest INFLUENCE Congo/Zaire, South Africa | 23.30 | 5.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Independent Reds COUP Colombia | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 5 | Independent Reds COUP Cameroon | 20.75 | 4.00 | 17.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Formosan Resolution[35], Allende[57], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Algeria | 31.45 | 5.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Allende INFLUENCE Algeria | 20.05 | 5.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.00 |
| 3 | Formosan Resolution INFLUENCE West Germany, Algeria | 20.05 | 5.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Allende COUP Saharan States | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Sudan | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Captured Nazi Scientist[18], South African Unrest[56], OAS Founded[71]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Libya, Morocco | 15.70 | 5.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | South African Unrest INFLUENCE Libya, Morocco | 15.70 | 5.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Captured Nazi Scientist COUP Colombia | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP Mozambique | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Allende [57] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Formosan Resolution[35], Allende[57]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE West Germany | 15.67 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 15.07 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Allende COUP Saharan States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende COUP Sudan | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Guatemala | 12.62 | 4.00 | 8.77 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:4`
- hand: `Captured Nazi Scientist[18], South African Unrest[56], OAS Founded[71]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Cameroon | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Mozambique | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Saharan States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP SE African States | 16.53 | 4.00 | 12.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 55: T4 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | 6.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Formosan Resolution COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Guatemala | 4.30 | 4.00 | 16.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Tunisia | -4.85 | 4.00 | 7.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:3`
- hand: `South African Unrest[56], OAS Founded[71]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | OAS Founded COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | OAS Founded COUP Mozambique | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP SE African States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 US

- chosen: `South African Unrest [56] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `South African Unrest[56]`
- state: `VP 0, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Colombia | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | South African Unrest COUP Cameroon | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | South African Unrest COUP Mozambique | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Saharan States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP SE African States | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-1`

## Step 58: T5 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Blockade[10], Romanian Abdication[12], Nasser[15], Containment[25], Suez Crisis[28], Red Scare/Purge[31], UN Intervention[32], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 59: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Nasser[15], Independent Reds[22], CIA Created[26], Red Scare/Purge[31], Formosan Resolution[35], SALT Negotiations[46], Missile Envy[52], Grain Sales to Soviets[68], Che[83]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR1 USSR

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Blockade[10], Romanian Abdication[12], Nasser[15], Containment[25], Suez Crisis[28], UN Intervention[32], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Libya | 39.86 | 4.00 | 36.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | Suez Crisis COUP Syria | 37.36 | 4.00 | 33.81 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 3 | Suez Crisis COUP Mexico | 34.61 | 4.00 | 31.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 4 | Suez Crisis COUP Algeria | 33.86 | 4.00 | 30.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 5 | Suez Crisis COUP Egypt | 32.86 | 4.00 | 29.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 61: T5 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Nasser[15], Independent Reds[22], CIA Created[26], Formosan Resolution[35], SALT Negotiations[46], Missile Envy[52], Grain Sales to Soviets[68], Che[83]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE Libya, South Africa | 33.84 | 5.00 | 35.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | SALT Negotiations COUP Colombia | 26.76 | 4.00 | 23.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, empty_coup_penalty, expected_swing:4.5 |
| 3 | SALT Negotiations COUP Cameroon | 26.76 | 4.00 | 23.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.71, empty_coup_penalty, expected_swing:4.5 |
| 4 | SALT Negotiations COUP Mozambique | 26.76 | 4.00 | 23.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:0.71, empty_coup_penalty, expected_swing:4.5 |
| 5 | SALT Negotiations COUP Saharan States | 26.76 | 4.00 | 23.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR2 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Blockade[10], Romanian Abdication[12], Nasser[15], Containment[25], UN Intervention[32], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | 18.33 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.67 |
| 2 | Romanian Abdication INFLUENCE West Germany | 18.33 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.67 |
| 3 | Nasser INFLUENCE West Germany | 18.33 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.67 |
| 4 | UN Intervention INFLUENCE West Germany | 18.33 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.67 |
| 5 | Lone Gunman INFLUENCE West Germany | 18.33 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:5`
- hand: `Nasser[15], Independent Reds[22], CIA Created[26], Formosan Resolution[35], Missile Envy[52], Grain Sales to Soviets[68], Che[83]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Colombia | 20.88 | 4.00 | 17.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 2 | Independent Reds COUP Cameroon | 20.88 | 4.00 | 17.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 3 | Independent Reds COUP Mozambique | 20.88 | 4.00 | 17.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 4 | Independent Reds COUP Saharan States | 20.88 | 4.00 | 17.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |
| 5 | Independent Reds COUP SE African States | 20.88 | 4.00 | 17.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:0.83, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 64: T5 AR3 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Romanian Abdication[12], Nasser[15], Containment[25], UN Intervention[32], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | 17.80 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.20 |
| 2 | Nasser INFLUENCE West Germany | 17.80 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.20 |
| 3 | UN Intervention INFLUENCE West Germany | 17.80 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.20 |
| 4 | Lone Gunman INFLUENCE West Germany | 17.80 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.20 |
| 5 | Duck and Cover INFLUENCE East Germany, West Germany | 13.05 | 5.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], CIA Created[26], Formosan Resolution[35], Missile Envy[52], Grain Sales to Soviets[68], Che[83]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Colombia | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 2 | Formosan Resolution COUP Cameroon | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 3 | Formosan Resolution COUP Mozambique | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 4 | Formosan Resolution COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |
| 5 | Formosan Resolution COUP SE African States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.60, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR4 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Nasser[15], Containment[25], UN Intervention[32], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE West Germany | 17.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 2 | UN Intervention INFLUENCE West Germany | 17.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 3 | Lone Gunman INFLUENCE West Germany | 17.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 4 | Nasser COUP Saharan States | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nasser COUP Sudan | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 US

- chosen: `Missile Envy [52] as COUP`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], CIA Created[26], Missile Envy[52], Grain Sales to Soviets[68], Che[83]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Colombia | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 2 | Missile Envy COUP Cameroon | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 3 | Missile Envy COUP Mozambique | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Missile Envy COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Missile Envy COUP SE African States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR5 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Containment[25], UN Intervention[32], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | 15.67 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 2 | Lone Gunman INFLUENCE West Germany | 15.67 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 3 | UN Intervention COUP Saharan States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Sudan | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP Saharan States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], CIA Created[26], Grain Sales to Soviets[68], Che[83]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Colombia | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Cameroon | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Grain Sales to Soviets COUP Mozambique | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Grain Sales to Soviets COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR6 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Containment[25], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Lone Gunman COUP Sudan | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Lone Gunman COUP Guatemala | 13.95 | 4.00 | 10.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman INFLUENCE West Germany | 7.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 5 | Duck and Cover COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], CIA Created[26], Che[83]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Che COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Nasser COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR7 USSR

- chosen: `Duck and Cover [4] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Containment[25]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Containment COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Duck and Cover COUP Sudan | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Containment COUP Sudan | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Duck and Cover COUP Guatemala | 9.65 | 4.00 | 26.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 US

- chosen: `Che [83] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Che[83]`
- state: `VP 0, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Nasser COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Che COUP Colombia | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Che COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Che COUP Mozambique | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 74: T6 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Blockade[10], Olympic Games[20], Brush War[39], We Will Bury You[53], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 75: T6 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Nuclear Test Ban[34], Cuban Missile Crisis[43], Quagmire[45], Bear Trap[47], Junta[50], Cultural Revolution[61], Latin American Death Squads[70], Ussuri River Skirmish[77]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 76: T6 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Blockade[10], Olympic Games[20], Brush War[39], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Saharan States | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Socialist Governments COUP Indonesia | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:4.5 |
| 3 | Brush War COUP Saharan States | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 4 | Brush War COUP Indonesia | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:4.5 |
| 5 | Socialist Governments COUP Libya | 46.43 | 4.00 | 42.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 77: T6 AR1 US

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `milops_shortfall:6`
- hand: `Fidel[8], Cuban Missile Crisis[43], Quagmire[45], Bear Trap[47], Junta[50], Cultural Revolution[61], Latin American Death Squads[70], Ussuri River Skirmish[77]`
- state: `VP 2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Saharan States | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Cuban Missile Crisis COUP Indonesia | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:4.5 |
| 3 | Bear Trap COUP Saharan States | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 4 | Bear Trap COUP Indonesia | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:4.5 |
| 5 | Ussuri River Skirmish COUP Saharan States | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 78: T6 AR2 USSR

- chosen: `Brush War [39] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Olympic Games[20], Brush War[39], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 4, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | Brush War COUP Indonesia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 3 | Brush War INFLUENCE East Germany, France, West Germany | 47.80 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 4 | Brush War COUP Libya | 45.00 | 4.00 | 41.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Quagmire[45], Bear Trap[47], Junta[50], Cultural Revolution[61], Latin American Death Squads[70], Ussuri River Skirmish[77]`
- state: `VP 2, DEFCON 4, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE Brazil, Venezuela, South Africa | 49.75 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | Ussuri River Skirmish INFLUENCE Brazil, Venezuela, South Africa | 49.75 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 3 | Bear Trap COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 4 | Bear Trap COUP Indonesia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 5 | Ussuri River Skirmish COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR3 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Olympic Games[20], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 4, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:3.5 |
| 2 | Portuguese Empire Crumbles COUP Indonesia | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:3.5 |
| 3 | Olympic Games COUP Libya | 39.05 | 4.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |
| 4 | Portuguese Empire Crumbles COUP Libya | 39.05 | 4.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |
| 5 | Olympic Games INFLUENCE West Germany, Nigeria | 36.65 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 81: T6 AR3 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Quagmire[45], Junta[50], Cultural Revolution[61], Latin American Death Squads[70], Ussuri River Skirmish[77]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE Argentina, Brazil, Venezuela | 56.35 | 5.00 | 56.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:4.80 |
| 2 | Ussuri River Skirmish COUP Saharan States | 48.30 | 4.00 | 44.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5 |
| 3 | Junta COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 5 | Junta INFLUENCE Brazil, Venezuela | 38.30 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR4 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, Nigeria | 35.45 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.00 |
| 2 | Portuguese Empire Crumbles COUP Libya | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Portuguese Empire Crumbles COUP Syria | 31.15 | 4.00 | 27.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:1.5 |
| 4 | Portuguese Empire Crumbles COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |
| 5 | Portuguese Empire Crumbles COUP Algeria | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Quagmire[45], Junta[50], Cultural Revolution[61], Latin American Death Squads[70]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 3 | Junta INFLUENCE Argentina, Chile | 38.70 | 5.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:6.00 |
| 4 | Latin American Death Squads INFLUENCE Argentina, Chile | 38.70 | 5.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:6.00 |
| 5 | Quagmire INFLUENCE Argentina, Chile, South Africa | 35.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR5 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Blockade COUP Libya | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Lonely Hearts Club Band COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Blockade COUP Syria | 25.80 | 4.00 | 21.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 5 | Blockade COUP Mexico | 23.05 | 4.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Quagmire[45], Cultural Revolution[61], Latin American Death Squads[70]`
- state: `VP 2, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Nigeria | 46.05 | 4.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads INFLUENCE Argentina, Chile | 36.70 | 5.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:8.00 |
| 3 | Quagmire INFLUENCE Argentina, Chile, South Africa | 33.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Cultural Revolution INFLUENCE Argentina, Chile, South Africa | 33.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Quagmire COUP Nigeria | 32.40 | 4.00 | 48.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 86: T6 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Lonely Hearts Club Band COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 4.40 | 5.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 5 | Lonely Hearts Club Band COUP Tunisia | -2.85 | 4.00 | 9.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], Quagmire[45], Cultural Revolution[61]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE Argentina, Chile, South Africa | 20.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | Cultural Revolution INFLUENCE Argentina, Chile, South Africa | 20.35 | 5.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 3 | Quagmire COUP Colombia | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Mozambique | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR7 US

- chosen: `Cultural Revolution [61] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], Cultural Revolution[61]`
- state: `VP 2, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Colombia | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Cultural Revolution COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Cultural Revolution COUP Mozambique | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Cultural Revolution COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Cultural Revolution COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 89: T7 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `De-Stalinization[33], The Cambridge Five[36], Special Relationship[37], Summit[48], ABM Treaty[60], Camp David Accords[66], Puppet Governments[67], John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Special Relationship EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T7 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], The Cambridge Five[36], NORAD[38], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Willy Brandt[58], Shuttle Diplomacy[74], Liberation Theology[76]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Brezhnev Doctrine EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 91: T7 AR1 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `De-Stalinization[33], The Cambridge Five[36], Special Relationship[37], Summit[48], Camp David Accords[66], Puppet Governments[67], John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 48.80 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 2 | Summit INFLUENCE East Germany, France, West Germany | 48.80 | 5.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 3 | De-Stalinization COUP Libya | 47.00 | 4.00 | 43.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Summit COUP Libya | 47.00 | 4.00 | 43.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | De-Stalinization COUP Mexico | 41.75 | 4.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR1 US

- chosen: `Shuttle Diplomacy [74] as COUP`
- flags: `milops_shortfall:7`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], The Cambridge Five[36], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Willy Brandt[58], Shuttle Diplomacy[74], Liberation Theology[76]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy COUP Indonesia | 56.90 | 4.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | How I Learned to Stop Worrying COUP Indonesia | 50.55 | 4.00 | 46.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Shuttle Diplomacy INFLUENCE Iran, Chile, South Africa | 48.35 | 5.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | Shuttle Diplomacy COUP Pakistan | 47.00 | 4.00 | 43.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Pakistan, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Shuttle Diplomacy COUP Mexico | 41.75 | 4.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 93: T7 AR2 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `The Cambridge Five[36], Special Relationship[37], Summit[48], Camp David Accords[66], Puppet Governments[67], John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 42.47 | 5.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 2 | Summit COUP Libya | 41.67 | 4.00 | 38.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Summit COUP Syria | 39.17 | 4.00 | 35.62 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:2.5 |
| 4 | Summit COUP Mexico | 36.42 | 4.00 | 32.87 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |
| 5 | Summit COUP Algeria | 35.67 | 4.00 | 32.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR2 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], The Cambridge Five[36], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE Iran, Chile | 34.37 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Chile:16.80, non_coup_milops_penalty:5.33 |
| 2 | De Gaulle Leads France INFLUENCE Iran, Chile, South Africa | 31.02 | 5.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Brezhnev Doctrine INFLUENCE Iran, Chile, South Africa | 31.02 | 5.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.20, control_break:Iran, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | How I Learned to Stop Worrying COUP Mexico | 28.07 | 4.00 | 24.37 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | How I Learned to Stop Worrying COUP Algeria | 27.32 | 4.00 | 23.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR3 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `The Cambridge Five[36], Special Relationship[37], Camp David Accords[66], Puppet Governments[67], John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Libya | 36.25 | 4.00 | 32.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | The Cambridge Five COUP Syria | 33.75 | 4.00 | 30.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:1.5 |
| 3 | The Cambridge Five COUP Mexico | 31.00 | 4.00 | 27.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 4 | The Cambridge Five COUP Algeria | 30.25 | 4.00 | 26.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, expected_swing:1.5 |
| 5 | The Cambridge Five INFLUENCE France, West Germany | 30.20 | 5.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 96: T7 AR3 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], The Cambridge Five[36], Brezhnev Doctrine[54], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Argentina, Chile, South Africa | 32.95 | 5.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 2 | Brezhnev Doctrine INFLUENCE Argentina, Chile, South Africa | 32.95 | 5.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Arab-Israeli War INFLUENCE Chile, South Africa | 20.90 | 5.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | The Cambridge Five INFLUENCE Chile, South Africa | 20.90 | 5.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Willy Brandt INFLUENCE Chile, South Africa | 20.90 | 5.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR4 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Special Relationship[37], Camp David Accords[66], Puppet Governments[67], John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE France, West Germany | 15.40 | 5.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Camp David Accords INFLUENCE France, West Germany | 15.40 | 5.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Puppet Governments INFLUENCE France, West Germany | 15.40 | 5.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | John Paul II Elected Pope INFLUENCE France, West Germany | 15.40 | 5.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Special Relationship COUP Saharan States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR4 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Arab-Israeli War[13], The Cambridge Five[36], Brezhnev Doctrine[54], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE Argentina, Chile, South Africa | 26.35 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Arab-Israeli War INFLUENCE Chile, South Africa | 14.30 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | The Cambridge Five INFLUENCE Chile, South Africa | 14.30 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Willy Brandt INFLUENCE Chile, South Africa | 14.30 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Liberation Theology INFLUENCE Chile, South Africa | 14.30 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR5 USSR

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Camp David Accords[66], Puppet Governments[67], John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 8.22 | 4.00 | 20.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Camp David Accords COUP Sudan | 8.22 | 4.00 | 20.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Saharan States | 8.22 | 4.00 | 20.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Sudan | 8.22 | 4.00 | 20.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope COUP Saharan States | 8.22 | 4.00 | 20.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR5 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Arab-Israeli War[13], The Cambridge Five[36], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Saharan States | 28.88 | 4.00 | 41.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Saharan States | 28.88 | 4.00 | 41.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Saharan States | 28.88 | 4.00 | 41.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Saharan States | 28.88 | 4.00 | 41.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War INFLUENCE Chile, South Africa | 11.63 | 5.00 | 33.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR6 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Puppet Governments[67], John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Puppet Governments COUP Sudan | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP Sudan | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Guatemala | 10.30 | 4.00 | 22.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR6 US

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `The Cambridge Five[36], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Colombia | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Cameroon | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `John Paul II Elected Pope[69], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Saharan States | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP Sudan | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope COUP Guatemala | 20.30 | 4.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Saharan States | 19.20 | 4.00 | 27.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Panama Canal Returned COUP Sudan | 19.20 | 4.00 | 27.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR7 US

- chosen: `Willy Brandt [58] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Willy Brandt[58], Liberation Theology[76]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Saharan States | 39.55 | 4.00 | 51.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Liberation Theology COUP Saharan States | 39.55 | 4.00 | 51.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Colombia | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Willy Brandt COUP Cameroon | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Mozambique | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 105: T8 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], UN Intervention[32], Cuban Missile Crisis[43], Cultural Revolution[61], Grain Sales to Soviets[68], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T8 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Marshall Plan[23], Nuclear Test Ban[34], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], South African Unrest[56], U2 Incident[63], Shuttle Diplomacy[74], The Reformer[90]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 107: T8 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Fidel[8], Blockade[10], UN Intervention[32], Cuban Missile Crisis[43], Cultural Revolution[61], Grain Sales to Soviets[68], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Nigeria | 49.21 | 5.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:9.14 |
| 2 | Cultural Revolution INFLUENCE East Germany, West Germany, Nigeria | 49.21 | 5.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:9.14 |
| 3 | Cuban Missile Crisis COUP Libya | 41.32 | 4.00 | 37.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Cultural Revolution COUP Libya | 41.32 | 4.00 | 37.77 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Cuban Missile Crisis COUP Syria | 38.82 | 4.00 | 35.27 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Nuclear Test Ban[34], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], South African Unrest[56], U2 Incident[63], Shuttle Diplomacy[74], The Reformer[90]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE East Germany, France, Poland, West Germany | 61.06 | 5.00 | 65.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Nuclear Test Ban COUP Saharan States | 56.82 | 4.00 | 53.42 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:5.5 |
| 3 | Shuttle Diplomacy COUP Saharan States | 50.47 | 4.00 | 46.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 44.91 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | How I Learned to Stop Worrying COUP Saharan States | 44.12 | 4.00 | 40.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Fidel[8], Blockade[10], UN Intervention[32], Cultural Revolution[61], Grain Sales to Soviets[68], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 48.38 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Cultural Revolution COUP Libya | 42.08 | 4.00 | 38.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Cultural Revolution COUP Syria | 39.58 | 4.00 | 36.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 4 | Cultural Revolution COUP Algeria | 36.33 | 4.00 | 32.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |
| 5 | Fidel COUP Libya | 35.73 | 4.00 | 32.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR2 US

- chosen: `Shuttle Diplomacy [74] as COUP`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], South African Unrest[56], U2 Incident[63], Shuttle Diplomacy[74], The Reformer[90]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy COUP Saharan States | 51.23 | 4.00 | 47.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:4.5 |
| 2 | How I Learned to Stop Worrying COUP Saharan States | 44.88 | 4.00 | 41.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 43.38 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | Shuttle Diplomacy COUP Algeria | 36.33 | 4.00 | 32.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |
| 5 | Shuttle Diplomacy COUP Mexico | 35.58 | 4.00 | 32.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 111: T8 AR3 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Fidel[8], Blockade[10], UN Intervention[32], Grain Sales to Soviets[68], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 45.95 | 4.00 | 42.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:3.5 |
| 2 | Blockade COUP Saharan States | 39.60 | 4.00 | 35.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Saharan States | 39.60 | 4.00 | 35.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 4 | Fidel COUP Libya | 36.80 | 4.00 | 33.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Fidel COUP Syria | 34.30 | 4.00 | 30.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 112: T8 AR3 US

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `milops_shortfall:5`
- hand: `De Gaulle Leads France[17], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], South African Unrest[56], U2 Incident[63], The Reformer[90]`
- state: `VP 3, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Nigeria | 46.05 | 4.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | De Gaulle Leads France COUP Nigeria | 32.40 | 4.00 | 48.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | U2 Incident COUP Nigeria | 32.40 | 4.00 | 48.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | The Reformer COUP Nigeria | 32.40 | 4.00 | 48.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Nigeria | 30.05 | 4.00 | 42.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 113: T8 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], UN Intervention[32], Grain Sales to Soviets[68], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Grain Sales to Soviets COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Defectors COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR4 US

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `De Gaulle Leads France[17], Portuguese Empire Crumbles[55], South African Unrest[56], U2 Incident[63], The Reformer[90]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | U2 Incident COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | The Reformer COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR5 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], Grain Sales to Soviets[68], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 41.20 | 4.00 | 37.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Grain Sales to Soviets COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Defectors COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | UN Intervention COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR5 US

- chosen: `U2 Incident [63] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56], U2 Incident[63], The Reformer[90]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident COUP Saharan States | 32.57 | 4.00 | 49.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | The Reformer COUP Saharan States | 32.57 | 4.00 | 49.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP Saharan States | 30.22 | 4.00 | 42.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Saharan States | 30.22 | 4.00 | 42.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | U2 Incident INFLUENCE East Germany, France, West Germany | 20.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR6 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Grain Sales to Soviets[68], Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Reagan Bombs Libya COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Defectors COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Reagan Bombs Libya COUP Sudan | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR6 US

- chosen: `The Reformer [90] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56], The Reformer[90]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer COUP Cameroon | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | The Reformer COUP Mozambique | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | The Reformer COUP Saharan States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | The Reformer COUP SE African States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | The Reformer COUP Sudan | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR7 USSR

- chosen: `Reagan Bombs Libya [87] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Reagan Bombs Libya[87], Defectors[108]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya COUP Saharan States | 47.55 | 4.00 | 59.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Defectors COUP Saharan States | 47.55 | 4.00 | 59.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Defectors COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Reagan Bombs Libya COUP Guatemala | 24.80 | 4.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Cameroon | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Portuguese Empire Crumbles COUP Mozambique | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP Saharan States | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP SE African States | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Sudan | 21.55 | 4.00 | 33.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 121: T9 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Socialist Governments[7], Formosan Resolution[35], Cultural Revolution[61], Latin American Death Squads[70], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Shuttle Diplomacy EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T9 AR0 US

- chosen: `Soviets Shoot Down KAL 007 [92] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], Containment[25], Suez Crisis[28], The Cambridge Five[36], Cuban Missile Crisis[43], Summit[48], Puppet Governments[67], Soviets Shoot Down KAL 007[92], Wargames[103]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 123: T9 AR1 USSR

- chosen: `Cultural Revolution [61] as COUP`
- flags: `milops_shortfall:9`
- hand: `Formosan Resolution[35], Cultural Revolution[61], Latin American Death Squads[70], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Saharan States | 51.04 | 4.00 | 47.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Cultural Revolution INFLUENCE East Germany, West Germany, Iraq | 46.01 | 5.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Iraq:13.55, control_break:Iraq, non_coup_milops_penalty:10.29 |
| 3 | Latin American Death Squads COUP Saharan States | 44.69 | 4.00 | 40.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Lone Gunman COUP Saharan States | 38.34 | 4.00 | 34.49 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |
| 5 | Shuttle Diplomacy COUP Saharan States | 31.04 | 4.00 | 47.49 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 124: T9 AR1 US

- chosen: `Wargames [103] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Fidel[8], Containment[25], Suez Crisis[28], The Cambridge Five[36], Cuban Missile Crisis[43], Summit[48], Puppet Governments[67], Wargames[103]`
- state: `VP 1, DEFCON 2, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames INFLUENCE East Germany, France, West Germany, Nigeria | 64.21 | 5.00 | 70.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:10.29 |
| 2 | Wargames COUP Saharan States | 57.39 | 4.00 | 53.99 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:5.5 |
| 3 | Containment COUP Saharan States | 51.04 | 4.00 | 47.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | Cuban Missile Crisis COUP Saharan States | 51.04 | 4.00 | 47.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 5 | Summit COUP Saharan States | 51.04 | 4.00 | 47.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR2 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Formosan Resolution[35], Latin American Death Squads[70], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE France, Algeria | 37.20 | 5.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:8.00 |
| 2 | Shuttle Diplomacy INFLUENCE France, Iraq, Algeria | 35.60 | 5.00 | 59.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:Iraq:13.55, control_break:Iraq, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE France, Iraq, Algeria | 35.60 | 5.00 | 59.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:Iraq:13.55, control_break:Iraq, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | AWACS Sale to Saudis INFLUENCE France, Iraq, Algeria | 35.60 | 5.00 | 59.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:Iraq:13.55, control_break:Iraq, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Latin American Death Squads COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR2 US

- chosen: `Containment [25] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Fidel[8], Containment[25], Suez Crisis[28], The Cambridge Five[36], Cuban Missile Crisis[43], Summit[48], Puppet Governments[67]`
- state: `VP 1, DEFCON 2, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment COUP Saharan States | 51.90 | 4.00 | 48.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:4.5 |
| 2 | Cuban Missile Crisis COUP Saharan States | 51.90 | 4.00 | 48.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:4.5 |
| 3 | Summit COUP Saharan States | 51.90 | 4.00 | 48.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:4.5 |
| 4 | Puppet Governments COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 5 | Containment INFLUENCE East Germany, West Germany, Mexico | 44.20 | 5.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 127: T9 AR3 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `milops_shortfall:6`
- hand: `Formosan Resolution[35], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Saharan States | 38.00 | 4.00 | 34.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 2 | Shuttle Diplomacy COUP Saharan States | 30.70 | 4.00 | 47.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Saharan States | 30.70 | 4.00 | 47.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | AWACS Sale to Saudis COUP Saharan States | 30.70 | 4.00 | 47.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Saharan States | 28.35 | 4.00 | 40.65 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR3 US

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Suez Crisis[28], The Cambridge Five[36], Cuban Missile Crisis[43], Summit[48], Puppet Governments[67]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Mexico | 46.60 | 5.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico, non_coup_milops_penalty:9.60 |
| 2 | Summit INFLUENCE East Germany, West Germany, Mexico | 46.60 | 5.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico, non_coup_milops_penalty:9.60 |
| 3 | Puppet Governments INFLUENCE West Germany, Mexico | 30.45 | 5.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico, non_coup_milops_penalty:9.60 |
| 4 | Cuban Missile Crisis COUP Cameroon | 28.70 | 4.00 | 25.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:4.5 |
| 5 | Cuban Missile Crisis COUP Mozambique | 28.70 | 4.00 | 25.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:1.20, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR4 USSR

- chosen: `Shuttle Diplomacy [74] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Formosan Resolution[35], Nixon Plays the China Card[72], Shuttle Diplomacy[74], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Ask Not What Your Country Can Do For You COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | AWACS Sale to Saudis COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR4 US

- chosen: `Summit [48] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Suez Crisis[28], The Cambridge Five[36], Summit[48], Puppet Governments[67]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Saharan States | 51.90 | 4.00 | 48.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5 |
| 2 | Puppet Governments COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | Summit INFLUENCE East Germany, France, West Germany | 42.05 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Suez Crisis COUP Saharan States | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Summit COUP Cameroon | 29.90 | 4.00 | 26.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR5 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Formosan Resolution[35], Nixon Plays the China Card[72], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Iraq | 20.30 | 5.00 | 51.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Iraq:13.55, control_break:Iraq, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, West Germany, Iraq | 20.30 | 5.00 | 51.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Iraq:13.55, control_break:Iraq, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Ask Not What Your Country Can Do For You COUP Saharan States | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP Sudan | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | AWACS Sale to Saudis COUP Saharan States | 11.90 | 4.00 | 28.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR5 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Fidel[8], Suez Crisis[28], The Cambridge Five[36], Puppet Governments[67]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Suez Crisis COUP Saharan States | 33.90 | 4.00 | 50.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Fidel COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Cameroon | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR6 USSR

- chosen: `AWACS Sale to Saudis [107] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Formosan Resolution[35], Nixon Plays the China Card[72], AWACS Sale to Saudis[107]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis COUP Saharan States | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Formosan Resolution COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | AWACS Sale to Saudis COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | AWACS Sale to Saudis COUP Guatemala | 15.15 | 4.00 | 31.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR6 US

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Fidel[8], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Cameroon | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Suez Crisis COUP Mozambique | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Suez Crisis COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Suez Crisis COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Suez Crisis COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR7 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Formosan Resolution[35], Nixon Plays the China Card[72]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 47.55 | 4.00 | 59.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 47.55 | 4.00 | 59.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Guatemala | 24.80 | 4.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR7 US

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Fidel[8], The Cambridge Five[36]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Cameroon | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Fidel COUP Mozambique | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Fidel COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Fidel COUP SE African States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Fidel COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 137: T10 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Blockade[10], De Gaulle Leads France[17], Brush War[39], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Terrorism[95], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Terrorism EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T10 AR0 US

- chosen: `Summit [48] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Romanian Abdication[12], De-Stalinization[33], Brush War[39], Summit[48], Grain Sales to Soviets[68], Liberation Theology[76], Alliance for Progress[79], Iranian Hostage Crisis[85], Solidarity[104]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Solidarity EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 139: T10 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Blockade[10], Brush War[39], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Terrorism[95], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Brush War COUP Saharan States | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 3 | Brush War COUP Sudan | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 4 | Brush War COUP Guatemala | 28.86 | 4.00 | 25.31 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 5 | Terrorism INFLUENCE East Germany, West Germany | 26.47 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR1 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Romanian Abdication[12], De-Stalinization[33], Brush War[39], Grain Sales to Soviets[68], Liberation Theology[76], Alliance for Progress[79], Iranian Hostage Crisis[85], Solidarity[104]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 42.62 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Alliance for Progress COUP Cameroon | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 3 | Alliance for Progress COUP Mozambique | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 4 | Alliance for Progress COUP Saharan States | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |
| 5 | Alliance for Progress COUP SE African States | 29.61 | 4.00 | 26.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:10, milops_urgency:1.43, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR2 USSR

- chosen: `Terrorism [95] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Blockade[10], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Terrorism[95], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Terrorism INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Terrorism COUP Saharan States | 24.22 | 4.00 | 20.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | Terrorism COUP Sudan | 24.22 | 4.00 | 20.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Saharan States | 24.22 | 4.00 | 20.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR2 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Romanian Abdication[12], De-Stalinization[33], Brush War[39], Grain Sales to Soviets[68], Liberation Theology[76], Iranian Hostage Crisis[85], Solidarity[104]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | Solidarity INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Grain Sales to Soviets COUP Cameroon | 24.22 | 4.00 | 20.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Mozambique | 24.22 | 4.00 | 20.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | Grain Sales to Soviets COUP Saharan States | 24.22 | 4.00 | 20.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR3 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:10`
- hand: `Blockade[10], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Saharan States | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Colonial Rear Guards COUP Sudan | 25.55 | 4.00 | 21.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:10, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Guatemala | 24.80 | 4.00 | 21.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:10, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | Blockade COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 144: T10 AR3 US

- chosen: `Solidarity [104] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Romanian Abdication[12], De-Stalinization[33], Brush War[39], Liberation Theology[76], Iranian Hostage Crisis[85], Solidarity[104]`
- state: `VP -1, DEFCON 2, MilOps U2/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity COUP Saharan States | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | De-Stalinization COUP Saharan States | 33.90 | 4.00 | 50.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Brush War COUP Saharan States | 33.90 | 4.00 | 50.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Iranian Hostage Crisis COUP Saharan States | 33.90 | 4.00 | 50.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Liberation Theology COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 145: T10 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Saharan States | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende COUP Sudan | 19.20 | 4.00 | 15.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade COUP Guatemala | 18.45 | 4.00 | 14.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR4 US

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Romanian Abdication[12], De-Stalinization[33], Brush War[39], Liberation Theology[76], Iranian Hostage Crisis[85]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Saharan States | 33.90 | 4.00 | 50.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Brush War COUP Saharan States | 33.90 | 4.00 | 50.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Iranian Hostage Crisis COUP Saharan States | 33.90 | 4.00 | 50.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Saharan States | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Saharan States | 29.20 | 4.00 | 37.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 147: T10 AR5 USSR

- chosen: `Allende [57] as COUP`
- flags: `milops_shortfall:8`
- hand: `Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Saharan States | 21.87 | 4.00 | 18.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Allende COUP Sudan | 21.87 | 4.00 | 18.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Guatemala | 21.12 | 4.00 | 17.27 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Ask Not What Your Country Can Do For You COUP Saharan States | 14.57 | 4.00 | 31.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP Sudan | 14.57 | 4.00 | 31.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:2.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR5 US

- chosen: `Brush War [39] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], Brush War[39], Liberation Theology[76], Iranian Hostage Crisis[85]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War COUP Saharan States | 35.23 | 4.00 | 51.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Iranian Hostage Crisis COUP Saharan States | 35.23 | 4.00 | 51.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Saharan States | 32.88 | 4.00 | 45.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Saharan States | 30.53 | 4.00 | 38.68 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Brush War INFLUENCE East Germany, France, West Germany | 15.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR6 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as COUP`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You COUP Saharan States | 41.90 | 4.00 | 58.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Lonely Hearts Club Band COUP Saharan States | 39.55 | 4.00 | 51.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Sudan | 19.90 | 4.00 | 36.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP Guatemala | 19.15 | 4.00 | 35.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band COUP Sudan | 17.55 | 4.00 | 29.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 150: T10 AR6 US

- chosen: `Iranian Hostage Crisis [85] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], Liberation Theology[76], Iranian Hostage Crisis[85]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis COUP Saharan States | 39.90 | 4.00 | 56.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Liberation Theology COUP Saharan States | 37.55 | 4.00 | 49.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Saharan States | 35.20 | 4.00 | 43.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Iranian Hostage Crisis COUP Cameroon | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Iranian Hostage Crisis COUP Mozambique | 17.90 | 4.00 | 34.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Saharan States | 51.55 | 4.00 | 63.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Lonely Hearts Club Band COUP Sudan | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Lonely Hearts Club Band COUP Guatemala | 28.80 | 4.00 | 41.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Tunisia | 19.15 | 4.00 | 31.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | -55.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR7 US

- chosen: `Liberation Theology [76] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], Liberation Theology[76]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Saharan States | 51.55 | 4.00 | 63.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Romanian Abdication COUP Saharan States | 49.20 | 4.00 | 57.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Mozambique | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Liberation Theology COUP SE African States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -15, DEFCON +1, MilOps U-3/A-3`
